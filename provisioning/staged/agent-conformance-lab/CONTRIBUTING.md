# Contributing

Contributions may improve metadata validation, protocol schemas, fixture tests, security-gate matrices and deterministic report generation. Live cross-repository tests require a separate reviewed runner and isolated environment.

## Development

- Python 3.10+
- Install: python -m pip install -r requirements-dev.txt
- Test: python -m unittest discover -s tests -v

Changes to protocol versions, status semantics, report hashing, dependency compatibility or security gates require positive, negative and boundary tests. Do not label declared dependencies as tested interoperability.
