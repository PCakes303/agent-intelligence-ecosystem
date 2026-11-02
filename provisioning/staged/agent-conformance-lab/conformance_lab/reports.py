"""Deterministic conformance report builder; reports are not signed or certified."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker

from .metadata import ConformanceError

_SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schemas" / "conformance-report.schema.json"
_SCHEMA = json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))
_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())

def _canonical(value: Any) -> bytes:
    try:
        return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode("utf-8")
    except (TypeError,ValueError,UnicodeError) as exc:
        raise ConformanceError("report is not canonical JSON") from exc

def _overall(checks: list[Mapping[str, Any]]) -> str:
    if not checks or any(item.get("status") == "FAIL" for item in checks):
        return "FAIL" if any(item.get("status") == "FAIL" for item in checks) else "BLOCKED"
    if any(item.get("status") == "BLOCKED" for item in checks):
        return "BLOCKED"
    return "PASS"

def build_report(*,suite_id:str,subject_repository:str,subject_commit:str,generated_at:str,checks:list[Mapping[str,Any]],limitations:list[str]) -> dict[str,Any]:
    normalized=[dict(item) for item in checks]
    if not normalized:
        normalized=[{"check_id":"suite.no-checks","status":"BLOCKED","description":"No conformance checks were executed.","evidence_refs":[],"limitations":["No evidence exists for this suite."]}]
    report={
        "report_version":"1.0","suite_id":suite_id,"subject_repository":subject_repository,
        "subject_commit":subject_commit,"generated_at":generated_at,
        "overall_status":_overall(normalized),"checks":normalized,
        "limitations":limitations or ["Local validation only; no live interoperability or certification."],
    }
    report["report_sha256"]=hashlib.sha256(_canonical(report)).hexdigest()
    validate_report(report)
    return report

def validate_report(report: Mapping[str,Any]) -> bool:
    errors=list(_VALIDATOR.iter_errors(report))
    if errors:
        raise ConformanceError(f"report schema error: {errors[0].message}")
    expected=_overall(report["checks"])
    if report["overall_status"] != expected:
        raise ConformanceError("overall_status does not match check results")
    unsigned={key:value for key,value in report.items() if key!="report_sha256"}
    digest=hashlib.sha256(_canonical(unsigned)).hexdigest()
    if report["report_sha256"] != digest:
        raise ConformanceError("report digest mismatch")
    return True
