# Roadmap

**Current maturity:** scaffolding  
**Planning rule:** roadmap items are intentions, not claims of implementation.

## Milestone 0 — Repository baseline
- [x] Establish repository identity, purpose, boundaries, dependencies, and security expectations.
- [x] Publish initial manifest, capability declarations, and compatibility placeholder.
- [ ] Add domain-specific specification and acceptance criteria.
- [ ] Add CI validation for metadata and documentation.

## Milestone 1 — Contract definition
- [ ] Define versioned domain interfaces and schemas.
- [ ] Add examples and invalid fixtures.
- [ ] Define compatibility and deprecation behavior.
- [ ] Complete threat model and privacy review.

## Milestone 2 — Reference implementation
- [ ] Implement the smallest useful reference validator or library.
- [ ] Add unit, negative, boundary, and failure-mode tests.
- [ ] Document reproducible local setup and usage.
- [ ] Add CI that runs all validation and tests.

## Milestone 3 — Integration
- [ ] Add contract tests with declared dependencies.
- [ ] Demonstrate at least one real downstream consumer.
- [ ] Review security findings and migration behavior.
- [ ] Publish release provenance and evidence before alpha.

## Open work

Keep the human-readable repository map synchronized with the master registry, add an automated public-entry count/consistency check, and ensure private repository entries never appear in generated public output.
