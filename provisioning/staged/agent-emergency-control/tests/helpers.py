import json
from datetime import datetime, timedelta, timezone
from uuid import uuid4

def command(action="STOP", epoch=1, now=None, scope=None, approvals=None):
    now = now or datetime.now(timezone.utc)
    scope = scope or {"kind": "global", "id": "*"}
    approvals = approvals if approvals is not None else []
    return {
        "command_version": "1.0",
        "command_id": str(uuid4()),
        "epoch": epoch,
        "action": action,
        "scope": scope,
        "issued_at": now.isoformat().replace("+00:00", "Z"),
        "expires_at": (now + timedelta(minutes=4)).isoformat().replace("+00:00", "Z"),
        "actor": {"principal_id": "operator-1", "key_id": "test-key", "signature": "TEST-ONLY-NOT-A-REAL-SIGNATURE-000000"},
        "reason": "Synthetic test emergency control event",
        "approvals": approvals,
    }

def approval(name):
    return {"principal_id": name, "key_id": "test-key-" + name, "signature": "TEST-ONLY-NOT-A-REAL-SIGNATURE-000000"}
