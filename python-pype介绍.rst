.. image::  http://www.deltat.com/uploaded/inline_pipe_heater_from_Convectronics.JPG
   :width: 600
   :align: center


什么是pipe?
----------------------------
在python里面实现命令行的pipe功能, 比如 

.. code-block:: python

    [1,3,2,0] | sort

介绍在这里: http://blog.csdn.net/lanphaday/archive/2011/03/29/6287114.aspx

安装只需要 ::

    easy_install pipe

我写了一个小用法:

在ruby下面有这样的魔法: 1.hours.ago, 它估计是采用修改整型这个类的方式来做的, 这样太不pythonic.. (不知道我说错没有?)

利用pipe的话, 可以这样写 ::

    1 | hour | ago

代码如下:
https://bitbucket.org/linjunhalida/code-example/src/tip/python/1hourago.py

个人觉得这个东西完全可以扩展到python核心模块中去了.

pipe是如何实现的?
-----------------------------

官方网站: https://github.com/JulienPalard/Pipe

我本来以为它是修改了python核心模块, 结果发现它只是这样的:
提供pipe功能的东西都继承至Pipe类:

.. code-block:: python

    class Pipe:
        def __init__(self, function):
            self.function = function
    
        def __ror__(self, other):
            return self.function(other)
    
核心在于 __ror__, 这个函数对应的就是 | 符号, 不过是右值的.

比如: 当python在解析 [1, 2, 3] | sort 的时候, 如果发现无法在左边的list里面找到or比较的函数的时候,
就会去调用右边的函数__ror__,
就会出现我们想要的结果: 把左边的值传给 sort.function 去执行.

核心代码少得可怜, 大家都可以去观摩下: https://github.com/JulienPalard/Pipe/blob/master/pipe.py
