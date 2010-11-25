PyQt4提供了非常好的皮肤机制，可以作出非常炫的效果。其中一个功能就是qss，利用类似css的方式来配置界面。
文档在这里。
使用方法(顺便分享一下我的qss配置):

.. code-block:: css

    /*背景贴图*/
    QWidget{ background-image: url(res/tex.png) }
    QAbstractScrollArea,QPushButton { background-image: None}

    /*背景色*/
    QWidget{ background-color: bgdColor }
    QPushButton,QSplashScreen{background-color: None}
    
    /*menu*/
    QMenuBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 lightgray, stop:1 darkgray);
    }
    QMenu {
    margin: 2px; /* some spacing around the menu */
    }
    QMenu::item:selected {
    border-color: borderColor;
    background: rgba(100, 100, 100, 150);
    }
    
    /*按钮*/
    QPushButton{
    border: 3px outset borderColor;
    background-color: bgdColor;
    padding: 5px;
    border-radius: 5px;
    }
    QPushButton:checked {border-color: red}
    /*醒目按下的按钮*/
    QPushButton:pressed {border-color: green}
    
    /*QSlider*/
    QSlider::groove { background: gray; }
    QSlider::groove:horizontal { height: 6px;}
    QSlider::groove:vertical { width: 6px;}
    QSlider::handle {
    border: 1px solid borderColor;
    border-radius: 3px;
    background: bgdColor;
    }
    QSlider::handle:horizontal { width: 18px; margin: -3px 0 ; }
    QSlider::handle:vertical { height: 18px; margin: 0 -3px ; }
    QSlider::add-page { background: gray; }
    QSlider::sub-page { background: green;}
    
    /*QTableView*/
    QTableView {
    alternate-background-color: darkContentColor;
    background-color: contentColor;
    }

上面作为字符串放在DEFAULT_STYLE里面, 然后具体的颜色在下面的python代码中设置:

.. code-block:: python
    
    #设置style里面的颜色
    COLOR_MAP = {
    'borderColor':'gray',
    'bgdColor':'#FCF6E4',
    'contentColor':'#E1EDFB',
    'darkContentColor':'#CDE2F8',
    }
    for k,v in COLOR_MAP.iteritems():
    DEFAULT_STYLE = DEFAULT_STYLE.replace(k, v)
    
    app = QApplication([])
    app.setStyleSheet(DEFAULT_STYLE)
    

显示的效果如下：

.. image:: http://lh5.ggpht.com/_os_zrveP8Ns/TMq9KU_BbTI/AAAAAAAADKw/IUfIQ7_oFjc/s800/screenshot-mainwindow.png
   :align: center
