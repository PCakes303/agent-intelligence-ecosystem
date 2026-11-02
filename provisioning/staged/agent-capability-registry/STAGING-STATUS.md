# Repository 15 deployment status

Public repository created and verified: https://github.com/PCakes303/agent-capability-registry (default branch `main`). All 20 product files have been deployed and staging parity refreshed. Latest code commit: https://github.com/PCakes303/agent-capability-registry/commit/dd636dafccad84fcd52e6c8c1e9fc199e38052a1. CI passed on Python 3.10, 3.11 and 3.12: https://github.com/PCakes303/agent-capability-registry/actions/runs/41520820882.

The implementation includes strict capability declaration validation, a bounded process-local registry, exact-match requirement filters, same-agent coverage for multi-capability requests, deterministic results, and a fail-closed policy callback. Both Capability and Requirement now have normative Draft 2020-12 schemas, and model/schema boundary tests cover identifiers, description, version, attribute keys/counts/values and unknown properties. The development dependency is pinned in requirements-dev.txt.

Matching is advisory; declarations are not attestations, and the callback is not a production authorization service.

Not included: cryptographic attestation, identity lifecycle integration, production policy adapter, distributed storage, network APIs, health/reputation scoring, execution scheduling, or cross-repository conformance. Dependency states remain `declared`, not `tested`. No GitHub Release is published. License selection remains pending review. Private vulnerability reporting, GitHub About metadata and repository administration settings remain unverified.

Next gates: add schema-registry, resource-manifest and policy-engine integration fixtures; add authenticated reviewer/issuer evidence and signed capability attestations; define package metadata and release criteria.
