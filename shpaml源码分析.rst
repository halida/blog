在上次已经 `介绍过shpaml <http://server.linjunhalida.com/blog/article/shpaml%E4%BB%8B%E7%BB%8D/>`_, 
它的代码总共只有365行, 既然这么一点代码, 没有理由不分析分析它的具体实现.

首先, 代码可以在这里看到: http://shpaml.webfactional.com/source_code

首先是入口出的代码:

.. code-block:: python

    if __name__ == "__main__":
        # if file name is given convert file, else convert stdin
        import sys
        if len(sys.argv) == 2:
            shpaml_text = open(sys.argv[1]).read()
        else:
            shpaml_text = sys.stdin.read()
        sys.stdout.write(convert_text(shpaml_text))

这里面是实现以下3种语法的功能, 太简单就不说了:

    python -c "import shpaml; shpaml.convert_text()"
    echo 'b | foo' | python shpaml.py
    touch test.shpaml; python shpaml.py test.shpaml

然后, 从convert_text函数, 一直深入调用到了indent_lines函数(外面的几层都是包装), 这个才是重心.

我们知道, html是树状的, 输入的shpaml格式的文档本质上也是树状的.
我们需要把shpaml按照树状的方式解析出来, 同时对分析出来的数据做处理(加<>以及结尾加</tag>).

简单地介绍下代码里面的处理方式. 程序内嵌一个recurse函数, 这个函数的输入是字符串列表(就是需要转换的文本啦), 处理文本的时候如果发现有新的子树, 就会嵌套调用recurse, 用函数调用栈的方式来遍历tag树.
每次处理文本, 都会把生成的文本放到output这个字符串列表里面去. 
下面是具体的代码:

.. code-block:: python

    def indent_lines(lines,
                output,
                branch_method,
                leaf_method,
                pass_syntax,
                flush_left_syntax,
                flush_left_empty_line,
                indentation_method,
                get_block,
                ):
        """Returns None.
        一堆注释不管它
        """
        append = output.append
        # 递归调用函数
        def recurse(prefix_lines):
            # 循环解析传进来的字符串列表
            while prefix_lines:
                # 列表已经处理过了, 分割成空格的前缀和后面的字符
                prefix, line = prefix_lines[0]
                if line == '':
                    prefix_lines.pop(0)
                    append('')
                    continue
                # 我们看看这一行是否有缩进
                block_size = get_block(prefix_lines)
                if block_size == 1:
                    # 如果没有缩进, 就根据状况来处理
                    prefix_lines.pop(0)
                    if line == pass_syntax:
                        pass
                    elif line.startswith(flush_left_syntax):
                        append(line[len(flush_left_syntax):])
                    elif line.startswith(flush_left_empty_line):
                        append('')
                    else:
                        append(prefix + leaf_method(line))
                else:
                    # 如果是一个新的缩进, 我们需要找到缩进的结尾, 然后把这一块数据取出来, 
                    # 让branch_method处理下来
                    block = prefix_lines[:block_size]
                    prefix_lines = prefix_lines[block_size:]
                    branch_method(output, block, recurse)
                # 循环消耗prefix_lines, 直到消耗完毕, 任务就完成了.
            return
        prefix_lines = list(map(indentation_method, lines))
        recurse(prefix_lines)


recurse 最后会进入到2个函数里面去, 一个是leaft_method, 它处理单行的一些语法, 比如: tag > tag2 > tag3 | text, 也是采用上面那种循环消耗字符串的方法. 这里略过不表. 

另一个就是branch_method, 这里面的值是函数html_block_tag. 它里面是处理缩进后的一些语法. 处理完头部之后, 会把缩进里面的内容传给recurse函数, 就这样一步步解析玩子树.
里面的append函数就把解析玩的内容传给output, 最后打印成html代码.

.. code-block:: python

def html_block_tag(output, block, recurse):
    append = output.append
    prefix, tag = block[0]
    if RAW_HTML.regex.match(tag):
        # 如果是html代码(<开头)就不解析头部
        append(prefix + tag)
        # 解析子树
        recurse(block[1:])
    elif COMMENT_SYNTAX.match(tag):
        # 注释..
        pass
    elif VERBATIM_SYNTAX.match(tag):
        # 子树不解析, 直接打印出来
        m = VERBATIM_SYNTAX.match(tag)
        tag = m.group(1).rstrip()
        start_tag, end_tag = apply_jquery_sugar(tag)
        append(prefix + start_tag)
        stream(append, block[1:])
        append(prefix + end_tag)
    else:
        # 普通的状况, 解析出tag
        start_tag, end_tag = apply_jquery_sugar(tag)
        # 输出tag头
        append(prefix + start_tag)
        # 解析子树
        recurse(block[1:])
        # 输出tag尾
        append(prefix + end_tag)


结论
---------------------
shpaml采用函数嵌套调用的方法来解析和处理树状结构, 这个也是通常用的解析树状结构的方法(如果树状结构嵌套不多的话), 对于编程语法的解析, 也可以采用类似这样的方式, 对于每一个语法规则都有一个函数, 然后嵌套调用解析, 直到解析完毕. 
