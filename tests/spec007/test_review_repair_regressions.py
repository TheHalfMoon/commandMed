"""Regression fixtures for material PR #53 review findings.

These tests remain synthetic and offline. They exercise fail-closed validation
only; no model, dataset payload, device, network, credential, or training
execution is performed.
"""

from __future__ import annotations

import pytest

from src.commandmed.spec007.activation import (
    compose_non_executing_planning_fixture,
    preflight_run_manifest,
)
from src.commandmed.spec007.foundation import parse_json_object, validate_closed_object
from src.commandmed.spec007.intelligence import validate_resource_accounting_record
from src.commandmed.spec007.preservation import (
    evaluate_abort_sentinel_effect,
    validate_capability_preservation_binding,
)
from src.commandmed.spec007.selection import validate_checkpoint_ranking_inputs
from src.commandmed.spec007.sequence import (
    compute_loss_mask_policy_sha256,
    compute_prompt_rendering_policy_sha256,
    evaluate_truncation_admission,
    validate_loss_mask_policy,
    validate_packing_truncation_policy,
)
from src.commandmed.spec007.snapshot import build_dataset_snapshot
from tests.spec007.test_activation_control_plane import (
    backend_evidence,
    base_binding,
    candidate_evidence,
    component_store,
    current_authority_state,
    run_manifest,
    training_config,
)
from tests.spec007.test_intelligence_failure_contracts import resource_record
from tests.spec007.test_preservation_contracts import (
    valid_abort_policy,
    valid_capability_binding,
)
from tests.spec007.test_quarantine_snapshot import rendered_record
from tests.spec007.test_selection_reproducibility import (
    environment_manifest,
    evaluation_binding,
    fixed_policy,
    recipe_evidence,
    separately_authorized_policy,
)
from tests.spec007.test_sequence_contracts import (
    valid_loss_policy,
    valid_packing_policy,
    valid_rendering_policy,
)


def _authorized_preflight_inputs() -> tuple[dict[str, object], dict[str, object]]:
    manifest = run_manifest()
    manifest["training_authorization_id"] = "training-auth:v1"
    manifest["finance_authorization_id"] = "finance-auth:v1"
    authority = current_authority_state()
    authority.update(
        {
            "training_authorization_id": "training-auth:v1",
            "finance_authorization_id": "finance-auth:v1",
            "model_execution_authority": "AUTHORIZED",
            "weight_access_authority": "AUTHORIZED",
            "device_execution_authority": "AUTHORIZED",
        }
    )
    return manifest, authority


def _valid_component_store() -> dict[str, dict[str, dict[str, object]]]:
    """Return complete synthetic component records for a fully authorized preflight."""
    store = component_store()

    rendering = valid_rendering_policy()
    rendering["policy_id"] = "render:synthetic:v1"
    rendering["base_checkpoint_binding_id"] = "base:synthetic:v1"
    rendering["policy_sha256"] = compute_prompt_rendering_policy_sha256(rendering)

    loss = valid_loss_policy()
    loss["policy_id"] = "loss:synthetic:v1"
    loss["rendering_policy_id"] = "render:synthetic:v1"
    loss["policy_sha256"] = compute_loss_mask_policy_sha256(loss)

    packing = valid_packing_policy()
    packing["policy_id"] = "packing:synthetic:v1"

    checkpoint = fixed_policy()
    checkpoint["policy_id"] = "checkpoint-policy:synthetic:v1"

    capability = valid_capability_binding()
    capability["binding_id"] = "capability:synthetic:v1"
    capability["base_checkpoint_binding_id"] = "base:synthetic:v1"
    capability["frozen_evaluation_protocol_id"] = "eval-binding:synthetic:v1"
    capability["quarantine_verification_id"] = "quarantine:synthetic:v1"

    environment = environment_manifest()
    environment["environment_id"] = "env:synthetic:v1"

    evaluation = evaluation_binding()
    evaluation["binding_id"] = "eval-binding:synthetic:v1"

    recipe = recipe_evidence()
    recipe["evidence_id"] = "recipe:synthetic:v1"

    dataset = build_dataset_snapshot(
        [],
        snapshot_id="dataset:synthetic:v1",
        canonical_order_identity="record-id-ascending-v1",
        duplicate_report_id="dup:synthetic:v1",
        contamination_report_id="contam:synthetic:v1",
        quarantine_verification_id="quarantine:synthetic:v1",
    )

    store["dataset_snapshots"]["dataset:synthetic:v1"] = dataset
    store["prompt_rendering_policies"]["render:synthetic:v1"] = rendering
    store["loss_mask_policies"]["loss:synthetic:v1"] = loss
    store["packing_truncation_policies"]["packing:synthetic:v1"] = packing
    store["checkpoint_selection_policies"]["checkpoint-policy:synthetic:v1"] = checkpoint
    store["capability_preservation_bindings"]["capability:synthetic:v1"] = capability
    store["environment_manifests"]["env:synthetic:v1"] = environment
    store["frozen_evaluation_protocol_bindings"]["eval-binding:synthetic:v1"] = evaluation
    store["non_executing_recipe_evidence"]["recipe:synthetic:v1"] = recipe
    return store


def test_snapshot_rejects_prohibited_source_authority_even_with_allowed_split() -> None:
    record = rendered_record("gold-bypass")
    record["source_authority_id"] = "COMMANDMED_CLINICAL_GOLD"
    record["split_id"] = "VERIFIED_SFT_CURRICULUM_DATA"
    from src.commandmed.spec007.curriculum import compute_curriculum_record_sha256

    record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)
    with pytest.raises(ValueError, match="source_authority_id"):
        build_dataset_snapshot(
            [record],
            snapshot_id="snapshot:gold-bypass",
            canonical_order_identity="record-id-ascending-v1",
            duplicate_report_id="dup:gold-bypass",
            contamination_report_id="contam:gold-bypass",
            quarantine_verification_id="quarantine:gold-bypass",
        )


def test_abort_sentinel_cannot_rank_even_with_separate_authorization() -> None:
    policy = separately_authorized_policy()
    policy["selection_source_ids"] = ["MODEL_SELECTION_DEV_SET"]
    auth = policy["selection_source_purpose_authorization"]
    assert isinstance(auth, dict)
    auth["authorized_source_ids"] = ["MODEL_SELECTION_DEV_SET"]
    decision = validate_checkpoint_ranking_inputs(
        policy,
        [{"source_id": "MODEL_SELECTION_DEV_SET", "source_class": "ABORT_SENTINEL"}],
    )
    assert decision["allowed"] is False
    assert decision["reason_code"] == "RANKING_SOURCE_CLASS_PROHIBITED"


def test_protected_or_noncanonical_checkpoint_source_cannot_rank() -> None:
    policy = separately_authorized_policy()
    policy["selection_source_ids"] = ["COMMANDMED_CLINICAL_GOLD"]
    auth = policy["selection_source_purpose_authorization"]
    assert isinstance(auth, dict)
    auth["authorized_source_ids"] = ["COMMANDMED_CLINICAL_GOLD"]
    decision = validate_checkpoint_ranking_inputs(
        policy,
        [{"source_id": "COMMANDMED_CLINICAL_GOLD", "source_class": "LLM_JUDGE"}],
    )
    assert decision["allowed"] is False
    assert decision["reason_code"] == "RANKING_SOURCE_QUARANTINED"


def test_nested_license_identity_mismatch_blocks_preflight() -> None:
    manifest, authority = _authorized_preflight_inputs()
    store = _valid_component_store()
    store["license_evidence"]["license:synthetic:v1"]["license_evidence_id"] = "license:other"
    decision = preflight_run_manifest(manifest, store, authority)
    assert decision["allowed"] is False
    assert "LICENSE_EVIDENCE_IDENTITY_MISMATCH" in decision["reason_codes"]


def test_nested_quarantine_identity_mismatch_blocks_preflight() -> None:
    manifest, authority = _authorized_preflight_inputs()
    store = _valid_component_store()
    store["quarantine_verifications"]["quarantine:synthetic:v1"][
        "quarantine_verification_id"
    ] = "quarantine:other"
    decision = preflight_run_manifest(manifest, store, authority)
    assert decision["allowed"] is False
    assert "QUARANTINE_VERIFICATION_IDENTITY_MISMATCH" in decision["reason_codes"]


def test_malformed_dataset_snapshot_blocks_authorized_preflight() -> None:
    manifest, authority = _authorized_preflight_inputs()
    store = _valid_component_store()
    assert preflight_run_manifest(manifest, store, authority)["allowed"] is True
    store["dataset_snapshots"]["dataset:synthetic:v1"]["snapshot_sha256"] = "BAD"
    decision = preflight_run_manifest(manifest, store, authority)
    assert decision["allowed"] is False
    assert "DATASET_SNAPSHOT_INVALID" in decision["reason_codes"]


def test_invalid_resolved_component_blocks_authorized_preflight() -> None:
    manifest, authority = _authorized_preflight_inputs()
    store = _valid_component_store()
    assert preflight_run_manifest(manifest, store, authority)["allowed"] is True
    store["environment_manifests"]["env:synthetic:v1"]["known_nondeterminism"] = "NONE"
    decision = preflight_run_manifest(manifest, store, authority)
    assert decision["allowed"] is False
    assert "COMPONENT_RECORD_INVALID:environment_manifest_id" in decision["reason_codes"]


def test_planning_composition_rejects_supplied_component_divergence() -> None:
    supplied_base = base_binding()
    supplied_base["checkpoint_identity"] = "checkpoint:different"
    fixture = compose_non_executing_planning_fixture(
        run_manifest=run_manifest(),
        component_store=component_store(),
        backend_evidence=backend_evidence(),
        candidate_evidence=candidate_evidence(),
        base_checkpoint_binding=supplied_base,
        training_configuration=training_config(),
    )
    assert fixture["valid"] is False
    assert fixture["validation"]["composition"]


def test_closed_object_with_mixed_key_types_returns_errors_not_exception() -> None:
    errors = validate_closed_object(
        {"required": "ok", 1: "bad", "extra": "bad"},
        required_fields=("required",),
    )
    assert any("object keys must be strings" in error for error in errors)
    assert any("undeclared fields" in error for error in errors)


def test_invalid_json_constants_are_rejected() -> None:
    for raw in ('{"value": NaN}', '{"value": Infinity}', '{"value": -Infinity}'):
        parsed, errors = parse_json_object(raw)
        assert parsed is None
        assert errors == ["record: malformed JSON"]


def test_malformed_required_context_entries_fail_closed_without_exception() -> None:
    policy = valid_packing_policy()
    policy["required_context_classes"] = [
        "SUPERVISED_TARGET",
        ["SAFETY_OR_EMERGENCY_CONTEXT"],
    ]
    errors = validate_packing_truncation_policy(policy)
    assert errors
    decision = evaluate_truncation_admission(policy, [], [])
    assert decision["allowed"] is False
    assert decision["reason_codes"] == ["INVALID_PACKING_POLICY"]


def test_malformed_loss_rule_value_fails_closed_without_exception() -> None:
    policy = valid_loss_policy()
    policy["token_class_rules"]["USER"] = ["MASKED"]
    assert validate_loss_mask_policy(policy)


def test_malformed_capability_slices_fail_closed_without_exception() -> None:
    binding = valid_capability_binding()
    binding["required_slices"] = ["SAFETY", ["ARABIC"]]
    errors = validate_capability_preservation_binding(binding)
    assert errors
    assert any("required_slices" in error for error in errors)


def test_malformed_abort_effect_fails_closed_without_exception() -> None:
    decision = evaluate_abort_sentinel_effect(valid_abort_policy(), ["ABORT_RUN"])
    assert decision["allowed"] is False
    assert decision["reason_code"] == "EFFECT_NOT_AUTHORIZED"


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
@pytest.mark.parametrize(
    "field",
    [
        "ttft_ms",
        "prefill_tokens_per_second",
        "decode_tokens_per_second",
        "sustained_tokens_per_second",
        "energy_joules_per_case",
    ],
)
def test_nonfinite_resource_measurements_are_rejected(field: str, value: float) -> None:
    record = resource_record()
    record[field] = value
    errors = validate_resource_accounting_record(record)
    assert any(field in error for error in errors)
