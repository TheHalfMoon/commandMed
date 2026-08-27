"""Spec 005 device qualification and pre-execution readiness validation.

This module is metadata-only. It deliberately separates static pre-execution
readiness from post-execution measured qualification so a first device run does
not depend on evidence that can only exist after that run. It never invokes
llama.cpp, model runtimes, devices, network clients, or subprocesses.
"""

from __future__ import annotations

import re
from typing import Any

PROTOCOL_ID = "commandmed-spec005-device-qualification-protocol"
PROTOCOL_VERSION = "1.1"
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
PACKAGE_SCOPE = "COMPLETE_MINIMUM_TEXT_CORE_HUGGINGFACE_BUNDLE"
PACKAGE_HARD_CAP_BYTES = 700 * 1024 * 1024
PACKAGE_TARGET_BYTES = 600 * 1024 * 1024
PACKAGE_STRETCH_BYTES = 500 * 1024 * 1024
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
PRE_EXECUTION_REQUIRED_FIELDS = (
    "candidate_id",
    "candidate_role",
    "model_artifact_sha256",
    "complete_bundle_sha256",
    "complete_bundle_bytes",
    "gguf_quantization",
    "llama_cpp_core_revision",
    "build_toolchain_identity",
    "runtime_artifact_sha256",
    "wrapper_identity",
    "memory_measurement_identity",
    "thermal_signal_identity",
    "energy_signal_identity",
    "execution_plan_sha256",
)
PRE_EXECUTION_SHA256_FIELDS = (
    "model_artifact_sha256",
    "complete_bundle_sha256",
    "runtime_artifact_sha256",
    "execution_plan_sha256",
)
SHARED_PRE_EXECUTION_FIELDS = (
    "candidate_id",
    "candidate_role",
    "model_artifact_sha256",
    "complete_bundle_sha256",
    "complete_bundle_bytes",
    "gguf_quantization",
    "llama_cpp_core_revision",
)
EXECUTABLE_CANDIDATE_ROLES = frozenset({"PRIMARY", "CONTROL"})
MUTABLE_IDENTITY_VALUES = frozenset(
    {
        "",
        "latest",
        "main",
        "master",
        "none",
        "unresolved",
        "pending",
        "needs_evidence",
        "not_assessed",
        "not_authorized",
    }
)
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_GIT_COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")


def _is_canonical_sha256(value: Any) -> bool:
    return isinstance(value, str) and _SHA256_RE.fullmatch(value) is not None


def _is_resolved_identity(value: Any) -> bool:
    return (
        isinstance(value, str)
        and bool(value.strip())
        and value.strip().lower() not in MUTABLE_IDENTITY_VALUES
    )


def _require_fields(record: Any, fields, prefix: str, errors: list[str]) -> None:
    if not isinstance(record, dict):
        errors.append(f"{prefix}:MALFORMED_RECORD_NOT_OBJECT")
        return
    for field in fields:
        value = record.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            errors.append(f"{prefix}:{field}_MISSING")


def _known_target_ids(contract: dict) -> set[str]:
    return {
        t.get("target_id") for t in contract.get("targets", []) if isinstance(t, dict)
    }


def _performance_policy_is_frozen(contract: Any) -> bool:
    if not isinstance(contract, dict):
        return False
    policy = contract.get("performance_threshold_policy")
    return (
        isinstance(policy, dict)
        and policy.get("state") == "FROZEN"
        and _is_resolved_identity(policy.get("record_id"))
        and _is_canonical_sha256(policy.get("record_canonical_sha256"))
    )


def validate_device_qualification_contract(contract: Any) -> list[str]:
    """Validate the frozen device protocol, including corrective reconciliations."""
    errors: list[str] = []
    if not isinstance(contract, dict):
        return ["DeviceContract:MALFORMED_RECORD_NOT_OBJECT"]

    if contract.get("protocol_id") != PROTOCOL_ID:
        errors.append(f"DeviceContract:protocol_id_MUST_BE_{PROTOCOL_ID}")
    if contract.get("protocol_version") != PROTOCOL_VERSION:
        errors.append(f"DeviceContract:protocol_version_MUST_BE_{PROTOCOL_VERSION}")

    targets = contract.get("targets")
    if not isinstance(targets, list):
        errors.append("DeviceContract:TARGETS_MISSING")
        targets = []
    target_ids = [t.get("target_id") for t in targets if isinstance(t, dict)]
    if len(targets) != len(EXPECTED_TARGET_IDS):
        errors.append(f"DeviceContract:TARGET_COUNT_MUST_BE_FIVE_GOT_{len(targets)}")
    if len(target_ids) != len(set(target_ids)):
        errors.append("DeviceContract:DUPLICATE_TARGET_ID")
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
    if measurement.get("aggregation") != "MEDIAN_WITH_WORST_CASE":
        errors.append("DeviceContract:aggregation_MUST_BE_MEDIAN_WITH_WORST_CASE")
    if measurement.get("warmup_runs_required_before_measurement") is not False:
        errors.append("DeviceContract:NON_MEASURED_WARMUP_MUST_BE_DISABLED")
    if measurement.get("non_measured_warmup_requests") != 0:
        errors.append("DeviceContract:non_measured_warmup_requests_MUST_BE_0")
    if measurement.get("fresh_process_per_measured_run_required") is not True:
        errors.append("DeviceContract:FRESH_PROCESS_PER_MEASURED_RUN_REQUIRED")
    if measurement.get("one_measured_request_per_fresh_process") is not True:
        errors.append("DeviceContract:ONE_MEASURED_REQUEST_PER_FRESH_PROCESS_REQUIRED")

    memory_gate = contract.get("memory_hard_gate") or {}
    if memory_gate.get("ceiling_bytes") != MEMORY_CEILING_BYTES:
        errors.append("DeviceContract:CEILING_BYTES_MUST_BE_2147483648")

    package = contract.get("package_boundaries") or {}
    expected_package = {
        "scope": PACKAGE_SCOPE,
        "package_hard_cap_bytes": PACKAGE_HARD_CAP_BYTES,
        "package_target_bytes": PACKAGE_TARGET_BYTES,
        "package_stretch_bytes": PACKAGE_STRETCH_BYTES,
        "hard_cap_roles": ["PRIMARY"],
    }
    for key, expected in expected_package.items():
        if package.get(key) != expected:
            errors.append(f"DeviceContract:{key}_MUST_BE_{expected}")

    pre_execution = contract.get("pre_execution_identity_policy") or {}
    if pre_execution.get("all_five_targets_required") is not True:
        errors.append("DeviceContract:PRE_EXECUTION_ALL_FIVE_TARGETS_REQUIRED")
    if pre_execution.get("measured_runs_required") is not False:
        errors.append("DeviceContract:PRE_EXECUTION_MEASURED_RUNS_MUST_BE_FALSE")
    required_fields = pre_execution.get("required_target_identity_fields")
    if not isinstance(required_fields, list) or set(required_fields) != set(
        PRE_EXECUTION_REQUIRED_FIELDS
    ):
        errors.append("DeviceContract:PRE_EXECUTION_REQUIRED_FIELDS_MISMATCH")

    performance = contract.get("performance_threshold_policy")
    if not isinstance(performance, dict):
        errors.append("DeviceContract:PERFORMANCE_THRESHOLD_POLICY_MISSING")
    else:
        state = performance.get("state")
        if state not in {"UNRESOLVED_PRE_EXECUTION", "FROZEN"}:
            errors.append(f"DeviceContract:UNKNOWN_PERFORMANCE_THRESHOLD_STATE_{state}")
        elif state == "UNRESOLVED_PRE_EXECUTION":
            if performance.get("record_id") is not None:
                errors.append("DeviceContract:UNRESOLVED_PERFORMANCE_RECORD_ID_MUST_BE_NULL")
            if performance.get("record_canonical_sha256") is not None:
                errors.append("DeviceContract:UNRESOLVED_PERFORMANCE_RECORD_SHA_MUST_BE_NULL")
        else:
            if not _is_resolved_identity(performance.get("record_id")):
                errors.append("DeviceContract:FROZEN_PERFORMANCE_RECORD_ID_REQUIRED")
            if not _is_canonical_sha256(performance.get("record_canonical_sha256")):
                errors.append("DeviceContract:FROZEN_PERFORMANCE_RECORD_SHA256_REQUIRED")
        if (
            performance.get("resolution_rule")
            != "MUST_BE_FROZEN_BEFORE_REAL_DEVICE_EXECUTION"
        ):
            errors.append("DeviceContract:PERFORMANCE_RESOLUTION_RULE_MISMATCH")

    return sorted(set(errors))


def validate_device_execution_readiness_metadata(
    record: Any, contract: Any
) -> list[str]:
    """Validate one target's static pre-execution identity record.

    Measured runs are intentionally neither required nor interpreted here.
    """
    errors: list[str] = []
    if not isinstance(record, dict):
        return ["DeviceExecutionReadiness:MALFORMED_RECORD_NOT_OBJECT"]

    known_targets = _known_target_ids(contract) if isinstance(contract, dict) else set()
    target_id = record.get("target_id")
    if target_id not in known_targets:
        errors.append(f"DeviceExecutionReadiness:UNKNOWN_TARGET_{target_id}")
        return errors

    _require_fields(
        record,
        PRE_EXECUTION_REQUIRED_FIELDS,
        "DeviceExecutionReadiness",
        errors,
    )

    role = record.get("candidate_role")
    if role not in EXECUTABLE_CANDIDATE_ROLES:
        errors.append(f"DeviceExecutionReadiness:UNSUPPORTED_CANDIDATE_ROLE_{role}")

    for field in PRE_EXECUTION_SHA256_FIELDS:
        value = record.get(field)
        if value is not None and not _is_canonical_sha256(value):
            errors.append(f"DeviceExecutionReadiness:{field}_NOT_CANONICAL_SHA256")

    bundle_bytes = record.get("complete_bundle_bytes")
    if (
        not isinstance(bundle_bytes, int)
        or isinstance(bundle_bytes, bool)
        or bundle_bytes <= 0
    ):
        errors.append("DeviceExecutionReadiness:complete_bundle_bytes_POSITIVE_INTEGER_REQUIRED")

    llama_revision = record.get("llama_cpp_core_revision")
    if llama_revision is not None and not (
        isinstance(llama_revision, str)
        and _GIT_COMMIT_RE.fullmatch(llama_revision) is not None
    ):
        errors.append("DeviceExecutionReadiness:llama_cpp_core_revision_EXACT_COMMIT_REQUIRED")

    for field in (
        "candidate_id",
        "gguf_quantization",
        "build_toolchain_identity",
        "wrapper_identity",
        "memory_measurement_identity",
        "thermal_signal_identity",
        "energy_signal_identity",
    ):
        value = record.get(field)
        if value is not None and not _is_resolved_identity(value):
            errors.append(f"DeviceExecutionReadiness:{field}_RESOLVED_IDENTITY_REQUIRED")

    if "measured_runs" in record:
        errors.append("DeviceExecutionReadiness:MEASURED_RUNS_PROHIBITED_IN_PRE_EXECUTION_RECORD")

    return sorted(set(errors))


def evaluate_device_execution_readiness(
    records: Any, contract: Any
) -> dict[str, object]:
    """Compute static device execution readiness without requiring measured runs."""
    reason_codes: list[str] = []
    hard_fail = False

    contract_errors = validate_device_qualification_contract(contract)
    reason_codes.extend(f"ExecutionReadiness:Contract:{e}" for e in contract_errors)

    if not _performance_policy_is_frozen(contract):
        reason_codes.append("ExecutionReadiness:PERFORMANCE_THRESHOLD_POLICY_UNRESOLVED")

    known_targets = _known_target_ids(contract) if isinstance(contract, dict) else set()
    if not isinstance(records, list) or not records:
        reason_codes.append("ExecutionReadiness:NO_TARGET_IDENTITY_RECORDS")
        records = []

    seen_targets: list[str] = []
    shared_reference: dict[str, Any] | None = None
    package = contract.get("package_boundaries", {}) if isinstance(contract, dict) else {}
    hard_cap = package.get("package_hard_cap_bytes")

    for index, record in enumerate(records):
        errors = validate_device_execution_readiness_metadata(record, contract)
        reason_codes.extend(f"ExecutionReadiness[{index}]:{e}" for e in errors)
        if not isinstance(record, dict):
            continue

        target_id = record.get("target_id")
        if isinstance(target_id, str):
            seen_targets.append(target_id)

        projection = {field: record.get(field) for field in SHARED_PRE_EXECUTION_FIELDS}
        if shared_reference is None:
            shared_reference = projection
        else:
            for field in SHARED_PRE_EXECUTION_FIELDS:
                if projection.get(field) != shared_reference.get(field):
                    reason_codes.append(
                        f"ExecutionReadiness:SHARED_{field}_MISMATCH_ACROSS_TARGETS"
                    )

        bundle_bytes = record.get("complete_bundle_bytes")
        if (
            record.get("candidate_role") == "PRIMARY"
            and isinstance(bundle_bytes, int)
            and not isinstance(bundle_bytes, bool)
            and isinstance(hard_cap, int)
            and bundle_bytes > hard_cap
        ):
            reason_codes.append(
                f"ExecutionReadiness:HARD_FAIL_PRIMARY_PACKAGE_CAP_EXCEEDED_{target_id}"
            )
            hard_fail = True

    for target in sorted(set(seen_targets)):
        if seen_targets.count(target) > 1:
            reason_codes.append(f"ExecutionReadiness:DUPLICATE_TARGET_IDENTITY_{target}")

    for missing_target in sorted(known_targets - set(seen_targets)):
        reason_codes.append(f"ExecutionReadiness:MISSING_TARGET_IDENTITY_{missing_target}")

    unique_sorted = sorted(set(reason_codes))
    if hard_fail:
        state = "HARD_FAIL"
    elif unique_sorted:
        state = "INCOMPLETE"
    else:
        state = "PRE_EXECUTION_READY"
    return {"state": state, "reason_codes": unique_sorted}


def build_device_execution_readiness_record(
    records: Any, contract: Any
) -> dict[str, object]:
    """Build the deterministic identity-bearing projection used by the manifest.

    Target records are set-like for this purpose and are sorted by target_id.
    The computed state is always produced by ``evaluate_device_execution_readiness``;
    callers cannot inject a favorable state into this projection.
    """
    result = evaluate_device_execution_readiness(records, contract)
    if isinstance(records, list) and all(isinstance(item, dict) for item in records):
        normalized_records: object = sorted(
            records, key=lambda item: str(item.get("target_id", ""))
        )
    else:
        normalized_records = records
    performance = (
        contract.get("performance_threshold_policy")
        if isinstance(contract, dict)
        else None
    )
    return {
        "protocol_id": contract.get("protocol_id") if isinstance(contract, dict) else None,
        "protocol_version": (
            contract.get("protocol_version") if isinstance(contract, dict) else None
        ),
        "performance_threshold_policy": performance,
        "target_identity_records": normalized_records,
        "state": result["state"],
        "reason_codes": result["reason_codes"],
    }


def validate_device_evidence_metadata(record: Any, contract: Any) -> list[str]:
    """Validate one target's post-execution measured qualification evidence."""
    errors: list[str] = []
    if not isinstance(record, dict):
        return ["DeviceEvidence:MALFORMED_RECORD_NOT_OBJECT"]

    known_targets = _known_target_ids(contract) if isinstance(contract, dict) else set()
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
        for field in (
            "thermal_state_before_run",
            "thermal_state_after_run",
            "energy_proxy_per_run",
        ):
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
                elif value.strip().lower() in MUTABLE_IDENTITY_VALUES:
                    errors.append(
                        f"DeviceEvidence:runtime_identity.{field}_MUTABLE_BINDING_PROHIBITED"
                    )
    return sorted(set(errors))


def evaluate_device_preflight(records: Any, contract: Any) -> dict[str, object]:
    """Compute post-execution measured qualification; historical name preserved.

    This function is intentionally *not* the pre-execution A15 gate. Five
    measured runs per target are required here because this is post-execution
    qualification evidence.
    """
    reason_codes: list[str] = []

    contract_errors = validate_device_qualification_contract(contract)
    reason_codes.extend(f"Qualification:Contract:{e}" for e in contract_errors)
    if not _performance_policy_is_frozen(contract):
        reason_codes.append("Qualification:PERFORMANCE_THRESHOLD_POLICY_UNRESOLVED")

    known_targets = _known_target_ids(contract) if isinstance(contract, dict) else set()
    if not isinstance(records, list) or not records:
        reason_codes.append("Qualification:NO_DEVICE_EVIDENCE_RECORDS")
        records = []

    seen_targets: list[str] = []
    hard_fail = False

    for index, evidence in enumerate(records):
        prefix = f"Qualification[{index}]"
        errors = validate_device_evidence_metadata(evidence, contract)
        reason_codes.extend(f"{prefix}:{e}" for e in errors)
        if not isinstance(evidence, dict):
            continue
        target_id = evidence.get("target_id")
        if isinstance(target_id, str):
            seen_targets.append(target_id)

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
                    f"Qualification:HARD_FAIL_MEMORY_CEILING_EXCEEDED_{target_id}"
                )
                hard_fail = True
            if run.get("os_memory_termination") is True:
                reason_codes.append(
                    f"Qualification:HARD_FAIL_OS_MEMORY_TERMINATION_{target_id}"
                )
                hard_fail = True
            if run.get("runtime_crash") is True:
                reason_codes.append(f"Qualification:HARD_FAIL_RUNTIME_CRASH_{target_id}")
                hard_fail = True

    for target in sorted(set(seen_targets)):
        if seen_targets.count(target) > 1:
            reason_codes.append(f"Qualification:DUPLICATE_TARGET_EVIDENCE_{target}")

    for missing_target in sorted(known_targets - set(seen_targets)):
        reason_codes.append(f"Qualification:MISSING_TARGET_EVIDENCE_{missing_target}")

    unique_sorted = sorted(set(reason_codes))
    if hard_fail:
        state = "HARD_FAIL"
    elif unique_sorted:
        state = "INCOMPLETE"
    else:
        state = "PREFLIGHT_PASS"
    return {"state": state, "reason_codes": unique_sorted}
