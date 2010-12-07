什么是宣告式编程?
-----------------------------

.. image:: http://i.ehow.com/images/a06/gg/32/declarative-statement_-800X800.jpg

我们编程的时候, 往往是实现某个领域的业务逻辑, 而这些业务逻辑, 往往可以用定义的方式来表述. 程序员需要做的工作是, 如何把把这些业务逻辑的表述(信息), 用写程序的方式又好又快地实现出来. 如果你是一个资深程序员, 你会发现, 自己会从: 根据需求, 命令式地写代码, 控制机器一个动作又一个动作; 慢慢转移到: 用合适的文本描述需求, 然后想办法写个简单的解释器, 把这个文本转换为可执行的程序. 这种开发程序的方式, 我们叫它 `宣告式編程 <http://zh.wikipedia.org/zh/%E5%AE%A3%E5%91%8A%E5%BC%8F%E7%B7%A8%E7%A8%8B>`_.

大多数情况下, 我们会受到工具的限制, 不能很自然地完成这样的一个转换工作, 如果你有遇到这样的问题, 我建议你, 使用python作为编程语言.

为什么用python?
-----------------------------

为了能够很好地支持宣告式編程, 我们需要满足几点:

- 编程语言能够方便地完成数据结构的定义, 并能嵌入在代码当中.

  python内嵌有list, dict, set等数据结构, 并且能够把它们组合起来, 搭建更复杂的结构. 而它们的定义, 是非常简单和清晰的:

.. code-block:: python

    data = dict(
        name = 'me',
        address = ['shanghai', 'chengdu'],
    )

- 也能够很方便地访问和修改这些数据结构.

  python是动态语言, 不需要用户去具体处理资源分配的问题, python会帮助处理这些琐碎的事情.

.. code-block:: python

    data['name'] = 'halida'
    data['address'].append('kunshang')

- 并且能够根据这些数据结构动态地完成一些具体的操作.

  python具有很高的动态特性, 能够在运行时动态生成, 修改对象的特性:

.. code-block:: python

    class P(): pass
    p = P()
    p.v # 错误! p没有v

    # 我们给它设置一个:
    P.v = 12

    p.v # --> 12

我们具体去看一个示例吧.

示例: 配置界面
-----------------------------

我们需要写一个简单的配置用户界面, 用户可以设置一些配置功能. 我们一开始的考虑是, 完全手写, 或者采用WYSIWYG工具, 拖拖拉拉把界面整理出来, 然后再写一个set/get的方法. 比方说, 这样写代码:

.. code-block:: python

    class ConfigDlg(QDialog):
        def init(self):
             self.leName = QLineEdit()
             self.sbValue = QSpinBox()
             ...

        def setUi(self, data):
             self.leName.setText(data['name'])
             self.sbValue.setValue(data['value'])
             ...
    
        def getUi(self):
             data = {}
             data['name'] = self.leName.text()
             data['value'] = self.sbValue.value()
             ...
             return data

但是如果需求变动了怎么办? 如果配置需要添加, 修改? 那么我们就再去修改程序或者代码. 问题是, 程序写了有一段时间了, 变得陌生起来, 除非通读一遍, 不然很容易修改错. 并且代码有点散乱, 就像上面的代码, 在setUi里面写了逻辑, 如果在getUi里面忘记写了就麻烦了.

pythonic的一个原则: Simple is better than complex. 上面写代码的方式不能反映问题的本质, 我们需求的本质信息, 是我们需要配置什么内容, 以及这些内容应该用什么方式表现出来. 在上面的例子里面, 就是name和value. 我们用python数据结构的方式, 重新整理一遍需要配置的内容:

.. code-block:: python

    CONFIG = (
        (unicode, 'name'), 
        (int, 'value'),
    )

这样是不是很清晰?

我们还要定义类型对应的控件, 以及具体处理数据的方法:

.. code-block:: python

    TYPES = dict(
        unicode: (QLineEdit, 'setText', 'text'),
        int: (QSpinBox, 'setValue', 'value'),
    )

现在我们需要把这样的配置转换为具体的界面, 下面就是具体转换的代码, 用命令式就很直截了当了:

.. code-block:: python

    class ConfigDlg(QDialog):
        def init(self):
            self.widgets = {}
            for type, name in CONFIG:
            self.widgets[name] = TYPES[type][0], type

        def setUi(self, data):
            for key, value in data.iteritems():
                w, type = self.widgets(key)
                getattr(w, types[type][1])(value)
    
        def getUi(self):
            data = {}
            for key, value in self.widgets.iteritems():
                w, type = value
                data[key] = getattr(w, types[type][2])()
            return data

要注意到, 我们能够这样'宣告式'地写设置内容, 有几个前提: 

- 设置部分的信息是属于变动的信息
  
  我们实现一个宣告式的平台付出的代价能够被需求变动挽回的时间损失所弥补. 如果设置永远都不需要去改, 我们就没有必要这样设计了. 在上面的例子对应的真实需求里面, 开始的时候也是用最上面的方法来完成. 然后发生了需求变更, 再改成了后面宣告的方式. 这里也反映了python的一个优点: 代码足够少, 足够清晰, 能够非常方便和快速地重构掉.

- 基础是不变的
  
  在上面的例子里面, 我们默认了一些前提: 这个设置见面是在一个QDialog里面, 如果要求配置是分类, 分多个QDialog怎么办? 这里我们需要进行一下预估, 什么信息是'泰山'一样永久不变, 什么信息是'羽毛'一样飘忽不定... 这个需要程序员对业务足够熟悉.

结论
------------------------------

当我们需要实现一个功能的时候, 首先去探索, 这个功能的本质信息是那些? 这样的信息中, 那些是固定的? 哪些是变动的? 然后我们根据信息的本质属性, 选择对应的处理方式. 如果信息是经常变动的, 而它们变动的范围也是可以包括在一个问题域里面, 我们可以用宣告式编程, 来把他们描述出来. 不过, 如果这个问题域足够大, 足够精深, 我们恐怕要考虑专门做一门语言来包容它们了.

