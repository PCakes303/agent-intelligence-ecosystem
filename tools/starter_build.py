#!/usr/bin/env python3
"""Run the ecosystem's entry-level build checks and staged component checks."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
commands = [
    (root, [sys.executable, "tools/validate_registry.py"]),
    (root, [sys.executable, "tools/validate_public_agent_catalog.py"]),
    (root, [sys.executable, "tools/validate_capability_metadata.py"]),
    (root, [sys.executable, "tools/validate_foundation_requirements.py"]),
    (root, [sys.executable, "tools/validate_supply_chain.py"]),
    (root, [sys.executable, "tools/validate_audit_event.py"]),
    (root, [sys.executable, "tools/validate_aix_message.py"]),
    (root, [sys.executable, "tools/evaluate_policy.py", "--policy", "prototypes/policy/examples/policy.json", "--request", "prototypes/policy/examples/allow-request.json"]),
    (root, [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]),
    (root / "provisioning/staged/agent-policy-engine", [sys.executable, "tools/starter_build.py"]),
    (root / "provisioning/staged/agent-audit-provenance", [sys.executable, "tools/starter_build.py"]),
    (root / "provisioning/staged/aix-core", [sys.executable, "tools/starter_build.py"]),
]
for cwd, command in commands:
    result = subprocess.run(command, cwd=cwd)
    if result.returncode:
        raise SystemExit(result.returncode)
print("Starter build passed: master contracts, registry, policy prototype, regression suite, staged policy-engine component, and staged audit-provenance and AIX Core components.")
