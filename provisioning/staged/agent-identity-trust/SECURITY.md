# Security Policy

## Scope
Security reports for this repository's identity and trust contracts are welcome.

## Reporting
Do not disclose exploitable vulnerabilities in public issues. Use GitHub private vulnerability reporting or a private security advisory if enabled for this repository. A dedicated private reporting address has not been published in this repository; if private reporting is unavailable, the owner must configure a private reporting channel before production use. Do not send exploit details, credentials, tokens, or sensitive personal information through public channels.

## Security baseline
- Treat all principals, credentials, claims, manifests, schemas, and remote messages as untrusted until independently validated.
- A principal identifier or valid schema is not proof of authentication, authorization, or human ownership.
- Validate issuer, audience, validity interval, intended use, and credential status at trust boundaries.
- Apply least privilege and deny by default; constrain delegation by action, resource, audience, and expiry.
- Support revocation and key rotation; fail closed when trust state cannot be established.
- Never commit secrets or log credentials and tokens.
- Preserve audit-relevant provenance without claiming hashes prove truth or completeness.
