#!/usr/bin/env python3
"""Validate the public agent catalog against authoritative portfolio registries."""
import json
from pathlib import Path
import sys
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def validate(catalog=None, registry=None, status=None, schema=None):
    catalog = catalog or load(ROOT / "registry/public-agent-catalog.json")
    registry = registry or load(ROOT / "registry/repositories.json")
    status = status or load(ROOT / "registry/implementation-status.json")
    schema = schema or load(ROOT / "schemas/public-agent-catalog.schema.json")
    errors = [f"schema: {e.message}" for e in Draft202012Validator(schema).iter_errors(catalog)]
    public = {r["name"]: r for r in registry["repositories"] if r["visibility"] == "public"}
    observed = {r["name"]: r for r in catalog["repositories"]}
    if catalog["repository_count"] != len(catalog["repositories"]):
        errors.append("repository_count does not match catalog length")
    if set(observed) != set(public):
        errors.append("catalog repositories do not exactly match public registry")
    if len(observed) != len(catalog["repositories"]):
        errors.append("duplicate repository names in catalog")
    status_by_name = {r["name"]: r for r in status["repositories"]}
    for name, item in observed.items():
        source = public.get(name)
        if not source:
            continue
        if item["id"] != source["id"] or item["dependencies"] != source["dependencies"]:
            errors.append(f"{name}: id or dependencies drift from authoritative registry")
        if item["role"] != source["role"] or item["layer"] != source["layer"]:
            errors.append(f"{name}: role or layer drift from authoritative registry")
        if item["visibility"] != "public":
            errors.append(f"{name}: non-public item leaked into public catalog")
        recorded = status_by_name.get(name)
        if recorded and (item["existence"] != recorded.get("existence") or item["implementation_status"] != recorded.get("status")):
            errors.append(f"{name}: existence or maturity drift from implementation status")
        if "private" in name.lower() or "agent-ecosystem-private" in item["repository_url"]:
            errors.append(f"{name}: private repository reference in public catalog")
    if catalog["repository_count"] != registry["counts"]["public"]:
        errors.append("catalog count does not match public registry count")
    return errors

if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        raise SystemExit(1)
    print("Public agent catalog valid: all public registry entries represented; private portfolio entry excluded.")
