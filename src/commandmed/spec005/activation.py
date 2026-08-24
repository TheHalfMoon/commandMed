"""Spec 005 A15 construction activation record validation.

Validates immutable activation records against a preconstruction snapshot.
A synthetic PASS here never creates canonical construction authority; real
activation requires separate founder authorization outside this code.
"""

from __future__ import annotations

from typing import Any

REQUIRED_GATES = (
    "R1",
    "T1",
    "D34",
    "G1",
    "G2",
    "G3",
    "G4",
    "S1",
    "P1",
    "C1",
    "H1",
    "I1",
    "F1",
)

ACTIVATION_REQUIRED_FIELDS = (
    "activation_id",
    "activation_version",
    "preconstruction_snapshot_id",
    "preconstruction_snapshot_sha256",
    "required_gate_identities",
    "authorized_construction_scope",
    "explicit_exclusions",
    "record_canonical_sha256",
)


def _require_fields(record: Any, fields, prefix: str, errors: list[str]) -> None:
    if not isinstance(record, dict):
        errors.append(f"{prefix}:MALFORMED_RECORD_NOT_OBJECT")
        return
    for field in fields:
        value = record.get(field)
        if value is None:
            errors.append(f"{prefix}:{field}_MISSING")


def validate_activation_record(record: Any, snapshot: Any) -> list[str]:
    """Validate structural integrity and exact snapshot/gate bindings."""
    errors: list[str] = []
    _require_fields(record, ACTIVATION_REQUIRED_FIELDS, "Activation", errors)
    if not isinstance(record, dict):
        return errors

    gate_identities = (
        record.get("required_gate_identities")
        if isinstance(record.get("required_gate_identities"), dict)
        else {}
    )
    snapshot_requirements = (
        snapshot.get("requirements", {}) if isinstance(snapshot, dict) else {}
    )
    for gate in REQUIRED_GATES:
        binding = gate_identities.get(gate)
        requirement = snapshot_requirements.get(gate)
        if not isinstance(requirement, dict):
            errors.append(f"Activation:SNAPSHOT_GATE_EVIDENCE_MISSING_{gate}")
            continue
        expected_record = requirement.get("record_id")
        expected_sha = requirement.get("record_canonical_sha256")
        if not isinstance(expected_record, str) or not expected_record.strip():
            errors.append(f"Activation:SNAPSHOT_GATE_{gate}_RECORD_ID_UNBOUND")
            continue
        if not isinstance(expected_sha, str) or not expected_sha.strip():
            errors.append(f"Activation:SNAPSHOT_GATE_{gate}_RECORD_SHA_UNBOUND")
            continue
        if not isinstance(binding, dict):
            errors.append(f"Activation:MISSING_GATE_IDENTITY_{gate}")
            continue
        bound_record = binding.get("record_id")
        bound_sha = binding.get("record_canonical_sha256")
        if bound_record != expected_record:
            errors.append(f"Activation:GATE_{gate}_IDENTITY_MISMATCH_WITH_SNAPSHOT")
        elif bound_sha != expected_sha:
            errors.append(f"Activation:GATE_{gate}_SHA_MISMATCH_WITH_SNAPSHOT")

    declared_snapshot_sha = record.get("preconstruction_snapshot_sha256")
    expected_snapshot_sha = (
        snapshot.get("snapshot_sha256") if isinstance(snapshot, dict) else None
    )
    if not isinstance(expected_snapshot_sha, str) or not expected_snapshot_sha.strip():
        errors.append("Activation:BOUND_SNAPSHOT_SHA256_REQUIRED")
    elif declared_snapshot_sha != expected_snapshot_sha:
        errors.append("Activation:PRECONSTRUCTION_SNAPSHOT_SHA_MISMATCH")

    if isinstance(snapshot, dict) and record.get(
        "preconstruction_snapshot_id"
    ) != snapshot.get("snapshot_id"):
        errors.append("Activation:SNAPSHOT_ID_MISMATCH_WITH_BOUND_SNAPSHOT")
    return errors


def evaluate_activation_readiness(
    record: Any, snapshot: Any
) -> dict[str, object]:
    """Compute readiness; caller-owned authorized claims are never trusted."""
    reason_codes: list[str] = []
    if not isinstance(record, dict) or not isinstance(snapshot, dict):
        return {
            "state": "BLOCKED",
            "reason_codes": ["ACTIVATION:MALFORMED_INPUT"],
        }

    errors = validate_activation_record(record, snapshot)
    reason_codes.extend(f"ACTIVATION:{e}" for e in errors)

    snapshot_state = snapshot.get("computed_readiness")
    if snapshot_state != "READY_FOR_SEPARATE_ACTIVATION_NOT_AUTHORIZED":
        reason_codes.append(
            f"ACTIVATION:SNAPSHOT_COMPUTED_STATE_INVALID_{snapshot_state}"
        )

    requirements = snapshot.get("requirements") or {}
    for gate in REQUIRED_GATES:
        evidence = requirements.get(gate)
        if not isinstance(evidence, dict):
            reason_codes.append(f"ACTIVATION:PREREQUISITE_GATE_{gate}_MISSING")
            continue
        gate_state = evidence.get("state")
        if gate_state != "PASS":
            reason_codes.append(f"ACTIVATION:PREREQUISITE_GATE_{gate}_STATE_{gate_state}")
        elif evidence.get("stale") is True:
            reason_codes.append(f"ACTIVATION:PREREQUISITE_GATE_{gate}_STALE")

    # The scientific A2/A3+A4 records are explicitly mandatory prerequisites.
    for scientific_gate in ("T1", "D34"):
        if scientific_gate not in requirements:
            reason_codes.append(
                f"ACTIVATION:SCIENTIFIC_RECORD_{scientific_gate}_REQUIRED"
            )

    unique_sorted = sorted(set(reason_codes))
    state = (
        "READY_FOR_SEPARATE_AUTHORIZATION" if not unique_sorted else "BLOCKED"
    )
    # No 'authorized' key is ever emitted by synthetic validation.
    result = {
        "state": state,
        "reason_codes": unique_sorted,
        "activation_id": record.get("activation_id"),
    }
    return result