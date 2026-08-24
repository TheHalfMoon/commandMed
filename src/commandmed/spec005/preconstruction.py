"""Spec 005 preconstruction evidence and source governance (A5-A12).

Deterministic, fail-closed validators for source routes, metadata-only case
provenance, review bindings, contamination plans, change control and the
A1-A14 preconstruction snapshot. No payload text is accepted; no contamination
assessment is executed; no real construction activation is created.
"""

from __future__ import annotations

from typing import Any

REQUIRED_SNAPSHOT_GATES = (
    "R1",
    "T1",
    "D34",
    "G1",
    "G2",
    "G3",
    "G4",
    "S1",
    "P1",
    "C1",
    "H1",
    "I1",
    "F1",
)

PROHIBITED_ROUTE_CLASSES = frozenset(
    {"MODEL_OR_PROVIDER_GENERATED", "PROHIBITED_OR_BLOCKED_SOURCE"}
)
DERIVED_ROUTE_CLASSES = frozenset(
    {"PUBLIC_DEV_DERIVED", "AUTHORIZED_INTERNAL_DERIVED"}
)
ALLOWED_REVIEW_DISPOSITIONS = frozenset(
    {"ACCEPTED", "REJECTED", "ESCALATED_FOR_ADJUDICATION"}
)
PRIVATE_GOLD_MARKERS = ("COMMANDMED_ARABIC_GOLD", "PRIVATE_GOLD")


def _require_fields(record: Any, fields, prefix: str, errors: list[str]) -> None:
    if not isinstance(record, dict):
        errors.append(f"{prefix}:MALFORMED_RECORD_NOT_OBJECT")
        return
    for field in fields:
        value = record.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            errors.append(f"{prefix}:{field}_MISSING")


def _contains_private_gold(value: Any) -> bool:
    if isinstance(value, str):
        return any(marker in value for marker in PRIVATE_GOLD_MARKERS)
    if isinstance(value, dict):
        return any(
            _contains_private_gold(k) or _contains_private_gold(v)
            for k, v in value.items()
        )
    if isinstance(value, (list, tuple, set)):
        return any(_contains_private_gold(item) for item in value)
    return False


def _guard_contract(contract: Any, prefix: str, errors: list[str]) -> bool:
    """Fail closed when the governing contract itself is malformed."""
    if not isinstance(contract, dict):
        errors.append(f"{prefix}:GOVERNING_CONTRACT_MALFORMED")
        return False
    return True


def _contract_vocab(contract: Any, key: str) -> set:
    if not isinstance(contract, dict):
        return set()
    value = contract.get(key)
    return set(value) if isinstance(value, list) else set()


def validate_preconstruction_contract(contract: Any) -> list[str]:
    """Validate closed vocabularies, invariants and the frozen dependency DAG."""
    errors: list[str] = []
    if not isinstance(contract, dict):
        return ["PreconstructionContract:MALFORMED_RECORD_NOT_OBJECT"]

    for key in (
        "source_route_classes",
        "snapshot_readiness_states",
        "invariants",
    ):
        if not isinstance(contract.get(key), list) or not contract[key]:
            errors.append(f"PreconstructionContract:{key}_MISSING")

    readiness_states = contract.get("snapshot_readiness_states") or []
    if isinstance(readiness_states, list) and contract.get(
        "prohibited_snapshot_state"
    ) in readiness_states:
        errors.append(
            "PreconstructionContract:PROHIBITED_STATE_"
            f"{contract.get('prohibited_snapshot_state')}_IN_READINESS_VOCABULARY"
        )

    dag = contract.get("preconstruction_dependency_dag")
    if not isinstance(dag, dict) or not dag.get("edges"):
        errors.append("PreconstructionContract:PRECONSTRUCTION_DEPENDENCY_DAG_MISSING")
    return errors


def validate_source_route(record: Any, contract: Any) -> list[str]:
    """Validate one A10 exact source-route record for selection development."""
    errors: list[str] = []
    if not _guard_contract(contract, "SourceRoute", errors):
        return errors
    _require_fields(
        record,
        (
            "source_route_record_id",
            "route_class",
            "lineage_record_id",
            "lineage_record_sha256",
            "parent_asset_ids",
            "rights_evidence_id",
            "privacy_evidence_id",
            "declared_use",
            "purpose",
            "record_canonical_sha256",
        ),
        "SourceRoute",
        errors,
    )
    if not isinstance(record, dict):
        return errors

    route_class = record.get("route_class")
    allowed_classes = _contract_vocab(contract, "source_route_classes")
    if route_class not in allowed_classes:
        errors.append(f"SourceRoute:UNKNOWN_ROUTE_CLASS_{route_class}")
    if route_class in PROHIBITED_ROUTE_CLASSES:
        errors.append(f"SourceRoute:ROUTE_CLASS_PROHIBITED_FOR_SELECTION_{route_class}")

    if record.get("declared_use") != "DEVELOPMENT_EVALUATION":
        errors.append("SourceRoute:DECLARED_USE_MUST_BE_DEVELOPMENT_EVALUATION")
    if record.get("purpose") != "CHECKPOINT_SELECTION":
        errors.append("SourceRoute:PURPOSE_MUST_BE_CHECKPOINT_SELECTION")

    parents_raw = record.get("parent_asset_ids")
    # Scan the raw supplied value so hidden Gold markers cannot hide behind
    # a type violation.
    if _contains_private_gold(parents_raw):
        errors.append("SourceRoute:PRIVATE_GOLD_CANNOT_BE_PARENT_OR_SOURCE")
    parents = parents_raw
    if parents is not None and not isinstance(parents, list):
        errors.append("SourceRoute:PARENT_ASSET_IDS_MUST_BE_LIST_OF_STRINGS")
        parents = []
    elif isinstance(parents, list) and any(not isinstance(item, str) for item in parents):
        errors.append("SourceRoute:PARENT_ASSET_IDS_MUST_BE_LIST_OF_STRINGS")
    if route_class in DERIVED_ROUTE_CLASSES and not parents:
        errors.append("SourceRoute:DERIVED_ROUTE_REQUIRES_PARENT_ASSET_IDS")
    return errors


PAYLOAD_FIELD_MARKERS = (
    "case_text",
    "answer",
    "rubric",
    "content_body",
)
PAYLOAD_FIELD_SUFFIX = "_text"


def _reject_payload_fields(record: dict, prefix: str, errors: list[str]) -> None:
    for key in record:
        lowered = str(key).lower()
        if any(marker in lowered for marker in PAYLOAD_FIELD_MARKERS) or (
            lowered.endswith(PAYLOAD_FIELD_SUFFIX)
            and not lowered.endswith("context_text")
        ):
            errors.append(f"{prefix}:PAYLOAD_TEXT_FIELD_PROHIBITED_{key}")


def validate_root_task_metadata(record: Any, contract: Any) -> list[str]:
    """Validate one A9 metadata-only root-task provenance envelope."""
    errors: list[str] = []
    if not _guard_contract(contract, "RootTaskMetadata", errors):
        return errors
    _require_fields(
        record,
        (
            "root_task_id",
            "root_task_record_version",
            "root_task_state",
            "root_content_artifact_sha256",
            "source_route_record_id",
            "source_route_record_sha256",
            "primary_coverage_anchor_id",
            "role_id",
            "statistical_stratum_id",
            "statistical_slot_id",
            "rights_instrument_evidence_id",
            "privacy_attestation_evidence_id",
            "gold_nonexposure_attestation_reference",
            "record_canonical_sha256",
        ),
        "RootTaskMetadata",
        errors,
    )
    if not isinstance(record, dict):
        return errors

    anchor_vocab = _contract_vocab(contract, "required_arabic_coverage_anchors")
    anchor = record.get("primary_coverage_anchor_id")
    known_anchors = {
        "MODERN_STANDARD_ARABIC_CLINICAL",
        "SAUDI_GULF_COLLOQUIAL_PATIENT",
        "ARABIC_ENGLISH_CODE_SWITCHING",
        "LOCAL_MEDICATION_NOMENCLATURE",
        "ARABIC_EMERGENCY_TRIAGE",
    }
    if anchor_vocab:
        known_anchors = anchor_vocab
    if isinstance(anchor, list) or anchor not in known_anchors:
        errors.append(f"RootTaskMetadata:UNKNOWN_PRIMARY_COVERAGE_ANCHOR_{anchor}")

    secondary = record.get("secondary_coverage_tags") or []
    if not isinstance(secondary, list):
        errors.append("RootTaskMetadata:SECONDARY_COVERAGE_TAGS_MUST_BE_LIST")

    _reject_payload_fields(record, "RootTaskMetadata", errors)
    return errors


def validate_pair_metadata(record: Any, contract: Any) -> list[str]:
    """Validate one paired Arabic/English statistical unit."""
    errors: list[str] = []
    if not _guard_contract(contract, "PairMetadata", errors):
        return errors
    _require_fields(
        record,
        (
            "pair_id",
            "root_task_id",
            "arabic_variant_id",
            "english_variant_id",
            "pair_review_binding_id",
            "record_canonical_sha256",
        ),
        "PairMetadata",
        errors,
    )
    if not isinstance(record, dict):
        return errors

    arabic_variant = record.get("arabic_variant_id")
    english_variant = record.get("english_variant_id")
    if (
        isinstance(arabic_variant, str)
        and arabic_variant == english_variant
    ):
        errors.append("PairMetadata:ARABIC_AND_ENGLISH_VARIANTS_MUST_BE_DISTINCT")

    unit_count = record.get("statistical_unit_count", 1)
    if unit_count != 1:
        errors.append("PairMetadata:PAIR_STATISTICAL_UNIT_COUNT_MUST_BE_ONE")
    return errors


def validate_review_binding(record: Any, contract: Any) -> list[str]:
    """Validate one A8 author/reviewer separation binding."""
    errors: list[str] = []
    if not _guard_contract(contract, "ReviewBinding", errors):
        return errors
    _require_fields(
        record,
        (
            "review_binding_id",
            "pair_id",
            "review_protocol_id",
            "review_protocol_version",
            "review_protocol_canonical_sha256",
            "final_review_disposition",
            "reviewed_pair_content_identity_sha256",
            "record_canonical_sha256",
        ),
        "ReviewBinding",
        errors,
    )
    if not isinstance(record, dict):
        return errors

    disposition = record.get("final_review_disposition")
    if disposition not in ALLOWED_REVIEW_DISPOSITIONS:
        errors.append(f"ReviewBinding:UNKNOWN_FINAL_REVIEW_DISPOSITION_{disposition}")

    author_refs = record.get("author_references")
    reviewer_refs = record.get("reviewer_references")
    if not isinstance(author_refs, list) or not author_refs:
        errors.append("ReviewBinding:AUTHOR_REFERENCES_REQUIRED")
    elif not all(isinstance(item, str) and item.strip() for item in author_refs):
        errors.append("ReviewBinding:AUTHOR_REFERENCES_MUST_BE_STRINGS")
        author_refs = []
    if not isinstance(reviewer_refs, list) or not reviewer_refs:
        errors.append("ReviewBinding:REVIEWER_REFERENCES_REQUIRED")
    elif not all(isinstance(item, str) and item.strip() for item in reviewer_refs):
        errors.append("ReviewBinding:REVIEWER_REFERENCES_MUST_BE_STRINGS")
        reviewer_refs = []
    authors = set(author_refs or [])
    reviewers = set(reviewer_refs or [])
    adjudicator = record.get("adjudicator_reference_or_none")
    if authors & reviewers:
        errors.append("ReviewBinding:SELF_REVIEW_PROHIBITED_AUTHOR_IS_REVIEWER")
    if adjudicator and (adjudicator in authors or adjudicator in reviewers):
        errors.append(
            "ReviewBinding:ADJUDICATOR_MUST_BE_SEPARATE_FROM_AUTHOR_AND_REVIEWER"
        )

    reviewed_identity = record.get("reviewed_pair_content_identity_sha256")
    current_identity = record.get("current_pair_content_identity_sha256")
    if (
        isinstance(current_identity, str)
        and current_identity.strip()
        and reviewed_identity != current_identity
    ):
        errors.append(
            "ReviewBinding:REVIEW_CONTENT_IDENTITY_STALE_FOR_CURRENT_PAIR_CONTENT"
        )
    return errors


def validate_contamination_plan(record: Any, contract: Any) -> list[str]:
    """Validate the A11 pre-declared contamination plan identity."""
    errors: list[str] = []
    if not _guard_contract(contract, "ContaminationPlan", errors):
        return errors
    errors: list[str] = []
    _require_fields(
        record,
        (
            "contamination_plan_id",
            "selection_content_universe_policy",
            "exact_method_id",
            "exact_method_version",
            "semantic_method_id",
            "semantic_method_version",
            "semantic_threshold_policy_id",
            "candidate_corpus_binding_policy",
            "parent_aware",
            "cross_lingual_semantic_assessment_required",
            "record_canonical_sha256",
        ),
        "ContaminationPlan",
        errors,
    )
    if not isinstance(record, dict):
        return errors

    if record.get("parent_aware") is not True:
        errors.append("ContaminationPlan:parent_aware_MUST_BE_TRUE")
    if record.get("cross_lingual_semantic_assessment_required") is not True:
        errors.append(
            "ContaminationPlan:cross_lingual_semantic_assessment_required_MUST_BE_TRUE"
        )

    threshold_policy = record.get("semantic_threshold_policy_id")
    if (
        isinstance(threshold_policy, str)
        and threshold_policy.strip().lower() == "latest"
    ):
        errors.append("ContaminationPlan:MUTABLE_LATEST_POLICY_BINDING_PROHIBITED")
    return errors


def evaluate_preconstruction_snapshot(
    snapshot: Any, contract: Any, scientific_readiness: Any
) -> dict[str, object]:
    """Compute A1-A14 snapshot readiness; never bypasses US2 scientific gates."""
    reason_codes: list[str] = []

    contract_errors = validate_preconstruction_contract(contract)
    reason_codes.extend(f"Snapshot:{e}" for e in contract_errors)

    if not isinstance(scientific_readiness, dict):
        reason_codes.append("Snapshot:SCIENTIFIC_READINESS_INPUT_MISSING")
    else:
        state = scientific_readiness.get("state")
        if state != "READY_FOR_PRECONSTRUCTION":
            reason_codes.append(
                f"Snapshot:SCIENTIFIC_READINESS_NOT_READY_STATE_{state}"
            )
            readiness_codes = scientific_readiness.get("reason_codes")
            if isinstance(readiness_codes, list):
                for code in readiness_codes:
                    reason_codes.append(f"Snapshot:SCIENTIFIC_{code}")
            elif readiness_codes is not None:
                reason_codes.append(
                    "Snapshot:SCIENTIFIC_REASON_CODES_MALFORMED"
                )

    requirements = snapshot.get("requirements") if isinstance(snapshot, dict) else None
    if not isinstance(requirements, dict) or not requirements:
        reason_codes.append("Snapshot:NO_GATE_REQUIREMENTS_PRESENT")
    else:
        for gate in REQUIRED_SNAPSHOT_GATES:
            evidence = requirements.get(gate)
            if not isinstance(evidence, dict):
                reason_codes.append(f"Snapshot:MISSING_GATE_{gate}")
                continue
            gate_state = evidence.get("state")
            record_id = evidence.get("record_id")
            record_sha = evidence.get("record_canonical_sha256")
            if gate_state != "PASS":
                reason_codes.append(f"Snapshot:GATE_{gate}_STATE_{gate_state}")
            elif evidence.get("stale") is True:
                reason_codes.append(f"Snapshot:GATE_{gate}_STALE")
            elif not isinstance(record_id, str) or not record_id.strip():
                reason_codes.append(f"Snapshot:GATE_{gate}_RECORD_ID_UNBOUND")
            elif not isinstance(record_sha, str) or not record_sha.strip():
                reason_codes.append(f"Snapshot:GATE_{gate}_RECORD_SHA_UNBOUND")

    unique_sorted = sorted(set(reason_codes))
    computed_state = (
        "READY_FOR_SEPARATE_ACTIVATION_NOT_AUTHORIZED"
        if not unique_sorted
        else "NOT_READY_TO_CONSTRUCT"
    )
    # Caller-owned ready/pass claims are ignored entirely.
    result = {
        "state": computed_state,
        "reason_codes": unique_sorted,
    }
    if isinstance(snapshot, dict) and snapshot.get("snapshot_id"):
        result["snapshot_id"] = snapshot["snapshot_id"]
    return result