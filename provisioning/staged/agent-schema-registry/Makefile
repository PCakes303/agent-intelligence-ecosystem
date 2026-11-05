.PHONY: starter test validate
starter:
	python tools/starter_build.py
test:
	python -m unittest discover -s tests -v
validate:
	python tools/check_schema_catalog.py
