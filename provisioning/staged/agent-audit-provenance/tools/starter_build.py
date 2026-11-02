#!/usr/bin/env python3
"""Run local audit-provenance starter checks."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], cwd=ROOT, check=True)
with tempfile.TemporaryDirectory() as tmp:
    log = Path(tmp) / "events.jsonl"
    subprocess.run([sys.executable, "tools/audit_log.py", "append", "--log", str(log), "--event", "examples/event.json"], cwd=ROOT, check=True)
    result = subprocess.run([sys.executable, "tools/audit_log.py", "verify", "--log", str(log)], cwd=ROOT, check=True, capture_output=True, text=True)
    payload = json.loads(result.stdout)
    if payload.get("status") != "valid" or payload.get("events_verified") != 1:
        raise SystemExit("audit log CLI smoke test failed")
print("Audit provenance starter build passed.")
