# Security Policy

## Scope

Security is a portfolio-wide engineering requirement. Each repository must publish its own supported-version policy and security reporting instructions before it accepts production use.

## Baseline controls

- Explicit authentication and authorization; least privilege and capability-scoped access.
- Treat all agents, tools, plugins, adapters, peers, inputs, and imported artifacts as untrusted until verified.
- Secure transport, credential rotation and revocation, bounded sessions, and auditable trust decisions.
- No secrets in source control, manifests, logs, issues, examples, or build artifacts.
- Use short-lived credentials and workload identity where supported; prefer OIDC over long-lived CI secrets.
- Pin third-party CI actions to immutable commit SHAs; minimize workflow permissions.
- Generate SBOMs and provenance for releasable artifacts; verify dependencies and signatures.
- Isolate execution with explicit CPU, memory, filesystem, process, and network boundaries.
- Protect audit records against unauthorized alteration; document retention and privacy controls.
- Apply rate limits, backpressure, abuse detection, and safe failure handling.
- Respect OSINT source authorization, terms, robots directives, privacy, and rate limits.

## Reporting

Do not disclose vulnerabilities publicly before coordinated remediation. Use GitHub private vulnerability reporting/security advisories when enabled, or contact the maintainers through the private channel configured for the repository. Do not include credentials or sensitive personal information in reports.

## Private repository boundary

`agent-ecosystem-private` is not a secrets manager. Store credentials only in an approved secrets manager; Git may contain non-secret references to secret identifiers and operational ownership. Public automation must not read from, mirror, or export private repository content. Any intentionally public disclosure requires explicit human review and sanitization.
