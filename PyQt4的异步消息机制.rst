因为工作需要，要在GUI的后台维护一个监控线程，该线程需要和主线程做通讯。为了完成这个需求，需要采用一种线程安全的消息机制。因为我采用PyQt4作为GUI的库，因此，直接使用PyQt4的消息机制成为我考虑的首选。

在PyQt4里面，发出消息采用emit的方式。比如:

.. code-block:: python

    # 新的pythonic的方式
    self.sbValue.setValue[int].emit(12)
    # 旧的
    self.sbValue.emit(SIGNAL("setValue(int)"), 12)

但是放到多线程里面，会发生什么事情呢？

先解释一下消息处理的原理。我们知道，GUI之所以能够处理消息，是因为GUI主线程在初始化完毕的时候，会运行一个ecec_()方法，在这个方法里面，线程不断地检查消息队列，看是否有新的消息发出来，如果有，就处理它。这就是我们说的：event loop。

然后看文档。 `Qt在多线程下的消息传递机制 <http://doc.trolltech.com/4.1/threads.html#synchronizing-threads>`_ :

.. image:: http://doc.trolltech.com/4.1/images/threadsandobjects.png
   :width: 600px
   :align: center

里面一段话:

Qt supports three types of signal-slot connections:
* With direct connections, the slot gets called immediately when the signal is emitted. The slot is executed in the thread that emitted the signal (which is not necessarily the thread where the receiver object lives).
* With queued connections, the slot is invoked when control returns to the event loop of the thread to which the object belongs. The slot is executed in the thread where the receiver object lives.
* With auto connections (the default), the behavior is the same as with direct connections if the signal is emitted in the thread where the receiver lives; otherwise, the behavior is that of a queued connection.

也就是说，有3种机制：
* 采用直接调用的方式。类似于callback。 调用者线程直接去执行被调用的方法。
* 队列方式。调用者线程把消息丢给消息队列，然后就不管它了。被调用者的线程在处理消息队列的时候，就会处理它。
* 自动方式（默认）。如果调用者和被调用者是属于一个线程的，系统选择直接调用，不然就采用队列的方式。

而机制的选择，可以在connect方法里面设置type:

.. code-block:: c++

    bool QObject::connect (const QObject * sender,
                           const char * signal,
                           const QObject * receiver,
                           const char * method,
                           Qt::ConnectionType type = Qt::AutoConnection)

那麽，我们可以开始做实验验证这样是否在PyQt4里面行得通了。

测试代码1：测试在单线程下，修改type之后，emit消息是否会立刻执行下一行代码:

.. code-block:: python

    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    """
    线程中发消息
    """
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    
    import threading
    import time
    
    class Main(QDialog):
        def __init__(self):
            QDialog.__init__(self)
            self.pbProcess = QPushButton("&amp;amp;amp;OK")
            self.leResult = QLineEdit("")
    
            layout = QHBoxLayout(self)
            for w in self.pbProcess, self.leResult:
                layout.addWidget(w)
    
            self.connect(self.pbProcess, SIGNAL("clicked()"),
                         self.process)
            self.connect(self, SIGNAL("waitProcess()"),
                         self.waitProcess)#, Qt.QueuedConnection)
    
        def process(self):
            threading.Thread(target=self.threadRun).start()
    
        def threadRun(self):
            time.sleep(3)
            self.emit(SIGNAL("waitProcess()"))
            print "sended.."
    
        def waitProcess(self):
            time.sleep(3)
            self.leResult.setText("hello！")
    
    def main():
        app = QApplication([])
        Main().exec_()
    
    if __name__=="__main__":
        main()

点击按钮，"sended!"要过一段时间才出现在命令行。
把上面的注释部分改为:

.. code-block:: c++

    self.connect(self, SIGNAL("waitProcess()"),
                 self.waitProcess, Qt.QueuedConnection)

再执行一次，点击按钮，"sended!"立刻就出现了。

测试代码2：现在转到线程里面:

.. code-block:: python

    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    """
    线程中发消息
    """
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    
    import threading
    import time
    
    class Main(QDialog):
        def __init__(self):
            QDialog.__init__(self)
            
            self.pbProcess = QPushButton("&amp;OK")
            self.leResult = QLineEdit("")
            
            layout = QHBoxLayout(self)
            for w in self.pbProcess, self.leResult:
            layout.addWidget(w)
            
            self.connect(self.pbProcess, SIGNAL("clicked()"),
            self.process)
            self.connect(self, SIGNAL("waitProcess()"),
            self.waitProcess)#, Qt.QueuedConnection)
        
        def process(self):
            threading.Thread(target=self.threadRun).start()
        
        def threadRun(self):
            time.sleep(3)
            self.emit(SIGNAL("waitProcess()"))
            print "sended.."
        
        def waitProcess(self):
            time.sleep(3)
            self.leResult.setText("hello！")
    
    def main():
        app = QApplication([])
        Main().exec_()
        #app.exec_()
    
    if __name__=="__main__":
        main()

执行后，前3秒线程等待，GUI不会卡死。然后线程打印："sended.."，然后GUI卡死3秒，然后GUI显示"hello!"。
