# Environment stuff
.PHONY: get-poetry
get-poetry:
        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

.PHONY: createvenv
createvenv:
        python3 -m venv .venv
        poetry run pip3 install --upgrade pip
        poetry run poetry install


# Linters
.PHONY: black
black:
        poetry run black src --check

.PHONY: black!
black!:
        poetry run black src

.PHONY: flake8
flake8:
        poetry run flake8 src

.PHONY: isort
isort:
        poetry run isort src --check

.PHONY: isort!
isort!:
        poetry run isort src

.PHONY: format!
format!: black! isort!
