build:
	rm ../blog/*
	python build.py
sync:
	hg pull
	hg up
publish: sync build
