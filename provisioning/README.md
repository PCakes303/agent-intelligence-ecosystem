# Remote Repository Provisioning

## Current verified state

The connected GitHub account currently has eight public portfolio repositories (the master, discovery, human guide, integration, and four foundation repositories) plus the separate private operations repository. The remaining 21 public repositories in the approved registry are not yet present.

The GitHub integration available to this session can inspect and write repository contents, branches, commits, issues, and pull requests, but does not expose repository creation or repository-administration operations. The provisioning script below bridges that gap through the GitHub CLI on a machine where the owner is authenticated.

## Provisioning bundle

- Machine-readable missing-repository list: remote-repositories-to-create.json (21 verified missing public repositories as of this reconciliation)
- Public-only local scaffold generator: ../tools/bootstrap_repositories.py
- Remote creation and initial push: ../tools/provision_public_repositories.sh
- Shared starter files: ../templates/repository/
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

## After provisioning

Re-run registry reconciliation and verify all repository visibility and default branches. Then configure branch protection, rulesets, security features, and least-privilege automation through GitHub settings. These administration settings cannot be verified or applied through the current connected integration.

Do not bulk-create private repositories from public scaffold output. The private operations repository already exists and remains a separate trust boundary.

## Entry-level builds in generated repositories

The reusable public template now includes a no-third-party-dependency starter build, a small test suite, a Makefile, an entry-level build guide, and a read-only GitHub Actions workflow pinned to immutable action SHAs. Every generated public repository begins with this Starter tier; its domain-specific Developer and Production tiers are added as implementation work proceeds. The scaffold generator still excludes the private repository.
