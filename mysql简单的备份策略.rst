策略很简单, 就是每天登录到服务器上面, mysqldump下来数据, 压缩, round-robin存放到本地即可(简单的根据星期几来保存).

备份方法
----------------------------------------
执行备份脚本: backup.sh (本项目根目录文件)
然后会按照星期做round-robin备份. 文件名是备份的星期几.

修改了/etc/crontab, 添加每天早晨3:00执行备份:

    0 3 * * * user cd ~/backup && bash backup.sh

backup.sh
-----------------------------------------

.. code-block:: sh

    #!/bin/sh
    ssh user@site.com "mysqldump -u root -p xxx | gzip > backup.gz"
    echo "get backup.gz" | sftp user@site.com 
    mv backup.gz `date +%a`.gz


恢复方法
-----------------------------------------
不管如何, 需要保存旧的数据库资料. mysqldump.

然后再用mysqlimport恢复即可.
