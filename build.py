#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: build
"""
import os, os.path, glob

content = glob.glob('*.rst')
content = [i for i in content if os.path.basename(i)[0] != '_']
for filename in content:
    newfile = filename.split('.')[0] + '.html'
    os.system("rst2html %s > ../blog/%s" % (filename, newfile))

