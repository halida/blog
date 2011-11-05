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
	ssh blog.linjunhalida.com "cd blog; hg pull; hg up; cd ../haliblog/; source /home/halida/.bashrc; source /home/halida/.rvm/scripts/rvm; rake update"

show: build
	chromium-browser ../blog/index.html

done:
	hg add 
	hg ci -m "edit"
	hg push
