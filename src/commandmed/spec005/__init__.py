"""Spec 005 preconstruction control plane.

Deterministic, offline, identity-bound validators and state machines for the
base-model tournament preconstruction phase. This package is metadata-only:
it never executes models, benchmarks, devices, providers, payments, or any
real construction activation. Importing this package has no side effects.

Modules:
    science        A2/A3+A4 scientific selection quality, thresholds, design.
    preconstruction A5/A6/A8/A9/A10/A11/A12 source governance snapshots.
    personnel      A7 opaque-identity role governance.
    access         A13 three-zone payload/result access firewall.
    finance        A14 spend/engagement requirement and authorization gates.
    device         Frozen device qualification protocol validation.
    activation     A15 construction activation record validation.
    manifest       Spec 005 tournament manifest and Spec 004 projection.
"""

from __future__ import annotations

__all__ = [
    "science",
    "preconstruction",
    "personnel",
    "access",
    "finance",
    "device",
    "activation",
    "manifest",
]
