# -*- coding: utf-8 -*-
BLOG_DIR = "."
TARGET_DIR = "/data/workspace/octopress/"

FORMAT = """
---
layout: post
title: ""%{title}""
date: %{created}
comments: true
categories: 
---
"""

maped_title = File.open("#{BLOG_DIR}/name_map.txt").read().split("\n").map{|line| line.split}
maped_title = Hash[maped_title]
MAPED_TITLE = maped_title

# 把文档rst变成markdown， 交给octopress用
def move
  # 更新
  `git pull`

  Dir.chdir BLOG_DIR

  # 获取列表
  lists = Dir.glob('*.rst')
  # # 不获取临时文件(_开头)
  # lists.reject!{|file| File.basename(file)[0] == '_'}

  # 生成时间, 文件名列表
  infos = lists.map do |file|
    [
     # created
     %x{git log --format=%ai "#{file}"| tail -1},
     # updated
     %x{git log --format=%ai "#{file}"| head -1},
     File.basename(file, '.rst')
    ]
  end

  # 按时间排序
  infos.sort!

  #生成新的文件
  infos.each do |created, updated, title|
    cmd = %{cat "#{title}.rst"| pandoc  -f rst -t markdown}
    text = `#{cmd}`
    # code
    text = text.strip
      .gsub(/~~~~ {\.sourceCode .([^\}]+)}/, '```\1')
      .gsub(/~~~~/, "```")
      .gsub("```lisp", "```")
    # first line image need a space
    text.sub!(/\n/, "\n\n") if text.start_with? "![image]"

    header = FORMAT % {title: title, created: created}
    target = title.start_with?("_") ? "#{TARGET_DIR}/t" : "#{TARGET_DIR}/source/_posts"
    File.open("#{target}/#{created.split[0]}-#{MAPED_TITLE[title]}.markdown", "w+").write("#{header}\n#{text}")
  end  
end

move()
