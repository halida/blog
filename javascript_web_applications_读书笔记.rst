这几天抽空把 `javascript web applications <http://book.douban.com/subject/6805476/>`_ 这本书看完了, 整理一下学到的东西.

在我看来, 整本书主要内容就是讲如何抽象js前端开发, 让代码变得更清晰. 具体采用的手法是在js里面实现class, MVC, module等抽象.

整理整理一下我觉得对我来说重要的知识点:

- context switch.
  js里面, new会转换context, 各种回调函数里面context会有变化, 具体影响到的是this以及环境变量.
  要利用到jQuery里面的proxy(底层调用apply等)来做context switch.
- js是prototype的语言, js里面实现继承, 需要通过递归调用prototype.
- 很多封装的技巧, 有种lisp的感觉. 看起来成为一个靠谱的js程序员需要掌握这些技巧了.
- MVC模型, 这个也不需要多说了, 都用烂了, 只要提一下大家就会注意了. Controller里面负责联系model和view, UI事件处理之类的事情.

对我来说比较有用资源的索引:

- 利用前端实现MVC
- 实现module以及对应的依赖关系
- file, drag&drop等的API实现
- 前端开发需要考虑的: performance, cache
- 浏览器调试方面的一些工具: profile, logging
- 一些前端MVC库的介绍: spine, backbone, javascriptMVC

我自己比较不足的地方, 可以在接下来的开发工作中提高的有:

- 针对MVC的理解, 重构现有的程序.
- 考虑使用一些前端的UI库.
- performance, profile, logging, 用它们来提高现有前端代码的性能.
