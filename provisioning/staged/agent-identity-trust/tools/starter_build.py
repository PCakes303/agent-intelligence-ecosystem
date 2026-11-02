#!/usr/bin/env python3
"""Run the entry-level identity-contract build."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.validate_principal import validate
root=Path(__file__).resolve().parents[1]
sample=json.loads((root/"examples/principal.json").read_text(encoding="utf-8"))
errors=validate(sample)
if errors: raise SystemExit("\n".join(errors))
print(json.dumps({"build_tier":"starter","project":"agent-identity-trust","principal_id":sample["principal_id"],"result":"passed","note":"record validation is not authentication"},indent=2))
