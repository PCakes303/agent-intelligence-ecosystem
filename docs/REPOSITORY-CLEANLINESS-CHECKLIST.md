# Repository Cleanliness and Acceptance Checklist

Use one copy of this checklist per public repository. The master control plane uses the same governance principles with its own registry-specific checks.

## Audit identity

- Repository:
- Portfolio ID:
- Default branch:
- Commit SHA:
- Audit date:
- Reviewer:
- Current maturity:
- Target maturity:
- Previous checkpoint:

## A. Structure and documentation

- [ ] README accurately states purpose, maturity, implemented features, non-goals and limitations.
- [ ] README includes setup, quick start, test commands, architecture, security boundary and license status.
- [ ] AGENTS.md has repository-specific safe working instructions and validation commands.
- [ ] CONTRIBUTING.md setup, tests, style and review instructions work.
- [ ] SECURITY.md has an accurate reporting path and does not promise unsupported response SLAs.
- [ ] llms.txt links to current authoritative docs and does not duplicate stale claims.
- [ ] manifest.json parses, validates and agrees with the master registry.
- [ ] capabilities.json contains only supported capabilities and labels maturity correctly.
- [ ] compatibility.json distinguishes tested, unsupported and unknown compatibility.
- [ ] docs/ is accurate, linked and maintained.
- [ ] Examples and fixtures are safe, runnable where claimed, synthetic or properly licensed.
- [ ] Required file exceptions are recorded and approved rather than silently omitted.

## B. Implementation evidence

- [ ] Each advertised capability links to implementation.
- [ ] Planned work is not presented as implemented.
- [ ] Experimental/advisory behavior is labeled.
- [ ] Public API and schemas match implementation.
- [ ] Error handling, invalid inputs, timeouts, retries and resource bounds are tested where relevant.
- [ ] No dead scaffolds, placeholder functions or unreferenced duplicate docs are presented as finished features.

## C. Tests and automation

- [ ] Reproducible local test/build command documented.
- [ ] CI invokes the documented checks.
- [ ] Unit and regression tests pass.
- [ ] Negative/security tests cover important failure modes.
- [ ] Schema and metadata validation passes.
- [ ] Dependency and secret checks are configured where supported.
- [ ] Cross-repository integration/conformance tests pass or are explicitly blocked/not yet applicable.
- [ ] Latest CI run URL, commit SHA and result recorded.

## D. Security and privacy

- [ ] No secrets, private keys, tokens, personal data or private operations content committed.
- [ ] Least privilege and deny-by-default semantics documented and enforced where claimed.
- [ ] Inputs, payload sizes, execution time, retries and resource use are bounded where applicable.
- [ ] Security-sensitive actions have attributable audit records.
- [ ] Policy decision points are distinguished from enforcement points.
- [ ] Emergency stop and revocation dependencies are integrated where required.
- [ ] Sandbox claims are backed by actual OS isolation tests; policy validation alone is not called sandboxing.
- [ ] Threat model and known limitations are current.

## E. Licensing and provenance

- [ ] Code license decision recorded.
- [ ] Documentation/media license decision recorded.
- [ ] Schemas/specification license decision recorded.
- [ ] Examples/fixtures/data provenance and terms recorded.
- [ ] Third-party dependency licenses and notices reviewed.
- [ ] LICENSE and notices match the approved decisions.
- [ ] If pending, the repository explicitly says license is pending and makes no license claim.

## F. GitHub repository settings

- [ ] About description matches README.
- [ ] Homepage points to the master ecosystem repository.
- [ ] Topics are relevant, lowercase and hyphenated.
- [ ] Live About values re-read after saving.
- [ ] Default branch and merge settings reviewed.
- [ ] Branch rules/rulesets reviewed and evidence captured.
- [ ] Actions permissions and workflow token scope reviewed.
- [ ] Secret scanning, push protection and dependency/security alerts reviewed where available.
- [ ] CODEOWNERS contains valid owners if used.

## G. Release and integration

- [ ] Dependencies match the canonical graph.
- [ ] Consumer/provider compatibility has an integration test or explicit exception.
- [ ] Build artifacts are reproducible where distribution is intended.
- [ ] SBOM/provenance/signature verification exists where release risk requires it.
- [ ] Changelog/release notes exist when versions are published.
- [ ] No placeholder release or package was created to simulate completeness.
- [ ] Known limitations and outstanding issues are linked.
- [ ] Master registry and status tracker updated.
- [ ] Audit checkpoint committed.

## Final disposition

Select one:
- [ ] PASS
- [ ] PASS WITH EXCEPTIONS
- [ ] BLOCKED
- [ ] NOT REVIEWED

**Evidence links:**
- Commit:
- CI:
- Tests:
- Integration:
- Security review:
- License decision:
- Settings review:
- Master checkpoint:

**Exceptions and follow-up issues:**

**Maturity decision and rationale:**
