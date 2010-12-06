什么是scons?
--------------------------
.. image:: http://www.gastronomiaycia.com/wp-content/uploads/2008/07/scones.jpg

scons不是上面的小甜饼, 而是一个基于python的自动化构建工具. 和make一个性质. 不过, 更高级一些.

为什么要用它呢?
--------------------------

- 高阶的make工具

  make是不错, 但是太过简单了, 很多东西都要重复写, 很多事情都做不了.. 我们需要一个更高级的工具.

- python

  既然我们要用更高级的工具, 去找找看: automake, cmake, qmake, ant.. 已经有一堆东西了, 我们选择哪一个呢?

  按照我的看法, 对于任何复杂的工具, 本质上来说, 都需要一个足够强大的编程语言来支持, 以便实现自动化和高可配置性.
  既然python已经成为我的"main stream"语言, 当然要看支持python的工具了. google python + make, 第一个结果就是scons了.
  当然, 还有很多其他的 `pyghon构建工具 <http://wiki.python.org/moin/ConfigurationAndBuildTools>`_ 可以选择.

简单的示例
--------------------------

构建工具核心: 描述关系
SConstruct
Program
Object
Library/SharedLibrary
Glob

LIBS, LIBPATH
CCFLAGS
combile objects

dependencies
MD5?
Decider('timestamp-newer'/make)
Decider('timestamp-match')
Decider('MD5-timestamp')

Env.Decider..

CPPPATH -I

SetOption('implicit_cache', 1)

Depends(hello, 'otherfile')/ Ignore
Command()

我如何用scons
--------------------------
下面是我如何用scons, 好孩子不要学, 去看 `scons官方文档`_



资源
--------------------------

- `scons官方文档 <http://www.scons.org/doc/production/HTML/scons-user.html>`_
