"""FD-009 T1/A2 non-human evidence-policy validation.

This module is a narrow compatibility layer over the frozen Spec 005 science
validator. It does not invent thresholds, margins, evidence, or statistical
design values. The legacy authority-reference field names remain structurally
compatible, but FD-009 requires them to bind explicit non-human policy
identities rather than people or reviewer dispositions.
"""

from __future__ import annotations

from typing import Any

from .science import (
    evaluate_scientific_selection_readiness,
    validate_threshold_policy,
)

FD009_POLICY_ID = "FD009_T1_A2_NON_HUMAN_EVIDENCE_POLICY_V1"
FD009_CLINICAL_POLICY_AUTHORITY = (
    "FD009_T1_A2_CLINICAL_MEANINGFULNESS_EVIDENCE_POLICY_V1"
)
FD009_STATISTICAL_POLICY_AUTHORITY = (
    "FD009_T1_A2_STATISTICAL_EVIDENCE_POLICY_V1"
)


def _is_nonempty_string_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, str) and bool(item.strip()) for item in value)
    )


def validate_fd009_threshold_policy(
    record: Any, quality_contract: Any, metrics_v2: Any
) -> list[str]:
    """Validate a T1/A2 threshold policy under the canonical FD-009 amendment.

    The underlying Spec 005 structural checks still apply. FD-009 additionally
    requires explicit non-human policy authority identities and non-empty
    clinical-meaningfulness/statistical evidence references. Arbitrary reviewer
    names, reviewer-like placeholders, and empty evidence lists cannot satisfy
    the gate.
    """

    errors = list(validate_threshold_policy(record, quality_contract, metrics_v2))
    if not isinstance(record, dict):
        return sorted(set(errors))

    if record.get("clinical_review_authority_reference") != (
        FD009_CLINICAL_POLICY_AUTHORITY
    ):
        errors.append(
            "FD009ThresholdPolicy:clinical_review_authority_reference_"
            "MUST_BIND_FD009_NON_HUMAN_POLICY"
        )

    if record.get("statistical_review_authority_reference") != (
        FD009_STATISTICAL_POLICY_AUTHORITY
    ):
        errors.append(
            "FD009ThresholdPolicy:statistical_review_authority_reference_"
            "MUST_BIND_FD009_NON_HUMAN_POLICY"
        )

    if not _is_nonempty_string_list(
        record.get("clinical_meaningfulness_evidence_ids")
    ):
        errors.append(
            "FD009ThresholdPolicy:clinical_meaningfulness_evidence_ids_"
            "MUST_BE_NONEMPTY_STRING_LIST"
        )

    if not _is_nonempty_string_list(
        record.get("statistical_justification_evidence_ids")
    ):
        errors.append(
            "FD009ThresholdPolicy:statistical_justification_evidence_ids_"
            "MUST_BE_NONEMPTY_STRING_LIST"
        )

    return sorted(set(errors))


def evaluate_fd009_scientific_selection_readiness(
    records: Any, quality_contract: Any, metrics_v2: Any
) -> dict[str, object]:
    """Compute Spec 005 readiness with the additional FD-009 policy gate."""

    base = evaluate_scientific_selection_readiness(
        records, quality_contract, metrics_v2
    )
    reason_codes = list(base.get("reason_codes", []))

    if isinstance(records, dict):
        thresholds = records.get("threshold_policies")
        if isinstance(thresholds, list):
            for index, threshold in enumerate(thresholds):
                for error in validate_fd009_threshold_policy(
                    threshold, quality_contract, metrics_v2
                ):
                    reason_codes.append(f"FD009ThresholdPolicy[{index}]:{error}")
        else:
            reason_codes.append("FD009ScientificReadiness:NO_THRESHOLD_POLICIES")
    else:
        reason_codes.append("FD009ScientificReadiness:MALFORMED_RECORDS_NOT_OBJECT")

    unique_sorted = sorted(set(reason_codes))
    state = "READY_FOR_PRECONSTRUCTION" if not unique_sorted else "INCOMPLETE"
    return {
        "policy_id": FD009_POLICY_ID,
        "state": state,
        "reason_codes": unique_sorted,
    }
