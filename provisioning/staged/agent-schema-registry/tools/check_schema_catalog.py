import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def check():
 paths=sorted((ROOT/"schemas").rglob("*.schema.json")); errors=[]
 if not paths: return ["no schema documents found"]
 ids=set()
 for p in paths:
  try: d=json.loads(p.read_text(encoding="utf-8"))
  except (OSError,json.JSONDecodeError) as e: errors.append(f"{p}: {e}"); continue
  for k in ("$schema","$id","title","type"):
   if not d.get(k): errors.append(f"{p}: missing {k}")
  if d.get("$schema")!="https://json-schema.org/draft/2020-12/schema": errors.append(f"{p}: expected Draft 2020-12")
  if d.get("$id") in ids: errors.append(f"{p}: duplicate $id")
  ids.add(d.get("$id"))
 return errors
if __name__=="__main__":
 errors=check()
 if errors: print("\n".join(errors),file=sys.stderr); sys.exit(1)
 print("schema catalog structural checks passed")
