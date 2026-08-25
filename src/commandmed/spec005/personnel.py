"""Spec 005 personnel governance (A7): opaque identity, eligibility, A7 signals.

Pure record validation and state evaluation. No credentials are stored, no
real person is assigned, no resource access is ever granted by this module.
"""

from __future__ import annotations

from typing import Any

IDENTITY_STATES = frozenset(
    {"REGISTERED_UNVERIFIED", "VERIFIED", "SUSPENDED", "RETIRED"}
)
ELIGIBILITY_STATES = frozenset(
    {
        "NOT_COMPUTED",
        "ELIGIBLE",
        "ELIGIBLE_WITH_SCOPE_LIMIT",
        "BLOCKED_PENDING_EVIDENCE",
        "INELIGIBLE",
        "STALE_RECOMPUTE_REQUIRED",
    }
)
ASSIGNMENT_STATES = frozenset(
    {"PROPOSED", "ACTIVE", "SUSPENDED", "REVOKED", "EXPIRED"}
)
CONTENT_ROLE_CLASSES = frozenset(
    {
        "CONTENT_AUTHOR_ARABIC_PAIRS",
        "CLINICAL_REVIEWER_ARABIC_PAIRS",
        "ADJUDICATOR_ARABIC_PAIRS",
    }
)
INCOMPATIBLE_ROLE_CLASSES = (
    {"CONTENT_AUTHOR_ARABIC_PAIRS", "CLINICAL_REVIEWER_ARABIC_PAIRS"},
    {"CONTENT_AUTHOR_ARABIC_PAIRS", "ADJUDICATOR_ARABIC_PAIRS"},
    {"CLINICAL_REVIEWER_ARABIC_PAIRS", "ADJUDICATOR_ARABIC_PAIRS"},
)

ELIGIBILITY_REQUIRED_FIELDS = (
    "eligibility_record_id",
    "personnel_reference",
    "role_class",
    "suite_or_scope_id",
    "identity_record_id",
    "record_canonical_sha256",
)
ASSIGNMENT_REQUIRED_FIELDS = (
    "assignment_id",
    "personnel_reference",
    "role_class",
    "suite_or_scope_id",
    "eligibility_record_id",
    "assignment_state",
    "record_canonical_sha256",
)


def _require_fields(record: Any, fields, prefix: str, errors: list[str]) -> None:
    if not isinstance(record, dict):
        errors.append(f"{prefix}:MALFORMED_RECORD_NOT_OBJECT")
        return
    for field in fields:
        value = record.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            errors.append(f"{prefix}:{field}_MISSING")


def validate_personnel_record(record: Any) -> list[str]:
    """Validate the opaque personnel identity record; no PII is permitted."""
    errors: list[str] = []
    _require_fields(
        record,
        ("personnel_reference", "identity_state", "record_version"),
        "PersonnelIdentity",
        errors,
    )
    if not isinstance(record, dict):
        return errors

    reference = record.get("personnel_reference")
    if isinstance(reference, str) and ("@" in reference or " " in reference):
        errors.append("PersonnelIdentity:REFERENCE_MUST_BE_OPAQUE_NO_PII")

    state = record.get("identity_state")
    if state not in IDENTITY_STATES:
        errors.append(f"PersonnelIdentity:UNKNOWN_IDENTITY_STATE_{state}")
    return errors


def validate_eligibility_record(record: Any, evidence: Any) -> list[str]:
    """Validate structural shape of one role/scope-specific eligibility record."""
    errors: list[str] = []
    _require_fields(record, ELIGIBILITY_REQUIRED_FIELDS, "EligibilityRecord", errors)
    if isinstance(record, dict):
        state = record.get("eligibility_state")
        if state not in ELIGIBILITY_STATES:
            errors.append(f"EligibilityRecord:UNKNOWN_ELIGIBILITY_STATE_{state}")
    return errors


def evaluate_role_eligibility(record: Any, evidence: Any) -> dict[str, object]:
    """Compute role/scope eligibility from bound evidence, never from claims."""
    reason_codes: list[str] = []
    if not isinstance(record, dict) or not isinstance(evidence, dict):
        return {
            "state": "BLOCKED_PENDING_EVIDENCE",
            "reason_codes": ["PERSONNEL:MALFORMED_INPUT"],
        }

    reference = record.get("personnel_reference")
    role_class = record.get("role_class")

    qualification = evidence.get("qualification_evidence_ids") or []
    if not qualification:
        reason_codes.append("PERSONNEL:QUALIFICATION_EVIDENCE_MISSING")

    conflict = evidence.get("conflict_disposition_record_id")
    if not conflict:
        reason_codes.append("PERSONNEL:CONFLICT_DISPOSITION_MISSING")

    gold_exposure = evidence.get("gold_exposure_state") or evidence.get(
        "result_exposure_state"
    )
    is_content_role = role_class in CONTENT_ROLE_CLASSES
    if is_content_role and gold_exposure in {
        "EXPOSED_TO_PRIVATE_GOLD",
        "SAME_SUITE_RESULTS_EXPOSED",
    }:
        if gold_exposure == "EXPOSED_TO_PRIVATE_GOLD":
            reason_codes.append(
                "PERSONNEL:PRIVATE_GOLD_EXPOSURE_BLOCKS_CONTENT_ROLES"
            )
        else:
            reason_codes.append(
                "PERSONNEL:SAME_SUITE_RESULT_EXPOSURE_INCOMPATIBLE"
            )

    if evidence.get("evidence_stale") is True:
        reason_codes.append("PERSONNEL:EVIDENCE_STALE")

    if any(code.endswith(("_MISSING", "_STALE")) for code in reason_codes):
        state = "BLOCKED_PENDING_EVIDENCE"
    elif reason_codes:
        state = "INELIGIBLE"
    else:
        state = "ELIGIBLE"

    result = {
        "state": state,
        "reason_codes": sorted(set(reason_codes)),
        "personnel_reference": reference,
        "role_class": role_class,
        "suite_or_scope_id": record.get("suite_or_scope_id"),
        "result_exposure_state": evidence.get("result_exposure_state"),
        "stale": evidence.get("evidence_stale") is True,
    }
    return result


def validate_role_assignment(record: Any, eligibility: Any) -> list[str]:
    """Validate an assignment against its computed eligibility."""
    errors: list[str] = []
    _require_fields(record, ASSIGNMENT_REQUIRED_FIELDS, "RoleAssignment", errors)
    if not isinstance(record, dict):
        return errors

    state = record.get("assignment_state")
    if state not in ASSIGNMENT_STATES:
        errors.append(f"RoleAssignment:UNKNOWN_ASSIGNMENT_STATE_{state}")

    if isinstance(eligibility, dict):
        eligible_states = {"ELIGIBLE", "ELIGIBLE_WITH_SCOPE_LIMIT"}
        if state == "ACTIVE" and eligibility.get("state") not in eligible_states:
            errors.append(
                f"RoleAssignment:ACTIVE_REQUIRES_ELIGIBLE_STATE_"
                f"{eligibility.get('state')}"
            )
        for field in ("personnel_reference", "role_class", "suite_or_scope_id"):
            if record.get(field) != eligibility.get(field):
                errors.append(f"RoleAssignment:{field}_MISMATCH_WITH_ELIGIBILITY")

    # ACTIVE assignment must never itself carry resource-access authority.
    if record.get("grants_resource_access"):
        errors.append(
            "RoleAssignment:ASSIGNMENT_CANNOT_GRANT_RESOURCE_ACCESS"
        )
    return errors


def validate_independence(assignments: Any) -> list[str]:
    """Fail closed on same-person independence collisions across roles."""
    errors: list[str] = []
    if not isinstance(assignments, list):
        return ["Independence:MALFORMED_INPUT"]
    seen: dict[tuple[str, str], set[tuple[str, str]]] = {}
    for assignment in assignments:
        if not isinstance(assignment, dict):
            continue
        reference = assignment.get("personnel_reference")
        role_class = assignment.get("role_class")
        suite = assignment.get("suite_or_scope_id")
        for incompatible_pair in INCOMPATIBLE_ROLE_CLASSES:
            for other_role in incompatible_pair:
                if role_class == other_role:
                    continue
                key = (reference, suite)
                held = seen.setdefault(key, set())
                if other_role in held:
                    errors.append(
                        f"Independence:SAME_PERSON_ROLE_COLLISION_{reference}_"
                        f"{role_class}_{other_role}"
                    )
        seen.setdefault((reference, suite), set()).add(role_class)
    return sorted(set(errors))


def evaluate_a7_handshake(
    assignment: Any, eligibility: Any
) -> dict[str, object]:
    """Emit the A7 signal toward A13; ALLOW_GRANT_CONSIDERATION grants nothing."""
    reason_codes: list[str] = []
    if not isinstance(assignment, dict) or not isinstance(eligibility, dict):
        return {
            "signal": "DENY_GRANT",
            "reason_codes": ["HANDSHAKE:MALFORMED_INPUT"],
        }

    stale = eligibility.get("stale") is True or eligibility.get("state") in {
        "STALE_RECOMPUTE_REQUIRED"
    }
    eligible_state = eligibility.get("state")
    active = assignment.get("assignment_state") == "ACTIVE"

    if stale:
        signal = "REVALIDATION_REQUIRED"
    elif active and eligible_state in {"ELIGIBLE", "ELIGIBLE_WITH_SCOPE_LIMIT"}:
        signal = "ALLOW_GRANT_CONSIDERATION"
    else:
        signal = "DENY_GRANT"
        if not active:
            reason_codes.append("HANDSHAKE:ASSIGNMENT_NOT_ACTIVE")
        reason_codes.append(f"HANDSHAKE:ELIGIBILITY_STATE_{eligible_state}")

    return {
        "signal": signal,
        "reason_codes": sorted(set(reason_codes)),
        "assignment_id": assignment.get("assignment_id"),
        "resource_zone": None,
    }