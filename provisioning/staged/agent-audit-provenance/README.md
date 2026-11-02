# Agent Audit & Provenance

**Repository:** `PCakes303/agent-audit-provenance`  
**Portfolio position:** 10 / 29 public repositories  
**Maturity:** scaffolding  
**License:** pending review

## Purpose

Provide portable audit-event contracts and a small append-only, hash-chained JSONL prototype for traceability across agent components.

## Initial implementation

- Versioned audit-event JSON Schema.
- Deterministic canonical JSON hashing with SHA-256.
- JSONL append and full-chain verification CLI.
- Fail-closed validation of required event fields and chain integrity.
- Synthetic examples and regression tests.

## License status

The repository's code, documentation, schemas, examples, and other materials do not yet have an approved license decision. No root `LICENSE` file or GitHub license declaration is present. Reuse and redistribution rights must not be assumed; licensing remains pending repository-specific review.

## Quick start

Requires Python 3.10+ and no third-party runtime dependencies.

```bash
python tools/audit_log.py append --log examples/events.jsonl --event examples/event.json
python tools/audit_log.py verify --log examples/events.jsonl
python -m unittest discover -s tests -v
```

The example log is a fixture. Copy it before appending if you want to preserve the baseline example.

## Security boundary

A hash chain detects accidental or unsophisticated modification only when a trusted prior digest is retained independently. It does not authenticate event producers, prove event truth, prevent truncation by itself, provide non-repudiation, encrypt data, or create a trusted timestamp. SHA-256 hashes are integrity links, **not digital signatures**.

Production deployment requires authenticated event ingestion, key management and signatures, externally anchored checkpoints, access controls, retention policy, privacy review, and independent security assessment.
