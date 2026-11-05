# Security Policy

## Scope
Security reports for this repository and its ecosystem-facing contracts are welcome.

## Reporting
Do not disclose exploitable vulnerabilities in public issues, discussions, commits, or pull requests. Use GitHub's private vulnerability reporting or a private security advisory only when that feature is enabled for this repository. If private reporting is not enabled, first contact the repository owner through an independently verified private channel to arrange secure disclosure; do not send exploit details, credentials, tokens, or sensitive personal information through public channels. This file does not assert that private reporting is currently enabled.

## Baseline
- Treat external inputs, manifests, schemas, events, plugins, and referenced artifacts as untrusted until independently validated.
- Apply least privilege and deny by default.
- Never place secrets in source, logs, examples, fixtures, or issue reports.
- Validate inputs at trust boundaries; bound resource use and reject ambiguous or malformed data.
- Preserve provenance and audit-relevant metadata without claiming hashes prove truth or completeness.
- Pin CI dependencies and use short-lived credentials for publishing.

## Operational status
Repository security-reporting settings and branch protections must be verified in GitHub repository settings. This policy is not evidence that any setting is enabled.