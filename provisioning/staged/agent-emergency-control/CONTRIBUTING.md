# Contributing

Contributions should improve the emergency-control contract, strict validation, deterministic state transitions, documentation or synthetic tests. Production adapters require a separate threat review and explicit integration plan.

## Development

- Python 3.10+
- Install: python -m pip install -r requirements-dev.txt
- Test: python -m unittest discover -s tests -v

Changes to STOP/RESUME semantics, quorum, epoch handling, scope matching, command lifetime or failure behavior require security-focused review and positive, negative and boundary tests. Never weaken fail-closed behavior to make a test pass. Do not include secrets, real signatures, personal information or incident evidence in examples or tests.
