# Component Audit — intelligence-knowledge-graph — 2026-11-02

**Repository:** [PCakes303/intelligence-knowledge-graph](https://github.com/PCakes303/intelligence-knowledge-graph)  
**Audited implementation commit:** `80bd60e153a49092f1630c64be7643175ba7a3db`  
**Baseline CI:** [Run 41497020106](https://github.com/PCakes303/intelligence-knowledge-graph/actions/runs/41497020106) — success; Python 3.10, 3.11 and 3.12 matrix  
**Documentation remediation commits:** `f5e056d3509d65d5e8d37a2d6cefed9c0c788d97`, `65a1c9977813a0982f935381db0f633ee68919d7`, `fde80de438257708b60cdf68fa21585947f22b2b`  
**Latest documentation CI:** [Run 41500500319](https://github.com/PCakes303/intelligence-knowledge-graph/actions/runs/41500500319) — success  
**Disposition:** **BLOCKED**  
**Maturity:** Experimental provenance-aware in-memory graph model and validator; no collection, identity resolution, inference, truth verification, or consequential decision service.

## Verified implementation

- Typed source, evidence and entity nodes; directed edges require evidence references, bounded confidence, explicit uncertainty and timezone-aware timestamps.
- Strict node/edge field validation, bounded identifiers/labels/metadata, HTTPS source URLs without embedded credentials, SHA-256 evidence digest syntax and reference integrity.
- Graph construction snapshots and validates direct node/edge inputs, exposes read-only mappings, checks node/edge capacity and serializes deterministically.
- CLI validates JSON with duplicate-key/nonstandard-number rejection, a 64 MiB input ceiling, Draft 2020-12 schema validation and reference-model validation.
- Query API validates direction and query bounds; `find_paths` caps depth at 12 and returned paths at 1,000.
- CI runs schema and reference implementation tests plus synthetic graph validation on Python 3.10, 3.11 and 3.12. Run 41497020106 passed after the recent input and model hardening.
- Capabilities accurately describe document validation, provenance model, deterministic serialization and bounded path queries. Compatibility metadata correctly leaves OSINT Evidence and Entity Resolution declared-only.
- README and documentation state that this is a graph data model, not a collection, scraping, identity-resolution, inference, truth-verification or decision system. Synthetic fixtures only.
- License remains pending review; no license was added.

## Corrections and staging work

- `f5e056d3509d65d5e8d37a2d6cefed9c0c788d97`: attempted removal of stale portfolio position; this commit was a no-op because trailing whitespace prevented the exact match.
- `65a1c9977813a0982f935381db0f633ee68919d7`: updated SECURITY.md to disclose that no dedicated private reporting address is published and clarified graph trust limitations.
- `fde80de438257708b60cdf68fa21585947f22b2b`: successfully removed the stale `23 / 29` portfolio-position line.
- Refreshed the master staging packet from the live remote after detecting drift across the CI workflow, SECURITY.md, graph/query code, requirements, schema, validator and tests. Current parity: **29 staged product files vs 29 remote product files; zero missing, extra or differing Git blob hashes**. `STAGING-STATUS.md` is retained as administrative evidence and excluded from product-file parity.
- Updated both remote and master-staged `STAGING-STATUS.md` with current parity evidence.
- Created [issue #1](https://github.com/PCakes303/intelligence-knowledge-graph/issues/1) for bounded query work, schema/model parity, About metadata and repository settings.

## Post-audit path-query work-budget hardening — 2026-11-02

The earlier audit identified that the path query bounded depth and returned paths but did not bound the intermediate queue, node expansions or total edge scans. This allowed combinatorial work before the result limit was reached.

- b96da59ffcc36ba05587519b928435ec38276f3e: builds one deterministic outgoing adjacency index per query and enforces explicit expansion (default 10,000; hard max 100,000), queue (default 10,000; hard max 100,000) and edge-scan (default 100,000; hard max 500,000) budgets in addition to depth/result limits. Budget exhaustion raises ValueError.
- 67678de1716e2a414a87696194718f319abf605c: adds four tests for expansion, queue, edge-scan and invalid work-budget boundaries.
- 086f5d21944b6bc7eabe6ce2f5f416579f0e4df0 and 745f94b4198cd76f0ada793915ba51ecb633e89f: document the work budgets in the graph contract and capability metadata.
- [CI run 41505793639](https://github.com/PCakes303/intelligence-knowledge-graph/actions/runs/41505793639) passed the unit tests and synthetic graph validator on Python 3.10, 3.11 and 3.12. The current test suite contains 38 tests.
- 381e1554bf294684db775d0d74242a3920e9f692: updated staging-status evidence; staging must be refreshed from the latest remote product files and parity rechecked.

The query work-budget finding is remediated in the reference implementation. The overall repository remains BLOCKED due to schema/model parity, metadata/security governance and absent upstream integration.

## Findings and remaining exceptions

1. **Blocking path-query work bound:** `find_paths` limits depth and number of returned paths, but does not cap queue size, node expansions or total edge scans. In a dense/high-branching graph, candidate path enumeration can grow combinatorially before the result limit is reached. `neighbors` rescans and sorts the entire edge set for each expansion. Add an explicit work/expansion budget and preferably an adjacency index, with adversarial dense-graph tests.
2. **Schema/model parity gap:** the CLI applies schema then model validation, but direct `Node.from_dict` / `KnowledgeGraph.from_dict` calls do not execute the schema. Some constraints differ: e.g. `entity_record_id` is pattern-constrained in the schema but the model only checks non-empty length; source URL schema format allows forms such as credential-bearing HTTPS URIs that the model rejects. Add a comprehensive parity matrix and enforce the same normative contract in direct APIs.
3. **Private reporting route unverified:** SECURITY.md now states that no dedicated private address is published. Verify GitHub private vulnerability reporting/security advisories or configure an owner-approved private route.
4. **GitHub About metadata incomplete:** live description, homepage and topics are empty. Apply and verify actual About settings.
5. **License pending:** no root LICENSE file or GitHub license declaration was observed. Reuse/redistribution rights must not be assumed.
6. **Administration controls unverified:** branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed through the available integration.
7. **No upstream integration:** OSINT Evidence and Entity Resolution remain planned/not-created upstream dependencies; no cross-repository tested combinations exist.

## Acceptance to clear BLOCKED

- Bound path-query queue/expansion/edge-scan work and add dense-graph adversarial tests.
- Align direct model APIs and schema constraints; add positive/negative parity tests across all node and edge fields.
- Verify private vulnerability reporting, About metadata and repository administration controls.
- Keep licensing pending until explicitly approved.
- Build reproducible integration fixtures after upstream evidence and entity-resolution contracts exist.

A passing three-version CI matrix validates the current tests and synthetic graph. It does not establish source authenticity, evidence truth, identity resolution, analytic correctness, or production readiness.
