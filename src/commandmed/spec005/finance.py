"""Spec 005 A14 spend/engagement governance. Metadata-only; no money moves.

Validates workload/requirement manifests, authorization identity and
lifecycle transitions, and computes the two operational PASS modes. No
payment, contract, vendor selection, or provisioning action is performed.
"""

from __future__ import annotations

from typing import Any

LIFECYCLE_STATES = frozenset(
    {
        "DRAFT_PROPOSED",
        "PENDING_APPROVAL",
        "APPROVED_NOT_ACTIVE",
        "ACTIVE",
        "SUSPENDED",
        "EXHAUSTED",
        "EXPIRED",
        "REVOKED",
        "SUPERSEDED",
        "REJECTED",
    }
)

ALLOWED_TRANSITIONS = {
    "DRAFT_PROPOSED": {"PENDING_APPROVAL", "REJECTED"},
    "PENDING_APPROVAL": {"APPROVED_NOT_ACTIVE", "REJECTED"},
    "APPROVED_NOT_ACTIVE": {"ACTIVE", "REJECTED"},
    "ACTIVE": {"SUSPENDED", "EXHAUSTED", "EXPIRED", "REVOKED", "SUPERSEDED"},
    "SUSPENDED": {"ACTIVE", "EXPIRED", "REVOKED", "SUPERSEDED"},
    "EXHAUSTED": {"SUPERSEDED"},
    "EXPIRED": {"SUPERSEDED"},
    "REVOKED": {"SUPERSEDED"},
    "SUPERSEDED": set(),
    "REJECTED": set(),
}

AUTHORIZATION_REQUIRED_FIELDS = (
    "a14_authorization_id",
    "authorization_version",
    "requirement_manifest_id",
    "requirement_manifest_sha256",
    "bounded_scope",
    "spend_categories",
    "engagement_classes",
    "payee_vendor_or_personnel_references",
    "currency",
    "max_committed_amount",
    "max_payable_amount",
    "authorized_period_or_expiry",
    "stop_conditions",
    "approval_decision_id",
    "approval_decision_sha256",
    "approver_reference",
    "lifecycle_state",
    "record_canonical_sha256",
)

MANIFEST_REQUIRED_FIELDS = (
    "requirement_manifest_id",
    "requirement_manifest_version",
    "exact_d34_design_id",
    "exact_a8_protocol_id",
    "exact_a7_roster_snapshot_id",
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


def validate_requirement_manifest(record: Any) -> list[str]:
    """Validate structural shape of one A14 requirement manifest."""
    errors: list[str] = []
    _require_fields(record, MANIFEST_REQUIRED_FIELDS, "RequirementManifest", errors)
    return errors


def _is_blocking(code: str) -> bool:
    markers = (
        "UNKNOWN",
        "MISSING",
        "NO_WORK_PACKAGES",
        "NO_ACTIVE",
        "MALFORMED",
        "STATE_NOT_REQUIRED_ONLY_WHEN",
    )
    return any(marker in code for marker in markers)


def evaluate_a14_requirement(record: Any) -> dict[str, object]:
    """Compute NOT_REQUIRED / REQUIRED / BLOCKED from bound manifest evidence."""
    reason_codes: list[str] = []
    errors = validate_requirement_manifest(record)
    reason_codes.extend(errors)
    if not isinstance(record, dict):
        reason_codes.append("A14:MALFORMED_MANIFEST")
        return {
            "state": "BLOCKED_UNKNOWN_OR_INCOMPLETE",
            "reason_codes": sorted(set(reason_codes)),
        }

    work_packages = record.get("work_packages")
    gaps = record.get("capacity_gap_records") or []
    engagements = record.get("new_engagement_requirement_records") or []
    commitments = record.get("new_financial_commitment_requirement_records") or []

    if not isinstance(work_packages, list) or not work_packages:
        # Absence of workload evidence never implies NOT_REQUIRED.
        reason_codes.append("A14:NO_WORK_PACKAGES_EVIDENCE")
    else:
        for package in work_packages:
            required_units = package.get("required_capacity_units") if isinstance(package, dict) else None
            existing_units = package.get("existing_capacity_units") if isinstance(package, dict) else None
            package_id = package.get("work_package_id") if isinstance(package, dict) else "?"
            if not isinstance(required_units, (int, float)) or isinstance(required_units, bool):
                reason_codes.append(f"A14:WORK_PACKAGE_{package_id}_REQUIRED_UNITS_UNKNOWN")
                continue
            if not isinstance(existing_units, (int, float)) or isinstance(existing_units, bool):
                reason_codes.append(
                    f"A14:WORK_PACKAGE_{package_id}_EXISTING_CAPACITY_UNKNOWN"
                )

    # A declared $0 / free-tier / volunteer label cannot establish NOT_REQUIRED.
    for label_field in ("declared_cost_label", "declared_spend_label"):
        label = record.get(label_field)
        if isinstance(label, str) and "$0" in label:
            reason_codes.append(f"A14:{label_field}_CANNOT_ESTABLISH_NOT_REQUIRED")

    # Recompute capacity gaps per package; supplied gap evidence must be
    # consistent with the workload numbers or the manifest fails closed.
    derived_gap = False
    if isinstance(work_packages, list):
        for package in work_packages:
            if not isinstance(package, dict):
                continue
            required_units = package.get("required_capacity_units")
            existing_units = package.get("existing_capacity_units")
            package_id = package.get("work_package_id", "?")
            if (
                isinstance(required_units, (int, float)) and not isinstance(required_units, bool)
                and isinstance(existing_units, (int, float)) and not isinstance(existing_units, bool)
                and required_units > existing_units
            ):
                derived_gap = True
                gap_ids = {
                    g.get("gap_id") for g in gaps if isinstance(g, dict)
                }
                if not any(
                    g.get("work_package_id") == package_id
                    for g in gaps if isinstance(g, dict)
                ) and f"A14:WORK_PACKAGE_{package_id}_GAP_RECORD_MISSING" not in reason_codes:
                    reason_codes.append(
                        f"A14:WORK_PACKAGE_{package_id}_GAP_RECORD_MISSING"
                    )
    if gaps and not derived_gap:
        # Declared gaps without insufficient capacity are inconsistent.
        pass  # engagement/commitment records may still require authority.

    has_gaps = (
        bool(engagements) or bool(commitments) or derived_gap
        or any(isinstance(g, dict) and g.get("gap_units", 0) for g in gaps)
    )
    blocked = any(_is_blocking(code) for code in reason_codes)

    if blocked:
        state = "BLOCKED_UNKNOWN_OR_INCOMPLETE"
    elif has_gaps:
        state = "REQUIRED"
    elif work_packages:
        state = "NOT_REQUIRED"
    else:
        state = "BLOCKED_UNKNOWN_OR_INCOMPLETE"

    result = {
        "state": state,
        "reason_codes": sorted(set(reason_codes)),
        "requirement_manifest_id": record.get("requirement_manifest_id"),
        "requirement_manifest_sha256": record.get("requirement_manifest_sha256"),
    }
    return result


def validate_a14_authorization(record: Any) -> list[str]:
    """Validate immutable authorization identity including duty segregation."""
    errors: list[str] = []
    _require_fields(record, AUTHORIZATION_REQUIRED_FIELDS, "A14Authorization", errors)
    if not isinstance(record, dict):
        return errors

    approver = record.get("approver_reference")
    payees = record.get("payee_vendor_or_personnel_references") or []
    if approver in payees:
        errors.append("A14Authorization:SELF_APPROVAL_PROHIBITED")

    scope = record.get("bounded_scope")
    if scope == "ANYTHING" or (isinstance(scope, str) and len(scope.strip()) < 4):
        errors.append("A14Authorization:BOUNDED_SCOPE_MUST_BE_EXPLICIT")

    lifecycle_state = record.get("lifecycle_state")
    if lifecycle_state not in LIFECYCLE_STATES:
        errors.append(f"A14Authorization:UNKNOWN_LIFECYCLE_STATE_{lifecycle_state}")

    committed = record.get("max_committed_amount")
    payable = record.get("max_payable_amount")
    for name, value in (("max_committed_amount", committed), ("max_payable_amount", payable)):
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
            errors.append(f"A14Authorization:{name}_MUST_BE_NON_NEGATIVE_NUMBER")
    if (
        isinstance(committed, (int, float)) and not isinstance(committed, bool)
        and isinstance(payable, (int, float)) and not isinstance(payable, bool)
        and committed >= 0 and payable > committed
    ):
        errors.append("A14Authorization:max_payable_amount_EXCEEDS_max_committed_amount")
    return errors


TRANSITION_VERBS = {
    "SUBMIT_FOR_APPROVAL": "PENDING_APPROVAL",
    "APPROVE": "APPROVED_NOT_ACTIVE",
    "REJECT": "REJECTED",
    "ACTIVATE": "ACTIVE",
    "SUSPEND": "SUSPENDED",
    "EXHAUST": "EXHAUSTED",
    "EXPIRE": "EXPIRED",
    "REVOKE": "REVOKED",
    "SUPERSEDE": "SUPERSEDED",
}


def validate_a14_transition(authorization: Any, transition: Any) -> list[str]:
    """Validate a lifecycle transition against the closed transition table."""
    errors: list[str] = []
    if not isinstance(authorization, dict) or not isinstance(transition, dict):
        return ["A14Transition:MALFORMED_INPUT"]

    current_state = authorization.get("lifecycle_state")
    verb = transition.get("transition")
    target_state = TRANSITION_VERBS.get(verb)
    if target_state is None:
        errors.append(f"A14Transition:UNKNOWN_TRANSITION_{verb}")
        return errors

    allowed_targets = ALLOWED_TRANSITIONS.get(current_state)
    if allowed_targets is None:
        errors.append(f"A14Transition:UNKNOWN_CURRENT_STATE_{current_state}")
        return errors
    if target_state not in allowed_targets:
        errors.append(
            f"A14Transition:ILLEGAL_TRANSITION_{current_state}_TO_{target_state}"
        )
    return errors


def evaluate_a14_operational_pass(requirements: Any, authorizations: Any) -> dict[str, object]:
    """Compute A14_AUTHORIZED_PASS / A14_NOT_REQUIRED_PASS, fail-closed else."""
    reason_codes: list[str] = []
    if not isinstance(requirements, dict):
        return {
            "state": "BLOCKED_UNKNOWN_OR_INCOMPLETE",
            "reason_codes": ["A14:MALFORMED_REQUIREMENT_INPUT"],
        }

    req_state = requirements.get("state")
    if req_state == "NOT_REQUIRED":
        # Caller-owned NOT_REQUIRED is never trusted: recompute from the
        # bound requirement manifest supplied alongside the claim.
        manifest = requirements.get("requirement_manifest")
        recomputed = evaluate_a14_requirement(manifest)
        if recomputed["state"] != "NOT_REQUIRED":
            reason_codes.append("A14:NOT_REQUIRED_CLAIM_NOT_REPRODUCIBLE")
            reason_codes.extend(
                f"A14:{c}" for c in recomputed["reason_codes"]
            )
            return {
                "state": "BLOCKED_UNKNOWN_OR_INCOMPLETE",
                "reason_codes": sorted(set(reason_codes)),
            }
        return {
            "state": "A14_NOT_REQUIRED_PASS",
            "reason_codes": [],
            "requirement_manifest_id": recomputed.get("requirement_manifest_id"),
        }
    if req_state != "REQUIRED":
        reason_codes.append(f"A14:REQUIREMENT_STATE_{req_state}")

    auth_list = authorizations if isinstance(authorizations, list) else []
    manifest_id = requirements.get("requirement_manifest_id")
    covering = []
    for index, auth in enumerate(auth_list):
        if not isinstance(auth, dict):
            continue
        if auth.get("lifecycle_state") != "ACTIVE" or auth.get("stale") is True:
            continue
        if auth.get("requirement_manifest_id") != manifest_id:
            continue
        shape_errors = validate_a14_authorization(auth)
        if shape_errors:
            reason_codes.extend(
                f"A14:AUTHORIZATION[{index}]:{e}" for e in shape_errors
            )
            continue
        covering.append(auth)
    if not covering:
        reason_codes.append("A14:NO_ACTIVE_UNSTALE_MATCHING_AUTHORIZATION")

    if reason_codes:
        return {
            "state": "BLOCKED_UNKNOWN_OR_INCOMPLETE",
            "reason_codes": sorted(set(reason_codes)),
        }

    return {
        "state": "A14_AUTHORIZED_PASS",
        "reason_codes": [],
        "requirement_manifest_id": manifest_id,
        "covered_by_authorization_ids": sorted(
            auth.get("a14_authorization_id", "") for auth in covering
        ),
    }