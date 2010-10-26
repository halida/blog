题目
------------------------------
TopLanguage论坛里有讨论一个面试题目,内容如下:

有个老的手机短信程序，由于当时的手机CPU，内存都很烂。所以这个短信程序只能记住256条短信，多了就删了。

每个短信有个唯一的ID，在0到255之间。当然用户可能自己删短信，现在我们收到了一个新短信，请分配给它一个唯一的ID。说白了，就是请你写一个函数: ::

    byte function(byte* ids);

该函数接受一个ids数组，返回一个可用的ID，由于手机很破，我要求你的程序尽量快，并少用内存。注意：ids是无序的。

Miro的分析在这里: http://www.cnblogs.com/miloyip/archive/2010/08/31/idalloc_clarify.html

我的分析
------------------------------

我觉得,因为短消息发送的频率很低,那么我们不需要考虑取ID和释放ID的响应速度问题,主要问题放在如何节约空间.那么,最节约空间的是按照比特来存储ID是否使用.

还有就是,重新整理了需求,需要提供一个释放和获取ID的接口.

解法
------------------------------

代码如下,没有测过,保证有错::

    #define SIZE_COUNT 256/8
    
    struct manager {
        byte map[SIZE_COUNT];

        byte alloc();
        void dealloc(byte id);
    };
    
    //获取ID    
    byte alloc(){
        for(int i=0; i<SIZE_COUNT; i++){
            byte data = map[i];
            if (data == 255) continue; //全满了

            for(int j=0; j<8; j++){
                if (((data >> j) & 1) == 0) {
                    //got it!
                    data |= 1<<j;
                    return i*8 + j;
                }     
            }
        }
    }

    //释放ID    
    dealloc(byte id){
        map[id/8] &= ~(1<<(id % 8));
    }

结论
------------------------------
上面的解法速度上还是很慢的,如果ID空间长期处于半饱和,那么每次获取都要循环一遍数组,那么效率无法接受,因此要考虑更复杂的链表方式,但是这样一来空间就不会最小了.
