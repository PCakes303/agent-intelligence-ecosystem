#!/usr/bin/env python3
"""Run the ecosystem's entry-level build checks."""
from pathlib import Path
import subprocess
import sys
root=Path(__file__).resolve().parents[1]
commands=[
 [sys.executable,"tools/validate_registry.py"],
 [sys.executable,"tools/validate_foundation_requirements.py"],
 [sys.executable,"-m","unittest","discover","-s","tests","-v"],
]
for command in commands:
 result=subprocess.run(command,cwd=root)
 if result.returncode:
  raise SystemExit(result.returncode)
print("Starter build passed: registry, foundation requirements, and test suite.")
