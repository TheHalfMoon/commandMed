"""Fail-closed SP007-RO-001 applicable-prerequisite snapshot contract.

This module is metadata-only corrective maintenance under the canonical E004
CM-3 execution-envelope authority. It never loads model weights, executes a
model or benchmark, opens a device, accesses a network or credential, selects
a winner, activates A15, starts training, or grants execution authority.
"""

from __future__ import annotations

import re
from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.foundation import is_canonical_sha256, validate_closed_object
from src.commandmed.spec007.research_execution import (
    RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
    build_research_component_execution_request,
    validate_research_component_preexecution_subject,
)
from src.commandmed.spec007.research_scope import RESEARCH_COMPONENT_SCOPE_ID
from src.commandmed.spec007.research_tournament import (
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
)

CANONICAL_CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256 = (
    "ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd"
)

# These are not new scientific gates. They are the exact pre-execution evidence
# families already required by the canonical V46 successor frontier and current
# ResearchComponentPreExecutionSubject contract.
APPLICABLE_PREREQUISITE_GATE_IDS: tuple[str, ...] = (
    "SUCCESSOR_SCOPE_POLICY",
    "SUCCESSOR_EXECUTION_AUTHORITY",
    "EVALUATION_ASSET_QUALIFICATION",
    "CANDIDATE_ARTIFACT_BUNDLE_BINDING",
    "EXECUTION_PLAN_ARGV",
    "MODEL_LOAD_COMPATIBILITY",
    "ORCHESTRATOR_IMPLEMENTATION_BINDING",
    "EXECUTION_ENVIRONMENT_BINDING",
    "RESOURCE_BINDING",
    "ACCESS_BINDING",
    "CREDENTIAL_BOUNDARY",
    "NETWORK_BOUNDARY",
    "RETENTION_BOUNDARY",
    "ZERO_INCREMENTAL_SPEND_BINDING",
)

_SNAPSHOT_FIELDS = (
    "schema_version",
    "snapshot_id",
    "snapshot_sha256",
    "scope_id",
    "protocol_id",
    "protocol_sha256",
    "evaluation_asset_set_sha256",
    "candidate_artifact_bundle_set_sha256",
    "gate_set_sha256",
    "gate_records",
    "disposition",
)
_GATE_FIELDS = (
    "gate_id",
    "evidence_id",
    "evidence_sha256",
    "evidence_repository_commit",
    "disposition",
)
_GIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "\x00" not in value


def compute_applicable_prerequisite_gate_set_sha256() -> str:
    """Return the canonical identity of the exact V46 prerequisite gate set."""
    return compute_canonical_sha256({"gate_ids": list(APPLICABLE_PREREQUISITE_GATE_IDS)})


def compute_research_component_applicable_prerequisite_snapshot_sha256(
    snapshot: Mapping[str, Any],
) -> str:
    """Compute one snapshot identity excluding its self-address field."""
    projection = dict(snapshot)
    projection.pop("snapshot_sha256", None)
    return compute_canonical_sha256(projection)


def validate_research_component_applicable_prerequisite_snapshot(
    snapshot: Any,
) -> list[str]:
    """Validate one exact, content-addressed applicable-prerequisite snapshot."""
    prefix = "ResearchComponentApplicablePrerequisiteSnapshot"
    errors = validate_closed_object(snapshot, required_fields=_SNAPSHOT_FIELDS, field=prefix)
    if errors or not isinstance(snapshot, dict):
        return errors

    if snapshot.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version must equal '1'")
    if not _nonempty(snapshot.get("snapshot_id")):
        errors.append(f"{prefix}: snapshot_id must be non-empty")
    if snapshot.get("scope_id") != RESEARCH_COMPONENT_SCOPE_ID:
        errors.append(f"{prefix}: scope_id mismatch")
    if snapshot.get("protocol_id") != RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID:
        errors.append(f"{prefix}: protocol_id mismatch")
    if snapshot.get("protocol_sha256") != RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256:
        errors.append(f"{prefix}: protocol_sha256 mismatch")
    if (
        snapshot.get("evaluation_asset_set_sha256")
        != RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256
    ):
        errors.append(f"{prefix}: evaluation_asset_set_sha256 mismatch")
    if (
        snapshot.get("candidate_artifact_bundle_set_sha256")
        != CANONICAL_CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256
    ):
        errors.append(f"{prefix}: candidate_artifact_bundle_set_sha256 mismatch")

    expected_gate_set_sha256 = compute_applicable_prerequisite_gate_set_sha256()
    if snapshot.get("gate_set_sha256") != expected_gate_set_sha256:
        errors.append(f"{prefix}: gate_set_sha256 mismatch")

    records = snapshot.get("gate_records")
    expected_gate_ids = set(APPLICABLE_PREREQUISITE_GATE_IDS)
    seen_gate_ids: set[str] = set()
    if not isinstance(records, list) or len(records) != len(APPLICABLE_PREREQUISITE_GATE_IDS):
        errors.append(
            f"{prefix}.gate_records: exactly {len(APPLICABLE_PREREQUISITE_GATE_IDS)} "
            "applicable gate records are required"
        )
    else:
        for index, record in enumerate(records):
            item_prefix = f"{prefix}.gate_records[{index}]"
            item_errors = validate_closed_object(
                record,
                required_fields=_GATE_FIELDS,
                field=item_prefix,
            )
            errors.extend(item_errors)
            if item_errors or not isinstance(record, dict):
                continue

            gate_id = record.get("gate_id")
            if gate_id not in expected_gate_ids:
                errors.append(f"{item_prefix}: gate_id is outside the canonical applicable set")
            elif gate_id in seen_gate_ids:
                errors.append(f"{item_prefix}: duplicate gate_id '{gate_id}'")
            else:
                seen_gate_ids.add(gate_id)

            if not _nonempty(record.get("evidence_id")):
                errors.append(f"{item_prefix}: evidence_id must be non-empty")
            if not is_canonical_sha256(record.get("evidence_sha256")):
                errors.append(f"{item_prefix}: evidence_sha256 must be lowercase sha256 hex")
            repository_commit = record.get("evidence_repository_commit")
            if not isinstance(repository_commit, str) or _GIT_SHA_RE.fullmatch(repository_commit) is None:
                errors.append(
                    f"{item_prefix}: evidence_repository_commit must be an exact git sha"
                )
            if record.get("disposition") != "PASS":
                errors.append(f"{item_prefix}: disposition must equal PASS")

        if seen_gate_ids != expected_gate_ids:
            errors.append(f"{prefix}: gate_records must equal the exact canonical applicable set")

    if snapshot.get("disposition") != "PASS":
        errors.append(f"{prefix}: disposition must equal PASS")

    claimed = snapshot.get("snapshot_sha256")
    if not is_canonical_sha256(claimed):
        errors.append(f"{prefix}: snapshot_sha256 must be lowercase sha256 hex")
    elif claimed != compute_research_component_applicable_prerequisite_snapshot_sha256(
        snapshot
    ):
        errors.append(f"{prefix}: snapshot_sha256 mismatch")

    return sorted(set(errors))


def validate_research_component_applicable_prerequisite_binding(
    subject: Any,
    *,
    prerequisite_snapshot_store: Mapping[str, Mapping[str, Any]],
) -> list[str]:
    """Bind the subject's A1-A14-equivalent fields to an authoritative snapshot store."""
    prefix = "ResearchComponentApplicablePrerequisiteBinding"
    structural_errors = validate_research_component_preexecution_subject(subject)
    if structural_errors or not isinstance(subject, dict):
        return [f"{prefix}: subject: {error}" for error in structural_errors]

    snapshot_sha256 = subject.get("a1_a14_applicable_snapshot_sha256")
    if not is_canonical_sha256(snapshot_sha256):
        return [f"{prefix}: subject snapshot sha256 is invalid"]

    snapshot = prerequisite_snapshot_store.get(snapshot_sha256)
    if not isinstance(snapshot, Mapping):
        return [f"{prefix}: applicable prerequisite snapshot not found in authoritative store"]

    materialized = dict(snapshot)
    errors = [
        f"{prefix}: snapshot: {error}"
        for error in validate_research_component_applicable_prerequisite_snapshot(materialized)
    ]
    if materialized.get("snapshot_sha256") != snapshot_sha256:
        errors.append(f"{prefix}: store key does not match snapshot identity")
    if materialized.get("snapshot_id") != subject.get("a1_a14_applicable_snapshot_id"):
        errors.append(f"{prefix}: snapshot_id mismatch with pre-execution subject")
    if materialized.get("disposition") != subject.get("a1_a14_applicable_state"):
        errors.append(f"{prefix}: snapshot disposition mismatch with pre-execution subject")
    if materialized.get("scope_id") != subject.get("scope_id"):
        errors.append(f"{prefix}: scope_id mismatch with pre-execution subject")
    if materialized.get("protocol_id") != subject.get("protocol_id"):
        errors.append(f"{prefix}: protocol_id mismatch with pre-execution subject")
    if materialized.get("protocol_sha256") != subject.get("protocol_sha256"):
        errors.append(f"{prefix}: protocol_sha256 mismatch with pre-execution subject")
    if (
        materialized.get("evaluation_asset_set_sha256")
        != subject.get("evaluation_asset_set_sha256")
    ):
        errors.append(
            f"{prefix}: evaluation_asset_set_sha256 mismatch with pre-execution subject"
        )
    return sorted(set(errors))


def build_research_component_execution_request_with_prerequisites(
    subject: Any,
    *,
    prerequisite_snapshot_store: Mapping[str, Mapping[str, Any]],
) -> dict[str, object]:
    """Fail closed on prerequisite evidence before entering the canonical request builder.

    This wrapper creates no new authority. Even a fully valid snapshot remains
    blocked while the canonical live subject lock in research_execution is None.
    """
    errors = validate_research_component_applicable_prerequisite_binding(
        subject,
        prerequisite_snapshot_store=prerequisite_snapshot_store,
    )
    if errors:
        return {
            "state": "BLOCKED",
            "reason_codes": errors,
            "execution_performed": False,
            "request": None,
        }
    return build_research_component_execution_request(subject)
