什么是pyside?
--------------------------------------

`pyside`_ 是一个Qt4在python下面的绑定, 是PyQt4的取代. 它和PyQt4不同的地方是, 支持商业闭源应用, 以及是Qt4官方支持的.

pyside现在状况怎么样?
--------------------------------------
第一个beta版本已于2010/12/26释放. 处于火热开发中.

如何获取pyside?
--------------------------------------

如果你用ubuntu, 加一下ppa的源就好了.
网址: https://launchpad.net/~pyside/+archive/ppa

执行命令:

.. code-block: sh

    sudo add-apt-repository ppa:pyside/ppa
    sudo apt-get update
    sudo apt-get install python-pyside pyside-tools
    

尝试pyside
--------------------------------------
我们通过几个示例来看pyside的状况:

简单示例
``````````````````````````````````````
一个简单的示例, pyside提供和pyqt API级别的互通, 方便pyqt用户迁移. 与pyqt代码的区别, 只在import的时候把PyQt4改成PySide就好了:

.. code-block: python

    from PySide.QtCore import *
    from PySide.QtGui import *

    app = QApplication([])
    lb = QLabel('<h1>hello world!</h1>')
    lb.show()
    app.exec_()

UI
``````````````````````````````````````
看起来写代码还OK, 我们看一些其他的功能, 比如如何支持ui. 我们用qtdesigner写好了ui文件, 如何在pyside下面使用?

pyqt有几种方式:

- 采用pyuic4把ui文件转换为python代码. pyside也有一个这样的工具, 名称是pyside-uic.(还有pyside-rcc, pyside-lupdate与pyqt对应)

- 代码中动态导入, pyqt的代码是这样写的:

.. code-block:: python

    form, base = uic.loadUiType("score.ui")
    class ScoreDlg(QDialog, form):
        def __init__(self):
            super(ScoreDlg, self).__init__()
            self.setupUi(self)

  在pyside里面, 我只找到直接生成一个对象的方法:

.. code-block:: python

    from PySide.QtUiTools import QUiLoader
    loader = QUiLoader()
    widget = loader.load('mywidget.ui')
    widget.show()


QML, QML!
``````````````````````````````````````
等待进一步的测试.

发布
``````````````````````````````````````
等待windows下面的测试

结论
--------------------------------------

资源
--------------------------------------

- `pyside <http://www.pyside.org/>`_ 官方网站
- `pyside文档 <http://developer.qt.nokia.com/wiki/PySideDocumentation/>`_
