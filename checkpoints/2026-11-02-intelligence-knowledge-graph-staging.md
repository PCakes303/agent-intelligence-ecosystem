# Intelligence Knowledge Graph — Staging Checkpoint

**Date:** 2026-11-02  
**Portfolio position:** 23 / 29 public repositories  
**Technical sequence:** Repository 20  
**Target:** `PCakes303/intelligence-knowledge-graph`  
**Standalone remote:** Not yet created  
**Status:** 29-file implementation staged in master; deployment and CI pending

## Scope staged

- Provenance-aware graph contract v0.1.0.
- Source, evidence, and entity node records.
- Directed relationship edges with mandatory evidence references, confidence bounds, uncertainty, and timestamps.
- Evidence-to-source and edge-to-evidence referential-integrity checks.
- Deterministic graph serialization.
- Read-only adjacency and bounded path query helpers.
- JSON graph schema, synthetic fixture, validation CLI, unit tests, and Python 3.10–3.12 CI workflow.
- Security, contribution, support, roadmap, compatibility, capability, and AI-discovery metadata.

## Master staging location

`provisioning/staged/intelligence-knowledge-graph/`

## Dependencies

- `osint-evidence` — evidence record and provenance contract.
- `entity-resolution` — entity and relationship-resolution contract.

These dependencies are declared in the master registry. Their standalone repositories are not yet verified, so no production adapters have been implemented.

## Verification state

- [x] 29 staged files present in master.
- [x] Staging status and master portfolio updated.
- [x] Node metadata round-trip preservation correction committed.
- [ ] Standalone remote created.
- [ ] Files deployed and compared against staging.
- [ ] Unit tests and validator executed in remote CI.
- [ ] Python 3.10, 3.11, and 3.12 matrix green.

## Important boundaries

This is an experimental graph model, not a collector, scraper, identity resolver, inference engine, or truth-verification system. It uses synthetic fixtures only. A relationship edge is a sourced assertion with explicit uncertainty, not ground truth. The prototype does not provide authentication, authorization, encryption, signatures, persistent storage, or access control.

**Next action:** create the empty public repository `PCakes303/intelligence-knowledge-graph`, then publish the staged packet and verify CI before any upstream adapters are added.
