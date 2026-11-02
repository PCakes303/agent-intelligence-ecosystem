#!/usr/bin/env python3
"""Run the ecosystem's entry-level build checks."""
from pathlib import Path
import subprocess
import sys
root=Path(__file__).resolve().parents[1]
commands=[
 [sys.executable,"tools/validate_registry.py"],
 [sys.executable,"tools/validate_foundation_requirements.py"],
 [sys.executable,"tools/validate_supply_chain.py"],
 [sys.executable,"tools/validate_audit_event.py"],
 [sys.executable,"tools/validate_aix_message.py"],
 [sys.executable,"tools/evaluate_policy.py","--policy","prototypes/policy/examples/policy.json","--request","prototypes/policy/examples/allow-request.json"],
 [sys.executable,"-m","unittest","discover","-s","tests","-v"],
]
for command in commands:
 result=subprocess.run(command,cwd=root)
 if result.returncode:
  raise SystemExit(result.returncode)
print("Starter build passed: registry, foundation, supply chain, audit event, AIX message, policy example, and test suite.")
