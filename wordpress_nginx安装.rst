.. image:: http://smallbiztechnology.com/wp-content/uploads/2011/05/wordpress-logo-stacked-rgb.png
   :align: center

技术整理贴, 不感兴趣就跳过吧.

一般来说, wordpress都是和apache一起搭配起来的, 但是我现在的服务器是nginx, 于是我需要把他们搭配起来. 基本采用的方法是根据以下2篇文章的内容:

http://library.linode.com/web-servers/nginx/php-fastcgi/ubuntu-11.04-natty

http://joneslee85.wordpress.com/2010/03/13/howto-nginx-wordpress-ubuntu-shortest-setup/

原理
------------------------

nginx把网站导向到wordpress安装目录, 
对于php文件, 采用fastcgi的方式, 导向到一个php-fastcgi服务器上面处理.

具体安装过程
------------------------
新建一个wordpress nginx配置文件: /etc/nginx/site-avariable/wordpress

里面几个参数需要改: server_name就是你网站的地址, root指向wordpress, fastcgi_param就是下面fastcgi脚本文件.

::

    server{
            listen 80; #or change this to your public IP address eg 1.1.1.1:80
            server_name wordpress; #change this to the domain name, for example www.myblog.com
            access_log /var/log/wordpress.access_log;
            error_log /var/log/wordpress.error_log;
    
            location / {
              root /home/your-user-name/Sites/wordpress;
              index index.php index.html index.htm;
    
              # this serves static files that exist without running other rewrite tests
              if (-f $request_filename) {
                  expires 30d;
                  break;
              }
    
              # this sends all non-existing file or directory requests to index.php
              if (!-e $request_filename) {
                  rewrite ^(.+)$ /index.php?q=$1 last;
              }
            }
    
            location ~ \.php$ {
                fastcgi_pass    127.0.0.1:9000;
                fastcgi_index   index.php;
                fastcgi_param   SCRIPT_FILENAME /home/your-user-name/Sites/wordpress$fastcgi_script_name;
                include         fastcgi_params;
            }
    }

然后重启nginx:

::

    sudo service nginx restart


php fastcgi脚本: php-fastcgi

里面user你随便定, 但是要能够访问和修改wordpress目录, 我是直接用普通用户了(wordpress也是普通用户下载的)

::

    #!/bin/bash
    
    FASTCGI_USER=www-data
    FASTCGI_GROUP=www-data
    ADDRESS=127.0.0.1
    PORT=9000
    PIDFILE=/var/run/php-fastcgi/php-fastcgi.pid
    CHILDREN=6
    PHP5=/usr/bin/php5-cgi
    
    /usr/bin/spawn-fcgi -a $ADDRESS -p $PORT -P $PIDFILE -C $CHILDREN -u $FASTCGI_USER -g $FASTCGI_GROUP -f $PHP5

写好后, 执行这个文件就可以了:

::

    chmod u+x php-fastcgi
    ./php-fastcgi

这样就新建了一个一个php-fastcgi服务器. nginx发现php文件的时候, 就会交由这个服务器处理.


然后你就可以跟着wordpress教程一步步做了: http://codex.wordpress.org/zh-cn:%E5%AE%89%E8%A3%85_WordPress

对了, 里面还有设置mysql服务器的步骤, 基本上按照上面的教程来就行了.
