.PHONY: uv check format test build publish

uv:
	which uv || curl -LsSf https://astral.sh/uv/install.sh | sh
check: uv
	uv tool run ruff check
format: uv
	uv tool run ruff format
test: uv
	uv run -m unittest tests/test_tsv.py
build: test
	rm -rf dist/* build/*
	uv build
publish: build
	uv run --with twine -m twine upload dist/*
