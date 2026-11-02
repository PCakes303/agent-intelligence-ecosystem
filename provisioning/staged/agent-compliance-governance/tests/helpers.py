import json
from pathlib import Path
from compliance_governance.registry import load_json

ROOT = Path(__file__).resolve().parents[1]

def documents():
    return (
        load_json(ROOT / "registry" / "legal-applicability.json"),
        load_json(ROOT / "registry" / "control-catalog.json"),
        load_json(ROOT / "registry" / "evidence-index.json"),
    )
