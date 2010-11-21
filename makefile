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
	ssh server.linjunhalida.com "cd /var/www/django/mysite/;make blog_update"

show: build
	chromium-browser ../blog/index.html

done:
	hg add 
	hg ci -m "edit"
	hg push
