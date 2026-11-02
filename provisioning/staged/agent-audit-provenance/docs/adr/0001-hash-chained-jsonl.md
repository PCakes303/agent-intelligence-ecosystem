# ADR 0001: Initial hash-chained JSONL format

- **Status:** accepted for experimental scaffold
- **Decision:** use one UTF-8 JSON object per line, canonical JSON hashing, and SHA-256 previous-hash links.
- **Rationale:** small, inspectable, dependency-free format with deterministic verification.
- **Consequences:** chain integrity is locally checkable, but producer authenticity and completeness are not established. External checkpoints and signatures remain future work.
