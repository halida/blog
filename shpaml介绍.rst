.. image:: http://www.rubyinside.com/wp-content/uploads/2007/03/haml.jpg
   :align: center

不知道大家是否都写过html或者xml, 里面尖括号真是既然写又难看, 这里推荐给大家一个非常好用的工具: `shpaml`_.

`shpaml`_ 是借鉴 `haml`_ (就是上面那个图片啦) 的一个工具, 可以极大地简化html/xml的编写工作. 并且不像haml那么重量级. 

shpaml的生成工具只是一个简单的python文件, 你只需要在 `这里 <http://shpaml.webfactional.com/shpaml_py>`_ 下载即可. 整个文件只有365行!

简单尝试一下
-----------------------

我们来看一个实际的例子. 比如我们需要写下面的html代码:

.. code-block:: html

    <html>
      <body>
        <div id="top-nav">
          <div id="top-nav-items">
          </div>
        </div>
        <hr />
        <div id="wrapper">
          <div id="header">
          </div>
          <div id="content">
          </div>
          <div id="sidebar">
          </div>
          <div id="footer">
            @2010 linjunhalida, all right reserved
          </div>
        </div>
      </body>
    </html>

即使能够利用工具来自动生成很多文本, 上面的代码也非常难以阅读. 但是用shpaml的方式就不一样了 ::

    html
      body
        #top-nav
          #top-nav-items
        > hr
    
        #wrapper
          #header
          #content
          #sidebar
          #footer
            @2010 linjunhalida, all right reserved

是不是感觉一下清爽很多? 写起来也不那么废手指了? 

具体语法, 直接查阅 `shpaml官方教程 <http://shpaml.webfactional.com/tutorial/1>`_ , 很简单的, 半小时搞定.

生成html代码
--------------------

那么接下来我们如何把上面的文本生成html代码呢? 先保存成一个文件: xxx.shp, 然后运行 ::

    python shpaml.py xxx.shp > xxx.html

shpaml.py在 `这里`_ 下载. 

打开xxx.html, 是不是和上面的html一模一样? 其他生成方法, 可以见 `shpaml源码页面 <http://shpaml.webfactional.com/source_code>`_.

结论
-------------------
- shpaml采用缩进的方式来表示层级的递进, 这个方法和python的方法一致, 对于python程序员来说应该会很亲切. 
- shpaml用python写成, 整个代码只在一个文件里面, 感兴趣的同学可以学习学习. 它也非常容易嵌入到其他web框架中去.
- 同样的, 如果你发现一个数据源存在很多的冗余信息(就像上面的html/xml), 可以仿照shpaml的方法, 来实现一个上层的模板语言.

希望你和我一样, 喜欢上shpaml.

.. _`shpaml`: http://shpaml.webfactional.com/
.. _`haml`: http://haml-lang.com/
