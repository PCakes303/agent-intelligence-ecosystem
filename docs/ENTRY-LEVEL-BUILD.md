# Entry-level build

The master repository has a reproducible first build for contributors. It requires Python 3.10+ and the packages in `requirements-dev.txt`.

```bash
python -m pip install -r requirements-dev.txt
python tools/starter_build.py
```

The starter build validates the public repository registry and dependency graph, validates foundation requirements, then runs the repository test suite. It does not provision repositories, publish releases, access the private operations repository, or claim that planned components are implemented.

**Next tiers**
- Developer: update one contract and add traceable unit/contract tests.
- Production: run cross-repository compatibility, security, SBOM/provenance, release-signing, and reviewed synchronization checks.
