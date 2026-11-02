#!/usr/bin/env python3
"""Beginner-friendly, dependency-free starter build for a new ecosystem repo."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    manifest=json.loads((ROOT/"manifest.json").read_text(encoding="utf-8"))
    required=("id","name","visibility","maturity","summary","repository_url")
    missing=[key for key in required if not manifest.get(key)]
    if missing: raise SystemExit("manifest missing: "+", ".join(missing))
    if manifest["visibility"]!="public": raise SystemExit("public starter template refuses non-public repository metadata")
    if not (ROOT/"AGENTS.md").is_file(): raise SystemExit("AGENTS.md missing")
    if not (ROOT/"SECURITY.md").is_file(): raise SystemExit("SECURITY.md missing")
    print(json.dumps({"tier":"starter","repository":manifest["name"],"registry_id":manifest["id"],"result":"passed"},indent=2))
if __name__=="__main__": main()
