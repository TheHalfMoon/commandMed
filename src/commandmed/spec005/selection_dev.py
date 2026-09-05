"""Fail-closed Spec 005 selection-dev manifest validation.

This module implements the candidate-neutral Q2 manifest structure without
opening evaluation payloads or authoring clinical case content. It binds only
case metadata, lifecycle purpose, source identity, pairing, and contamination
state required before any separately authorized execution.
"""

from __future__ import annotations

import copy
import re
from typing import Any

from ..eval_contract.canonical import compute_canonical_sha256
from ..eval_contract.model import Purpose, Role
from .science import EXPECTED_LANES

MANIFEST_SCHEMA_VERSION = "1.0"
METRICS_CONTRACT_SCHEMA_ID = "commandmed-metrics-catalog"
METRICS_CONTRACT_SCHEMA_VERSION = "2.0"
METRICS_CATALOG_PATH = "data/eval/metrics-v2.json"
METRICS_V2_SHA256 = "bad51bffe30c0fb7de37afcaf8620ad1ad2deed2dd626a1ec6c2eb47c4107f4b"

SELECTION_DEV_PURPOSES = frozenset({Purpose.DEV.value, Purpose.CHECKPOINT_SELECTION.value})
CONCRETE_ROLES = frozenset(
    {
        Role.PATIENT_CAREGIVER.value,
        Role.CLINICAL_PROFESSIONAL.value,
        Role.LEARNER_RESEARCHER.value,
    }
)
LANGUAGE_VALUES = frozenset({"en", "ar", "EXPLICIT_NOT_APPLICABLE"})
EXPLICIT_NONE = "EXPLICIT_NONE"
UNRESOLVED_CONTAMINATION = frozenset(
    {"", "NONE", "UNRESOLVED", "UNBOUND", "PENDING", "NOT_ASSESSED"}
)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

MANIFEST_FIELDS = frozenset(
    {
        "manifest_id",
        "schema_version",
        "metrics_contract_schema_id",
        "metrics_contract_schema_version",
        "metrics_catalog_path",
        "metrics_catalog_sha256",
        "candidate_neutral",
        "pre_result_freeze",
        "case_records",
        "manifest_canonical_sha256",
    }
)
CASE_FIELDS = frozenset(
    {
        "case_id",
        "root_case_id_or_explicit_none",
        "quality_lane",
        "role",
        "language_or_explicit_not_applicable",
        "use_context_or_task_stratum",
        "source_component_id",
        "quarantine_purpose",
        "metric_id_or_metric_mapping_id",
        "pair_id_or_explicit_none",
        "fold_id_or_explicit_none",
        "artifact_identity",
        "source_revision",
        "contamination_evidence_identity_or_unresolved_state",
    }
)


def _resolved_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _exact_fields(value: Any, required: frozenset[str], prefix: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{prefix}: expected object"]
    keys = set(value)
    missing = sorted(required - keys)
    extra = sorted(keys - required)
    errors: list[str] = []
    if missing:
        errors.append(f"{prefix}: missing fields {missing}")
    if extra:
        errors.append(f"{prefix}: unexpected fields {extra}")
    return errors


def _canonical_payload(manifest: dict[str, Any]) -> dict[str, Any]:
    payload = copy.deepcopy(manifest)
    payload.pop("manifest_canonical_sha256", None)
    case_records = payload.get("case_records")
    if isinstance(case_records, list) and all(
        isinstance(case, dict) and isinstance(case.get("case_id"), str)
        for case in case_records
    ):
        payload["case_records"] = sorted(case_records, key=lambda case: case["case_id"])
    return payload


def compute_selection_dev_manifest_sha256(manifest: Any) -> str | None:
    if not isinstance(manifest, dict):
        return None
    return compute_canonical_sha256(_canonical_payload(manifest))


def validate_selection_dev_case(case: Any, *, execution_ready: bool = False) -> list[str]:
    errors = _exact_fields(case, CASE_FIELDS, "case")
    if not isinstance(case, dict):
        return errors

    for field in (
        "case_id",
        "root_case_id_or_explicit_none",
        "use_context_or_task_stratum",
        "source_component_id",
        "metric_id_or_metric_mapping_id",
        "pair_id_or_explicit_none",
        "fold_id_or_explicit_none",
        "artifact_identity",
        "source_revision",
        "contamination_evidence_identity_or_unresolved_state",
    ):
        if not _resolved_string(case.get(field)):
            errors.append(f"case.{field}: required non-empty string")

    lane = case.get("quality_lane")
    if lane not in EXPECTED_LANES:
        errors.append("case.quality_lane: unsupported lane")

    if case.get("role") not in CONCRETE_ROLES:
        errors.append("case.role: must bind one concrete canonical role")

    if case.get("language_or_explicit_not_applicable") not in LANGUAGE_VALUES:
        errors.append("case.language_or_explicit_not_applicable: unsupported language token")

    purpose = case.get("quarantine_purpose")
    if purpose not in SELECTION_DEV_PURPOSES:
        errors.append(
            "case.quarantine_purpose: must be DEV or CHECKPOINT_SELECTION; "
            "TRAIN/PRIVATE_GOLD/PUBLIC_EXTERNAL_EVAL are prohibited"
        )

    root_id = case.get("root_case_id_or_explicit_none")
    pair_id = case.get("pair_id_or_explicit_none")
    if lane == "E_ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY":
        if root_id == EXPLICIT_NONE:
            errors.append("case.root_case_id_or_explicit_none: Lane E requires root identity")
        if pair_id == EXPLICIT_NONE:
            errors.append("case.pair_id_or_explicit_none: Lane E requires matched pair identity")
        if case.get("language_or_explicit_not_applicable") not in {"ar", "en"}:
            errors.append("case.language_or_explicit_not_applicable: Lane E requires ar or en")
        if purpose != Purpose.CHECKPOINT_SELECTION.value:
            errors.append("case.quarantine_purpose: Lane E selection evidence requires CHECKPOINT_SELECTION")

    contamination = case.get("contamination_evidence_identity_or_unresolved_state")
    if execution_ready and (
        not isinstance(contamination, str)
        or contamination.strip().upper() in UNRESOLVED_CONTAMINATION
    ):
        errors.append(
            "case.contamination_evidence_identity_or_unresolved_state: "
            "execution-ready manifest requires resolved contamination evidence"
        )

    return sorted(set(errors))


def _validate_arabic_pair_completeness(cases: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    pairs: dict[str, list[dict[str, Any]]] = {}
    for case in cases:
        if case.get("quality_lane") != "E_ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY":
            continue
        pair_id = case.get("pair_id_or_explicit_none")
        if isinstance(pair_id, str) and pair_id != EXPLICIT_NONE:
            pairs.setdefault(pair_id, []).append(case)

    for pair_id, members in sorted(pairs.items()):
        languages = [member.get("language_or_explicit_not_applicable") for member in members]
        roots = {member.get("root_case_id_or_explicit_none") for member in members}
        if len(members) != 2 or sorted(languages) != ["ar", "en"]:
            errors.append(
                f"pair[{pair_id}]: must contain exactly one ar and one en case"
            )
        if len(roots) != 1 or EXPLICIT_NONE in roots:
            errors.append(f"pair[{pair_id}]: both variants must share one resolved root_case_id")
    return errors


def validate_selection_dev_manifest(
    manifest: Any, *, execution_ready: bool = False
) -> list[str]:
    errors = _exact_fields(manifest, MANIFEST_FIELDS, "manifest")
    if not isinstance(manifest, dict):
        return errors

    if not _resolved_string(manifest.get("manifest_id")):
        errors.append("manifest.manifest_id: required non-empty string")
    if manifest.get("schema_version") != MANIFEST_SCHEMA_VERSION:
        errors.append("manifest.schema_version: expected 1.0")
    if manifest.get("metrics_contract_schema_id") != METRICS_CONTRACT_SCHEMA_ID:
        errors.append("manifest.metrics_contract_schema_id: exact metrics-v2 binding required")
    if manifest.get("metrics_contract_schema_version") != METRICS_CONTRACT_SCHEMA_VERSION:
        errors.append("manifest.metrics_contract_schema_version: exact metrics-v2 binding required")
    if manifest.get("metrics_catalog_path") != METRICS_CATALOG_PATH:
        errors.append("manifest.metrics_catalog_path: exact metrics-v2 path required")
    if manifest.get("metrics_catalog_sha256") != METRICS_V2_SHA256:
        errors.append("manifest.metrics_catalog_sha256: exact canonical metrics-v2 SHA required")
    if manifest.get("candidate_neutral") is not True:
        errors.append("manifest.candidate_neutral: must be true")
    if manifest.get("pre_result_freeze") is not True:
        errors.append("manifest.pre_result_freeze: must be true")

    cases = manifest.get("case_records")
    valid_cases: list[dict[str, Any]] = []
    if not isinstance(cases, list) or not cases:
        errors.append("manifest.case_records: non-empty list required")
    else:
        seen_case_ids: set[str] = set()
        for index, case in enumerate(cases):
            case_errors = validate_selection_dev_case(case, execution_ready=execution_ready)
            errors.extend(f"manifest.case_records[{index}]:{error}" for error in case_errors)
            if isinstance(case, dict):
                valid_cases.append(case)
                case_id = case.get("case_id")
                if isinstance(case_id, str):
                    if case_id in seen_case_ids:
                        errors.append(f"manifest.case_records[{index}].case_id: duplicate '{case_id}'")
                    seen_case_ids.add(case_id)
        errors.extend(_validate_arabic_pair_completeness(valid_cases))

    expected_sha = compute_selection_dev_manifest_sha256(manifest)
    claimed_sha = manifest.get("manifest_canonical_sha256")
    if not isinstance(claimed_sha, str) or not SHA256_RE.fullmatch(claimed_sha):
        errors.append("manifest.manifest_canonical_sha256: expected lowercase SHA-256")
    elif expected_sha != claimed_sha:
        errors.append("manifest.manifest_canonical_sha256: canonical SHA mismatch")

    return sorted(set(errors))
