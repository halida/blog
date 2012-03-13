.. image:: https://www.rapleaf.com/images/developers/open_source/rspec.gif
   :align: center

我现在在做的 `GuruDigger <http://gurudigger.com>`_ 项目一直没有用测试框架, 最近我做了几次大的重构, 结果出现了许多bug, 为了能够保证以后项目不会在重构中挂掉, 我还是需要把测试给整起来.

rails的测试框架用得比较多的是rspec. 

rspec的原理
----------------------
我们有一段代码:

.. code-block:: ruby

    def exp number n
      result = 1
      n.times.each{result *= number}
      result 
    end

我们需要给出一个单元测试. rspec的写法是这样的:

.. code-block:: ruby

    describe exp do
      it "should work" do
        exp(2, 3).should == 8
        exp(5, 3).should == 125
        exp(1, 3).should == 1
      end
    end

我们来解释一下. 里面的describe和it是什么意思呢? rspec里面的测试是采用描述性的方式进行的. describe说明具体描述的是什么东西, it指代这个东西它的行为应该是怎么样. 上面的代码一方面做好了测试, 另外一方面也直观地描述了这个方法需要做的事情, 符合人类直觉.

然后, 我们看具体验证的部分. 和其他单元测试框架的 assert_equal 函数不同, rspec-expectations 修改了Kernel, 给了一个should方法. 这样让原先的外层函数调用, 变成了内层的方法调用, 造成的结果就是写起来超级直观. 这个算是ruby比较常用的套路了.

should的写法可以去看 `rspec-expectations的文档 <https://github.com/rspec/rspec-expectations>`_.

https://github.com/rspec/rspec-mocks 这一块不太容易懂, 需要看看.

factory_girl
----------------------
factory_girl是取代rails默认生成测试数据的yml格式的一种写法, 原生ruby, 写起来比较舒服和能够嵌入ruby代码.

.. code-block:: ruby

    # 定义一个对象
    FactoryGirl.define do
      factory :user do
        first_name 'John'
        last_name  'Doe'
        admin false
      end
    end

    # 用到的时候build一下就好.
    user = FactoryGirl.build(:user)

网上也有很详细的教程:

https://github.com/thoughtbot/factory_girl/blob/master/GETTING_STARTED.md

rspec和rails整合
----------------------
上面是rspec做测试的部分, 下面我们看如何和rails整合. 其实文档都全了, 我觉得大家还是直接去看官方的文档就好:

https://github.com/rspec/rspec-rails

重点是测试的几个类型.

rspec加上spork
---------------------------------
rspec跑一遍下来超级慢, 于是就有了 `spork <http://spork.rubyforge.org/>`_ 这样的东西. 原理就是先跑一个服务器, 加载好对应的环境. 然后需要执行测试的时候, 就通知这个服务器开始测试. 服务器会fork一下, 执行对应的测试.

如何使用上面的文档都有. 重点是几步:

- 用spork --bootstrap初始化spec_helper.rb, 把每次fork需要做的事情填到对应的方法里面去.
- 跑服务器, 执行spork
- 跑测试. 执行rspec --drb

配置
----------------------
这里有别人贴出来的配置, 还是挺复杂的, 需要搞搞清楚. 但是搞清楚了, 开发起来你会发现非常舒服(前提是你的机器够好...)
https://gist.github.com/1191428

一些资料
----------------------

rspec书籍:
http://pragprog.com/book/achbd/the-rspec-book

rspec cheetsheet:
http://cheat.errtheblog.com/s/rspec/

capybara cheetsheet:
https://gist.github.com/428105
http://cheat.errtheblog.com/s/rspec_shoulda/

rspec最佳实践:
http://eggsonbread.com/2010/03/28/my-rspec-best-practices-and-tips/


