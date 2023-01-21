SHELL = /bin/bash

# Environment
venv:
	python3 -m venv python_project_template_env
	source python_project_template_env/bin/activate && \
	python3 -m pip install pip setuptools wheel && \
	python3 -m pip install --upgrade pip && \
	python3 -m pip install -e .[dev] && \
	pre-commit install


# Style
style:
	black .
	flake8 python_project_template/
	python3 -m isort -rc python_project_template/

# Test
test:
	python3 -m flake8 ./python_project_template ./tests
	python3 -m mypy ./python_project_template ./tests
	# https://stackoverflow.com/a/55095253
	python -m pytest -s --durations=0 --disable-warnings ./python_project_template/ tests/
