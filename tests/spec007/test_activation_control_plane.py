"""RED-first tests for Spec 007 final offline activation control plane."""

from __future__ import annotations

from copy import deepcopy

import pytest

from src.commandmed.spec007.activation import (
    compose_non_executing_planning_fixture,
    preflight_run_manifest,
    validate_backend_candidate_evidence,
    validate_base_checkpoint_binding,
    validate_candidate_evidence_record,
    validate_run_manifest,
    validate_training_configuration,
)


def training_config() -> dict[str, object]:
    return {
        "config_id": "config:synthetic:v1",
        "base_checkpoint_binding_id": "base:synthetic:v1",
        "dataset_snapshot_id": "dataset:synthetic:v1",
        "rendering_policy_id": "render:synthetic:v1",
        "loss_mask_policy_id": "loss:synthetic:v1",
        "packing_truncation_policy_id": "packing:synthetic:v1",
        "update_strategy": "NEEDS_EVIDENCE",
        "precision_policy": "NEEDS_EVIDENCE",
        "sequence_length": "NEEDS_EVIDENCE",
        "role_mix_policy": "NEEDS_EVIDENCE",
        "optimizer_class": "NEEDS_EVIDENCE",
        "scheduler_class": "NEEDS_EVIDENCE",
        "learning_rate_record": "NEEDS_EVIDENCE",
        "effective_batch_semantics": "NEEDS_EVIDENCE",
        "token_budget": "NEEDS_EVIDENCE",
        "epoch_or_step_budget": "NEEDS_EVIDENCE",
        "gradient_accumulation": "NEEDS_EVIDENCE",
        "clipping_policy": "NEEDS_EVIDENCE",
        "checkpoint_schedule": "NEEDS_EVIDENCE",
        "seed": "NEEDS_EVIDENCE",
        "data_seed": "NEEDS_EVIDENCE",
        "deterministic_mode": "NEEDS_EVIDENCE",
        "backend_id": "backend:synthetic:v1",
        "environment_manifest_id": "env:synthetic:v1",
    }


def backend_evidence() -> dict[str, object]:
    return {
        "backend_candidate_id": "backend:synthetic:v1",
        "software_identity": "software:synthetic:v1",
        "architecture_support_evidence": "NEEDS_EVIDENCE",
        "rendering_fidelity_evidence": "NEEDS_EVIDENCE",
        "loss_mask_support_evidence": "NEEDS_EVIDENCE",
        "packing_truncation_support_evidence": "NEEDS_EVIDENCE",
        "resume_support_evidence": "NEEDS_EVIDENCE",
        "reproducibility_support_evidence": "NEEDS_EVIDENCE",
        "precision_update_strategy_support": "NEEDS_EVIDENCE",
        "network_telemetry_behavior": "NEEDS_EVIDENCE",
        "maintenance_dependency_cost": "NEEDS_EVIDENCE",
        "non_executing_evidence_only": True,
        "status": "NEEDS_EVIDENCE",
    }


def candidate_evidence() -> dict[str, object]:
    return {
        "candidate_id": "candidate:synthetic:v1",
        "checkpoint_identity": "checkpoint:synthetic:v1",
        "license_evidence_id": "license:synthetic:v1",
        "parameter_accounting": {"status": "NEEDS_EVIDENCE"},
        "package_accounting": {"status": "NEEDS_EVIDENCE"},
        "medical_quality_evidence": {"status": "NEEDS_EVIDENCE"},
        "patient_conversation_evidence": {"status": "NEEDS_EVIDENCE"},
        "abstention_evidence": {"status": "NEEDS_EVIDENCE"},
        "arabic_english_evidence": {"status": "NEEDS_EVIDENCE"},
        "tool_use_evidence": {"status": "NEEDS_EVIDENCE"},
        "general_capability_evidence": {"status": "NEEDS_EVIDENCE"},
        "training_tooling_evidence": {"status": "NEEDS_EVIDENCE"},
        "resource_evidence": {"status": "NEEDS_EVIDENCE"},
        "runtime_compatibility_evidence": {"status": "NEEDS_EVIDENCE"},
        "known_limitations": ["SYNTHETIC_FIXTURE_ONLY"],
        "qualification_reason_codes": ["NEEDS_EVIDENCE"],
        "pi_recommendation": "NONE",
    }


def base_binding() -> dict[str, object]:
    return {
        "binding_id": "base:synthetic:v1",
        "winner_decision_record_id": "winner-decision:synthetic-fixture:v1",
        "model_repository_id": "synthetic:repository:not-a-winner",
        "model_revision": "synthetic:revision:not-a-winner",
        "checkpoint_identity": "checkpoint:synthetic:not-a-winner",
        "weight_content_identity": "sha256:" + "a" * 64,
        "total_parameter_count": 100,
        "active_parameter_semantics": None,
        "reference_precision_bytes": 200,
        "tokenizer_identity": "tokenizer:synthetic:v1",
        "chat_template_identity": "template:synthetic:v1",
        "special_token_map_identity": "special-tokens:synthetic:v1",
        "license_evidence_id": "license:synthetic:v1",
        "lineage_evidence_id": "lineage:synthetic:v1",
        "tournament_evidence_pack_id": "tournament:synthetic-fixture:v1",
        "resource_evidence_id": None,
    }


def run_manifest() -> dict[str, object]:
    return {
        "run_manifest_id": "run:synthetic:v1",
        "base_checkpoint_binding_id": "base:synthetic:v1",
        "dataset_snapshot_id": "dataset:synthetic:v1",
        "prompt_rendering_policy_id": "render:synthetic:v1",
        "loss_mask_policy_id": "loss:synthetic:v1",
        "packing_truncation_policy_id": "packing:synthetic:v1",
        "training_config_id": "config:synthetic:v1",
        "checkpoint_selection_policy_id": "checkpoint-policy:synthetic:v1",
        "capability_preservation_binding_id": "capability:synthetic:v1",
        "environment_manifest_id": "env:synthetic:v1",
        "frozen_evaluation_protocol_binding_id": "eval-binding:synthetic:v1",
        "non_executing_recipe_evidence_id": "recipe:synthetic:v1",
        "software_commit": "b" * 40,
        "software_tree": "c" * 40,
        "access_authorization_ids": [],
        "finance_requirement_id": "finance-requirement:synthetic:v1",
        "finance_authorization_id": "NONE",
        "training_authorization_id": "NONE",
    }


def component_store() -> dict[str, dict[str, dict[str, object]]]:
    return {
        "base_checkpoint_bindings": {
            "base:synthetic:v1": base_binding(),
        },
        "dataset_snapshots": {
            "dataset:synthetic:v1": {
                "snapshot_id": "dataset:synthetic:v1",
                "snapshot_sha256": "d" * 64,
                "quarantine_verification_id": "quarantine:synthetic:v1",
            },
        },
        "prompt_rendering_policies": {
            "render:synthetic:v1": {"policy_id": "render:synthetic:v1"},
        },
        "loss_mask_policies": {
            "loss:synthetic:v1": {"policy_id": "loss:synthetic:v1"},
        },
        "packing_truncation_policies": {
            "packing:synthetic:v1": {"policy_id": "packing:synthetic:v1"},
        },
        "training_configurations": {
            "config:synthetic:v1": training_config(),
        },
        "checkpoint_selection_policies": {
            "checkpoint-policy:synthetic:v1": {"policy_id": "checkpoint-policy:synthetic:v1"},
        },
        "capability_preservation_bindings": {
            "capability:synthetic:v1": {"binding_id": "capability:synthetic:v1"},
        },
        "environment_manifests": {
            "env:synthetic:v1": {"environment_id": "env:synthetic:v1"},
        },
        "frozen_evaluation_protocol_bindings": {
            "eval-binding:synthetic:v1": {"binding_id": "eval-binding:synthetic:v1"},
        },
        "non_executing_recipe_evidence": {
            "recipe:synthetic:v1": {"evidence_id": "recipe:synthetic:v1"},
        },
        "license_evidence": {
            "license:synthetic:v1": {"license_evidence_id": "license:synthetic:v1", "status": "PASS"},
        },
        "quarantine_verifications": {
            "quarantine:synthetic:v1": {"quarantine_verification_id": "quarantine:synthetic:v1", "status": "PASS"},
        },
    }


def current_authority_state() -> dict[str, object]:
    return {
        "training_authorization_id": "NONE",
        "finance_authorization_id": "NONE",
        "access_authorization_ids": [],
        "model_execution_authority": "NONE",
        "weight_access_authority": "NONE",
        "device_execution_authority": "NONE",
    }


def test_training_configuration_keeps_unresolved_values_typed() -> None:
    assert validate_training_configuration(training_config(), planning_only=True) == []


@pytest.mark.parametrize(
    ("field", "placeholder"),
    [
        ("update_strategy", "LORA"),
        ("sequence_length", 2048),
        ("token_budget", 1000000),
        ("gradient_accumulation", 8),
        ("seed", 42),
        ("data_seed", 42),
    ],
)
def test_planning_configuration_rejects_premature_placeholder_resolution(
    field: str, placeholder: object
) -> None:
    config = training_config()
    config[field] = placeholder
    errors = validate_training_configuration(config, planning_only=True)
    assert any(field in error and "NEEDS_EVIDENCE" in error for error in errors)


def test_backend_candidate_evidence_is_strictly_non_executing() -> None:
    assert validate_backend_candidate_evidence(backend_evidence()) == []
    bad = backend_evidence()
    bad["non_executing_evidence_only"] = False
    errors = validate_backend_candidate_evidence(bad)
    assert any("non_executing_evidence_only" in error for error in errors)


def test_candidate_evidence_cannot_recommend_a_winner() -> None:
    assert validate_candidate_evidence_record(candidate_evidence()) == []
    bad = candidate_evidence()
    bad["pi_recommendation"] = "SELECT"
    errors = validate_candidate_evidence_record(bad)
    assert any("pi_recommendation" in error for error in errors)


def test_synthetic_base_binding_validates_without_becoming_actual_winner() -> None:
    assert validate_base_checkpoint_binding(base_binding()) == []


def test_base_binding_requires_positive_parameter_and_precision_accounting() -> None:
    bad = base_binding()
    bad["total_parameter_count"] = 0
    bad["reference_precision_bytes"] = True
    errors = validate_base_checkpoint_binding(bad)
    assert any("total_parameter_count" in error for error in errors)
    assert any("reference_precision_bytes" in error for error in errors)


def test_run_manifest_requires_resolvable_component_references() -> None:
    assert validate_run_manifest(run_manifest(), component_store()) == []
    store = component_store()
    del store["loss_mask_policies"]["loss:synthetic:v1"]
    errors = validate_run_manifest(run_manifest(), store)
    assert any("loss_mask_policy_id" in error and "unresolved" in error for error in errors)


def test_run_manifest_rejects_credentials_and_bad_software_hashes() -> None:
    manifest = run_manifest()
    manifest["credential"] = "forbidden"
    manifest["software_commit"] = "BAD"
    errors = validate_run_manifest(manifest, component_store())
    assert any("credential" in error for error in errors)
    assert any("software_commit" in error for error in errors)


def test_run_manifest_requires_explicit_finance_and_training_authorization_fields() -> None:
    manifest = run_manifest()
    del manifest["finance_authorization_id"]
    del manifest["training_authorization_id"]
    errors = validate_run_manifest(manifest, component_store())
    assert any("finance_authorization_id" in error for error in errors)
    assert any("training_authorization_id" in error for error in errors)


def test_non_executing_planning_fixture_composes_all_manifest_components() -> None:
    fixture = compose_non_executing_planning_fixture(
        run_manifest=run_manifest(),
        component_store=component_store(),
        backend_evidence=backend_evidence(),
        candidate_evidence=candidate_evidence(),
        base_checkpoint_binding=base_binding(),
        training_configuration=training_config(),
    )
    assert fixture["valid"] is True
    assert fixture["execution_authorized"] is False
    assert fixture["activation_state"] == "PLANNING_ONLY"
    assert fixture["winner_selection_performed"] is False


def test_current_none_authority_preflight_blocks_execution_with_reason_codes() -> None:
    decision = preflight_run_manifest(
        run_manifest(), component_store(), current_authority_state()
    )
    assert decision["allowed"] is False
    assert set(decision["reason_codes"]) >= {
        "TRAINING_AUTHORITY_NONE",
        "FINANCE_AUTHORITY_NONE",
        "MODEL_EXECUTION_AUTHORITY_NONE",
        "WEIGHT_ACCESS_AUTHORITY_NONE",
        "DEVICE_EXECUTION_AUTHORITY_NONE",
    }


def test_preflight_rejects_stale_authority_identity() -> None:
    manifest = run_manifest()
    manifest["training_authorization_id"] = "training-auth:manifest:v1"
    manifest["finance_authorization_id"] = "finance-auth:manifest:v1"
    authority = current_authority_state()
    authority["training_authorization_id"] = "training-auth:current:v2"
    authority["finance_authorization_id"] = "finance-auth:current:v2"
    authority["model_execution_authority"] = "AUTHORIZED"
    authority["weight_access_authority"] = "AUTHORIZED"
    authority["device_execution_authority"] = "AUTHORIZED"
    decision = preflight_run_manifest(manifest, component_store(), authority)
    assert decision["allowed"] is False
    assert "TRAINING_AUTHORITY_STALE_OR_MISMATCH" in decision["reason_codes"]
    assert "FINANCE_AUTHORITY_STALE_OR_MISMATCH" in decision["reason_codes"]


def test_preflight_rejects_missing_weight_hash_before_any_execution() -> None:
    store = component_store()
    del store["base_checkpoint_bindings"]["base:synthetic:v1"]["weight_content_identity"]
    decision = preflight_run_manifest(run_manifest(), store, current_authority_state())
    assert decision["allowed"] is False
    assert "BASE_WEIGHT_IDENTITY_MISSING" in decision["reason_codes"]


def test_preflight_rejects_missing_dataset_hash_and_quarantine_evidence() -> None:
    store = component_store()
    dataset = store["dataset_snapshots"]["dataset:synthetic:v1"]
    del dataset["snapshot_sha256"]
    store["quarantine_verifications"]["quarantine:synthetic:v1"]["status"] = "PENDING"
    decision = preflight_run_manifest(run_manifest(), store, current_authority_state())
    assert "DATASET_SNAPSHOT_HASH_MISSING" in decision["reason_codes"]
    assert "QUARANTINE_VERIFICATION_NOT_PASS" in decision["reason_codes"]


def test_preflight_rejects_missing_or_nonpassing_license_evidence() -> None:
    store = component_store()
    store["license_evidence"]["license:synthetic:v1"]["status"] = "UNRESOLVED"
    decision = preflight_run_manifest(run_manifest(), store, current_authority_state())
    assert "LICENSE_EVIDENCE_NOT_PASS" in decision["reason_codes"]


def test_preflight_is_validation_only_and_never_claims_execution() -> None:
    decision = preflight_run_manifest(
        run_manifest(), component_store(), current_authority_state()
    )
    assert decision["model_loaded"] is False
    assert decision["device_opened"] is False
    assert decision["training_started"] is False
