什么是ipython
-----------------------

.. image :: http://ipython.scipy.org/screenshots/snapshot1.png
   :width: 600

python里面的一个杀手级应用就是它的解释器, 我们可以利用这个解释器来完成一些日常的工作, 比如计算器, 字符串处理, 其他计算显示什么的. 但是python本身自带的解释器功能不够强大, 所以有了 `ipython <http://ipython.scipy.org/moin/>`_ 这个大杀器. 上面的图片显示的就是ipython的具体效果.

ipython的目标是成为一个全方位的交互性和探索计算的平台, 它好像是隶属于scipy下面的, 莫非有替代matlab的期望? 对于我们普通人来说, 它的特性已经足够好到替换掉python自带的那个解释器了. 下面为大家介绍.

如何安装
-----------------------
先把ipython装起来吧. ubuntu下面:
.. code-block:: sh

    sudo apt-get install ipython

其他系统可以看 `安装文档 <http://ipython.scipy.org/doc/stable/html/install/install.html#installing-ipython-itself>`_

ipython好在哪里?
-----------------------

列出一些我觉得好用的东西:

- 自动补全: 

  按下tab键会自动补全当前输入的对象名称.比如:

::

    In [1]: os.<tab> # 会自动列出os下面的所有东西
    In [2]: abcd = 12
    In [3]: abc<tab> # 自动补全成abcd

- 缓存输入输出:

  提示符是In [n]: 的格式, 也就是说, 你可以访问In和Out这2个list, 获取输入和输出.

- 整合命令行工具:

  可以用!ls的方式来执行命令行工具, 甚至可以把结果当作参数来使用:

::

    In [4]: out = !ls
    In [5]: for file in out: print file
  
    bin
    temp

- 省略括号

::

    In [6]: s = "hello"
    In [7]: s.replace 'he', 'yi'

    'yillo'

- 交互式GUI操作

  ipython内嵌GUI处理机制, 使用tk/wxpython/pyqt可以交互式地创建和修改类. 创建出的对象是可以响应用户输入的, 并且能够实时修改.

::

    In [8]: from PyQt4.QtGui import *
    In [9]: dlg = QDialog(); dlg.show()
    In [10]: le = QLineEdit(); lw = QListWidget(); 
    In [11]: l = QVBoxLayout(dlg); l.addWidget(le); l.addWidget(lw)



- 帮助系统

  对于任何对象s, 都可以用s??, s?的方式来看它的帮助文档.

- run
  
  可以用

::

    In[12]: run xxx.py

  来执行代码.

- sh模式

  ipython可以当作shell来使用. 只要执行:

.. code-block:: sh

    ipython -p sh

  具体说明见: http://ipython.scipy.org/doc/stable/html/interactive/shell.html

还有其他的很多很多很多特性, 我不一一列出来了.. 具体可以看 `overview <http://ipython.scipy.org/doc/stable/html/overview.html#id1>`_, 以及进入ipython后, 运行:

::

    %quickref

来获取介绍信息. 

emacs + ipython
-----------------------

作为emacs控, 所有东西都要整合到emacs里面去.
根据 `emacs python文档 <http://www.emacswiki.org/emacs/PythonProgrammingInEmacs#toc10>`_ , 我只设置了这几行代码:

.. code-block:: lisp

    (require 'ipython)
    (global-set-key (kbd "C-; 4") 'py-shell)

不过, 我还装了几个其他东西(ubuntu下面):

- ipython
- python-mode
- emacs23

安装ipython后, 会自动给你一个配置文件: 

::

    /usr/share/emacs/site-lisp/ipython.el 

所以只要require它就可以了.

相关资源
-----------------------

- `ipython`_ 官方网站
- `文档 <http://ipython.scipy.org/doc/stable/html/>`_

