.. image:: http://www.pyside.org/docs/shiboken-0.5.0/_images/generatorworkings.png

pyside的项目已经beta了一段时间了, 它采用的方法是开发一个名为shiboken的绑定生成工具来做处理. 我们也可以利用这个工具来简化做python绑定的工作.

具体工作流程
-----------------
上面的图代表了整个体系工作的方法. 用户提供2个信息: 需要绑定的库的头文件, 以及建立一个需要绑定的库的描述信息文件(xml), 以及在这个描述文件里面手动对生成内容做一些修改. 如果一切顺利的话, 只需要在描述文件里面说明需要绑定到python里面的类/枚举等信息即可. 

如何用?
-----------------

具体可以见 `shiboken官方教程`_, 走到这一步的同学应该对英文没有压力的吧, 我就不再整理成中文了, 毕竟作者他们也都不是英语母语的.

一般情况下, 我们只需要直接下载里面附带的示例, 然后修改一番, 就可以用来给我们自己的库来做绑定了. 我现在就是这样做的.

如何实现的?
-----------------
上面都是具体的做法, 在实际的使用过程中还会遇到各种各样的问题, 我们可能还需要对shiboken机制有一定的了解. 

编译过程
`````````````````

我们写了xml描述文件之后, 实际执行的命令是generatorrunner, 它会按照xml文件,
以及引入的库头文件, 生成wrapper的cpp/h文件. 之后, 我们把这些文件编译成动态链接库, 这个链接库能够直接被python调用.
如下图:

::

    global.h             generatorrunner                       gcc
    typesystem_foo.xml -------------------> wrapper.h/cpp ---------> libfoo.so

generatorrunner运作机制
```````````````````````````````````
这里是 `generator运作机制`_ 的介绍. 

.. image:: http://www.pyside.org/docs/generatorrunner/_images/bindinggen-development.png

如上图, 分成几个模块, api extractor获取头文件的信息, typesystem和injected code就是那个xml描述文件.
shiboken就是generatorrunner后台调用的cpp文件生成工具了.

结论
-----------------
具体shiboken是如何处理的, 以及为了调试方便, 如何获取中间生成的类信息, 这个我还需要时间去了解.
他们的作者也是很开放的, 如果发现问题, 可以往: pyside@lists.openbossa.org 邮件列表上面发邮件提问, 作者基本上是会给回应的(毕竟他们是nokia雇来做这个事情的).

.. _`generator运作机制`: http://www.pyside.org/docs/generatorrunner/overview.html
.. _`shiboken官方教程`: http://developer.qt.nokia.com/wiki/PySide_Binding_Generation_Tutorial
