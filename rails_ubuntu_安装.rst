.. image:: http://tech.chitgoks.com/wp-content/uploads/2009/07/ruby_rails.png
   :align: center

安装rvm
---------------------

首先, 安装源里面的ruby, git, curl等依赖 

.. code-block:: bash

    sudo apt-get install ruby git-core curl zlib1g-dev libssl-dev libsqlite3-dev libreadline-dev g++ libxml2-dev libxslt1-dev libmysqlclient-dev autoconf

然后安装rvm (按照 https://rvm.beginrescueend.com/rvm/install/ ) 

.. code-block:: bash

    bash -s stable < <(curl -s https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer)

把环境加到shell path里面 

.. code-block:: bash

    echo '[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm" # Load RVM function' >> ~/.bash_profile

不过我发现bash好像不调用.bash_profile, 所以还是用.bashrc吧 

.. code-block:: bash

    echo '[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm" # Load RVM function' >> ~/.bashrc


重新加载 

.. code-block:: bash

    source .bash_profile

测试rvm是否装好了 

.. code-block:: bash

    type rvm | head -1

安装ruby1.9.3 

.. code-block:: bash

    rvm install 1.9.3

设置默认环境 

.. code-block:: bash

    rvm use 1.9.3 --default

安装rails
-------------------------

gem安装即可

.. code-block:: bash

    gem install rails

mysql设置
-------------------------

rails默认db是sqlite, 为了调试, 也可能整成mysql的, 这里也加上mysql方面的设置方式.

安装mysql 

.. code-block:: bash

  sudo apt-get install mysql-server

mysql默认编码是latin, 我们要改成utf8, 修改/etc/mysql/my.cnf, 

* 在[mysql] 的下面加上 default-character-set=utf8 这一段代码.
* 在[client] 的下面加上 default-character-set=utf8 这一段代码.
* 在 [mysqld] 下面加上 default-character-set=utf8  这一段代码.

设置完后需要重启mysql:

..code-block:: bash

    sudo service mysql restart

然后我们重置mysql root密码 

.. code-block:: bash

    sudo dpkg-reconfigure mysql-server 

进入命令行: mysql -u root -p 

然后在密码提示上面设置一个root密码.

进入命令行后, 我们需要 

.. code-block:: bash

    # 创建一个数据库
    create database test;
    # 建立对应的mysql的用户
    create user tester identified by '密码';
    # 设置权限
    grant all privileges on test.* to tester;

postgresql设置
-------------------------
我们也可以设置采用postgresql。

安装postgresql

.. code-block:: bash

  sudo apt-get install postgresql postgresql-client


进入命令行后, 我们需要加上用户和数据库：

.. code-block:: bash

    sudo -u postgres psql postgres << EOF
    CREATE DATABASE test;                           
    CREATE USER test WITH PASSWORD 'test';          
    GRANT ALL PRIVILEGES ON DATABASE test to test;  
    EOF

好了, 现在东西都已经可以用了, 开始干活吧.


issues
---------------------------------------------
如果sqlite安装出现问题, 需要

.. code-block:: bash

    sudo apt-get install libsqlite3-dev
    gem install sqlite3-ruby
