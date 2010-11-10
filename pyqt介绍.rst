.. include:: <s5defs.txt>

================================
最强大的GUI库 -- PyQt4
================================

:Authors: 机械唯物主义 <linjunhalida@gmai.com>
:Date:    2010-11-09

.. container:: handout

   PyQt4是我见到过的最好用的GUI开发库, 具体不多讲, 直接上例子.

.. contents::
   :class: handout

.. footer:: PyQt4

一个简单的实例
============================

.. class:: incremental

* 计算器
* 10分钟

.. image:: http://lh6.ggpht.com/_os_zrveP8Ns/TNnrsk8C64I/AAAAAAAADMc/TMTjkv1is7k/s800/caculator_ui.png

.. class:: handout

   pyqt实现一个简单的计算器界面, 只需要10分钟.

代码
============================

.. image:: http://lh3.ggpht.com/_os_zrveP8Ns/TNnooDH5dtI/AAAAAAAADLo/KK7FwKekTRo/s800/caculator.JPG

.. class:: handout

   这个是计算器的代码::

    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    class Caculator(QDialog):
        def __init__(self):
            super(Caculator, self).__init__()
            #widgets
            self.leInput = QLineEdit()
            self.lwResult = QListWidget()
            #layouts
            l = QVBoxLayout(self)
            for w in self.leInput, self.lwResult:
                l.addWidget(w)
            #events
            self.leInput.returnPressed.connect(self.caculate)
    
        def caculate(self):
            data = unicode(self.leInput.text())
            if not data: return
            self.leInput.clear()
    
            try:
                result = unicode(eval(data))
            except Exception as e:
                result = unicode(e)
    
            self.lwResult.addItem(result)
    
            
    def main():
        app = QApplication([])
        Caculator().exec_()
        
    if __name__=="__main__":
        main()

类层级
============================

::

    QObject
       |----- QWidget
                 |----- QDialog
                 |----- QLineEdit
                 |----- QListWidget

.. class:: handout

   以及计算器这个界面的控件是如何组织的.

layout
============================
.. image:: http://lh3.ggpht.com/_os_zrveP8Ns/TNnoon5j6aI/AAAAAAAADLw/ITJ9fVU9YtE/s800/layout.JPG

.. class:: handout

   qt采用非常简洁的方式来组织界面.
   只需要设置子控件是如何在父控件上面排列的, qt自动帮你调整好大小.

layout
============================

* 层级::

    QDialog (QVBoxLayout)
       |----- QLineEdit
       |----- QListWidget

* 代码::

    l = QVBoxLayout(self)
    for w in self.leInput, self.lwResult:
        l.addWidget(w)


Signal and Slot in Qt
============================
.. image:: http://lh4.ggpht.com/_os_zrveP8Ns/TNnoo68TzKI/AAAAAAAADL4/jPjbRhwQEI8/s800/signal_and_slot.JPG

.. class:: handout

   至于消息如何传递的呢? 只需要把一个消息链接到处理的方法上面就好了.

Qt和PyQt 事件机制区别
============================
* Qt::

    this->connect(leInput, SINGAL(returnPressed()), this, caculate))

* PyQt::

    self.leInput.returnPressed.connect(self.caculate)

.. class:: handout

   pyqt比qt要简单得多, pythonic!


一个复杂的实例: 扫雷
============================

* 花费时间: 2个晚上, 基础:2.5小时, 一点点提升:1小时
* 扫雷下载: pyqtmine_ 

.. image:: http://lh6.ggpht.com/_os_zrveP8Ns/TNnoooQuryI/AAAAAAAADL0/MLwyt5qromk/s800/pyqtmine.JPG

.. class:: handout

   上面是基础的一些概念, 我们深入一些, 看看更复杂的例子. 比如一个扫雷的程序(其实也很简单)

UI designer
============================
.. image:: http://lh4.ggpht.com/_os_zrveP8Ns/TNnoodk5clI/AAAAAAAADLs/cbHdyQCMco8/s800/designer.JPG

.. class:: handout

   自己写UI是不是太复杂了? 拖拖拉拉不是更好? qt提供了这样的一个工具.
   非常好用! 可以和tk/wxpython等说再见了!

UI with Code
============================
::

    form, base = uic.loadUiType("score.ui")
    class ScoreDlg(QDialog, form):
        def __init__(self):
            super(ScoreDlg, self).__init__()
            self.setupUi(self)

.. class:: handout

   写好score.ui之后, 需要补充后面的逻辑, 把ui转换成class, 然后继承就好了.

Event
============================
::

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            ...

    def paintEvent(self, event=None):
        p = QPainter(self)
        ...
	p.drawLine(mx+i*sx, my, mx+i*sx, my+y*sy)

.. class:: handout

   不是所有的时间机制都可以用signal&slot解决的, 有些事件, 只能通过重载来解决.
   比如上面鼠标和画图事件, 必须重载对应的处理函数.

其他强大特性
============================

* 足够多和好用的控件/自定控件/整合到designer中
* webkit/script支持
* 强大/方便/快速的绘图控件
* 富文本/文本解析
* 多国语言支持
* 其他第三方控件支持: pyqwt

发布
============================
pyinstaller_!

.. class:: handout

   pyinstaller可以完美支持pyqt的打包工作, 不过对于python2.6以上的版本, 需要下载使用开发版本, 这里有 `介绍 <http://www.pyinstaller.org/wiki/Python26Win>`_.
   不推荐py2exe, 比较复杂.

资源
============================
* PyQt安装
    * ubuntu::

          sudo apt-get install python-qt4 python-qt4-doc 

    * windows可以下载一个python包: pythonxy_

* 学习材料
    * qt_ 以及 pyqt_ 官方网站
    * 书籍请google: pyqt book or qt book

    * 中文资料: qteverywhere_

.. _qt: http://qt.nokia.com/products/
.. _pyqt: http://www.riverbankcomputing.co.uk/software/pyqt/intro
.. _pyqtmine: https://bitbucket.org/linjunhalida/pyqtmine/
.. _pythonxy: http://www.pythonxy.com
.. _qteverywhere: http://www.qteverywhere.com/
.. _pyinstaller: http://www.pyinstaller.org/
