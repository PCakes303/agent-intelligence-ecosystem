import json, sys
from pathlib import Path

def validate(doc):
    errors=[]
    if not isinstance(doc,dict) or not isinstance(doc.get("requirements"),list): return ["requirements must be an array"]
    seen=set()
    for i,item in enumerate(doc["requirements"]):
        if not isinstance(item,dict): errors.append(f"requirements[{i}] must be an object"); continue
        for k in ("id","title","statement","priority"):
            if not isinstance(item.get(k),str) or not item[k].strip(): errors.append(f"requirements[{i}].{k} must be non-empty")
        if isinstance(item.get("id"),str):
            if item["id"] in seen: errors.append("duplicate requirement id: "+item["id"])
            seen.add(item["id"])
        if item.get("priority") not in {"MUST","SHOULD","MAY"}: errors.append(f"requirements[{i}].priority must be MUST, SHOULD, or MAY")
    return errors

if __name__=="__main__":
    p=Path(sys.argv[1]) if len(sys.argv)>1 else Path("requirements/requirements.json")
    try: d=json.loads(p.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as e: print(e,file=sys.stderr); sys.exit(2)
    errors=validate(d)
    if errors: print("\n".join(errors),file=sys.stderr); sys.exit(1)
    print(f"validated {len(d['requirements'])} requirements")
