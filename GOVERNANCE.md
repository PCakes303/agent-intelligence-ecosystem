# Governance

## Authority and ownership

Each repository is authoritative for its own source, tests, releases, and repository-local documentation. The master repository is authoritative for the public portfolio registry, declared dependency graph, ecosystem-wide architecture decisions, and cross-repository compatibility status. The integration repository implements automation under contracts approved here.

## Change process

- Use issues for proposals and defects; use pull requests for changes.
- Significant architectural changes require an Architecture Decision Record (ADR).
- Changes to public interfaces, schemas, dependencies, licensing, security boundaries, or maturity status require explicit review.
- Registry changes must be generated from or checked against repository-owned manifests; manual edits require a traceable rationale.
- Do not auto-merge registry updates or trust unvalidated external PR metadata.
- Releases and maturity changes require evidence, not assertion.

## Required repository metadata

Every public technical repository should maintain a machine-readable manifest with: stable repository ID, name, purpose, owner, visibility, maturity, license, default branch, interfaces, dependencies, compatibility, security contact, release metadata, and manifest schema version. No credentials, private endpoints, or restricted operational details belong in public manifests.

## Decision records

ADRs use sequential identifiers and include context, decision, alternatives, consequences, status, date, and supersession links. Proposed decisions remain proposed until accepted.

## Licensing

Licensing is mixed by repository and artifact. Candidate defaults are Apache-2.0 for code and CC-BY-4.0 for documentation; schemas may use Apache-2.0 or CC0 depending on intended reuse. Dataset/source terms remain specific to each source. These are proposals pending explicit legal review and per-repository selection. Never assume one license covers the entire portfolio.

## Project identity

Public identity: MrCakes931. GitHub owner: PCakes303 until an account rename is formally completed. The profile repository `PCakes303/PCakes303` remains separate.

## Security and disclosure

Follow SECURITY.md. Report vulnerabilities privately through the owning repository's security reporting channel where available. Do not publish exploit details or embargoed vulnerability data in public issues or registry fields.
