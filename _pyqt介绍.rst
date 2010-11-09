.. include:: <s5defs.txt>

================================
最强大的GUI库 -- PyQt4
================================

:Authors: 机械唯物主义 <linjunhalida@gmai.com>
:Date:    2010-11-09

.. container:: handout

   PyQt4是我见到过的最好用的GUI开发库, 具体不多讲, 直接上例子.

.. footer:: PyQt4

一个简单的实例
============================

.. class:: incremental

* 计算器
* 10分钟

代码
============================

.. image:: data/caculator.jpg


类层级
============================

::

    QObject
       |
       |----- QWidget
                 |
                 |----- QDialog
                 |
                 |----- QLineEdit
                 |
                 |----- QListWidget


layout
============================
.. image:: data/layout.jpg


layout
============================

* 层级::

    QDialog (QVBoxLayout)
       |
       |----- QLineEdit
       |
       |----- QListWidget

* 代码::

    #layouts
    l = QVBoxLayout(self)
    for w in self.leInput, self.lwResult:
        l.addWidget(w)


Signal and Slot in Qt
============================
.. image:: data/signal_and_slot.jpg

Qt和PyQt 事件机制区别
============================
* Qt::

    this->connect(leInput, SINGAL(returnPressed()), this, caculate))

* PyQt::

    self.leInput.returnPressed.connect(self.caculate)


一个复杂的实例: 扫雷
============================

* 花费时间: 2个晚上, 基础:2.5小时, 一点点提升:1小时
* 扫雷下载: pyqtmine_ 


UI designer
============================
.. image:: data/designer.jpg


UI with Code
============================
::

    form, base = uic.loadUiType("score.ui")
    class ScoreDlg(QDialog, form):
        def __init__(self):
            super(ScoreDlg, self).__init__()
            self.setupUi(self)


Event
============================
::

    #响应鼠标事件
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            ...

    #画图
    def paintEvent(self, event=None):
        ...
        p = QPainter(self)
        ...
            p.drawLine(mx+i*sx, my, mx+i*sx, my+y*sy)
        ...


资源
============================
* PyQt安装
    * ubuntu::

          sudo apt-get install python-qt4 python-qt4-doc 

    * windows可以下载一个python包: pythonxy_

* 学习材料
    * 书籍请google: pyqt book or qt book

    * 中文资料: qteverywhere_

.. _pyqtmine: https://bitbucket.org/linjunhalida/pyqtmine/
.. _pythonxy: http://www.pythonxy.com
.. _qteverywhere: http://www.qteverywhere.com/

