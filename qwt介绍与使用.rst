什么是Qwt?
----------------------

.. image:: http://qwt.sourceforge.net/plot.png

`Qwt <http://qwt.sourceforge.net/>`_ 是一个Qt的第三方库, 它的作用是为了方便一些科学技术相关领域GUI程序的开发. 它提供了一些好的控件: 2D谱图的绘制, 示波器等仪器上面有的控件:比如旋钮什么的. 

我使用它, 是因为我要画曲线图, 频谱图等一系列科学领域需要展示的东西. 其实, 任何数据图, 都可以采用Qwt来绘制. 个人觉得它Qt里面最好用的画谱图工具. 对了, 它的性能很好, 可以做实时显示数据.

Qwt官方网站上面没有一步步的教程, 但是API的文档很全, 并且代码库中带有有很多例子可以参考. 因为我现在是采用pyqt做开发, 所以我使用 `pyqwt <http://pyqwt.sourceforge.net/>`_ 这个python下面的绑定. 上面也有很多示例. 虽然是python的代码, 我想, C++程序员照样能够看懂(应该说所有的程序员都应该可以看懂..)

Qwt架构
----------------------

Qwt的架构很简单, 官方文档上面虽然没有说, 但是我整理了一下:

::

    QwtPlot
       |
       |------- QwtCurve
       |
       |------- QwtCurve

QwtPlot就是谱图显示的控件, 任何需要显示的曲线(包括网格什么的), 都是QwtCurve, 一个QwtPlot上面可以放很多的QwtCurve.

具体职责:

- `QwtPlot <http://qwt.sourceforge.net/class_qwt_plot.html>`_ 负责坐标的部分, 比如显示的范围, X轴Y轴什么的. 要注意的是, 它可以有多个X和多个Y, 方便不同Y值的谱图叠在一起.
- QwtCurve负责如何去绘制谱图, 比如画直方图, 网格什么的. 它还有一个子类: `QwtPlotMarker <http://qwt.sourceforge.net/class_qwt_plot_marker.html>`_, 可以对谱图的特定位置做标记.

上代码
--------------------

下面是我的一个实例代码, 内容就是负责画一个直方图, 效果如下:

.. image:: http://bitbucket.org/linjunhalida/code-example/raw/tip/qwt/barplot.png
   :width: 600

代码在 `这里 <http://bitbucket.org/linjunhalida/code-example/src/tip/qwt/main.py>`_ .

