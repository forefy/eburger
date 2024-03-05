.PHONY: install
install:
	$(MAKE) uninstall
	pip3 install .

.PHONY: install-local
install-local:
	$(MAKE) uninstall-local
	poetry build
	poetry run pip install eburger

.PHONY: pytest
pytest:
	pytest -s tests/

.PHONY: uninstall
uninstall:
	pip3 uninstall -y eburger

.PHONY: uninstall-local
uninstall-local:
	poetry run pip uninstall -y eburger
