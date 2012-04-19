.. image:: http://webification.com/wp-content/uploads/2011/03/pjaxascii.png
   :align: center

什么是pjax?
----------------------------
现在很多网站(`facebook <https://twitter.com/>`_, `twitter <https://twitter.com/>`_)都支持这样的一种浏览方式， 
当你点击一个站内的链接的时候， 不是做页面跳转， 而是只是站内页面刷新。 这样的用户体验， 比起整个页面都闪一下来说， 好很多。

其中有一个很重要的组成部分， 这些网站的ajax刷新是支持浏览器历史的， 刷新页面的同时， 浏览器地址栏位上面的地址也是会更改， 
用浏览器的回退功能也能够回退到上一个页面。

那么如果我们想要实现这样的功能， 我们如何做呢？

我发现pjax提供了一个脚本支持这样的功能。 

pjax项目地址在 https://github.com/defunkt/jquery-pjax 。 实际的效果见： http://pjax.heroku.com/ 
没有勾选pjax的时候， 点击链接是跳转的。 勾选了之后， 链接都是变成了ajax刷新。

为什么要用pjax?
----------------------------
pjax有好几个好处：

- 用户体验提升。 

  页面跳转的时候人眼需要对整个页面作重新识别， 刷新部分页面的时候， 
  只需要重新识别其中一块区域。自从我在自己的网站 `GuruDigger <http://gurudigger.com/>`_ 上面采用了pjax技术后， 
  不由觉得访问其他只有页面跳转的网站难受了许多。
  同时， 由于刷新部分页面的时候提供了一个loading的提示， 以及在刷新的时候旧页面还是显示在浏览器中， 
  用户能够容忍更长的页面加载时间。

- 极大地减少带宽消耗和服务器消耗。 

  由于只是刷新部分页面， 大部分的请求（css/js）都不会重新获取， 
  网站带有用户登录信息的外框部分都不需要重新生成了。
  虽然我没有具体统计这部分的消耗， 我估计至少有40%以上的请求， 30%以上的服务器消耗被节省了。

坏处我觉得也有：

- IE6等历史浏览器的支持

  虽然我没有实际测试， 但是由于pjax利用到了新的标准， 旧的浏览器兼容会有问题。 不过pjax本身支持fallback， 
  当发现浏览器不支持该功能的时候， 会回到原始的页面跳转上面去。

- 复杂的服务器端支持

  服务器端需要根据过来的请求， 判断是作全页面渲染还是部分页面渲染， 相对来说系统复杂度增大了。
  不过对于设计良好的服务器代码， 支持这样的功能不会有太大的问题。

综合起来， 由于用户体验和资源利用率的提升， 坏处是可以完全得到弥补的。 **我强烈推荐大家使用。**

如何使用pjax?
----------------------------

直接看 `官方文档 <https://github.com/defunkt/jquery-pjax>`_ 就可以了。 

我觉得做技术的人要养成看一手的技术资料的习惯。 

有一个rails针对pjax的 `gem插件 <https://github.com/rails/pjax_rails>`_ 可以直接使用。 也有 `django的支持 <https://github.com/jacobian/django-pjax>`_ 。

pjax的原理
----------------------------

为了能够处理问题， 我们需要能够理解pjax的运作方式。 pjax的代码只有一个文件： https://github.com/defunkt/jquery-pjax/blob/master/jquery.pjax.js

如果有能力， 可以自己去看一遍。 我这里解释一下原理。

首先， 我们在html里面指定， 需要做pjax的链接内容是哪些， 以及点击之后需要更新的部分（放在data-pjax属性里面）:

.. code-block:: js

    $('a[data-pjax]').pjax()

当加载了pjax脚本之后， 它会拦截这些链接的事件， 然后包装成一个ajax请求， 发送给服务器。 

.. code-block:: js

    $.fn.pjax = function( container, options ) {
      return this.live('click.pjax', function(event){
        handleClick(event, container, options)
      })
    }

    function handleClick(event, container, options) {
      $.pjax($.extend({}, defaults, options))
      ...
      event.preventDefault()
    }
    var pjax = $.pjax = function( options ) {
      ...
      pjax.xhr = $.ajax(options)
    }


这个请求带有X-PJAX的HEADER标识， 服务器在收到这样的请求的时候， 就知道只需要渲染部分页面返回就可以了。

.. code-block:: js

    xhr.setRequestHeader('X-PJAX', 'true')
    xhr.setRequestHeader('X-PJAX-Container', context.selector)


pjax接受到返回的请求之后， 更新data-pjax指定的区域， 同时也会更新浏览器的地址。


.. code-block:: js

    options.success = function(data, status, xhr) {
      var container = extractContainer(data, xhr, options)
      ...
      if (container.title) document.title = container.title
      context.html(container.contents)
    }


为了能够支持浏览器的后退， 利用到了history的api， 记录下来对应的信息， 

.. code-block:: js

    pjax.state = {
      id: options.id || uniqueId(),
      url: container.url,
      container: context.selector,
      fragment: options.fragment,
      timeout: options.timeout
    }

    if (options.push || options.replace) {
      window.history.replaceState(pjax.state, container.title, container.url)
    }

当浏览器后退的时候， 拦截事件， 根据记录的历史信息， 产生一个新的ajax请求。

.. code-block:: js

    $(window).bind('popstate', function(event){
      var state = event.state
      if (state && state.container) {
        var container = $(state.container)
        if (container.length) {
          ...
          var options = {
            id: state.id,
            url: state.url,
            container: container,
            push: false,
            fragment: state.fragment,
            timeout: state.timeout,
            scrollTo: false
          }
    
          if (contents) {
            // pjax event is deprecated
            $(document).trigger('pjax', [null, options])
            container.trigger('pjax:start', [null, options])
            // end.pjax event is deprecated
            container.trigger('start.pjax', [null, options])
    
            container.html(contents)
            pjax.state = state
    
            container.trigger('pjax:end', [null, options])
            // end.pjax event is deprecated
            container.trigger('end.pjax', [null, options])
          } else {
            $.pjax(options)
          }
          ...
        }
      }
    }

为了支持fallback， 一个是在加载的时候判断浏览器是否支持history push state API：

.. code-block:: js

    // Is pjax supported by this browser?
    $.support.pjax =
      window.history && window.history.pushState && window.history.replaceState
      // pushState isn't reliable on iOS until 5.
      && !navigator.userAgent.match(/((iPod|iPhone|iPad).+\bOS\s+[1-4]|WebApps\/.+CFNetwork)/)

另一个是当发现请求一段时间没有回复的时候（可以设置参数timeout）， 直接做页面跳转。

.. code-block:: js

    options.beforeSend = function(xhr, settings) {
      if (settings.timeout > 0) {
        timeoutTimer = setTimeout(function() {
          if (fire('pjax:timeout', [xhr, options]))
            xhr.abort('timeout')
        }, settings.timeout)
  
        // Clear timeout setting so jquerys internal timeout isn't invoked
        settings.timeout = 0
  

结论
----------------------------
既然都看到这里了， 你为什么不去实际使用一下pjax呢？ 有那么多好处， 我觉得几乎所有网站都应该采用pjax。 赶紧用起来吧！
