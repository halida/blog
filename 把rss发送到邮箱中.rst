.. image:: http://freshbump.com/graphics/image_files_480x400/480x400_elisa-strozyk-sebastian-neeb-accordion-cabinet.jpg
   :align: center

根据 `大妈gurudigger里面的idea <http://gurudigger.com/idea/detail?iid=14987>`_, 我研究了一下如何把rss订阅都发送到邮箱中, 统一采用邮箱来处理每日的rss阅读.

尝试了一下以下工具/网站:

- http://www.feedmyinbox.com/
  可以订阅站点, 但是只有5个免费站点名额, 并且是每个站点一封邮件.
- http://www.emailrss.cn/
  国内的站点, 但是不知道效果如何.

最后, 我在shlugchat里面发问, 某人推荐我使用 `rss2email`_, 然后一试, 果然挺好用的.

rss2email会把所有的文章都以分开的邮件发送, 在gmail里面很好做阅读.

安装方法(已经在ubuntu源里面了) ::
	 
    sudo apt-get install rss2email

其他系统请见 `rss2email`_ 官方网站.

使用方法
------------------

rss2email的工作目录在 ~/.rss2email里面, 需要先拷贝配置文件 ::
    
    mkdir ~/.rss2email
    cp /usr/share/doc/rss2email/examples/config.py ~/.rss2email/

然后, 需要修改config.py, 用来设置发送邮件的一些参数, 重点需要修改的是 ::

    # 默认是0, 需要改成1, 如果你像我一样采用gmail来发送的.
    SMTP_SEND = 1 
    # gmail的smtp服务器
    SMTP_SERVER = "smtp.gmail.com"
    # gmail需要认证, 所以改成1
    AUTHREQUIRED = 1 
    # 发送的邮箱用户名, 我为了区分专门注册了一个邮箱.
    SMTP_USER = 'linjunhalida.rss.mail'  
    # 密码
    SMTP_PASS = 'xxx'  

好了, 我们输入需要接收rss邮件的邮箱 ::

    r2e new you@yourdomain.com

然后一个一个增加rss源(必须是rss的位置, 而不是网站的名称, 不然抓取不到) ::

    r2e add http://feeds.feedburner.com/allthingsrss/hJBr

最后, 我们需要让r2e不发邮件跑一遍, 放弃当前时间点之前的数据 ::

    r2e run --no-send

现在配置完成了, 每次只要你想看新的内容, 就可以执行以下命令 ::

    r2e run

我设置了160个源, 运行比较慢. 我把它用crontab来作为后台程序跑了. 修改/etc/crontab, 添加上 ::

    1 * * * * halida /usr/bin/r2e run

我设置的是每个小时的第一分钟去抓取, 以我自己的用户名(halida)来跑.

结论
--------------

更多的内容和介绍, 在: http://www.allthingsrss.com/rss2email/getting-started-with-rss2email/

鉴于现在做这个服务的网站不多, 什么时候我搭建一个服务器来玩玩..
	
.. _`rss2email`: http://www.allthingsrss.com/rss2email/
