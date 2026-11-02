"""CLI for validating legal register, control catalogue and evidence index."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from .registry import RegistryError, validate_repository

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate compliance governance metadata (not legal applicability).")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="repository root")
    args = parser.parse_args()
    try:
        result = validate_repository(args.root.resolve())
    except (RegistryError, OSError) as exc:
        print(json.dumps({"status": "invalid", "error": str(exc)}, indent=2))
        return 1
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
