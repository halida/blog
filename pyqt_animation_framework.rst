Qt animation framework介绍
--------------------------------
传统的GUI界面, 一般是静态的, 按钮就是按钮, 不会到处乱蹦, 不过现在这个时代, 冷冰冰的界面不是很吸引人. Qt 4.6里面带有新的animation framework, 就可以帮助我们完成让界面"动起来"的工作.

系统架构
--------------------

.. image:: http://doc.qt.nokia.com/4.7/images/animations-architecture.png
   :width: 600

上面是Qt支持动画的所有类的继承关系列表, 最主要的有几个:

- `QPropertyAnimation <http://doc.qt.nokia.com/4.7/qpropertyanimation.html>`_ 类负责具体的动画效果, 它可以通过设置QWidget属性(property)的方式来完成动画.

- `QAnimationGroup <http://doc.qt.nokia.com/4.7/qanimationgroup.html>`_, 用来把不同的动画拼在一起, 实现连续和复杂的动画效果.

具体我们看实际的代码吧.

示例1: 一个简单的动画
-------------------------------
正如上面所说的, `QPropertyAnimation`_ 负责动画, 这里一个简单的示例, 控制一个按钮移动. 代码如下:

.. code-block:: python

    # 动来动去的按钮
    button = QPushButton("Button")
    button.show()

    # 生成一个动画, 它会修改button的geometry属性
    animation = QPropertyAnimation(button, "geometry")
    # 动画时间是10秒
    animation.setDuration(10000)
    # 开始的位置
    animation.setStartValue(QRect(0, 0, 100, 30))
    # 结束的位置
    animation.setEndValue(QRect(250, 250, 100, 30))
    # 开始吧
    animation.start()

很简单吧? 它默认是以恒定速度运动的, 可以通过设置 `easyCurve <http://doc.qt.nokia.com/4.7/qvariantanimation.html#easingCurve-prop>`_ 来设置运动的类型, 比如先加速后减速什么的, 很方便.

示例2: 分组
----------------------------
上面只是一个普通的动作, 如果我们需要做一组复杂的动作的话, 就要用 `QAnimationGroup`_ 来组织. 
有2种group, QParallelAnimationGroup和QtSequentialAnimationGroup, 一个平行动作, 一个顺序动作.
这个示例设置无数个按钮淡入到窗口中. 上代码:

.. code-block:: python

    #生成一堆按钮, 不同的初始位置
    self.pbs = []
    for i in range(8):
        pb = QPushButton(str(i), self)
        pb.move((i*100) % 600, i*40 + 10)
        self.pbs.append(pb)

    # 建立一个平行执行的动作组
    ag = QParallelAnimationGroup()
    for w in self.pbs:
        # 对于每个按钮, 都生成一个进入的动作
        a = QPropertyAnimation(w, "geometry")
        a.setDuration(1000)
        a.setEasingCurve(QEasingCurve.OutQuad)
        a.setStartValue(QRect(-100, w.y(), w.width(), w.height()))
        a.setEndValue(w.geometry())
        # 添加到组里面去
        ag.addAnimation(a)

    ag.start()

其实简单点说, 只要把要动作的animation添加到group里面, 然后start就好了.

示例3: 状态机
----------------------------
Qt本身提供一个状态机的功能, 和animation结合起来, 可以很方便地完成我们想要的工作. 毕竟, 不同状态的切换, 才是界面运动的本质.
这个示例演示一个按钮, 点击后会在两个位置之间移动.

.. code-block:: python

    dlg = QDialog()
    dlg.resize(500, 300)
    button = QPushButton("Button", dlg)

    # 我们先生成一个状态机
    machine = QStateMachine()

    # 然后给状态机加上几个状态:
    # 不同状态下, button的位置是不同的.
    state1 =  QState(machine)
    state1.assignProperty(button, "geometry", QRect(0, 0, 100, 30))
    state2 =  QState(machine)
    state2.assignProperty(button, "geometry", QRect(250, 250, 100, 30))
    machine.setInitialState(state1) # 初始状态是哪个
    
    # 然后, 我们需要设置状态变化的转换方式.
    transition1 = state1.addTransition(button.clicked, state2)
    transition2 = state2.addTransition(button.clicked, state1)

    # 把动作加到转换方式里面去
    an = QPropertyAnimation(button, "geometry")
    transition1.addAnimation(an)
    an2 = QPropertyAnimation(button, "geometry")
    transition2.addAnimation(an2)
    # 设置完了, 开始吧.
    machine.start()
    dlg.exec_()

就是这么简单..

资源
----------------------------
如果你安装了Qt4.6以上版本, 可以在assistant-qt4里面搜索the animation framework看具体的文档, 也可以看 `在线版本 <http://doc.qt.nokia.com/4.7/animation-overview.html>`. 上面的例子都是脱胎于这个文档的.

Qt附带有几个好玩的示例, 在qt example下面的animation目录下面. pyqt也是一样.

上面我写的的几个示例代码, 可以在这里下载到: http://bitbucket.org/linjunhalida/code-example/src/tip/animation/

结论
----------------------------

Qt animation framework已经出来那么久了, 我现在才真正去学习它, 是有点晚了, 后面的QML都出来的时候, 现在再来看是否有点不合时宜? 但是看着Qt演变的过程, 还是有意义的. 有时间的话, 我去看看它实现的原理, 能不能从中借鉴点什么.

PS: pythonxy里面的pyqt还是4.5, 没有带有animation framework, 郁闷. 不好把功能加到公司项目里面去了.


