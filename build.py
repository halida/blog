#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: build
"""
import os, os.path, glob
from docutils.core import publish_parts

target_path = u"../blog/"

HTML_HEADER = u"""\
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head>
<body>
%s
</body></html>
"""
INDEX_HTML = HTML_HEADER % u"<h1>网络寻租</h1>\n%s"
ARTICLE_HTML = HTML_HEADER % u"""\
<h1>%(title)s</h1>
%(content)s
<hr/>
<div id="disqus_thread"></div>
<script type="text/javascript">
  /**
    * var disqus_identifier; [Optional but recommended: Define a unique identifier (e.g. post id or slug) for this thread] 
    */
  (function() {
   var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
   dsq.src = 'http://halidasvps.disqus.com/embed.js';
   (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
  })();
</script>
<noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript=halidasvps">comments powered by Disqus.</a></noscript>
<a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>

<script type="text/javascript">
var disqus_shortname = 'halidasvps';
(function () {
  var s = document.createElement('script'); s.async = true;
  s.src = 'http://disqus.com/forums/halidasvps/count.js';
  (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
}());
</script>

<hr/>
<a href="index.html">回到目录</a>
"""

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
