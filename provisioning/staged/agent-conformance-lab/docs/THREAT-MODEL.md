# Threat Model

## Assets

- Contract and protocol schema correctness.
- Pinned subject/dependency versions.
- Test result integrity and report provenance.
- Accurate security-gate status and limitations.

## Threats and controls

| Threat | Reference control | Remaining requirement |
|---|---|---|
| Declared dependency presented as compatible | Empty tested-combinations list and explicit report limitations | Reproducible pinned integration tests |
| Untrusted code execution | No arbitrary code runner | Isolated execution environment for future lab |
| Forged test evidence | Evidence references and report digest | Authenticated runner, signed attestations and external provenance |
| Missing safety gate hidden | PASS/FAIL/BLOCKED semantics and mandatory gate matrix | Actual integration evidence |
| Schema drift | Versioned local schemas and fixtures | Cross-repository schema compatibility tests |
| Report tampering | SHA-256 report digest | Digital signatures and trusted storage |
| Resource exhaustion | Fixture sizes and report counts bounded by schemas | Service-level quotas and isolated runner |

## Non-goals

No production security certification, legal compliance certification, live network interoperability, swarm benchmarking, arbitrary code execution or independent audit opinion.
