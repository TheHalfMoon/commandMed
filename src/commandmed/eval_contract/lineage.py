"""Fail-closed lineage validation and admission for commandMed Spec 003."""

from __future__ import annotations

import copy
import re
from typing import Any

from .canonical import compute_canonical_sha256
from .model import AccessClass, Purpose, VerificationStatus
from .validate import check_no_payload_markers

ASSET_CLASSES = frozenset({
    "DATASET_OR_CORPUS", "BENCHMARK_OR_EVALUATION_ASSET", "PRIVATE_GOLD_METADATA",
    "MODEL_OR_CHECKPOINT", "MODEL_GENERATED_OR_SYNTHETIC_ASSET",
    "EVIDENCE_OR_RETRIEVAL_SOURCE", "DERIVED_RESEARCH_ARTIFACT",
})
ADMISSION_STATES = frozenset({"ELIGIBLE", "REFERENCE_ONLY", "BLOCKED", "PROHIBITED"})
DECLARED_USES = frozenset({
    "REFERENCE", "DEVELOPMENT_EVALUATION", "PRIVATE_RELEASE_EVALUATION",
    "TRAINING_OR_ADAPTATION", "TEACHER_OR_SYNTHETIC_GENERATION",
    "RETRIEVAL_OR_EVIDENCE_USE", "MODIFICATION_OR_DERIVATION", "REDISTRIBUTION",
})
ARTIFACT_BINDING_STATES = frozenset({
    "DIRECT_DIGEST", "IMMUTABLE_REVISION_LOCATOR", "UNBOUND", "NOT_APPLICABLE",
})
RIGHTS_STATES = frozenset({"SUPPORTED", "CONDITIONAL", "UNRESOLVED", "INCOMPATIBLE"})
PRIVACY_STATES = frozenset({
    "NO_PHI_KNOWN", "DEIDENTIFIED", "RESTRICTED_OR_PHI", "UNRESOLVED", "NOT_APPLICABLE",
})
CONTAMINATION_STATES = frozenset({
    "NOT_ASSESSED", "PENDING", "ASSESSED_CLEAN", "OVERLAP_OR_HIGH_RISK", "BLOCKED", "NOT_APPLICABLE",
})
ORIGIN_TYPES = frozenset({"ORIGINAL", "DERIVED", "MODEL_GENERATED", "SYNTHETIC"})
QUARANTINE_STATES = frozenset({"NOT_QUARANTINED", "QUARANTINED", "PRIVATE_GOLD", "NOT_APPLICABLE"})

UNIVERSAL_REQUIRED_FIELDS = frozenset({
    "asset_id", "asset_class", "canonical_name", "record_version", "source_identifier",
    "source_uri", "source_revision", "source_verification_status", "source_evidence_uri",
    "declared_use", "access_class", "rights_state", "rights_evidence_uri", "artifact_binding_state",
})
EXACT_BINDING_REQUIRED_USES = frozenset(DECLARED_USES - {"REFERENCE"})
CLEAN_CONTAMINATION_REQUIRED_USES = frozenset({
    "TRAINING_OR_ADAPTATION", "TEACHER_OR_SYNTHETIC_GENERATION", "MODIFICATION_OR_DERIVATION",
})
PRIVATE_GOLD_PROHIBITED_USES = frozenset({
    "DEVELOPMENT_EVALUATION", "TRAINING_OR_ADAPTATION", "TEACHER_OR_SYNTHETIC_GENERATION",
    "RETRIEVAL_OR_EVIDENCE_USE", "MODIFICATION_OR_DERIVATION", "REDISTRIBUTION",
})
PURPOSE_ALLOWED_DECLARED_USES: dict[str, frozenset[str]] = {
    Purpose.TRAIN.value: frozenset({
        "TRAINING_OR_ADAPTATION", "TEACHER_OR_SYNTHETIC_GENERATION", "MODIFICATION_OR_DERIVATION",
    }),
    Purpose.DEV.value: frozenset({"DEVELOPMENT_EVALUATION"}),
    Purpose.CALIBRATION.value: frozenset({"DEVELOPMENT_EVALUATION"}),
    Purpose.CHECKPOINT_SELECTION.value: frozenset({"DEVELOPMENT_EVALUATION"}),
    Purpose.PUBLIC_EXTERNAL_EVAL.value: frozenset({"DEVELOPMENT_EVALUATION", "PRIVATE_RELEASE_EVALUATION"}),
    Purpose.PRIVATE_GOLD.value: frozenset({"PRIVATE_RELEASE_EVALUATION"}),
}

REQUIRED_INVARIANT_IDS = frozenset({
    "CONTRACT_MUST_VALIDATE_FIRST", "ADMISSION_IS_COMPUTED", "SOURCE_VERIFIED_NE_ARTIFACT_BOUND",
    "DIRECT_SHA256_BINDING_ALLOWED", "CRYPTO_REVISION_LOCATOR_BINDING_ALLOWED",
    "UNBOUND_EXACT_BYTE_USE_BLOCKED", "UNCLEAR_RIGHTS_BLOCK_USE", "PRIVATE_GOLD_QUARANTINED",
    "UNKNOWN_PRIVACY_FAILS_CLOSED", "UNRESOLVED_CONTAMINATION_BLOCKS_CLEAN_USE",
    "DERIVED_ASSETS_KEEP_PARENTS", "PURPOSE_USE_COMPATIBILITY_ENFORCED",
    "PARENT_RESTRICTIONS_PROPAGATE",
})
COMPUTED_OUTPUT_FIELDS = frozenset({
    "admission_state", "admission_reasons", "contract_sha256", "record_sha256", "scientific_record_identity",
})
AUDIT_ONLY_FIELDS = frozenset({
    "retrieval_timestamp", "verification_timestamp", "local_path", "reviewer_environment",
    "convenience_uri", "audit_notes",
})
HEX_SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")
CRYPTO_REVISION_RE = re.compile(r"^(?:[0-9a-fA-F]{40}|[0-9a-fA-F]{64})$")
UNBOUND_SENTINELS = frozenset({"", "NONE", "UNBOUND", "UNRESOLVED", "NOT_APPLICABLE"})
EXPECTED_CONTRACT_ID = "commandmed-lineage-contract-v1"
EXPECTED_SCHEMA_VERSION = "1.0"
EXPECTED_RECORD_VERSION = "1"
CONTROL_CHAR_RE = re.compile(r"[\x00-\x1f\x7f]")
DATA_LIKE_CLASSES = frozenset({
    "DATASET_OR_CORPUS", "BENCHMARK_OR_EVALUATION_ASSET", "PRIVATE_GOLD_METADATA",
})
DERIVED_CLASSES = frozenset({"MODEL_GENERATED_OR_SYNTHETIC_ASSET", "DERIVED_RESEARCH_ARTIFACT"})

_CONTRACT_SET_FIELDS: dict[str, frozenset[str]] = {
    "asset_classes": ASSET_CLASSES, "admission_states": ADMISSION_STATES, "declared_uses": DECLARED_USES,
    "artifact_binding_states": ARTIFACT_BINDING_STATES, "rights_states": RIGHTS_STATES,
    "privacy_states": PRIVACY_STATES, "contamination_states": CONTAMINATION_STATES,
    "origin_types": ORIGIN_TYPES, "quarantine_states": QUARANTINE_STATES,
    "universal_required_fields": UNIVERSAL_REQUIRED_FIELDS,
    "exact_binding_required_uses": EXACT_BINDING_REQUIRED_USES,
    "clean_contamination_required_uses": CLEAN_CONTAMINATION_REQUIRED_USES,
    "private_gold_prohibited_uses": PRIVATE_GOLD_PROHIBITED_USES,
}


def _normalized_string(value: Any) -> str | None:
    """Return a stripped non-empty string or ``None``."""
    if not isinstance(value, str):
        return None
    stripped = value.strip()
    return stripped if stripped else None


def _append_required_string_error(obj: dict[str, Any], field: str, prefix: str, errors: list[str]) -> str | None:
    """Validate one required non-empty string and append a deterministic error."""
    value = _normalized_string(obj.get(field))
    if value is None:
        errors.append(f"{prefix}: '{field}' must be a non-empty string")
    return value


def _validate_string_set_field(obj: dict[str, Any], field: str, expected: frozenset[str], prefix: str, errors: list[str]) -> None:
    """Require an exact duplicate-free closed-vocabulary list."""
    value = obj.get(field)
    if not isinstance(value, list) or not value:
        errors.append(f"{prefix}: '{field}' must be a non-empty list")
        return
    strings: list[str] = []
    for idx, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            errors.append(f"{prefix}: '{field}[{idx}]' must be a non-empty string")
        else:
            strings.append(item)
    if len(strings) != len(set(strings)):
        errors.append(f"{prefix}: '{field}' contains duplicate values")
    actual = set(strings)
    missing = sorted(set(expected) - actual)
    extra = sorted(actual - set(expected))
    if missing:
        errors.append(f"{prefix}: '{field}' is missing required values {missing}")
    if extra:
        errors.append(f"{prefix}: '{field}' contains unknown values {extra}")


def _validate_purpose_matrix(contract: dict[str, Any], prefix: str, errors: list[str]) -> None:
    """Require the canonical Purpose-to-declared-use authorization matrix exactly."""
    matrix = contract.get("purpose_allowed_declared_uses")
    if not isinstance(matrix, dict):
        errors.append(f"{prefix}: 'purpose_allowed_declared_uses' must be an object")
        return
    expected_keys = set(PURPOSE_ALLOWED_DECLARED_USES)
    actual_keys = set(matrix) if all(isinstance(key, str) for key in matrix) else set()
    if actual_keys != expected_keys:
        missing = sorted(expected_keys - actual_keys)
        extra = sorted(actual_keys - expected_keys)
        if missing:
            errors.append(f"{prefix}: purpose matrix missing purposes {missing}")
        if extra:
            errors.append(f"{prefix}: purpose matrix contains unknown purposes {extra}")
    for purpose, expected in PURPOSE_ALLOWED_DECLARED_USES.items():
        value = matrix.get(purpose)
        if not isinstance(value, list) or not value:
            errors.append(f"{prefix}: purpose matrix '{purpose}' must be a non-empty list")
            continue
        if any(not isinstance(item, str) or not item.strip() for item in value):
            errors.append(f"{prefix}: purpose matrix '{purpose}' contains invalid use values")
            continue
        if len(value) != len(set(value)):
            errors.append(f"{prefix}: purpose matrix '{purpose}' contains duplicate use values")
        actual = set(value)
        if actual != set(expected):
            errors.append(
                f"{prefix}: purpose matrix '{purpose}' must equal {sorted(expected)}, got {sorted(actual)}"
            )


def _contract_identity_projection(contract: dict[str, Any]) -> dict[str, Any]:
    """Return a representation-order-stable contract projection."""
    result = copy.deepcopy(contract)
    for field in _CONTRACT_SET_FIELDS:
        if isinstance(result.get(field), list):
            result[field] = sorted(result[field])
    matrix = result.get("purpose_allowed_declared_uses")
    if isinstance(matrix, dict):
        result["purpose_allowed_declared_uses"] = {
            key: sorted(value) if isinstance(value, list) else value for key, value in sorted(matrix.items())
        }
    invariants = result.get("invariants")
    if isinstance(invariants, list):
        normalized = [copy.deepcopy(item) for item in invariants]
        if all(isinstance(item, dict) for item in normalized):
            normalized.sort(key=lambda item: str(item.get("invariant_id", "")))
        result["invariants"] = normalized
    return result


def compute_lineage_contract_sha256(contract: dict[str, Any]) -> str:
    """Compute canonical SHA-256 for a validated lineage contract."""
    return compute_canonical_sha256(_contract_identity_projection(contract))


def validate_lineage_contract(contract: Any) -> list[str]:
    """Validate the Spec 003 contract before it can govern records."""
    prefix = "LineageContract"
    if not isinstance(contract, dict):
        return [f"{prefix}: contract must be a JSON object"]
    errors: list[str] = []
    contract_id = _append_required_string_error(contract, "contract_id", prefix, errors)
    schema_version = _append_required_string_error(contract, "schema_version", prefix, errors)
    if contract_id is not None and contract_id != EXPECTED_CONTRACT_ID:
        errors.append(f"{prefix}: unsupported contract_id '{contract_id}'; expected '{EXPECTED_CONTRACT_ID}'")
    if schema_version is not None and schema_version != EXPECTED_SCHEMA_VERSION:
        errors.append(f"{prefix}: unsupported schema_version '{schema_version}'; expected '{EXPECTED_SCHEMA_VERSION}'")
    for field, expected in _CONTRACT_SET_FIELDS.items():
        _validate_string_set_field(contract, field, expected, prefix, errors)
    _validate_purpose_matrix(contract, prefix, errors)

    invariants = contract.get("invariants")
    if not isinstance(invariants, list) or not invariants:
        errors.append(f"{prefix}: 'invariants' must be a non-empty list")
    else:
        ids: list[str] = []
        for idx, item in enumerate(invariants):
            item_prefix = f"{prefix}.invariants[{idx}]"
            if not isinstance(item, dict):
                errors.append(f"{item_prefix}: invariant must be an object")
                continue
            invariant_id = _append_required_string_error(item, "invariant_id", item_prefix, errors)
            if invariant_id is not None:
                ids.append(invariant_id)
            if item.get("required") is not True:
                errors.append(f"{item_prefix}: 'required' must be true")
            _append_required_string_error(item, "description", item_prefix, errors)
        if len(ids) != len(set(ids)):
            errors.append(f"{prefix}: duplicate invariant_id values are not allowed")
        actual_ids = set(ids)
        missing = sorted(REQUIRED_INVARIANT_IDS - actual_ids)
        extra = sorted(actual_ids - REQUIRED_INVARIANT_IDS)
        if missing:
            errors.append(f"{prefix}: missing required invariant IDs {missing}")
        if extra:
            errors.append(f"{prefix}: unknown invariant IDs {extra}")

    errors.extend(check_no_payload_markers(contract, "lineage_contract"))
    if not errors:
        try:
            digest = compute_lineage_contract_sha256(contract)
        except (TypeError, ValueError) as exc:
            errors.append(f"{prefix}: canonical identity computation failed: {exc}")
        else:
            if not HEX_SHA256_RE.fullmatch(digest):
                errors.append(f"{prefix}: canonical identity must be a SHA-256 hex digest")
    return errors


def _validate_parent_asset_ids(record: dict[str, Any], prefix: str, errors: list[str]) -> None:
    """Validate the local shape of parent asset references."""
    parents = record.get("parent_asset_ids")
    if not isinstance(parents, list) or not parents:
        errors.append(f"{prefix}: 'parent_asset_ids' must be a non-empty list")
        return
    valid: list[str] = []
    for idx, item in enumerate(parents):
        value = _normalized_string(item)
        if value is None:
            errors.append(f"{prefix}: 'parent_asset_ids[{idx}]' must be a non-empty string")
        else:
            valid.append(value)
    if len(valid) != len(set(valid)):
        errors.append(f"{prefix}: 'parent_asset_ids' contains duplicate values")


def validate_lineage_record(record: Any, contract: Any) -> list[str]:
    """Validate one evidence record without trusting computed admission or identity fields."""
    contract_errors = validate_lineage_contract(contract)
    if contract_errors:
        return [f"Invalid contract: {error}" for error in contract_errors]
    prefix = "LineageRecord"
    if not isinstance(record, dict):
        return [f"{prefix}: record must be a JSON object"]
    errors: list[str] = []
    errors.extend(check_no_payload_markers(record, "lineage_record"))
    for field in COMPUTED_OUTPUT_FIELDS:
        if field in record:
            errors.append(f"{prefix}: computed output field '{field}' is not accepted as evidence input")
    for field in sorted(UNIVERSAL_REQUIRED_FIELDS):
        _append_required_string_error(record, field, prefix, errors)

    asset_id = _normalized_string(record.get("asset_id"))
    if asset_id is not None:
        prefix = f"LineageRecord({asset_id})"
    if record.get("record_version") != EXPECTED_RECORD_VERSION:
        errors.append(f"{prefix}: unsupported record_version '{record.get('record_version')}'; expected '{EXPECTED_RECORD_VERSION}'")

    asset_class = record.get("asset_class")
    declared_use = record.get("declared_use")
    verification = record.get("source_verification_status")
    access = record.get("access_class")
    rights_state = record.get("rights_state")
    binding = record.get("artifact_binding_state")
    if asset_class not in ASSET_CLASSES:
        errors.append(f"{prefix}: invalid asset_class '{asset_class}'")
    if declared_use not in DECLARED_USES:
        errors.append(f"{prefix}: invalid declared_use '{declared_use}'")
    if verification not in {e.value for e in VerificationStatus}:
        errors.append(f"{prefix}: invalid source_verification_status '{verification}'")
    if access not in {e.value for e in AccessClass}:
        errors.append(f"{prefix}: invalid access_class '{access}'")
    if rights_state not in RIGHTS_STATES:
        errors.append(f"{prefix}: invalid rights_state '{rights_state}'")

    if binding not in ARTIFACT_BINDING_STATES:
        errors.append(f"{prefix}: invalid artifact_binding_state '{binding}'")
    elif binding == "DIRECT_DIGEST":
        digest = _normalized_string(record.get("content_sha256"))
        if digest is None or not HEX_SHA256_RE.fullmatch(digest):
            errors.append(f"{prefix}: DIRECT_DIGEST requires 'content_sha256' as exactly 64 hex characters")
    elif binding == "IMMUTABLE_REVISION_LOCATOR":
        revision = _normalized_string(record.get("source_revision"))
        locator = _normalized_string(record.get("artifact_locator"))
        evidence = _normalized_string(record.get("source_evidence_uri"))
        if revision is None or not CRYPTO_REVISION_RE.fullmatch(revision):
            errors.append(f"{prefix}: IMMUTABLE_REVISION_LOCATOR requires a 40- or 64-hex content-addressed source_revision")
        if locator is None or locator.upper() in UNBOUND_SENTINELS:
            errors.append(f"{prefix}: IMMUTABLE_REVISION_LOCATOR requires an exact 'artifact_locator'")
        if evidence is None or evidence.upper() in UNBOUND_SENTINELS:
            errors.append(f"{prefix}: IMMUTABLE_REVISION_LOCATOR requires resolved 'source_evidence_uri'")

    if rights_state == "SUPPORTED":
        evidence = _normalized_string(record.get("rights_evidence_uri"))
        if evidence is None or evidence.upper() in UNBOUND_SENTINELS:
            errors.append(f"{prefix}: rights_state SUPPORTED requires resolved 'rights_evidence_uri'")

    privacy_state = record.get("phi_privacy_state")
    if "phi_privacy_state" in record and privacy_state not in PRIVACY_STATES:
        errors.append(f"{prefix}: invalid phi_privacy_state '{privacy_state}'")
    if isinstance(declared_use, str) and declared_use != "REFERENCE" and privacy_state not in PRIVACY_STATES:
        errors.append(f"{prefix}: non-reference declared use requires 'phi_privacy_state' in {sorted(PRIVACY_STATES)}")

    purpose = record.get("purpose")
    quarantine_state = record.get("quarantine_state")
    contamination_state = record.get("contamination_state")
    origin_type = record.get("origin_type")
    if "purpose" in record and purpose not in {e.value for e in Purpose}:
        errors.append(f"{prefix}: invalid purpose '{purpose}'")
    if "quarantine_state" in record and quarantine_state not in QUARANTINE_STATES:
        errors.append(f"{prefix}: invalid quarantine_state '{quarantine_state}'")
    if "contamination_state" in record and contamination_state not in CONTAMINATION_STATES:
        errors.append(f"{prefix}: invalid contamination_state '{contamination_state}'")
    if "origin_type" in record and origin_type not in ORIGIN_TYPES:
        errors.append(f"{prefix}: invalid origin_type '{origin_type}'")
    if "parent_asset_ids" in record:
        _validate_parent_asset_ids(record, prefix, errors)

    if "content_sha256" in record:
        content_sha = _normalized_string(record.get("content_sha256"))
        if content_sha is None or not HEX_SHA256_RE.fullmatch(content_sha):
            errors.append(f"{prefix}: supplied 'content_sha256' must be exactly 64 hex characters")
    if "artifact_locator" in record and _normalized_string(record.get("artifact_locator")) is None:
        errors.append(f"{prefix}: supplied 'artifact_locator' must be a non-empty string")
    for evidence_field in ("spdx_license_expression", "custom_terms_id"):
        if evidence_field in record:
            evidence_value = _normalized_string(record.get(evidence_field))
            if evidence_value is None:
                errors.append(f"{prefix}: supplied '{evidence_field}' must be a non-empty string")
            elif len(evidence_value) > 512 or CONTROL_CHAR_RE.search(evidence_value):
                errors.append(f"{prefix}: supplied '{evidence_field}' contains unsafe/control content")

    if asset_class in DATA_LIKE_CLASSES and declared_use != "REFERENCE":
        if purpose not in {e.value for e in Purpose}:
            errors.append(f"{prefix}: data/evaluation non-reference use requires canonical Spec 001 'purpose'")
        if quarantine_state not in QUARANTINE_STATES:
            errors.append(f"{prefix}: data/evaluation non-reference use requires valid 'quarantine_state'")
        if purpose == Purpose.PRIVATE_GOLD.value and quarantine_state != "PRIVATE_GOLD":
            errors.append(f"{prefix}: purpose='PRIVATE_GOLD' requires quarantine_state='PRIVATE_GOLD'")
        if quarantine_state == "PRIVATE_GOLD" and purpose != Purpose.PRIVATE_GOLD.value:
            errors.append(f"{prefix}: quarantine_state='PRIVATE_GOLD' requires purpose='PRIVATE_GOLD'")

    if asset_class == "PRIVATE_GOLD_METADATA":
        if purpose != Purpose.PRIVATE_GOLD.value:
            errors.append(f"{prefix}: PRIVATE_GOLD_METADATA requires purpose='PRIVATE_GOLD'")
        if quarantine_state != "PRIVATE_GOLD":
            errors.append(f"{prefix}: PRIVATE_GOLD_METADATA requires quarantine_state='PRIVATE_GOLD'")

    if isinstance(declared_use, str) and declared_use in CLEAN_CONTAMINATION_REQUIRED_USES:
        if contamination_state not in CONTAMINATION_STATES:
            errors.append(f"{prefix}: declared use '{declared_use}' requires a valid 'contamination_state'")

    if asset_class in DERIVED_CLASSES:
        if "parent_asset_ids" not in record:
            errors.append(f"{prefix}: derived/synthetic asset requires 'parent_asset_ids'")
        if origin_type not in ORIGIN_TYPES:
            errors.append(f"{prefix}: derived/synthetic asset requires valid 'origin_type'")
        if asset_class == "MODEL_GENERATED_OR_SYNTHETIC_ASSET":
            _append_required_string_error(record, "generator_identity", prefix, errors)
            _append_required_string_error(record, "generation_config_id", prefix, errors)
        if asset_class == "DERIVED_RESEARCH_ARTIFACT" and origin_type not in {None, "DERIVED"}:
            errors.append(f"{prefix}: DERIVED_RESEARCH_ARTIFACT requires origin_type='DERIVED'")
        if declared_use == "TRAINING_OR_ADAPTATION":
            output_evidence = _normalized_string(record.get("output_use_evidence_uri"))
            if output_evidence is None or output_evidence.upper() in UNBOUND_SENTINELS:
                errors.append(f"{prefix}: training/adaptation of generated or derived output requires resolved 'output_use_evidence_uri'")
    return errors


def _registry_index(records: list[Any]) -> dict[str, dict[str, Any]]:
    """Build a stable ID index from structurally validated records."""
    result: dict[str, dict[str, Any]] = {}
    for record in records:
        if isinstance(record, dict):
            asset_id = _normalized_string(record.get("asset_id"))
            if asset_id is not None and asset_id not in result:
                result[asset_id] = record
    return result


def _find_parent_cycle(index: dict[str, dict[str, Any]]) -> str | None:
    """Return one asset ID participating in a parent cycle, if any."""
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(asset_id: str) -> str | None:
        """Depth-first search one lineage branch for cycles."""
        if asset_id in visiting:
            return asset_id
        if asset_id in visited:
            return None
        visiting.add(asset_id)
        record = index.get(asset_id, {})
        parents = record.get("parent_asset_ids", [])
        if isinstance(parents, list):
            for parent in parents:
                if isinstance(parent, str) and parent in index:
                    found = visit(parent)
                    if found is not None:
                        return found
        visiting.remove(asset_id)
        visited.add(asset_id)
        return None

    for asset_id in index:
        found = visit(asset_id)
        if found is not None:
            return found
    return None


def validate_lineage_registry(records: Any, contract: Any) -> tuple[bool, list[str]]:
    """Validate records, stable IDs, parent resolution, and acyclic parent lineage."""
    contract_errors = validate_lineage_contract(contract)
    if contract_errors:
        return False, [f"Invalid contract: {error}" for error in contract_errors]
    if not isinstance(records, list) or not records:
        return False, ["LineageRegistry: registry must be a non-empty list"]
    errors: list[str] = []
    seen: set[str] = set()
    for idx, record in enumerate(records):
        errors.extend([f"Record[{idx}]: {error}" for error in validate_lineage_record(record, contract)])
        if isinstance(record, dict):
            asset_id = _normalized_string(record.get("asset_id"))
            if asset_id is not None:
                if asset_id in seen:
                    errors.append(f"LineageRegistry: duplicate asset_id '{asset_id}'")
                seen.add(asset_id)
    index = _registry_index(records)
    for asset_id, record in index.items():
        parents = record.get("parent_asset_ids")
        if not isinstance(parents, list):
            continue
        for parent in parents:
            if not isinstance(parent, str) or not parent.strip():
                continue
            if parent == asset_id:
                errors.append(f"LineageRegistry: asset_id '{asset_id}' cannot be its own parent")
            elif parent not in index:
                errors.append(f"LineageRegistry: parent_asset_id '{parent}' referenced by '{asset_id}' is unresolved")
    if not errors:
        cycle = _find_parent_cycle(index)
        if cycle is not None:
            errors.append(f"LineageRegistry: parent lineage cycle detected at '{cycle}'")
    return len(errors) == 0, errors


def lineage_scientific_identity_projection(record: dict[str, Any]) -> dict[str, Any]:
    """Project validated evidence onto scientific identity-bearing fields."""
    result: dict[str, Any] = {}
    for key, value in record.items():
        if key in AUDIT_ONLY_FIELDS or key in COMPUTED_OUTPUT_FIELDS:
            continue
        normalized = copy.deepcopy(value)
        if key == "parent_asset_ids" and isinstance(normalized, list):
            normalized = sorted(normalized)
        elif key in {"content_sha256", "source_revision"} and isinstance(normalized, str):
            if re.fullmatch(r"[0-9a-fA-F]{40}|[0-9a-fA-F]{64}", normalized):
                normalized = normalized.lower()
        result[key] = normalized
    return result


def compute_lineage_record_sha256(record: dict[str, Any]) -> str:
    """Compute the scientific identity for a validated lineage evidence record."""
    return compute_canonical_sha256(lineage_scientific_identity_projection(record))


def _admission_result(state: str, reasons: set[str], contract_sha256: str | None, record_sha256: str | None) -> dict[str, Any]:
    """Build a deterministic admission result envelope."""
    return {
        "state": state,
        "reason_codes": sorted(reasons),
        "contract_sha256": contract_sha256,
        "record_sha256": record_sha256,
    }


def _evaluate_base_admission(record: dict[str, Any], contract_sha: str, record_sha: str) -> dict[str, Any]:
    """Evaluate one record without considering parent records."""
    declared_use = str(record["declared_use"])
    reasons: set[str] = set()

    if record["source_verification_status"] == VerificationStatus.EXCLUDED.value:
        reasons.add("SOURCE_EXCLUDED")
    if record["rights_state"] == "INCOMPATIBLE":
        reasons.add("RIGHTS_INCOMPATIBLE")
    if record.get("phi_privacy_state") == "RESTRICTED_OR_PHI" and declared_use in {
        "TRAINING_OR_ADAPTATION", "TEACHER_OR_SYNTHETIC_GENERATION", "MODIFICATION_OR_DERIVATION", "REDISTRIBUTION",
    }:
        reasons.add("RESTRICTED_OR_PHI")
    purpose = record.get("purpose")
    if purpose == Purpose.PRIVATE_GOLD.value and declared_use in PRIVATE_GOLD_PROHIBITED_USES:
        reasons.add("PRIVATE_GOLD_PROHIBITED_USE")
    if record.get("quarantine_state") == "QUARANTINED" and declared_use != "REFERENCE":
        reasons.add("QUARANTINE_CONFLICT")
    if purpose in PURPOSE_ALLOWED_DECLARED_USES and declared_use != "REFERENCE":
        if declared_use not in PURPOSE_ALLOWED_DECLARED_USES[purpose]:
            reasons.add("PURPOSE_USE_INCOMPATIBLE")
    if declared_use in CLEAN_CONTAMINATION_REQUIRED_USES and record.get("contamination_state") == "OVERLAP_OR_HIGH_RISK":
        reasons.add("CONTAMINATION_HIGH_RISK")
    if reasons:
        return _admission_result("PROHIBITED", reasons, contract_sha, record_sha)

    if record["source_verification_status"] != VerificationStatus.VERIFIED.value:
        reasons.add("SOURCE_UNVERIFIED")
    if record["rights_state"] in {"CONDITIONAL", "UNRESOLVED"}:
        reasons.add("RIGHTS_UNRESOLVED")
    if declared_use != "REFERENCE":
        privacy = record.get("phi_privacy_state")
        if privacy == "UNRESOLVED":
            reasons.add("PRIVACY_UNRESOLVED")
        elif privacy == "RESTRICTED_OR_PHI":
            reasons.add("RESTRICTED_OR_PHI")
    if declared_use in CLEAN_CONTAMINATION_REQUIRED_USES:
        contamination = record.get("contamination_state")
        if contamination not in {"ASSESSED_CLEAN", "NOT_APPLICABLE"}:
            reasons.add("CONTAMINATION_UNRESOLVED")
    if reasons:
        return _admission_result("BLOCKED", reasons, contract_sha, record_sha)

    if record["access_class"] == AccessClass.REFERENCE_ONLY.value and declared_use != "REFERENCE":
        reasons.add("ACCESS_REFERENCE_ONLY")
    if declared_use in EXACT_BINDING_REQUIRED_USES and record["artifact_binding_state"] in {"UNBOUND", "NOT_APPLICABLE"}:
        reasons.add("ARTIFACT_UNBOUND")
    if reasons:
        return _admission_result("REFERENCE_ONLY", reasons, contract_sha, record_sha)
    return _admission_result("ELIGIBLE", set(), contract_sha, record_sha)


def _evaluate_with_parents(
    record: dict[str, Any],
    contract: dict[str, Any],
    contract_sha: str,
    registry_index: dict[str, dict[str, Any]] | None,
    visiting: frozenset[str],
) -> dict[str, Any]:
    """Evaluate one record and propagate exact-use restrictions from resolved parents."""
    record_sha = compute_lineage_record_sha256(record)
    base = _evaluate_base_admission(record, contract_sha, record_sha)
    if base["state"] != "ELIGIBLE":
        return base

    parents = record.get("parent_asset_ids")
    if not isinstance(parents, list) or not parents:
        return base
    if registry_index is None:
        return _admission_result("BLOCKED", {"PARENT_REGISTRY_REQUIRED"}, contract_sha, record_sha)

    child_id = str(record.get("asset_id", ""))
    next_visiting = visiting | {child_id}
    for parent_id in sorted(str(item) for item in parents):
        if parent_id in next_visiting:
            return _admission_result("BLOCKED", {"PARENT_LINEAGE_CYCLE"}, contract_sha, record_sha)
        parent = registry_index.get(parent_id)
        if parent is None:
            return _admission_result("BLOCKED", {"PARENT_UNRESOLVED"}, contract_sha, record_sha)
        if parent.get("declared_use") != record.get("declared_use"):
            return _admission_result("BLOCKED", {"PARENT_USE_EVIDENCE_MISMATCH"}, contract_sha, record_sha)
        parent_errors = validate_lineage_record(parent, contract)
        if parent_errors:
            return _admission_result("BLOCKED", {"PARENT_RECORD_INVALID"}, contract_sha, record_sha)
        parent_result = _evaluate_with_parents(parent, contract, contract_sha, registry_index, next_visiting)
        parent_state = parent_result["state"]
        if parent_state == "PROHIBITED":
            return _admission_result("PROHIBITED", {"PARENT_PROHIBITED"}, contract_sha, record_sha)
        if parent_state == "REFERENCE_ONLY":
            return _admission_result("BLOCKED", {"PARENT_REFERENCE_ONLY"}, contract_sha, record_sha)
        if parent_state != "ELIGIBLE":
            return _admission_result("BLOCKED", {"PARENT_BLOCKED"}, contract_sha, record_sha)
    return base


def evaluate_lineage_admission(record: Any, contract: Any, registry: Any = None) -> dict[str, Any]:
    """Compute admission for the exact declared use, including resolved parent restrictions."""
    contract_errors = validate_lineage_contract(contract)
    if contract_errors:
        return _admission_result("BLOCKED", {"INVALID_CONTRACT"}, None, None)
    assert isinstance(contract, dict)
    contract_sha = compute_lineage_contract_sha256(contract)
    record_errors = validate_lineage_record(record, contract)
    if record_errors:
        return _admission_result("BLOCKED", {"INVALID_RECORD"}, contract_sha, None)
    assert isinstance(record, dict)

    registry_index: dict[str, dict[str, Any]] | None = None
    if record.get("parent_asset_ids"):
        if registry is None:
            return _admission_result(
                "BLOCKED", {"PARENT_REGISTRY_REQUIRED"}, contract_sha, compute_lineage_record_sha256(record)
            )
        valid, registry_errors = validate_lineage_registry(registry, contract)
        if not valid or registry_errors:
            return _admission_result(
                "BLOCKED", {"PARENT_REGISTRY_INVALID"}, contract_sha, compute_lineage_record_sha256(record)
            )
        assert isinstance(registry, list)
        registry_index = _registry_index(registry)

    return _evaluate_with_parents(record, contract, contract_sha, registry_index, frozenset())
