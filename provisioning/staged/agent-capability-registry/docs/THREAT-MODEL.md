# Threat model

Capability declarations are untrusted input. Strict validation, immutable snapshots of registered attributes, bounded requirement counts and bounded storage reduce mutation, malformed-input and resource-exhaustion risks. Declarations remain assertions, not proof. Policy callback absence, denial, non-boolean responses or exceptions exclude candidates. This prototype has no identity lifecycle, cryptographic attestation, production authorization, distributed consistency, transport security or execution isolation. Never use it alone as a security control.
