#!/usr/bin/env python3
"""Validate traceability and dependency integrity in foundation requirements.

Uses only the Python standard library. JSON Schema validation is separately
performed by the repository's schema-validation workflow when configured.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ID_PATTERN = re.compile(r"^FND-[0-9]{3}$")
VALID_PRIORITIES = {"critical", "high", "medium", "low"}
VALID_DOMAINS = {
    "identity", "authorization", "data-integrity", "resource-description",
    "audit", "supply-chain", "resilience",
}
VALID_OWNERS = {
    "agent-foundation-spec", "agent-resource-manifest", "agent-schema-registry",
    "agent-identity-trust", "agent-secure-supply-chain", "agent-policy-engine",
    "agent-audit-provenance",
}


def validate(document: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(document, dict):
        return ["document must be a JSON object"]
    if document.get("status") not in {"proposed", "experimental", "approved", "deprecated"}:
        errors.append("status must be proposed, experimental, approved, or deprecated")
    requirements = document.get("requirements")
    if not isinstance(requirements, list) or not requirements:
        return errors + ["requirements must be a non-empty array"]

    by_id: dict[str, dict] = {}
    for index, item in enumerate(requirements):
        prefix = f"requirements[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        req_id = item.get("id")
        if not isinstance(req_id, str) or not ID_PATTERN.fullmatch(req_id):
            errors.append(f"{prefix}.id must match FND-NNN")
        elif req_id in by_id:
            errors.append(f"duplicate requirement id: {req_id}")
        else:
            by_id[req_id] = item
        for field in ("title", "statement"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{prefix}.{field} must be a non-empty string")
        if item.get("priority") not in VALID_PRIORITIES:
            errors.append(f"{prefix}.priority is invalid")
        if item.get("domain") not in VALID_DOMAINS:
            errors.append(f"{prefix}.domain is invalid")
        if item.get("owner") not in VALID_OWNERS:
            errors.append(f"{prefix}.owner is invalid")
        checks = item.get("verification")
        if not isinstance(checks, list) or not checks:
            errors.append(f"{prefix}.verification must be a non-empty array")
        dependencies = item.get("depends_on")
        if not isinstance(dependencies, list):
            errors.append(f"{prefix}.depends_on must be an array")
        elif len(dependencies) != len(set(dependencies)):
            errors.append(f"{prefix}.depends_on contains duplicates")

    for req_id, item in by_id.items():
        for dependency in item.get("depends_on", []):
            if dependency not in by_id:
                errors.append(f"{req_id} depends on unknown requirement {dependency}")
            elif dependency == req_id:
                errors.append(f"{req_id} cannot depend on itself")

    # Detect cycles among known requirement IDs.
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(req_id: str) -> None:
        if req_id in visiting:
            errors.append(f"dependency cycle detected at {req_id}")
            return
        if req_id in visited:
            return
        visiting.add(req_id)
        for dependency in by_id[req_id].get("depends_on", []):
            if dependency in by_id:
                visit(dependency)
        visiting.remove(req_id)
        visited.add(req_id)

    for req_id in by_id:
        visit(req_id)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", default="contracts/foundation/requirements.json")
    args = parser.parse_args()
    try:
        document = json.loads(Path(args.file).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    errors = validate(document)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {len(document['requirements'])} foundation requirements validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
