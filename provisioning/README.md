# Remote Repository Provisioning

## Current verified state

The latest portfolio reconciliation verified 23 existing public portfolio repositories, 6 public repositories still to be created, and the separate existing private operations repository. The private repository is excluded from all public scaffold generation, catalogs, and synchronization. The separate profile repository is not part of the portfolio.

The GitHub integration available to this session can inspect and write repository contents, branches, commits, issues, and pull requests, but does not expose repository creation or repository-administration operations. It also does not expose GitHub Projects v2 mutations or repository metadata administration. GitHub's current Projects v2 API is GraphQL-based and requires the project scope; the connected integration does not provide that action. A repository-resident portfolio tracker and a master-repository issue are therefore used as the current work wireframe until that capability is available. The provisioning script below bridges that gap through the GitHub CLI on a machine where the owner is authenticated.

## Provisioning bundle

- Machine-readable missing-repository list: remote-repositories-to-create.json (6 verified missing public repositories as of the 2026-11-02 reconciliation)
- 30-repository status wireframe: ../PORTFOLIO-STATUS.md and ../registry/implementation-status.json
- Public-only local scaffold generator: ../tools/bootstrap_repositories.py
- Remote creation and initial push: ../tools/provision_public_repositories.sh
- Shared starter files: ../templates/repository/
- Repository 09 deployed: `agent-policy-engine` (public remote exists; starter CI passes)
- Repository 10 deployed: `agent-audit-provenance` (public remote exists; CI verified; retained staging packet is an exact parity reference)
- Repository 11 deployed: `aix-core` (public remote exists; CI verified; retained staging packet is an exact parity reference)
- GitHub About descriptions and topics: ../docs/GITHUB-REPOSITORY-ABOUT-METADATA.md
- Canonical registry: ../registry/repositories.json

## Requirements

- Git
- Python 3.10+
- GitHub CLI (gh), authenticated as PCakes303
- Git author email configured locally
- Permission to create public repositories under PCakes303

## Run

From a clone of the master repository:

```bash
python3 tools/bootstrap_repositories.py --output dist/public-repositories
```

Inspect the generated files and the list of targets. Then run the explicit-confirmation provisioner:

```bash
bash tools/provision_public_repositories.sh --confirm
```

The script checks the authenticated GitHub login, refuses to guess a Git email, creates public repositories only, skips repositories that already exist, and pushes an initial main branch. It does not create or modify the private repository. It does not configure branch protection, secrets, environments, or GitHub App permissions.

## Repository 10 prepared bundle

The [agent-audit-provenance staging bundle](staged/agent-audit-provenance/STAGING-STATUS.md) is prepared. Create an empty public repository named `agent-audit-provenance` under `PCakes303`, then send its URL so the staged files can be deployed and CI verified. Do not mark it as created until GitHub confirms the remote exists.

## After provisioning

Re-run registry reconciliation and verify all repository visibility and default branches. Then configure branch protection, rulesets, security features, and least-privilege automation through GitHub settings. These administration settings cannot be verified or applied through the current connected integration.

Do not bulk-create private repositories from public scaffold output. The private operations repository already exists and remains a separate trust boundary.

## Entry-level builds in generated repositories

The reusable public template now includes a no-third-party-dependency starter build, a small test suite, a Makefile, an entry-level build guide, and a read-only GitHub Actions workflow pinned to immutable action SHAs. Every generated public repository begins with this Starter tier; its domain-specific Developer and Production tiers are added as implementation work proceeds. The scaffold generator still excludes the private repository.

## Repository 11 prepared bundle

The [AIX Core staging bundle](staged/aix-core/STAGING-STATUS.md) is prepared. Create an empty public repository named `aix-core` under `PCakes303`, then send its URL so the staged files can be deployed and CI verified. Do not mark it as created until GitHub confirms the remote exists.

## Repository 24 prepared bundle

The [agent-tool-adapters staging bundle](staged/agent-tool-adapters/STAGING-STATUS.md) was deployed to [PCakes303/agent-tool-adapters](https://github.com/PCakes303/agent-tool-adapters). Its 16 product files have exact Git blob parity with staging; all 13 unit tests pass on Python 3.10, 3.11 and 3.12. The sandbox-security prerequisite remains planned and is not implemented; all four declared dependencies remain contract-only, not tested runtime integrations.


## Repository 25 deployment

The [agent-skill-library staging bundle](staged/agent-skill-library/STAGING-STATUS.md) was deployed to [PCakes303/agent-skill-library](https://github.com/PCakes303/agent-skill-library). Its 17 product files match the retained staging packet by Git blob SHA. CI passed on Python 3.10, 3.11 and 3.12 with 18 unit tests. It is an experimental declarative format and validator, not a workflow executor or security boundary.
