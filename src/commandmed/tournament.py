"""Deterministic fixture-only tournament harness for commandMed Spec 004.

This module consumes only in-memory canonical metadata and precomputed result
records. It intentionally contains no model runner, benchmark loader, provider
client, subprocess, network, or training surface.
"""

from __future__ import annotations

import copy
import math
import re
from typing import Any

from .eval_contract.canonical import compute_canonical_sha256
from .eval_contract.lineage import (
    compute_lineage_contract_sha256,
    evaluate_lineage_admission,
    validate_lineage_contract,
)
from .eval_contract.model import GateEvaluationState, MetricDirection
from .eval_contract.safety import (
    evaluate_safety_qualification_hard_gates,
    validate_evaluation_scope,
    validate_safety_policy,
)
from .eval_contract.validate import (
    validate_benchmark_registry,
    validate_gold_protocols,
    validate_metrics_catalog,
    validate_quarantine_rules,
)


CANONICAL_UPSTREAM_IDENTITIES_V1: dict[str, str] = {
    "benchmarks_sha256": "7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7",
    "metrics_sha256": "304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a",
    "gold_protocols_sha256": "40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666",
    "quarantine_sha256": "b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080",
    "safety_policy_sha256": "79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f",
    "lineage_contract_sha256": "2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962",
}

ARTIFACT_KEYS = frozenset(
    {"benchmarks", "metrics", "gold_protocols", "quarantine", "safety_policy", "lineage_contract"}
)
MANIFEST_KEYS = frozenset(
    {
        "tournament_id",
        "schema_version",
        "execution_mode",
        "comparison_strategy",
        "comparison_metric_ids",
        "candidate_ids",
        "tie_policy",
        "safety_scope",
        "canonical_artifact_identities",
    }
)
CANDIDATE_REQUIRED_KEYS = frozenset(
    {"candidate_id", "tournament_manifest_sha256", "candidate_lineage_record", "metric_results"}
)
CANDIDATE_OPTIONAL_KEYS = frozenset({"lineage_registry"})
METRIC_RESULT_REQUIRED_KEYS = frozenset({"status", "score", "evidence_artifact_id"})
METRIC_RESULT_OPTIONAL_KEYS = frozenset({"reason"})

EXECUTION_MODE = "PRECOMPUTED_RESULTS_ONLY"
COMPARISON_STRATEGY = "LEXICOGRAPHIC_PREDECLARED"
TIE_POLICY = "NO_SELECTION_ON_TIE"
SCHEMA_VERSION = "1.0"

CANDIDATE_STATES = frozenset({"QUALIFIED", "DISQUALIFIED", "INCOMPLETE"})
TOURNAMENT_STATES = frozenset({"SELECTED", "NO_SELECTION"})

PROHIBITED_NORMALIZED_KEYS = frozenset(
    {
        "command",
        "commands",
        "shell",
        "argv",
        "executable",
        "hook",
        "hooks",
        "prompt",
        "prompts",
        "messages",
        "api_key",
        "access_token",
        "token",
        "credential",
        "credentials",
        "secret",
        "secrets",
        "provider_endpoint",
        "endpoint",
        "model_path",
        "weights_path",
        "checkpoint_path",
        "benchmark_payload",
        "case_payload",
        "question_text",
        "private_gold_payload",
        "model_output",
        "generated_text",
    }
)

RESOLVED_SENTINELS = frozenset({"", "NONE", "UNRESOLVED", "UNBOUND", "PENDING", "NOT_APPLICABLE"})
HEX_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
CONTROL_CHAR_RE = re.compile(r"[\x00-\x1f\x7f]")
VALID_GATE_STATES = frozenset(state.value for state in GateEvaluationState)


def _normalized_key(value: str) -> str:
    """Normalize a mapping key for the exact Spec 004 execution-surface denylist."""
    return value.strip().casefold().replace("-", "_").replace(" ", "_")


def _resolved_string(value: Any) -> bool:
    return (
        isinstance(value, str)
        and bool(value.strip())
        and value.strip().upper() not in RESOLVED_SENTINELS
        and CONTROL_CHAR_RE.search(value) is None
    )


def _exact_keys(value: Any, required: frozenset[str], optional: frozenset[str] = frozenset()) -> list[str]:
    if not isinstance(value, dict):
        return ["expected an object"]
    actual = set(value)
    missing = sorted(required - actual)
    extra = sorted(actual - required - optional)
    errors: list[str] = []
    if missing:
        errors.append(f"missing required fields {missing}")
    if extra:
        errors.append(f"unknown fields {extra}")
    return errors


def _scan_prohibited_keys(value: Any, path: str = "root") -> list[str]:
    """Reject hidden execution, credential, model, or payload channels recursively."""
    errors: list[str] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            if not isinstance(key, str):
                errors.append(f"{path}: object key must be a string")
                continue
            normalized = _normalized_key(key)
            child = f"{path}.{key}"
            if normalized in PROHIBITED_NORMALIZED_KEYS:
                errors.append(f"{child}: prohibited execution/payload key '{normalized}'")
            errors.extend(_scan_prohibited_keys(nested, child))
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            errors.extend(_scan_prohibited_keys(nested, f"{path}[{index}]"))
    return errors


def _validate_artifact_bundle(artifacts: Any) -> tuple[list[str], dict[str, str] | None]:
    errors: list[str] = []
    key_errors = _exact_keys(artifacts, ARTIFACT_KEYS)
    errors.extend(f"artifacts: {error}" for error in key_errors)
    if key_errors or not isinstance(artifacts, dict):
        return errors, None

    validators = (
        ("benchmarks", validate_benchmark_registry),
        ("metrics", validate_metrics_catalog),
        ("gold_protocols", validate_gold_protocols),
        ("quarantine", validate_quarantine_rules),
    )
    for name, validator in validators:
        try:
            valid, nested = validator(artifacts[name])
        except (KeyError, TypeError, ValueError) as exc:
            errors.append(f"artifacts.{name}: canonical validator failed closed: {exc}")
            continue
        if not valid or nested:
            errors.extend(f"artifacts.{name}: {error}" for error in nested)

    try:
        safety_errors = validate_safety_policy(artifacts["safety_policy"])
    except (KeyError, TypeError, ValueError) as exc:
        safety_errors = [f"canonical validator failed closed: {exc}"]
    errors.extend(f"artifacts.safety_policy: {error}" for error in safety_errors)

    try:
        lineage_errors = validate_lineage_contract(artifacts["lineage_contract"])
    except (KeyError, TypeError, ValueError) as exc:
        lineage_errors = [f"canonical validator failed closed: {exc}"]
    errors.extend(f"artifacts.lineage_contract: {error}" for error in lineage_errors)

    if errors:
        return errors, None

    try:
        identities = compute_canonical_tournament_artifact_identities(artifacts)
    except (KeyError, TypeError, ValueError) as exc:
        return [f"artifacts: canonical identity computation failed closed: {exc}"], None

    if identities != CANONICAL_UPSTREAM_IDENTITIES_V1:
        errors.append(
            "artifacts: supplied artifact identities do not equal CANONICAL_UPSTREAM_IDENTITIES_V1"
        )
    return errors, identities


def compute_canonical_tournament_artifact_identities(artifacts: dict[str, Any]) -> dict[str, str]:
    """Compute the six canonical upstream semantic identities used by Spec 004 V1."""
    return {
        "benchmarks_sha256": compute_canonical_sha256(artifacts["benchmarks"]),
        "metrics_sha256": compute_canonical_sha256(artifacts["metrics"]),
        "gold_protocols_sha256": compute_canonical_sha256(artifacts["gold_protocols"]),
        "quarantine_sha256": compute_canonical_sha256(artifacts["quarantine"]),
        "safety_policy_sha256": compute_canonical_sha256(artifacts["safety_policy"]),
        "lineage_contract_sha256": compute_lineage_contract_sha256(artifacts["lineage_contract"]),
    }


def _manifest_identity_projection(manifest: Any) -> Any:
    if not isinstance(manifest, dict):
        return copy.deepcopy(manifest)
    projection = copy.deepcopy(manifest)
    candidate_ids = projection.get("candidate_ids")
    if isinstance(candidate_ids, list):
        projection["candidate_ids"] = sorted(candidate_ids, key=lambda item: str(item))
    return projection


def compute_tournament_manifest_sha256(manifest: Any) -> str:
    """Hash the semantic tournament manifest; candidate set order is non-semantic."""
    return compute_canonical_sha256(_manifest_identity_projection(manifest))


def _report_identity_projection(report: Any) -> Any:
    if not isinstance(report, dict):
        return copy.deepcopy(report)
    projection = copy.deepcopy(report)
    projection.pop("report_sha256", None)
    candidate_reports = projection.get("candidate_reports")
    if isinstance(candidate_reports, list):
        projection["candidate_reports"] = sorted(
            candidate_reports,
            key=lambda item: str(item.get("candidate_id", "")) if isinstance(item, dict) else str(item),
        )
    for candidate in projection.get("candidate_reports", []):
        if isinstance(candidate, dict) and isinstance(candidate.get("reason_codes"), list):
            candidate["reason_codes"] = sorted(candidate["reason_codes"])
        if isinstance(candidate, dict) and isinstance(candidate.get("validation_errors"), list):
            candidate["validation_errors"] = sorted(candidate["validation_errors"])
    if isinstance(projection.get("result_set_errors"), list):
        projection["result_set_errors"] = sorted(projection["result_set_errors"])
    return projection


def compute_tournament_report_sha256(report: Any) -> str:
    """Hash scientific report fields without self-reference or runtime metadata."""
    return compute_canonical_sha256(_report_identity_projection(report))


def _metric_index(metrics: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(metrics, list):
        return {}
    return {
        item["metric_id"]: item
        for item in metrics
        if isinstance(item, dict) and isinstance(item.get("metric_id"), str)
    }


def validate_tournament_manifest(manifest: Any, artifacts: Any) -> list[str]:
    """Validate one exact V1 manifest against the canonical Specs 001-003 baseline."""
    errors: list[str] = []
    key_errors = _exact_keys(manifest, MANIFEST_KEYS)
    errors.extend(f"manifest: {error}" for error in key_errors)
    errors.extend(_scan_prohibited_keys(manifest, "manifest"))
    if key_errors or not isinstance(manifest, dict):
        return errors

    if not _resolved_string(manifest.get("tournament_id")):
        errors.append("manifest.tournament_id: resolved non-empty string required")
    if manifest.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"manifest.schema_version: expected '{SCHEMA_VERSION}'")
    if manifest.get("execution_mode") != EXECUTION_MODE:
        errors.append(f"manifest.execution_mode: expected '{EXECUTION_MODE}'")
    if manifest.get("comparison_strategy") != COMPARISON_STRATEGY:
        errors.append(f"manifest.comparison_strategy: expected '{COMPARISON_STRATEGY}'")
    if manifest.get("tie_policy") != TIE_POLICY:
        errors.append(f"manifest.tie_policy: expected '{TIE_POLICY}'")

    candidate_ids = manifest.get("candidate_ids")
    if not isinstance(candidate_ids, list) or not candidate_ids:
        errors.append("manifest.candidate_ids: non-empty list required")
    else:
        valid_candidates: list[str] = []
        for index, candidate_id in enumerate(candidate_ids):
            if not _resolved_string(candidate_id):
                errors.append(f"manifest.candidate_ids[{index}]: resolved string required")
            else:
                valid_candidates.append(candidate_id.strip())
        if len(valid_candidates) != len(set(valid_candidates)):
            errors.append("manifest.candidate_ids: duplicate candidate IDs are prohibited")

    comparison_ids = manifest.get("comparison_metric_ids")
    if not isinstance(comparison_ids, list) or not comparison_ids:
        errors.append("manifest.comparison_metric_ids: non-empty ordered list required")
    else:
        valid_metrics: list[str] = []
        for index, metric_id in enumerate(comparison_ids):
            if not _resolved_string(metric_id):
                errors.append(f"manifest.comparison_metric_ids[{index}]: resolved string required")
            else:
                valid_metrics.append(metric_id.strip())
        if len(valid_metrics) != len(set(valid_metrics)):
            errors.append("manifest.comparison_metric_ids: duplicates are prohibited")

    artifact_errors, identities = _validate_artifact_bundle(artifacts)
    errors.extend(artifact_errors)

    declared_identities = manifest.get("canonical_artifact_identities")
    if not isinstance(declared_identities, dict):
        errors.append("manifest.canonical_artifact_identities: exact identity map required")
    else:
        actual_keys = set(declared_identities)
        expected_keys = set(CANONICAL_UPSTREAM_IDENTITIES_V1)
        if actual_keys != expected_keys:
            errors.append("manifest.canonical_artifact_identities: identity keys must exactly match V1")
        for key, value in declared_identities.items():
            if not isinstance(value, str) or HEX_SHA256_RE.fullmatch(value) is None:
                errors.append(f"manifest.canonical_artifact_identities.{key}: lowercase SHA-256 required")
        if declared_identities != CANONICAL_UPSTREAM_IDENTITIES_V1:
            errors.append(
                "manifest.canonical_artifact_identities: must equal CANONICAL_UPSTREAM_IDENTITIES_V1"
            )
        if identities is not None and declared_identities != identities:
            errors.append("manifest.canonical_artifact_identities: supplied artifacts do not match manifest")

    if isinstance(artifacts, dict):
        metrics_by_id = _metric_index(artifacts.get("metrics"))
        if isinstance(comparison_ids, list):
            for metric_id in comparison_ids:
                if not isinstance(metric_id, str):
                    continue
                metric = metrics_by_id.get(metric_id)
                if metric is None:
                    errors.append(f"manifest.comparison_metric_ids: unknown metric '{metric_id}'")
                    continue
                if metric.get("is_hard_gate") is True:
                    errors.append(
                        f"manifest.comparison_metric_ids: hard-gate metric '{metric_id}' cannot rank candidates"
                    )
                direction = metric.get("direction")
                if direction not in {
                    MetricDirection.HIGHER_BETTER.value,
                    MetricDirection.LOWER_BETTER.value,
                }:
                    errors.append(
                        f"manifest.comparison_metric_ids: metric '{metric_id}' has unsupported direction '{direction}'"
                    )

        try:
            scope_errors = validate_evaluation_scope(
                artifacts.get("safety_policy"), manifest.get("safety_scope")
            )
        except (KeyError, TypeError, ValueError) as exc:
            scope_errors = [f"canonical scope validator failed closed: {exc}"]
        errors.extend(f"manifest.safety_scope: {error}" for error in scope_errors)

    return errors


def _validate_metric_result_shapes(metric_results: Any, metrics: Any) -> list[str]:
    if not isinstance(metric_results, dict):
        return ["metric_results: expected an object"]
    errors: list[str] = []
    metrics_by_id = _metric_index(metrics)
    for metric_id, result in metric_results.items():
        if not isinstance(metric_id, str) or metric_id not in metrics_by_id:
            errors.append(f"metric_results: unknown canonical metric '{metric_id}'")
            continue
        nested = _exact_keys(result, METRIC_RESULT_REQUIRED_KEYS, METRIC_RESULT_OPTIONAL_KEYS)
        errors.extend(f"metric_results.{metric_id}: {error}" for error in nested)
        if nested or not isinstance(result, dict):
            continue
        status = result.get("status")
        if status not in VALID_GATE_STATES:
            errors.append(f"metric_results.{metric_id}.status: unsupported state '{status}'")
        score = result.get("score")
        if score is not None and (isinstance(score, bool) or not isinstance(score, (int, float))):
            errors.append(f"metric_results.{metric_id}.score: numeric or null required")
        evidence = result.get("evidence_artifact_id")
        if evidence is not None and not isinstance(evidence, str):
            errors.append(f"metric_results.{metric_id}.evidence_artifact_id: string or null required")
        if "reason" in result and not isinstance(result["reason"], str):
            errors.append(f"metric_results.{metric_id}.reason: string required when present")
    return errors


def _candidate_structural_errors(result: Any, manifest: dict[str, Any], artifacts: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    nested = _exact_keys(result, CANDIDATE_REQUIRED_KEYS, CANDIDATE_OPTIONAL_KEYS)
    errors.extend(f"candidate: {error}" for error in nested)
    errors.extend(_scan_prohibited_keys(result, "candidate"))
    if nested or not isinstance(result, dict):
        return errors

    candidate_id = result.get("candidate_id")
    if not _resolved_string(candidate_id):
        errors.append("candidate.candidate_id: resolved string required")
    elif candidate_id not in manifest.get("candidate_ids", []):
        errors.append(f"candidate.candidate_id: undeclared candidate '{candidate_id}'")

    expected_manifest_sha = compute_tournament_manifest_sha256(manifest)
    supplied_manifest_sha = result.get("tournament_manifest_sha256")
    if supplied_manifest_sha != expected_manifest_sha:
        errors.append("candidate.tournament_manifest_sha256: exact manifest identity mismatch")

    lineage_record = result.get("candidate_lineage_record")
    if not isinstance(lineage_record, dict):
        errors.append("candidate.candidate_lineage_record: object required")
    else:
        if lineage_record.get("asset_id") != candidate_id:
            errors.append("candidate.candidate_lineage_record.asset_id: must equal candidate_id")
        if lineage_record.get("asset_class") != "MODEL_OR_CHECKPOINT":
            errors.append("candidate.candidate_lineage_record.asset_class: must be MODEL_OR_CHECKPOINT")
        if lineage_record.get("declared_use") != "DEVELOPMENT_EVALUATION":
            errors.append(
                "candidate.candidate_lineage_record.declared_use: must be DEVELOPMENT_EVALUATION"
            )

    if "lineage_registry" in result and not isinstance(result.get("lineage_registry"), list):
        errors.append("candidate.lineage_registry: list required when present")

    errors.extend(_validate_metric_result_shapes(result.get("metric_results"), artifacts.get("metrics")))
    return errors


def _comparison_evidence_errors(
    result: dict[str, Any], manifest: dict[str, Any], artifacts: dict[str, Any]
) -> tuple[list[str], list[dict[str, Any]]]:
    errors: list[str] = []
    vector: list[dict[str, Any]] = []
    metrics_by_id = _metric_index(artifacts["metrics"])
    metric_results = result.get("metric_results")
    if not isinstance(metric_results, dict):
        return ["comparison: metric_results object required"], []

    for metric_id in manifest["comparison_metric_ids"]:
        metric = metrics_by_id[metric_id]
        evidence = metric_results.get(metric_id)
        if not isinstance(evidence, dict):
            errors.append(f"comparison.{metric_id}: result required")
            continue
        if evidence.get("status") != GateEvaluationState.PASS.value:
            errors.append(f"comparison.{metric_id}: status must be PASS")
            continue
        score = evidence.get("score")
        if isinstance(score, bool) or not isinstance(score, (int, float)) or not math.isfinite(score):
            errors.append(f"comparison.{metric_id}: finite numeric score required")
            continue
        evidence_id = evidence.get("evidence_artifact_id")
        if not _resolved_string(evidence_id):
            errors.append(f"comparison.{metric_id}: resolved evidence_artifact_id required")
            continue
        vector.append(
            {
                "metric_id": metric_id,
                "direction": metric["direction"],
                "score": score,
                "evidence_artifact_id": evidence_id,
            }
        )
    return errors, vector


def validate_candidate_result(result: Any, manifest: Any, artifacts: Any) -> list[str]:
    """Return deterministic reasons why one precomputed result cannot qualify."""
    manifest_errors = validate_tournament_manifest(manifest, artifacts)
    if manifest_errors:
        return [f"manifest invalid: {error}" for error in manifest_errors]
    assert isinstance(manifest, dict) and isinstance(artifacts, dict)

    errors = _candidate_structural_errors(result, manifest, artifacts)
    if errors or not isinstance(result, dict):
        return errors

    lineage = evaluate_lineage_admission(
        result["candidate_lineage_record"],
        artifacts["lineage_contract"],
        result.get("lineage_registry"),
    )
    if lineage.get("state") != "ELIGIBLE":
        errors.append(
            f"candidate lineage admission is {lineage.get('state')}: {lineage.get('reason_codes', [])}"
        )

    try:
        safety_state, _ = evaluate_safety_qualification_hard_gates(
            artifacts["safety_policy"],
            manifest["safety_scope"],
            artifacts["metrics"],
            result["metric_results"],
        )
    except (KeyError, TypeError, ValueError) as exc:
        errors.append(f"candidate safety qualification failed closed: {exc}")
    else:
        if safety_state != GateEvaluationState.PASS.value:
            errors.append(f"candidate safety qualification is {safety_state}")

    comparison_errors, _ = _comparison_evidence_errors(result, manifest, artifacts)
    errors.extend(comparison_errors)
    return errors


def _candidate_report(
    candidate_id: str,
    state: str,
    reason_codes: set[str],
    validation_errors: list[str],
    *,
    lineage: dict[str, Any] | None = None,
    safety_state: str | None = None,
    safety_breakdown: list[dict[str, Any]] | None = None,
    comparison_vector: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    assert state in CANDIDATE_STATES
    return {
        "candidate_id": candidate_id,
        "state": state,
        "reason_codes": sorted(reason_codes),
        "validation_errors": sorted(validation_errors),
        "lineage_state": lineage.get("state") if isinstance(lineage, dict) else None,
        "lineage_reason_codes": lineage.get("reason_codes", []) if isinstance(lineage, dict) else [],
        "safety_state": safety_state,
        "safety_breakdown": safety_breakdown or [],
        "comparison_vector": comparison_vector or [],
    }


def _evaluate_candidate(
    candidate_id: str,
    result: Any,
    manifest: dict[str, Any],
    artifacts: dict[str, Any],
) -> dict[str, Any]:
    structural_errors = _candidate_structural_errors(result, manifest, artifacts)
    if structural_errors or not isinstance(result, dict):
        reason_codes = {"MALFORMED_CANDIDATE_RESULT"}
        if any("tournament_manifest_sha256" in error for error in structural_errors):
            reason_codes.add("MANIFEST_IDENTITY_MISMATCH")
        return _candidate_report(
            candidate_id, "INCOMPLETE", reason_codes, structural_errors
        )

    lineage = evaluate_lineage_admission(
        result["candidate_lineage_record"],
        artifacts["lineage_contract"],
        result.get("lineage_registry"),
    )
    lineage_state = lineage.get("state")
    if lineage_state in {"PROHIBITED", "REFERENCE_ONLY"}:
        return _candidate_report(
            candidate_id,
            "DISQUALIFIED",
            {"LINEAGE_NOT_ELIGIBLE"},
            [],
            lineage=lineage,
        )
    if lineage_state != "ELIGIBLE":
        return _candidate_report(
            candidate_id,
            "INCOMPLETE",
            {"LINEAGE_INCOMPLETE"},
            [],
            lineage=lineage,
        )

    try:
        safety_state, safety_breakdown = evaluate_safety_qualification_hard_gates(
            artifacts["safety_policy"],
            manifest["safety_scope"],
            artifacts["metrics"],
            result["metric_results"],
        )
    except (KeyError, TypeError, ValueError) as exc:
        return _candidate_report(
            candidate_id,
            "INCOMPLETE",
            {"SAFETY_EVIDENCE_INCOMPLETE"},
            [f"safety qualification failed closed: {exc}"],
            lineage=lineage,
        )

    if safety_state == GateEvaluationState.FAIL.value:
        return _candidate_report(
            candidate_id,
            "DISQUALIFIED",
            {"SAFETY_FAIL"},
            [],
            lineage=lineage,
            safety_state=safety_state,
            safety_breakdown=safety_breakdown,
        )
    if safety_state != GateEvaluationState.PASS.value:
        return _candidate_report(
            candidate_id,
            "INCOMPLETE",
            {"SAFETY_EVIDENCE_INCOMPLETE"},
            [],
            lineage=lineage,
            safety_state=safety_state,
            safety_breakdown=safety_breakdown,
        )

    comparison_errors, vector = _comparison_evidence_errors(result, manifest, artifacts)
    if comparison_errors:
        return _candidate_report(
            candidate_id,
            "INCOMPLETE",
            {"COMPARISON_EVIDENCE_INVALID"},
            comparison_errors,
            lineage=lineage,
            safety_state=safety_state,
            safety_breakdown=safety_breakdown,
        )

    return _candidate_report(
        candidate_id,
        "QUALIFIED",
        set(),
        [],
        lineage=lineage,
        safety_state=safety_state,
        safety_breakdown=safety_breakdown,
        comparison_vector=vector,
    )


def _ranking_tuple(candidate_report: dict[str, Any]) -> tuple[float | int, ...]:
    values: list[float | int] = []
    for item in candidate_report["comparison_vector"]:
        score = item["score"]
        if item["direction"] == MetricDirection.HIGHER_BETTER.value:
            values.append(score)
        else:
            values.append(-score)
    return tuple(values)


def _finalize_report(report: dict[str, Any]) -> dict[str, Any]:
    report["candidate_reports"] = sorted(
        report.get("candidate_reports", []), key=lambda item: item["candidate_id"]
    )
    report["result_set_errors"] = sorted(report.get("result_set_errors", []))
    report["report_sha256"] = compute_tournament_report_sha256(report)
    return report


def _base_report(manifest: Any) -> dict[str, Any]:
    tournament_id = manifest.get("tournament_id") if isinstance(manifest, dict) else None
    manifest_sha = compute_tournament_manifest_sha256(manifest)
    return {
        "tournament_id": tournament_id,
        "tournament_manifest_sha256": manifest_sha,
        "tournament_state": "NO_SELECTION",
        "reason_code": None,
        "selected_candidate_id": None,
        "candidate_reports": [],
        "result_set_errors": [],
    }


def evaluate_tournament(manifest: Any, candidate_results: Any, artifacts: Any) -> dict[str, Any]:
    """Evaluate a frozen fixture/precomputed-result tournament without executing models."""
    report = _base_report(manifest)
    manifest_errors = validate_tournament_manifest(manifest, artifacts)
    if manifest_errors:
        report["reason_code"] = "INVALID_MANIFEST_OR_PROTOCOL"
        report["result_set_errors"] = manifest_errors
        return _finalize_report(report)

    assert isinstance(manifest, dict) and isinstance(artifacts, dict)
    declared_ids = list(manifest["candidate_ids"])

    if not isinstance(candidate_results, list):
        report["reason_code"] = "CANDIDATE_RESULT_SET_INVALID"
        report["result_set_errors"] = ["candidate_results: expected a list"]
        report["candidate_reports"] = [
            _candidate_report(
                candidate_id,
                "INCOMPLETE",
                {"MISSING_CANDIDATE_RESULT"},
                ["candidate result set is malformed"],
            )
            for candidate_id in declared_ids
        ]
        return _finalize_report(report)

    buckets: dict[str, list[Any]] = {candidate_id: [] for candidate_id in declared_ids}
    result_set_errors: list[str] = []
    for index, result in enumerate(candidate_results):
        if not isinstance(result, dict):
            result_set_errors.append(f"candidate_results[{index}]: expected an object")
            continue
        candidate_id = result.get("candidate_id")
        if not isinstance(candidate_id, str) or not candidate_id.strip():
            result_set_errors.append(f"candidate_results[{index}]: resolved candidate_id required")
            continue
        if candidate_id not in buckets:
            result_set_errors.append(
                f"candidate_results[{index}]: undeclared candidate_id '{candidate_id}'"
            )
            continue
        buckets[candidate_id].append(result)

    candidate_reports: list[dict[str, Any]] = []
    for candidate_id in sorted(declared_ids):
        entries = buckets[candidate_id]
        if not entries:
            candidate_reports.append(
                _candidate_report(
                    candidate_id,
                    "INCOMPLETE",
                    {"MISSING_CANDIDATE_RESULT"},
                    ["declared candidate result is missing"],
                )
            )
        elif len(entries) > 1:
            result_set_errors.append(f"duplicate candidate result '{candidate_id}'")
            candidate_reports.append(
                _candidate_report(
                    candidate_id,
                    "INCOMPLETE",
                    {"DUPLICATE_CANDIDATE_RESULT"},
                    ["duplicate result envelopes are prohibited"],
                )
            )
        else:
            candidate_reports.append(
                _evaluate_candidate(candidate_id, entries[0], manifest, artifacts)
            )

    report["candidate_reports"] = candidate_reports
    report["result_set_errors"] = result_set_errors

    if result_set_errors:
        report["reason_code"] = "CANDIDATE_RESULT_SET_INVALID"
        return _finalize_report(report)

    if any(candidate["state"] == "INCOMPLETE" for candidate in candidate_reports):
        report["reason_code"] = "CANDIDATE_EVIDENCE_INCOMPLETE"
        return _finalize_report(report)

    qualified = [candidate for candidate in candidate_reports if candidate["state"] == "QUALIFIED"]
    if not qualified:
        report["reason_code"] = "NO_QUALIFIED_CANDIDATE"
        return _finalize_report(report)

    ranked = [(candidate, _ranking_tuple(candidate)) for candidate in qualified]
    best_rank = max(rank for _, rank in ranked)
    best = [candidate for candidate, rank in ranked if rank == best_rank]
    if len(best) != 1:
        report["reason_code"] = "TOP_TIE"
        return _finalize_report(report)

    report["tournament_state"] = "SELECTED"
    report["reason_code"] = "UNIQUE_BEST_QUALIFIED_CANDIDATE"
    report["selected_candidate_id"] = best[0]["candidate_id"]
    return _finalize_report(report)
