#!/usr/bin/env python3
"""Validate the starter supply-chain artifact record (stdlib only)."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
def validate(d):
    errors=[]
    if not isinstance(d,dict): return ["record must be an object"]
    if d.get("record_version")!="1.0": errors.append("record_version must be 1.0")
    a=d.get("artifact")
    if not isinstance(a,dict): errors.append("artifact must be an object")
    else:
        for k in ("name","version"):
            if not isinstance(a.get(k),str) or not a[k].strip(): errors.append(f"artifact.{k} must be non-empty")
        digest=a.get("digest")
        if not isinstance(digest,dict) or digest.get("algorithm")!="sha256" or not isinstance(digest.get("value"),str) or not re.fullmatch(r"[a-fA-F0-9]{64}",digest["value"]):
            errors.append("artifact.digest must contain a 64-character SHA-256 hex value")
    s=d.get("source")
    if not isinstance(s,dict): errors.append("source must be an object")
    else:
        u=urlparse(s.get("repository",""))
        if u.scheme!="https" or not u.netloc: errors.append("source.repository must be an HTTPS URI")
        if not isinstance(s.get("commit"),str) or not re.fullmatch(r"[a-fA-F0-9]{40,64}",s["commit"]): errors.append("source.commit must be a 40-64 character hex commit")
    b=d.get("sbom")
    if not isinstance(b,dict) or b.get("format") not in {"SPDX","CycloneDX"}: errors.append("sbom.format must be SPDX or CycloneDX")
    elif not isinstance(b.get("uri"),str) or urlparse(b["uri"]).scheme!="https": errors.append("sbom.uri must be HTTPS")
    v=d.get("verification")
    if not isinstance(v,dict) or not isinstance(v.get("signature_present"),bool) or not isinstance(v.get("signature_verified"),bool): errors.append("verification must declare boolean signature_present and signature_verified")
    elif v["signature_verified"] and not v["signature_present"]: errors.append("a signature cannot be verified when none is present")
    return errors

if __name__=="__main__":
    p=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/"examples/supply-chain-artifact.json"
    try: data=json.loads(p.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as exc: print(exc,file=sys.stderr); raise SystemExit(2)
    errors=validate(data)
    if errors: print("\n".join(errors),file=sys.stderr); raise SystemExit(1)
    print("supply-chain record structure valid; cryptographic verification not performed")
