build:
	rm ../blog/* -f
	python build.py
sync:
	hg pull
	hg up
publish: sync build
