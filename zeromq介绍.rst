.. image:: http://github.com/imatix/zguide/raw/master/images/fig14.png
   :align: center

什么是zeromq?
----------------------
最近断断续续知道了有message queue这种东西, 可以很好地作为不同程序间的粘合剂. 补上了我工具链上面缺失的一环. 在考虑了几个mq的工具之后, 我决定学习 `zeromq`_ . 为什么选它呢, 因为它的API和它的网站一样简洁优美, 暗合禅道.

zeromq的基础
----------------------
zeromq采用api形式来实现队列功能, 它的核心就是: socket.

这个socket和tcp/ip的socket在概念上有点类似, 只不过, 它的socket不需要给出具体通讯的实现以及其他的一些特性, 我们可以把它理解为更高级的socket. socket处理消息是按照份数来进行的, 每次发送一份或者多份消息. 并且, 这个socket不一定是基于网络的, 它可以设置为其他形式的东西, 比如ipc, 进程内部通讯, 通讯方式和代码是解耦合的.

这样的话, 程序员只需要关心数据流的流动方式, 以及对应的网络拓扑应该如何搭建. 我们还是来看看具体的代码吧.

一个简单的例子
----------------------
如果我们要实现下面这个简单的通讯方式:

client发出'hello'请求, server回应'world'.

.. image:: http://github.com/imatix/zguide/raw/master/images/fig1.png
   :align: center

只需要写这样的代码:

server.py:

.. code-block:: python
    
    # 导入zmq
    import zmq, time
    # 初始化上下文
    context = zmq.Context()
    # 生成一个新的服务socket
    socket = context.socket(zmq.REP)
    # 绑定在一个地址上面
    socket.bind("tcp://*:5555")
    
    while True:
        # 等待客户端发起请求
        message = socket.recv()
        # 做一些'具体的'工作
        time.sleep (1)
        # 返回结果
        socket.send("World")

client.py:

.. code-block:: python

    import zmq
    context = zmq.Context()

    # 生成一个请求socket    
    socket = context.socket(zmq.REQ)
    # 连接上服务器
    socket.connect ("tcp://localhost:5555")
    
    for request in range (1,3):
        # 发出请求
        socket.send ("Hello")
        # 得到回应
        print socket.recv()

分别在2个终端里面执行上面的代码, 你会发现自己实现了一个非常简单的服务器, 而上面的代码正好是他们应该执行的逻辑, 没有任何底层的肮脏处理代码!

神奇的地方:

- 你可以开启任意多个client, 服务器都可以响应得过来.
- 你不需要处理通讯异常的问题, zeromq都帮你实现好了.
- client和server他们启动的顺序是不互相依赖的, 谁都可以先启动.
- 不需要其他程序执行, 消息机制是在程序执行的时候, zeromq自动开线程处理的.

zeromq是搭建复杂拓扑的基石. 除了上面那个简单的同步回应请求模式以外, zeromq还可以实现许许多多更为复杂的模式, 这些是依靠它基础的几类socket完成的:

- REQ 请求socket
- REP 回应socket. 上面利用这2类来实现了一个简单的服务器.
- PUB 发布socket. 该socket可以发布消息, 但是不关心订阅者是否收到消息.
- SUB 订阅socket. 它可以连上PUB, 获取PUB随机发送的消息.
- PUSH 只送出消息.
- PULL 只收取消息.
- PAIR 一对一的管道.
- XREQ 异步请求.
- XREP 异步回应.

利用上面的几类基础socket, 可以实现以下的复杂拓扑: 2个云计算集群, 能够根据负载互相转移任务.

.. image:: http://github.com/imatix/zguide/raw/master/images/fig52.png
   :align: center

具体的实现方法这里就不多说了, 你可以看 `zeromq教程`_, 里面解释得非常详细.

安装方法
----------------------
因为ubuntu源里面的zeromq好像不是最新的, 我是直接上: http://www.zeromq.org/intro:get-the-software 上面下载2.0.10版本的(python绑定最高是2.1.1, 但是没有下载, 于是我选择这个版本).

然后就是解压编译安装. 需要g++以及uuid-dev. 安装完毕后, 需要手动做一下链接库的链接, 不然无法用pyzmq:

:: 

    ln -s /usr/local/lib/libzmq.so.0 /usr/lib/libzmq.so.0 

然后安装pyzmq ::

    sudo easy_install pyzmq==2.0.10

然后就可以执行上面的python代码了.

结论
----------------------
zeromq的抽象方式非常优美, 在此层面上, 我们可以专注处理数据流的问题, 而不需要考虑下面的杂活. 我早就希望能够有这样的工具存在了, 现在得偿所愿, 可以构建一些很有意思的系统了.

.. _`zeromq`: http://www.zeromq.org/

.. _`zeromq教程`: http://zguide.zeromq.org/page:all
