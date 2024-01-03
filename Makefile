.PHONY: install
install:
	$(MAKE) uninstall
	pip3 install .

.PHONY: install-local
install-local:
	$(MAKE) uninstall-local
	poetry build
	pip install dist/eburger-0.1.0-py3-none-any.whl
	eburger -h

.PHONY: test
test:
	pytest -s

.PHONY: uninstall
uninstall:
	pip3 uninstall -y eburger

.PHONY: uninstall-local
uninstall-local:
	poetry run pip uninstall -y eburger
