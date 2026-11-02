# Conformance Contract v1.0

## Scope

The first implementation validates repository metadata consistency, synthetic AIX message envelopes and conformance report integrity. It does not execute repository code or perform live interoperability tests.

## Status semantics

- PASS: the named local check ran and its supplied evidence supports the defined result.
- FAIL: the check ran and found a contract violation.
- BLOCKED: required integration evidence or execution was unavailable.

A suite with no checks is BLOCKED. Any FAIL makes the overall report FAIL; otherwise any BLOCKED makes it BLOCKED; only all-PASS checks produce PASS.

## Report requirements

Each report pins a subject repository and commit, generated timestamp, check IDs, status, evidence references, limitations and a deterministic SHA-256 digest. The digest detects report-byte changes but does not authenticate the author or prove that supplied test evidence is true.

## Compatibility semantics

A dependency declaration is not a tested combination. Interoperability is established only by reproducible tests using pinned artifacts, protocol versions, explicit expected outcomes and recorded evidence. Current staging tests are local synthetic tests only.
