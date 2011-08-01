.. image:: http://docs.cython.org/_static/cython-logo-light.png
   :align: center

python是门很强大很易用的动态语言, 像其他动态语言一样, 非静态绑定而是在执行时确定值会造成很多性能损耗, 我们可以用cython来解决这样的性能问题.

cython的策略是这样的: 在python语法的基础上, 加上一些静态语言的特性, 比如确定值类型等, 然后把这种类似python语法的代码, 编译成c代码, 
然后利用c编译器, 把代码做成python模块. 这样通过静态编译的方式, 来提高执行代码的性能. 

具体如何使用和学习我就不多说了, `官方文档 <http://docs.cython.org/index.html>`_ 上面写得很清楚.

我写了一个简单的实例代码: https://bitbucket.org/linjunhalida/code-example/src/tip/python/cython_test/
但是转变成cython性能提高只有一倍左右, 不知道到底出了什么问题...
