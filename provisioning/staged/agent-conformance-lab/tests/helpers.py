from datetime import datetime, timezone

NOW = "2026-11-02T12:00:00Z"
COMMIT = "a"*40

def envelope():
    return {
        "protocol_version":"1.0","message_id":"123e4567-e89b-12d3-a456-426614174000",
        "sender_id":"agent-a","recipient_id":"agent-b","message_type":"request",
        "created_at":NOW,"expires_at":"2026-11-02T12:01:00Z",
        "correlation_id":"123e4567-e89b-12d3-a456-426614174001",
        "payload_sha256":"b"*64,"ttl_seconds":60,"auth_ref":"auth-synthetic",
        "signature_ref":"signature-synthetic","scope":"public-metadata"
    }

def metadata_documents():
    manifest={"id":"test-repo","name":"test-repo","maturity":"scaffolded","dependencies":["foundation","policy"]}
    capabilities={"repository_id":"test-repo","maturity":"scaffolded","capabilities":[{"id":"test.capability"}],"explicit_non_capabilities":["network"]}
    compatibility={"repository":"test-repo","dependencies":[{"repository_id":"foundation"},{"repository_id":"policy"}]}
    return manifest,capabilities,compatibility

def check(check_id,status="PASS"):
    return {"check_id":check_id,"status":status,"description":"Synthetic conformance fixture result.","evidence_refs":["fixture:001"],"limitations":["Synthetic local evidence only."]}
