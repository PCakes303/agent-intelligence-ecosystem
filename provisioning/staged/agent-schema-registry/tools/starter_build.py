#!/usr/bin/env python3
"""Run the entry-level schema catalog build."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.check_schema_catalog import check
root=Path(__file__).resolve().parents[1]
errors=check()
if errors: raise SystemExit("\n".join(errors))
schemas=list((root/"schemas").rglob("*.schema.json"))
print(json.dumps({"build_tier":"starter","project":"agent-schema-registry","schemas":len(schemas),"result":"passed"},indent=2))
