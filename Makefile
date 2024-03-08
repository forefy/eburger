.PHONY: install
install:
	$(MAKE) uninstall
	pip3 install .

.PHONY: install-poetry
install-poetry:
	$(MAKE) uninstall-poetry
	poetry build
	poetry run pip install .

.PHONY: pytest
pytest:
	pytest -s tests/

.PHONY: uninstall
uninstall:
	pip3 uninstall -y eburger

.PHONY: uninstall-poetry
uninstall-poetry:
	poetry run pip uninstall -y eburger
