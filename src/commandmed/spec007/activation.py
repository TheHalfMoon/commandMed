"""Final offline Spec 007 activation control-plane validators.

This module composes and validates planning records and produces preflight
decisions only. It deliberately contains no model loader, device opener,
credential handler, network client, optimizer, or training entry point.
"""

from __future__ import annotations

import re
from typing import Any, Mapping

from src.commandmed.spec007.foundation import validate_closed_object
from src.commandmed.spec007.snapshot import validate_dataset_snapshot

_TRAINING_REQUIRED_FIELDS = (
    "config_id",
    "base_checkpoint_binding_id",
    "dataset_snapshot_id",
    "rendering_policy_id",
    "loss_mask_policy_id",
    "packing_truncation_policy_id",
    "update_strategy",
    "precision_policy",
    "sequence_length",
    "role_mix_policy",
    "optimizer_class",
    "scheduler_class",
    "learning_rate_record",
    "effective_batch_semantics",
    "token_budget",
    "gradient_accumulation",
    "clipping_policy",
    "checkpoint_schedule",
    "seed",
    "data_seed",
    "deterministic_mode",
    "backend_id",
    "environment_manifest_id",
)
_TRAINING_OPTIONAL_FIELDS = ("epoch_or_step_budget",)
_UPDATE_STRATEGIES = frozenset({"FULL", "LORA", "QLORA", "NEEDS_EVIDENCE"})
_PLANNING_UNRESOLVED_FIELDS = (
    "update_strategy",
    "sequence_length",
    "token_budget",
    "gradient_accumulation",
    "seed",
    "data_seed",
)

_BACKEND_FIELDS = (
    "backend_candidate_id",
    "software_identity",
    "architecture_support_evidence",
    "rendering_fidelity_evidence",
    "loss_mask_support_evidence",
    "packing_truncation_support_evidence",
    "resume_support_evidence",
    "reproducibility_support_evidence",
    "precision_update_strategy_support",
    "network_telemetry_behavior",
    "maintenance_dependency_cost",
    "non_executing_evidence_only",
    "status",
)
_BACKEND_STATUSES = frozenset(
    {"NEEDS_EVIDENCE", "ADMISSIBLE_STATIC_EVIDENCE", "INADMISSIBLE_STATIC_EVIDENCE"}
)

_CANDIDATE_FIELDS = (
    "candidate_id",
    "checkpoint_identity",
    "license_evidence_id",
    "parameter_accounting",
    "package_accounting",
    "medical_quality_evidence",
    "patient_conversation_evidence",
    "abstention_evidence",
    "arabic_english_evidence",
    "tool_use_evidence",
    "general_capability_evidence",
    "training_tooling_evidence",
    "resource_evidence",
    "runtime_compatibility_evidence",
    "known_limitations",
    "qualification_reason_codes",
    "pi_recommendation",
)
_CANDIDATE_OBJECT_FIELDS = (
    "parameter_accounting",
    "package_accounting",
    "medical_quality_evidence",
    "patient_conversation_evidence",
    "abstention_evidence",
    "arabic_english_evidence",
    "tool_use_evidence",
    "general_capability_evidence",
    "training_tooling_evidence",
    "resource_evidence",
    "runtime_compatibility_evidence",
)

_BASE_REQUIRED_FIELDS = (
    "binding_id",
    "winner_decision_record_id",
    "model_repository_id",
    "model_revision",
    "checkpoint_identity",
    "weight_content_identity",
    "total_parameter_count",
    "reference_precision_bytes",
    "tokenizer_identity",
    "chat_template_identity",
    "special_token_map_identity",
    "license_evidence_id",
    "lineage_evidence_id",
    "tournament_evidence_pack_id",
)
_BASE_OPTIONAL_FIELDS = ("active_parameter_semantics", "resource_evidence_id")

_RUN_FIELDS = (
    "run_manifest_id",
    "base_checkpoint_binding_id",
    "dataset_snapshot_id",
    "prompt_rendering_policy_id",
    "loss_mask_policy_id",
    "packing_truncation_policy_id",
    "training_config_id",
    "checkpoint_selection_policy_id",
    "capability_preservation_binding_id",
    "environment_manifest_id",
    "frozen_evaluation_protocol_binding_id",
    "non_executing_recipe_evidence_id",
    "software_commit",
    "software_tree",
    "access_authorization_ids",
    "finance_requirement_id",
    "finance_authorization_id",
    "training_authorization_id",
)

_REFERENCE_BINDINGS = {
    "base_checkpoint_binding_id": ("base_checkpoint_bindings", "binding_id"),
    "dataset_snapshot_id": ("dataset_snapshots", "snapshot_id"),
    "prompt_rendering_policy_id": ("prompt_rendering_policies", "policy_id"),
    "loss_mask_policy_id": ("loss_mask_policies", "policy_id"),
    "packing_truncation_policy_id": ("packing_truncation_policies", "policy_id"),
    "training_config_id": ("training_configurations", "config_id"),
    "checkpoint_selection_policy_id": ("checkpoint_selection_policies", "policy_id"),
    "capability_preservation_binding_id": ("capability_preservation_bindings", "binding_id"),
    "environment_manifest_id": ("environment_manifests", "environment_id"),
    "frozen_evaluation_protocol_binding_id": (
        "frozen_evaluation_protocol_bindings",
        "binding_id",
    ),
    "non_executing_recipe_evidence_id": (
        "non_executing_recipe_evidence",
        "evidence_id",
    ),
}

_TRAINING_TO_MANIFEST_REFERENCES = {
    "base_checkpoint_binding_id": "base_checkpoint_binding_id",
    "dataset_snapshot_id": "dataset_snapshot_id",
    "rendering_policy_id": "prompt_rendering_policy_id",
    "loss_mask_policy_id": "loss_mask_policy_id",
    "packing_truncation_policy_id": "packing_truncation_policy_id",
    "environment_manifest_id": "environment_manifest_id",
}


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_list(value: Any, field: str, *, unique: bool = False) -> list[str]:
    if not isinstance(value, list):
        return [f"{field}: expected list"]
    errors: list[str] = []
    if any(not _nonempty(item) for item in value):
        errors.append(f"{field}: entries must be non-empty strings")
    if unique and len(value) != len(set(item for item in value if isinstance(item, str))):
        errors.append(f"{field}: entries must be unique")
    return errors


def _is_int(value: Any) -> bool:
    return type(value) is int


def validate_training_configuration(config: Any, *, planning_only: bool = False) -> list[str]:
    """Validate TrainingConfigurationRecord; planning mode forbids invented resolution."""
    prefix = "TrainingConfigurationRecord"
    errors = validate_closed_object(
        config,
        required_fields=_TRAINING_REQUIRED_FIELDS,
        optional_fields=_TRAINING_OPTIONAL_FIELDS,
        field=prefix,
    )
    if not isinstance(config, dict):
        return errors

    string_fields = (
        "config_id",
        "base_checkpoint_binding_id",
        "dataset_snapshot_id",
        "rendering_policy_id",
        "loss_mask_policy_id",
        "packing_truncation_policy_id",
        "precision_policy",
        "role_mix_policy",
        "optimizer_class",
        "scheduler_class",
        "learning_rate_record",
        "effective_batch_semantics",
        "clipping_policy",
        "checkpoint_schedule",
        "deterministic_mode",
        "backend_id",
        "environment_manifest_id",
    )
    for field in string_fields:
        if field in config and not _nonempty(config.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    strategy = config.get("update_strategy")
    if strategy not in _UPDATE_STRATEGIES:
        errors.append(f"{prefix}: unsupported update_strategy")

    for field in ("sequence_length", "token_budget", "gradient_accumulation"):
        if field not in config:
            continue
        value = config.get(field)
        if value != "NEEDS_EVIDENCE" and (not _is_int(value) or value < 1):
            errors.append(f"{prefix}: {field} must be integer >= 1 or 'NEEDS_EVIDENCE'")
    for field in ("seed", "data_seed"):
        if field not in config:
            continue
        value = config.get(field)
        if value != "NEEDS_EVIDENCE" and not _is_int(value):
            errors.append(f"{prefix}: {field} must be integer or 'NEEDS_EVIDENCE'")
    epoch_budget = config.get("epoch_or_step_budget")
    if epoch_budget is not None and not (
        isinstance(epoch_budget, str) or _is_int(epoch_budget)
    ):
        errors.append(f"{prefix}: epoch_or_step_budget must be string or integer")

    if planning_only:
        for field in _PLANNING_UNRESOLVED_FIELDS:
            if config.get(field) != "NEEDS_EVIDENCE":
                errors.append(
                    f"{prefix}: planning-only {field} must remain 'NEEDS_EVIDENCE'"
                )
    return errors


def validate_backend_candidate_evidence(record: Any) -> list[str]:
    """Validate static backend evidence; execution-derived backend evidence is excluded."""
    prefix = "BackendCandidateEvidence"
    errors = validate_closed_object(record, required_fields=_BACKEND_FIELDS, field=prefix)
    if not isinstance(record, dict):
        return errors
    for field in _BACKEND_FIELDS:
        if field in ("non_executing_evidence_only", "status") or field not in record:
            continue
        if not _nonempty(record.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    if record.get("non_executing_evidence_only") is not True:
        errors.append(f"{prefix}: non_executing_evidence_only must be true")
    if record.get("status") not in _BACKEND_STATUSES:
        errors.append(f"{prefix}: unsupported status")
    return errors


def validate_candidate_evidence_record(record: Any) -> list[str]:
    """Validate candidate evidence while forbidding a PI/winner recommendation."""
    prefix = "CandidateEvidenceRecord"
    errors = validate_closed_object(record, required_fields=_CANDIDATE_FIELDS, field=prefix)
    if not isinstance(record, dict):
        return errors
    for field in ("candidate_id", "checkpoint_identity", "license_evidence_id"):
        if field in record and not _nonempty(record.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    for field in _CANDIDATE_OBJECT_FIELDS:
        if field in record and not isinstance(record.get(field), dict):
            errors.append(f"{prefix}: {field} must be an object")
    if "known_limitations" in record:
        errors.extend(_string_list(record.get("known_limitations"), f"{prefix}.known_limitations"))
    if "qualification_reason_codes" in record:
        errors.extend(
            _string_list(
                record.get("qualification_reason_codes"),
                f"{prefix}.qualification_reason_codes",
            )
        )
    if record.get("pi_recommendation") != "NONE":
        errors.append(f"{prefix}: pi_recommendation must equal 'NONE'")
    return errors


def validate_base_checkpoint_binding(record: Any) -> list[str]:
    """Validate a supplied binding structurally; this function never selects a winner."""
    prefix = "BaseCheckpointBinding"
    errors = validate_closed_object(
        record,
        required_fields=_BASE_REQUIRED_FIELDS,
        optional_fields=_BASE_OPTIONAL_FIELDS,
        field=prefix,
    )
    if not isinstance(record, dict):
        return errors
    for field in _BASE_REQUIRED_FIELDS:
        if field in ("total_parameter_count", "reference_precision_bytes") or field not in record:
            continue
        if not _nonempty(record.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    for field in ("total_parameter_count", "reference_precision_bytes"):
        if field in record:
            value = record.get(field)
            if not _is_int(value) or value < 1:
                errors.append(f"{prefix}: {field} must be an integer >= 1")
    for field in _BASE_OPTIONAL_FIELDS:
        if field in record:
            value = record.get(field)
            if value is not None and not _nonempty(value):
                errors.append(f"{prefix}: {field} must be non-empty string or null")
    return errors


def _resolve_reference(
    component_store: Mapping[str, Mapping[str, Mapping[str, Any]]],
    category: str,
    identity_field: str,
    reference_id: Any,
) -> bool:
    if not _nonempty(reference_id):
        return False
    category_store = component_store.get(category)
    if not isinstance(category_store, Mapping):
        return False
    record = category_store.get(reference_id)
    if not isinstance(record, Mapping):
        return False
    return record.get(identity_field) == reference_id


def validate_run_manifest(
    manifest: Any,
    component_store: Mapping[str, Mapping[str, Mapping[str, Any]]],
) -> list[str]:
    """Validate a RunManifest and resolve all static component references."""
    prefix = "RunManifest"
    errors = validate_closed_object(manifest, required_fields=_RUN_FIELDS, field=prefix)
    if not isinstance(manifest, dict):
        return errors

    string_fields = tuple(
        field
        for field in _RUN_FIELDS
        if field not in ("access_authorization_ids", "software_commit", "software_tree")
    )
    for field in string_fields:
        if field in manifest and not _nonempty(manifest.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    for field in ("software_commit", "software_tree"):
        value = manifest.get(field)
        if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{40}", value) is None:
            errors.append(f"{prefix}: {field} must be exactly 40 lowercase hex characters")

    if "access_authorization_ids" in manifest:
        errors.extend(
            _string_list(
                manifest.get("access_authorization_ids"),
                f"{prefix}.access_authorization_ids",
                unique=True,
            )
        )

    for field, (category, identity_field) in _REFERENCE_BINDINGS.items():
        if field not in manifest:
            continue
        if not _resolve_reference(component_store, category, identity_field, manifest.get(field)):
            errors.append(f"{prefix}: {field} unresolved in component store")
    return errors


def _composition_validation_errors(
    *,
    run_manifest: Mapping[str, Any],
    component_store: Mapping[str, Mapping[str, Mapping[str, Any]]],
    backend_evidence: Mapping[str, Any],
    base_checkpoint_binding: Mapping[str, Any],
    training_configuration: Mapping[str, Any],
) -> list[str]:
    """Bind supplied planning records to the exact manifest/store identities."""
    errors: list[str] = []

    manifest_base_id = run_manifest.get("base_checkpoint_binding_id")
    if base_checkpoint_binding.get("binding_id") != manifest_base_id:
        errors.append("composition: supplied base binding does not match RunManifest")
    store_base = _record_from_store(component_store, "base_checkpoint_bindings", manifest_base_id)
    if store_base is None or dict(store_base) != dict(base_checkpoint_binding):
        errors.append("composition: supplied base binding diverges from component store")

    manifest_config_id = run_manifest.get("training_config_id")
    if training_configuration.get("config_id") != manifest_config_id:
        errors.append("composition: supplied training configuration does not match RunManifest")
    store_config = _record_from_store(component_store, "training_configurations", manifest_config_id)
    if store_config is None or dict(store_config) != dict(training_configuration):
        errors.append("composition: supplied training configuration diverges from component store")

    for config_field, manifest_field in _TRAINING_TO_MANIFEST_REFERENCES.items():
        if training_configuration.get(config_field) != run_manifest.get(manifest_field):
            errors.append(
                f"composition: training configuration {config_field} does not match "
                f"RunManifest {manifest_field}"
            )

    if training_configuration.get("backend_id") != backend_evidence.get("backend_candidate_id"):
        errors.append("composition: training backend does not match backend evidence")
    return errors


def compose_non_executing_planning_fixture(
    *,
    run_manifest: Mapping[str, Any],
    component_store: Mapping[str, Mapping[str, Mapping[str, Any]]],
    backend_evidence: Mapping[str, Any],
    candidate_evidence: Mapping[str, Any],
    base_checkpoint_binding: Mapping[str, Any],
    training_configuration: Mapping[str, Any],
) -> dict[str, Any]:
    """Compose a planning-only fixture spanning the final control-plane surfaces."""
    validation = {
        "run_manifest": validate_run_manifest(run_manifest, component_store),
        "backend_candidate_evidence": validate_backend_candidate_evidence(backend_evidence),
        "candidate_evidence": validate_candidate_evidence_record(candidate_evidence),
        "base_checkpoint_binding": validate_base_checkpoint_binding(base_checkpoint_binding),
        "training_configuration": validate_training_configuration(
            training_configuration, planning_only=True
        ),
        "composition": _composition_validation_errors(
            run_manifest=run_manifest,
            component_store=component_store,
            backend_evidence=backend_evidence,
            base_checkpoint_binding=base_checkpoint_binding,
            training_configuration=training_configuration,
        ),
    }
    valid = all(not errors for errors in validation.values())
    return {
        "valid": valid,
        "validation": validation,
        "execution_authorized": False,
        "activation_state": "PLANNING_ONLY" if valid else "INVALID_PLANNING_FIXTURE",
        "winner_selection_performed": False,
    }


def _record_from_store(
    store: Mapping[str, Mapping[str, Mapping[str, Any]]], category: str, identity: Any
) -> Mapping[str, Any] | None:
    category_store = store.get(category)
    if not isinstance(category_store, Mapping) or not _nonempty(identity):
        return None
    record = category_store.get(identity)
    return record if isinstance(record, Mapping) else None


def preflight_run_manifest(
    manifest: Any,
    component_store: Mapping[str, Mapping[str, Mapping[str, Any]]],
    authority_state: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a fail-closed validation decision without loading model/device state."""
    reason_codes: list[str] = []
    manifest_errors = validate_run_manifest(manifest, component_store)
    if manifest_errors:
        reason_codes.append("RUN_MANIFEST_INVALID_OR_UNRESOLVED")

    if isinstance(manifest, dict):
        base = _record_from_store(
            component_store,
            "base_checkpoint_bindings",
            manifest.get("base_checkpoint_binding_id"),
        )
        if base is None:
            reason_codes.append("BASE_CHECKPOINT_BINDING_INVALID")
        else:
            if validate_base_checkpoint_binding(dict(base)):
                reason_codes.append("BASE_CHECKPOINT_BINDING_INVALID")
            if not _nonempty(base.get("weight_content_identity")):
                reason_codes.append("BASE_WEIGHT_IDENTITY_MISSING")

        dataset = _record_from_store(
            component_store,
            "dataset_snapshots",
            manifest.get("dataset_snapshot_id"),
        )
        if dataset is None:
            reason_codes.append("DATASET_SNAPSHOT_INVALID")
            reason_codes.append("DATASET_SNAPSHOT_HASH_MISSING")
        else:
            if validate_dataset_snapshot(dict(dataset)):
                reason_codes.append("DATASET_SNAPSHOT_INVALID")
            if not _nonempty(dataset.get("snapshot_sha256")):
                reason_codes.append("DATASET_SNAPSHOT_HASH_MISSING")

        quarantine_id = dataset.get("quarantine_verification_id") if dataset is not None else None
        quarantine = _record_from_store(
            component_store, "quarantine_verifications", quarantine_id
        )
        if quarantine is None:
            reason_codes.append("QUARANTINE_VERIFICATION_NOT_PASS")
        elif quarantine.get("quarantine_verification_id") != quarantine_id:
            reason_codes.append("QUARANTINE_VERIFICATION_IDENTITY_MISMATCH")
        elif quarantine.get("status") != "PASS":
            reason_codes.append("QUARANTINE_VERIFICATION_NOT_PASS")

        license_id = base.get("license_evidence_id") if base is not None else None
        license_record = _record_from_store(component_store, "license_evidence", license_id)
        if license_record is None:
            reason_codes.append("LICENSE_EVIDENCE_NOT_PASS")
        elif license_record.get("license_evidence_id") != license_id:
            reason_codes.append("LICENSE_EVIDENCE_IDENTITY_MISMATCH")
        elif license_record.get("status") != "PASS":
            reason_codes.append("LICENSE_EVIDENCE_NOT_PASS")

        manifest_training = manifest.get("training_authorization_id")
        current_training = authority_state.get("training_authorization_id")
        if manifest_training == "NONE" or current_training == "NONE":
            reason_codes.append("TRAINING_AUTHORITY_NONE")
        elif manifest_training != current_training:
            reason_codes.append("TRAINING_AUTHORITY_STALE_OR_MISMATCH")

        manifest_finance = manifest.get("finance_authorization_id")
        current_finance = authority_state.get("finance_authorization_id")
        if manifest_finance == "NONE" or current_finance == "NONE":
            reason_codes.append("FINANCE_AUTHORITY_NONE")
        elif manifest_finance != current_finance:
            reason_codes.append("FINANCE_AUTHORITY_STALE_OR_MISMATCH")

        manifest_access = manifest.get("access_authorization_ids")
        current_access = authority_state.get("access_authorization_ids")
        if isinstance(manifest_access, list) and isinstance(current_access, list):
            if set(manifest_access) != set(current_access) or len(manifest_access) != len(current_access):
                reason_codes.append("ACCESS_AUTHORITY_STALE_OR_MISMATCH")
        else:
            reason_codes.append("ACCESS_AUTHORITY_UNRESOLVED")

    if authority_state.get("model_execution_authority") != "AUTHORIZED":
        reason_codes.append("MODEL_EXECUTION_AUTHORITY_NONE")
    if authority_state.get("weight_access_authority") != "AUTHORIZED":
        reason_codes.append("WEIGHT_ACCESS_AUTHORITY_NONE")
    if authority_state.get("device_execution_authority") != "AUTHORIZED":
        reason_codes.append("DEVICE_EXECUTION_AUTHORITY_NONE")

    ordered_reasons = list(dict.fromkeys(reason_codes))
    return {
        "allowed": not ordered_reasons,
        "reason_codes": ordered_reasons,
        "manifest_validation_errors": manifest_errors,
        "model_loaded": False,
        "device_opened": False,
        "training_started": False,
    }