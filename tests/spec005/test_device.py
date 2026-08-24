"""US7 fixture tests: device qualification metadata. No runtime invocation."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from src.commandmed.spec005.device import (
    evaluate_device_preflight,
    validate_device_evidence_metadata,
    validate_device_qualification_contract,
)

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = ROOT / "data/spec005/device_qualification_contract.json"


def load_contract():
    return json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))


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
        "llama_cpp_core_revision": "abcdef1234567890abcdef1234567890abcdef12",
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


class ContractTests(unittest.TestCase):
    def test_canonical_contract_validates(self):
        self.assertEqual(validate_device_qualification_contract(load_contract()), [])

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

    def test_unresolved_package_thresholds_are_fail_closed_not_defaults(self):
        contract = load_contract()
        # null package caps stay unresolved; validator must not invent values.
        errors = validate_device_qualification_contract(contract)
        self.assertFalse(any("package" in e.lower() for e in errors))

    def test_malformed_does_not_raise(self):
        for bad in (None, [], 1):
            self.assertTrue(validate_device_qualification_contract(bad))


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
        self.assertTrue(any("LATEST" in e.upper() or "MUTABLE" in e.upper() for e in errors))

    def test_mixed_target_runs_rejected(self):
        runs = make_evidence()["measured_runs"]
        runs[0]["target_id"] = "APPLE_LOW_RESOURCE_REPRESENTATIVE"
        errors = validate_device_evidence_metadata(
            make_evidence(measured_runs=runs), load_contract()
        )
        self.assertTrue(any("TARGET" in e.upper() for e in errors))

    def test_duplicate_target_records_rejected_in_preflight(self):
        contract = load_contract()
        records = [
            make_evidence(
                evidence_id="DEV-DUP",
                target_id="FLAGSHIP_REPRESENTATIVE",
                measured_runs=[
                    make_run(run_index=i) for i in range(1, 6)
                ],
            )
        ]
        result = evaluate_device_preflight(records + [dict(records[0])], contract)
        self.assertNotEqual(result["state"], "PREFLIGHT_PASS")
        self.assertTrue(any("DUPLICATE" in c.upper() for c in result["reason_codes"]))

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


class PreflightTests(unittest.TestCase):
    def _all_targets_pass(self):
        contract = load_contract()
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

    def test_all_five_targets_pass_preflight(self):
        result = evaluate_device_preflight(self._all_targets_pass(), load_contract())
        self.assertEqual(result["state"], "PREFLIGHT_PASS")

    def test_missing_target_is_incomplete_never_silent(self):
        records = self._all_targets_pass()[:-1]
        result = evaluate_device_preflight(records, load_contract())
        self.assertEqual(result["state"], "INCOMPLETE")
        self.assertTrue(any("MISSING_TARGET" in c for c in result["reason_codes"]))

    def test_memory_ceiling_exceeded_is_hard_fail(self):
        records = self._all_targets_pass()
        records[0]["measured_runs"][0]["absolute_peak_memory_bytes"] = (
            2_147_483_649
        )
        result = evaluate_device_preflight(records, load_contract())
        self.assertEqual(result["state"], "HARD_FAIL")
        self.assertTrue(any("MEMORY_CEILING" in c for c in result["reason_codes"]))

    def test_os_memory_termination_is_hard_fail_even_below_ceiling(self):
        records = self._all_targets_pass()
        records[1]["measured_runs"][2]["os_memory_termination"] = True
        result = evaluate_device_preflight(records, load_contract())
        self.assertEqual(result["state"], "HARD_FAIL")

    def test_incomplete_never_reported_as_pass(self):
        records = self._all_targets_pass()
        records[3]["measured_runs"] = records[3]["measured_runs"][:2]
        result = evaluate_device_preflight(records, load_contract())
        self.assertIn(result["state"], {"INCOMPLETE", "HARD_FAIL"})
        self.assertNotEqual(result["state"], "PREFLIGHT_PASS")

    def test_preflight_validates_contract_first(self):
        contract = load_contract()
        contract["common_protocol"]["core_context_tokens"] = 4096
        result = evaluate_device_preflight(self._all_targets_pass(), contract)
        self.assertNotEqual(result["state"], "PREFLIGHT_PASS")
        self.assertTrue(any("core_context_tokens" in c for c in result["reason_codes"]))

    def test_no_llama_cpp_invocation_possible(self):
        import src.commandmed.spec005.device as device
        source = open(device.__file__, encoding="utf-8").read()
        for banned in ("subprocess", "os.system", "requests", "urllib", "socket"):
            self.assertNotIn(banned, source)

    def test_malformed_records_fail_closed(self):
        result = evaluate_device_preflight(None, load_contract())
        self.assertIn(result["state"], {"INCOMPLETE", "HARD_FAIL"})


if __name__ == "__main__":
    unittest.main()
