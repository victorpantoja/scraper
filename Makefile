
all: clean

tests:
	@echo "Running tests..."
	@nosetests -s --verbose --with-coverage --cover-package=scraper scraper/tests/*.py
