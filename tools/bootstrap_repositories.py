#!/usr/bin/env python3
"""Render public repository starter trees from the canonical portfolio registry.

This tool creates local scaffold directories only. It does not create GitHub
repositories, change visibility, configure permissions, or publish anything.
Private repository metadata is intentionally excluded from generated output.
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render(output: Path, force: bool = False) -> list[str]:
    registry = json.loads((ROOT / "registry/repositories.json").read_text(encoding="utf-8"))
    template = ROOT / "templates/repository"
    output.mkdir(parents=True, exist_ok=True)
    created: list[str] = []
    for repo in registry["repositories"]:
        if repo["visibility"] != "public" or repo["id"] == "master":
            continue
        target = output / repo["name"]
        if target.exists():
            if not force:
                raise FileExistsError(f"{target} already exists; rerun with --force to replace generated scaffold")
            shutil.rmtree(target)
        shutil.copytree(template, target)
        manifest = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": f"https://github.com/PCakes303/{repo['name']}/blob/main/manifest.json",
            "manifest_version": "1.0.0",
            "id": repo["id"],
            "name": repo["name"],
            "visibility": "public",
            "maturity": repo["status"],
            "summary": repo["role"],
            "license": {
                "expression": None,
                "status": "pending-review",
                "notes": "Select after legal and third-party dependency review."
            },
            "interfaces": [],
            "dependencies": [
                {"id": dep, "constraint": "unreleased", "kind": "contract"}
                for dep in repo["dependencies"]
            ],
            "security": {
                "threat_model": "docs/THREAT_MODEL.md",
                "secrets_in_repository": False,
                "data_classification": "public",
                "security_contact": None
            },
            "repository_url": f"https://github.com/PCakes303/{repo['name']}",
            "default_branch": "main",
            "compatibility": [],
            "evidence": []
        }
        (target / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        readme_path = target / "README.md"
        readme = readme_path.read_text(encoding="utf-8")
        readme = readme.replace("<repository-name>", repo["name"])
        readme = readme.replace(
            "Describe the problem this repository solves, its intended users, and its explicit non-goals.",
            repo["role"]
        )
        readme += (
            "\n## Ecosystem relationships\n\n"
            f"Registry ID: {repo['id']}.\n\n"
            f"Declared prerequisites: {', '.join(repo['dependencies']) if repo['dependencies'] else 'none'}.\n"
        )
        readme_path.write_text(readme, encoding="utf-8")
        created.append(repo["name"])
    output.mkdir(parents=True, exist_ok=True)
    (output / "SCAFFOLD-REPORT.json").write_text(
        json.dumps({"generated_from": "registry/repositories.json", "count": len(created),
                    "visibility": "public-only", "repositories": created}, indent=2) + "\n",
        encoding="utf-8"
    )
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("dist/public-repositories"))
    parser.add_argument("--force", action="store_true", help="replace existing generated scaffold directories")
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    created = render(output, force=args.force)
    print(f"Generated {len(created)} public repository scaffolds in {output}")
    print("No GitHub repositories were created or modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
