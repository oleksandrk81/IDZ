install:
	pip install -r requirements.txt

test:
	pytest --doctest-modules main.py test_main.py

lint:
	ruff check .

security:
	safety check

all: install lint test security