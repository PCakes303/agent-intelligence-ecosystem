# Entry-level build

Requires Python 3.10+ and no third-party packages.

```bash
python tools/starter_build.py
python tools/generate_repository_map.py path/to/repositories.json --output build/repository-map.md
python -m unittest discover -s tests -v
```

The starter build validates the public guide's own manifest and confirms that architecture/onboarding documentation exists. To generate the full public repository map, provide a downloaded copy of the authoritative master registry as the input JSON.

**Next tiers**
- Developer: add onboarding pages and regenerate the public map from the master registry.
- Production: add link checks, registry drift checks, accessibility review, and automated public/private boundary tests.
