# Universal Repository Standard

**Portfolio:** MrCakes931 Agent Intelligence Ecosystem  
**GitHub owner:** PCakes303  
**Master control plane:** https://github.com/PCakes303/agent-intelligence-ecosystem  
**Applies to:** all 31 public repositories, including the master repository, with role-specific exceptions.  
**Policy:** mandatory release gate; not a claim that every repository is already compliant.

## 1. Purpose and governing principles

This standard makes every public repository understandable, reproducible, maintainable, auditable and honest about its maturity.

1. Preserve history and working implementation. Correct through reviewed, traceable commits; do not erase checkpoints to make status look clean.
2. Distinguish planned, scaffolded, experimental, alpha, beta and stable. A README, schema, test scaffold or passing CI job alone cannot advance maturity.
3. Every claim must be traceable to code, schema, tests, workflow, integration evidence or a clearly labeled design decision.
4. Do not imply production security, authentication, compliance, OS isolation, interoperability or performance without evidence for the actual property.
5. Prefer small, role-appropriate repositories over empty boilerplate. Required common materials are universal; technical artifacts are conditional on repository purpose.
6. The master repository is the canonical portfolio control plane. Component repositories own their implementation details and local technical documentation.
7. The private operations repository is outside this public standard's publication scope. Never mirror private content into public repositories.

## 2. Common repository baseline

Every public repository must have the following, unless a documented, approved exception is recorded in the master registry:

- `README.md`: purpose, scope, maturity, implemented functionality, explicit non-goals/limitations, quick start, development/test commands, architecture, security boundary, links to canonical docs and license status.
- `AGENTS.md`: repository-specific contribution/agent instructions, safety constraints, validation commands and authoritative file locations.
- `CONTRIBUTING.md`: contribution workflow, setup, tests, style, review and change expectations.
- `SECURITY.md`: supported reporting channel, response expectations where supportable, scope, known security limitations and prohibited disclosure practices. Do not promise a response SLA that is not staffed.
- `llms.txt`: concise, accurate navigation to the canonical project docs, schemas, code, tests and limitations. Do not duplicate stale prose.
- `manifest.json`: machine-readable identity, version/maturity, purpose, entrypoints, dependency declarations and links. It must agree with the registry and implementation.
- `capabilities.json`: only capabilities demonstrably implemented; distinguish implemented, experimental, advisory and planned.
- `compatibility.json`: tested compatibility and protocol/version matrix. Unknown or untested compatibility must be marked unknown/not-tested, not assumed.
- `.github/workflows/`: reproducible CI for the languages and checks the repository actually uses.
- `tests/`: meaningful tests, including negative/invalid-input cases for validators and security-sensitive contracts.
- `docs/`: detailed, maintained documentation for the repository's actual domain.

Existing component repositories currently contain these entrypoints. Their presence is not a pass: contents and claims must be checked.

## 3. Conditional technical materials

Add these when they fit the repository's role; do not create empty placeholder files just to satisfy a checklist.

- `LICENSE` and third-party notices: only after an explicit per-repository and artifact-category license decision has been reviewed and approved. Until then, state clearly that licensing is pending and do not claim the project is open source under a particular license.
- `CHANGELOG.md`: required when versions or user-visible releases are published; use a documented format.
- `CODE_OF_CONDUCT.md`: required before inviting an open external contributor community.
- `SUPPORT.md`: use when there is a real support path and capacity.
- `CITATION.cff`: add when software citation is useful and metadata can be maintained.
- `pyproject.toml`, `package.json`, lockfiles, build scripts and package metadata: only for actual distributable software in that ecosystem.
- `schemas/`: for machine-validated contracts; include schema dialect/version and validation tests.
- `examples/` and fixtures: provide runnable, safe, synthetic or properly licensed examples where applicable.
- SBOM, provenance, signatures and release attestations: required for distributable artifacts before stable release, with real verification rather than decorative metadata.
- `CODEOWNERS`: add only with valid, maintained owner identities; do not invent teams or use placeholder owners.

## 4. README content contract

The README must answer, without requiring the reader to infer:

1. What this repository is and is not.
2. Its current maturity and what evidence supports that status.
3. What actually works today, with links to implementation and tests.
4. What remains planned or experimental.
5. How to install/setup, run a safe example and run tests.
6. Its dependencies and compatibility boundaries.
7. Its security model, trust boundaries and known limitations.
8. Its license status and third-party material status.
9. Where to report a vulnerability and contribute.

The README's description must match the GitHub About description. Do not present roadmap items as current capabilities.

## 5. Manifest and capability integrity

- Validate JSON syntax and schema in CI.
- Use stable repository IDs and canonical names from the master registry.
- Use explicit semantic versions for versioned contracts; do not invent a release version for unreleased work.
- Keep dependency declarations aligned with `registry/repositories.json` and `registry/dependencies.json`.
- Do not claim MCP, A2A, AIX, authentication, federation, sandboxing or protocol compatibility solely because an adapter interface or design document exists.
- Capabilities must link to implementation and tests; unsupported claims are removed or marked planned.
- Compatibility entries must identify what was tested, how, and against which version.

## 6. Implementation and test quality

Every repository must define a reproducible local validation command and use the same command in CI where feasible.

CI should include, as applicable:
- syntax/type/static checks;
- formatter/linter;
- schema and manifest validation;
- unit and regression tests;
- negative/security tests;
- dependency and secret scanning;
- build/package verification for distributable projects;
- integration/conformance tests for shared contracts.

Tests must be substantive and fail when behavior is incorrect. Avoid tests that only assert constants, import modules, or duplicate schema shape without testing behavior. Fixtures must be synthetic, non-sensitive and appropriately licensed.

## 7. Security baseline

- Least privilege and deny-by-default at authorization boundaries.
- No secrets, tokens, private keys, personal data or private operations content in public repositories.
- Validate untrusted inputs and bound size, time, retries, resource consumption and network access.
- Log security-relevant decisions without leaking credentials or unnecessary personal data.
- Use dependency pinning/lockfiles where the ecosystem supports them.
- Separate policy decision logic from enforcement; document where enforcement actually occurs.
- No arbitrary tool/skill/workload execution until emergency stop, identity/revocation, policy enforcement, provenance and actual OS-level isolation have been integrated and tested.
- The sandbox policy validator is not OS isolation. A successful CI workflow is not a security certification.

## 8. Licensing and intellectual property

The portfolio uses a mixed-license strategy, but each repository and artifact category requires an explicit decision. Do not bulk-apply a single license.

For each repository, record:
- approved code license or explicit no-license status;
- documentation and media terms;
- schema/specification terms;
- example/fixture/data provenance and license;
- third-party dependencies and required notices;
- compatibility of combined/distributed artifacts;
- attribution and patent terms where relevant.

Until the decision is made, retain the work and state that licensing is pending. Public visibility alone does not grant reuse rights. Legal review is required where the intended distribution or dependency mix creates uncertainty.

## 9. Repository metadata

Every public repository must have:
- a concise, accurate GitHub About description;
- the common master repository homepage;
- a small set of meaningful lowercase, hyphenated topics;
- a README title and summary consistent with the About description;
- a license declaration only when backed by the actual approved license files.

The metadata guide in `docs/GITHUB-REPOSITORY-ABOUT-METADATA.md` is a proposed application manifest, not proof of settings being applied. Verify the live repository metadata after changes. Topics should describe the repository's actual purpose, not planned capabilities.

## 10. Governance and maintenance

- Keep a root-level project status and roadmap where useful; the master registry remains the portfolio-wide source of truth.
- Record architectural changes as ADRs.
- Keep release notes and deprecation/migration notes for user-visible changes.
- Preserve checkpoints and mark them superseded when the portfolio changes.
- Review dependencies, issues, workflow failures, docs links, metadata and security advisories regularly.
- Keep generated indexes and catalogs derived from canonical sources; do not hand-maintain contradictory copies.
- Every material change needs a commit, passing validation and a checkpoint/update to the master tracker.

## 11. Required acceptance record

Before a repository is marked clean, record:
- repository and commit SHA audited;
- required file presence and content review;
- schema/manifest/capability/compatibility validation;
- exact test and CI run links/results;
- dependency and integration status;
- license/IP decision or explicit pending status;
- GitHub About metadata status;
- branch rules, Actions permissions and security feature review status;
- known limitations and follow-up issues;
- auditor date and final maturity decision.

Use one of: `PASS`, `PASS WITH EXCEPTIONS`, `BLOCKED`, `NOT REVIEWED`. Never use an ambiguous green check without evidence.

## 12. Portfolio release gate

A public repository is clean only when its common baseline and applicable conditional materials pass, metadata is accurate, claims match implementation, and all exceptions are documented.

A repository is release-ready only when the relevant seven gates also pass: structure, implementation, testing, integration, security, governance/licensing and deployment evidence.

The master repository must fail validation when registry counts, dependency edges, public catalog, implementation status or provisioning inventory drift without an explicit approved update.
