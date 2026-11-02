#!/usr/bin/env python3
"""Validate a resource manifest against the ecosystem contract."""
import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", nargs="?", type=Path, default=ROOT / "examples/agent-resource.example.json")
    parser.add_argument("--schema", type=Path, default=ROOT / "schemas/agent-resource.schema.json")
    args = parser.parse_args()
    try:
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
    errors = sorted(validator.iter_errors(manifest), key=lambda e: list(map(str, e.absolute_path)))
    if errors:
        for error in errors:
            print(f"ERROR: {error.message} at {list(error.absolute_path)}", file=sys.stderr)
        return 1
    print(f"OK: valid {manifest['resource_type']} resource manifest: {manifest['resource_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
