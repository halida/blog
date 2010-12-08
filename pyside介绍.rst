什么是pyside?
--------------------------------------

`pyside`_ 是一个Qt4在python下面的绑定, 是PyQt4的取代. 它和PyQt4不同的地方是, 支持商业闭源应用, 以及是Qt4官方支持的.

pyside现在状况怎么样?
--------------------------------------
第一个beta版本已于2010/12/26释放. 处于火热开发中. pyside是完全跟进qt的. beta里面带有qml的支持.

如何获取pyside?
--------------------------------------

如果你用ubuntu, 加一下ppa的源就好了.
网址: https://launchpad.net/~pyside/+archive/ppa

执行命令:

.. code-block: sh

    sudo add-apt-repository ppa:pyside/ppa
    sudo apt-get update
    sudo apt-get install python-pyside pyside-tools

也可以去clone `pyside源码库`_. 

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

  在pyside里面, 直接生成一个对象的方法:

.. code-block:: python

    from PySide.QtUiTools import QUiLoader
    loader = QUiLoader()
    widget = loader.load('mywidget.ui')
    widget.show()

  我上pyside的maillist, 找到了动态生成的方式, 把代码放在这里吧:

.. code-block:: python

    class MyQUiLoader(QUiLoader):
       def __init__(self, baseinstance):
           super(MyQUiLoader, self).__init__()
           self.baseinstance = baseinstance
    
       def createWidget(self, className, parent=None, name=""):
           widget = QUiLoader.createWidget(self, className, parent, name)
           if parent is None:
               return self.baseinstance
           else:
               setattr(self.baseinstance, name, widget)
               return widget

    def loadUi(uifile, baseinstance=None):
       loader = MyQUiLoader(baseinstance)
       ui = loader.load(uifile)
       QMetaObject.connectSlotsByName(ui)
       return ui

  然后, 我们就可以用loadUi来扩展一个类了:

.. code-block:: python

    class Inputer(QDialog):
        def __init__(self):
            super(Inputer, self).__init__()
            loadUi('draw.ui', self)
            self.leInput.returnPressed.connect(self.input)
            ...

QML, QML!
``````````````````````````````````````
pyside可以和qml一起使用, 不过我对qml不熟悉, 等以后熟悉了再来修改具体的示例吧. 你可以直接看 `pyside示例代码`_ 里面关于declarative的部分.

结论
--------------------------------------
经过测试, pyside现在大致可用, 不过在一些地方会有bug, 现在是beta版本, 根据这个态势, 很快就能稳定了. 如果因为pyqt价格问题观望的同学, 现在可以下手pyside了, 也可以当当小白鼠, 为开源社区做点贡献(从我做起吧).

资源
--------------------------------------

- `pyside <http://www.pyside.org/>`_ 官方网站
- `pyside文档 <http://developer.qt.nokia.com/wiki/PySideDocumentation/>`_
- `pyside示例代码 http://qt.gitorious.org/pyside/pyside-examples`_
- `pyside源码库 <http://qt.gitorious.org/pyside>`_
