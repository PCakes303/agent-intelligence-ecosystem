.PHONY: starter test validate-registry validate-foundation
starter:
	python tools/starter_build.py
test:
	python -m unittest discover -s tests -v
validate-registry:
	python tools/validate_registry.py
validate-foundation:
	python tools/validate_foundation_requirements.py
