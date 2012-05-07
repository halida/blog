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
	ssh linjunhalida.com "cd blog; git pull; cd ../haliblog-middleman/; ruby blog_update.rb; bundle exec middleman build; cp build/* /var/www/nginx-default -rf"

show: build
	chromium-browser ../blog/index.html

done:
	hg add 
	hg ci -m "edit"
	hg push
