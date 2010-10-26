需求
----------------
作为设备开发者, 一般需要让设备与上位机PC通讯, 我们往往考虑采用以下几种接口: rs232, USB, ethernet.

现在在PC机上已经很难见到rs232的接口, 而ethernet也需要做特殊的配置, USB大多成为我们的首选. 对于数据偏少的应用, 我们可以利用USB虚拟串口的方式来完成这样的任务, 虚拟串口的驱动和实例, 对于下位机来说也非常常见. 有个问题: 很多应用无法用虚拟串口的方式来得到满足, 只能按照USB的方式来解决问题. 这个时候, 我们只好针对USB进行编程. 对于复杂的驱动编程, 大多数程序员往往望而却步. 不过总有其他简单的方法解决问题. 这里, 我们介绍一个USB通讯库: libusb.

介绍
----------------

libusb是一个针对usb通讯的库. 使用它, 你不需要知道操作系统的细节, 你只需要对USB有足够的了解即可. 它也不需要你写驱动, 所有的工作都可以在用户态完成. 使用方法很简单, 这里有一个示例: http://sourceforge.net/apps/trac/libusb-win32/wiki/libusbwin32_documentation#IV.Examples , 是不是很简单?

原理
----------------

libusb自己带有一个内核驱动, 名字叫libusb0.sys, 放在WINDOWS\SYSTEM32\DRIVERS里面. 用户程序调用libusb0.dll, dll会把任务交由驱动来完成. 这样保证用户态就能够完成USB通讯的作业.

具体做了什么, 可以通过下载项目的源文件来了解, 等我有时间的时候再看看吧.

安装方法
----------------

libusb现在有好几个版本. 主页面在这里: http://www.libusb.org/

 * 因为我们一般是进行工程应用, 选择相对稳定的版本: libusb-0.1. 
 * 平台在windows下的话, 我们采用libusb-win32: http://www.libusb.org/wiki/libusb-win32
 * linux下一般已经添加到源里面去了, 查找libusb即可.

windows下安装方法: http://www.libusb.org/wiki/libusb-win32#Installation

里面有2种安装方式, Filter Driver Installation 和 Device Driver Installation, 前面一个可以说是开发环境, 后面可以说是发布驱动本身. 我们因为是做系统, 选择前面一个方式, 省得麻烦.

使用
----------------

这里有比较详细的文档: http://sourceforge.net/apps/trac/libusb-win32/wiki/libusbwin32_documentation
