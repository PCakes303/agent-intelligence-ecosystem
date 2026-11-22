# Python Runtime Support Policy

**Effective:** 2026-11-22  
**Owner:** PCakes303 / MrCakes931  
**Scope:** Public Agent Intelligence Ecosystem repositories with Python-based tooling, validators, libraries, and CI.

## Policy

1. Python 3.10 is no longer an approved active CI runtime. It reached end of life on 2026-10-01 and must not be retained as a supported target for maintained portfolio code.
2. The portfolio's current baseline is Python 3.11 or newer.
3. Matrix-based repositories should validate at least Python 3.11 and 3.12 where their dependencies support both. The project manifest and README must state the actual tested range; do not imply compatibility beyond tested versions.
4. Projects using a single Python 3.12 validation workflow may retain it temporarily. They must describe their narrower validation evidence honestly; do not infer Python 3.11 compatibility from another repository's matrix.
5. Do not add Python 3.13, 3.14, or 3.15 to every repository by default. Add a runtime only after dependency resolution, packaging/build compatibility, tests, and platform support have been checked for that repository.
6. The master staging matrix may exercise additional Python versions as a contract/fixture check. A passing staging job does not automatically certify every package or application repository for that runtime.
7. Revisit this policy at each release cycle and before a Python version reaches end of life. Update CI, package metadata, documentation, and support statements together.

## 2026-11-22 remediation

- Removed Python 3.10 from the CI matrices of 17 repositories.
- The affected matrix now targets Python 3.11 and 3.12.
- Three repositories retain single-version Python 3.12 workflows pending a separate dependency and test-coverage review: agent-policy-engine, agent-identity-trust, and agent-resource-manifest.
- The 17 updated repositories must have successful post-change CI recorded before the runtime remediation is marked complete.
- No blanket Python 3.15 support claim is made.

## Acceptance criteria

- No active maintained CI matrix includes Python 3.10.
- Every Python package's declared minimum and tested CI range are consistent.
- Any single-version workflow is explicitly recorded as a narrower validation scope.
- Newer Python versions are added only with passing repository-specific dependency and test evidence.
- The master portfolio registry and status report match the repository workflows.
