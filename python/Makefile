.PHONY: lint

all: lint test clean

lint:
	poetry run black .
	poetry run pylint ./aoc2021 ./tests

test:
	poetry run pytest tests/

clean:
	find . -name "__pycache__" -type d | xargs rm -rf
	find . -name ".pytest_cache" -type d | xargs rm -rf