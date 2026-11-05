# Security Policy

## Scope
This public repository provides human-facing navigation and onboarding only. It is not the canonical registry, an implementation authority, or a security enforcement service.

## Reporting
Do not publish exploitable vulnerabilities, credentials, personal data, or sensitive operational details in public issues. Use GitHub private vulnerability reporting or a private security advisory only if enabled for this repository. No dedicated private reporting address is published here; if GitHub private reporting is unavailable, the owner must configure an approved private reporting channel before production use. Do not include secrets in public reports.

## Baseline requirements
- No secrets or credentials in source control, examples, logs, or test fixtures.
- Validate all untrusted input and constrain resource use.
- Apply least privilege and default-deny to protected actions.
- Fail closed when required authentication, authorization, integrity, or revocation checks cannot complete.
- Pin and review dependencies and CI actions; use short-lived credentials where supported.
- Record security-relevant events while minimizing sensitive payloads.
- Distinguish authentication from authorization and descriptive metadata from proof of trust.

## Current status
This policy is an initial baseline, not a completed threat model or independent security audit.
