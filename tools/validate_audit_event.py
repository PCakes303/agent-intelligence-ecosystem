#!/usr/bin/env python3
"""Validate the starter audit event contract using the Python standard library."""
import json, sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
EVENT_TYPES={"authentication","authorization","tool_invocation","delegation","data_access","build","release","administrative_change"}
OUTCOMES={"success","denied","failure","unknown"}
CLASSIFICATIONS={"public","internal","confidential","restricted"}
def validate(d):
    e=[]
    if not isinstance(d,dict): return ["event must be an object"]
    for k in ("event_id","action"):
        if not isinstance(d.get(k),str) or not d[k].strip(): e.append(f"{k} must be non-empty")
    if d.get("event_type") not in EVENT_TYPES: e.append("event_type is unsupported")
    if d.get("outcome") not in OUTCOMES: e.append("outcome is unsupported")
    if d.get("data_classification") not in CLASSIFICATIONS: e.append("data_classification is unsupported")
    try: datetime.fromisoformat(d.get("occurred_at","").replace("Z","+00:00"))
    except (ValueError,AttributeError): e.append("occurred_at must be ISO-8601 date-time")
    actor=d.get("actor")
    if not isinstance(actor,dict) or not isinstance(actor.get("principal_id"),str) or not actor["principal_id"].strip(): e.append("actor.principal_id must be non-empty")
    elif actor.get("issuer") is not None:
        u=urlparse(actor["issuer"])
        if u.scheme!="https" or not u.netloc: e.append("actor.issuer must be HTTPS")
    if "target" in d and d["target"] is not None and not isinstance(d["target"],str): e.append("target must be string or null")
    if "correlation_id" in d and d["correlation_id"] is not None and not isinstance(d["correlation_id"],str): e.append("correlation_id must be string or null")
    if "policy_version" in d and d["policy_version"] is not None and not isinstance(d["policy_version"],str): e.append("policy_version must be string or null")
    refs=d.get("evidence_refs",[])
    if not isinstance(refs,list) or any(not isinstance(x,str) or urlparse(x).scheme!="https" for x in refs): e.append("evidence_refs must be HTTPS URI strings")
    return e
if __name__=="__main__":
    p=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/"examples/audit-provenance-event.json"
    try: data=json.loads(p.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as exc: print(exc,file=sys.stderr); raise SystemExit(2)
    errors=validate(data)
    if errors: print("\n".join(errors),file=sys.stderr); raise SystemExit(1)
    print("audit event structure valid; authenticity and completeness not established")
