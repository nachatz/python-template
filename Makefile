install:
	@poetry install --all-extras --with dev
	poetry lock

lock:
	@poetry lock

run:
	poetry run python examples/main.py

# Use --check to avoid auto format
fmt:
	@poetry run black src tests

mypy:
	@poetry run mypy src tests

check: fmt mypy
	@poetry run prospector --profile prospector.yaml

validate: check
	@poetry run coverage run --source=src -m pytest && \
	poetry run coverage report -m 
