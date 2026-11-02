#!/usr/bin/env python3
"""Evaluate a JSON policy request using the experimental default-deny PDP."""
import argparse
import json
import sys
from pathlib import Path

from policy_engine import validate_and_evaluate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--request", type=Path, required=True)
    root = Path(__file__).resolve().parents[1]
    args = parser.parse_args()
    try:
        policy = json.loads(args.policy.read_text(encoding="utf-8"))
        request = json.loads(args.request.read_text(encoding="utf-8"))
        policy_schema = json.loads((root / "prototypes/policy/policy.schema.json").read_text())
        request_schema = json.loads((root / "prototypes/policy/request.schema.json").read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"effect":"deny","decision_id":"input-error","reason":str(exc)}))
        return 2
    result = validate_and_evaluate(policy, request, policy_schema, request_schema)
    print(json.dumps(result, indent=2))
    return 0 if result["effect"] == "allow" else 1


if __name__ == "__main__":
    raise SystemExit(main())
