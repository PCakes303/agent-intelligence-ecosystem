#!/usr/bin/env python3
"""Generate a public repository directory from the master registry JSON."""
import argparse
import json
from pathlib import Path

def render(registry):
    if not isinstance(registry, dict) or not isinstance(registry.get("repositories"), list):
        raise ValueError("registry must contain a repositories array")
    rows=[]
    for item in registry["repositories"]:
        if item.get("visibility") != "public":
            continue
        name=item.get("name")
        if not isinstance(name,str) or not name:
            raise ValueError("public repository is missing a valid name")
        rows.append((item.get("layer","other"),name,item.get("role","")))
    rows.sort(key=lambda x:(x[0],x[1]))
    lines=["# Public repository directory","","> Generated from the master registry. The registry remains authoritative.",""]
    current=None
    for layer,name,role in rows:
        if layer != current:
            current=layer
            lines.extend([f"## {layer.replace('-', ' ').title()}",""])
        lines.append(f"- [{name}](https://github.com/PCakes303/{name}) — {role}")
    lines.append("")
    return "\n".join(lines)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry",type=Path,help="local copy of registry/repositories.json")
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    data=json.loads(args.registry.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(render(data),encoding="utf-8")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
