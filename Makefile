.PHONY: test build release pre-release clean

test:
	tox

build:
	python -m build

# Releases are published by GitHub workflow on version tag, these targets are a manual fallback
release: clean build
	twine upload dist/*

pre-release: clean build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
