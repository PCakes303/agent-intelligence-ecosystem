# GitHub About metadata rollout

The approved descriptions, common homepage and repository topics for the 24 existing public portfolio repositories are maintained in `registry/github-repository-metadata.json`.

## Apply through an authorized GitHub session

The connected ChatGPT GitHub integration does not expose repository About settings write access. This guarded GitHub CLI script provides a reproducible local path.

Requirements:
- GitHub CLI (`gh`) authenticated as `PCakes303`.
- `jq` installed.
- Repository Administration: write permission on each of the 24 public portfolio repositories.

From a clone of `agent-intelligence-ecosystem`:

```bash
bash scripts/apply-github-metadata.sh --dry-run
```

Review the proposed descriptions, homepage and topics. If correct, apply:

```bash
bash scripts/apply-github-metadata.sh --apply
```

The script:
1. Validates that the manifest contains exactly 24 unique repositories and valid metadata fields.
2. Confirms the authenticated GitHub login is `PCakes303`.
3. Checks repository administration permission before changing each repository.
4. Updates description, homepage and topics using GitHub's repository API.
5. Reads each repository back and verifies the applied values.

The script stops on the first permission error or read-back mismatch. It is safe to rerun after correcting permissions or a transient API failure. It does not modify branch protection, vulnerability reporting, Actions permissions, secret scanning, push protection or dependency alerts; those require a separate security-settings review.

## Scope

This rollout applies only to the 24 existing public portfolio repositories. The separate public profile repository and private operations repository are excluded. New planned repositories should receive About metadata at creation from the canonical registry and an approved metadata entry.
