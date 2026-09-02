.PHONY: run check format

# run main app locally
run:
	uvicorn src.api.main:app --reload

# checks linter issues
check:
	mypy src/
	ruff check src/

# auto-formatting
format:
	ruff format src/
