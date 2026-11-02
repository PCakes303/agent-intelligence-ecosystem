#!/usr/bin/env python3
"""Validate public component capability and compatibility metadata."""
import json, re, sys
from pathlib import Path
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]
REPO_ID=re.compile(r"^[a-z0-9-]+$")
MATURITY={"planned","research","scaffolding","experimental","alpha","beta","stable","maintenance","deprecated","archived"}
CAP_STATUS={"planned","scaffolded","implemented","tested","released"}
COMPAT_STATUS={"declared","tested","unsupported"}

def load_text(raw): return json.loads(raw)
def validate_capabilities(data,expected_repo=None):
    errors=[]; required={"capabilities_version","repository","repository_id","maturity","capabilities","explicit_non_capabilities"}
    if set(data)!=required: errors.append("capabilities: incorrect top-level fields")
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
            cid=cap.get("id")
            if not isinstance(cid,str) or not cid: errors.append(f"capabilities[{i}]: missing id")
            elif cid in ids: errors.append(f"capabilities[{i}]: duplicate id")
            else: ids.add(cid)
            if cap.get("status") not in CAP_STATUS: errors.append(f"capabilities[{i}]: invalid status")
            if not isinstance(cap.get("evidence"),list): errors.append(f"capabilities[{i}]: evidence must be array")
            if cap.get("status")!="planned" and not cap.get("evidence"): errors.append(f"capabilities[{i}]: non-planned claim needs evidence")
    if not isinstance(data.get("explicit_non_capabilities"),list): errors.append("capabilities: explicit_non_capabilities must be array")
    return errors

def validate_compatibility(data,expected_repo=None):
    errors=[]; required={"compatibility_version","repository","policy","dependencies","tested_combinations","breaking_change_policy"}
    if set(data)!=required: errors.append("compatibility: incorrect top-level fields")
    if data.get("compatibility_version")!="1.1.0": errors.append("compatibility: version must be 1.1.0")
    if not REPO_ID.fullmatch(str(data.get("repository",""))): errors.append("compatibility: invalid repository")
    if expected_repo and data.get("repository")!=expected_repo: errors.append("compatibility: repository mismatch")
    seen=set()
    if not isinstance(data.get("dependencies"),list): errors.append("compatibility: dependencies must be array")
    else:
        for i,dep in enumerate(data["dependencies"]):
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

def fetch_json(url):
    req=Request(url,headers={"User-Agent":"MrCakes931-metadata-validator/1.0","Accept":"application/json"})
    with urlopen(req,timeout=20) as response: return json.loads(response.read().decode("utf-8"))

def main():
    registry=json.loads((ROOT/"registry/repositories.json").read_text(encoding="utf-8"))
    errors=[]; checked=0
    for entry in registry["repositories"]:
        if entry.get("visibility")!="public" or entry.get("id")=="master" or entry.get("status")=="planned": continue
        name=entry["name"]; base=f"https://raw.githubusercontent.com/PCakes303/{name}/main/"
        try:
            caps=fetch_json(base+"capabilities.json")
            compat=fetch_json(base+"compatibility.json")
            errors += [f"{name}: {e}" for e in validate_capabilities(caps,name)]
            errors += [f"{name}: {e}" for e in validate_compatibility(compat,name)]
            checked+=1
        except Exception as exc: errors.append(f"{name}: unable to retrieve/parse public metadata: {exc}")
    if errors: print("\n".join(errors)); return 1
    print(f"Capability and compatibility metadata validation passed for {checked} existing public component repositories.")
    return 0

if __name__=="__main__": raise SystemExit(main())
