.. include:: <s5defs.txt>

================================
reStructuredText介绍
================================

:Authors: 机械唯物主义 <linjunhalida@gmai.com>
:Date:    2010-11-10

什么是sphinx?
================================
.. image:: http://www.openerofways.com/images/essays/sphinx.jpg
   :width: 600

.. class:: handout

    sphinx不是那个全文检索引擎! 是一个写文档的工具: sphinx_

它有什么特性?
================================
.. class:: incremental

* python文档所使用的系统
* 输出HTML, LaTeX, manual pages, 纯文本..
* 层级结构, 内链
* 自动索引
* 语法高亮
* 扩展: graphivz, docstrings, 等等..

让我们开始尝试一下
================================

安装
    easy_install -U Sphinx

教程
    http://sphinx.pocoo.org/tutorial.html

创建一个项目
================================

.. class:: handout

    新建一个目录, 然后执行下面的命令:

::

    sphinx-quickstart

.. class:: handout

    只要回答一些问题就好了. 全部默认, 除了一个: 文档和生成的文件不要放在一个目录下, 方便整理

    会在你指定的目录下面生成一些文件. 我们来看看这些文件吧.

目录
================================

::

    $ find
    .
    ./Makefile               # 工具帮我们生成的makefile
    ./build                  # 生成文档后放置的目录
    ./source                 # 文档源码的位置
    ./source/index.rst       # 文档的入口
    ./source/conf.py         # 项目的一些设置, 上面quickstart设置的部分内容可以在里面修改
    ./source/_static         # 静态文档存放目录
    ./source/_templates      # 模板存放目录

开写哈
================================

.. class:: handout

    我们开启index.rst, 主要结构是这里, 我们可以在上面加东西扩展文档:

::

    Contents:
    
    .. toctree::
       :maxdepth: 2

    # 我们在这里加内容
    intro
    tutorial

.. class:: handout

    然后我们就可以继续写intro.rst, tutorial.rst等文档了.
    这些文档的格式都采用restructuredtext方式.

文档对象
================================

.. class:: handout

    如果你要写一个python函数的定义, 这样写:

::

    .. py:function:: enumerate(sequence[, start=0])

    Return an iterator that yields tuples of an index and an item of the
    *sequence*. (And so on.)

    这里是连接 :py:func:`enumerate`

.. class:: handout

    对应的文档介绍在这里: http://sphinx.pocoo.org/tutorial.html#documenting-objects

自动导入代码中的文档
================================

.. class:: handout

    sphinx一个非常好的功能, 就是可以自动嵌入代码中的文档, 如果你有一个模块io.open

::

    .. autofunction:: io.open

    .. automodule:: io
       :members:

.. class:: handout

    sphinx必须先知道你的模块位置, 要在 conf.py 里面把目录加到 sys.path 里面去.

    conf.py里面必须加sphinx.ext.autodoc的模块.

生成我们需要的格式
================================

.. class:: handout

    最后我们需要把文档生成我们想要的格式, 方法如下:

sphinx-build

    $ sphinx-build -b html sourcedir builddir

make

    $ make html

资源
================================

官方文档

    http://sphinx.pocoo.org/

.. _sphinx: http://sphinx.pocoo.org/

