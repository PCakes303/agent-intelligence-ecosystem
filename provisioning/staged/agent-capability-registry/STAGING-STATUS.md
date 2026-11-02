# Repository 15 deployment and audit status

**Repository:** [PCakes303/agent-capability-registry](https://github.com/PCakes303/agent-capability-registry)  
**Current code commit:** `dd636dafccad84fcd52e6c8c1e9fc199e38052a1`  
**Current CI:** [Run 41520820882](https://github.com/PCakes303/agent-capability-registry/actions/runs/41520820882) — success on Python 3.10, 3.11 and 3.12  
**Product files:** 20  
**Staging source:** `provisioning/staged/agent-capability-registry/` in the master repository.

## Current deployment record

The public remote is authoritative for current implementation. Exact staging-to-remote path/blob-SHA parity is verified: 20 staged product files, 20 remote product files, zero missing, extra or differing blobs. The STAGING-STATUS.md file is included in this parity comparison.

## Remediation completed

Registered capability declarations are copied into immutable attribute mappings. Match requests are bounded to 128 requirements by default. Policy callback results must be explicit boolean `True`; false, non-boolean and exception outcomes deny candidates.

Capability and Requirement now have normative Draft 2020-12 schemas. CI executes schema/model parity tests for identifier lengths, description and version constraints, attribute key/count/value limits and unknown properties. The pinned development validator is declared in requirements-dev.txt.

## Remaining verification

- Bind capability declarations to Resource Manifest and Schema Registry canonical contracts; pin compatible versions and publish reproducible cross-repository fixtures.
- Connect policy callback to an authenticated policy service; it remains a test/integration seam.
- Verify GitHub private vulnerability reporting/security advisory configuration; SECURITY.md records that no dedicated private reporting address is published.
- Apply and verify GitHub About homepage/topics (description exists).
- Verify branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts.
- Retain pending license status until an explicit repository/artifact licensing decision is approved.

## Maturity and limitations

This remains an experimental process-local registry. Matching is advisory only; it does not authenticate agents, prove capability claims, grant permissions, execute work, verify health or provide distributed discovery/consistency. No release is published.
