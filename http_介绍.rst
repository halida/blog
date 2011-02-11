.. image:: http://perl.apache.org/docs/2.0/user/handlers/http_cycle.gif
   :align: center

HTTP是什么就不说了, 大家都知道. 这篇文章对HTTP实现方式的相关内容做一个整理, 满足大家的窥私欲望.

用户如何利用HTTP
------------------------------
先不管HTTP下面是如何实现的, 我们看看上层: 对于用户而言, HTTP的使用很简单: 打开一个浏览器, 输入网址, 比如: http://www.example.com, 
然后按回车, 浏览器就打开了一个界面. 整体工作逻辑就是 ::

    发出网址(URL) --> 服务器传回网站内容 --> 浏览器显示界面

我们理清接口(不用去管浏览器渲染的部分):

输入
    用户给本地的一个程序URL信息
输出
    服务器返回状态, 以及HTML内容

HTTP通讯过程
------------------------------
HTTP是如何实现上面的目标的呢? HTTP直接利用TCP连接, 并且通讯模式很简单, 客户端发出一个请求, 服务器给出一个响应. 并且这个通讯过程是纯文本的.

我们看一个实际的例子, 通过telnet来直接看看HTTP是如何通讯的:

首先连接目标服务器, 80端口是HTTP协议的默认端口. 

::

    halida@halida-desktop:~$ telnet tonycode.com 80
    Trying 67.205.49.228...
    Connected to tonycode.com.
    Escape character is '^]'.

telnet连接上之后, 我们发出请求.

::

    GET / HTTP/1.1
    Host: tonycode.com

"GET"是HTTP请求的方法, "/"是获取资源的目录, "HTTP/1.1"标示采用的是什么HTTP协议版本.
"Host"行代表的是HTTP header, 请求附带的一些其他信息. cookie, 页面缓存等. 具体可见: `HTTP headers`

最后输入2行回车, 表示请求内容发送完毕.

下面是接收到的内容 ::
    
    HTTP/1.1 200 OK

200是状态码, 表示...就是上面的OK, 请求处理完成.

::

    Date: Wed, 09 Feb 2011 01:06:45 GMT
    Server: Apache
    Last-Modified: Wed, 21 Apr 2010 15:49:54 GMT
    ETag: "71de2eb-bce-484c1252b6c80"
    Accept-Ranges: bytes
    Content-Length: 3022
    Vary: Accept-Encoding
    Content-Type: text/html

然后就是返回的一串 `HTTP header`, 里面含有返回内容的信息等.

最后是正文了, 就是我们喜闻乐见的HTML文档了(太长就不显示出来了) ::
    
    <!DOCTYPE html> ...

整体过程就是那么简单. 更多的细节在 `HTTP` wiki文档.

状态码
-----------------
不是每次请求都是200 OK的, 这里面列出一些常见的状态码:

200 OK 
    没什么好说的.

400 Bad Request
    请求有问题.

404 Not Found
    最常见的错误, 无法在服务器上找到对应的资源.

403 Forbidden
    服务器禁止访问此资源.

其他的见: `status code wiki页面 <http://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`_

连接状态
-----------------
HTTP/0.9, HTTP/1.0都是请求/响应后立刻断开, HTTP/1.1里面可以同一个TCP连接使用多次, 以减小多次重复连接带来的资源消耗和延迟.

cookies
-----------------
HTTP协议本身是无状态的, 一个请求一个响应, 就是那么简单. 但是很多时候我们需要记录状态, 比如用户登录等功能. 一般比较常用的是采用 `cookie`_ 的方式实现.

简单点说, 当客户端发出一个请求后, 服务器返回的HTTP header里面会带有一个 ::

    Set-Cookie: name=value; name2=value2

的段, 然后客户端会把这个字符段缓存下来, 下次请求的时候, 就会在自己的header里面带上 ::

    Cookie: name=value; name2=value2

就是这么简单. 其他一些技术细节, 比如cookie的作用时间和范围, 见 `cookie`_ wiki介绍.

HTTPS
-----------------
HTTP本身是明文的, 非常不安全. 为了解决这方面的问题, 就有了HTTPS.

简单地说, HTTPS和HTTP的区别在于, 不是使用TCP作为连接方式, 而是采用SSL的方式来做连接, 上层应用层是没有多少变化的, 传输的时候数据做了加密, 以及连接到服务器的时候, 会有一套验证机制保证服务器是真正的服务器.

具体还是见 `HTTPS` 的wiki界面.

结论
-----------------
HTTP协议很简单优雅, 或许是这样的简单优雅才承载起来一个庞大的web世界. 
对它的掌握是web程序员必备的基础, 之后才能更好地理解在此之上的很多精妙应用.

.. _`cookie`: http://en.wikipedia.org/wiki/HTTP_cookie
.. _`HTTPS`: http://en.wikipedia.org/wiki/HTTP_Secure
.. _`HTTP headers`: http://en.wikipedia.org/wiki/List_of_HTTP_headers
.. _`HTTP`: http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
