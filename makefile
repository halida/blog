build:
	rm ../blog/* -f
	python build.py
up:
	hg add 
	hg ci -m "update"
	hg push

down:
	hg pull
	hg up

vps-publish: down build

publish: up
	ssh blog.linjunhalida.com "cd /data/workspace/blog-src/;hg pull;hg up; cd /home/halida/haliblog/;ruby-1.9.2-p180 blog_update.rb"

show: build
	chromium-browser ../blog/index.html

done:
	hg add 
	hg ci -m "edit"
	hg push
