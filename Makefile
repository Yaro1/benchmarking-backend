# Installation Instructions:
# 1. Install pre-commit: `pip install pre-commit`
# 2. Install hooks: `pre-commit install`
# 3. Run on all files: `pre-commit run --all-files`

# Makefile for Python Project Setup and Pre-commit Hooks

.PHONY: install install-hooks run-hooks format check clean

# Install project dependencies and development tools
install:
	pip install -r requirements.txt
	pip install pre-commit black mypy flake8 isort

# Install pre-commit hooks
install-hooks:
	pre-commit install

# Run all pre-commit hooks manually
run-hooks:
	pre-commit run --all-files

# Apply formatting using Black and isort
format:
	isort .
	black .

# Check formatting and linting without applying changes
check:
	black --check .
	isort --check-only .
	flake8 .
# mypy .

# Clean Python cache and artifacts
clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .venv
	rm -rf build dist *.egg-info
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete

# Run benchmarks
run:
	python3 generation/backend/generator.py
	python3 generation/dockerfile/generator.py
	python3 generation/benchmark/generator.py
	streamlit run streamlit_app.py

# Usage:
# make install        # Install dependencies and tools
# make install-hooks  # Set up pre-commit hooks
# make run-hooks      # Run all hooks on all files
# make format         # Format the code with Black and isort
# make check          # Check code formatting, linting, and types
# make clean          # Clean up Python caches and artifact
# make run            # Generate all backends, dockerfiles, results for the written functions run streamlit app
