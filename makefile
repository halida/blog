build:
	rm ../blog/* -f
	python build.py
sync:
	hg pull
	hg up
publish: sync build

vps: build
	scp -r ../blog vps.linjunhalida.com:/var/www/
