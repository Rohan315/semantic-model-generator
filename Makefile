


check-deps: ## Check if poetry is installed on your system.
	@command -v poetry >/dev/null 2>&1 || { echo >&2 "Poetry is required but it's not installed. Please install Poetry by following the instructions at: https://python-poetry.org/docs/#installation"; exit 1; }
	@command -v pyenv >/dev/null 2>&1 || { echo >&2 "pyenv is recommended for managing Python versions but it's not installed. Install via `brew install pyenv`"; exit 1; }
	@echo "Setting Python version to 3.10 using pyenv."
	@pyenv local 3.10

shell: check-deps ## Get into a poetry shell
	poetry shell

setup: check-deps shell ## Install dependencies into your poetry environment.
	poetry install

# Linting and formatting below.
run_mypy:  ## Run mypy
	mypy --config-file=mypy.ini .

run_flake8:  ## Run flake8
	flake8 --ignore=E203,E501,W503 --exclude=pyvenv,tmp,*_pb2.py,*_pb2.pyi,images/*/src .

check_black:  ## Check to see if files would be updated with black.
    # Exclude pyvenv and all generated protobuf code.
	black --check --exclude="pyvenv|.*_pb2.py|.*_pb2.pyi" .

run_black:  ## Run black to format files.
    # Exclude pyvenv, tmp, and all generated protobuf code.
	black --exclude="pyvenv|tmp|.*_pb2.py|.*_pb2.pyi" .

check_isort:  ## Check if files would be updated with isort.
	isort --profile black --check --skip=pyvenv --skip-glob='*_pb2.py*' .

run_isort:  ## Run isort to update imports.
	isort --profile black --skip=pyvenv --skip=tmp --skip-glob='*_pb2.py*' .


fmt_lint: shell ## lint/fmt in current python environment
	make run_mypy run_black run_isort run_flake8

# Test below
test: shell ## Run tests.
	python -m pytest -vvs semantic_model_generator

test_github_workflow:  ## For use on github workflow.
	python -m pytest -vvs semantic_model_generator

# Release
update-version: ## Bump poetry and github version. TYPE should be `patch` `minor` or `major`
	@echo "Updating Poetry version ($(TYPE)) and creating a Git tag..."
	@poetry version $(TYPE)
	@echo "Version updated to $$VERSION. Update the CHANGELOG.md `make release`"

release: ## Runs the release workflow.
	@VERSION=$$(poetry version -s) && git add pyproject.toml && \
	git add CHANGELOG.md &&  git commit -m "Bump version to $$VERSION" && git tag release/v$$VERSION && \
 	git push && git push --tags

help: ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's