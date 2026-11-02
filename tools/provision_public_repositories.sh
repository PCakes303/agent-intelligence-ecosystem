#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OWNER="PCakes303"
OUT="$ROOT/dist/public-repositories"

if [[ "${1:-}" != "--confirm" ]]; then
  echo "Refusing to create 28 public GitHub repositories without explicit confirmation."
  echo "Review provisioning/remote-repositories-to-create.json, then rerun with --confirm."
  exit 2
fi

command -v gh >/dev/null || { echo "GitHub CLI (gh) is required." >&2; exit 2; }
command -v git >/dev/null || { echo "git is required." >&2; exit 2; }
command -v python3 >/dev/null || { echo "python3 is required." >&2; exit 2; }
gh auth status >/dev/null
LOGIN="$(gh api user --jq .login)"
if [[ "$LOGIN" != "$OWNER" ]]; then
  echo "Authenticated GitHub user is $LOGIN, expected $OWNER. Refusing to continue." >&2
  exit 2
fi
if [[ -z "$(git config --get user.email || true)" ]]; then
  echo "Configure git user.email before provisioning; no email will be guessed." >&2
  exit 2
fi

python3 "$ROOT/tools/bootstrap_repositories.py" --output "$OUT"

created=0
skipped=0
while IFS=$'\t' read -r name description; do
  [[ -n "$name" ]] || continue
  full="$OWNER/$name"
  path="$OUT/$name"
  if gh repo view "$full" >/dev/null 2>&1; then
    echo "SKIP existing: $full"
    skipped=$((skipped + 1))
    continue
  fi

  git -C "$path" init --initial-branch=main >/dev/null
  git -C "$path" add .
  git -C "$path" commit -m "chore: initialize MrCakes931 ecosystem repository" >/dev/null
  gh repo create "$full" --public --description "$description" --source "$path" --remote origin --push
  echo "CREATED: $full"
  created=$((created + 1))
done < <(python3 - "$OUT/SCAFFOLD-REPORT.json" <<'PY'
import json, pathlib, sys
report = json.loads(pathlib.Path(sys.argv[1]).read_text())
for name in report["repositories"]:
    manifest = json.loads((pathlib.Path(sys.argv[1]).parent / name / "manifest.json").read_text())
    print(name + "\t" + manifest["summary"].replace("\t", " "))
PY
)

echo "Provisioning finished. Created: $created; skipped existing: $skipped."
echo "Private repositories are intentionally excluded."
