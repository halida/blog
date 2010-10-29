#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: build
"""
import os, os.path, glob, commands
from docutils.core import publish_parts
from xml.sax.saxutils import escape

target_path = u"../blog/"
res_path = u"build-res/"

DISQUS_INFO = open(os.path.join(res_path, 'disqus.html')).read().encode('utf-8')
HTML_HEADER = open(os.path.join(res_path, 'base.html')).read().decode('utf-8')
RSS_ITEM = open(os.path.join(res_path, 'rss_item.html')).read().decode('utf-8')
RSS_HTML = open(os.path.join(res_path, 'rss.html')).read().decode('utf-8')
INDEX_HTML = HTML_HEADER % {'title': u"网络寻租", 'body': u'%s'}
ARTICLE_HTML = HTML_HEADER % {'title': "%(title)s", 'body': ur'''
<div id="title"><h1>%(title)s</h1></div>
%(content)s
<a href="index.html">回到目录</a>
<div id="comments">%(disqus)s</div>
'''}

def main():
    #获取文件列表
    content = glob.glob('*.rst')
    content = [i.decode('utf-8')
               for i in content 
               if os.path.basename(i)[0] != '_']
    content = [(commands.getoutput((
                    u"hg log -r0:tip -l 1 --template  '{date|isodate}' " + i
                    ).encode('utf-8')), i)
               for i in content]
    content.sort(reverse=True)
    #对于每个文件
    indexs, items = [], []
    for updated, filename in content:
        title = filename.split('.')[0]
        htmlname = title + u'.html'
        #生成html
        content = publish_parts(
            source=open(filename).read(),
            writer_name='html')['html_body']
        content_html = (ARTICLE_HTML % {
                'title': title,
                'content': unicode(content),
                'disqus': DISQUS_INFO,
                }).encode('utf-8')
        open(os.path.join(
                target_path, htmlname).encode('utf-8'),
             'w+').write(content_html)
        indexs.append(u'%s <a href="%s">%s</a>' % (updated, htmlname, title))
        items.append(RSS_ITEM % {'title': title,
                                 'updated': updated,
                                 'content': escape(content.encode('utf-8')).decode('utf-8')})

    #生成index
    open(os.path.join(target_path, 'index.html'),'w+').write(
        (INDEX_HTML % u"\n<br/><br/>".join(indexs)).encode('utf-8'))
    #生成rss
    open(os.path.join(target_path, 'rss'),'w+').write(
        (RSS_HTML % u"\n\n".join(items)).encode('utf-8'))
    
if __name__=="__main__":
    main()
