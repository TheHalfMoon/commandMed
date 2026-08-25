"""Spec 006 patient safety scaffold and deterministic tools.

Deterministic, offline, identity-bound validators for the behavioral-state
safety scaffold. This package is metadata-only: it never executes models,
network calls, external clinical databases, devices, or any real tool
service. Importing this package has no side effects.

Modules:
    registry  DeterministicTool record and closed allow-list bundle validation.
    policy    SafetyRule records, precedence evaluation, fail-closed semantics.
    trace     InteractionTrace hash chains, seals, manifests, trusted-tree set
              verification.
    scaffold  Interaction evaluation composing registry + policy + trace into
              exactly one terminal behavioral state.
"""

from __future__ import annotations

__all__ = [
    "registry",
    "policy",
    "trace",
    "scaffold",
]
