方法
----------------------

上次讲了如何使用预编译头来加速编译,现在给出一个Qt程序实际的例子,来演示
预编译头的好处.

我们采用qmake来编译Qt程序,qmake本身支持预编译头,
文档在这:http://doc.trolltech.com/3.3/qmake-manual-7.html

使用方法很简单,在pro文件里面加上这几行即可::

    PRECOMPILED_HEADER = lib.hpp #头文件名
    CONFIG += precompile_header #设置使用预编译头功能

示例
----------------------

以下是我测试项目的例子. 文件目录::

    halida@halida-desktop:~/temp/build-qt$ ls
    build-qt.pro   lib.hpp    main.cpp   shower.cpp    shower.hpp

没有使用预编译头时消耗的时间::

    halida@halida-desktop:~/temp/build-qt$ touch *.cpp
    halida@halida-desktop:~/temp/build-qt$ time make>>/dev/null
    real	0m7.292s
    user	0m4.696s
    sys 	0m2.340s

使用预编译头后消耗的时间::

    halida@halida-desktop:~/temp/build-qt$ touch *.cpp
    halida@halida-desktop:~/temp/build-qt$ time make>>/dev/null
    real	0m2.416s
    user	0m1.324s
    sys 	0m1.004s

很明显,提升了相当多的速度.

例子可以在这里下载: http://linjunhalida.72pines.com/files/2010/09/build-qt.zip
