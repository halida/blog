需求
--------------------
作为乐于分享的开发人员, 总是免不了想向其他人介绍一些好玩的东西. 这个时候, 我们需要写幻灯片, 用展示自己要讲的东西. 

其他人 [1]_ 往往使用PPT, PPT是很好, 但是作为纯文本文件爱好者, 无法以文本方式编辑, 也无法进行版本管控的PPT文件, 无法满足我们的需求. 那么我们应该用什么工具来做幻灯片呢?

在wikipedia上面有 `专门的页面 <http://en.wikipedia.org/wiki/Category:Presentation_software/>`_ 来介绍现有的幻灯片工具, 我选择了: S5_ .

为什么要用S5?
--------------------

S5其实就是一个html文件, 带有一堆的css, 脚本什么的, 可以让你以这种方式写 ::

    <div class="slide" id="id1">
    <h1>实例</h1>
    <ul class="incremental simple">
    <li>计算器</li>
    <li>10分钟</li>
    </ul>
    </div>

上面就是一张PPT的内容, 是不是很简单?

不过写html也太累了, 那么多尖括号也不直观, 最后我在 `大妈 <http://zoomquiet.org>`_ 的指导下, 找到了rst2s5这个工具. 可以用rst的方式来写, 然后转为S5格式.

用rst方式写S5
--------------------

rst2s5是属于 docutils_ 的, 需要下载 docutils_ , 然后可以在命令行执行 ::
    
    rst2s5.py xxx.rst xxx.html

就可以了.

如何写rst
--------------------

网上有 `rst2s5教程`_ , 但是没有示例, 我找了半天, 发现这个教程其实也是用rst写出来的, 源文件是 `这个 <http://docutils.sourceforge.net/docs/user/slide-shows.txt>`_, 只要仿照这个文件去写就可以了. 或者你可以看我写的 `文档 <http://dl.dropbox.com/u/1167873/PyQt%E4%BB%8B%E7%BB%8D/pyqt_intro/pyqt_intro.rst>`_. 不需要去学, 直接抄就好了.

至于rst格式, 你可以看: `ReST快速入门`_, 来学习如何写.

.. [1] 麻瓜们
.. _`rst2s5教程`: http://docutils.sourceforge.net/docs/user/slide-shows.html
.. _`ReST快速入门`: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _S5: http://meyerweb.com/eric/tools/s5/
.. _docutils: http://docutils.sourceforge.net/
