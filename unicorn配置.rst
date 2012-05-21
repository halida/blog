.. image:: http://i.imgur.com/hYztb.png
   :align: center

什么是unicorn?
-------------------------------------
`unicorn <http://unicorn.bogomips.org/>`_ 是ruby下面的一个基于Rack的HTTP server. 类似的工具有 passenger, thin 等。

unicorn简单的使用方式
-------------------------------------
在你的rails项目下面， 直接执行下面的代码就可以了 ::

    unicorn_rails

unicorn的原理
-------------------------------------
它的工作模式是master/worker多进程模式。 简单地说， 首先建立一个master进程， 然后fork出来worker进程。

worker进程处理进来的请求， master负责管控， 当worker消耗内存过多， 或者相应时间太长， 杀掉worker进程。

这里是一篇github使用他们的文档：

https://github.com/blog/517-unicorn


unicorn详细配置
-------------------------------------

一般来说， 按照这个架构方式:

.. image:: http://i.imgur.com/s6dth.png
  :align: center

nginx负责端口映射， 从80端口映射到本地unix socket, 然后unicorn按照daemon方式执行。


设置nginx
`````````````````````````````````````
nginx只需要设置一下端口转发就可以了。 （对于rails， 另外提供静态资源服务）

::

    server
    {
        listen 80;
        server_name doubanmash.com;
        location / {
            proxy_pass http://127.0.0.1:8080;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }

设置unicorn
`````````````````````````````````````
基本摘抄 `上面github的配置 <https://github.com/blog/517-unicorn>`_ ， 
文件保存为./config/unicorn.rb， 稍微解释一下。

.. code-block:: ruby

    # -*- coding: utf-8 -*-
    rails_env = ENV['RAILS_ENV'] || 'production'
    # 需要设置一下rail的路径
    RAILS_ROOT = "/rails/path"
    
    # 设置生产和开发环境下面跑的worker数量
    worker_processes (rails_env == 'production' ? 16 : 4)
    
    # rails环境是需要预先加载的， 节省时间和内存
    preload_app true
    
    # 每个请求最长的响应时间， 超过了就杀掉worker
    timeout 30
    
    # 监听端口设置， 可以设置成unix socket或者tcp， 这里是用tcp, 因为开发环境可以直接看网站
    # listen '/data/github/current/tmp/sockets/unicorn.sock', :backlog => 2048
    listen 8080, backlog: 2048    
    
    before_fork do |server, worker|
      ##
      # 这里是实现重启的时候无缝衔接的代码。
      # 首先unicorn提供了这样一个机制：
      # 当我们发送 USR2 信号给master的时候， unicorn就会把旧的pidfile加上.oldbin后缀，
      # 然后启动一个新的master， 新的master也会fork worker出来。
      #
      # 下面的代码就是当新的master起来的时候， 检查oldbin这个文件， 告诉旧的master退出（发送QUIT信号）。
      # 这样我们保证了无缝重启。
    
      old_pid = RAILS_ROOT + '/tmp/pids/unicorn.pid.oldbin'
      if File.exists?(old_pid) && server.pid != old_pid
        begin
          Process.kill("QUIT", File.read(old_pid).to_i)
        rescue Errno::ENOENT, Errno::ESRCH
          # someone else did our job for us
        end
      end
    end
    
    
    after_fork do |server, worker|
      ##
      # fork了之后， 原先开启的socket就不能用了， 重新开启
      ActiveRecord::Base.establish_connection
      # Redis 和 Memcached 的连接是按需的， 不需要重新开启
    end

信号是外界给unicorn发命令的方式， 我们利用发信号来控制unicorn。
上面的配置中无缝重启的部分利用到了这个机制。 最好看看 `unicorn 信号文档 <http://unicorn.bogomips.org/SIGNALS.html>`_ 。 

更多的配置， 可以见 `unicorn 配置文档 <http://unicorn.bogomips.org/Unicorn/Configurator.html>`_
    
具体使用
`````````````````````````````````````
设置完成后， 在命令行下面执行 ::

    bundle exec unicorn_rails -c ./config/unicorn.rb -D

如果是生产环境 ::

    bundle exec unicorn_rails -c ./config/unicorn.rb -D -E production

当新版本上线， 需要重启的时候， 执行 ::

    kill -USR2 `cat ${RAILS_ROOT}/tmp/pids/unicorn.pid`

如何监控
`````````````````````````````````````
好像有的时候, unicorn master会出现内存泄漏的状况， 还需要一个进程来监控它。 
有人推荐我用 `god <http://godrb.com/>`_ ， 不过我还没有评测过。

性能和易用性
-------------------------------------
没有评测过， 等我有时间的时候考虑一下。

结论
-------------------------------------
听说rails的初学者去用passenger， 熟悉了一些之后会用unicorn， 我对为什么要用它并没有什么太多的感受。
听说应该是它的可配置性， 以及比较好的性能吧。
