"""Deterministic admission and freeze helpers for SP007-RO-001 evaluation assets.

This module is offline control-plane code. It validates only project-authored,
non-clinical synthetic evaluation fixtures and their evidence bindings. It never
loads model weights, executes inference, opens a device, performs training,
accesses protected data, or selects a winner.
"""

from __future__ import annotations

import hashlib
from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.eval_contract.lineage import (
    evaluate_lineage_admission,
    validate_lineage_contract,
    validate_lineage_record,
)
from src.commandmed.spec007.foundation import is_canonical_sha256, validate_closed_object
from src.commandmed.spec007.quarantine import (
    canonical_quarantine_matrix_sha256,
    evaluate_quarantine_source,
)
from src.commandmed.spec007.research_scope import RESEARCH_COMPONENT_SCOPE_ID
from src.commandmed.spec007.research_tournament import (
    ALLOWED_RANKING_METRIC_FAMILIES,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
    validate_research_component_tournament_protocol,
)

E001_CANDIDATE_MANIFEST_VERSION = "e001-mass-reach-v1"
E001_CANDIDATE_MANIFEST_SHA256 = (
    "98d586500d12e7904bce199061c48d5ac50e9f66a372de034d9ecba4e2d3cc28"
)
ASSET_NAMESPACE_SEED = "b85f140192a511cfbfe190476bdb3f6baf784b4d"
RIGHTS_INSTRUMENT_ID = "E004_RESEARCH_COMPONENT_PROJECT_AUTHORED_EVAL_RIGHTS_V1"
RIGHTS_INSTRUMENT_SHA256 = (
    "877205412550ac16a074634c6549e3e169bf216ddbb6216646307a05bf2f59d0"
)
PROVENANCE_AUTHORITY_ID = "E004_RESEARCH_COMPONENT_DETERMINISTIC_FIXTURE_PROVENANCE_V1"
CONTAMINATION_METHOD_ID = (
    "E004_RESEARCH_COMPONENT_POST_FREEZE_SYNTHETIC_NONEXPOSURE_V1"
)
CONTAMINATION_METHOD_SHA256 = (
    "190c8107cbf9f2f942cdc404f9cc7a00f185514c9e9a609431645f78261a8b6b"
)
EXPECTED_QUARANTINE_MATRIX_SHA256 = (
    "e2b2fd52e2eef007935ffe497fb50656960fa4ab82caac45138e117594475477"
)
ASSET_SET_ID = "SP007_RO_001_NONCLINICAL_EVALUATION_ASSET_SET_V1"

_FORBIDDEN_CLINICAL_SUBSTRINGS = (
    "patient",
    "diagnosis",
    "treatment",
    "medication",
    "prescription",
    "dose",
    "clinical",
    "triage",
    "emergency",
    "مريض",
    "تشخيص",
    "علاج",
    "دواء",
    "جرعة",
)

_RIGHTS_FIELDS = (
    "schema_version",
    "instrument_id",
    "instrument_sha256",
    "scope_id",
    "subject_class",
    "permitted_use",
    "external_payload_rights_reliance",
    "external_dataset_content_included",
    "private_gold_content_included",
    "phi_content_included",
    "training_or_adaptation_use_authorized",
    "redistribution_rights_claim_created",
    "commercial_rights_claim_created",
    "rights_basis",
    "current_authorized_spend_usd",
)
_CONTAMINATION_FIELDS = (
    "schema_version",
    "method_id",
    "method_sha256",
    "scope_id",
    "candidate_manifest_version",
    "candidate_manifest_sha256",
    "candidate_manifest_freeze_record",
    "candidate_manifest_freeze_date",
    "fixture_namespace_seed",
    "fixture_construction_after_candidate_freeze",
    "external_payloads_used",
    "candidate_outputs_observed_before_fixture_freeze",
    "adaptive_generation_from_candidate_outputs",
    "exact_fixture_nonce_method",
    "pass_semantics",
    "semantic_task_novelty_claim",
    "candidate_pretraining_corpus_inspection_claim",
    "private_gold_comparison",
    "current_authorized_spend_usd",
)
_ASSET_COMMON_FIELDS = (
    "schema_version",
    "asset_id",
    "asset_sha256",
    "scope_id",
    "metric_family",
    "source_class",
    "source_authority_id",
    "source_license_id",
    "rights_instrument_sha256",
    "contamination_method_id",
    "contamination_method_sha256",
    "candidate_manifest_version",
    "candidate_manifest_sha256",
    "fixture_namespace_seed",
    "split_id",
    "quarantine_purpose",
    "quarantine_matrix_sha256",
    "candidate_outputs_observed_before_freeze",
    "optimization_feedback_allowed",
    "external_payloads_used",
    "purpose",
    "asset_kind",
    "scoring_method",
)
_ASSET_SET_FIELDS = (
    "schema_version",
    "asset_set_id",
    "asset_set_sha256",
    "scope_id",
    "pre_result_freeze",
    "candidate_result_visibility_before_freeze",
    "asset_records",
)
_MC_CASE_FIELDS = (
    "case_id",
    "case_nonce",
    "prompt",
    "choices",
    "correct_choice_id",
    "scoring_method",
)
_CHOICE_FIELDS = ("choice_id", "text")
_RESOURCE_PROBE_FIELDS = (
    "probe_id",
    "probe_nonce",
    "input_text",
    "max_new_tokens",
    "warmup_runs",
    "measured_runs",
    "required_measurements",
)
_REQUIRED_RESOURCE_MEASUREMENTS = frozenset(
    {
        "MODEL_ARTIFACT_BYTES",
        "PEAK_RSS_BYTES",
        "TIME_TO_FIRST_TOKEN_MS",
        "DECODE_TOKENS_PER_SECOND",
        "WALL_CLOCK_MS",
    }
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _self_hash(record: Mapping[str, Any], identity_field: str) -> str:
    projection = dict(record)
    projection.pop(identity_field, None)
    return compute_canonical_sha256(projection)


def compute_rights_instrument_sha256(record: Mapping[str, Any]) -> str:
    return _self_hash(record, "instrument_sha256")


def compute_contamination_method_sha256(record: Mapping[str, Any]) -> str:
    return _self_hash(record, "method_sha256")


def compute_research_component_evaluation_asset_sha256(
    record: Mapping[str, Any],
) -> str:
    return _self_hash(record, "asset_sha256")


def compute_research_component_evaluation_asset_set_sha256(
    record: Mapping[str, Any],
) -> str:
    return _self_hash(record, "asset_set_sha256")


def _validate_self_hash(
    record: Mapping[str, Any],
    field: str,
    expected: str,
    prefix: str,
) -> list[str]:
    value = record.get(field)
    if not is_canonical_sha256(value):
        return [f"{prefix}: {field} must be lowercase sha256 hex"]
    if value != expected:
        return [f"{prefix}: {field} mismatch"]
    return []


def validate_research_component_evaluation_rights_instrument(
    record: Any,
) -> list[str]:
    prefix = "ResearchComponentEvaluationRightsInstrument"
    errors = validate_closed_object(record, required_fields=_RIGHTS_FIELDS, field=prefix)
    if errors or not isinstance(record, dict):
        return errors

    expected = {
        "schema_version": "1",
        "instrument_id": RIGHTS_INSTRUMENT_ID,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "subject_class": "PROJECT_AUTHORED_SYNTHETIC_NONCLINICAL_EVALUATION",
        "permitted_use": "COMPONENT_TOURNAMENT_SELECTION",
        "external_payload_rights_reliance": False,
        "external_dataset_content_included": False,
        "private_gold_content_included": False,
        "phi_content_included": False,
        "training_or_adaptation_use_authorized": False,
        "redistribution_rights_claim_created": False,
        "commercial_rights_claim_created": False,
        "rights_basis": "PROJECT_AUTHORED_CONTENT_INTERNAL_RESEARCH_EVALUATION_ONLY",
        "current_authorized_spend_usd": 0,
    }
    for field, value in expected.items():
        if record.get(field) != value:
            errors.append(f"{prefix}: {field} mismatch")
    errors.extend(
        _validate_self_hash(
            record,
            "instrument_sha256",
            compute_rights_instrument_sha256(record),
            prefix,
        )
    )
    if record.get("instrument_sha256") != RIGHTS_INSTRUMENT_SHA256:
        errors.append(f"{prefix}: canonical instrument identity mismatch")
    return sorted(set(errors))


def validate_research_component_contamination_method(record: Any) -> list[str]:
    prefix = "ResearchComponentEvaluationContaminationMethod"
    errors = validate_closed_object(
        record, required_fields=_CONTAMINATION_FIELDS, field=prefix
    )
    if errors or not isinstance(record, dict):
        return errors

    expected = {
        "schema_version": "1",
        "method_id": CONTAMINATION_METHOD_ID,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "candidate_manifest_version": E001_CANDIDATE_MANIFEST_VERSION,
        "candidate_manifest_sha256": E001_CANDIDATE_MANIFEST_SHA256,
        "candidate_manifest_freeze_record": (
            "specs/007-sft-v1/e001-candidate-manifest-freeze-2026-08-27.md"
        ),
        "candidate_manifest_freeze_date": "2026-08-27",
        "fixture_namespace_seed": ASSET_NAMESPACE_SEED,
        "fixture_construction_after_candidate_freeze": True,
        "external_payloads_used": False,
        "candidate_outputs_observed_before_fixture_freeze": False,
        "adaptive_generation_from_candidate_outputs": False,
        "exact_fixture_nonce_method": (
            "SHA256_NAMESPACE_SEED_METRIC_FAMILY_CASE_INDEX"
        ),
        "pass_semantics": (
            "EXACT_FIXTURE_NONEXPOSURE_AND_NONADAPTIVE_PRE_RESULT_FREEZE_ONLY"
        ),
        "semantic_task_novelty_claim": False,
        "candidate_pretraining_corpus_inspection_claim": False,
        "private_gold_comparison": False,
        "current_authorized_spend_usd": 0,
    }
    for field, value in expected.items():
        if record.get(field) != value:
            errors.append(f"{prefix}: {field} mismatch")
    errors.extend(
        _validate_self_hash(
            record,
            "method_sha256",
            compute_contamination_method_sha256(record),
            prefix,
        )
    )
    if record.get("method_sha256") != CONTAMINATION_METHOD_SHA256:
        errors.append(f"{prefix}: canonical method identity mismatch")
    return sorted(set(errors))


def _expected_nonce(metric_family: str, index: int) -> str:
    raw = f"{ASSET_NAMESPACE_SEED}|{metric_family}|{index}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]


def _contains_clinical_content(value: str) -> bool:
    # The frozen asset vocabulary explicitly uses "non-clinical" to mark
    # research-only content. Remove only that exact negative descriptor before
    # applying the unchanged positive clinical-marker denylist.
    lowered = value.lower().replace("non-clinical", "")
    return any(marker in lowered for marker in _FORBIDDEN_CLINICAL_SUBSTRINGS)


def _validate_mc_cases(asset: Mapping[str, Any]) -> list[str]:
    prefix = f"ResearchComponentEvaluationAsset({asset.get('asset_id')}).cases"
    cases = asset.get("cases")
    if not isinstance(cases, list) or len(cases) != 12:
        return [f"{prefix}: must contain exactly 12 frozen cases"]

    errors: list[str] = []
    seen_ids: set[str] = set()
    for index, case in enumerate(cases, start=1):
        item_prefix = f"{prefix}[{index - 1}]"
        item_errors = validate_closed_object(
            case, required_fields=_MC_CASE_FIELDS, field=item_prefix
        )
        errors.extend(item_errors)
        if item_errors or not isinstance(case, dict):
            continue
        case_id = case.get("case_id")
        if not _nonempty(case_id) or case_id in seen_ids:
            errors.append(f"{item_prefix}: case_id must be unique and non-empty")
        elif case_id != f"{asset.get('asset_id')}-CASE-{index:02d}":
            errors.append(f"{item_prefix}: case_id does not match frozen sequence")
        else:
            seen_ids.add(case_id)

        expected_nonce = _expected_nonce(str(asset.get("metric_family")), index)
        if case.get("case_nonce") != expected_nonce:
            errors.append(f"{item_prefix}: case_nonce mismatch")
        prompt = case.get("prompt")
        if not _nonempty(prompt) or expected_nonce not in str(prompt):
            errors.append(f"{item_prefix}: prompt must contain exact case nonce")
        elif _contains_clinical_content(str(prompt)):
            errors.append(f"{item_prefix}: clinical content is prohibited")
        if case.get("scoring_method") != "NORMALIZED_CONDITIONAL_LOG_LIKELIHOOD_ARGMAX":
            errors.append(f"{item_prefix}: scoring_method mismatch")

        choices = case.get("choices")
        if not isinstance(choices, list) or len(choices) != 4:
            errors.append(f"{item_prefix}: choices must contain exactly A-D")
            continue
        expected_choice_ids = ["A", "B", "C", "D"]
        actual_choice_ids: list[str] = []
        for choice_index, choice in enumerate(choices):
            choice_prefix = f"{item_prefix}.choices[{choice_index}]"
            choice_errors = validate_closed_object(
                choice, required_fields=_CHOICE_FIELDS, field=choice_prefix
            )
            errors.extend(choice_errors)
            if choice_errors or not isinstance(choice, dict):
                continue
            actual_choice_ids.append(str(choice.get("choice_id")))
            text = choice.get("text")
            if not _nonempty(text):
                errors.append(f"{choice_prefix}: text must be non-empty")
            elif _contains_clinical_content(str(text)):
                errors.append(f"{choice_prefix}: clinical content is prohibited")
        if actual_choice_ids != expected_choice_ids:
            errors.append(f"{item_prefix}: choice IDs must equal ['A','B','C','D']")
        if case.get("correct_choice_id") not in expected_choice_ids:
            errors.append(f"{item_prefix}: correct_choice_id must select A-D")
    return errors


def _validate_resource_probes(asset: Mapping[str, Any]) -> list[str]:
    prefix = f"ResearchComponentEvaluationAsset({asset.get('asset_id')}).probes"
    probes = asset.get("probes")
    if not isinstance(probes, list) or len(probes) != 8:
        return [f"{prefix}: must contain exactly 8 frozen probes"]

    errors: list[str] = []
    for index, probe in enumerate(probes, start=1):
        item_prefix = f"{prefix}[{index - 1}]"
        item_errors = validate_closed_object(
            probe, required_fields=_RESOURCE_PROBE_FIELDS, field=item_prefix
        )
        errors.extend(item_errors)
        if item_errors or not isinstance(probe, dict):
            continue
        if probe.get("probe_id") != f"{asset.get('asset_id')}-PROBE-{index:02d}":
            errors.append(f"{item_prefix}: probe_id mismatch")
        expected_nonce = _expected_nonce(str(asset.get("metric_family")), index)
        if probe.get("probe_nonce") != expected_nonce:
            errors.append(f"{item_prefix}: probe_nonce mismatch")
        text = probe.get("input_text")
        if not _nonempty(text) or expected_nonce not in str(text):
            errors.append(f"{item_prefix}: input_text must contain exact probe nonce")
        elif _contains_clinical_content(str(text)):
            errors.append(f"{item_prefix}: clinical content is prohibited")
        if probe.get("max_new_tokens") != 8:
            errors.append(f"{item_prefix}: max_new_tokens must equal 8")
        if probe.get("warmup_runs") != 1:
            errors.append(f"{item_prefix}: warmup_runs must equal 1")
        if probe.get("measured_runs") != 3:
            errors.append(f"{item_prefix}: measured_runs must equal 3")
        measurements = probe.get("required_measurements")
        if (
            not isinstance(measurements, list)
            or len(measurements) != len(set(measurements))
            or set(measurements) != set(_REQUIRED_RESOURCE_MEASUREMENTS)
        ):
            errors.append(f"{item_prefix}: required_measurements mismatch")
    return errors


def validate_research_component_evaluation_asset(record: Any) -> list[str]:
    prefix = "ResearchComponentEvaluationAsset"
    if not isinstance(record, dict):
        return [f"{prefix}: record must be an object"]

    required = list(_ASSET_COMMON_FIELDS)
    kind = record.get("asset_kind")
    if kind == "MULTIPLE_CHOICE_CONDITIONAL_LIKELIHOOD":
        required.append("cases")
    elif kind == "RESOURCE_MEASUREMENT_PROTOCOL":
        required.append("probes")
    errors = validate_closed_object(record, required_fields=tuple(required), field=prefix)

    expected = {
        "schema_version": "1",
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "source_class": "SYNTHETIC_NONCLINICAL_EVALUATION",
        "source_authority_id": PROVENANCE_AUTHORITY_ID,
        "source_license_id": RIGHTS_INSTRUMENT_ID,
        "rights_instrument_sha256": RIGHTS_INSTRUMENT_SHA256,
        "contamination_method_id": CONTAMINATION_METHOD_ID,
        "contamination_method_sha256": CONTAMINATION_METHOD_SHA256,
        "candidate_manifest_version": E001_CANDIDATE_MANIFEST_VERSION,
        "candidate_manifest_sha256": E001_CANDIDATE_MANIFEST_SHA256,
        "fixture_namespace_seed": ASSET_NAMESPACE_SEED,
        "split_id": "MODEL_SELECTION_DEV_SET",
        "quarantine_purpose": "CHECKPOINT_SELECTION",
        "quarantine_matrix_sha256": EXPECTED_QUARANTINE_MATRIX_SHA256,
        "candidate_outputs_observed_before_freeze": False,
        "optimization_feedback_allowed": False,
        "external_payloads_used": False,
        "purpose": "COMPONENT_TOURNAMENT_SELECTION",
    }
    for field, value in expected.items():
        if record.get(field) != value:
            errors.append(f"{prefix}: {field} mismatch")
    if record.get("metric_family") not in ALLOWED_RANKING_METRIC_FAMILIES:
        errors.append(f"{prefix}: metric_family is outside frozen non-clinical set")
    if not _nonempty(record.get("asset_id")):
        errors.append(f"{prefix}: asset_id must be non-empty")

    if kind == "MULTIPLE_CHOICE_CONDITIONAL_LIKELIHOOD":
        if record.get("metric_family") == "RESOURCE_EFFICIENCY":
            errors.append(f"{prefix}: RESOURCE_EFFICIENCY requires resource protocol kind")
        if record.get("scoring_method") != "NORMALIZED_CONDITIONAL_LOG_LIKELIHOOD_ARGMAX":
            errors.append(f"{prefix}: scoring_method mismatch")
        errors.extend(_validate_mc_cases(record))
    elif kind == "RESOURCE_MEASUREMENT_PROTOCOL":
        if record.get("metric_family") != "RESOURCE_EFFICIENCY":
            errors.append(f"{prefix}: resource protocol kind is reserved for RESOURCE_EFFICIENCY")
        if record.get("scoring_method") != "RESOURCE_MEASUREMENT_RECORD_V1":
            errors.append(f"{prefix}: scoring_method mismatch")
        errors.extend(_validate_resource_probes(record))
    else:
        errors.append(f"{prefix}: unsupported asset_kind")

    errors.extend(
        _validate_self_hash(
            record,
            "asset_sha256",
            compute_research_component_evaluation_asset_sha256(record),
            prefix,
        )
    )
    return sorted(set(errors))


def validate_research_component_evaluation_asset_set(record: Any) -> list[str]:
    prefix = "ResearchComponentEvaluationAssetSet"
    errors = validate_closed_object(
        record, required_fields=_ASSET_SET_FIELDS, field=prefix
    )
    if errors or not isinstance(record, dict):
        return errors
    if record.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version mismatch")
    if record.get("asset_set_id") != ASSET_SET_ID:
        errors.append(f"{prefix}: asset_set_id mismatch")
    if record.get("scope_id") != RESEARCH_COMPONENT_SCOPE_ID:
        errors.append(f"{prefix}: scope_id mismatch")
    if record.get("pre_result_freeze") is not True:
        errors.append(f"{prefix}: pre_result_freeze must be true")
    if record.get("candidate_result_visibility_before_freeze") is not False:
        errors.append(f"{prefix}: candidate_result_visibility_before_freeze must be false")

    assets = record.get("asset_records")
    if not isinstance(assets, list) or len(assets) != len(ALLOWED_RANKING_METRIC_FAMILIES):
        errors.append(f"{prefix}: exact seven-asset set required")
    else:
        seen_ids: set[str] = set()
        families: set[str] = set()
        for asset in assets:
            errors.extend(validate_research_component_evaluation_asset(asset))
            if isinstance(asset, dict):
                asset_id = asset.get("asset_id")
                family = asset.get("metric_family")
                if asset_id in seen_ids:
                    errors.append(f"{prefix}: duplicate asset_id")
                elif isinstance(asset_id, str):
                    seen_ids.add(asset_id)
                if family in families:
                    errors.append(f"{prefix}: duplicate metric_family")
                elif isinstance(family, str):
                    families.add(family)
        if families != set(ALLOWED_RANKING_METRIC_FAMILIES):
            errors.append(f"{prefix}: metric-family set mismatch")
    errors.extend(
        _validate_self_hash(
            record,
            "asset_set_sha256",
            compute_research_component_evaluation_asset_set_sha256(record),
            prefix,
        )
    )
    return sorted(set(errors))


def build_spec003_lineage_record(asset: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "asset_id": str(asset["asset_id"]),
        "asset_class": "BENCHMARK_OR_EVALUATION_ASSET",
        "canonical_name": str(asset["asset_id"]),
        "record_version": "1",
        "source_identifier": "github:TheHalfMoon/commandMed",
        "source_uri": "https://github.com/TheHalfMoon/commandMed",
        "source_revision": "UNBOUND",
        "source_verification_status": "VERIFIED",
        "source_evidence_uri": (
            "https://github.com/TheHalfMoon/commandMed/blob/main/"
            "specs/007-sft-v1/"
            "e004-research-component-tournament-evaluation-assets-v1.json"
        ),
        "declared_use": "DEVELOPMENT_EVALUATION",
        "access_class": "PUBLIC",
        "rights_state": "SUPPORTED",
        "rights_evidence_uri": (
            "https://github.com/TheHalfMoon/commandMed/blob/main/"
            "specs/007-sft-v1/"
            "e004-research-component-evaluation-asset-rights-instrument-v1.json"
        ),
        "artifact_binding_state": "DIRECT_DIGEST",
        "content_sha256": str(asset["asset_sha256"]),
        "phi_privacy_state": "NO_PHI_KNOWN",
        "purpose": "CHECKPOINT_SELECTION",
        "quarantine_state": "NOT_QUARANTINED",
        "contamination_state": "ASSESSED_CLEAN",
        "contamination_evidence_id": CONTAMINATION_METHOD_ID,
        "origin_type": "SYNTHETIC",
        "custom_terms_id": RIGHTS_INSTRUMENT_ID,
    }


def evaluate_research_component_asset_admission(
    asset: Mapping[str, Any],
    lineage_contract: Any,
) -> dict[str, Any]:
    errors = validate_research_component_evaluation_asset(asset)
    if errors:
        return {"state": "BLOCKED", "reason_codes": ["INVALID_COMPONENT_ASSET"]}
    contract_errors = validate_lineage_contract(lineage_contract)
    if contract_errors:
        return {"state": "BLOCKED", "reason_codes": ["INVALID_LINEAGE_CONTRACT"]}

    lineage = build_spec003_lineage_record(asset)
    record_errors = validate_lineage_record(lineage, lineage_contract)
    if record_errors:
        return {
            "state": "BLOCKED",
            "reason_codes": ["INVALID_LINEAGE_RECORD"],
            "record_errors": record_errors,
        }

    quarantine = evaluate_quarantine_source(
        str(asset["split_id"]), str(asset["quarantine_purpose"])
    )
    if (
        quarantine.get("quarantine_matrix_sha256")
        != EXPECTED_QUARANTINE_MATRIX_SHA256
        or quarantine.get("allowed") is not True
        or quarantine.get("can_select_model") is not True
        or quarantine.get("can_train") is not False
    ):
        return {
            "state": "BLOCKED",
            "reason_codes": ["QUARANTINE_SELECTION_BINDING_FAILED"],
        }

    return evaluate_lineage_admission(lineage, lineage_contract)


def build_protocol_asset_manifest(asset: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "asset_id": str(asset["asset_id"]),
        "metric_family": str(asset["metric_family"]),
        "source_class": str(asset["source_class"]),
        "source_authority_id": str(asset["source_authority_id"]),
        "source_license_id": str(asset["source_license_id"]),
        "license_validation_status": "PASS",
        "content_sha256": str(asset["asset_sha256"]),
        "split_id": str(asset["split_id"]),
        "provenance_validation_status": "PASS",
        "source_verification_status": "PASS",
        "contamination_status": "PASS",
        "quarantine_can_select_model": True,
        "purpose": "COMPONENT_TOURNAMENT_SELECTION",
    }


def validate_frozen_research_component_tournament_subject(
    *,
    rights_instrument: Any,
    contamination_method: Any,
    asset_set: Any,
    protocol: Any,
    lineage_contract: Any,
) -> list[str]:
    prefix = "FrozenResearchComponentTournamentSubject"
    errors: list[str] = []
    errors.extend(
        validate_research_component_evaluation_rights_instrument(rights_instrument)
    )
    errors.extend(validate_research_component_contamination_method(contamination_method))
    asset_errors = validate_research_component_evaluation_asset_set(asset_set)
    errors.extend(asset_errors)

    if canonical_quarantine_matrix_sha256() != EXPECTED_QUARANTINE_MATRIX_SHA256:
        errors.append(f"{prefix}: canonical quarantine matrix identity mismatch")

    if not asset_errors and isinstance(asset_set, dict):
        assets = asset_set.get("asset_records", [])
        expected_manifests = [build_protocol_asset_manifest(asset) for asset in assets]
        if not isinstance(protocol, dict):
            errors.append(f"{prefix}: protocol must be an object")
        else:
            if protocol.get("protocol_id") != RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID:
                errors.append(f"{prefix}: protocol_id mismatch")
            if protocol.get("evaluation_asset_manifests") != expected_manifests:
                errors.append(
                    f"{prefix}: protocol evaluation_asset_manifests do not match "
                    "the exact admitted asset set"
                )
        for asset in assets:
            result = evaluate_research_component_asset_admission(asset, lineage_contract)
            if result.get("state") != "ELIGIBLE":
                errors.append(
                    f"{prefix}: Spec003 admission is not ELIGIBLE for "
                    f"{asset.get('asset_id')}: {result.get('reason_codes')}"
                )

    errors.extend(validate_research_component_tournament_protocol(protocol))
    return sorted(set(errors))
