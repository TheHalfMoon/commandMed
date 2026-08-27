"""Offline CurriculumRecord and duplicate-report contracts for Spec 007."""

from __future__ import annotations

from typing import Any

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.foundation import (
    ROLE_CLASSES,
    validate_canonical_sha256,
    validate_closed_object,
    validate_role_class,
)

KNOWLEDGE_PLACEMENTS = frozenset(
    {
        "DURABLE_WEIGHT_ELIGIBLE",
        "MUTABLE_RUNTIME_EVIDENCE_PREFERRED",
        "DETERMINISTIC_TOOL_REQUIRED",
        "REJECTED",
    }
)
TRANSLATION_STATES = frozenset(
    {
        "ORIGINAL",
        "HUMAN_TRANSLATED",
        "CLINICALLY_TRANSREATED",
        "MACHINE_TRANSLATED_UNVERIFIED",
        "NOT_APPLICABLE",
    }
)

_CURRICULUM_REQUIRED_FIELDS = (
    "schema_version",
    "record_id",
    "record_canonical_sha256",
    "content_sha256",
    "source_authority_id",
    "source_license_id",
    "source_verification_status",
    "split_id",
    "contamination_status",
    "review_state",
    "role_class",
    "curriculum_strata",
    "language_profile",
    "conversation_structure_id",
    "knowledge_placement",
    "quarantine_disposition",
)
_RENDERING_FIELDS = (
    "rendering_policy_id",
    "rendered_input_sha256",
    "rendered_token_count",
    "supervised_token_count",
    "loss_mask_policy_id",
)
_LANGUAGE_PROFILE_FIELDS = (
    "primary_language",
    "authored_language",
    "translation_state",
    "dialect_or_register",
    "code_switch_state",
    "transliteration_state",
    "terminology_normalization_id",
    "qualified_review_state",
)
_DUPLICATE_REPORT_FIELDS = (
    "report_id",
    "input_snapshot_candidate_id",
    "exact_duplicate_groups",
    "near_duplicate_groups",
    "benchmark_overlap_findings",
    "quarantine_overlap_findings",
    "source_concentration_findings",
    "post_render_overlap_findings",
    "disposition",
)


def _is_nonempty_string(value: Any, *, min_length: int = 1) -> bool:
    return isinstance(value, str) and len(value) >= min_length and bool(value.strip())


def _validate_nonempty_string(record: dict[str, Any], field: str) -> list[str]:
    if _is_nonempty_string(record.get(field)):
        return []
    return [f"CurriculumRecord: '{field}' must be a non-empty string"]


def compute_curriculum_record_sha256(record: dict[str, Any]) -> str:
    """Compute the self-excluding canonical identity of one curriculum record."""
    projection = dict(record)
    projection.pop("record_canonical_sha256", None)
    return compute_canonical_sha256(projection)


def validate_knowledge_placement(
    value: Any, field: str = "knowledge_placement"
) -> list[str]:
    if not isinstance(value, str):
        return [f"{field}: expected knowledge-placement string"]
    if value not in KNOWLEDGE_PLACEMENTS:
        return [f"{field}: unsupported value '{value}'"]
    return []


def _validate_language_profile(profile: Any) -> list[str]:
    prefix = "CurriculumRecord.language_profile"
    errors = validate_closed_object(
        profile,
        required_fields=_LANGUAGE_PROFILE_FIELDS,
        field=prefix,
    )
    if errors or not isinstance(profile, dict):
        return errors

    for field in (
        "primary_language",
        "authored_language",
    ):
        if not _is_nonempty_string(profile.get(field), min_length=2):
            errors.append(f"{prefix}: '{field}' must be a string of length >= 2")

    for field in (
        "dialect_or_register",
        "code_switch_state",
        "transliteration_state",
        "qualified_review_state",
    ):
        if not _is_nonempty_string(profile.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    translation = profile.get("translation_state")
    if not isinstance(translation, str) or translation not in TRANSLATION_STATES:
        errors.append(f"{prefix}: invalid translation_state")

    normalization = profile.get("terminology_normalization_id")
    if normalization is not None and not isinstance(normalization, str):
        errors.append(
            f"{prefix}: 'terminology_normalization_id' must be a string or null"
        )
    return errors


def validate_curriculum_record(record: Any) -> list[str]:
    """Validate one synthetic/offline CurriculumRecord fail closed."""
    prefix = "CurriculumRecord"
    errors = validate_closed_object(
        record,
        required_fields=_CURRICULUM_REQUIRED_FIELDS,
        optional_fields=_RENDERING_FIELDS,
        field=prefix,
    )
    if errors or not isinstance(record, dict):
        return errors

    if record.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version must equal '1'")

    for field in (
        "record_id",
        "source_authority_id",
        "source_license_id",
        "split_id",
        "conversation_structure_id",
        "quarantine_disposition",
    ):
        errors.extend(_validate_nonempty_string(record, field))

    errors.extend(
        validate_canonical_sha256(record.get("record_canonical_sha256"), "record_canonical_sha256")
    )
    errors.extend(validate_canonical_sha256(record.get("content_sha256"), "content_sha256"))
    errors.extend(validate_role_class(record.get("role_class")))
    errors.extend(validate_knowledge_placement(record.get("knowledge_placement")))

    strata = record.get("curriculum_strata")
    if (
        not isinstance(strata, list)
        or not strata
        or any(not _is_nonempty_string(item) for item in strata)
    ):
        errors.append(f"{prefix}: curriculum_strata must be a non-empty string list")
    elif len(strata) != len(set(strata)):
        errors.append(f"{prefix}: curriculum_strata must not contain duplicates")

    errors.extend(_validate_language_profile(record.get("language_profile")))

    if record.get("source_verification_status") != "VERIFIED":
        errors.append(f"{prefix}: source_verification_status must equal 'VERIFIED'")
    if record.get("contamination_status") != "ASSESSED_CLEAN":
        errors.append(f"{prefix}: contamination_status must equal 'ASSESSED_CLEAN'")
    if record.get("review_state") != "PASS":
        errors.append(f"{prefix}: review_state must equal 'PASS'")
    if record.get("quarantine_disposition") != "PASS":
        errors.append(f"{prefix}: quarantine_disposition must equal 'PASS'")

    present_rendering = [field for field in _RENDERING_FIELDS if field in record]
    if present_rendering and len(present_rendering) != len(_RENDERING_FIELDS):
        errors.append(f"{prefix}: rendering fields must be all present or all absent")
    elif len(present_rendering) == len(_RENDERING_FIELDS):
        for field in ("rendering_policy_id", "loss_mask_policy_id"):
            if not _is_nonempty_string(record.get(field)):
                errors.append(f"{prefix}: '{field}' must be a non-empty string")
        errors.extend(
            validate_canonical_sha256(record.get("rendered_input_sha256"), "rendered_input_sha256")
        )
        rendered = record.get("rendered_token_count")
        supervised = record.get("supervised_token_count")
        for field, value in (
            ("rendered_token_count", rendered),
            ("supervised_token_count", supervised),
        ):
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                errors.append(f"{prefix}: '{field}' must be a non-negative integer")
        if (
            isinstance(rendered, int)
            and not isinstance(rendered, bool)
            and isinstance(supervised, int)
            and not isinstance(supervised, bool)
            and supervised > rendered
        ):
            errors.append(
                f"{prefix}: supervised_token_count must be <= rendered_token_count"
            )

    claimed_identity = record.get("record_canonical_sha256")
    if not errors and claimed_identity != compute_curriculum_record_sha256(record):
        errors.append(f"{prefix}: record_canonical_sha256 mismatch")
    elif (
        isinstance(claimed_identity, str)
        and len(claimed_identity) == 64
        and all(ch in "0123456789abcdef" for ch in claimed_identity)
        and claimed_identity != compute_curriculum_record_sha256(record)
    ):
        errors.append(f"{prefix}: record_canonical_sha256 mismatch")
    return errors


def _validate_list_field(report: dict[str, Any], field: str, errors: list[str]) -> None:
    if not isinstance(report.get(field), list):
        errors.append(f"DuplicateContaminationReport: '{field}' must be a list")


def validate_duplicate_contamination_report(report: Any) -> list[str]:
    """Validate the raw duplicate/contamination report shape and PASS invariant."""
    prefix = "DuplicateContaminationReport"
    errors = validate_closed_object(
        report,
        required_fields=_DUPLICATE_REPORT_FIELDS,
        field=prefix,
    )
    if errors or not isinstance(report, dict):
        return errors

    for field in ("report_id", "input_snapshot_candidate_id"):
        if not _is_nonempty_string(report.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    for field in (
        "exact_duplicate_groups",
        "near_duplicate_groups",
        "benchmark_overlap_findings",
        "quarantine_overlap_findings",
        "source_concentration_findings",
    ):
        _validate_list_field(report, field, errors)
    post_render = report.get("post_render_overlap_findings")
    if post_render is not None and not isinstance(post_render, list):
        errors.append(f"{prefix}: 'post_render_overlap_findings' must be a list or null")

    disposition = report.get("disposition")
    if disposition not in {"PASS", "FAIL", "BLOCKED"}:
        errors.append(f"{prefix}: unsupported disposition '{disposition}'")

    prohibited_overlap_fields = (
        "exact_duplicate_groups",
        "near_duplicate_groups",
        "benchmark_overlap_findings",
        "quarantine_overlap_findings",
    )
    has_prohibited_overlap = any(
        isinstance(report.get(field), list) and bool(report[field])
        for field in prohibited_overlap_fields
    ) or (isinstance(post_render, list) and bool(post_render))
    if disposition == "PASS" and has_prohibited_overlap:
        errors.append(f"{prefix}: disposition PASS prohibited when overlap remains")
    return errors
