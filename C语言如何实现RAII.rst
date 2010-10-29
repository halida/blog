资源的获取与释放，C语言里面是要让程序员考虑的，比如 ::

    void work(){
      Buffer b;
      init(b);
      do_sth(b);
      del(&b);
    };

在C++里面，有raii这样很方便的特性，当离开作用域的时候，自动释放资源，如 ::

    void work(){
      Buffer b;
      do_sth(b);
    };

我在想，如何让C支持这样的特性？于是就有了下面这个宏 ::

    #define using(b) \
    for(int i=0; i<2; i++){\
    if (i==0) \
      { init(b); } \
    else \
      { if (i==1) \
        { del(b); \
          break; \
        }; \
      }; 
    void work() {
      Buffer b;
      using(&b)
        printf("working..\n");
      };
    };

edit: 被批了，C就按照C的方式干活，RAII交给C++.
