"""Spec 005 tournament manifest validation and Spec 004 projection adapter.

Validates the pre-execution Spec 005 manifest against exact bound identities
and emits a fail-closed readiness evaluation. A real Spec 004 projection is
only producible after a separately authorized A15 activation; synthetic or
complete-but-unauthorized evidence never produces one.
"""

from __future__ import annotations

from typing import Any

from ..eval_contract.validate import validate_metrics_catalog_v2
from ..eval_contract.canonical import compute_canonical_sha256
from ..tournament import CANONICAL_METRICS_V2_BINDING

CANDIDATE_ROLES = frozenset({"PRIMARY", "CONTROL", "CONDITIONAL", "REFERENCE_ONLY"})
PROHIBITED_EVIDENCE_MARKERS = ("COMMANDMED_ARABIC_GOLD", "PRIVATE_GOLD")

MANIFEST_REQUIRED_FIELDS = (
    "manifest_id",
    "manifest_version",
    "metrics_v2_identity",
    "selection_quality_contract_identity",
    "threshold_policy_identities",
    "statistical_design_identities",
    "preconstruction_snapshot_identity",
    "candidate_admission_records",
    "device_protocol_identity",
    "comparison_policy",
    "record_canonical_sha256",
)


def _require_fields(record: Any, fields, prefix: str, errors: list[str]) -> None:
    if not isinstance(record, dict):
        errors.append(f"{prefix}:MALFORMED_RECORD_NOT_OBJECT")
        return
    for field in fields:
        value = record.get(field)
        if value is None:
            errors.append(f"{prefix}:{field}_MISSING")


def _contains_private_gold(value: Any) -> bool:
    if isinstance(value, str):
        return any(marker in value for marker in PROHIBITED_EVIDENCE_MARKERS)
    if isinstance(value, dict):
        return any(_contains_private_gold(v) for v in value.values())
    if isinstance(value, list):
        return any(_contains_private_gold(item) for item in value)
    return False


def validate_spec005_manifest(manifest: Any, artifacts: Any) -> list[str]:
    """Validate exact identity bindings of the Spec 005 manifest."""
    errors: list[str] = []
    _require_fields(manifest, MANIFEST_REQUIRED_FIELDS, "Manifest", errors)
    if not isinstance(manifest, dict):
        return errors
    if not isinstance(artifacts, dict):
        errors.append("Manifest:Artifacts:MALFORMED_RECORD_NOT_OBJECT")
        return errors

    # Exact metrics-v2 binding, verified against the supplied catalog content.
    metrics_identity = manifest.get("metrics_v2_identity") or {}
    for field, expected in CANONICAL_METRICS_V2_BINDING.items():
        if metrics_identity.get(field) != expected:
            errors.append(
                f"Manifest:metrics_v2_identity.{field}_MISMATCH_WITH_CANONICAL_BINDING"
            )
    catalog = artifacts.get("metrics_v2_catalog")
    valid, catalog_errors = validate_metrics_catalog_v2(catalog)
    if not valid:
        errors.extend(f"Manifest:MetricsV2Catalog:{e}" for e in catalog_errors)
    else:
        actual_sha = compute_canonical_sha256(catalog)
        if actual_sha != CANONICAL_METRICS_V2_BINDING["metrics_catalog_sha256"]:
            errors.append("Manifest:MetricsV2Catalog:SEMANTIC_SHA_MISMATCH")

    quality = artifacts.get("selection_quality_contract")
    quality_identity = manifest.get("selection_quality_contract_identity") or {}
    if not isinstance(quality, dict):
        errors.append("Manifest:SelectionQualityContract:SUPPLIED_ARTIFACT_REQUIRED")
    elif (
        quality_identity.get("contract_id") != quality.get("contract_id")
        or quality_identity.get("contract_version") != quality.get("contract_version")
    ):
        errors.append("Manifest:SELECTION_QUALITY_CONTRACT_IDENTITY_MISMATCH")

    thresholds_supplied = {
        t.get("threshold_policy_id")
        for t in artifacts.get("threshold_policies", []) or []
        if isinstance(t, dict)
    }
    thresholds_declared = {
        t.get("threshold_policy_id")
        for t in manifest.get("threshold_policy_identities") or []
        if isinstance(t, dict)
    }
    if thresholds_declared != thresholds_supplied:
        errors.append("Manifest:THRESHOLD_POLICY_IDENTITIES_MISMATCH_WITH_SUPPLIED")

    designs_supplied = {
        d.get("statistical_design_id")
        for d in artifacts.get("statistical_designs", []) or []
        if isinstance(d, dict)
    }
    designs_declared = {
        d.get("statistical_design_id")
        for d in manifest.get("statistical_design_identities") or []
        if isinstance(d, dict)
    }
    if designs_declared != designs_supplied:
        errors.append("Manifest:STATISTICAL_DESIGN_IDENTITIES_MISMATCH_WITH_SUPPLIED")

    device_identity = manifest.get("device_protocol_identity")
    if not isinstance(device_identity, dict) or device_identity.get("preflight_state") != (
        "PREFLIGHT_PASS"
    ):
        errors.append("Manifest:DEVICE_PROTOCOL_PREFLIGHT_PASS_REQUIRED")

    candidates = manifest.get("candidate_admission_records") or []
    if not isinstance(candidates, list) or not candidates:
        errors.append("Manifest:CANDIDATE_ADMISSION_RECORDS_NON_EMPTY_REQUIRED")
    else:
        for index, candidate in enumerate(candidates):
            prefix = f"Manifest:Candidate[{index}]"
            if not isinstance(candidate, dict):
                errors.append(f"{prefix}:MALFORMED_RECORD_NOT_OBJECT")
                continue
            role = candidate.get("candidate_role")
            if role not in CANDIDATE_ROLES:
                errors.append(f"{prefix}:UNKNOWN_CANDIDATE_ROLE_{role}")
            if candidate.get("base_pretrained") is not True:
                errors.append(
                    f"{prefix}:BASE_PRETRAINED_REQUIRED_FOR_BASELINE_TOURNAMENT"
                )
            if _contains_private_gold(candidate):
                errors.append(f"{prefix}:PRIVATE_GOLD_EVIDENCE_PROHIBITED")

    comparison = manifest.get("comparison_policy") or {}
    if comparison.get("comparison_strategy") != "LEXICOGRAPHIC_PREDECLARED" or (
        comparison.get("tie_policy") != "NO_SELECTION_ON_TIE"
    ):
        errors.append("Manifest:COMPARISON_POLICY_MUST_INHERIT_SPEC004_SEMANTICS")
    return errors


def evaluate_spec005_preflight(manifest: Any, artifacts: Any) -> dict[str, object]:
    """Fail-closed preflight; only complete exact evidence may pass."""
    reason_codes: list[str] = []

    errors = validate_spec005_manifest(manifest, artifacts)
    reason_codes.extend(f"PROJECTION:{e}" for e in errors)

    if isinstance(manifest, dict):
        if not manifest.get("threshold_policy_identities"):
            reason_codes.append("PROJECTION:NO_THRESHOLD_POLICY_IDENTITIES")
        if not manifest.get("statistical_design_identities"):
            reason_codes.append("PROJECTION:NO_STATISTICAL_DESIGN_IDENTITIES")

        activation = manifest.get("construction_activation_identity")
        if not isinstance(activation, dict):
            reason_codes.append("PROJECTION:A15_REAL_ACTIVATION_NOT_AUTHORIZED")
        elif activation.get("activation_state") != "AUTHORIZED_TO_CONSTRUCT":
            reason_codes.append("PROJECTION:A15_REAL_ACTIVATION_NOT_AUTHORIZED")

    unique_sorted = sorted(set(reason_codes))
    state = "PREFLIGHT_COMPLETE" if not unique_sorted else "PREFLIGHT_BLOCKED"
    return {"state": state, "reason_codes": unique_sorted}


def build_spec004_projection(manifest: Any, artifacts: Any) -> dict[str, object] | None:
    """Produce a Spec 004-compatible manifest only when fully authorized.

    A15 real construction activation is separately authorized; until then no
    executable projection exists. This function therefore returns None unless
    preflight is complete AND an explicitly authorized activation is bound.
    """
    preflight = evaluate_spec005_preflight(manifest, artifacts)
    if preflight["state"] != "PREFLIGHT_COMPLETE":
        return None

    if not isinstance(manifest, dict):
        return None
    activation = manifest.get("construction_activation_identity")
    if not isinstance(activation, dict) or activation.get(
        "activation_state"
    ) != "AUTHORIZED_TO_CONSTRUCT":
        return None

    metrics_identity = manifest["metrics_v2_identity"]
    return {
        "manifest_kind": "SPEC004_TOURNAMENT_MANIFEST_FROM_SPEC005",
        "schema_version": "1.0",
        "execution_mode": "PRECOMPUTED_RESULTS_ONLY",
        "comparison_strategy": manifest["comparison_policy"]["comparison_strategy"],
        "tie_policy": manifest["comparison_policy"]["tie_policy"],
        "candidate_ids": [
            c["candidate_id"]
            for c in manifest["candidate_admission_records"]
        ],
        "metrics_v2_binding": dict(metrics_identity),
    }