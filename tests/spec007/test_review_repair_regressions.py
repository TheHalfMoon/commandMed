"""Regression fixtures for material PR #53 review findings.

These tests remain synthetic and offline. They exercise fail-closed validation
only; no model, dataset payload, device, network, credential, or training
execution is performed.
"""

from __future__ import annotations

from copy import deepcopy

import pytest

from src.commandmed.spec007.activation import (
    compose_non_executing_planning_fixture,
    preflight_run_manifest,
)
from src.commandmed.spec007.foundation import parse_json_object, validate_closed_object
from src.commandmed.spec007.intelligence import validate_resource_accounting_record
from src.commandmed.spec007.preservation import validate_capability_preservation_binding
from src.commandmed.spec007.selection import validate_checkpoint_ranking_inputs
from src.commandmed.spec007.sequence import (
    evaluate_truncation_admission,
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
from tests.spec007.test_preservation_contracts import valid_capability_binding
from tests.spec007.test_quarantine_snapshot import rendered_record
from tests.spec007.test_selection_reproducibility import separately_authorized_policy
from tests.spec007.test_sequence_contracts import valid_packing_policy


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


def test_snapshot_rejects_prohibited_source_authority_even_with_allowed_split() -> None:
    record = rendered_record("gold-bypass")
    record["source_authority_id"] = "COMMANDMED_CLINICAL_GOLD"
    # Keep the split apparently train-eligible to prove authority cannot hide behind it.
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
    store = component_store()
    store["license_evidence"]["license:synthetic:v1"]["license_evidence_id"] = "license:other"
    decision = preflight_run_manifest(manifest, store, authority)
    assert decision["allowed"] is False
    assert "LICENSE_EVIDENCE_IDENTITY_MISMATCH" in decision["reason_codes"]


def test_nested_quarantine_identity_mismatch_blocks_preflight() -> None:
    manifest, authority = _authorized_preflight_inputs()
    store = component_store()
    store["quarantine_verifications"]["quarantine:synthetic:v1"][
        "quarantine_verification_id"
    ] = "quarantine:other"
    decision = preflight_run_manifest(manifest, store, authority)
    assert decision["allowed"] is False
    assert "QUARANTINE_VERIFICATION_IDENTITY_MISMATCH" in decision["reason_codes"]


def test_malformed_dataset_snapshot_blocks_authorized_preflight() -> None:
    manifest, authority = _authorized_preflight_inputs()
    store = component_store()
    dataset = store["dataset_snapshots"]["dataset:synthetic:v1"]
    dataset["snapshot_sha256"] = "not-a-canonical-digest"
    decision = preflight_run_manifest(manifest, store, authority)
    assert decision["allowed"] is False
    assert "DATASET_SNAPSHOT_INVALID" in decision["reason_codes"]


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


def test_malformed_capability_slices_fail_closed_without_exception() -> None:
    binding = valid_capability_binding()
    binding["required_slices"] = ["SAFETY", ["ARABIC"]]
    errors = validate_capability_preservation_binding(binding)
    assert errors
    assert any("required_slices" in error for error in errors)


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
