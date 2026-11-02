#!/usr/bin/env python3
"""Validate an AIX experimental message against its Draft 2020-12 schema."""
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
def main():
    message_path=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/"prototypes/aix/examples/task-request.json"
    schema=json.loads((ROOT/"prototypes/aix/aix-message.schema.json").read_text(encoding="utf-8"))
    message=json.loads(message_path.read_text(encoding="utf-8"))
    errors=sorted(Draft202012Validator(schema,format_checker=Draft202012Validator.FORMAT_CHECKER).iter_errors(message),key=lambda e:list(e.absolute_path))
    if errors:
        for error in errors: print(f"{'/'.join(map(str,error.absolute_path))}: {error.message}",file=sys.stderr)
        return 1
    print("AIX experimental message is schema-valid; sender authentication and authorization are not performed.")
    return 0
if __name__=="__main__": raise SystemExit(main())
