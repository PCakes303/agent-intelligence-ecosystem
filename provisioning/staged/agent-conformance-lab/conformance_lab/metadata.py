"""Consistency checks for repository metadata; not interoperability proof."""
from __future__ import annotations

from typing import Any, Mapping

class ConformanceError(ValueError):
    """Raised when a local contract declaration is inconsistent."""

def validate_repository_metadata(manifest: Mapping[str, Any], capabilities: Mapping[str, Any], compatibility: Mapping[str, Any]) -> dict[str, Any]:
    if not all(isinstance(item, Mapping) for item in (manifest, capabilities, compatibility)):
        raise ConformanceError("repository metadata documents must be objects")
    repo_id = manifest.get("id")
    if not isinstance(repo_id, str) or capabilities.get("repository_id") != repo_id or compatibility.get("repository") != manifest.get("name"):
        raise ConformanceError("repository identity fields do not agree")
    if manifest.get("maturity") != capabilities.get("maturity"):
        raise ConformanceError("manifest and capabilities maturity differ")
    dependencies = manifest.get("dependencies")
    compat_dependencies = compatibility.get("dependencies")
    if not isinstance(dependencies, list) or not isinstance(compat_dependencies, list):
        raise ConformanceError("dependency declarations must be arrays")
    if len(dependencies) != len(set(dependencies)):
        raise ConformanceError("manifest contains duplicate dependencies")
    compat_ids = [item.get("repository_id") for item in compat_dependencies if isinstance(item, Mapping)]
    if len(compat_ids) != len(compat_dependencies) or len(compat_ids) != len(set(compat_ids)):
        raise ConformanceError("compatibility dependency entries are malformed or duplicated")
    if set(dependencies) != set(compat_ids):
        raise ConformanceError("manifest and compatibility dependencies differ")
    caps = capabilities.get("capabilities")
    if not isinstance(caps, list):
        raise ConformanceError("capabilities must be an array")
    cap_ids = [item.get("id") for item in caps if isinstance(item, Mapping)]
    if len(cap_ids) != len(caps) or len(cap_ids) != len(set(cap_ids)):
        raise ConformanceError("capability IDs are malformed or duplicated")
    non_caps = capabilities.get("explicit_non_capabilities")
    if not isinstance(non_caps, list) or not non_caps:
        raise ConformanceError("explicit non-capabilities must be declared")
    return {"status":"PASS","repository_id":repo_id,"capabilities":len(caps),"dependencies":len(dependencies),"scope":"local metadata consistency only"}
