"""Spec 005 device qualification protocol validation. Metadata only.

Validates the frozen five-target protocol, per-target evidence records and
preflight readiness. Never invokes llama.cpp, model runtimes, or devices.
"""

from __future__ import annotations

from typing import Any

EXPECTED_TARGET_IDS = (
    "FLAGSHIP_REPRESENTATIVE",
    "APPLE_LOW_RESOURCE_REPRESENTATIVE",
    "MODERN_MIDRANGE_ANDROID_REPRESENTATIVE",
    "LOW_RESOURCE_ANDROID_REPRESENTATIVE",
    "LOW_RESOURCE_LAPTOP_ENVELOPE",
)
PINNED_PROTOCOL = {
    "core_context_tokens": 8192,
    "stress_context_tokens": 16384,
    "prompt_budget_core": 7168,
    "generation_budget": 1024,
    "prompt_budget_stress": 15360,
    "kv_k_type": "Q8_0",
    "kv_v_type": "Q8_0",
    "batch": 512,
    "ubatch": 128,
    "cache_reuse": False,
}
MEMORY_CEILING_BYTES = 2147483648
REQUIRED_RUN_COUNT = 5
REQUIRED_TIMING_RECORDS = (
    "ttft_ms",
    "prefill_tokens_per_second",
    "decode_tokens_per_second",
    "sustained_throughput_tokens_per_second",
)
REQUIRED_RUNTIME_IDENTITY_FIELDS = (
    "model_artifact_sha256",
    "gguf_quantization",
    "llama_cpp_core_revision",
    "build_toolchain_identity",
)
MUTABLE_IDENTITY_VALUES = frozenset({"latest", ""})


def _require_fields(record: Any, fields, prefix: str, errors: list[str]) -> None:
    if not isinstance(record, dict):
        errors.append(f"{prefix}:MALFORMED_RECORD_NOT_OBJECT")
        return
    for field in fields:
        value = record.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            errors.append(f"{prefix}:{field}_MISSING")


def validate_device_qualification_contract(contract: Any) -> list[str]:
    """Validate the frozen five-target protocol contract."""
    errors: list[str] = []
    if not isinstance(contract, dict):
        return ["DeviceContract:MALFORMED_RECORD_NOT_OBJECT"]

    targets = contract.get("targets")
    if not isinstance(targets, list):
        errors.append("DeviceContract:TARGETS_MISSING")
        targets = []
    target_ids = [t.get("target_id") for t in targets if isinstance(t, dict)]
    if len(targets) != 5:
        errors.append(f"DeviceContract:TARGET_COUNT_MUST_BE_FIVE_GOT_{len(targets)}")
    for expected in EXPECTED_TARGET_IDS:
        if expected not in target_ids:
            errors.append(f"DeviceContract:MISSING_TARGET_{expected}")

    protocol = contract.get("common_protocol") or {}
    for key, pinned in PINNED_PROTOCOL.items():
        if protocol.get(key) != pinned:
            errors.append(f"DeviceContract:{key}_MUST_BE_{pinned}")

    measurement = contract.get("measurement_policy") or {}
    if measurement.get("measured_runs") != REQUIRED_RUN_COUNT:
        errors.append("DeviceContract:measured_runs_MUST_BE_5")

    memory_gate = contract.get("memory_hard_gate") or {}
    if memory_gate.get("ceiling_bytes") != MEMORY_CEILING_BYTES:
        errors.append("DeviceContract:CEILING_BYTES_MUST_BE_2147483648")

    # Package thresholds intentionally remain unresolved (null): they are
    # fail-closed prerequisites, never defaulted.
    return errors


def _known_target_ids(contract: dict) -> set[str]:
    return {
        t.get("target_id") for t in contract.get("targets", []) if isinstance(t, dict)
    }


def validate_device_evidence_metadata(
    record: Any, contract: Any
) -> list[str]:
    """Validate one target's metadata evidence record and its measured runs."""
    errors: list[str] = []
    if not isinstance(record, dict):
        return ["DeviceEvidence:MALFORMED_RECORD_NOT_OBJECT"]

    known_targets = (
        _known_target_ids(contract) if isinstance(contract, dict) else set()
    )
    target_id = record.get("target_id")
    if target_id not in known_targets:
        errors.append(f"DeviceEvidence:UNKNOWN_TARGET_{target_id}")
        return errors

    runs = record.get("measured_runs")
    if not isinstance(runs, list):
        errors.append(f"DeviceEvidence:INCOMPLETE_MEASURED_RUNS_0_OF_{REQUIRED_RUN_COUNT}")
        return errors
    if len(runs) != REQUIRED_RUN_COUNT:
        code = (
            f"DeviceEvidence:INCOMPLETE_MEASURED_RUNS_{len(runs)}_OF_{REQUIRED_RUN_COUNT}"
            if len(runs) < REQUIRED_RUN_COUNT
            else f"DeviceEvidence:RUN_COUNT_VIOLATION_{len(runs)}_OF_EXACTLY_{REQUIRED_RUN_COUNT}"
        )
        errors.append(code)
        if len(runs) < REQUIRED_RUN_COUNT:
            return errors

    for index, run in enumerate(runs):
        prefix = f"DeviceEvidence[{index}]"
        if not isinstance(run, dict):
            errors.append(f"{prefix}:MALFORMED_RUN_NOT_OBJECT")
            continue
        if run.get("target_id") != target_id:
            errors.append(f"{prefix}:TARGET_ID_MISMATCH_WITH_EVIDENCE_HEADER")
        for field in ("absolute_peak_memory_bytes", *REQUIRED_TIMING_RECORDS):
            value = run.get(field)
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                errors.append(f"{prefix}:{field}_MISSING_OR_NON_NUMERIC")
        for field in ("thermal_state_before_run", "thermal_state_after_run",
                      "energy_proxy_per_run"):
            value = run.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{prefix}:{field}_MISSING")
        if run.get("os_memory_termination") is None:
            errors.append(f"{prefix}:os_memory_termination_ASSERTION_REQUIRED")
        if run.get("throttling_observed") is None:
            errors.append(f"{prefix}:throttling_observed_ASSERTION_REQUIRED")

    if record.get("claims_complete"):
        runtime_identity = record.get("runtime_identity")
        if not isinstance(runtime_identity, dict):
            errors.append("DeviceEvidence:RUNTIME_IDENTITY_REQUIRED_FOR_COMPLETENESS_CLAIM")
        else:
            for field in REQUIRED_RUNTIME_IDENTITY_FIELDS:
                value = runtime_identity.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"DeviceEvidence:runtime_identity.{field}_MISSING")
                elif isinstance(value, str) and value.strip().lower() in MUTABLE_IDENTITY_VALUES:
                    errors.append(
                        f"DeviceEvidence:runtime_identity.{field}_MUTABLE_LATEST_BINDING_PROHIBITED"
                    )
    return errors


def evaluate_device_preflight(records: Any, contract: Any) -> dict[str, object]:
    """Compute preflight state across all five targets; fail closed."""
    reason_codes: list[str] = []

    contract_errors = validate_device_qualification_contract(contract)
    reason_codes.extend(f"Preflight:Contract:{e}" for e in contract_errors)

    known_targets = (
        _known_target_ids(contract) if isinstance(contract, dict) else set()
    )
    if not isinstance(records, list) or not records:
        reason_codes.append("Preflight:NO_DEVICE_EVIDENCE_RECORDS")
        records = []

    seen_targets: set[str] = set()
    hard_fail = False
    incomplete = False

    for index, evidence in enumerate(records):
        prefix = f"Preflight[{index}]"
        errors = validate_device_evidence_metadata(evidence, contract)
        translated = [f"{prefix}:{e}" for e in errors]
        reason_codes.extend(translated)
        if any(("INCOMPLETE" in e or "_MISSING" in e or "MISMATCH" in e) for e in translated):
            incomplete = True
        if not isinstance(evidence, dict):
            continue
        seen_targets.add(evidence.get("target_id"))

        for run in evidence.get("measured_runs") or []:
            if not isinstance(run, dict):
                continue
            peak = run.get("absolute_peak_memory_bytes")
            if (
                isinstance(peak, (int, float))
                and not isinstance(peak, bool)
                and peak > MEMORY_CEILING_BYTES
            ):
                reason_codes.append(
                    f"Preflight:HARD_FAIL_MEMORY_CEILING_EXCEEDED_{evidence.get('target_id')}"
                )
                hard_fail = True
            if run.get("os_memory_termination") is True:
                reason_codes.append(
                    f"Preflight:HARD_FAIL_OS_MEMORY_TERMINATION_{evidence.get('target_id')}"
                )
                hard_fail = True
            if run.get("runtime_crash") is True:
                reason_codes.append(
                    f"Preflight:HARD_FAIL_RUNTIME_CRASH_{evidence.get('target_id')}"
                )
                hard_fail = True

    duplicates = sorted(
        target for target in seen_targets
        if sum(
            1 for r in records
            if isinstance(r, dict) and r.get("target_id") == target
        ) > 1
    )
    for dup in duplicates:
        reason_codes.append(f"Preflight:DUPLICATE_TARGET_EVIDENCE_{dup}")
        incomplete = True

    for missing_target in sorted(known_targets - seen_targets):
        reason_codes.append(f"Preflight:MISSING_TARGET_EVIDENCE_{missing_target}")
        incomplete = True

    unique_sorted = sorted(set(reason_codes))
    if hard_fail:
        state = "HARD_FAIL"
    elif incomplete or unique_sorted:
        state = "INCOMPLETE"
    else:
        state = "PREFLIGHT_PASS"
    return {"state": state, "reason_codes": unique_sorted}