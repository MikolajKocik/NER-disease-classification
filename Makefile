.PHONY: run check format

# run main app locally
run:
	uvicorn src.api.main:app --reload

# checks linter issues
check:
	mypy src/ model/
	ruff check src/ model/

# auto-formatting
format:
	ruff format src/ model/
