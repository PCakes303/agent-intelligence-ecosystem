"""Pure fail-closed stop/resume reducer; adapters and enforcement are out of scope."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .commands import EmergencyCommand, Scope

class TransitionError(ValueError):
    """Raised when a transition cannot be proven safe."""

@dataclass(frozen=True)
class StopState:
    epoch: int = 0
    active: bool = False
    scope: Scope | None = None
    command_id: str | None = None

@dataclass(frozen=True)
class VerificationEvidence:
    signature_valid: bool = False
    actor_authorized: bool = False
    revocation_clear: bool = False
    command_fresh: bool = False
    resume_quorum_valid: bool = False
    resume_policy_allowed: bool = False

class CommandVerifier(Protocol):
    """Trusted integration boundary; implementation must verify signatures and authority."""
    def verify(self, command: EmergencyCommand) -> VerificationEvidence: ...

def _require_true(value: object, name: str) -> None:
    if value is not True:
        raise TransitionError(f"deny:{name}")

def apply_command(current: StopState, command: EmergencyCommand, verifier: CommandVerifier) -> StopState:
    """Return a proposed next state only; callers must persist, audit and propagate safely."""
    if not isinstance(current, StopState) or not isinstance(command, EmergencyCommand):
        raise TransitionError("deny:invalid-input")
    if verifier is None or not callable(getattr(verifier, "verify", None)):
        raise TransitionError("deny:verifier-unavailable")
    try:
        evidence = verifier.verify(command)
    except Exception as exc:
        raise TransitionError("deny:verification-error") from exc
    if not isinstance(evidence, VerificationEvidence):
        raise TransitionError("deny:invalid-verification-evidence")
    _require_true(evidence.signature_valid, "signature")
    _require_true(evidence.actor_authorized, "actor-authorization")
    _require_true(evidence.revocation_clear, "revocation")
    _require_true(evidence.command_fresh, "freshness")
    if command.epoch <= current.epoch:
        raise TransitionError("deny:stale-or-replayed-epoch")
    if current.active and current.scope != command.scope:
        raise TransitionError("deny:active-scope-conflict")
    if command.action == "STOP":
        # Emergency STOP is deliberately not subject to ordinary policy veto.
        return StopState(epoch=command.epoch, active=True, scope=command.scope, command_id=command.command_id)
    if command.action == "RESUME":
        if current.active is not True or current.scope != command.scope:
            raise TransitionError("deny:no-matching-active-stop")
        _require_true(evidence.resume_quorum_valid, "resume-quorum")
        _require_true(evidence.resume_policy_allowed, "resume-policy")
        return StopState(epoch=command.epoch, active=False, scope=command.scope, command_id=command.command_id)
    raise TransitionError("deny:unknown-action")
