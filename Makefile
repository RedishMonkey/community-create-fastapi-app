# prevent make from not running a target if a file with the same name exists
.PHONY: run setup activate clean freeze full-clean

run:
	/usr/bin/env python3 run.py


setup:
	/usr/bin/env python -m venv venv
	chmod +x venv/bin/activate
	. venv/bin/activate
	pip install -r requirements.txt
	chmod +x run.py
	
activate:
	@if [ -d "venv" ]; then \
		. venv/bin/activate; \
	else \
		echo "venv directory not found. Please run 'make setup' first."; \
	fi

clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +


freeze:
	@pip freeze > requirements.txt
	@echo "saved freeze to $$PWD/requirements.txt"

full-clean: clean
	@rm -rf venv

