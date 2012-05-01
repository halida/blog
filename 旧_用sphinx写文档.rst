-- 发布时间: 2009-02-10

现在的自动文档生成系统很多了，今天我介绍一个：sphinx。sphinx是python官方文档所使用的一套很简单的文档自动生成系统。

官方网站：http://sphinx.pocoo.org/index.html

 

安装方式：

ubuntu下面： 

::

    sudo apt-get install python-sphinx

windows下面：因为我没有装过，不知道sphinx依赖什么，估计很多，很难装。

 

使用方法：

打开命令行，找到你想要建立文档的位置，运行：

::

    sphinx-quickstart

这是sphinx一个自带的快速配置工具，一路点回车，除了要你输入project名称的时候。（我就是这样的。。）

然后就会在当前目录下面建立一些文档：

build：自动生成的html，pdf之类都会放到这里。

makefile：上面设置的时候，对于unix系统，会默认生成makefile，以后要做什么事情，只要make一下就好了。（不要告诉我你不知道什么是make。）

source：当然是文档源文件目录了呀。

source文件夹初始时里面会放这个东西：

conf.py：sphinx-quickstart里面的设置都会放到这里。随便修改吧。

index.rst：文档的最顶端。

 

写文档：

修改index.rst，

改为：

::
    .. toctree::
       :maxdepth: 2
    
       test

上面增加了一个test的东西。sphinx是把文档当作一个树来看待的，你要加新的东西，需要在原先旧的地方添加你要加的东西的名称，在这个例子是test。现在可以在source目录下新建一个文件：test.rst

内容为：

::

    test
    ==== 

    这个是一个测试。

    * This is a bulleted list.
    * It has two items, the second
      item uses two lines.

回到目录最上层，运行make html，然后就会自动生成html的文档。

再开启 build/html/index.html ，这就是显示的结果，是不是很简单？

.. image:: http://dl.dropbox.com/u/1167873/images/sphinx.png
   :align: center 

更多的文档在 http://sphinx.pocoo.org/contents.html , 以后我会介绍sphinx文档具体怎么写。

