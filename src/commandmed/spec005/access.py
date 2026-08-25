"""Spec 005 A13 payload/result access firewall. Metadata-only, default deny.

No storage is provisioned and no real ACL is modified; this module validates
access metadata against the three-zone policy and the A7 handshake signals.
"""

from __future__ import annotations

from typing import Any

REQUIRED_ZONES = ("METADATA_ZONE", "SELECTION_CONTENT_ZONE", "CANDIDATE_RESULT_ZONE")
CONTENT_ROLE_CLASSES = frozenset(
    {
        "CONTENT_AUTHOR_ARABIC_PAIRS",
        "CLINICAL_REVIEWER_ARABIC_PAIRS",
        "ADJUDICATOR_ARABIC_PAIRS",
    }
)

GRANT_REQUIRED_FIELDS = (
    "access_grant_id",
    "personnel_reference",
    "assignment_id",
    "eligibility_record_id",
    "resource_zone",
    "scope_id",
    "purpose",
    "grant_state",
    "authorization_reference",
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


def validate_access_policy(record: Any) -> list[str]:
    """Validate the closed three-zone default-deny access policy."""
    errors: list[str] = []
    _require_fields(
        record,
        ("access_policy_id", "default_disposition", "record_canonical_sha256"),
        "AccessPolicy",
        errors,
    )
    if not isinstance(record, dict):
        return errors

    zones = record.get("resource_zones")
    if not isinstance(zones, list):
        zones = []
    for zone in REQUIRED_ZONES:
        if zone not in zones:
            errors.append(f"AccessPolicy:MISSING_RESOURCE_ZONE_{zone}")

    if record.get("default_disposition") != "DENY":
        errors.append("AccessPolicy:DEFAULT_DISPOSITION_MUST_BE_DENY")

    private_gold_zone = record.get("private_gold_zone")
    selection_zones = set(REQUIRED_ZONES)
    if private_gold_zone in selection_zones:
        errors.append("AccessPolicy:PRIVATE_GOLD_OUTSIDE_SELECTION_ZONES_REQUIRED")
    elif private_gold_zone != "PRIVATE_GOLD_QUARANTINE_ZONE":
        errors.append("AccessPolicy:PRIVATE_GOLD_QUARANTINE_ZONE_EXPECTED")
    return errors


def validate_access_grant_metadata(record: Any, a7_handshake: Any) -> list[str]:
    """Validate one A13 grant metadata record against the handshake signal."""
    errors: list[str] = []
    _require_fields(record, GRANT_REQUIRED_FIELDS, "AccessGrant", errors)
    if not isinstance(record, dict):
        return errors

    zone = record.get("resource_zone")
    if zone not in REQUIRED_ZONES:
        errors.append(f"AccessGrant:UNKNOWN_RESOURCE_ZONE_{zone}")
    if zone in ("SELECTION_CONTENT_ZONE", "CANDIDATE_RESULT_ZONE"):
        errors.append(f"AccessGrant:NO_DIRECT_GRANT_FOR_{zone}")

    # ALLOW_GRANT_CONSIDERATION authorizes consideration only, never access.
    if record.get("grant_state") == "ACTIVE":
        errors.append("AccessGrant:ALLOW_CONSIDERATION_IS_NOT_A_GRANT")

    if not isinstance(a7_handshake, dict) or not a7_handshake.get("signal"):
        errors.append("AccessGrant:A7_HANDSHAKE_SIGNAL_REQUIRED")
    return errors


def evaluate_access_disposition(
    record: Any, a7_handshake: Any
) -> dict[str, object]:
    """Default deny; compute the disposition from signal plus zone/role rules."""
    reason_codes: list[str] = []

    if not isinstance(a7_handshake, dict):
        return {"state": "DENIED", "reason_codes": ["ACCESS:MALFORMED_HANDSHAKE"]}
    if not isinstance(record, dict):
        return {"state": "DENIED", "reason_codes": ["ACCESS:MALFORMED_GRANT"]}

    # Structural grant validation gates every disposition; malformed grants
    # are denied outright rather than partially considered.
    shape_errors = validate_access_grant_metadata(record, a7_handshake)
    if any("UNKNOWN_RESOURCE_ZONE" in e or "_MISSING" in e for e in shape_errors):
        return {
            "state": "DENIED",
            "reason_codes": sorted(f"ACCESS:{e}" for e in shape_errors),
        }

    signal = a7_handshake.get("signal")

    if signal == "DENY_GRANT":
        reason_codes.append("ACCESS:A7_SIGNAL_DENY")
    elif signal == "REVOKE_REQUIRED":
        return {
            "state": "REVOCATION_REQUIRED",
            "reason_codes": ["ACCESS:A7_SIGNAL_REVOKE"],
        }
    elif signal == "REVALIDATION_REQUIRED":
        return {
            "state": "REVALIDATION_REQUIRED",
            "reason_codes": ["ACCESS:A7_SIGNAL_REVALIDATE"],
        }

    zone = record.get("resource_zone")
    holder_role = record.get("holder_role_class")
    if (
        zone == "CANDIDATE_RESULT_ZONE"
        and holder_role in CONTENT_ROLE_CLASSES
        and record.get("holder_result_exposure") == "RESULT_BLIND"
    ):
        reason_codes.append(
            "ACCESS:CANDIDATE_RESULTS_CANNOT_FLOW_TO_ACTIVE_CONTENT_ROLES"
        )

    if not reason_codes and signal == "ALLOW_GRANT_CONSIDERATION":
        result = {
            "state": "GRANT_CONSIDERATION_ALLOWED",
            "reason_codes": [],
            "resource_zone": zone,
        }
        # Deliberately no 'granted' key: consideration is not an access grant.
        return result

    if not reason_codes:
        reason_codes.append("ACCESS:DEFAULT_DENY_NO_QUALIFYING_SIGNAL")

    unique_sorted = sorted(set(reason_codes))
    state = "DENIED"
    return {"state": state, "reason_codes": unique_sorted}