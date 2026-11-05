#!/usr/bin/env python3
"""Run the entry-level public-guide integrity build."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/"manifest.json").read_text(encoding="utf-8"))
required=("id","name","visibility","maturity","summary","repository_url")
missing=[key for key in required if not manifest.get(key)]
if missing: raise SystemExit("manifest missing: "+", ".join(missing))
if manifest["visibility"]!="public": raise SystemExit("public guide must not describe a private repository as public")
docs=sorted(p.relative_to(root).as_posix() for p in (root/"docs").glob("*.md"))
if not docs: raise SystemExit("no guide documentation found")
print(json.dumps({"build_tier":"starter","project":"mrcakes931-ecosystem","docs":docs,"result":"passed"},indent=2))
