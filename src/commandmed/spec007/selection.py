"""Offline selection, reproducibility, resume, and evaluation-freeze contracts.

This module validates static Spec 007 control-plane records only. It does not
select a checkpoint, access a device, load model weights, execute evaluation,
or grant any authority referenced by a record.
"""

from __future__ import annotations

from typing import Any

from src.commandmed.spec007.foundation import (
    validate_canonical_sha256,
    validate_closed_object,
)
from src.commandmed.spec007.quarantine import evaluate_quarantine_source

_SELECTION_FIELDS = (
    "policy_id",
    "selection_mode",
    "checkpoint_rule",
    "selection_source_ids",
    "selection_source_purpose_authorization",
    "evaluation_asset_ranking_allowed",
    "abort_sentinel_can_rank",
    "recipe_tuning_allowed",
    "hyperparameter_tuning_allowed",
    "frozen_before_run",
)
_SELECTION_AUTH_FIELDS = (
    "authorization_id",
    "authority_record_id",
    "exact_purpose",
    "authorized_source_ids",
    "quarantine_disposition",
    "provenance_validation_status",
    "frozen_before_run",
)
_SELECTION_MODES = frozenset(
    {
        "FIXED_PRE_REGISTERED_CHECKPOINT",
        "SEPARATELY_AUTHORIZED_NON_QUARANTINED_SELECTION",
    }
)
_PROHIBITED_RANKING_SOURCE_CLASSES = frozenset(
    {"ABORT_SENTINEL", "PROTECTED_EVALUATION"}
)

_ENVIRONMENT_REQUIRED_FIELDS = (
    "environment_id",
    "os_or_container_identity",
    "python_identity",
    "framework_identity",
    "training_backend_identity",
    "device_runtime_identity",
    "device_identity",
    "driver_identity",
    "attention_kernel_identity",
    "precision_identity",
    "dependency_lock_identity",
    "seed_policy",
    "deterministic_mode",
    "known_nondeterminism",
)
_ENVIRONMENT_OPTIONAL_FIELDS = ("compiler_flags_identity",)

_CHECKPOINT_REQUIRED_FIELDS = (
    "checkpoint_manifest_id",
    "model_or_adapter_state_identity",
    "optimizer_state_identity",
    "scheduler_state_identity",
    "rng_state_identity",
    "data_position_identity",
    "global_step",
    "training_config_id",
    "base_checkpoint_binding_id",
    "dataset_snapshot_id",
    "rendering_policy_id",
    "environment_manifest_id",
)
_CHECKPOINT_OPTIONAL_FIELDS = ("scaler_state_identity",)
_RESUME_STATE_FIELDS = (
    "optimizer_state_identity",
    "scheduler_state_identity",
    "rng_state_identity",
    "data_position_identity",
)

_EVAL_BINDING_FIELDS = (
    "binding_id",
    "metric_catalog_identity",
    "hard_gate_identity",
    "statistical_protocol_identity",
    "stratification_identity",
    "sample_size_rationale_identity",
    "acceptance_threshold_identity",
    "quarantine_matrix_identity",
    "evaluation_asset_manifests",
    "frozen_before_training_authorization",
)
_EVAL_ASSET_FIELDS = (
    "asset_id",
    "asset_role",
    "source_authority_id",
    "source_license_id",
    "content_sha256",
    "split_id",
    "contamination_status",
    "source_verification_status",
    "review_state",
    "provenance_validation_status",
)
_EVAL_ASSET_ROLES = frozenset(
    {
        "METRIC_INPUT",
        "REPLAY_FIXTURE",
        "THRESHOLD_ASSET",
        "STRATIFICATION_ASSET",
        "SAMPLE_SIZE_EVIDENCE",
        "OTHER_PROTOCOL_ASSET",
    }
)

_RECIPE_FIELDS = (
    "evidence_id",
    "evidence_classes",
    "contains_execution_derived_evidence",
    "model_weights_loaded",
    "gradient_work_performed",
    "benchmark_payload_executed",
)
_STATIC_RECIPE_EVIDENCE_CLASSES = frozenset(
    {
        "SCHEMA_COMPLETENESS",
        "DOCUMENTED_COMPATIBILITY",
        "STATIC_RESOURCE_ESTIMATE",
        "RENDERING_CONFORMANCE_DEFINITION",
        "LOSS_MASK_CONFORMANCE_DEFINITION",
        "PACKING_TRUNCATION_CONFORMANCE_DEFINITION",
        "PROVENANCE_QUARANTINE_BINDING",
        "ENVIRONMENT_IDENTITY",
        "ARTIFACT_EXPORT_REQUIREMENT",
        "LICENSE_POSTURE",
    }
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_unique_nonempty_strings(value: Any, field: str, *, allow_empty: bool) -> list[str]:
    if not isinstance(value, list):
        return [f"{field}: expected list"]
    errors: list[str] = []
    if not allow_empty and not value:
        errors.append(f"{field}: must be non-empty")
    if any(not _nonempty(item) for item in value):
        errors.append(f"{field}: entries must be non-empty strings")
    if len(value) != len(set(item for item in value if isinstance(item, str))):
        errors.append(f"{field}: entries must be unique")
    return errors


def _validate_selection_authorization(value: Any) -> list[str]:
    prefix = "CheckpointSelectionPolicy.selection_source_purpose_authorization"
    errors = validate_closed_object(value, required_fields=_SELECTION_AUTH_FIELDS, field=prefix)
    if errors or not isinstance(value, dict):
        return errors
    for field in ("authorization_id", "authority_record_id"):
        if not _nonempty(value.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    if value.get("exact_purpose") != "SFT_CHECKPOINT_SELECTION":
        errors.append(f"{prefix}: exact_purpose must equal 'SFT_CHECKPOINT_SELECTION'")
    errors.extend(
        _validate_unique_nonempty_strings(
            value.get("authorized_source_ids"),
            f"{prefix}.authorized_source_ids",
            allow_empty=False,
        )
    )
    if value.get("quarantine_disposition") != "VERIFIED_NON_QUARANTINED_FOR_SFT_CHECKPOINT_SELECTION":
        errors.append(
            f"{prefix}: quarantine_disposition must equal "
            "'VERIFIED_NON_QUARANTINED_FOR_SFT_CHECKPOINT_SELECTION'"
        )
    if value.get("provenance_validation_status") != "PASS":
        errors.append(f"{prefix}: provenance_validation_status must equal 'PASS'")
    if value.get("frozen_before_run") is not True:
        errors.append(f"{prefix}: frozen_before_run must be true")
    return errors


def validate_checkpoint_selection_policy(policy: Any) -> list[str]:
    """Validate pre-registered checkpoint selection without granting selection authority."""
    prefix = "CheckpointSelectionPolicy"
    errors = validate_closed_object(policy, required_fields=_SELECTION_FIELDS, field=prefix)
    if errors or not isinstance(policy, dict):
        return errors

    for field in ("policy_id", "checkpoint_rule"):
        if not _nonempty(policy.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    mode = policy.get("selection_mode")
    if mode not in _SELECTION_MODES:
        errors.append(f"{prefix}: unsupported selection_mode")

    errors.extend(
        _validate_unique_nonempty_strings(
            policy.get("selection_source_ids"),
            f"{prefix}.selection_source_ids",
            allow_empty=True,
        )
    )

    for field in ("abort_sentinel_can_rank", "recipe_tuning_allowed", "hyperparameter_tuning_allowed"):
        if policy.get(field) is not False:
            errors.append(f"{prefix}: {field} must be false")
    if policy.get("frozen_before_run") is not True:
        errors.append(f"{prefix}: frozen_before_run must be true")

    source_ids = policy.get("selection_source_ids")
    authorization = policy.get("selection_source_purpose_authorization")

    if mode == "FIXED_PRE_REGISTERED_CHECKPOINT":
        if source_ids != []:
            errors.append(
                f"{prefix}: FIXED_PRE_REGISTERED_CHECKPOINT requires selection_source_ids=[]"
            )
        if authorization is not None:
            errors.append(
                f"{prefix}: FIXED_PRE_REGISTERED_CHECKPOINT requires null source-purpose authorization"
            )
        if policy.get("evaluation_asset_ranking_allowed") is not False:
            errors.append(
                f"{prefix}: FIXED_PRE_REGISTERED_CHECKPOINT forbids evaluation-asset ranking"
            )

    if mode == "SEPARATELY_AUTHORIZED_NON_QUARANTINED_SELECTION":
        if not isinstance(source_ids, list) or not source_ids:
            errors.append(
                f"{prefix}: separately authorized selection requires non-empty selection_source_ids"
            )
        if not isinstance(authorization, dict):
            errors.append(
                f"{prefix}: separately authorized selection requires structured source-purpose authorization"
            )
        else:
            errors.extend(_validate_selection_authorization(authorization))
            authorized = authorization.get("authorized_source_ids")
            if isinstance(source_ids, list) and isinstance(authorized, list):
                if set(source_ids) != set(authorized) or len(source_ids) != len(authorized):
                    errors.append(
                        f"{prefix}: selection source set must exactly match authorization source set"
                    )
        if policy.get("evaluation_asset_ranking_allowed") is not True:
            errors.append(
                f"{prefix}: separately authorized selection requires evaluation_asset_ranking_allowed=true"
            )

    return errors


def validate_checkpoint_ranking_inputs(policy: Any, source_records: Any) -> dict[str, Any]:
    """Fail closed unless exact, canonical, non-protected ranking sources are authorized."""
    policy_errors = validate_checkpoint_selection_policy(policy)
    if policy_errors:
        return {
            "allowed": False,
            "reason_code": "INVALID_CHECKPOINT_SELECTION_POLICY",
            "validation_errors": policy_errors,
        }
    if not isinstance(source_records, list):
        return {
            "allowed": False,
            "reason_code": "INVALID_RANKING_SOURCE_RECORDS",
            "validation_errors": ["ranking sources: expected list"],
        }
    if not source_records:
        return {"allowed": True, "reason_code": "NO_RANKING_INPUTS", "validation_errors": []}

    source_ids: list[str] = []
    validated_records: list[dict[str, str]] = []
    record_errors: list[str] = []
    for index, record in enumerate(source_records):
        prefix = f"ranking_sources[{index}]"
        errors = validate_closed_object(
            record,
            required_fields=("source_id", "source_class"),
            field=prefix,
        )
        record_errors.extend(errors)
        if not isinstance(record, dict):
            continue
        source_id = record.get("source_id")
        source_class = record.get("source_class")
        if not _nonempty(source_id):
            record_errors.append(f"{prefix}: source_id must be a non-empty string")
        if not _nonempty(source_class):
            record_errors.append(f"{prefix}: source_class must be a non-empty string")
        if _nonempty(source_id) and _nonempty(source_class):
            source_ids.append(source_id)
            validated_records.append(
                {"source_id": source_id, "source_class": source_class}
            )
    if record_errors:
        return {
            "allowed": False,
            "reason_code": "INVALID_RANKING_SOURCE_RECORDS",
            "validation_errors": record_errors,
        }
    if len(source_ids) != len(set(source_ids)):
        return {
            "allowed": False,
            "reason_code": "RANKING_SOURCE_IDENTITY_DUPLICATE",
            "validation_errors": [],
        }

    if policy["selection_mode"] != "SEPARATELY_AUTHORIZED_NON_QUARANTINED_SELECTION":
        return {
            "allowed": False,
            "reason_code": "RANKING_SOURCE_NOT_AUTHORIZED",
            "validation_errors": [],
        }
    configured = policy["selection_source_ids"]
    if set(source_ids) != set(configured) or len(source_ids) != len(configured):
        return {
            "allowed": False,
            "reason_code": "RANKING_SOURCE_SET_MISMATCH",
            "validation_errors": [],
        }

    if any(
        record["source_class"] in _PROHIBITED_RANKING_SOURCE_CLASSES
        for record in validated_records
    ):
        return {
            "allowed": False,
            "reason_code": "RANKING_SOURCE_CLASS_PROHIBITED",
            "validation_errors": [],
        }

    for record in validated_records:
        quarantine = evaluate_quarantine_source(
            record["source_id"], "CHECKPOINT_SELECTION"
        )
        if not quarantine["allowed"] or not quarantine["can_select_model"]:
            return {
                "allowed": False,
                "reason_code": "RANKING_SOURCE_QUARANTINED",
                "validation_errors": [],
            }

    return {
        "allowed": True,
        "reason_code": "SEPARATELY_AUTHORIZED_RANKING_INPUTS",
        "validation_errors": [],
    }


def validate_environment_manifest(manifest: Any) -> list[str]:
    """Validate a pinned environment identity without authorizing device use."""
    prefix = "EnvironmentManifest"
    errors = validate_closed_object(
        manifest,
        required_fields=_ENVIRONMENT_REQUIRED_FIELDS,
        optional_fields=_ENVIRONMENT_OPTIONAL_FIELDS,
        field=prefix,
    )
    if errors or not isinstance(manifest, dict):
        return errors
    for field in _ENVIRONMENT_REQUIRED_FIELDS:
        if field == "known_nondeterminism":
            continue
        if not _nonempty(manifest.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    compiler_flags = manifest.get("compiler_flags_identity")
    if compiler_flags is not None and not _nonempty(compiler_flags):
        errors.append(f"{prefix}: compiler_flags_identity must be non-empty string or null")
    nondeterminism = manifest.get("known_nondeterminism")
    if not isinstance(nondeterminism, list):
        errors.append(f"{prefix}: known_nondeterminism must be a list")
    else:
        if any(not _nonempty(item) for item in nondeterminism):
            errors.append(f"{prefix}: known_nondeterminism entries must be non-empty strings")
        if len(nondeterminism) != len(set(item for item in nondeterminism if isinstance(item, str))):
            errors.append(f"{prefix}: known_nondeterminism entries must be unique")
    return errors


def classify_training_checkpoint_artifact(record: Any) -> dict[str, Any]:
    """Classify a static artifact as resumable only when all resume state exists."""
    if not isinstance(record, dict):
        return {
            "artifact_class": "INVALID_ARTIFACT",
            "missing_resume_state": list(_RESUME_STATE_FIELDS),
        }
    missing = [field for field in _RESUME_STATE_FIELDS if not _nonempty(record.get(field))]
    return {
        "artifact_class": (
            "RESUMABLE_TRAINING_CHECKPOINT" if not missing else "EXPORT_NOT_RESUMABLE"
        ),
        "missing_resume_state": missing,
    }


def validate_training_checkpoint_manifest(manifest: Any) -> list[str]:
    """Validate full resumable checkpoint state; exports fail this manifest contract."""
    prefix = "TrainingCheckpointManifest"
    errors = validate_closed_object(
        manifest,
        required_fields=_CHECKPOINT_REQUIRED_FIELDS,
        optional_fields=_CHECKPOINT_OPTIONAL_FIELDS,
        field=prefix,
    )
    if errors or not isinstance(manifest, dict):
        return errors
    for field in _CHECKPOINT_REQUIRED_FIELDS:
        if field == "global_step":
            continue
        if not _nonempty(manifest.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    scaler = manifest.get("scaler_state_identity")
    if scaler is not None and not _nonempty(scaler):
        errors.append(f"{prefix}: scaler_state_identity must be non-empty string or null")
    step = manifest.get("global_step")
    if type(step) is not int or step < 0:
        errors.append(f"{prefix}: global_step must be a non-negative integer")
    classification = classify_training_checkpoint_artifact(manifest)
    if classification["artifact_class"] != "RESUMABLE_TRAINING_CHECKPOINT":
        errors.append(
            f"{prefix}: missing resumable state {classification['missing_resume_state']}; "
            "artifact is export-only"
        )
    return errors


def validate_frozen_evaluation_protocol_binding(binding: Any) -> list[str]:
    """Validate a frozen protocol whose every consumed asset is provenance-complete."""
    prefix = "FrozenEvaluationProtocolBinding"
    errors = validate_closed_object(binding, required_fields=_EVAL_BINDING_FIELDS, field=prefix)
    if errors or not isinstance(binding, dict):
        return errors
    for field in _EVAL_BINDING_FIELDS:
        if field in ("evaluation_asset_manifests", "frozen_before_training_authorization"):
            continue
        if not _nonempty(binding.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    assets = binding.get("evaluation_asset_manifests")
    if not isinstance(assets, list) or not assets:
        errors.append(f"{prefix}: evaluation_asset_manifests must be a non-empty list")
    else:
        asset_ids: list[str] = []
        for index, asset in enumerate(assets):
            asset_prefix = f"{prefix}.evaluation_asset_manifests[{index}]"
            asset_errors = validate_closed_object(
                asset,
                required_fields=_EVAL_ASSET_FIELDS,
                field=asset_prefix,
            )
            errors.extend(asset_errors)
            if asset_errors or not isinstance(asset, dict):
                continue
            for field in _EVAL_ASSET_FIELDS:
                if field in ("content_sha256", "asset_role", "provenance_validation_status"):
                    continue
                if not _nonempty(asset.get(field)):
                    errors.append(f"{asset_prefix}: '{field}' must be a non-empty string")
            if _nonempty(asset.get("asset_id")):
                asset_ids.append(asset["asset_id"])
            if asset.get("asset_role") not in _EVAL_ASSET_ROLES:
                errors.append(f"{asset_prefix}: unsupported asset_role")
            errors.extend(
                validate_canonical_sha256(asset.get("content_sha256"), f"{asset_prefix}.content_sha256")
            )
            if asset.get("provenance_validation_status") != "PASS":
                errors.append(f"{asset_prefix}: provenance_validation_status must equal 'PASS'")
        if len(asset_ids) != len(set(asset_ids)):
            errors.append(f"{prefix}: evaluation asset_id values must be unique")

    if binding.get("frozen_before_training_authorization") is not True:
        errors.append(f"{prefix}: frozen_before_training_authorization must be true")
    return errors


def validate_non_executing_recipe_evidence(evidence: Any) -> list[str]:
    """Admit static recipe evidence only; any execution-derived signal fails closed."""
    prefix = "NonExecutingRecipeEvidence"
    errors = validate_closed_object(evidence, required_fields=_RECIPE_FIELDS, field=prefix)
    if errors or not isinstance(evidence, dict):
        return errors
    if not _nonempty(evidence.get("evidence_id")):
        errors.append(f"{prefix}: evidence_id must be a non-empty string")

    classes = evidence.get("evidence_classes")
    if not isinstance(classes, list) or not classes:
        errors.append(f"{prefix}: evidence_classes must be a non-empty list")
    else:
        if len(classes) != len(set(item for item in classes if isinstance(item, str))):
            errors.append(f"{prefix}: evidence_classes must be unique")
        invalid = [
            item
            for item in classes
            if not isinstance(item, str) or item not in _STATIC_RECIPE_EVIDENCE_CLASSES
        ]
        if invalid:
            rendered_invalid = sorted(
                item if isinstance(item, str) else repr(item) for item in invalid
            )
            errors.append(
                f"{prefix}: evidence_classes contain forbidden or unknown values {rendered_invalid}"
            )

    for field in (
        "contains_execution_derived_evidence",
        "model_weights_loaded",
        "gradient_work_performed",
        "benchmark_payload_executed",
    ):
        if evidence.get(field) is not False:
            errors.append(f"{prefix}: {field} must be false")
    return errors