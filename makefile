build:
	rm ../blog/* -f
	python build.py
up:
	hg push

down:
	hg pull
	hg up

vps-publish: down build

publish: up
	ssh vps.linjunhalida.com "cd /var/www/blog-src/;make publish"

show: build
	chromium-browser ../blog/index.html