# Entry-level build

Requires Python 3.10+; no third-party dependencies.

```bash
python tools/starter_build.py
python -m unittest discover -s tests -v
```

The starter build checks that the repository's public manifest and minimum safety documentation are present. It does not prove implementation completeness or production readiness.

## Progression

- **Starter:** runnable local checks and a small, inspectable example.
- **Developer:** working feature implementation, fixtures, unit tests, and interface/contract tests.
- **Production:** threat model, security tests, observability, release automation, SBOM/provenance, compatibility policy, and operational runbooks.
