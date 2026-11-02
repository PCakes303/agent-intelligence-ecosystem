#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANIFEST="${ROOT}/registry/github-repository-metadata.json"
MODE="dry-run"

if [[ "${1:-}" == "--apply" ]]; then
  MODE="apply"
elif [[ "${1:-}" != "" && "${1:-}" != "--dry-run" ]]; then
  echo "Usage: $0 [--dry-run|--apply]" >&2
  exit 2
fi

for cmd in gh jq; do
  command -v "$cmd" >/dev/null 2>&1 || { echo "Missing required command: $cmd" >&2; exit 2; }
done

[[ -f "$MANIFEST" ]] || { echo "Metadata manifest not found: $MANIFEST" >&2; exit 2; }

jq -e '
  .owner == "PCakes303"
  and (.repositories | length == 24)
  and (([.repositories[].name] | unique | length) == 24)
  and all(.repositories[];
    (.description | type == "string" and length > 0 and length <= 350)
    and (.homepage | type == "string" and startswith("https://"))
    and (.topics | type == "array" and length <= 20)
    and all(.topics[]; test("^[a-z0-9][a-z0-9-]*$"))
  )
' "$MANIFEST" >/dev/null || {
  echo "Metadata manifest failed validation; no changes made." >&2
  exit 1
}

LOGIN="$(gh api user --jq '.login')"
[[ "$LOGIN" == "PCakes303" ]] || {
  echo "Authenticated GitHub account is '$LOGIN', expected PCakes303." >&2
  exit 1
}

echo "Mode: $MODE"
echo "Manifest: $MANIFEST"
echo "Repositories: 24"
echo

while IFS= read -r row; do
  name="$(jq -r '.name' <<<"$row")"
  repo="PCakes303/$name"
  description="$(jq -r '.description' <<<"$row")"
  homepage="$(jq -r '.homepage' <<<"$row")"
  topics="$(jq -r '.topics | join(", ")' <<<"$row")"

  is_admin="$(gh api "repos/$repo" --jq '.permissions.admin // false')"
  [[ "$is_admin" == "true" ]] || {
    echo "Missing repository administration permission: $repo" >&2
    exit 1
  }

  payload="$(jq -c '{description, homepage, topics}' <<<"$row")"

  if [[ "$MODE" == "dry-run" ]]; then
    printf 'WOULD UPDATE %-34s description=%s\n' "$repo" "$description"
    printf '  homepage=%s\n  topics=%s\n' "$homepage" "$topics"
    continue
  fi

  echo "Updating $repo"
  gh api --method PATCH "repos/$repo" --input - <<<"$payload" >/dev/null

  actual="$(gh api "repos/$repo" --jq '{description, homepage, topics} | .topics |= sort' | jq -S -c .)"
  expected="$(jq -S -c '{description, homepage, topics} | .topics |= sort' <<<"$row")"
  [[ "$actual" == "$expected" ]] || {
    echo "Read-back mismatch after updating $repo" >&2
    echo "Expected: $expected" >&2
    echo "Actual:   $actual" >&2
    exit 1
  }
  echo "Verified $repo"
done < <(jq -c '.repositories[]' "$MANIFEST")

if [[ "$MODE" == "dry-run" ]]; then
  echo
  echo "Dry run only. Review the manifest, then run this script with --apply."
else
  echo
  echo "All 24 repository About settings updated and read back successfully."
fi
