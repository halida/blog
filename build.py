#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: build
"""
import os, os.path, glob
from docutils.core import publish_parts

target_path = u"../blog/"
res_path = u"build-res/"

HTML_HEADER = open(os.path.join(res_path, 'base.html')).read().encode('utf-8')
INDEX_HTML = HTML_HEADER % u"<h1>网络寻租</h1>\n%s"
ARTICLE_HTML = HTML_HEADER % u"""\
<h1>%(title)s</h1>
%(content)s
<hr/>%(disqus)s
<hr/><a href="index.html">回到目录</a>
"""
DISQUS_INFO = open(os.path.join(res_path, 'disqus.html')).read().encode('utf-8')

def main():
    #获取文件列表
    content = glob.glob('*.rst')
    content = [i.decode('utf-8')
               for i in content 
               if os.path.basename(i)[0] != '_']
    content.sort()
    #对于每个文件
    indexs = []
    for filename in content:
        title = filename.split('.')[0]
        htmlname = title + u'.html'
        #生成html
        content = publish_parts(
            source=open(filename).read(),
            writer_name='html')['html_body']
        content = (ARTICLE_HTML % {
                'title': title,
                'content': unicode(content),
                'disqus': DISQUS_INFO,
                }).encode('utf-8')
        open(os.path.join(
                target_path, htmlname).encode('utf-8'),
             'w+').write(content)
        indexs.append(u'<a href="%s#disqus_thread">%s</a>' % (htmlname, title))
    #生成index
    open(os.path.join(target_path, 'index.html'),'w+').write(
        (INDEX_HTML % u"\n<br/><br/>".join(indexs)).encode('utf-8'))

if __name__=="__main__":
    main()
