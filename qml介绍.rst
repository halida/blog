QML
--------------------

今天去看Qt的最新进展, 发现: Qt 4.7 已于2010年九月份发布了, 里面带有一个全新的写GUI的方式: QML. 

具体相关的介绍, 在 `Qt4.7官方文档 <http://doc.qt.nokia.com/4.7-snapshot/index.html>`_ 上面有 `QML介绍 <http://doc.qt.nokia.com/4.7-snapshot/qdeclarativeintroduction.html>`_ . 我花了半个晚上的时间来学习 `QML的教程 <http://doc.qt.nokia.com/4.7-snapshot/qml-tutorial.html>`_ , 发现真的不错.

下面是 `QML的教程`_ 里面的内容, 我稍微介绍一下.

示例1
--------------------

简单点说, QML就是以定义的方式来写界面, 格式很像CSS. 一个简单的示例代码:

::

    //首先引入相关的模块
    import QtQuick 1.0
   
    Rectangle {
        id: page
        width: 500; height: 200
        color: "lightgray"
   
        Text {
            id: helloText
            text: "Hello world!"
            y: 30
            anchors.horizontalCenter: page.horizontalCenter
            font.pointSize: 24; font.bold: true
        }
    }

这里面定义了一个Rectangle(其实就是方块啦)作为背景, 上面再加了一个Text. 注意, Text的位置是通过设定anchors的方法来定位的.

显示的效果就是:

.. image:: http://doc.qt.nokia.com/4.7-snapshot/images/declarative-tutorial1.png


示例2
----------------------

QML能够自己定义对象类型, 比如,新建一个文件Cell.qml:

::

    import QtQuick 1.0
   
    Item {
        id: container
        property alias cellColor: rectangle.color
        signal clicked(color cellColor)
   
        width: 40; height: 25
   
        Rectangle {
            id: rectangle
            border.color: "white"
            anchors.fill: parent
        }
   
        MouseArea {
            anchors.fill: parent
            onClicked: container.clicked(container.cellColor)
        }
    }

这里面定义了一个Cell类型, 它里面有一个Rectangle, 以及一个MouseArea(后面再说).

我们可以定义新的属性:

::

    property alias cellColor: rectangle.color

这个属性只是Rectangle颜色的别名.



也可以定义新的事件:

::

    signal clicked(color cellColor)

MouseArea是用来做用户交互的, 我们把它的onClicked事件和我们定义的clicked事件绑定起来:

::

    MouseArea {
        ...
        onClicked: container.clicked(container.cellColor)
    }

这样, 当用户点击Cell之后, 就会触发clicked事件, 这个事件附带Cell方块的颜色作为参数.

我们定义了一个Cell之后, 如何使用呢? 这里是使用Cell的代码 ::

    import QtQuick 1.0
   
    Rectangle {
        id: page
        width: 500; height: 200
        color: "lightgray"
   
        Text {
            id: helloText
            text: "Hello world!"
            y: 30
            anchors.horizontalCenter: page.horizontalCenter
            font.pointSize: 24; font.bold: true
        }
   
        Grid {
            id: colorPicker
            x: 4; anchors.bottom: page.bottom; anchors.bottomMargin: 4
            rows: 2; columns: 3; spacing: 3
   
            Cell { cellColor: "red"; onClicked: helloText.color = cellColor }
            Cell { cellColor: "green"; onClicked: helloText.color = cellColor }
            Cell { cellColor: "blue"; onClicked: helloText.color = cellColor }
            Cell { cellColor: "yellow"; onClicked: helloText.color = cellColor }
            Cell { cellColor: "steelblue"; onClicked: helloText.color = cellColor }
            Cell { cellColor: "black"; onClicked: helloText.color = cellColor }
        }
    }

效果如下:

.. image:: http://doc.qt.nokia.com/4.7-snapshot/images/declarative-tutorial2.png

别看上面那些代码那么多, 其实都是些图块的定义. 功能就是, 点击上面一堆Cell其中的一个, 就会改变Hello world的颜色. 如何做到的呢? 只要定义Cell的onClicked事件引发后, 对应执行的代码就好了:

::

    Cell { cellColor: "blue"; onClicked: helloText.color = cellColor }

示例3
----------------------

QML最神奇的地方是, 能够定义效果, 比如实现这个:

.. image:: http://doc.qt.nokia.com/4.7-snapshot/images/declarative-tutorial3_animation.gif

当鼠标点击hello world的时候, 就会出现上面的动画.

核心代码是这个 ::

    Text {
        text: "Hello world!"
        ...

        MouseArea { id: mouseArea; anchors.fill: parent }

        states: State {
            name: "down"; when: mouseArea.pressed == true
            PropertyChanges { target: helloText; y: 160; rotation: 180; color: "red" }
        }

        transitions: Transition {
            from: ""; to: "down"; reversible: true
            ParallelAnimation {
                NumberAnimation { properties: "y,rotation"; duration: 500; easing.type: Easing.InOutQuad }
                ColorAnimation { duration: 500 }
            }
        }
    }

先定义一个MouseArea, 捕捉用户点击的事件 
::

    MouseArea { id: mouseArea; anchors.fill: parent }

然后定义一个Hello world翻转的状态, 当mouseArea被点击的时候, 就会把自己变成翻转的状态.

::

        states: State {
            name: "down"; when: mouseArea.pressed == true
            PropertyChanges { target: helloText; y: 160; rotation: 180; color: "red" }
        }

当然, 现在的话点击之后, 就会立刻把hello world翻转过来, 我们要定义一个效果 

::

        transitions: Transition {
            // 这个效果是为从初始状态变为down状态而设定的
            from: ""; to: "down"; 

	    // 并且这个效果是双向的, down变回初始状态也会反过来执行这样的效果.
            reversible: true

	    // 好了, 这里具体定义效果是什么. ParallelAnimation是说同时进行若干效果
            ParallelAnimation {
	        // 转换方向
                NumberAnimation { properties: "y,rotation"; duration: 500; easing.type: Easing.InOutQuad }

                // 变色
                ColorAnimation { duration: 500 }
            }
        }

通过这样定义的方式来写GUI, 是不是很清晰明了?

结论
-------------------

我原先接触过WPF, 也是定义的方式来做的, 现在看到Qt也支持了, 感到蛮欣慰的. 我现在使用pyqt, 听说pyside的snapshot里面已经支持qml了, 期待稳定版本的发布.

对了, 还有一个 `深入教程 <http://doc.qt.nokia.com/4.7-snapshot/qml-advtutorial.html>`_, 可以看看.
