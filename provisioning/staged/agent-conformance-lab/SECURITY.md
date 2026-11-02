# Security Policy

This repository validates local metadata and synthetic fixtures. It does not execute repository code, connect to networks or certify production security.

## Reporting

Do not publish exploitable vulnerability details, credentials, personal data or confidential test artifacts in public issues. Use GitHub private vulnerability reporting or a private security advisory only if enabled for this repository. No dedicated private reporting address is published here; configure an owner-approved private channel if GitHub private reporting is unavailable.

## Security invariants

- Untrusted code is never executed.
- Missing identity, policy, audit, emergency-stop, compliance or supply-chain evidence is BLOCKED.
- Local schema conformance is not interoperability.
- Report hashes do not authenticate the report author.
- No test result may be fabricated or promoted to PASS without evidence.
