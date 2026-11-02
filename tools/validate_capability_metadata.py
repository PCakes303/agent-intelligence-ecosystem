#!/usr/bin/env python3
"""Validate capability and compatibility metadata against the ecosystem's governed contract."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO_ID = re.compile(r"^[a-z0-9-]+$")
MATURITY = {"planned","research","scaffolding","experimental","alpha","beta","stable","maintenance","deprecated","archived"}
CAP_STATUS = {"planned","scaffolded","implemented","tested","released"}
COMPAT_STATUS = {"declared","tested","unsupported"}

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def validate_capabilities(data, expected_repo=None):
    errors=[]
    required={"capabilities_version","repository","repository_id","maturity","capabilities","explicit_non_capabilities"}
    if set(data)-required or required-set(data): errors.append("capabilities: incorrect top-level fields")
    if data.get("capabilities_version")!="1.1.0": errors.append("capabilities: version must be 1.1.0")
    if not REPO_ID.fullmatch(str(data.get("repository",""))): errors.append("capabilities: invalid repository")
    if expected_repo and data.get("repository")!=expected_repo: errors.append("capabilities: repository mismatch")
    if not REPO_ID.fullmatch(str(data.get("repository_id",""))): errors.append("capabilities: invalid repository_id")
    if data.get("maturity") not in MATURITY: errors.append("capabilities: invalid maturity")
    if not isinstance(data.get("capabilities"),list): errors.append("capabilities: capabilities must be an array")
    else:
        ids=set()
        for i,cap in enumerate(data["capabilities"]):
            if not isinstance(cap,dict): errors.append(f"capabilities[{i}]: must be object"); continue
            req={"id","name","status","description","evidence"}
            if set(cap)-req-{"limitations"} or req-set(cap): errors.append(f"capabilities[{i}]: incorrect fields")
            if not isinstance(cap.get("id"),str) or not cap["id"]: errors.append(f"capabilities[{i}]: missing id")
            elif cap["id"] in ids: errors.append(f"capabilities[{i}]: duplicate id")
            else: ids.add(cap["id"])
            if cap.get("status") not in CAP_STATUS: errors.append(f"capabilities[{i}]: invalid status")
            if not isinstance(cap.get("evidence"),list): errors.append(f"capabilities[{i}]: evidence must be array")
            if cap.get("status")!="planned" and not cap.get("evidence"): errors.append(f"capabilities[{i}]: non-planned claim needs evidence")
    for field in ("explicit_non_capabilities",):
        if not isinstance(data.get(field),list): errors.append(f"capabilities: {field} must be array")
    return errors

def validate_compatibility(data, expected_repo=None):
    errors=[]
    required={"compatibility_version","repository","policy","dependencies","tested_combinations","breaking_change_policy"}
    if set(data)!=required: errors.append("compatibility: incorrect top-level fields")
    if data.get("compatibility_version")!="1.1.0": errors.append("compatibility: version must be 1.1.0")
    if not REPO_ID.fullmatch(str(data.get("repository",""))): errors.append("compatibility: invalid repository")
    if expected_repo and data.get("repository")!=expected_repo: errors.append("compatibility: repository mismatch")
    seen=set()
    for i,dep in enumerate(data.get("dependencies",[])):
        if not isinstance(dep,dict) or set(dep)!={"repository_id","version_range","status","evidence"}:
            errors.append(f"compatibility.dependencies[{i}]: incorrect shape"); continue
        rid=dep["repository_id"]
        if not REPO_ID.fullmatch(str(rid)): errors.append(f"compatibility.dependencies[{i}]: invalid repository_id")
        if rid in seen: errors.append(f"compatibility.dependencies[{i}]: duplicate dependency")
        seen.add(rid)
        if dep["status"] not in COMPAT_STATUS: errors.append(f"compatibility.dependencies[{i}]: invalid status")
        if dep["status"]=="tested" and not dep["evidence"]: errors.append(f"compatibility.dependencies[{i}]: tested claim needs evidence")
    for i,item in enumerate(data.get("tested_combinations",[])):
        if not isinstance(item,dict) or set(item)!={"repositories","result","evidence"}:
            errors.append(f"compatibility.tested_combinations[{i}]: incorrect shape"); continue
        if item["result"] not in {"passed","failed"} or not item["evidence"]:
            errors.append(f"compatibility.tested_combinations[{i}]: result and evidence required")
    return errors

def main():
    errors=[]
    for repo in sorted(p for p in ROOT.iterdir() if p.is_dir() and (p/"capabilities.json").exists() and (p/"compatibility.json").exists()):
        try:
            errors += [f"{repo.name}: {e}" for e in validate_capabilities(load(repo/"capabilities.json"),repo.name)]
            errors += [f"{repo.name}: {e}" for e in validate_compatibility(load(repo/"compatibility.json"),repo.name)]
        except (OSError,json.JSONDecodeError) as exc: errors.append(f"{repo.name}: {exc}")
    if errors:
        print("\n".join(errors)); return 1
    print("Capability and compatibility metadata validation passed.")
    return 0

if __name__=="__main__": raise SystemExit(main())
