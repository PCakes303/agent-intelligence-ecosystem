# Mandatory Security and Governance Gates

Every agent, adapter, swarm or federation conformance profile must include the following gates:

| Gate | Required evidence | Missing evidence status |
|---|---|---|
| Identity and revocation | Authenticated principal, role, credential lifecycle and revocation tests | BLOCKED |
| Policy enforcement | Allow/deny, scope and policy-outage tests | BLOCKED |
| Audit provenance | Attributable event, integrity and failure-path tests | BLOCKED |
| Emergency control | STOP propagation, acknowledgement, monotonic state and resume quorum tests | BLOCKED |
| Compliance governance | Counsel-reviewed applicability, control mapping and evidence references | BLOCKED |
| Secure supply chain | Pinned dependencies, provenance, vulnerability and artifact verification | BLOCKED |
| Runtime isolation | OS-level sandbox and network/resource-boundary evidence | BLOCKED for privileged execution |

A repository's presence of a SECURITY.md file or a passing unit test does not satisfy a gate. Each gate requires actual evidence and a defined scope. No production certification is issued by this lab.
