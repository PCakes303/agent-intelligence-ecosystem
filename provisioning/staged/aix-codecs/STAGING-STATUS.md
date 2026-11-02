# Staging status

Repository 12 (`aix-codecs`) prepared as a standalone build packet in the master control plane.

- RFC 8785 canonical JSON contract: drafted.
- Strict UTF-8 JSON decoder: drafted.
- Duplicate-key and non-standard-number rejection: drafted.
- Positive and negative unit tests: included.
- Pinned development dependency: included.
- GitHub Actions workflow: included.
- Cross-language conformance, fuzzing, schema-bound message validation, payload/depth limits, release signing, and production readiness: not implemented.
- License: pending portfolio mixed-license review.

This directory is the source bundle for the standalone repository. It has not yet been copied to a separate GitHub remote.


**Deployment update (2026-11-02):** The prepared packet has been deployed to the standalone public repository [PCakes303/aix-codecs](https://github.com/PCakes303/aix-codecs). The staging directory is retained as the master control plane's provisioning archive. The standalone repository contains 14 files and its GitHub Actions matrix passed on Python 3.10, 3.11 and 3.12. No release has been published.
