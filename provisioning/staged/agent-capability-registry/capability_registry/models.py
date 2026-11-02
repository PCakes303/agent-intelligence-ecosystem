"""Capability declaration models and strict validation."""
from dataclasses import dataclass, field
from collections.abc import Mapping
import re

_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
_VERSION = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


class ValidationError(ValueError):
    pass


@dataclass(frozen=True)
class Capability:
    capability_id: str
    agent_id: str
    description: str
    version: str
    attributes: Mapping[str, str] = field(default_factory=dict)

    def validate(self):
        if not isinstance(self.capability_id, str) or not _ID.fullmatch(self.capability_id):
            raise ValidationError("capability_id is invalid")
        if not isinstance(self.agent_id, str) or not _ID.fullmatch(self.agent_id):
            raise ValidationError("agent_id is invalid")
        if not isinstance(self.description, str) or not self.description.strip() or len(self.description) > 1024:
            raise ValidationError("description must contain 1..1024 characters")
        if not isinstance(self.version, str) or not _VERSION.fullmatch(self.version):
            raise ValidationError("version must be numeric major.minor.patch")
        if not isinstance(self.attributes, Mapping) or len(self.attributes) > 32:
            raise ValidationError("attributes must be a dictionary of at most 32 entries")
        for key, value in self.attributes.items():
            if not isinstance(key, str) or not _ID.fullmatch(key):
                raise ValidationError("attribute key is invalid")
            if not isinstance(value, str) or len(value) > 256:
                raise ValidationError("attribute values must be strings of at most 256 characters")


@dataclass(frozen=True)
class Requirement:
    capability_id: str
    attributes: dict[str, str] = field(default_factory=dict)

    def validate(self):
        if not isinstance(self.capability_id, str) or not _ID.fullmatch(self.capability_id):
            raise ValidationError("required capability_id is invalid")
        if not isinstance(self.attributes, dict) or len(self.attributes) > 32:
            raise ValidationError("requirement attributes must be a dictionary of at most 32 entries")
        for key, value in self.attributes.items():
            if not isinstance(key, str) or not _ID.fullmatch(key) or not isinstance(value, str) or len(value) > 256:
                raise ValidationError("requirement attributes must contain bounded string pairs")
