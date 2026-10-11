# Keep the virtualenv out of the (Dropbox-synced) source tree
VENV := $(HOME)/.venvs$(CURDIR)/venv
.PHONY: venv test build deploy
venv:
	python3 -m venv $(VENV)
test: venv
	$(VENV)/bin/python -m unittest tests/test_tsv.py
build:
	python3 -m pip install --upgrade build
	python3 -m pip install --upgrade twine
	python3 -m build
deploy: build
	python3 -m twine upload dist/*
