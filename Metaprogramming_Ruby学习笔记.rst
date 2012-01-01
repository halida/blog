虽然我现在一直在用ruby做rails开发, 但是ruby基本上是属于拿起来用的那种, 很多东西都不是很熟悉.

现在发现有一本Metaprogramming Ruby的书, 就看起来了. 这里整理一下学习笔记, 省得学了白学. 下面其实只是一些tips, 只是给我自己看看的. 所以大家就不要抱有什么期待了.

星期一
--------------------------------

Ruby是全运行态, 没有编译态(对于程序员而言).

Class本身也能运行时创建.

Ruby里面的Class继承自Module, 多了一些实例化, 继承的东西.

所有Class的class是Class, Class继承Module继承Object继承BasicObject.

method的查找方式, 先看object, 然后查Class树, 中间会穿插class include的Module.

所有位置都隐含一个self, 调用方法就是把调用者当作self, irb默认self是main.

private的method只能被隐含self的方式调用, self.private_method是不能调用的.

星期二
------------------------------------

obj.send(:my_method, 3) 用来做动态方法调用. 

define_method用来动态定义方法.

method_missing用来处理找不到方法的时候的状况.

还有undef_method, 这些方法可以用来做很多有意思的事情了.

星期三
-------------------------------------

回顾了block和using.

scope在class, model, def这3个阶层. 可以用Class.new, Module.new, Module@define_method动态生成.

有了instance_eval可以切换到object的scope里面去.

Proc, lambda可以保存block, &用来转换Proc和block.

Proc里面return是从定义Proc的scope里面return, 这个太恶心了吧? 还有不严格判断参数. 还是用lambda比较好.

星期四
-------------------------------------

class 也是 module, 在它们的作用域里面执行代码, 用module_eval.

我有点明白为什么不用缩进来限制作用域了, 缩进没有明确限制作用域来得灵活.

def并不会开启一个新的scope, 还是在class的scope里面.

在class里面用"@"定义instance variable, 用"@@"定义Class instance variable(真绕). 因为@@定义在类树里面, 容易产生bug, 不建议使用.

class method其实是singleton methods, 有趣.

每个object还有eigenclass. 用class << obj; self end; 这样的方式访问.

加上eigenclass, ruby的类树就比较复杂了, 不过看图就好理解一些.

alias和alias_method创建别名.


星期五
-------------------------------------

binding用来缓存作用域, 给eval用. TOPLEVEL_BINDING是最上层的binding.

class里面有无数事件的hook, 比如inherited, included, method_added.

最后一部分activerecord用到的魔法, 我就稍微带过了, 因为具体的方法我兴趣不是很大. 

结论
-------------------------------------

上面只是给我自己总结的一些tip, 一些我已经知道的东西, 但是对其他人非常重要的地方没有写出来. 所以需要理解的话大家还是看书吧.
