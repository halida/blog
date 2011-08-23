.. image:: https://a248.e.akamai.net/assets.github.com/img/7744a8503993132e8a14c79be38e3724c6564fa2/687474703a2f2f696d672e736b697463682e636f6d2f32303130303131312d6b6d326635676d747062713233656e70756a6272756a366d676b2e706e67
   :align: center

resque
--------------------------------
resque是ruby on rails下面的一个异步工作分配框架, 它利用redis的队列功能, 来达到异步处理工作的目的. 好处在于使用简便以及很容易和rails整合. 

项目地址在 https://github.com/defunkt/resque, 如何使用里面写的很清楚, 这里就不多说了. 具体逻辑也没有什么好说的, 无非是需要调用任务了, 塞任务到队列里面, 然后worker取队列, 然后把任务做掉.

一些细节:

**resque是如何enque的?**

.. code-block:: ruby

    redis.rpush "queue:#{queue}", encode(item)

**presistance如何做?**

.. code-block:: ruby

  encode: MultiJson.decode(object)

**resque是如何取work的?**

.. code-block:: ruby

    decode redis.lpop("queue:#{queue}")

resque-scheduler
--------------------------------

resque-scheduler是基于resque的一个计划任务插件, 简单地说, 就是能够利用它来做一些定时和定时循环的任务. 项目主页: https://github.com/bvandenbos/resque-scheduler, 使用方法我也不多说了. 项目主页上都有.

**resque-scheduler计划的队列如何处理?**

.. code-block:: ruby

    # First add this item to the list for this timestamp
    redis.rpush("delayed:#{timestamp.to_i}", encode(item))

    # Now, add this timestamp to the zsets.  The score and the value are
    # the same since we'll be querying by timestamp, and we don't have
    # anything else to store.
    redis.zadd :delayed_queue_schedule, timestamp.to_i, timestamp.to_i

竟然根据每个timestamp做了一个队列.. 计划任务都保存到一个sorted set里面.

**scheduler如何检查是否有新的任务?**

核心在于这段代码:

.. code-block:: ruby

    if timestamp = Resque.next_delayed_timestamp(at_time)
      enqueue_delayed_items_for_timestamp(timestamp)
  
    resque_scheduler.rb:
  
    def next_delayed_timestamp(at_time=nil)
      items = redis.zrangebyscore :delayed_queue_schedule, '-inf', (at_time || Time.now).to_i, :limit => [0, 1]
      timestamp = items.nil? ? nil : Array(items).first
      timestamp.to_i unless timestamp.nil?
    end

enqueue_delayed_items_for_timestamp比较复杂, 就不贴了. 

结论
-------------------------------
基本上resque的逻辑很直观, 和想象中的一样. resque-scheduler就不一样了. 复杂很多.

我学习他们的示例代码放在: https://bitbucket.org/linjunhalida/code-example/src/tip/ruby/resque/
