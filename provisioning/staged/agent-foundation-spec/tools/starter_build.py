#!/usr/bin/env python3
"""Run the entry-level foundation contract build."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.validate_requirements import validate
root=Path(__file__).resolve().parents[1]
data=json.loads((root/"requirements/requirements.json").read_text(encoding="utf-8"))
errors=validate(data)
if errors: raise SystemExit("\n".join(errors))
print(json.dumps({"build_tier":"starter","project":"agent-foundation-spec","requirements":len(data["requirements"]),"result":"passed"},indent=2))
