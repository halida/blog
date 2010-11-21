qt的多国语言支持方案
-------------------------------

qt在设计的时候就考虑到了多国语言应该如何处理, 原理以及使用方法很简单. 如下:

第一步: 写代码的时候, 对于需要翻译的词语, 用tr()包起来, 比如::

    QPushButton hello(QPushButton::tr("Hello world!"));

这样qt就知道这些词语是需要翻译的了. 然后qt需要把这些词语取出来, 放到一个文件里面去, 好进行下一步的翻译工作.

在你的pro文件里面说明这个文件的名称::

    TRANSLATIONS    = clabel_zh_CN.ts

这样就可以利用lupdate这个工具来把需要翻译的词语取出来::

    lupdate-qt4 clabel.pro

然后, 我们就可以开始翻译工作了. qt提供了一个配套的翻译工具: linguist::

    linguist-qt4 clabel_zh_CN.ts

其实ts文件是xml的格式, 你想直接编辑文本也是可以的.

当做完翻译工作之后, 我们需要把ts文件编译一下, 方便程序使用::

    lrelease-qt4 clabel_zh_CN.ts

这样就会生成clabel_zh_CN.qm. 最后, 在代码里面加上选择语言的代码::

    QTranslator trans;
    trans.load("clabel_zh_CN");
    app.installTranslator(&trans);

    QPushButton hello(QPushButton::tr("Hello world!"));
    hello.show();

    app.exec();

qt多国语言更详细的介绍在: http://doc.qt.nokia.com/4.6/i18n-source-translation.html

pyqt下面如何实现多国语言
-------------------------------

pyqt里面实现的过程和qt里面的类似, 只是因为第一步需要扫描的不是c++代码, 所以需要利用一个pyqt的工具: pylupdate4, 用法和lupdate一样.

首先写程序 ::

    trans = QTranslator()
    trans.load('plabel_zh_CN')
    app.installTranslator(trans)

    button = QPushButton(tr("hello world!"))
    button.show()

等等, 里面的tr是什么? ::

    def tr(msg):
        return QCoreApplication.translate("@default", msg)

qt翻译是根据类的名称来走的, 调用了什么类的tr, 就取这个类里面设置的翻译. 

qt里面是可以利用QObject::tr来翻译, 但是pyqt里面不能, 
pylupdate4只是做字符串查找, 看有什么字符串是在tr后面的, 然后根据tr调用者来把这个词语归类, 如果没有调用者, 就把它归类到 "@default" 里面. 于是我就只好利用上面的方法来做一个规避..有点恶心, 看看以后是否会有更好的方法来处理.

然后运行pylupdate, 因为我们是python程序, 没有pro, 就只能手动指定文件了 ::

    pylupdate4 main.py -ts plabel_zh_CN.ts

好了, 下面的步骤和c++的方法一样 ::

    linguist-qt4 clabel_zh_CN.ts
    lrelease-qt4 plabel_zh_CN.ts

然后执行代码, 程序按照我们期望的方式翻译过来了, 是不是很简单?

上面的示例代码放在这里: http://bitbucket.org/linjunhalida/pyqt-i10n-example
