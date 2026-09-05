"""Evidence-bound freeze validation for SP007-RO-001 evaluation assets.

This module validates provenance and source-verification instruments and composes
them with the existing rights, contamination, quarantine, Spec003 admission, and
tournament-protocol validators. It is offline control-plane code only: no model
loading, inference, device access, training, protected data, winner selection, or
spend occurs here.
"""

from __future__ import annotations

from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.foundation import is_canonical_sha256, validate_closed_object
from src.commandmed.spec007.research_scope import RESEARCH_COMPONENT_SCOPE_ID
from src.commandmed.spec007.research_tournament import ALLOWED_RANKING_METRIC_FAMILIES
from src.commandmed.spec007.research_tournament_assets import (
    ASSET_NAMESPACE_SEED,
    ASSET_SET_ID,
    CONTAMINATION_METHOD_SHA256,
    EXPECTED_QUARANTINE_MATRIX_SHA256,
    PROVENANCE_AUTHORITY_ID,
    RIGHTS_INSTRUMENT_SHA256,
    validate_frozen_research_component_tournament_subject,
)

ASSET_SET_SHA256 = "709d5f73c1599364fc184b959cbdfd199c7ec07307fef8f8091d8eafb10f5454"
PROVENANCE_INSTRUMENT_SHA256 = "82d29ba6374b1f74cd70d4c77be567f16ff78efb38008a8bc1764d9e1ac73d1f"
SOURCE_VERIFICATION_INSTRUMENT_ID = "E004_RESEARCH_COMPONENT_SOURCE_VERIFICATION_V1"
SOURCE_VERIFICATION_INSTRUMENT_SHA256 = (
    "6a71619aa8a940d97beeef13be935fbf83d865f2892f0fd3c37e53e32f427529"
)

_PROVENANCE_FIELDS = (
    "schema_version",
    "instrument_id",
    "instrument_sha256",
    "scope_id",
    "asset_set_id",
    "asset_set_sha256",
    "source_class",
    "authoring_repository",
    "fixture_namespace_seed",
    "generation_method",
    "external_payloads_used",
    "candidate_outputs_observed_before_freeze",
    "adaptive_generation_from_candidate_outputs",
    "purpose",
    "current_authorized_spend_usd",
)
_SOURCE_VERIFICATION_FIELDS = (
    "schema_version",
    "instrument_id",
    "instrument_sha256",
    "scope_id",
    "asset_set_id",
    "asset_set_sha256",
    "verification_subject",
    "repository_full_name",
    "source_authority_id",
    "provenance_instrument_sha256",
    "rights_instrument_sha256",
    "contamination_method_sha256",
    "quarantine_matrix_sha256",
    "required_asset_count",
    "required_metric_families",
    "all_asset_self_hashes_required",
    "all_cases_or_probes_nonce_bound",
    "private_gold_present",
    "external_payloads_used",
    "verification_status",
    "current_authorized_spend_usd",
)


def _self_hash(record: Mapping[str, Any]) -> str:
    projection = dict(record)
    projection.pop("instrument_sha256", None)
    return compute_canonical_sha256(projection)


def _validate_hash(record: Mapping[str, Any], expected: str, prefix: str) -> list[str]:
    claimed = record.get("instrument_sha256")
    errors: list[str] = []
    if not is_canonical_sha256(claimed):
        errors.append(f"{prefix}: instrument_sha256 must be lowercase sha256 hex")
    elif claimed != _self_hash(record):
        errors.append(f"{prefix}: instrument_sha256 mismatch")
    if claimed != expected:
        errors.append(f"{prefix}: canonical instrument identity mismatch")
    return errors


def validate_research_component_provenance_instrument(record: Any) -> list[str]:
    prefix = "ResearchComponentEvaluationProvenanceInstrument"
    errors = validate_closed_object(record, required_fields=_PROVENANCE_FIELDS, field=prefix)
    if errors or not isinstance(record, dict):
        return errors
    expected = {
        "schema_version": "1",
        "instrument_id": PROVENANCE_AUTHORITY_ID,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "asset_set_id": ASSET_SET_ID,
        "asset_set_sha256": ASSET_SET_SHA256,
        "source_class": "SYNTHETIC_NONCLINICAL_EVALUATION",
        "authoring_repository": "TheHalfMoon/commandMed",
        "fixture_namespace_seed": ASSET_NAMESPACE_SEED,
        "generation_method": "SHA256_NAMESPACE_SEED_METRIC_FAMILY_CASE_INDEX",
        "external_payloads_used": False,
        "candidate_outputs_observed_before_freeze": False,
        "adaptive_generation_from_candidate_outputs": False,
        "purpose": "COMPONENT_TOURNAMENT_SELECTION",
        "current_authorized_spend_usd": 0,
    }
    for field, value in expected.items():
        if record.get(field) != value:
            errors.append(f"{prefix}: {field} mismatch")
    errors.extend(_validate_hash(record, PROVENANCE_INSTRUMENT_SHA256, prefix))
    return sorted(set(errors))


def validate_research_component_source_verification_instrument(record: Any) -> list[str]:
    prefix = "ResearchComponentEvaluationSourceVerificationInstrument"
    errors = validate_closed_object(
        record, required_fields=_SOURCE_VERIFICATION_FIELDS, field=prefix
    )
    if errors or not isinstance(record, dict):
        return errors
    expected = {
        "schema_version": "1",
        "instrument_id": SOURCE_VERIFICATION_INSTRUMENT_ID,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "asset_set_id": ASSET_SET_ID,
        "asset_set_sha256": ASSET_SET_SHA256,
        "verification_subject": "CANONICAL_REPOSITORY_ASSET_SET_AND_SELF_HASHES",
        "repository_full_name": "TheHalfMoon/commandMed",
        "source_authority_id": PROVENANCE_AUTHORITY_ID,
        "provenance_instrument_sha256": PROVENANCE_INSTRUMENT_SHA256,
        "rights_instrument_sha256": RIGHTS_INSTRUMENT_SHA256,
        "contamination_method_sha256": CONTAMINATION_METHOD_SHA256,
        "quarantine_matrix_sha256": EXPECTED_QUARANTINE_MATRIX_SHA256,
        "required_asset_count": 7,
        "required_metric_families": sorted(ALLOWED_RANKING_METRIC_FAMILIES),
        "all_asset_self_hashes_required": True,
        "all_cases_or_probes_nonce_bound": True,
        "private_gold_present": False,
        "external_payloads_used": False,
        "verification_status": "PASS",
        "current_authorized_spend_usd": 0,
    }
    for field, value in expected.items():
        if record.get(field) != value:
            errors.append(f"{prefix}: {field} mismatch")
    errors.extend(_validate_hash(record, SOURCE_VERIFICATION_INSTRUMENT_SHA256, prefix))
    return sorted(set(errors))


def validate_frozen_research_component_evaluation_package(
    *,
    provenance_instrument: Any,
    source_verification_instrument: Any,
    rights_instrument: Any,
    contamination_method: Any,
    asset_set: Any,
    protocol: Any,
    lineage_contract: Any,
) -> list[str]:
    """Validate the complete pre-result evaluation freeze package fail closed."""
    prefix = "FrozenResearchComponentEvaluationPackage"
    errors: list[str] = []
    provenance_errors = validate_research_component_provenance_instrument(
        provenance_instrument
    )
    source_errors = validate_research_component_source_verification_instrument(
        source_verification_instrument
    )
    errors.extend(provenance_errors)
    errors.extend(source_errors)

    if isinstance(asset_set, dict):
        if asset_set.get("asset_set_id") != ASSET_SET_ID:
            errors.append(f"{prefix}: asset_set_id mismatch")
        if asset_set.get("asset_set_sha256") != ASSET_SET_SHA256:
            errors.append(f"{prefix}: asset_set_sha256 mismatch")
    else:
        errors.append(f"{prefix}: asset_set must be an object")

    if not provenance_errors and isinstance(provenance_instrument, dict):
        if provenance_instrument.get("asset_set_sha256") != ASSET_SET_SHA256:
            errors.append(f"{prefix}: provenance instrument does not bind asset set")
    if not source_errors and isinstance(source_verification_instrument, dict):
        if source_verification_instrument.get("asset_set_sha256") != ASSET_SET_SHA256:
            errors.append(f"{prefix}: source verification does not bind asset set")

    errors.extend(
        validate_frozen_research_component_tournament_subject(
            rights_instrument=rights_instrument,
            contamination_method=contamination_method,
            asset_set=asset_set,
            protocol=protocol,
            lineage_contract=lineage_contract,
        )
    )
    return sorted(set(errors))
