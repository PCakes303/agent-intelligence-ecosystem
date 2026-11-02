# Threat model

Capability declarations are untrusted input. Strict validation and bounded storage reduce malformed-input and resource-exhaustion risks. Declarations are assertions, not proof. Policy callback absence, denial or exceptions exclude candidates. This prototype has no identity lifecycle, cryptographic attestation, production authorization, distributed consistency, transport security or execution isolation. Never use it alone as a security control.
