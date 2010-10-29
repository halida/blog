#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: build
"""
import os, os.path, glob

content = glob.glob('*.rst')
content = [i for i in content if os.path.basename(i)[0] != '_']
# create html files
for filename in content:
    newfile = filename.split('.')[0] + '.html'
    os.system("rst2html %s > ../blog/%s" % (filename, newfile))
# create index
HTML = """\
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  </head>

  <body>
  <h1>网络寻租</h1>

  %s

  </body>
</html>
"""
open('../blog/index.html','w+').write(
    HTML % "<br/><br/>".join(
        ['<a href="/blog/%(1)s.html">%(1)s</a>' % \
             {'1': n.split('.')[0]}
         for n in content]
        ))
