# Entry-level build

Requires Python 3.10+; no third-party packages are required for the starter checks.

```bash
python tools/starter_build.py
python -m unittest discover -s tests -v
```

The build scans the schema catalog, parses each JSON document, and checks required metadata, Draft 2020-12 dialect declarations, and unique schema IDs. It is a structural check, not a full JSON Schema implementation.

**Next tiers**
- Developer: add a versioned schema and positive/negative example payloads.
- Production: run a conformant Draft 2020-12 validator, compatibility analysis, fuzz/property tests, and signed release attestations.
