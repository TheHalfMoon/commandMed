"""RED-first tests for Spec 007 selection, reproducibility, and resume contracts."""

from __future__ import annotations

from copy import deepcopy

import pytest

from src.commandmed.spec007.selection import (
    classify_training_checkpoint_artifact,
    validate_checkpoint_ranking_inputs,
    validate_checkpoint_selection_policy,
    validate_environment_manifest,
    validate_frozen_evaluation_protocol_binding,
    validate_non_executing_recipe_evidence,
    validate_training_checkpoint_manifest,
)


def fixed_policy() -> dict[str, object]:
    return {
        "policy_id": "checkpoint-policy:v1",
        "selection_mode": "FIXED_PRE_REGISTERED_CHECKPOINT",
        "checkpoint_rule": "USE_CHECKPOINT_STEP_1000",
        "selection_source_ids": [],
        "selection_source_purpose_authorization": None,
        "evaluation_asset_ranking_allowed": False,
        "abort_sentinel_can_rank": False,
        "recipe_tuning_allowed": False,
        "hyperparameter_tuning_allowed": False,
        "frozen_before_run": True,
    }


def separately_authorized_policy() -> dict[str, object]:
    return {
        "policy_id": "checkpoint-policy:authorized:v1",
        "selection_mode": "SEPARATELY_AUTHORIZED_NON_QUARANTINED_SELECTION",
        "checkpoint_rule": "MAXIMIZE_PRE_REGISTERED_DEV_METRIC",
        "selection_source_ids": ["eval:dev-safe"],
        "selection_source_purpose_authorization": {
            "authorization_id": "auth:sft-checkpoint-selection:v1",
            "authority_record_id": "authority:founder:v1",
            "exact_purpose": "SFT_CHECKPOINT_SELECTION",
            "authorized_source_ids": ["eval:dev-safe"],
            "quarantine_disposition": "VERIFIED_NON_QUARANTINED_FOR_SFT_CHECKPOINT_SELECTION",
            "provenance_validation_status": "PASS",
            "frozen_before_run": True,
        },
        "evaluation_asset_ranking_allowed": True,
        "abort_sentinel_can_rank": False,
        "recipe_tuning_allowed": False,
        "hyperparameter_tuning_allowed": False,
        "frozen_before_run": True,
    }


def environment_manifest() -> dict[str, object]:
    return {
        "environment_id": "env:synthetic:v1",
        "os_or_container_identity": "container:sha256:synthetic",
        "python_identity": "python:3.11",
        "framework_identity": "framework:NEEDS_EVIDENCE",
        "training_backend_identity": "backend:NEEDS_EVIDENCE",
        "device_runtime_identity": "runtime:NEEDS_EVIDENCE",
        "device_identity": "device:NEEDS_EVIDENCE",
        "driver_identity": "driver:NEEDS_EVIDENCE",
        "attention_kernel_identity": "attention:NEEDS_EVIDENCE",
        "precision_identity": "precision:NEEDS_EVIDENCE",
        "compiler_flags_identity": None,
        "dependency_lock_identity": "lock:synthetic:v1",
        "seed_policy": "FIXED_SEED",
        "deterministic_mode": "BEST_EFFORT_DECLARED",
        "known_nondeterminism": ["DEVICE_RUNTIME_NOT_EXECUTED"],
    }


def checkpoint_manifest() -> dict[str, object]:
    return {
        "checkpoint_manifest_id": "checkpoint:synthetic:v1",
        "model_or_adapter_state_identity": "state:model:synthetic",
        "optimizer_state_identity": "state:optimizer:synthetic",
        "scheduler_state_identity": "state:scheduler:synthetic",
        "scaler_state_identity": None,
        "rng_state_identity": "state:rng:synthetic",
        "data_position_identity": "state:data-position:synthetic",
        "global_step": 1000,
        "training_config_id": "config:synthetic:v1",
        "base_checkpoint_binding_id": "base:synthetic:v1",
        "dataset_snapshot_id": "dataset:synthetic:v1",
        "rendering_policy_id": "render:synthetic:v1",
        "environment_manifest_id": "env:synthetic:v1",
    }


def evaluation_binding() -> dict[str, object]:
    return {
        "binding_id": "eval-binding:synthetic:v1",
        "metric_catalog_identity": "metric-catalog:v1",
        "hard_gate_identity": "hard-gates:v1",
        "statistical_protocol_identity": "stats:v1",
        "stratification_identity": "strata:v1",
        "sample_size_rationale_identity": "sample-size:v1",
        "acceptance_threshold_identity": "thresholds:v1",
        "quarantine_matrix_identity": "quarantine:canonical:v1",
        "evaluation_asset_manifests": [
            {
                "asset_id": "asset:metric:synthetic:v1",
                "asset_role": "METRIC_INPUT",
                "source_authority_id": "authority:synthetic:v1",
                "source_license_id": "license:synthetic:v1",
                "content_sha256": "a" * 64,
                "split_id": "split:dev:synthetic:v1",
                "contamination_status": "NOT_ASSESSED",
                "source_verification_status": "VERIFIED",
                "review_state": "APPROVED_SYNTHETIC_FIXTURE",
                "provenance_validation_status": "PASS",
            },
            {
                "asset_id": "asset:threshold:synthetic:v1",
                "asset_role": "THRESHOLD_ASSET",
                "source_authority_id": "authority:synthetic:v1",
                "source_license_id": "license:synthetic:v1",
                "content_sha256": "b" * 64,
                "split_id": "split:protocol:synthetic:v1",
                "contamination_status": "NOT_APPLICABLE",
                "source_verification_status": "VERIFIED",
                "review_state": "APPROVED_SYNTHETIC_FIXTURE",
                "provenance_validation_status": "PASS",
            },
        ],
        "frozen_before_training_authorization": True,
    }


def recipe_evidence() -> dict[str, object]:
    return {
        "evidence_id": "recipe-evidence:synthetic:v1",
        "evidence_classes": [
            "SCHEMA_COMPLETENESS",
            "DOCUMENTED_COMPATIBILITY",
            "PROVENANCE_QUARANTINE_BINDING",
        ],
        "contains_execution_derived_evidence": False,
        "model_weights_loaded": False,
        "gradient_work_performed": False,
        "benchmark_payload_executed": False,
    }


def test_fixed_checkpoint_selection_policy_is_default_fail_closed_mode() -> None:
    assert validate_checkpoint_selection_policy(fixed_policy()) == []


def test_fixed_policy_rejects_any_ranking_source_or_authorization() -> None:
    policy = fixed_policy()
    policy["selection_source_ids"] = ["eval:dev-safe"]
    policy["selection_source_purpose_authorization"] = separately_authorized_policy()[
        "selection_source_purpose_authorization"
    ]
    errors = validate_checkpoint_selection_policy(policy)
    assert errors
    assert any("FIXED_PRE_REGISTERED_CHECKPOINT" in error for error in errors)


def test_separately_authorized_selection_requires_exact_source_set_equality() -> None:
    policy = separately_authorized_policy()
    policy["selection_source_ids"] = ["eval:different"]
    errors = validate_checkpoint_selection_policy(policy)
    assert any("source set" in error.lower() for error in errors)


def test_separately_authorized_selection_rejects_wrong_purpose_and_quarantine() -> None:
    policy = separately_authorized_policy()
    authorization = policy["selection_source_purpose_authorization"]
    assert isinstance(authorization, dict)
    authorization["exact_purpose"] = "PUBLIC_EXTERNAL_EVAL"
    authorization["quarantine_disposition"] = "UNVERIFIED"
    errors = validate_checkpoint_selection_policy(policy)
    assert any("SFT_CHECKPOINT_SELECTION" in error for error in errors)
    assert any("VERIFIED_NON_QUARANTINED" in error for error in errors)


@pytest.mark.parametrize(
    "source_class",
    ["PROTECTED_EVALUATION", "LLM_JUDGE", "HUMAN_INSPECTION", "ABORT_SENTINEL"],
)
def test_protected_ranking_inputs_fail_without_separate_authority(source_class: str) -> None:
    policy = fixed_policy()
    source_records = [
        {
            "source_id": f"source:{source_class.lower()}",
            "source_class": source_class,
        }
    ]
    decision = validate_checkpoint_ranking_inputs(policy, source_records)
    assert decision["allowed"] is False
    assert decision["reason_code"] == "RANKING_SOURCE_NOT_AUTHORIZED"


@pytest.mark.parametrize(
    "source_class",
    ["PROTECTED_EVALUATION", "LLM_JUDGE", "HUMAN_INSPECTION", "ABORT_SENTINEL"],
)
def test_protected_ranking_input_requires_exact_authorized_source_identity(source_class: str) -> None:
    policy = separately_authorized_policy()
    policy["selection_source_ids"] = ["source:protected"]
    authorization = policy["selection_source_purpose_authorization"]
    assert isinstance(authorization, dict)
    authorization["authorized_source_ids"] = ["source:protected"]
    decision = validate_checkpoint_ranking_inputs(
        policy,
        [{"source_id": "source:protected", "source_class": source_class}],
    )
    assert decision["allowed"] is True
    assert decision["reason_code"] == "SEPARATELY_AUTHORIZED_RANKING_INPUTS"


def test_environment_manifest_is_closed_and_requires_explicit_nondeterminism() -> None:
    manifest = environment_manifest()
    assert validate_environment_manifest(manifest) == []

    wrong_nondeterminism = deepcopy(manifest)
    wrong_nondeterminism["known_nondeterminism"] = "NONE"
    errors = validate_environment_manifest(wrong_nondeterminism)
    assert any("known_nondeterminism" in error for error in errors)

    undeclared = deepcopy(manifest)
    undeclared["undeclared"] = True
    errors = validate_environment_manifest(undeclared)
    assert any("undeclared" in error for error in errors)


def test_training_checkpoint_manifest_is_resumable_only_with_full_state() -> None:
    manifest = checkpoint_manifest()
    assert validate_training_checkpoint_manifest(manifest) == []
    classification = classify_training_checkpoint_artifact(manifest)
    assert classification == {
        "artifact_class": "RESUMABLE_TRAINING_CHECKPOINT",
        "missing_resume_state": [],
    }


def test_export_is_not_mislabeled_as_resumable_checkpoint() -> None:
    export = checkpoint_manifest()
    del export["optimizer_state_identity"]
    del export["rng_state_identity"]
    classification = classify_training_checkpoint_artifact(export)
    assert classification["artifact_class"] == "EXPORT_NOT_RESUMABLE"
    assert classification["missing_resume_state"] == [
        "optimizer_state_identity",
        "rng_state_identity",
    ]
    errors = validate_training_checkpoint_manifest(export)
    assert errors


def test_frozen_evaluation_binding_requires_complete_provenance_for_every_asset() -> None:
    binding = evaluation_binding()
    assert validate_frozen_evaluation_protocol_binding(binding) == []
    bad = deepcopy(binding)
    del bad["evaluation_asset_manifests"][1]["source_license_id"]
    bad["evaluation_asset_manifests"][0]["provenance_validation_status"] = "PENDING"
    errors = validate_frozen_evaluation_protocol_binding(bad)
    assert any("source_license_id" in error for error in errors)
    assert any("provenance_validation_status" in error for error in errors)


def test_frozen_evaluation_binding_rejects_duplicate_asset_ids_and_bad_hash() -> None:
    binding = evaluation_binding()
    binding["evaluation_asset_manifests"][1]["asset_id"] = binding[
        "evaluation_asset_manifests"
    ][0]["asset_id"]
    binding["evaluation_asset_manifests"][0]["content_sha256"] = "BAD"
    errors = validate_frozen_evaluation_protocol_binding(binding)
    assert any("asset_id" in error and "unique" in error for error in errors)
    assert any("content_sha256" in error for error in errors)


def test_frozen_evaluation_binding_must_precede_training_authorization() -> None:
    binding = evaluation_binding()
    binding["frozen_before_training_authorization"] = False
    errors = validate_frozen_evaluation_protocol_binding(binding)
    assert any("frozen_before_training_authorization" in error for error in errors)


@pytest.mark.parametrize(
    "field",
    [
        "contains_execution_derived_evidence",
        "model_weights_loaded",
        "gradient_work_performed",
        "benchmark_payload_executed",
    ],
)
def test_non_executing_recipe_evidence_rejects_execution_derived_signals(field: str) -> None:
    evidence = recipe_evidence()
    evidence[field] = True
    errors = validate_non_executing_recipe_evidence(evidence)
    assert any(field in error for error in errors)


def test_non_executing_recipe_evidence_rejects_empirical_training_classes() -> None:
    evidence = recipe_evidence()
    evidence["evidence_classes"] = ["LOSS_CURVE"]
    errors = validate_non_executing_recipe_evidence(evidence)
    assert any("evidence_classes" in error for error in errors)


def test_non_executing_recipe_evidence_accepts_static_classes_only() -> None:
    assert validate_non_executing_recipe_evidence(recipe_evidence()) == []
