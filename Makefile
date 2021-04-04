createvenv:
	python3 -m venv .venv
	poetry run pip3 install --upgrade pip
	poetry run poetry install

format:
	poetry run black
	poetry run isort
