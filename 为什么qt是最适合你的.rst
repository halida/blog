.. image:: http://cdn.softsailor.com/wp-content/uploads/2010/09/Qt-.png
   :width: 600

很多python开发人员, 在选择界面库的时候都会犹豫一段时间, 到底是选择tk, wxpython, pygtk, pyqt, 还是什么其他奇怪的解决方案. 这里, 我建议, 不要多想了, 节省你的时间和精力, 选择pyqt.

很多开发人员, 在选择界面库时候(至少是你能够选择的时候)都会犹豫很长时间, 到底是MFC, winform, WPF, flash, swing, VCL(还有人知道delphi吗), 还是什么其他奇怪的解决方案, 这里, 我建议, 不要多想了, 节省你的时间和精力, 选择pyqt.

好了, 广告时间结束, 这里说明理由:

- 为什么python? 

  - python是最好用最好学的编程语言(没有之一, VB不够好用)
  - 根据GUI的本质思维, 只有动态语言才能做到那么强的灵活性. 所以C/C++/java什么的不方便开发. 不然你动态生成页面试试?
  - 快速开发. 同样的功能, python的代码是其他语言的若干分之一. 代码量少了, 开发速度和质量都提高了.

- 为什么Qt?

  - 工业级别的界面库. tk, wxpython都太简陋了, 不堪大用. wxpython还有性能问题. (by Jimmy Kuu)
  - 跨平台. VCL, winform, WPF, GTK可能好用一些, 但是跨平台试试? 以后一辈子和某个平台挂钩了. (好吧, GTK, mono可能多平台.. 但是没有pyqt好用)
  - 简单直观的事件处理方式. 只需要把一个signal插入到一个slot里面就好了, 并且是热拔插. callback机制已经过时了.
  - 性能很好, 足够工程使用. 一个实际的例子: linux下面的桌面系统KDE是基於Qt的. 

- 虽然pyqt很好, 但是还有其他需要注意的方面

  - 如果你是开源项目, 随便用. 但是如果是商业闭源, 那需要给 `riverbank <http://www.riverbankcomputing.co.uk/news>`_ 他们交费, 一个开发者350英镑, 还是蛮划算的(比起开发时间来说). 或者你可以考虑 `pyside <http://www.pyside.org>`_?
  - 发布. 打包后的pyqt程序, 10M左右, 如果你对空间要求很严格的话, 就不适合了. 但是现在这个网络时代, 这应该不成问题. QQ都非常大了..
  - 性能. 如果你要画实时图片, 3d什么的, python恐怕太慢了, 老实用回C++吧.
  - 移动应用. `meego <http://meego.com/>`_ 还早, 好像可以在android上面写python, 但是pyqt.. 哈哈哈.
  - web2.0. 好吧, jquery是你的武器. 写javascript去吧. 还有flash..

还有我一些其他的看法:

- Qt的designer是杀手级的. 在linux下面. glader什么的都去死吧.
- tk8.5好像解决了中文问题. 但是控件是不是太少了? 不够用阿.
- wxpython太丑了. 哪里比得上Qt支持的qss方式动态设置风格.
- pyGTK? 没用过. 有时间看看.
- MFC sucks. 
- delphi. 编译飞快. 但是动态生成界面? 当年研究了很久..
- WPF: WTF..
- winform. 他们说不好, 我觉得还好吧?
- android/iOS. 好吧, 我落伍了.

