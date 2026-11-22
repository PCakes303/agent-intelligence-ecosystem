# Owner Security Actions — 2026-11-22

This checklist records GitHub settings that the connected GitHub integration could not change.

## Confirmed finding

The GitHub branches API reported protected=false for the default main branch in all 32 public ecosystem repositories and the separate public profile repository PCakes303/PCakes303. The master repository's rulesets endpoint returned an empty list. Treat all 33 public account repositories as lacking verified merge protection until these settings are applied and re-checked.

## Apply to all 33 public repositories (32 ecosystem repositories plus the profile repository)

For each public repository:

1. Open Settings → Rules → Rulesets.
2. Create a branch ruleset targeting the default branch main.
3. Require a pull request before merging.
4. Require the repository's CI validation workflow/checks to pass before merge.
5. Require conversation resolution.
6. Block force pushes and branch deletion.
7. Restrict bypass permissions to the minimum necessary owner/admin roles; avoid broad bypass lists.
8. Save the ruleset and verify that the main branch reports as protected.

Do not require an approval count that the repository cannot satisfy. If a second trusted reviewer is available, require at least one approval; otherwise use required CI and owner review policy until a reviewer is configured.

## Security features to verify

Under each repository's Settings → Security areas:

- Enable Dependabot alerts.
- Enable Dependabot security updates.
- Confirm dependency graph access and supported ecosystems.
- Enable secret scanning and push protection where available.
- Enable code scanning / CodeQL default setup where the language and plan support it.
- Enable private vulnerability reporting.
- Review Actions permissions: default to read-only GITHUB_TOKEN; grant write permissions only to workflows that require them.
- Review third-party Actions and keep them pinned to verified full commit SHAs.

## Existing automation

- Weekly Dependabot GitHub Actions updates are configured in all 32 public ecosystem repositories.
- Weekly pip updates are configured in 25 repositories with Python package manifests.
- This configuration schedules version-update pull requests; it does not by itself enable Dependabot security alerts or security updates.

## Verification evidence to record

For each repository, record:
- Ruleset name and target branch.
- Required status-check names.
- Whether secret scanning, push protection, code scanning, Dependabot alerts/security updates, and private reporting are enabled.
- Actions default token permission and any workflow-specific write scopes.
- Date and reviewer for the verification.

## Release gate

Do not claim the portfolio is hardened or production-ready solely because CI passes. Merge protection, secret controls, security alerts, file-level provenance, emergency-stop enforcement, and OS sandbox isolation remain separate controls that require verification.


## Public repository execution register

The current account inventory contains these 33 public repositories. Use this as the checklist for the per-repository ruleset and security-settings review; the two private repositories are intentionally not in this public register.

- [ ] PCakes303 (separate profile repository)
- [ ] agent-intelligence-ecosystem
- [ ] agent-ai-discovery
- [ ] mrcakes931-ecosystem
- [ ] agent-ecosystem-integration
- [ ] agent-foundation-spec
- [ ] agent-resource-manifest
- [ ] agent-schema-registry
- [ ] agent-identity-trust
- [ ] agent-secure-supply-chain
- [ ] agent-policy-engine
- [ ] agent-audit-provenance
- [ ] aix-core
- [ ] aix-codecs
- [ ] agent-transport-gateway
- [ ] agent-discovery-network
- [ ] agent-capability-registry
- [ ] swarm-runtime
- [ ] swarm-coordination
- [ ] swarm-state-mesh
- [ ] osint-source-registry
- [ ] intelligence-knowledge-graph
- [ ] agent-tool-adapters
- [ ] agent-skill-library
- [ ] agent-sandbox-security
- [ ] agent-emergency-control
- [ ] agent-compliance-governance
- [ ] agent-conformance-lab
- [ ] osint-collection-framework
- [ ] osint-evidence-engine
- [ ] osint-entity-resolution
- [ ] agent-federation-network
- [ ] adaptive-swarm-compression

Private repositories excluded from this public checklist: agent-ecosystem-private and swarm-information-research. Their settings and source contents require a separate private-repository audit.


## Reverification — 2026-11-22

- Live branch API rechecked all 33 public account repositories (32 ecosystem repositories plus PCakes303 profile). Every default main branch still reports protected=false. No branch ruleset/protection write action is exposed by the connected integration; owner action remains required.
- Live About metadata was refreshed for all 33 public repositories: 18 descriptions present, 15 blank, 0 homepage URLs, 0 topics. See [GitHub About Metadata Audit](GITHUB-ABOUT-AUDIT-2026-11-22.md). The integration cannot apply About settings.
- Security alert/scanning, secret scanning, push protection, private vulnerability reporting, and Actions default token permissions remain unverified through the connected integration. Do not infer enabled/disabled or zero-alert status from missing data.
