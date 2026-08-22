"""Deterministic fixture-only tournament harness for commandMed Spec 004.

This module consumes only canonical governance metadata plus precomputed
synthetic result envelopes. It deliberately exposes no model, benchmark,
provider, network, subprocess, credential, or training execution surface.
"""

from __future__ import annotations

import copy
import math
import re
import unicodedata
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
    validate_contamination_records,
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
QUARANTINE_CONTAINER_KEYS = frozenset({"quarantine_rules", "contamination_records"})
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

SCHEMA_VERSION = "1.0"
EXECUTION_MODE = "PRECOMPUTED_RESULTS_ONLY"
COMPARISON_STRATEGY = "LEXICOGRAPHIC_PREDECLARED"
TIE_POLICY = "NO_SELECTION_ON_TIE"
CANDIDATE_STATES = frozenset({"QUALIFIED", "DISQUALIFIED", "INCOMPLETE"})
VALID_GATE_STATES = frozenset(state.value for state in GateEvaluationState)

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
PROHIBITED_COMPACT_KEYS = frozenset(key.replace("_", "") for key in PROHIBITED_NORMALIZED_KEYS)
UNRESOLVED = frozenset({"", "NONE", "UNRESOLVED", "UNBOUND", "PENDING", "NOT_APPLICABLE"})
HEX_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
CONTROL_CHAR_RE = re.compile(r"[\x00-\x1f\x7f]")


def _resolved_string(value: Any) -> bool:
    """Return true only for resolved, printable, non-sentinel strings."""
    return (
        isinstance(value, str)
        and bool(value.strip())
        and value.strip().upper() not in UNRESOLVED
        and CONTROL_CHAR_RE.search(value) is None
    )


def _exact_keys(
    value: Any,
    required: frozenset[str],
    optional: frozenset[str] = frozenset(),
) -> list[str]:
    """Validate a closed object shape without normalizing unknown fields away."""
    if not isinstance(value, dict):
        return ["expected an object"]
    actual = set(value)
    errors: list[str] = []
    missing = sorted(required - actual)
    extra = sorted(actual - required - optional)
    if missing:
        errors.append(f"missing required fields {missing}")
    if extra:
        errors.append(f"unknown fields {extra}")
    return errors


def _normalize_prohibited_key(key: str) -> str:
    """Normalize separators and Unicode compatibility forms for denylist matching."""
    compatible = unicodedata.normalize("NFKC", key).casefold()
    return re.sub(r"[^a-z0-9]+", "_", compatible).strip("_")


def _scan_prohibited_keys(value: Any, path: str) -> list[str]:
    """Reject hidden execution/payload keys recursively with order-neutral list paths."""
    errors: list[str] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            if not isinstance(key, str):
                errors.append(f"{path}: object key must be a string")
                continue
            normalized = _normalize_prohibited_key(key)
            compact = normalized.replace("_", "")
            child = f"{path}.{normalized or '<empty-key>'}"
            if normalized in PROHIBITED_NORMALIZED_KEYS or compact in PROHIBITED_COMPACT_KEYS:
                errors.append(f"{child}: prohibited execution/payload key '{normalized}'")
            errors.extend(_scan_prohibited_keys(nested, child))
    elif isinstance(value, list):
        for nested in value:
            errors.extend(_scan_prohibited_keys(nested, f"{path}[]"))
    return errors


def compute_canonical_tournament_artifact_identities(artifacts: dict[str, Any]) -> dict[str, str]:
    """Compute the six inherited semantic identities pinned by Spec 004 V1."""
    return {
        "benchmarks_sha256": compute_canonical_sha256(artifacts["benchmarks"]),
        "metrics_sha256": compute_canonical_sha256(artifacts["metrics"]),
        "gold_protocols_sha256": compute_canonical_sha256(artifacts["gold_protocols"]),
        "quarantine_sha256": compute_canonical_sha256(artifacts["quarantine"]),
        "safety_policy_sha256": compute_canonical_sha256(artifacts["safety_policy"]),
        "lineage_contract_sha256": compute_lineage_contract_sha256(artifacts["lineage_contract"]),
    }


def _validate_artifacts(artifacts: Any) -> tuple[list[str], dict[str, str] | None]:
    """Validate canonical artifact semantics before trusting their identities."""
    errors = [f"artifacts: {error}" for error in _exact_keys(artifacts, ARTIFACT_KEYS)]
    if errors or not isinstance(artifacts, dict):
        return errors, None

    for name, validator in (
        ("benchmarks", validate_benchmark_registry),
        ("metrics", validate_metrics_catalog),
        ("gold_protocols", validate_gold_protocols),
    ):
        try:
            valid, nested = validator(artifacts[name])
        except (KeyError, TypeError, ValueError) as exc:
            errors.append(f"artifacts.{name}: canonical validator failed closed: {exc}")
        else:
            if not valid or nested:
                errors.extend(f"artifacts.{name}: {error}" for error in nested)

    quarantine = artifacts.get("quarantine")
    quarantine_key_errors = _exact_keys(quarantine, QUARANTINE_CONTAINER_KEYS)
    errors.extend(f"artifacts.quarantine: {error}" for error in quarantine_key_errors)
    if not quarantine_key_errors and isinstance(quarantine, dict):
        for field, validator in (
            ("quarantine_rules", validate_quarantine_rules),
            ("contamination_records", validate_contamination_records),
        ):
            try:
                valid, nested = validator(quarantine[field])
            except (KeyError, TypeError, ValueError) as exc:
                errors.append(
                    f"artifacts.quarantine.{field}: canonical validator failed closed: {exc}"
                )
            else:
                if not valid or nested:
                    errors.extend(f"artifacts.quarantine.{field}: {error}" for error in nested)

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


def _manifest_projection(manifest: Any) -> Any:
    """Normalize only the manifest fields explicitly defined as set-like."""
    if not isinstance(manifest, dict):
        return copy.deepcopy(manifest)
    result = copy.deepcopy(manifest)
    if isinstance(result.get("candidate_ids"), list):
        result["candidate_ids"] = sorted(result["candidate_ids"], key=str)
    return result


def compute_tournament_manifest_sha256(manifest: Any) -> str:
    """Hash the manifest while treating candidate ordering as non-semantic."""
    return compute_canonical_sha256(_manifest_projection(manifest))


def _exact_integer_hash_projection(value: Any) -> Any:
    """Encode report integers as exact tagged hex values before canonical JSON hashing.

    Python 3.11 intentionally limits conversion of extremely large integers to
    decimal strings. Hex conversion is exact and is not subject to that decimal
    conversion limit. Booleans remain booleans rather than integers.
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return {"__commandmed_exact_int_hex__": hex(value)}
    if isinstance(value, dict):
        return {key: _exact_integer_hash_projection(nested) for key, nested in value.items()}
    if isinstance(value, list):
        return [_exact_integer_hash_projection(nested) for nested in value]
    return value


def _report_projection(report: Any) -> Any:
    """Normalize report collections while preserving lexicographic vector order."""
    if not isinstance(report, dict):
        return copy.deepcopy(report)
    result = copy.deepcopy(report)
    result.pop("report_sha256", None)
    if isinstance(result.get("candidate_reports"), list):
        result["candidate_reports"] = sorted(
            result["candidate_reports"],
            key=lambda item: str(item.get("candidate_id", "")) if isinstance(item, dict) else str(item),
        )
        for candidate in result["candidate_reports"]:
            if not isinstance(candidate, dict):
                continue
            for field in ("reason_codes", "validation_errors", "lineage_reason_codes"):
                if isinstance(candidate.get(field), list):
                    candidate[field] = sorted(candidate[field])
            vector = candidate.get("comparison_vector")
            if isinstance(vector, list):
                candidate["comparison_vector"] = [
                    [
                        item.get("metric_id"),
                        item.get("direction"),
                        item.get("score"),
                        item.get("evidence_artifact_id"),
                    ]
                    if isinstance(item, dict)
                    else item
                    for item in vector
                ]
    if isinstance(result.get("result_set_errors"), list):
        result["result_set_errors"] = sorted(result["result_set_errors"])
    return _exact_integer_hash_projection(result)


def compute_tournament_report_sha256(report: Any) -> str:
    """Hash scientific report fields without self-reference or runtime metadata."""
    return compute_canonical_sha256(_report_projection(report))


def _metric_index(metrics: Any) -> dict[str, dict[str, Any]]:
    """Index canonical metric records by exact metric ID."""
    if not isinstance(metrics, list):
        return {}
    return {
        item["metric_id"]: item
        for item in metrics
        if isinstance(item, dict) and isinstance(item.get("metric_id"), str)
    }


def validate_tournament_manifest(manifest: Any, artifacts: Any) -> list[str]:
    """Validate the exact V1 manifest against canonical Specs 001-003 identities."""
    errors = [f"manifest: {error}" for error in _exact_keys(manifest, MANIFEST_KEYS)]
    errors.extend(_scan_prohibited_keys(manifest, "manifest"))
    if errors or not isinstance(manifest, dict):
        return errors

    if not _resolved_string(manifest.get("tournament_id")):
        errors.append("manifest.tournament_id: resolved non-empty string required")
    for field, expected in (
        ("schema_version", SCHEMA_VERSION),
        ("execution_mode", EXECUTION_MODE),
        ("comparison_strategy", COMPARISON_STRATEGY),
        ("tie_policy", TIE_POLICY),
    ):
        if manifest.get(field) != expected:
            errors.append(f"manifest.{field}: expected '{expected}'")

    candidates = manifest.get("candidate_ids")
    if not isinstance(candidates, list) or not candidates:
        errors.append("manifest.candidate_ids: non-empty list required")
    else:
        normalized_candidates: list[str] = []
        for candidate_id in candidates:
            if not _resolved_string(candidate_id):
                errors.append("manifest.candidate_ids: unresolved candidate ID is prohibited")
            else:
                normalized_candidates.append(candidate_id.strip())
        if len(normalized_candidates) != len(set(normalized_candidates)):
            errors.append("manifest.candidate_ids: duplicate candidate IDs are prohibited")

    comparison_ids = manifest.get("comparison_metric_ids")
    if not isinstance(comparison_ids, list) or not comparison_ids:
        errors.append("manifest.comparison_metric_ids: non-empty ordered list required")
    else:
        normalized_metrics: list[str] = []
        for index, metric_id in enumerate(comparison_ids):
            if not _resolved_string(metric_id):
                errors.append(f"manifest.comparison_metric_ids[{index}]: resolved string required")
            else:
                normalized_metrics.append(metric_id.strip())
        if len(normalized_metrics) != len(set(normalized_metrics)):
            errors.append("manifest.comparison_metric_ids: duplicates are prohibited")

    artifact_errors, identities = _validate_artifacts(artifacts)
    errors.extend(artifact_errors)

    declared = manifest.get("canonical_artifact_identities")
    if not isinstance(declared, dict):
        errors.append("manifest.canonical_artifact_identities: exact identity map required")
    else:
        if set(declared) != set(CANONICAL_UPSTREAM_IDENTITIES_V1):
            errors.append("manifest.canonical_artifact_identities: identity keys must exactly match V1")
        for key, value in declared.items():
            if not isinstance(value, str) or HEX_SHA256_RE.fullmatch(value) is None:
                errors.append(f"manifest.canonical_artifact_identities.{key}: lowercase SHA-256 required")
        if declared != CANONICAL_UPSTREAM_IDENTITIES_V1:
            errors.append(
                "manifest.canonical_artifact_identities: must equal CANONICAL_UPSTREAM_IDENTITIES_V1"
            )
        if identities is not None and declared != identities:
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
                if metric.get("direction") not in {
                    MetricDirection.HIGHER_BETTER.value,
                    MetricDirection.LOWER_BETTER.value,
                }:
                    errors.append(
                        f"manifest.comparison_metric_ids: metric '{metric_id}' has unsupported direction '{metric.get('direction')}'"
                    )
        try:
            scope_errors = validate_evaluation_scope(
                artifacts.get("safety_policy"), manifest.get("safety_scope")
            )
        except (KeyError, TypeError, ValueError) as exc:
            scope_errors = [f"canonical scope validator failed closed: {exc}"]
        errors.extend(f"manifest.safety_scope: {error}" for error in scope_errors)
    return errors


def _metric_shape_errors(metric_results: Any, metrics: Any) -> list[str]:
    """Validate exact precomputed metric-result envelope shapes."""
    if not isinstance(metric_results, dict):
        return ["metric_results: expected an object"]
    errors: list[str] = []
    known = _metric_index(metrics)
    for metric_id, result in metric_results.items():
        if not isinstance(metric_id, str) or metric_id not in known:
            errors.append(f"metric_results: unknown canonical metric '{metric_id}'")
            continue
        nested = _exact_keys(result, METRIC_RESULT_REQUIRED_KEYS, METRIC_RESULT_OPTIONAL_KEYS)
        errors.extend(f"metric_results.{metric_id}: {error}" for error in nested)
        if nested or not isinstance(result, dict):
            continue
        if result.get("status") not in VALID_GATE_STATES:
            errors.append(f"metric_results.{metric_id}.status: unsupported state '{result.get('status')}'")
        score = result.get("score")
        if score is not None:
            if isinstance(score, bool) or not isinstance(score, (int, float)):
                errors.append(f"metric_results.{metric_id}.score: numeric or null required")
            elif isinstance(score, float) and not math.isfinite(score):
                errors.append(f"metric_results.{metric_id}.score: finite numeric or null required")
        evidence = result.get("evidence_artifact_id")
        if evidence is not None and not isinstance(evidence, str):
            errors.append(f"metric_results.{metric_id}.evidence_artifact_id: string or null required")
        if "reason" in result and not isinstance(result["reason"], str):
            errors.append(f"metric_results.{metric_id}.reason: string required when present")
    return errors


def _candidate_structural_errors(
    result: Any,
    manifest: dict[str, Any],
    artifacts: dict[str, Any],
) -> list[str]:
    """Validate candidate envelope structure without duplicating lineage/safety policy."""
    errors = [
        f"candidate: {error}"
        for error in _exact_keys(result, CANDIDATE_REQUIRED_KEYS, CANDIDATE_OPTIONAL_KEYS)
    ]
    errors.extend(_scan_prohibited_keys(result, "candidate"))
    if errors or not isinstance(result, dict):
        return errors

    candidate_id = result.get("candidate_id")
    if not _resolved_string(candidate_id):
        errors.append("candidate.candidate_id: resolved string required")
    elif candidate_id not in manifest.get("candidate_ids", []):
        errors.append(f"candidate.candidate_id: undeclared candidate '{candidate_id}'")
    if result.get("tournament_manifest_sha256") != compute_tournament_manifest_sha256(manifest):
        errors.append("candidate.tournament_manifest_sha256: exact manifest identity mismatch")

    lineage = result.get("candidate_lineage_record")
    if not isinstance(lineage, dict):
        errors.append("candidate.candidate_lineage_record: object required")
    else:
        if lineage.get("asset_id") != candidate_id:
            errors.append("candidate.candidate_lineage_record.asset_id: must equal candidate_id")
        if lineage.get("asset_class") != "MODEL_OR_CHECKPOINT":
            errors.append("candidate.candidate_lineage_record.asset_class: must be MODEL_OR_CHECKPOINT")
        if lineage.get("declared_use") != "DEVELOPMENT_EVALUATION":
            errors.append(
                "candidate.candidate_lineage_record.declared_use: must be DEVELOPMENT_EVALUATION"
            )
    if "lineage_registry" in result and not isinstance(result.get("lineage_registry"), list):
        errors.append("candidate.lineage_registry: list required when present")
    errors.extend(_metric_shape_errors(result.get("metric_results"), artifacts.get("metrics")))
    return errors


def _comparison_evidence(
    result: dict[str, Any],
    manifest: dict[str, Any],
    artifacts: dict[str, Any],
) -> tuple[list[str], list[dict[str, Any]]]:
    """Build a comparable vector while keeping arbitrary integers out of float conversion."""
    metric_results = result.get("metric_results")
    if not isinstance(metric_results, dict):
        return ["comparison: metric_results object required"], []
    metrics = _metric_index(artifacts["metrics"])
    errors: list[str] = []
    vector: list[dict[str, Any]] = []
    for metric_id in manifest["comparison_metric_ids"]:
        evidence = metric_results.get(metric_id)
        if not isinstance(evidence, dict):
            errors.append(f"comparison.{metric_id}: result required")
            continue
        if evidence.get("status") != GateEvaluationState.PASS.value:
            errors.append(f"comparison.{metric_id}: status must be PASS")
            continue
        score = evidence.get("score")
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            errors.append(f"comparison.{metric_id}: finite numeric score required")
            continue
        if isinstance(score, float) and not math.isfinite(score):
            errors.append(f"comparison.{metric_id}: finite numeric score required")
            continue
        evidence_id = evidence.get("evidence_artifact_id")
        if not _resolved_string(evidence_id):
            errors.append(f"comparison.{metric_id}: resolved evidence_artifact_id required")
            continue
        vector.append(
            {
                "metric_id": metric_id,
                "direction": metrics[metric_id]["direction"],
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
    comparison_errors, _ = _comparison_evidence(result, manifest, artifacts)
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
    """Create one deterministic candidate qualification record."""
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
    """Classify a declared candidate as qualified, disqualified, or incomplete."""
    structural = _candidate_structural_errors(result, manifest, artifacts)
    if structural or not isinstance(result, dict):
        reasons = {"MALFORMED_CANDIDATE_RESULT"}
        if any("tournament_manifest_sha256" in error for error in structural):
            reasons.add("MANIFEST_IDENTITY_MISMATCH")
        return _candidate_report(candidate_id, "INCOMPLETE", reasons, structural)

    lineage = evaluate_lineage_admission(
        result["candidate_lineage_record"],
        artifacts["lineage_contract"],
        result.get("lineage_registry"),
    )
    if lineage.get("state") in {"PROHIBITED", "REFERENCE_ONLY"}:
        return _candidate_report(
            candidate_id,
            "DISQUALIFIED",
            {"LINEAGE_NOT_ELIGIBLE"},
            [],
            lineage=lineage,
        )
    if lineage.get("state") != "ELIGIBLE":
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

    comparison_errors, vector = _comparison_evidence(result, manifest, artifacts)
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


def _rank(candidate: dict[str, Any]) -> tuple[float | int, ...]:
    """Convert a qualified comparison vector into a direction-normalized rank tuple."""
    return tuple(
        item["score"]
        if item["direction"] == MetricDirection.HIGHER_BETTER.value
        else -item["score"]
        for item in candidate["comparison_vector"]
    )


def _base_report(manifest: Any) -> dict[str, Any]:
    """Create the report shell, including the exact canonical upstream identity map."""
    return {
        "tournament_id": manifest.get("tournament_id") if isinstance(manifest, dict) else None,
        "tournament_manifest_sha256": compute_tournament_manifest_sha256(manifest),
        "canonical_artifact_identities": dict(CANONICAL_UPSTREAM_IDENTITIES_V1),
        "tournament_state": "NO_SELECTION",
        "reason_code": None,
        "selected_candidate_id": None,
        "candidate_reports": [],
        "result_set_errors": [],
    }


def _finalize(report: dict[str, Any]) -> dict[str, Any]:
    """Canonicalize report collections and append the non-self-referential report digest."""
    report["candidate_reports"] = sorted(
        report["candidate_reports"], key=lambda item: item["candidate_id"]
    )
    report["result_set_errors"] = sorted(report["result_set_errors"])
    report["report_sha256"] = compute_tournament_report_sha256(report)
    return report


def evaluate_tournament(manifest: Any, candidate_results: Any, artifacts: Any) -> dict[str, Any]:
    """Evaluate a frozen fixture tournament without producing or executing model output."""
    report = _base_report(manifest)
    manifest_errors = validate_tournament_manifest(manifest, artifacts)
    if manifest_errors:
        report["reason_code"] = "INVALID_MANIFEST_OR_PROTOCOL"
        report["result_set_errors"] = manifest_errors
        return _finalize(report)

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
        return _finalize(report)

    buckets: dict[str, list[Any]] = {candidate_id: [] for candidate_id in declared_ids}
    result_set_errors: list[str] = []
    for result in candidate_results:
        if not isinstance(result, dict):
            result_set_errors.append("candidate_results: non-object result envelope present")
            continue
        candidate_id = result.get("candidate_id")
        if not _resolved_string(candidate_id):
            result_set_errors.append("candidate_results: result envelope has unresolved candidate_id")
            continue
        if candidate_id not in buckets:
            result_set_errors.append(f"candidate_results: undeclared candidate_id '{candidate_id}'")
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
        return _finalize(report)
    if any(item["state"] == "INCOMPLETE" for item in candidate_reports):
        report["reason_code"] = "CANDIDATE_EVIDENCE_INCOMPLETE"
        return _finalize(report)

    qualified = [item for item in candidate_reports if item["state"] == "QUALIFIED"]
    if not qualified:
        report["reason_code"] = "NO_QUALIFIED_CANDIDATE"
        return _finalize(report)

    ranked = [(item, _rank(item)) for item in qualified]
    best_rank = max(rank for _, rank in ranked)
    best = [item for item, rank in ranked if rank == best_rank]
    if len(best) != 1:
        report["reason_code"] = "TOP_TIE"
        return _finalize(report)

    report["tournament_state"] = "SELECTED"
    report["reason_code"] = "UNIQUE_BEST_QUALIFIED_CANDIDATE"
    report["selected_candidate_id"] = best[0]["candidate_id"]
    return _finalize(report)
