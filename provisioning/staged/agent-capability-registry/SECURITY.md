# Security Policy

This repository is an experimental, process-local capability catalog and advisory matcher. It is not an authentication, authorization, execution, or capability-attestation security boundary.

## Reporting

Do not publish exploitable vulnerabilities, credentials, tokens, or sensitive agent data in public issues. Use GitHub private vulnerability reporting or a private security advisory if enabled for this repository. A dedicated private reporting address is not published here; if private reporting is unavailable, the owner must configure an owner-approved private channel before production use.

## Trust and data handling

- Capability declarations are untrusted claims, not evidence that an agent can perform a capability safely or correctly.
- The policy callback is an integration seam. Only explicit boolean `True` accepts a candidate; missing, false, non-boolean or raising callbacks deny.
- Registered declarations are snapshotted with immutable attribute mappings so caller mutation cannot alter validated registry state.
- Match requests are bounded (128 requirements by default); declaration attributes and registry entries are bounded by the local contract.
- The index is in-memory and process-local. It does not provide authenticated discovery, distributed consistency, execution isolation, or durable audit.
