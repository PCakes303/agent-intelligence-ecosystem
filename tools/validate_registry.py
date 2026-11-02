#!/usr/bin/env python3
"""Validate the public ecosystem registry and its dependency graph."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot load {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def validate_registry(registry: dict[str, Any], schema: dict[str, Any], graph: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    errors.extend(f"registry schema: {e.message} at {list(e.absolute_path)}"
                  for e in Draft202012Validator(schema).iter_errors(registry))
    repos = registry.get("repositories", [])
    ids = [r.get("id") for r in repos]
    names = [r.get("name") for r in repos]
    if len(ids) != len(set(ids)):
        errors.append("duplicate repository IDs")
    if len(names) != len(set(names)):
        errors.append("duplicate repository names")
    id_set = set(ids)
    by_id = {r.get("id"): r for r in repos}
    for repo in repos:
        unknown = set(repo.get("dependencies", [])) - id_set
        if unknown:
            errors.append(f"{repo.get('id')}: unknown dependencies {sorted(unknown)}")
        if repo.get("visibility") == "private" and repo.get("public_export", False) is not False:
            errors.append(f"{repo.get('id')}: private repository must set public_export=false")

    edges = graph.get("edges", [])
    excluded = set(graph.get("excluded", []))
    private_ids = {r.get("id") for r in repos if r.get("visibility") == "private"}
    if excluded != private_ids:
        errors.append(f"dependency graph excluded nodes {sorted(excluded)} do not match private IDs {sorted(private_ids)}")
    adjacency = {node: [] for node in id_set}
    seen_edges: set[tuple[str, str]] = set()
    for edge in edges:
        if not isinstance(edge, list) or len(edge) != 2:
            errors.append(f"invalid dependency edge: {edge!r}")
            continue
        source, target = edge
        if source not in id_set or target not in id_set:
            errors.append(f"unknown dependency node: {source}->{target}")
            continue
        if source in private_ids or target in private_ids:
            errors.append(f"private repository leaked into public dependency graph: {source}->{target}")
        if (source, target) in seen_edges:
            errors.append(f"duplicate dependency edge: {source}->{target}")
        seen_edges.add((source, target))
        adjacency[source].append(target)

    state: dict[str, int] = {}
    def visit(node: str, trail: list[str]) -> None:
        if state.get(node) == 1:
            errors.append("dependency cycle: " + " -> ".join(trail + [node]))
            return
        if state.get(node) == 2:
            return
        state[node] = 1
        for dep in adjacency.get(node, []):
            visit(dep, trail + [node])
        state[node] = 2
    for node in id_set:
        if state.get(node, 0) == 0:
            visit(node, [])

    # The registry's dependency declarations and graph edges must agree exactly.
    declared = {(r.get("id"), dep) for r in repos for dep in r.get("dependencies", [])}
    if declared != seen_edges:
        errors.append(
            f"dependency mismatch: {len(declared - seen_edges)} declared edges missing from graph; "
            f"{len(seen_edges - declared)} graph edges not declared by manifests"
        )
    if len(repos) != registry.get("counts", {}).get("total"):
        errors.append("registry count does not match repository entry count")
    if sum(r.get("visibility") == "public" for r in repos) != registry.get("counts", {}).get("public"):
        errors.append("public repository count mismatch")
    if sum(r.get("visibility") == "private" for r in repos) != registry.get("counts", {}).get("private"):
        errors.append("private repository count mismatch")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        registry = load_json(root / "registry/repositories.json")
        schema = load_json(root / "schemas/repository-registry.schema.json")
        graph = load_json(root / "registry/dependencies.json")
        errors = validate_registry(registry, schema, graph)
        manifest_schema = load_json(root / "schemas/repository-manifest.schema.json")
        manifest_template = load_json(root / "templates/repository/manifest.json")
        errors.extend(
            f"manifest template: {e.message} at {list(e.absolute_path)}"
            for e in Draft202012Validator(manifest_schema).iter_errors(manifest_template)
        )
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {len(registry['repositories'])} repositories; {len(graph['edges'])} dependency edges; manifest template valid; private nodes excluded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
