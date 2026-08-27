"""Corrective-maintenance fixture tests for Spec 005 device gates.

All records are synthetic metadata. No model runtime or physical device is
opened by these tests.
"""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec005.device import (
    PACKAGE_HARD_CAP_BYTES,
    PACKAGE_SCOPE,
    PACKAGE_STRETCH_BYTES,
    PACKAGE_TARGET_BYTES,
    build_device_execution_readiness_record,
    evaluate_device_execution_readiness,
    evaluate_device_preflight,
    validate_device_evidence_metadata,
    validate_device_execution_readiness_metadata,
    validate_device_qualification_contract,
)

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = ROOT / "data/spec005/device_qualification_contract.json"


def load_contract():
    return json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))


def make_ready_contract():
    contract = copy.deepcopy(load_contract())
    contract["performance_threshold_policy"] = {
        "state": "FROZEN",
        "record_id": "PERF-THRESHOLD-SYNTHETIC-001",
        "record_canonical_sha256": "9" * 64,
        "resolution_rule": "MUST_BE_FROZEN_BEFORE_REAL_DEVICE_EXECUTION",
    }
    return contract


def target_ids(contract):
    return [t["target_id"] for t in contract["targets"]]


def make_run(**overrides):
    run = {
        "target_id": "FLAGSHIP_REPRESENTATIVE",
        "condition": "CORE_8K",
        "run_index": 1,
        "absolute_peak_memory_bytes": 1_600_000_000,
        "peak_delta_bytes": 1_200_000_000,
        "baseline_before_load_bytes": 400_000_000,
        "os_memory_termination": False,
        "runtime_crash": False,
        "ttft_ms": 380.0,
        "prefill_tokens_per_second": 900.0,
        "decode_tokens_per_second": 22.5,
        "sustained_throughput_tokens_per_second": 20.0,
        "thermal_state_before_run": "NOMINAL",
        "thermal_state_after_run": "NOMINAL",
        "throttling_observed": False,
        "energy_proxy_per_run": "BATTERY_DELTA_RECORDED",
    }
    run.update(overrides)
    return run


def make_runtime_identity(**overrides):
    identity = {
        "model_artifact_sha256": "a" * 64,
        "gguf_quantization": "Q4_K_M",
        "llama_cpp_core_revision": "c" * 40,
        "build_toolchain_identity": "XCODE_15_4_ARM64_RELEASE",
        "wrapper_identity": "IOS_WRAPPER_V1",
    }
    identity.update(overrides)
    return identity


def make_evidence(**overrides):
    evidence = {
        "evidence_id": "DEV-001",
        "target_id": "FLAGSHIP_REPRESENTATIVE",
        "model_artifact_sha256": "a" * 64,
        "measured_runs": [make_run(run_index=i) for i in range(1, 6)],
        "runtime_identity": make_runtime_identity(),
        "claims_complete": True,
    }
    evidence.update(overrides)
    return evidence


def make_execution_identity(target_id="FLAGSHIP_REPRESENTATIVE", **overrides):
    record = {
        "target_id": target_id,
        "candidate_id": "candidate-alpha",
        "candidate_role": "PRIMARY",
        "model_artifact_sha256": "a" * 64,
        "complete_bundle_sha256": "b" * 64,
        "complete_bundle_bytes": 563_035_840,
        "gguf_quantization": "Q4_0",
        "llama_cpp_core_revision": "c" * 40,
        "build_toolchain_identity": f"TOOLCHAIN_{target_id}",
        "runtime_artifact_sha256": "d" * 64,
        "wrapper_identity": f"WRAPPER_{target_id}",
        "memory_measurement_identity": f"MEMORY_METHOD_{target_id}",
        "thermal_signal_identity": f"THERMAL_SIGNAL_{target_id}",
        "energy_signal_identity": f"ENERGY_SIGNAL_{target_id}",
        "execution_plan_sha256": "e" * 64,
    }
    record.update(overrides)
    return record


def all_execution_identities(contract=None, **overrides):
    contract = contract or make_ready_contract()
    return [make_execution_identity(tid, **overrides) for tid in target_ids(contract)]


class ContractTests(unittest.TestCase):
    def test_canonical_contract_validates_structurally(self):
        self.assertEqual(validate_device_qualification_contract(load_contract()), [])

    def test_corrective_contract_reconciles_package_and_warmup(self):
        contract = load_contract()
        package = contract["package_boundaries"]
        measurement = contract["measurement_policy"]
        self.assertEqual(package["scope"], PACKAGE_SCOPE)
        self.assertEqual(package["package_hard_cap_bytes"], PACKAGE_HARD_CAP_BYTES)
        self.assertEqual(package["package_target_bytes"], PACKAGE_TARGET_BYTES)
        self.assertEqual(package["package_stretch_bytes"], PACKAGE_STRETCH_BYTES)
        self.assertEqual(package["hard_cap_roles"], ["PRIMARY"])
        self.assertIs(measurement["warmup_runs_required_before_measurement"], False)
        self.assertEqual(measurement["non_measured_warmup_requests"], 0)
        self.assertIs(measurement["fresh_process_per_measured_run_required"], True)
        self.assertIs(measurement["one_measured_request_per_fresh_process"], True)

    def test_wrong_target_count_fails(self):
        contract = load_contract()
        contract["targets"] = contract["targets"][:4]
        errors = validate_device_qualification_contract(contract)
        self.assertTrue(any("TARGET" in e.upper() for e in errors))

    def test_protocol_parameters_pinned(self):
        contract = load_contract()
        contract["common_protocol"]["core_context_tokens"] = 4096
        errors = validate_device_qualification_contract(contract)
        self.assertTrue(any("core_context_tokens" in e for e in errors))

    def test_reintroducing_non_measured_warmup_fails(self):
        contract = load_contract()
        contract["measurement_policy"]["warmup_runs_required_before_measurement"] = True
        errors = validate_device_qualification_contract(contract)
        self.assertTrue(any("WARMUP" in e.upper() for e in errors))

    def test_malformed_does_not_raise(self):
        for bad in (None, [], 1):
            self.assertTrue(validate_device_qualification_contract(bad))


class ExecutionReadinessTests(unittest.TestCase):
    def test_readiness_requires_no_measured_runs(self):
        contract = make_ready_contract()
        records = all_execution_identities(contract)
        self.assertTrue(all("measured_runs" not in record for record in records))
        result = evaluate_device_execution_readiness(records, contract)
        self.assertEqual(result["state"], "PRE_EXECUTION_READY")
        self.assertEqual(result["reason_codes"], [])

    def test_unresolved_performance_policy_blocks_first_execution(self):
        contract = load_contract()
        result = evaluate_device_execution_readiness(
            all_execution_identities(make_ready_contract()), contract
        )
        self.assertEqual(result["state"], "INCOMPLETE")
        self.assertTrue(any("PERFORMANCE_THRESHOLD" in c for c in result["reason_codes"]))

    def test_missing_target_is_incomplete_without_measured_evidence(self):
        contract = make_ready_contract()
        result = evaluate_device_execution_readiness(
            all_execution_identities(contract)[:-1], contract
        )
        self.assertEqual(result["state"], "INCOMPLETE")
        self.assertTrue(any("MISSING_TARGET" in c for c in result["reason_codes"]))

    def test_missing_static_identity_is_incomplete(self):
        contract = make_ready_contract()
        records = all_execution_identities(contract)
        records[0]["thermal_signal_identity"] = "UNRESOLVED"
        result = evaluate_device_execution_readiness(records, contract)
        self.assertEqual(result["state"], "INCOMPLETE")
        self.assertTrue(any("thermal_signal_identity" in c for c in result["reason_codes"]))

    def test_primary_package_cap_exceeded_is_hard_fail(self):
        contract = make_ready_contract()
        records = all_execution_identities(
            contract, complete_bundle_bytes=PACKAGE_HARD_CAP_BYTES + 1
        )
        result = evaluate_device_execution_readiness(records, contract)
        self.assertEqual(result["state"], "HARD_FAIL")
        self.assertTrue(any("PACKAGE_CAP" in c for c in result["reason_codes"]))

    def test_control_package_cap_is_not_a_control_winning_gate(self):
        contract = make_ready_contract()
        records = all_execution_identities(
            contract,
            candidate_role="CONTROL",
            complete_bundle_bytes=PACKAGE_HARD_CAP_BYTES + 1,
        )
        result = evaluate_device_execution_readiness(records, contract)
        self.assertEqual(result["state"], "PRE_EXECUTION_READY")

    def test_shared_candidate_artifact_identity_must_match_across_targets(self):
        contract = make_ready_contract()
        records = all_execution_identities(contract)
        records[2]["model_artifact_sha256"] = "f" * 64
        result = evaluate_device_execution_readiness(records, contract)
        self.assertEqual(result["state"], "INCOMPLETE")
        self.assertTrue(any("SHARED_model_artifact" in c for c in result["reason_codes"]))

    def test_measured_runs_prohibited_in_pre_execution_record(self):
        contract = make_ready_contract()
        record = make_execution_identity(measured_runs=[])
        errors = validate_device_execution_readiness_metadata(record, contract)
        self.assertTrue(any("MEASURED_RUNS_PROHIBITED" in e for e in errors))

    def test_readiness_record_identity_is_order_invariant_for_targets(self):
        contract = make_ready_contract()
        records = all_execution_identities(contract)
        left = build_device_execution_readiness_record(records, contract)
        right = build_device_execution_readiness_record(list(reversed(records)), contract)
        self.assertEqual(
            compute_canonical_sha256(left), compute_canonical_sha256(right)
        )


class EvidenceMetadataTests(unittest.TestCase):
    def test_complete_five_run_evidence_validates(self):
        errors = validate_device_evidence_metadata(make_evidence(), load_contract())
        self.assertEqual(errors, [])

    def test_unknown_target_rejected(self):
        errors = validate_device_evidence_metadata(
            make_evidence(target_id="TARGET_TITAN"), load_contract()
        )
        self.assertTrue(any("TARGET_TITAN" in e for e in errors))

    def test_fewer_than_five_runs_is_incomplete(self):
        evidence = make_evidence(measured_runs=make_evidence()["measured_runs"][:4])
        errors = validate_device_evidence_metadata(evidence, load_contract())
        self.assertTrue(any("INCOMPLETE" in e.upper() for e in errors))

    def test_completeness_claim_requires_runtime_identity(self):
        evidence = make_evidence()
        del evidence["runtime_identity"]["llama_cpp_core_revision"]
        errors = validate_device_evidence_metadata(evidence, load_contract())
        self.assertTrue(any("llama_cpp_core_revision" in e for e in errors))

    def test_mutable_latest_revision_rejected(self):
        evidence = make_evidence(
            runtime_identity=make_runtime_identity(llama_cpp_core_revision="latest")
        )
        errors = validate_device_evidence_metadata(evidence, load_contract())
        self.assertTrue(any("MUTABLE" in e.upper() for e in errors))

    def test_missing_timing_or_protocol_run_fields_rejected(self):
        evidence = make_evidence()
        del evidence["measured_runs"][0]["ttft_ms"]
        evidence["measured_runs"][1]["thermal_state_before_run"] = ""
        evidence["measured_runs"][2]["os_memory_termination"] = None
        errors = validate_device_evidence_metadata(evidence, load_contract())
        self.assertTrue(any("ttft_ms" in e for e in errors))
        self.assertTrue(any("thermal_state_before_run" in e for e in errors))
        self.assertTrue(any("os_memory_termination" in e for e in errors))

    def test_mixed_target_runs_rejected(self):
        runs = make_evidence()["measured_runs"]
        runs[0]["target_id"] = "APPLE_LOW_RESOURCE_REPRESENTATIVE"
        errors = validate_device_evidence_metadata(
            make_evidence(measured_runs=runs), load_contract()
        )
        self.assertTrue(any("TARGET" in e.upper() for e in errors))

    def test_more_than_five_runs_rejected(self):
        runs = [make_run(run_index=i) for i in range(1, 7)]
        errors = validate_device_evidence_metadata(
            make_evidence(measured_runs=runs), load_contract()
        )
        self.assertTrue(any("RUN_COUNT" in e.upper() for e in errors))

    def test_malformed_does_not_raise(self):
        for bad in (None, 8, []):
            errors = validate_device_evidence_metadata(bad, load_contract())
            self.assertIsInstance(errors, list)
            self.assertTrue(errors)


class PostExecutionQualificationTests(unittest.TestCase):
    def _all_targets_pass(self, contract):
        records = []
        for tid in target_ids(contract):
            records.append(
                make_evidence(
                    evidence_id=f"DEV-{tid}",
                    target_id=tid,
                    measured_runs=[
                        make_run(target_id=tid, run_index=i) for i in range(1, 6)
                    ],
                )
            )
        return records

    def test_all_five_targets_pass_only_after_threshold_freeze(self):
        contract = make_ready_contract()
        result = evaluate_device_preflight(self._all_targets_pass(contract), contract)
        self.assertEqual(result["state"], "PREFLIGHT_PASS")

    def test_unresolved_threshold_policy_never_yields_post_execution_pass(self):
        contract = load_contract()
        result = evaluate_device_preflight(self._all_targets_pass(contract), contract)
        self.assertEqual(result["state"], "INCOMPLETE")
        self.assertTrue(any("PERFORMANCE_THRESHOLD" in c for c in result["reason_codes"]))

    def test_missing_target_is_incomplete_never_silent(self):
        contract = make_ready_contract()
        records = self._all_targets_pass(contract)[:-1]
        result = evaluate_device_preflight(records, contract)
        self.assertEqual(result["state"], "INCOMPLETE")
        self.assertTrue(any("MISSING_TARGET" in c for c in result["reason_codes"]))

    def test_memory_ceiling_exceeded_is_hard_fail(self):
        contract = make_ready_contract()
        records = self._all_targets_pass(contract)
        records[0]["measured_runs"][0]["absolute_peak_memory_bytes"] = 2_147_483_649
        result = evaluate_device_preflight(records, contract)
        self.assertEqual(result["state"], "HARD_FAIL")
        self.assertTrue(any("MEMORY_CEILING" in c for c in result["reason_codes"]))

    def test_os_memory_termination_is_hard_fail_even_below_ceiling(self):
        contract = make_ready_contract()
        records = self._all_targets_pass(contract)
        records[1]["measured_runs"][2]["os_memory_termination"] = True
        result = evaluate_device_preflight(records, contract)
        self.assertEqual(result["state"], "HARD_FAIL")

    def test_incomplete_never_reported_as_pass(self):
        contract = make_ready_contract()
        records = self._all_targets_pass(contract)
        records[3]["measured_runs"] = records[3]["measured_runs"][:2]
        result = evaluate_device_preflight(records, contract)
        self.assertNotEqual(result["state"], "PREFLIGHT_PASS")

    def test_preflight_validates_contract_first(self):
        contract = make_ready_contract()
        contract["common_protocol"]["core_context_tokens"] = 4096
        result = evaluate_device_preflight(self._all_targets_pass(contract), contract)
        self.assertNotEqual(result["state"], "PREFLIGHT_PASS")
        self.assertTrue(any("core_context_tokens" in c for c in result["reason_codes"]))

    def test_no_external_invocation_surface(self):
        import src.commandmed.spec005.device as device

        source = open(device.__file__, encoding="utf-8").read()
        for banned in ("subprocess", "os.system", "requests", "urllib", "socket"):
            self.assertNotIn(banned, source)

    def test_malformed_records_fail_closed(self):
        result = evaluate_device_preflight(None, make_ready_contract())
        self.assertIn(result["state"], {"INCOMPLETE", "HARD_FAIL"})


if __name__ == "__main__":
    unittest.main()
