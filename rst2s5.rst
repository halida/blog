.. include:: <s5defs.txt>

================================
文本方式写幻灯片
================================

:Authors: 机械唯物主义 <linjunhalida@gmai.com>
:Date:    2010-11-10

.. container:: handout

   使用rst2s5来写幻灯片.

.. contents::
   :class: handout

为什么要用S5?
================================

.. class:: handout

   作为乐于分享的开发人员, 总是免不了想向其他人介绍一些好玩的东西. 这个时候, 我们需要写幻灯片, 用展示自己要讲的东西. 
   其他人往往使用PPT, PPT是很好, 但是作为纯文本文件爱好者, 无法以文本方式编辑, 也无法进行版本管控的PPT文件,
   无法满足我们的需求. 那么我们应该用什么工具来做幻灯片呢?
   在wikipedia上面有 `slide工具列表`_ 来介绍现有的幻灯片工具, 我选择的是 S5_ .

   那么S5有什么好处呢?

.. class:: incremental

* 纯文本
* html

.. class:: handout

   纯文本, 直观, 清爽, 方便编写以及后期的维护.
   文件本身其实是html格式的, 利用其他javascript, css之类的设置弄成slide的效果.
   本身方便分发以及发布, 再也不用超级大的PPT工具啦!

S5实例
================================

.. class:: handout

   S5其实就是一个html文件, 带有一堆的css, 脚本什么的, 可以让你以这种方式写:

.. class:: incremental

::

    <div class="slide" id="id1">
      <h1>为什么要用S5?</h1>
      <ul class="incremental simple">
        <li>纯文本</li>
        <li>html</li>
      </ul>
    </div>
    ...

.. class:: handout

   上面就是一张PPT的内容, 是不是很简单?
   其实这个文档本身也是S5..

rst2s5实例
================================

.. class:: handout

   不过写html也太累了, 那么多尖括号也不直观, 最后我在 `大妈 <http://zoomquiet.org>`_ 的指导下, 
   找到了rst2s5这个工具. 可以用rst的方式来写, 然后转为S5格式.

代码 ::

    为什么要用S5?
    ================================
    
    .. class:: incremental
    
    * 纯文本
    * html

试用一下
================================

不多说, `在线rst2s5`_ : http://vps.linjunhalida.com/tools/rst2s5/

本地生成
================================

.. class:: handout

   rst2s5是属于 docutils_ 的, 安装后可以在命令行执行

need docutils::
    
    rst2s5 xxx.rst xxx.html
    rst2s5 --theme small-white xxx.rst xxx.html
    rst2s5 --theme-url http://xxx.com/ui/small-white xxx.rst xxx.html

如何写rst2s5?
================================

* `rst2s5教程`_ : google rst2s5

.. class:: handout

   网上有 `rst2s5教程`_ , 但是没有示例, 我找了半天, 发现这个教程其实也是用rst写出来的, 源文件是 `这个 <http://docutils.sourceforge.net/docs/user/slide-shows.txt>`_, 只要仿照这个文件去写就可以了. 或者你可以看我写的 `文档 <http://dl.dropbox.com/u/1167873/PyQt%E4%BB%8B%E7%BB%8D/pyqt_intro/pyqt_intro.rst>`_. 不需要去学, 直接抄就好了.

   至于rst格式, 你可以看: `ReST快速入门`_, 来学习如何写.

写代码
================================

.. class:: handout

   rst2s5也可以写程序整合到自己的系统中. 比如 `我的博客 <http://vps.linjunhalida.com/blog/article/pyqt%E4%BB%8B%E7%BB%8D/>`_

代码::
    
    from docutils.core import publish_string
    
    overrides = {'theme': '',
                 'theme_url': '/statics/S5/ui/small-white',}

    def rst2S5(string):
        return publish_string(
            source=string,
            settings_overrides=overrides,
            writer_name='s5')

.. class:: handout

   上面的代码, theme里面填的是本地有的theme, 如果要引用网站上面的theme,
   需要把theme栏留空, 设置theme_url.
   我花了好几个小时才发现只有这样才能激活theme_url的选项.

资源
================================

* `在线rst2s5`_: http://vps.linjunhalida.com/tools/rst2s5/
* `slide工具列表`_: http://en.wikipedia.org/wiki/Category:Presentation_software/
* `rst2s5教程`_: http://docutils.sourceforge.net/docs/user/slide-shows.html
* `ReST快速入门`_: http://docutils.sourceforge.net/docs/user/rst/quickref.html
* S5_: http://meyerweb.com/eric/tools/s5/
* docutils_: http://docutils.sourceforge.net/

.. _`在线rst2s5`: http://vps.linjunhalida.com/tools/rst2s5/
.. _`slide工具列表`: http://en.wikipedia.org/wiki/Category:Presentation_software/
.. _`rst2s5教程`: http://docutils.sourceforge.net/docs/user/slide-shows.html
.. _`ReST快速入门`: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _S5: http://meyerweb.com/eric/tools/s5/
.. _docutils: http://docutils.sourceforge.net/
