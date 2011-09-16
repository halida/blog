这里整理一下设置mongodb访问权限的资料.

我们有通用的方法, 用iptable严格限制访问ip, 以及mongodb自带的密码验证(key验证等有需求的时候再研究)

iptable限制访问资源
----------------------------------------

服务器完全开放mongodb, 通过iptables来限制访问.

修改/etc/mongo.conf, host为0.0.0.0, 允许外部访问.

设置规则:

.. code-block:: sh

    sudo iptables -I INPUT 1 -p tcp --dport 27017 -s 允许的外部IP -j ACCEPT
    iptables -A INPUT -p tcp --dport 27017 -j DROP

设置完毕后, 安装iptables-persistent 保证重启后iptables还是有效.

mongodb权限管理
-----------------------------------------
有的时候还是需要限制权限, 方法整理如下:

在服务器本地执行 mongo

.. code-block:: sh

    use crawler_db
    db.addUser('admin','admin')

然后修改/etc/mongo.conf, 设置 auth = true
需要重启mongo

连接上的时候, 需要db auth一下:

.. code-block:: sh

    $db.authenticate('admin', 'admin')
