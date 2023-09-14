install:
	@poetry install --all-extras --with dev	

lock:
	@poetry lock

run:
	@poetry run python3 main.py

# Use --check to avoid auto format
fmt:
	@poetry run black $(FLAGS) .

mypy:
	@poetry run mypy .

pylint:
	@poetry run pylint src

test:
	@poetry run pytest

check: fmt mypy
	@poetry run prospector --profile prospector.yaml

validate: check
	@poetry run coverage run --source=lib -m pytest && \
	poetry run coverage report -m 
