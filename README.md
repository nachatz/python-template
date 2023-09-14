# Python Template

This is a Python project template that provides a starting point for building Python applications with essential development tools such as tests, linting, formatting, coverage, and CI/CD setup using Poetry to manage dependencies.

## Getting Started

To use this template for your Python project, follow these steps:

1. Clone the repository to your local machine:

```bash
   git clone https://github.com/nachatz/python-template.git
```

2. Evaluate and set your initial dependencies

Navigate to the `pyproject.toml` and update all of the metadata for your usecase (no version changes yet).

Run `make install` and `make lock`

3. Run the sample code

`make run`

4. Update for your usecase

Navigate to the `pyproject.toml` and update all of the versions you need. It's highly recommended to utilize Poetry's API for this.

`poetry add <PACKAGE>`
`poetry remove <PACKAGE>`

Add any technology you only will use as a developer into the `dev` group to prevent it being packaged in release.

## Make commands

This project includes a set of make commands to help you manage your development tasks. Here are the available commands:


- `make install`: Install project dependencies, including development extras.

- `make lock`: Lock project dependencies using Poetry.

- `make fmt`: Format code using Black. Use the FLAGS variable to pass additional formatting options. Example: make fmt FLAGS="--exclude some_folder".

- `make mypy`: Run MyPy type checking.

- `make pylint`: Run pylint for code analysis.

- `make test`: Run pytest for testing.

- `make check`: Run formatting and type checking (fmt and mypy).

- `make validate`: Run full validation, including checks, tests, and coverage.