.PHONY: clean-pyc test release upload-docs docs

all: clean-pyc test

test-old:
	python run-tests.py OldSecureCookieSessionInterface

test-upgrade:
	python run-tests.py UpgradingSessionInterface

test: test-old test-upgrade

release:
	python setup.py sdist upload

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

upload-docs:
	python setup.py upload_docs

docs:
	$(MAKE) -C docs html
