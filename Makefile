install:
	python -m venv .venv
	. .venv/bin/activate
	pip install -r requirements.txt

gen:
	python -m PyInstaller --onefile --windowed --add-data "Pr;Pr" main.py