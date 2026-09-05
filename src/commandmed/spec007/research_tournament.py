"""Offline SP007-RO-001 research-component tournament contracts.

This module validates only static protocol, evaluation-asset, and evidence-pack
metadata. It never loads model weights, executes inference, accesses a device,
selects a winner, starts training, accesses protected data, or grants authority.
"""

from __future__ import annotations

from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.foundation import is_canonical_sha256, validate_closed_object
from src.commandmed.spec007.research_scope import (
    RESEARCH_COMPONENT_CLAIM_CLASS,
    RESEARCH_COMPONENT_REQUIRED_GUARDS,
    RESEARCH_COMPONENT_SCOPE_ID,
)

RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID = (
    "SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1"
)
RESEARCH_COMPONENT_TOURNAMENT_PURPOSE = "SP007_RO_001_BACKBONE_EVIDENCE"
RESEARCH_COMPONENT_EXECUTION_AUTHORITY_ID = "E004_SUCCESSOR_EXECUTION_DECISION_B"
SENTINEL_FIXTURE_SET_SHA256 = (
    "5a2bd28b391010c9575c99654899cd442fea8d94cbb4176045b654c940fa2fd3"
)
SENTINEL_FIXTURE_SHA256_SET_SHA256 = (
    "b65b36689cf2006bad8b446536d50ccd3f3440a4b244c044a1b26409aea0fef2"
)
CANONICAL_GUARD_FIXTURE_SHA256 = {
    "RO_GUARD_001_OUT_OF_SCOPE_PATIENT_ADVICE": (
        "6ae5dcdfe4ab75b55cee81439f26242ed89c4867fb5fca125de1cf7b713ce4d4"
    ),
    "RO_GUARD_002_OUT_OF_SCOPE_CLINICAL_PROFESSIONAL_ADVICE": (
        "0104be64bebbcd08dbf27971cc953d3abeb9ca07cc84dd7432e6d30f9646f518"
    ),
    "RO_GUARD_003_EMERGENCY_SENTINEL": (
        "7b6653af5e0260ce01b42dca82be476b1cff1d6ba7c46a0ea82a7b492d45606b"
    ),
    "RO_GUARD_004_MEDICATION_SENTINEL": (
        "136d3520fe3fc9569615be66072e4cb634fe91c15a56b0af21915dba2cff94b7"
    ),
    "RO_GUARD_005_DETERMINISTIC_TOOL_BOUNDARY": (
        "2c3a5519c4bb6cd79f8e2f8a8d95fe05bf3e90b520ab80f7f6a43b4f6f294d5e"
    ),
    "RO_GUARD_006_UNSUPPORTED_CERTAINTY": (
        "eb7557b946f7c55c4e99a69783aad015f04e21026c1564ba4098f697d1ecc825"
    ),
    "RO_GUARD_007_SCOPE_ESCAPE": (
        "83628c0c1ef3cd5c89b77b4c88756784b24fc0647f76d97b355bd06363ae15e4"
    ),
}

PRIMARY_CANDIDATES = (
    ("Qwen/Qwen3-0.6B-Base", "da87bfb608c14b7cf20ba1ce41287e8de496c0cd"),
    ("Qwen/Qwen3.5-0.8B-Base", "dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68"),
    (
        "ibm-granite/granite-4.0-350m-base",
        "a50b46cef21c8a86b15f0496cb794487a78a910b",
    ),
)
CONTROL_CANDIDATE = (
    "Qwen/Qwen3-4B-Base",
    "906bfd4b4dc7f14ee4320094d8b41684abff8539",
)

ALLOWED_RANKING_METRIC_FAMILIES = frozenset(
    {
        "GENERAL_INSTRUCTION_FOLLOWING",
        "GENERAL_ENGLISH_LANGUAGE",
        "GENERAL_ARABIC_LANGUAGE_NON_CLINICAL",
        "UNCERTAINTY_AND_ABSTENTION",
        "SYNTHETIC_NON_CLINICAL_TOOL_ROUTING",
        "GENERAL_CAPABILITY_PRESERVATION",
        "RESOURCE_EFFICIENCY",
    }
)
ALLOWED_SELECTION_SOURCE_CLASSES = frozenset(
    {
        "PUBLIC_UNGATED_NONCLINICAL",
        "REPOSITORY_FROZEN_NONCLINICAL",
        "SYNTHETIC_NONCLINICAL_EVALUATION",
    }
)
PROHIBITED_CLINICAL_METRIC_IDS = frozenset(
    {
        "emergency_miss_rate",
        "medication_critical_error_rate",
        "selective_risk_at_target_coverage",
        "citation_entailment_fidelity",
        "arabic_clinical_parity_gap",
        "lab_report_field_extraction_accuracy",
        "benign_case_over_triage_rate",
    }
)
PROHIBITED_SELECTION_SOURCE_CLASSES = frozenset(
    {
        "PRIVATE_GOLD",
        "PRIVATE_GOLD_FINAL_AUDIT",
        "PROTECTED_EVALUATION",
        "ABORT_SENTINEL",
        "HUMAN_REVIEW_DISPOSITION",
        "CLINICAL_REVIEW_DISPOSITION",
        "STATISTICAL_REVIEW_DISPOSITION",
    }
)

_PROTOCOL_FIELDS = (
    "schema_version",
    "protocol_id",
    "protocol_sha256",
    "scope_id",
    "claim_class",
    "purpose",
    "candidate_bindings",
    "ranking_metric_families",
    "evaluation_asset_manifests",
    "sentinel_fixture_set_sha256",
    "sentinel_fixture_sha256_set_sha256",
    "sentinel_can_rank",
    "private_gold_allowed",
    "clinical_metric_ids_allowed",
    "candidate_result_visibility_before_freeze",
    "winner_selection_performed_by_protocol",
    "pre_result_freeze",
    "authorized_spend_usd",
)
_CANDIDATE_FIELDS = (
    "candidate_id",
    "upstream_revision",
    "candidate_role",
    "winner_eligible",
    "purpose",
)
_ASSET_FIELDS = (
    "asset_id",
    "metric_family",
    "source_class",
    "source_authority_id",
    "source_license_id",
    "license_validation_status",
    "content_sha256",
    "split_id",
    "provenance_validation_status",
    "source_verification_status",
    "contamination_status",
    "quarantine_can_select_model",
    "purpose",
)
_EVIDENCE_PACK_FIELDS = (
    "schema_version",
    "evidence_pack_id",
    "evidence_pack_sha256",
    "protocol_id",
    "protocol_sha256",
    "candidate_results",
    "sentinel_guard_results",
    "execution_environment_id",
    "execution_authority_id",
    "spend_usd",
    "winner_selected",
    "recommendation",
)
_CANDIDATE_RESULT_FIELDS = (
    "candidate_id",
    "upstream_revision",
    "candidate_role",
    "metric_results",
    "resource_result_ids",
    "qualification_disposition",
)
_METRIC_RESULT_FIELDS = (
    "metric_family",
    "asset_id",
    "value_identity",
    "deterministic_evaluator_id",
)
_SENTINEL_RESULT_FIELDS = (
    "guard_id",
    "fixture_sha256",
    "violation_count",
    "disposition",
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _unique_nonempty_strings(value: Any, field: str) -> list[str]:
    if not isinstance(value, list) or not value:
        return [f"{field}: must be a non-empty list"]
    if any(not _nonempty(item) for item in value):
        return [f"{field}: entries must be non-empty strings"]
    if len(value) != len(set(value)):
        return [f"{field}: entries must be unique"]
    return []


def _self_hash(record: Mapping[str, Any], identity_field: str) -> str:
    projection = dict(record)
    projection.pop(identity_field, None)
    return compute_canonical_sha256(projection)


def compute_research_component_tournament_protocol_sha256(
    protocol: Mapping[str, Any],
) -> str:
    return _self_hash(protocol, "protocol_sha256")


def compute_research_component_tournament_evidence_pack_sha256(
    evidence_pack: Mapping[str, Any],
) -> str:
    return _self_hash(evidence_pack, "evidence_pack_sha256")


def _validate_self_hash(
    record: Mapping[str, Any], field: str, expected: str, prefix: str
) -> list[str]:
    claimed = record.get(field)
    if not is_canonical_sha256(claimed):
        return [f"{prefix}: {field} must be lowercase sha256 hex"]
    if claimed != expected:
        return [f"{prefix}: {field} mismatch"]
    return []


def _validate_candidate_bindings(value: Any) -> list[str]:
    prefix = "ResearchComponentTournamentProtocol.candidate_bindings"
    if not isinstance(value, list) or len(value) != 4:
        return [f"{prefix}: must contain exactly four frozen candidates"]
    errors: list[str] = []
    expected_primary = set(PRIMARY_CANDIDATES)
    seen: set[tuple[str, str]] = set()
    seen_primary: set[tuple[str, str]] = set()
    seen_control = False
    for index, candidate in enumerate(value):
        item_prefix = f"{prefix}[{index}]"
        item_errors = validate_closed_object(
            candidate, required_fields=_CANDIDATE_FIELDS, field=item_prefix
        )
        errors.extend(item_errors)
        if item_errors or not isinstance(candidate, dict):
            continue
        pair = (candidate.get("candidate_id"), candidate.get("upstream_revision"))
        if not all(_nonempty(item) for item in pair):
            errors.append(f"{item_prefix}: candidate identity must be non-empty")
            continue
        if pair in seen:
            errors.append(f"{item_prefix}: duplicate candidate identity")
        seen.add(pair)
        if pair in expected_primary:
            seen_primary.add(pair)
            if candidate.get("candidate_role") != "PRIMARY":
                errors.append(f"{item_prefix}: frozen primary must have role PRIMARY")
            if candidate.get("winner_eligible") is not True:
                errors.append(f"{item_prefix}: frozen primary must be winner eligible")
            if candidate.get("purpose") != "BACKBONE_CANDIDATE":
                errors.append(f"{item_prefix}: primary purpose must be BACKBONE_CANDIDATE")
        elif pair == CONTROL_CANDIDATE:
            seen_control = True
            if candidate.get("candidate_role") != "CONTROL":
                errors.append(f"{item_prefix}: frozen control must have role CONTROL")
            if candidate.get("winner_eligible") is not False:
                errors.append(f"{item_prefix}: control must not be winner eligible")
            if candidate.get("purpose") != "SCALE_QUALITY_OPPORTUNITY_COST":
                errors.append(
                    f"{item_prefix}: control purpose must be SCALE_QUALITY_OPPORTUNITY_COST"
                )
        else:
            errors.append(f"{item_prefix}: candidate identity is outside frozen E001 set")
    if seen_primary != expected_primary:
        errors.append(f"{prefix}: exact frozen primary set required")
    if not seen_control:
        errors.append(f"{prefix}: exact frozen control required")
    return errors


def _validate_evaluation_assets(value: Any, metric_families: set[str]) -> list[str]:
    prefix = "ResearchComponentTournamentProtocol.evaluation_asset_manifests"
    if not isinstance(value, list) or not value:
        return [f"{prefix}: must be a non-empty list"]
    errors: list[str] = []
    seen_asset_ids: set[str] = set()
    seen_families: set[str] = set()
    for index, asset in enumerate(value):
        item_prefix = f"{prefix}[{index}]"
        item_errors = validate_closed_object(
            asset, required_fields=_ASSET_FIELDS, field=item_prefix
        )
        errors.extend(item_errors)
        if item_errors or not isinstance(asset, dict):
            continue
        asset_id = asset.get("asset_id")
        family = asset.get("metric_family")
        source_class = asset.get("source_class")
        if not _nonempty(asset_id):
            errors.append(f"{item_prefix}: asset_id must be non-empty")
        elif asset_id in seen_asset_ids:
            errors.append(f"{item_prefix}: duplicate asset_id")
        else:
            seen_asset_ids.add(asset_id)
        if asset_id in PROHIBITED_CLINICAL_METRIC_IDS:
            errors.append(f"{item_prefix}: clinical metric identity is prohibited")
        if family not in ALLOWED_RANKING_METRIC_FAMILIES or family not in metric_families:
            errors.append(f"{item_prefix}: metric_family is not frozen for ranking")
        elif family in seen_families:
            errors.append(f"{item_prefix}: duplicate metric_family")
        else:
            seen_families.add(family)
        if source_class in PROHIBITED_SELECTION_SOURCE_CLASSES:
            errors.append(f"{item_prefix}: source_class is prohibited for selection")
        elif source_class not in ALLOWED_SELECTION_SOURCE_CLASSES:
            errors.append(f"{item_prefix}: source_class is not in the frozen allowlist")
        for field in ("source_authority_id", "source_license_id", "split_id"):
            if not _nonempty(asset.get(field)):
                errors.append(f"{item_prefix}: {field} must be non-empty")
        if asset.get("license_validation_status") != "PASS":
            errors.append(f"{item_prefix}: license_validation_status must equal PASS")
        if not is_canonical_sha256(asset.get("content_sha256")):
            errors.append(f"{item_prefix}: content_sha256 must be lowercase sha256 hex")
        if asset.get("provenance_validation_status") != "PASS":
            errors.append(f"{item_prefix}: provenance_validation_status must equal PASS")
        if asset.get("source_verification_status") != "PASS":
            errors.append(f"{item_prefix}: source_verification_status must equal PASS")
        if asset.get("contamination_status") != "PASS":
            errors.append(f"{item_prefix}: contamination_status must equal PASS")
        if asset.get("quarantine_can_select_model") is not True:
            errors.append(f"{item_prefix}: quarantine_can_select_model must be true")
        if asset.get("purpose") != "COMPONENT_TOURNAMENT_SELECTION":
            errors.append(
                f"{item_prefix}: purpose must equal COMPONENT_TOURNAMENT_SELECTION"
            )
    if seen_families != metric_families:
        errors.append(f"{prefix}: exact one-asset-per-ranking-family coverage required")
    if isinstance(value, list) and len(value) != len(metric_families):
        errors.append(f"{prefix}: asset count must equal ranking metric-family count")
    return errors


def validate_research_component_tournament_protocol(protocol: Any) -> list[str]:
    """Validate a frozen non-clinical tournament protocol for SP007-RO-001."""
    prefix = "ResearchComponentTournamentProtocol"
    errors = validate_closed_object(protocol, required_fields=_PROTOCOL_FIELDS, field=prefix)
    if errors or not isinstance(protocol, dict):
        return errors
    if protocol.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version must equal '1'")
    if protocol.get("protocol_id") != RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID:
        errors.append(f"{prefix}: protocol_id mismatch")
    if protocol.get("scope_id") != RESEARCH_COMPONENT_SCOPE_ID:
        errors.append(f"{prefix}: scope_id mismatch")
    if protocol.get("claim_class") != RESEARCH_COMPONENT_CLAIM_CLASS:
        errors.append(f"{prefix}: claim_class mismatch")
    if protocol.get("purpose") != RESEARCH_COMPONENT_TOURNAMENT_PURPOSE:
        errors.append(f"{prefix}: purpose mismatch")
    errors.extend(_validate_candidate_bindings(protocol.get("candidate_bindings")))

    metric_families = protocol.get("ranking_metric_families")
    errors.extend(
        _unique_nonempty_strings(metric_families, f"{prefix}.ranking_metric_families")
    )
    metric_set = set(metric_families) if isinstance(metric_families, list) else set()
    if metric_set != set(ALLOWED_RANKING_METRIC_FAMILIES):
        errors.append(
            f"{prefix}: ranking_metric_families must equal the frozen non-clinical set"
        )
    errors.extend(
        _validate_evaluation_assets(protocol.get("evaluation_asset_manifests"), metric_set)
    )

    if protocol.get("sentinel_fixture_set_sha256") != SENTINEL_FIXTURE_SET_SHA256:
        errors.append(f"{prefix}: sentinel_fixture_set_sha256 mismatch")
    if (
        protocol.get("sentinel_fixture_sha256_set_sha256")
        != SENTINEL_FIXTURE_SHA256_SET_SHA256
    ):
        errors.append(f"{prefix}: sentinel_fixture_sha256_set_sha256 mismatch")
    if protocol.get("sentinel_can_rank") is not False:
        errors.append(f"{prefix}: sentinel_can_rank must be false")
    if protocol.get("private_gold_allowed") is not False:
        errors.append(f"{prefix}: private_gold_allowed must be false")
    if protocol.get("clinical_metric_ids_allowed") != []:
        errors.append(f"{prefix}: clinical_metric_ids_allowed must be []")
    if protocol.get("candidate_result_visibility_before_freeze") is not False:
        errors.append(
            f"{prefix}: candidate_result_visibility_before_freeze must be false"
        )
    if protocol.get("winner_selection_performed_by_protocol") is not False:
        errors.append(f"{prefix}: protocol must not select a winner")
    if protocol.get("pre_result_freeze") is not True:
        errors.append(f"{prefix}: pre_result_freeze must be true")
    if protocol.get("authorized_spend_usd") != 0:
        errors.append(f"{prefix}: authorized_spend_usd must equal 0")
    errors.extend(
        _validate_self_hash(
            protocol,
            "protocol_sha256",
            compute_research_component_tournament_protocol_sha256(protocol),
            prefix,
        )
    )
    return sorted(set(errors))


def validate_research_component_tournament_evidence_pack(
    evidence_pack: Any, protocol: Any
) -> list[str]:
    """Validate evidence only; winner selection remains outside this contract."""
    prefix = "ResearchComponentTournamentEvidencePack"
    errors = validate_closed_object(
        evidence_pack, required_fields=_EVIDENCE_PACK_FIELDS, field=prefix
    )
    if errors or not isinstance(evidence_pack, dict):
        return errors
    protocol_errors = validate_research_component_tournament_protocol(protocol)
    if protocol_errors or not isinstance(protocol, dict):
        errors.append(f"{prefix}: bound protocol is invalid")
        return sorted(set(errors))

    if evidence_pack.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version must equal '1'")
    if not _nonempty(evidence_pack.get("evidence_pack_id")):
        errors.append(f"{prefix}: evidence_pack_id must be non-empty")
    if evidence_pack.get("protocol_id") != protocol.get("protocol_id"):
        errors.append(f"{prefix}: protocol_id mismatch")
    if evidence_pack.get("protocol_sha256") != protocol.get("protocol_sha256"):
        errors.append(f"{prefix}: protocol_sha256 mismatch")

    expected_candidates = {
        (item["candidate_id"], item["upstream_revision"]): item
        for item in protocol["candidate_bindings"]
    }
    assets_by_family = {
        item["metric_family"]: item["asset_id"]
        for item in protocol["evaluation_asset_manifests"]
    }
    candidate_results = evidence_pack.get("candidate_results")
    if not isinstance(candidate_results, list) or len(candidate_results) != 4:
        errors.append(f"{prefix}: candidate_results must contain exactly four records")
    else:
        seen: set[tuple[str, str]] = set()
        for index, result in enumerate(candidate_results):
            item_prefix = f"{prefix}.candidate_results[{index}]"
            item_errors = validate_closed_object(
                result, required_fields=_CANDIDATE_RESULT_FIELDS, field=item_prefix
            )
            errors.extend(item_errors)
            if item_errors or not isinstance(result, dict):
                continue
            pair = (result.get("candidate_id"), result.get("upstream_revision"))
            binding = expected_candidates.get(pair)
            if binding is None:
                errors.append(f"{item_prefix}: result candidate is outside frozen set")
                continue
            if pair in seen:
                errors.append(f"{item_prefix}: duplicate candidate result")
            seen.add(pair)
            if result.get("candidate_role") != binding.get("candidate_role"):
                errors.append(f"{item_prefix}: candidate_role mismatch")

            metric_results = result.get("metric_results")
            if not isinstance(metric_results, list) or len(metric_results) != len(
                ALLOWED_RANKING_METRIC_FAMILIES
            ):
                errors.append(f"{item_prefix}: exact metric-family coverage required")
            else:
                families: set[str] = set()
                for metric_index, metric_result in enumerate(metric_results):
                    metric_prefix = f"{item_prefix}.metric_results[{metric_index}]"
                    metric_errors = validate_closed_object(
                        metric_result,
                        required_fields=_METRIC_RESULT_FIELDS,
                        field=metric_prefix,
                    )
                    errors.extend(metric_errors)
                    if metric_errors or not isinstance(metric_result, dict):
                        continue
                    family = metric_result.get("metric_family")
                    if family not in ALLOWED_RANKING_METRIC_FAMILIES:
                        errors.append(f"{metric_prefix}: prohibited metric_family")
                    elif family in families:
                        errors.append(f"{metric_prefix}: duplicate metric_family")
                    else:
                        families.add(family)
                    if metric_result.get("asset_id") != assets_by_family.get(family):
                        errors.append(f"{metric_prefix}: asset_id mismatch for metric_family")
                    for field in ("value_identity", "deterministic_evaluator_id"):
                        if not _nonempty(metric_result.get(field)):
                            errors.append(f"{metric_prefix}: {field} must be non-empty")
                if families != set(ALLOWED_RANKING_METRIC_FAMILIES):
                    errors.append(f"{item_prefix}: metric-family set mismatch")
            errors.extend(
                _unique_nonempty_strings(
                    result.get("resource_result_ids"),
                    f"{item_prefix}.resource_result_ids",
                )
            )
            if result.get("qualification_disposition") not in {
                "PASS",
                "FAIL",
                "DISQUALIFIED",
            }:
                errors.append(f"{item_prefix}: unsupported qualification_disposition")
        if seen != set(expected_candidates):
            errors.append(f"{prefix}: exact frozen candidate result set required")

    sentinel_results = evidence_pack.get("sentinel_guard_results")
    if not isinstance(sentinel_results, list) or len(sentinel_results) != 7:
        errors.append(f"{prefix}: sentinel_guard_results must contain exactly seven records")
    else:
        guard_ids: set[str] = set()
        for index, result in enumerate(sentinel_results):
            item_prefix = f"{prefix}.sentinel_guard_results[{index}]"
            item_errors = validate_closed_object(
                result, required_fields=_SENTINEL_RESULT_FIELDS, field=item_prefix
            )
            errors.extend(item_errors)
            if item_errors or not isinstance(result, dict):
                continue
            guard_id = result.get("guard_id")
            if guard_id not in RESEARCH_COMPONENT_REQUIRED_GUARDS:
                errors.append(f"{item_prefix}: guard_id is outside canonical set")
            elif guard_id in guard_ids:
                errors.append(f"{item_prefix}: duplicate guard_id")
            else:
                guard_ids.add(guard_id)
            if result.get("fixture_sha256") != CANONICAL_GUARD_FIXTURE_SHA256.get(guard_id):
                errors.append(f"{item_prefix}: fixture_sha256 mismatch for guard_id")
            violations = result.get("violation_count")
            if type(violations) is not int or violations < 0:
                errors.append(f"{item_prefix}: violation_count must be non-negative integer")
            disposition = result.get("disposition")
            if disposition not in {"PASS", "FAIL"}:
                errors.append(f"{item_prefix}: disposition must be PASS or FAIL")
            if violations == 0 and disposition != "PASS":
                errors.append(f"{item_prefix}: zero violations require PASS")
            if type(violations) is int and violations > 0 and disposition != "FAIL":
                errors.append(f"{item_prefix}: positive violations require FAIL")
        if guard_ids != set(RESEARCH_COMPONENT_REQUIRED_GUARDS):
            errors.append(f"{prefix}: exact canonical guard set required")

    if not _nonempty(evidence_pack.get("execution_environment_id")):
        errors.append(f"{prefix}: execution_environment_id must be non-empty")
    if evidence_pack.get("execution_authority_id") != RESEARCH_COMPONENT_EXECUTION_AUTHORITY_ID:
        errors.append(f"{prefix}: execution_authority_id mismatch")
    if evidence_pack.get("spend_usd") != 0:
        errors.append(f"{prefix}: spend_usd must equal 0")
    if evidence_pack.get("winner_selected") is not False:
        errors.append(f"{prefix}: winner_selected must be false")
    if evidence_pack.get("recommendation") != "NONE":
        errors.append(f"{prefix}: recommendation must equal NONE")
    errors.extend(
        _validate_self_hash(
            evidence_pack,
            "evidence_pack_sha256",
            compute_research_component_tournament_evidence_pack_sha256(evidence_pack),
            prefix,
        )
    )
    return sorted(set(errors))
