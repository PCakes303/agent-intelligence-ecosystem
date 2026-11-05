# Entry-level build

This is the first runnable milestone for contributors. It needs Python 3.10+ and no third-party packages.

```bash
python tools/starter_build.py
python -m unittest discover -s tests -v
```

The starter build loads the normative requirements catalog and runs its structural validator. A successful run proves only that the catalog satisfies the repository's current checks; it does not certify downstream systems.

**Next tiers**
- Developer: add a requirement with a stable ID, rationale, acceptance criteria, and linked test.
- Production: add traceability reports, schema-conformant validation, change-impact checks, and reviewed release evidence.
