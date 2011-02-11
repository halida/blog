.. image:: http://www.webaxes.com/wp-content/uploads/2010/06/ruby-on-rails.jpg
   :width: 600
   :align: center

好吧, 昨天看了一下ruby, 今天就要来看看ruby on rails了.

哲学
----------------

- DRY: 不写重复的东西
- 约定取代设置: rails假定了你要做的事情, 而不是你自己设置一切.
- REST方式.

教程
----------------

这里是一篇 `rails教程 <http://guides.rubyonrails.org/getting_started.html#guide-assumptions>`_, 按照上面的指示做一遍, 就对rails的思路和哲学有了一定了解了, 这里就不再重复.

整体架构
----------------
.. image:: http://dedicatedwebserverhosting.co.uk/Images/Tools%20for%20Ruby%20on%20Rails-2.png

如上图, rails采用MVC架构. 进来的http请求, 交由Dispatcher分发给(设置文件是app/routes.rb)对应的controller(app/controller下面), 然后controller把数据交给view(app/views)渲染返回.

特性
----------------

自动代码生成
````````````````

rails3里面可以用命令直接生成大量代码 ::

    rails generate controller home index
    rails generate scaffold Post name:string title:string content:text

运行之后生成了一堆文件. 节省了工作, 但是对于有洁癖的人来说, 会很不舒服.

快捷方式
````````````````

rails提供了很多快捷方式以减少代码量, 比如对数据做验证:

.. code-block:: ruby

    class Post < ActiveRecord::Base
      validates :name,  :presence => true
      validates :title, :presence => true,
                        :length => { :minimum => 5 }
    end

比如访问权限控制:

.. code-block:: ruby

    class PostsController < ApplicationController
     
      before_filter :authenticate, :except => [:index, :show]
     
      # GET /posts
      def index
        @posts = Post.all
      ...

这些看起来是ruby的哲学, 减少了代码量的同时, 把复杂度隐藏到framework里面了, 不好说是好事还是坏事.

结论
----------------
按照上面的教程走了一遍, 个人感觉:

- 它注重快速开发, 用最少的代码来生成最多的功能.
- ruby on rails采用命令来生成大量代码, 我个人非常不喜欢, 因为不够简洁. 但是对于快速开发, 这个方式节省了大量的编码工作.
- 它假设了一条最好的方式来做开发, 并鼓励开发者走这条道路.
- 个人觉得, 适合一次又一次地开发同类型的网站.

上面只是对rails的初探, 很不完全, 也不深入. 如果有机会开发过一个项目, 
可能有更深刻的体会. 但是还有其他的很多事情在等着我... 这个就先放下吧.
