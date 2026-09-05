"""Final deterministic qualification boundary for SP007-RO-001 evaluation assets.

This module binds the canonical Founder Decision B record and a deliberately
narrow privacy classification to the existing rights, provenance, quarantine,
contamination, Spec003 admission, and protocol-freeze validators. It performs no
model loading, inference, device access, training, protected-data access, winner
selection, network access, or spend.
"""

from __future__ import annotations

import re
from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.foundation import is_canonical_sha256, validate_closed_object
from src.commandmed.spec007.research_scope import RESEARCH_COMPONENT_SCOPE_ID
from src.commandmed.spec007.research_tournament_asset_evidence import (
    ASSET_SET_SHA256,
    validate_frozen_research_component_evaluation_package,
)
from src.commandmed.spec007.research_tournament_assets import ASSET_SET_ID

FOUNDER_DECISION_TOKEN = (
    "FOUNDER_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION="
    "E004_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION_B"
)
DECISION_PATH = (
    "specs/007-sft-v1/"
    "e004-research-component-evaluation-qualification-founder-decision-2026-09-05.md"
)
PRIVACY_INSTRUMENT_ID = "E004_RESEARCH_COMPONENT_DECLARED_SYNTHETIC_NONPHI_PRIVACY_V1"
PRIVACY_INSTRUMENT_SHA256 = (
    "52301182ca6b4b7e07a8a2442cc8168c313f81e11fb47b2ca62f725cb6156f1f"
)

_REQUIRED_DECISION_LINES = frozenset(
    {
        FOUNDER_DECISION_TOKEN,
        "RESEARCH_COMPONENT_EVAL_ASSET_CONSTRUCTION_AUTHORITY=AUTHORIZED_EXACT_DECLARED_SET_ONLY",
        "RESEARCH_COMPONENT_EVAL_RIGHTS_EVALUATION_AUTHORITY=AUTHORIZED_PROJECT_AUTHORED_INTERNAL_SELECTION_ONLY",
        "RESEARCH_COMPONENT_EVAL_PROVENANCE_VERIFICATION_AUTHORITY=AUTHORIZED_EXACT_DECLARED_SET_ONLY",
        "RESEARCH_COMPONENT_EVAL_PRIVACY_CLASSIFICATION_AUTHORITY=AUTHORIZED_EXACT_DECLARED_FIXTURES_ONLY_NO_EXTERNAL_PROVIDER",
        "RESEARCH_COMPONENT_EVAL_QUARANTINE_EVIDENCE_AUTHORITY=AUTHORIZED_EXACT_DECLARED_SET_CHECKPOINT_SELECTION_ONLY",
        "RESEARCH_COMPONENT_EVAL_CONTAMINATION_ASSESSMENT_AUTHORITY=AUTHORIZED_EXACT_DECLARED_SET_NONEXPOSURE_METHOD_ONLY",
        "RESEARCH_COMPONENT_EVAL_SPEC003_ADMISSION_AUTHORITY=AUTHORIZED_EXACT_DECLARED_SET_EVALUATOR_ONLY",
        "RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_FREEZE_AUTHORITY=AUTHORIZED_ONLY_IF_ALL_EXACT_ASSET_GATES_PASS",
        "CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED",
        "CURRENT_AUTHORIZED_SPEND_USD=0",
        "TRAINING_AUTHORITY=NONE",
    }
)

_PRIVACY_FIELDS = (
    "schema_version",
    "instrument_id",
    "instrument_sha256",
    "scope_id",
    "asset_set_id",
    "asset_set_sha256",
    "classification_subject",
    "classification_method",
    "classification_semantics",
    "external_provider_used",
    "external_payloads_used",
    "private_gold_present",
    "raw_external_records_present",
    "phi_present",
    "pii_present",
    "general_phi_detection_claim",
    "semantic_reidentification_risk_claim",
    "required_asset_count",
    "current_authorized_spend_usd",
)

_FORBIDDEN_DIRECT_IDENTIFIER_KEYS = frozenset(
    {
        "user_id",
        "patient_id",
        "person_id",
        "medical_record_number",
        "mrn",
        "email",
        "email_address",
        "phone",
        "phone_number",
        "address",
        "street_address",
        "date_of_birth",
        "dob",
        "person_name",
        "patient_name",
    }
)
_EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
_PHONE_RE = re.compile(r"(?<![A-Za-z0-9])\+?\d[\d\s().-]{8,}\d(?![A-Za-z0-9])")
_SSN_RE = re.compile(r"(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)")
_EXPLICIT_IDENTIFIER_LABEL_RE = re.compile(
    r"(?i)\b(?:patient[_ -]?id|user[_ -]?id|medical record number|mrn|"
    r"date of birth|phone number|email address|street address)\b"
)


def _privacy_self_hash(record: Mapping[str, Any]) -> str:
    projection = dict(record)
    projection.pop("instrument_sha256", None)
    return compute_canonical_sha256(projection)


def validate_founder_eval_qualification_decision(decision_text: Any) -> list[str]:
    prefix = "ResearchComponentEvaluationFounderDecision"
    if not isinstance(decision_text, str) or not decision_text.strip():
        return [f"{prefix}: decision text must be non-empty"]
    present = {line.strip() for line in decision_text.splitlines()}
    missing = sorted(_REQUIRED_DECISION_LINES - present)
    return [f"{prefix}: missing exact line {line}" for line in missing]


def validate_research_component_privacy_instrument(record: Any) -> list[str]:
    prefix = "ResearchComponentEvaluationPrivacyInstrument"
    errors = validate_closed_object(record, required_fields=_PRIVACY_FIELDS, field=prefix)
    if errors or not isinstance(record, dict):
        return errors
    expected = {
        "schema_version": "1",
        "instrument_id": PRIVACY_INSTRUMENT_ID,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "asset_set_id": ASSET_SET_ID,
        "asset_set_sha256": ASSET_SET_SHA256,
        "classification_subject": "EXACT_DECLARED_PROJECT_AUTHORED_SYNTHETIC_FIXTURES_ONLY",
        "classification_method": "STRUCTURAL_DIRECT_IDENTIFIER_PATTERN_SCAN_V1",
        "classification_semantics": (
            "NO_EXPLICIT_DIRECT_IDENTIFIERS_OR_EXTERNAL_RECORD_PAYLOADS_IN_EXACT_FIXTURE_BYTES_ONLY"
        ),
        "external_provider_used": False,
        "external_payloads_used": False,
        "private_gold_present": False,
        "raw_external_records_present": False,
        "phi_present": False,
        "pii_present": False,
        "general_phi_detection_claim": False,
        "semantic_reidentification_risk_claim": False,
        "required_asset_count": 7,
        "current_authorized_spend_usd": 0,
    }
    for field, value in expected.items():
        if record.get(field) != value:
            errors.append(f"{prefix}: {field} mismatch")
    claimed = record.get("instrument_sha256")
    if not is_canonical_sha256(claimed):
        errors.append(f"{prefix}: instrument_sha256 must be lowercase sha256 hex")
    elif claimed != _privacy_self_hash(record):
        errors.append(f"{prefix}: instrument_sha256 mismatch")
    if claimed != PRIVACY_INSTRUMENT_SHA256:
        errors.append(f"{prefix}: canonical instrument identity mismatch")
    return sorted(set(errors))


def _scan_direct_identifiers(value: Any, path: str = "$" ) -> list[str]:
    errors: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key).strip().lower()
            child_path = f"{path}.{key}"
            if key_text in _FORBIDDEN_DIRECT_IDENTIFIER_KEYS:
                errors.append(f"PrivacyFixtureScan: prohibited direct-identifier field {child_path}")
            errors.extend(_scan_direct_identifiers(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            errors.extend(_scan_direct_identifiers(child, f"{path}[{index}]"))
    elif isinstance(value, str):
        if _EMAIL_RE.search(value):
            errors.append(f"PrivacyFixtureScan: email-like direct identifier at {path}")
        if _PHONE_RE.search(value):
            errors.append(f"PrivacyFixtureScan: phone-like direct identifier at {path}")
        if _SSN_RE.search(value):
            errors.append(f"PrivacyFixtureScan: SSN-like direct identifier at {path}")
        if _EXPLICIT_IDENTIFIER_LABEL_RE.search(value):
            errors.append(f"PrivacyFixtureScan: explicit identifier label at {path}")
    return errors


def validate_research_component_fixture_privacy(asset_set: Any) -> list[str]:
    prefix = "ResearchComponentEvaluationFixturePrivacy"
    if not isinstance(asset_set, dict):
        return [f"{prefix}: asset_set must be an object"]
    errors: list[str] = []
    if asset_set.get("asset_set_id") != ASSET_SET_ID:
        errors.append(f"{prefix}: asset_set_id mismatch")
    if asset_set.get("asset_set_sha256") != ASSET_SET_SHA256:
        errors.append(f"{prefix}: asset_set_sha256 mismatch")
    assets = asset_set.get("asset_records")
    if not isinstance(assets, list) or len(assets) != 7:
        errors.append(f"{prefix}: asset_records must contain exactly 7 assets")
    errors.extend(_scan_direct_identifiers(asset_set))
    return sorted(set(errors))


def validate_qualified_research_component_evaluation_package(
    *,
    founder_decision_text: Any,
    privacy_instrument: Any,
    provenance_instrument: Any,
    source_verification_instrument: Any,
    rights_instrument: Any,
    contamination_method: Any,
    asset_set: Any,
    protocol: Any,
    lineage_contract: Any,
) -> list[str]:
    """Validate the post-Decision-B pre-result qualification package fail closed."""
    errors: list[str] = []
    decision_errors = validate_founder_eval_qualification_decision(founder_decision_text)
    privacy_errors = validate_research_component_privacy_instrument(privacy_instrument)
    fixture_privacy_errors = validate_research_component_fixture_privacy(asset_set)
    errors.extend(decision_errors)
    errors.extend(privacy_errors)
    errors.extend(fixture_privacy_errors)
    errors.extend(
        validate_frozen_research_component_evaluation_package(
            provenance_instrument=provenance_instrument,
            source_verification_instrument=source_verification_instrument,
            rights_instrument=rights_instrument,
            contamination_method=contamination_method,
            asset_set=asset_set,
            protocol=protocol,
            lineage_contract=lineage_contract,
        )
    )
    return sorted(set(errors))
