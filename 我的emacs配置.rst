每个emacs使用者的配置都是不一样的, 都会根据自己的习惯和喜好来调整. 这里我整理一些对emacs用户调整有帮助的内容, 以及我自己觉得不错的配置.

emacs配置如何管理?
-----------------------
配置多了, 放在.emacs里面不是一回事, 我的解法是, .emacs导入真正放配置的目录, 然后require:

.. code-block:: lisp

    (add-to-list 'load-path (expand-file-name "~/Dropbox/sync/emacs/srcs"))
    (load "main")

main.el是配置的汇总, 配置按照模块和功能分割成不同的文件:

.. code-block:: lisp

    (provide 'main)
    
    ;; requires
    (require 'mylib)
    (require 'template)
    (require 'mypython)
    (require 'mydired)
    (require 'myc)
    (require 'mykeymap)
    (require 'mygtd)
    (require 'top-mode)
    (require 'tabbar)
    (require 'fullscreen)

dropbox是我同步emacs配置的工具, 你也可以用其他网盘工具.

如何绑定自己的键位?
-----------------------
每个emacs用户都会自己设定键位, 不会傻傻地M-x然后输入字符. 
我个人的经验, 绑定键位的指导思想是: 对于显示buffer, 切换buffer之类使用非常频繁的功能, 找一些方便的直接键位来绑定, 比如:

.. code-block:: lisp

    (global-set-key [C-tab] 'other-window)

对于一些其他不是那么频繁, 但是经常要使用的功能, 都可以绑定到间接键位上面. 我发现C-;没有使用, 按起来还很方便, 然后把所有自己定义的功能都加到上面去了:

.. code-block:: lisp

    (global-set-key (kbd "C-; 1") 'gtd)
    (global-set-key (kbd "C-; 2") 'note)
    (global-set-key (kbd "C-; 3") 'scratch)
    (global-set-key (kbd "C-; 4") 'py-shell)
    (global-set-key (kbd "C-; 5") 'woman)
    (global-set-key (kbd "C-; 7") 'twit-follow-recent-tweets)
    (global-set-key (kbd "C-; C-7") 'twit-post)

对于针对某些mode的键位绑定, 只需要改变那个mode的键位就可以了:

.. code-block:: lisp

    (define-key dired-mode-map (kbd "b") 'dired-up-directory)

一定要设置的功能
-----------------------
有些功能是如此的强大, 以至于缺少了他们emacs就不完整了..

- `ido <http://www.emacswiki.org/emacs/InteractivelyDoThings>`_, 如果你发现开启文件和切换buffer输入有点累的话, 用ido来节省输入.

- `auto-complete <http://www.emacswiki.org/emacs/AutoComplete>`_ 自动补全. 这里面的补全方案默认是取当前buffer的词语的, 对于我写python代码来说足够用了. 至于c/c++/java..等我写的时候再配置吧.

.. code-block:: lisp

    (require 'auto-complete)
    (global-auto-complete-mode t)
    ;; 匹配项目不用动手腕啦
    (define-key ac-complete-mode-map "\C-n" 'ac-next)
    (define-key ac-complete-mode-map "\C-p" 'ac-previous)


- 漂亮的配色. color-theme有一堆配色可以选的.

.. code-block:: lisp

    (require 'color-theme)
    (color-theme-arjen)

还有一些零散的配置, 都放在 `main.el <http://bitbucket.org/linjunhalida/emacs/src/tip/srcs/main.el>`_ 里面.

- template 模板系统. 写东西怎么不能用模板呢. 一遍遍地输入同样的东西多烦. 我用的是 `template.el <http://bitbucket.org/linjunhalida/emacs/src/tip/srcs/template.el>`_, 不过感觉用的不是很熟, 还要改改.

- `org-mode <http://orgmode.org/>`_. 用来写notes/todo/gtd的. 看看吧, 功能强大.


其他有价值的东西
-----------------------

- shell-command功能. 可以在buffer当前目录执行命令. 如果不想它卡死的话, 可以在命令后面加&(linux). 
- `artist-mode <http://www.lysator.liu.se/~tab/artist/>`_, 可以在emacs里面画图. `artist-mode视频介绍 <http://www.cinsk.org/emacs/emacs-artist.html>`_
- 半透明. linux下面要开启特效才能半透明.

.. code-block:: lisp

    (set-frame-parameter (selected-frame) 'alpha '(80 50))
    (add-to-list 'default-frame-alist '(alpha 80 50))

- `全屏 <http://www.emacswiki.org/emacs/FullScreen>`_, 不全屏怎么对得起emacs呢?

资源
-----------------------

emacs自带的info文档已经很多了, 不过有一些其他地方的资源不错, 值得提一下:

- `emacs wiki <http://www.emacswiki.org/>`_, 我想emacs用户都应该知道这里吧.
- `我的配置 <http://bitbucket.org/linjunhalida/emacs>`_, 好吧, 分享下.
