VENV = ./venv
PYTHON = $(VENV)/bin/python
FASTAPI = $(VENV)/bin/fastapi
PIP = $(VENV)/bin/pip

.PHONY: venv install run clean

venv:
	python3 -m venv $(VENV)

install: venv
	$(PIP) install -r requirements.txt

run:
	$(FASTAPI) dev main.py

clean:
	rm -rf $(VENV)

