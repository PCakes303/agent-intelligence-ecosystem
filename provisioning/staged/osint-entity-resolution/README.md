# OSINT Entity Resolution

Portfolio ID: entity-resolution  
Maturity: scaffolded public-entity candidate matcher; no identity resolution or graph writes.

Generate bounded, evidence-backed candidate matches among public organizations, software projects, datasets, publications and public registries. Preserve ambiguity and require human review.

## Safety boundary

The initial profile does not resolve real people, private individuals, social accounts, personal identifiers or sensitive attributes. It does not infer identity, build personal profiles, score people or make consequential decisions. It only produces candidate matches between permitted public entity types.

The matcher does not automatically merge entities or assert identity. A score is a heuristic similarity measure, not a calibrated probability. Every candidate remains review-required and must retain evidence references and uncertainty.

## Quick start

Python 3.10+:

    python -m pip install -r requirements-dev.txt
    python -m unittest discover -s tests -v

See docs/RESOLUTION-CONTRACT.md, docs/THREAT-MODEL.md and docs/INTEGRATION-GATES.md.

## Licensing

License selection is pending portfolio review. No license is asserted.
