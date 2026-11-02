# ADR 0001: Missing integration evidence remains BLOCKED

- Status: accepted
- Date: 2026-11-02

## Context

The ecosystem contains many declared contract dependencies, but passing local tests does not demonstrate runtime interoperability or production security.

## Decision

The conformance model uses PASS, FAIL and BLOCKED. A missing integration, security gate or evidence artifact is BLOCKED. Only reproducible pinned tests may move a dependency into tested combinations. Reports include limitations and a deterministic digest; no certification claim is made.

## Consequences

- Empty compatibility test matrices remain empty.
- Security gates cannot pass from documentation presence alone.
- No arbitrary repository code execution is included.
- Production certification remains outside this tool's authority.
