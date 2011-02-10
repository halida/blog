python和ruby的区别
-------------------------

python经常被拿来和ruby做比较, 他们都是动态脚本语言, 在应用场景上面也非常相似.
我们听到的, 它们之间广为认知的区别是: 

python
    "There should be one - and preferably only one - obvious way to do it."
ruby
    "There Is More Than One Way To Do It."

但是远远不止这些, 它们之间有无数的细节不同. 根据ruby官方网站上面给出的 `针对python程序员的介绍 <http://www.ruby-lang.org/en/documentation/ruby-from-other-languages/to-ruby-from-python/>`_ :

- Strings are mutable. **字符串是可写的.**
- You can make constants (variables whose value you don’t intend to change). **可以设置常量.**
- There are some enforced case-conventions (ex. class names start with a capital letter, variables start with a lowercase letter). **强制名称大小写.**
- There’s only one kind of list container (an Array), and it’s mutable. **只有一个list容器**
- Double-quoted strings allow escape sequences (like \t) and a special “expression substitution” syntax (which allows you to insert the results of Ruby expressions directly into other strings without having to "add " + "strings " + "together"). Single-quoted strings are like Python’s r"raw strings". **""字符串可以内嵌语句**
- There are no “new style” and “old style” classes. Just one kind. **只有一种类.(相对python有新旧之分)**
- You never directly access attributes. With Ruby, it’s all method calls. **无法访问类的属性, 只能通过方法访问.**
- Parentheses for method calls are usually optional. **执行方法可以不用括号.**
- There’s public, private, and protected to enforce access, instead of Python’s _voluntary_ underscore __convention__. **可以限制类方法的访问范围了.**
- “mixin’s” are used instead of multiple inheritance. **mixin取代了多重继承.**
- You can add or modify the methods of built-in classes. Both languages let you open up and modify classes at any point, but Python prevents modification of built-ins — Ruby does not. **可以修改系统内建类的方法.**
- You’ve got true and false instead of True and False (and nil instead of None). **true/false/nil取代True/False/None**
- When tested for truth, only false and nil evaluate to a false value. Everything else is true (including 0, 0.0, "", and []). **只有false/nil为假, 其他都为真.**
- It’s elsif instead of elif. **elsif取代elif**
- It’s require instead of import. Otherwise though, usage is the same. **require取代import.**
- The usual-style comments on the line(s) above things (instead of docstrings below them) are used for generating docs. **代码上面的注释是文档.**
- There are a number of shortcuts that, although give you more to remember, you quickly learn. They tend to make Ruby fun and very productive. **很多快捷方式增加产能.**
- There’s no way to unset a variable once set (like Python’s del statement). You can reset a variable to nil, allowing the old contents to be garbage collected, but the variable will remain in the symbol table as long as it is in scope. **变量是持久的, 不能被删除(除非自动垃圾收集掉)**

上面只是一个总览, 没有给出实际的写ruby的感觉. 我们还是通过示例来看看ruby的特质.

ruby特质
---------------------------
下面的内容取自 `the ruby programming language`_.

首先, ruby是面向对象的. 所有的值都是对象, 比如:

.. code-block:: ruby

    1.class   # => Fixnum
    0.0.class # => Float

注意上面, 函数和方法(上面的class)可以不用带括号, 直接执行, 并且没有歧义. ruby是不能直接访问属性的, 所以不会混淆.

blocks 和 iterators 对python程序员看起来有点怪异, 但是看多了还是很好理解:

.. code-block:: ruby

    3.times {print "ruby"}  # 打印3遍 ruby
    1.upto(9) {|x| print x} # 打印 123456789

times和upto是整型的方法, 他们返回一个迭代器, 然后这个迭代器就执行下面{}内的代码.

ruby也有list和dict对应的数据结构:

.. code-block:: ruby

    a  = [1, 2, 3, 4] # 和python一样也有list
    a.map do     # do end和{}等价
        |x| x*x
    end

    # :one是符号, 如果你知道lisp, 应该明白这个是什么, 
    # 如果你不知道.. 我也不知道怎么说, 就是符号啦.
    # ruby的hash table写法好像没有python简洁.   
    d = {:one => 1, :two => 2, "3" => 3} 
    d[:one] # => 1
    d.each do |key, value|
        print "#{value} : #{key}; " # ruby 里面的字符串可以嵌入语句
    end

ruby的语法是面向表达式的, if之类的控制符也是表达式, 比如:

.. code-block:: ruby

    minimum = if x < y then x else y end

ruby的操作符是作为方法来实现的, 比如 + - * / [] 等, 都可以按照需要来定义. 

取值和赋值是用不同的方法, 只是读取, 用 [], 如果要赋值, 就要用 []= 了.

这些个概念的区别, 需要好好体会.

方法定义:

.. code-block:: ruby
    
    def square(x) # 没有":"
        x*x       # 方法的返回值是最后一个表达式的值.
    end

赋值:

.. code-block:: ruby

    x  = 12
    x += 1
    a, b = 1, 2 # 可以同时赋值多个变量

还有些值得一提的对象: 正则表达式对象(Regexp)和范围对象(Range):

.. code-block:: ruby

    1..10 === 5         # 5在1..10中间
    /\d{5}/ === "12345" # 匹配5个数字

上面的1..10是Range, /\d{5}/是Regexp.

然后是类了:

.. code-block:: ruby

    class Seq
        include Enumerate # 导入Enumerate module
        def initialize(from, to, by) # 初始化函数, 和__init__一样.
            @from, @to, @by = from, to, by # @表示的是类的属性.
        end

    def each
        x = @from
        while x <= @to # while做循环
            yield x # 和python的yield一样.
            x += @by
        end
    end

    s = Seq.new(1, 10, 2)
    s.each {|x| print x} #显示 "13579"

还有一些令人意外的东西:

ruby的字符串是可变的, 比如:

.. code-block:: ruby

    s = "hello"
    s[1..2]= "mo"
    s # => "hmolo"

ruby里面, 只有false和nil是假, 0和""都是为真, 需要注意.

如何学习ruby
------------------------------
直接去 `ruby看官方文档` 吧. 当然, 作者写的书: `the ruby programming language`_ 是深入了解ruby的基础, 和K&R对C的重要性一样.

结论
------------------------------
花了一下午的时间熟悉ruby, 学习前, 感觉ruby会很繁杂, 以及会有"有了python干嘛学习ruby"的想法.
真正开始学了之后, 还是体会到一点ruby的精妙之处的. 个人感觉ruby离lisp比较近(当然, 只有lisp才有那么强大的宏).
等我再深入一点ruby, 再看看有什么意思吧. 恩, 还有ruby的神器: ruby on rails.

.. _`the ruby programming language`: http://www.amazon.com/Ruby-Programming-Language-David-Flanagan/dp/0596516177
