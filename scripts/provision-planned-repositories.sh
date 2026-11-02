#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "Run this script from a clone of agent-intelligence-ecosystem." >&2
  exit 2
}
MANIFEST="$ROOT/registry/planned-repository-metadata.json"
OWNER="PCakes303"
MODE="dry-run"

if [[ "${1:-}" == "--apply" ]]; then
  MODE="apply"
elif [[ "${1:-}" != "" && "${1:-}" != "--dry-run" ]]; then
  echo "Usage: $0 [--dry-run|--apply]" >&2
  exit 2
fi

for cmd in gh git jq; do
  command -v "$cmd" >/dev/null 2>&1 || { echo "Missing required command: $cmd" >&2; exit 2; }
done
[[ -f "$MANIFEST" ]] || { echo "Missing planned repository metadata: $MANIFEST" >&2; exit 2; }
[[ "$(git -C "$ROOT" branch --show-current)" == "main" ]] || {
  echo "Checkout main before provisioning." >&2; exit 1;
}
[[ -z "$(git -C "$ROOT" status --porcelain)" ]] || {
  echo "Working tree must be clean. Commit or stash local changes first." >&2; exit 1;
}

jq -e '
  .owner == "PCakes303"
  and (.repositories | length == 7)
  and (([.repositories[].name] | unique | length) == 7)
  and all(.repositories[];
    (.description | type == "string" and length > 0 and length <= 350)
    and (.homepage | type == "string" and startswith("https://"))
    and (.topics | type == "array" and length <= 20)
    and all(.topics[]; test("^[a-z0-9][a-z0-9-]*$"))
  )
' "$MANIFEST" >/dev/null || {
  echo "Planned repository metadata failed validation; no changes made." >&2
  exit 1
}

LOGIN="$(gh api user --jq '.login')"
[[ "$LOGIN" == "$OWNER" ]] || {
  echo "Authenticated GitHub account is '$LOGIN'; expected $OWNER." >&2
  exit 1
}

REMOTE_HEAD="$(gh api "repos/$OWNER/agent-intelligence-ecosystem/commits/main" --jq '.sha')"
LOCAL_HEAD="$(git -C "$ROOT" rev-parse HEAD)"
[[ "$REMOTE_HEAD" == "$LOCAL_HEAD" ]] || {
  echo "Local master clone is not at origin/main. Pull the latest master commit and retry." >&2
  exit 1
}

echo "Mode: $MODE"
echo "Owner: $OWNER"
echo "Master commit: $LOCAL_HEAD"
echo "Planned public repositories: 7"
echo

while IFS= read -r row; do
  name="$(jq -r '.name' <<<"$row")"
  full="$OWNER/$name"
  stage="$ROOT/provisioning/staged/$name"
  description="$(jq -r '.description' <<<"$row")"
  homepage="$(jq -r '.homepage' <<<"$row")"
  topics_payload="$(jq -c '{names: .topics}' <<<"$row")"

  for required in README.md LICENSE.md manifest.json capabilities.json .github/workflows; do
    [[ -e "$stage/$required" ]] || {
      echo "Missing staged release input: $stage/$required" >&2; exit 1;
    }
  done
  grep -q 'LICENSE.md' "$stage/README.md" || {
    echo "README does not link LICENSE.md: $name" >&2; exit 1;
  }

  if gh api "repos/$full" >/dev/null 2>&1; then
    exists="yes"
  else
    exists="no"
  fi

  if [[ "$MODE" == "dry-run" ]]; then
    printf 'WOULD CREATE/PUBLISH %-34s\n' "$full"
    printf '  description: %s\n' "$description"
    printf '  homepage: %s\n' "$homepage"
    printf '  topics: %s\n' "$(jq -r '.topics | join(", ")' <<<"$row")"
    printf '  staged files: %s\n' "$(find "$stage" -type f ! -name STAGING-STATUS.md | wc -l | tr -d ' ')"
    printf '  remote already exists: %s\n' "$exists"
    continue
  fi

  TMP="$(mktemp -d)"
  trap 'rm -rf "$TMP"' EXIT
  cp -R "$stage/." "$TMP/"
  rm -f "$TMP/STAGING-STATUS.md"

  git -C "$TMP" init --initial-branch=main >/dev/null
  git -C "$TMP" add -A
  git -C "$TMP" -c user.name="MrCakes931" -c user.email="noreply@github.com" commit -m "Initial scaffold: $name" >/dev/null
  LOCAL_TREE="$(git -C "$TMP" rev-parse 'HEAD^{tree}')"

  if [[ "$exists" == "no" ]]; then
    gh repo create "$full" --public --description "$description" --homepage "$homepage"
    git -C "$TMP" remote add origin "https://github.com/$full.git"
    git -C "$TMP" push -u origin main
  else
    DEFAULT_BRANCH="$(gh api "repos/$full" --jq '.default_branch')"
    [[ "$DEFAULT_BRANCH" == "main" ]] || {
      echo "$full exists with default branch '$DEFAULT_BRANCH'; refusing automatic changes." >&2
      exit 1
    }
    if gh api "repos/$full/git/ref/heads/main" >/dev/null 2>&1; then
      REMOTE_COMMIT="$(gh api "repos/$full/git/ref/heads/main" --jq '.object.sha')"
      REMOTE_TREE="$(gh api "repos/$full/git/commits/$REMOTE_COMMIT" --jq '.tree.sha')"
      [[ "$REMOTE_TREE" == "$LOCAL_TREE" ]] || {
        echo "$full already exists with a different tree; refusing to overwrite. Reconcile manually." >&2
        exit 1
      }
    else
      git -C "$TMP" remote add origin "https://github.com/$full.git"
      git -C "$TMP" push -u origin main
    fi
  fi

  gh api --method PATCH "repos/$full" -f description="$description" -f homepage="$homepage" >/dev/null
  gh api --method PUT "repos/$full/topics" --input - <<<"$topics_payload" >/dev/null

  ACTUAL="$(gh api "repos/$full" --jq '{description, homepage}' | jq -S -c .)"
  EXPECTED="$(jq -S -c '{description, homepage}' <<<"$row")"
  [[ "$ACTUAL" == "$EXPECTED" ]] || {
    echo "Description/homepage read-back mismatch: $full" >&2; exit 1;
  }
  ACTUAL_TOPICS="$(gh api "repos/$full/topics" --jq '{names: (.names | sort)}' | jq -S -c .)"
  EXPECTED_TOPICS="$(jq -S -c '{names: (.topics | sort)}' <<<"$row")"
  [[ "$ACTUAL_TOPICS" == "$EXPECTED_TOPICS" ]] || {
    echo "Topics read-back mismatch: $full" >&2; exit 1;
  }

  echo "Created/verified $full. Check Actions for the initial CI run."
  rm -rf "$TMP"
  trap - EXIT
done < <(jq -c '.repositories[]' "$MANIFEST")

if [[ "$MODE" == "dry-run" ]]; then
  echo
  echo "Dry run only. Review all seven repositories, then run with --apply."
else
  echo
  echo "Provisioning completed. Verify the first GitHub Actions run for each new repository before marking it deployed."
fi
