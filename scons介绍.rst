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

安装
--------------------------

- debian源:

::

    sudo apt-get install scons

- 或者直接在安装了python的环境里面easy_install:

::

    eays_install scons

  对了, 如果在windows下面, easy_install安装后有可能出现: import error: 找不到Scons.Script, 我研究了一下, 发现在scons放的位置不对, 只要搜索下把scons的目录放到dist-packages文件夹里面就好了.

一个简单的示例
--------------------------

我们直接去看一个示例吧, 目标是编译一个hello world c程序:


.. code-block:: sh

    # 新建一个目录
    rm t1 -rf; mkdir t1; cd t1

    # 这里是我们的程序    
    cat > hello.c <<EOF
    #include <stdio.h>
    int main(){
        printf("hello, world!\n");
        return 0;
    }
    EOF

    # scons的脚本文件名称是SConstruct/Sconstruct/sconstruct, 如果直接执行scons, 会按照上面的顺序找文件. 和make类似.
    cat > sconstruct <<EOF
    # sconstruct其实就是一个python脚本, 支持所有python能做的事情.
    BIN = 'hello'
    # scons和其他构建工具一样, 是定义式的, 我们定义需要构建一个程序, 名称是BIN, 依赖hello.c
    Program(BIN, ['hello.c'])
    # 然后, 我们再定义一个执行的命令, 方便看结果. 它依赖BIN, 方法就是直接执行这个程序.
    Command('run', BIN, './'+BIN)
    EOF

    # 最后, 我们调用scons来执行run的命令.    
    scons run

这里是结果:

.. code-block:: sh

    scons: Reading SConscript files ...
    scons: done reading SConscript files.
    scons: Building targets ...
    gcc -o hello.o -c hello.c
    gcc -o hello hello.o
    ./hello
    hello, world!
    scons: done building targets.

scons会自动根据文件来调用对应的构建工具.

上面只是一个示例, 更多的最好去看 `scons官方文档`_. 文档有了我就不需要再写一遍了.

我自己整理的一些重点
-----------------------

我们可以构建:

- Program
- Object
- Library
- SharedLibrary

批量获取源文件:

.. code-block:: python

    Program('hello', Glob('*.c'))

设置参数: LIBS, LIBPATH, CCFLAGS, CPPPATH

我们可以设置一个环境:

.. code-block:: python

    env = Environment(CC = 'gcc',
                      CCFLAGS = '-O2')
    env.Program('hello.c')

可以设置判断是否修改的算法:

.. code-block:: python

    # 默认采用算MD5的方法判断文件是否修改
    Decider('MD5')
    # 可以设置传统的看timestamp是不是最新的方式
    Decider('timestamp-newer'/make) #
    # 也可以设置只要timestamp变了就算文件被修改了
    Decider('timestamp-match')
    # 混合: timestamp改变了, MD5也变了才算修改了
    Decider('MD5-timestamp')

可以根据Enviroment设置Decider

缓存判断依赖关系

.. code-block:: python

    SetOption('implicit_cache', 1)

设置依赖关系

.. code-block:: python

    Depends(hello, 'otherfile')
    Ignore(hello_obj, 'hello.h')

我最喜欢的, 执行自定义的命令:

.. code-block:: python

    Command('hello.o', 'hello.c',
            ['gcc $SOURCE -c',
             'wc -l $SOURCE >> summary'])

结论
--------------------------
看起来scons还是有点意思的, 我先用一段时间, 等有了一定的感觉之后再来看看.

资源
--------------------------

- `scons官方文档 <http://www.scons.org/doc/production/HTML/scons-user.html>`_
