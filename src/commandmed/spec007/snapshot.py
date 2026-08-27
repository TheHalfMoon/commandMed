"""Synthetic DatasetSnapshot and curriculum-coverage generation for Spec 007."""

from __future__ import annotations

from collections import Counter
from typing import Any, Iterable

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.curriculum import validate_curriculum_record
from src.commandmed.spec007.foundation import (
    validate_canonical_sha256,
    validate_closed_object,
)
from src.commandmed.spec007.quarantine import evaluate_quarantine_source

_SNAPSHOT_REQUIRED_FIELDS = (
    "snapshot_id",
    "snapshot_sha256",
    "record_ids",
    "canonical_order_identity",
    "record_count",
    "source_summary",
    "license_summary",
    "role_coverage",
    "curriculum_coverage",
    "language_coverage",
    "duplicate_report_id",
    "contamination_report_id",
    "quarantine_verification_id",
    "knowledge_placement_summary",
)
_SNAPSHOT_OPTIONAL_FIELDS = (
    "rendered_token_count",
    "supervised_token_count",
)


def _is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def compute_dataset_snapshot_sha256(snapshot: dict[str, Any]) -> str:
    projection = dict(snapshot)
    projection.pop("snapshot_sha256", None)
    return compute_canonical_sha256(projection)


def validate_dataset_snapshot(snapshot: Any) -> list[str]:
    """Validate DatasetSnapshot shape and frozen cross-field invariants."""
    prefix = "DatasetSnapshot"
    errors = validate_closed_object(
        snapshot,
        required_fields=_SNAPSHOT_REQUIRED_FIELDS,
        optional_fields=_SNAPSHOT_OPTIONAL_FIELDS,
        field=prefix,
    )
    if errors or not isinstance(snapshot, dict):
        return errors

    for field in (
        "snapshot_id",
        "canonical_order_identity",
        "duplicate_report_id",
        "contamination_report_id",
        "quarantine_verification_id",
    ):
        if not _is_nonempty_string(snapshot.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    errors.extend(
        validate_canonical_sha256(snapshot.get("snapshot_sha256"), "snapshot_sha256")
    )

    record_ids = snapshot.get("record_ids")
    if not isinstance(record_ids, list) or any(
        not _is_nonempty_string(item) for item in record_ids
    ):
        errors.append(f"{prefix}: record_ids must be a string list")
    elif len(record_ids) != len(set(record_ids)):
        errors.append(f"{prefix}: record_ids must be unique")

    record_count = snapshot.get("record_count")
    if isinstance(record_count, bool) or not isinstance(record_count, int) or record_count < 0:
        errors.append(f"{prefix}: record_count must be a non-negative integer")
    elif isinstance(record_ids, list) and record_count != len(record_ids):
        errors.append(f"{prefix}: record_count must equal len(record_ids)")

    for field in (
        "source_summary",
        "license_summary",
        "role_coverage",
        "curriculum_coverage",
        "language_coverage",
        "knowledge_placement_summary",
    ):
        if not isinstance(snapshot.get(field), dict):
            errors.append(f"{prefix}: '{field}' must be an object")

    rendered = snapshot.get("rendered_token_count")
    supervised = snapshot.get("supervised_token_count")
    for field, value in (
        ("rendered_token_count", rendered),
        ("supervised_token_count", supervised),
    ):
        if value is not None and (
            isinstance(value, bool) or not isinstance(value, int) or value < 0
        ):
            errors.append(f"{prefix}: '{field}' must be a non-negative integer or null")
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

    claimed = snapshot.get("snapshot_sha256")
    if (
        isinstance(claimed, str)
        and len(claimed) == 64
        and all(ch in "0123456789abcdef" for ch in claimed)
        and claimed != compute_dataset_snapshot_sha256(snapshot)
    ):
        errors.append(f"{prefix}: snapshot_sha256 mismatch")
    return errors


def _validated_records(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    materialized = list(records)
    seen_ids: set[str] = set()
    for index, record in enumerate(materialized):
        errors = validate_curriculum_record(record)
        if errors:
            raise ValueError(f"record[{index}] invalid: {'; '.join(errors)}")
        record_id = record["record_id"]
        if record_id in seen_ids:
            raise ValueError(f"duplicate record_id '{record_id}'")
        seen_ids.add(record_id)

        authority_quarantine = evaluate_quarantine_source(
            record["source_authority_id"], "TRAIN"
        )
        if not authority_quarantine["allowed"] or not authority_quarantine["can_train"]:
            raise ValueError(
                f"record[{index}] source_authority_id not authorized for TRAIN: "
                f"{authority_quarantine['reason_code']}"
            )

        split_quarantine = evaluate_quarantine_source(record["split_id"], "TRAIN")
        if not split_quarantine["allowed"] or not split_quarantine["can_train"]:
            raise ValueError(
                f"record[{index}] split_id not authorized for TRAIN: "
                f"{split_quarantine['reason_code']}"
            )
    return materialized


def _count_fields(records: list[dict[str, Any]], field: str) -> dict[str, int]:
    return dict(sorted(Counter(str(record[field]) for record in records).items()))


def build_curriculum_coverage_report(
    records: Iterable[dict[str, Any]], *, required_strata: Iterable[str] = ()
) -> dict[str, Any]:
    """Generate deterministic raw curriculum coverage over validated synthetic records."""
    validated = _validated_records(records)
    strata = Counter(
        stratum for record in validated for stratum in record["curriculum_strata"]
    )
    languages = Counter(
        record["language_profile"]["primary_language"] for record in validated
    )
    rendered_counts = [record.get("rendered_token_count") for record in validated]
    supervised_counts = [record.get("supervised_token_count") for record in validated]
    required = tuple(required_strata)
    uncovered = sorted({item for item in required if item not in strata})

    source_counts = _count_fields(validated, "source_authority_id") if validated else {}
    return {
        "record_count": len(validated),
        "role_coverage": _count_fields(validated, "role_class") if validated else {},
        "curriculum_coverage": dict(sorted(strata.items())),
        "language_coverage": dict(sorted(languages.items())),
        "multi_turn_coverage": sum(
            1
            for record in validated
            if "multi" in record["conversation_structure_id"].lower()
        ),
        "abstention_coverage": sum(
            1
            for record in validated
            if any("abstention" in stratum.lower() for stratum in record["curriculum_strata"])
        ),
        "supervised_token_distribution": [
            value for value in supervised_counts if isinstance(value, int)
        ],
        "rendered_token_distribution": [
            value for value in rendered_counts if isinstance(value, int)
        ],
        "source_concentration": source_counts,
        "verification_state_distribution": _count_fields(
            validated, "source_verification_status"
        )
        if validated
        else {},
        "knowledge_placement_distribution": _count_fields(
            validated, "knowledge_placement"
        )
        if validated
        else {},
        "uncovered_required_strata": uncovered,
    }


def build_dataset_snapshot(
    records: Iterable[dict[str, Any]],
    *,
    snapshot_id: str,
    canonical_order_identity: str,
    duplicate_report_id: str,
    contamination_report_id: str,
    quarantine_verification_id: str,
) -> dict[str, Any]:
    """Build a deterministic synthetic snapshot without reading real training data."""
    validated = _validated_records(records)
    coverage = build_curriculum_coverage_report(validated)

    rendered_values = [record.get("rendered_token_count") for record in validated]
    supervised_values = [record.get("supervised_token_count") for record in validated]
    all_rendered = all(isinstance(value, int) and not isinstance(value, bool) for value in rendered_values)
    all_supervised = all(isinstance(value, int) and not isinstance(value, bool) for value in supervised_values)

    snapshot: dict[str, Any] = {
        "snapshot_id": snapshot_id,
        "snapshot_sha256": "0" * 64,
        "record_ids": [record["record_id"] for record in validated],
        "canonical_order_identity": canonical_order_identity,
        "record_count": len(validated),
        "rendered_token_count": sum(rendered_values) if all_rendered else None,
        "supervised_token_count": sum(supervised_values) if all_supervised else None,
        "source_summary": _count_fields(validated, "source_authority_id") if validated else {},
        "license_summary": _count_fields(validated, "source_license_id") if validated else {},
        "role_coverage": coverage["role_coverage"],
        "curriculum_coverage": coverage["curriculum_coverage"],
        "language_coverage": coverage["language_coverage"],
        "duplicate_report_id": duplicate_report_id,
        "contamination_report_id": contamination_report_id,
        "quarantine_verification_id": quarantine_verification_id,
        "knowledge_placement_summary": coverage["knowledge_placement_distribution"],
    }
    snapshot["snapshot_sha256"] = compute_dataset_snapshot_sha256(snapshot)
    errors = validate_dataset_snapshot(snapshot)
    if errors:
        raise ValueError("generated DatasetSnapshot invalid: " + "; ".join(errors))
    return snapshot