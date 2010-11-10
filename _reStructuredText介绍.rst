.. include:: <s5defs.txt>

================================
reStructuredText介绍
================================

:Authors: 机械唯物主义 <linjunhalida@gmai.com>
:Date:    2010-11-10

什么是reStructuredText?
================================
一种写文档的格式. 简称: ReST_

.. class:: handout

   已经有那么多的写文档的方式了, 为什么要用它? 

.. class:: incremental

* 简单, 易学易用
* 源文件易读
* 方便生成html/pdf等其他格式
* 以及: python文档是用它的格式

怎么玩?
================================

不多说, 直接用: http://goo.gl/1jNF4

.. class:: handout
   
   大家可以上 http://www.tele3.cz/jbar/rest/rest.html 或者: http://goo.gl/1jNF4 直接试用

语法
================================

.. class:: handout

   那么具体的语法怎么学呢?
   何必再写一份? 大家自己看就好了哈
   我也看不懂多少英文, 但是会抄就好了..

There should be one-- and preferably only one --obvious way to do it.

http://docutils.sourceforge.net/docs/user/rst/quickstart.html
http://docutils.sourceforge.net/docs/user/rst/quickref.html

如何生成其他格式
================================

* html: 有个东西叫rst2html::

    rst2html xxx.rst xxx.html

* pdf: 有个东西叫rst2pdf::

    rst2pdf xxx.rst
  
* latex: 有个东西叫rst2latex::

    rst2latex --input-encoding=utf-8 --output-encoding=utf-8 xxx.rst >> s.tex


.. class:: handout

   没有弄明白rst2pdf如何弄中文.. 发了 `issue <http://code.google.com/p/rst2pdf/issues/detail?id=377>`_

python code
================================

有个东西叫docutils::

    from docutils.core import publish_string
    content = publish_string(
        source="doc here"
        writer_name='html'
        )

我用它来干什么?
================================

* 写博客
* 写文档
* 问题: 支持ReST的网站不多..

连接
================================

* 官方网站: ReST_ 

.. _ReST: http://docutils.sourceforge.net/rst.html#try-it-online
