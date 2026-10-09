"""Fail-closed V5 development execution preflight.

This module validates a prospective run manifest only. It never grants authority,
downloads weights, loads a model, performs inference, or starts training.
"""
from __future__ import annotations

from dataclasses import dataclass
import re

APPROVED_MODEL_REPO = "Qwen/Qwen3.5-0.8B-Base"
APPROVED_MODEL_REVISION = "dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68"
ALLOWED_ROLES = frozenset({
    "RULE_ORACLE_DEVELOPMENT",
    "RULE_ORACLE_CALIBRATION",
    "SQUAD_RETENTION",
    "SYNTHETIC_MECHANICAL",
})
ALLOWED_INTERVENTIONS = frozenset({
    "BASELINE_V1",
    "A1_TS_V1",
    "A2_SELBIAS_V1",
    "B1_TYPED_V1",
    "C1_CRDI_V1",
    "C2_CRDI_RETAIN_V1",
    "D1_DEFER_V1",
    "D2_RULETOOL_V1",
})
TRAINABLE_INTERVENTIONS = frozenset({"B1_TYPED_V1", "C1_CRDI_V1", "C2_CRDI_RETAIN_V1"})
ALLOWED_ACTIONS = frozenset({"MODEL_LOAD", "INFERENCE", "TRAINING"})
_HEX40 = re.compile(r"^[0-9a-f]{40}$")
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_ENV_ID = re.compile(r"^sha256:[0-9a-f]{64}$")
_OUTPUT_PREFIX = "artifacts/v5/development/"


@dataclass(frozen=True)
class DevelopmentAuthority:
    approved: bool = False
    authority_id: str = "NONE"
    paid_compute: bool = False
    paid_api: bool = False
    spend_usd: float = 0.0
    phi_allowed: bool = False
    gated_data_allowed: bool = False
    confirmatory_allowed: bool = False
    reserve_allowed: bool = False


@dataclass(frozen=True)
class DevelopmentRunManifest:
    action: str
    model_repo: str
    model_revision: str
    model_artifact_sha256: str
    intervention_id: str
    data_roles: tuple[str, ...]
    code_sha: str
    environment_id: str
    output_destination: str
    confirmatory_materialized: bool = False
    reserve_materialized: bool = False
    contains_phi: bool = False
    uses_gated_data: bool = False
    paid_resource: bool = False
    expected_spend_usd: float = 0.0


@dataclass(frozen=True)
class PreflightDecision:
    allowed: bool
    state: str
    reason_codes: tuple[str, ...]


def evaluate_development_preflight(
    manifest: DevelopmentRunManifest,
    authority: DevelopmentAuthority,
) -> PreflightDecision:
    """Validate the bounded V5 development contract and fail closed on any mismatch."""
    reasons: list[str] = []
    if not authority.approved or authority.authority_id == "NONE":
        reasons.append("AUTHORITY_NOT_APPROVED")
    if authority.paid_compute or authority.paid_api or authority.spend_usd != 0.0:
        reasons.append("AUTHORITY_COST_POLICY_VIOLATION")
    if authority.phi_allowed or authority.gated_data_allowed:
        reasons.append("AUTHORITY_DATA_SCOPE_VIOLATION")
    if authority.confirmatory_allowed or authority.reserve_allowed:
        reasons.append("AUTHORITY_ROLE_SCOPE_VIOLATION")
    if manifest.action not in ALLOWED_ACTIONS:
        reasons.append("ACTION_NOT_ALLOWED")
    if manifest.model_repo != APPROVED_MODEL_REPO:
        reasons.append("MODEL_REPO_MISMATCH")
    if manifest.model_revision != APPROVED_MODEL_REVISION:
        reasons.append("MODEL_REVISION_MISMATCH")
    if not _HEX64.fullmatch(manifest.model_artifact_sha256):
        reasons.append("MODEL_ARTIFACT_HASH_MISSING_OR_INVALID")
    if not _HEX40.fullmatch(manifest.code_sha):
        reasons.append("CODE_SHA_INVALID")
    roles = set(manifest.data_roles)
    if not roles or not roles.issubset(ALLOWED_ROLES):
        reasons.append("DATA_ROLE_NOT_ALLOWED")
    if manifest.intervention_id not in ALLOWED_INTERVENTIONS:
        reasons.append("INTERVENTION_NOT_ALLOWED")
    if manifest.action == "TRAINING" and manifest.intervention_id not in TRAINABLE_INTERVENTIONS:
        reasons.append("TRAINING_INTERVENTION_NOT_ALLOWED")
    if "SQUAD_RETENTION" in roles and manifest.intervention_id != "C2_CRDI_RETAIN_V1":
        reasons.append("SQUAD_ROLE_REQUIRES_C2")
    if manifest.confirmatory_materialized or manifest.reserve_materialized:
        reasons.append("HOLDOUT_MATERIALIZATION_FORBIDDEN")
    if manifest.contains_phi or manifest.uses_gated_data:
        reasons.append("PROTECTED_OR_GATED_DATA_FORBIDDEN")
    if manifest.paid_resource or manifest.expected_spend_usd != 0.0:
        reasons.append("RUN_COST_POLICY_VIOLATION")
    if not _ENV_ID.fullmatch(manifest.environment_id):
        reasons.append("ENVIRONMENT_ID_INVALID")
    output = manifest.output_destination.replace("\\", "/")
    if not output.startswith(_OUTPUT_PREFIX) or ".." in output.split("/"):
        reasons.append("OUTPUT_DESTINATION_INVALID")
    unique = tuple(dict.fromkeys(reasons))
    return PreflightDecision(
        allowed=not unique,
        state="PREFLIGHT_PASS" if not unique else "PREFLIGHT_BLOCKED",
        reason_codes=unique,
    )
