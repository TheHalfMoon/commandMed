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
    metrics_identity = manifest.get("metrics_v2_identity")
    if not isinstance(metrics_identity, dict):
        errors.append("Manifest:metrics_v2_identity_MUST_BE_OBJECT")
        metrics_identity = {}
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
    quality_identity = manifest.get("selection_quality_contract_identity")
    if not isinstance(quality_identity, dict):
        errors.append("Manifest:selection_quality_contract_identity_MUST_BE_OBJECT")
        quality_identity = {}
    if not isinstance(quality, dict):
        errors.append("Manifest:SelectionQualityContract:SUPPLIED_ARTIFACT_REQUIRED")
    else:
        if (
            quality_identity.get("contract_id") != quality.get("contract_id")
            or quality_identity.get("contract_version")
            != quality.get("contract_version")
        ):
            errors.append("Manifest:SELECTION_QUALITY_CONTRACT_IDENTITY_MISMATCH")
        declared_sha = quality_identity.get("selection_quality_contract_sha256")
        supplied_sha = quality.get("canonical_sha256")
        if not isinstance(supplied_sha, str) or not supplied_sha.strip():
            errors.append(
                "Manifest:SelectionQualityContract:SUPPLIED_CANONICAL_SHA_ABSENT"
            )
        elif declared_sha != supplied_sha:
            errors.append("Manifest:SELECTION_QUALITY_CONTRACT_SHA_MISMATCH")

    def _id_sha_map(value: Any, prefix: str, id_field: str) -> dict:
        if not isinstance(value, list):
            errors.append(f"{prefix}:MUST_BE_LIST")
            return {}
        mapping: dict = {}
        for entry in value:
            if not isinstance(entry, dict):
                errors.append(f"{prefix}:MALFORMED_RECORD_NOT_OBJECT")
                continue
            entry_id = entry.get(id_field)
            if not isinstance(entry_id, str) or not entry_id.strip():
                errors.append(f"{prefix}:{id_field}_RESOLVED_STRING_REQUIRED")
                continue
            mapping[entry_id] = entry.get("record_canonical_sha256")
        return mapping

    supplied_thresholds = _id_sha_map(
        artifacts.get("threshold_policies"),
        "Manifest:ThresholdPolicies",
        "threshold_policy_id",
    )
    declared_thresholds = _id_sha_map(
        manifest.get("threshold_policy_identities"),
        "Manifest:ThresholdPolicyIdentities",
        "threshold_policy_id",
    )
    for policy_id in sorted(set(declared_thresholds) - set(supplied_thresholds)):
        errors.append(f"Manifest:THRESHOLD_POLICY_{policy_id}_NOT_SUPPLIED")
    for policy_id in sorted(set(supplied_thresholds) - set(declared_thresholds)):
        errors.append(f"Manifest:THRESHOLD_POLICY_{policy_id}_NOT_DECLARED")
    for policy_id in sorted(set(declared_thresholds) & set(supplied_thresholds)):
        if declared_thresholds[policy_id] != supplied_thresholds[policy_id]:
            errors.append(
                f"Manifest:THRESHOLD_POLICY_{policy_id}_SHA_MISMATCH_WITH_SUPPLIED"
            )

    supplied_designs = _id_sha_map(
        artifacts.get("statistical_designs"),
        "Manifest:StatisticalDesigns",
        "statistical_design_id",
    )
    declared_designs = _id_sha_map(
        manifest.get("statistical_design_identities"),
        "Manifest:StatisticalDesignIdentities",
        "statistical_design_id",
    )
    for design_id in sorted(set(declared_designs) - set(supplied_designs)):
        errors.append(f"Manifest:STATISTICAL_DESIGN_{design_id}_NOT_SUPPLIED")
    for design_id in sorted(set(supplied_designs) - set(declared_designs)):
        errors.append(f"Manifest:STATISTICAL_DESIGN_{design_id}_NOT_DECLARED")
    for design_id in sorted(set(declared_designs) & set(supplied_designs)):
        if declared_designs[design_id] != supplied_designs[design_id]:
            errors.append(
                f"Manifest:STATISTICAL_DESIGN_{design_id}_SHA_MISMATCH_WITH_SUPPLIED"
            )

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
            candidate_id = candidate.get("candidate_id")
            if not isinstance(candidate_id, str) or not candidate_id.strip():
                errors.append(f"{prefix}:candidate_id_RESOLVED_STRING_REQUIRED")
            role = candidate.get("candidate_role")
            if role not in CANDIDATE_ROLES:
                errors.append(f"{prefix}:UNKNOWN_CANDIDATE_ROLE_{role}")
            if candidate.get("base_pretrained") is not True:
                errors.append(
                    f"{prefix}:BASE_PRETRAINED_REQUIRED_FOR_BASELINE_TOURNAMENT"
                )
            if _contains_private_gold(candidate):
                errors.append(f"{prefix}:PRIVATE_GOLD_EVIDENCE_PROHIBITED")

    comparison = manifest.get("comparison_policy")
    if not isinstance(comparison, dict):
        errors.append("Manifest:comparison_policy_MUST_BE_OBJECT")
        comparison = {}
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
            if isinstance(c, dict) and isinstance(c.get("candidate_id"), str)
        ],
        "metrics_v2_binding": dict(metrics_identity),
    }