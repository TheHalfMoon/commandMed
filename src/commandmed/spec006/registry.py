"""Spec 006 deterministic tool registry validation.

Implements the frozen ``contracts/tool-registry.schema.json`` contract as a
typed standard-library validator. Every registry entry is a record, not a
service binding: ``network_required`` must be false and
``execution_authority`` must be ``NONE``. Bundle identity is the projection
hash ``sha256(canonical_json({registry_version, tools}))`` computed over the
canonical JSON that omits ``registry_sha256`` itself.
"""

from __future__ import annotations

import re
from typing import Any

from src.commandmed.eval_contract.canonical import compute_canonical_sha256

TOOL_CLASSES = frozenset(
    {
        "unit_conversion",
        "pure_arithmetic",
        "validated_clinical_score",
        "interaction_lookup",
        "schema_validation",
        "evidence_retrieval",
    }
)

FAIL_STATES = frozenset({"ASK_MORE", "ABSTAIN", "ESCALATE", "EMERGENCY"})

EXECUTION_AUTHORITY_ALLOWED = frozenset({"NONE"})

SHA256_HEX = re.compile(r"^[0-9a-f]{64}$")

TOOL_REQUIRED_FIELDS = (
    "tool_id",
    "tool_version",
    "tool_content_identity",
    "tool_class",
    "input_schema",
    "output_schema",
    "source_authority",
    "failure_semantics",
    "applicable_when",
    "prohibited_when",
    "freshness_policy",
    "result_provenance_required",
    "network_required",
    "execution_authority",
)


def _is_sha256(value: Any) -> bool:
    return isinstance(value, str) and SHA256_HEX.match(value) is not None


def validate_tool_record(record: Any, field: str = "tools") -> list[str]:
    """Validate one DeterministicTool record against the frozen contract.

    Returns a list of error strings; an empty list means the record is valid.
    Undeclared nested fields are rejected (closed objects).
    """
    errors: list[str] = []
    if not isinstance(record, dict):
        return [f"{field}: expected an object record"]

    for key in TOOL_REQUIRED_FIELDS:
        if key not in record:
            errors.append(f"{field}.{key}: required field missing")

    undeclared = set(record) - set(TOOL_REQUIRED_FIELDS)
    if undeclared:
        errors.append(
            f"{field}: undeclared fields {sorted(undeclared)}; additionalProperties=false"
        )
    if errors:
        return errors

    for text_key in ("tool_id", "tool_version", "source_authority", "applicable_when", "prohibited_when"):
        value = record[text_key]
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field}.{text_key}: expected non-empty string")

    if not _is_sha256(record["tool_content_identity"]):
        errors.append(f"{field}.tool_content_identity: expected lowercase sha256 hex")

    if record["tool_class"] not in TOOL_CLASSES:
        errors.append(f"{field}.tool_class: unsupported value '{record['tool_class']}'")

    if not isinstance(record["input_schema"], dict):
        errors.append(f"{field}.input_schema: expected object (JSON Schema)")
    if not isinstance(record["output_schema"], dict):
        errors.append(f"{field}.output_schema: expected object (JSON Schema)")

    failure = record["failure_semantics"]
    if not isinstance(failure, dict):
        errors.append(f"{field}.failure_semantics: expected object")
    else:
        undeclared = set(failure) - {"fail_state", "reason_code", "retryable"}
        if undeclared:
            errors.append(
                f"{field}.failure_semantics: undeclared fields {sorted(undeclared)}"
            )
        else:
            if failure["fail_state"] not in FAIL_STATES:
                errors.append(
                    f"{field}.failure_semantics.fail_state: unsupported value"
                    f" '{failure['fail_state']}'"
                )
            reason = failure["reason_code"]
            if not isinstance(reason, str) or not reason.strip():
                errors.append(
                    f"{field}.failure_semantics.reason_code: expected non-empty string"
                )
            if not isinstance(failure["retryable"], bool):
                errors.append(f"{field}.failure_semantics.retryable: expected boolean")

    freshness = record["freshness_policy"]
    if not isinstance(freshness, dict):
        errors.append(f"{field}.freshness_policy: expected object")
    else:
        undeclared = set(freshness) - {"max_age_days", "revocation_signal"}
        if undeclared:
            errors.append(
                f"{field}.freshness_policy: undeclared fields {sorted(undeclared)}"
            )
        max_age = freshness.get("max_age_days")
        if not isinstance(max_age, int) or isinstance(max_age, bool) or max_age < 1:
            errors.append(f"{field}.freshness_policy.max_age_days: expected integer >= 1")
        revocation = freshness.get("revocation_signal")
        if revocation is not None and not isinstance(revocation, str):
            errors.append(
                f"{field}.freshness_policy.revocation_signal: expected string or null"
            )

    if not isinstance(record["result_provenance_required"], bool):
        errors.append(f"{field}.result_provenance_required: expected boolean")
    if record["network_required"] is not False:
        errors.append(f"{field}.network_required: must be false (const)")
    if record["execution_authority"] not in EXECUTION_AUTHORITY_ALLOWED:
        errors.append(
            f"{field}.execution_authority: must be NONE (got"
            f" '{record['execution_authority']}')"
        )

    if (
        record["tool_class"]
        in ("validated_clinical_score", "interaction_lookup", "evidence_retrieval")
        and record["result_provenance_required"] is not True
    ):
        errors.append(
            f"{field}.result_provenance_required: must be true for clinical,"
            " interaction, or evidence tools"
        )

    return errors


def compute_registry_identity(registry_version: Any, tools: Any) -> str:
    """Projection bundle identity omitting ``registry_sha256`` itself."""
    projection = {"registry_version": registry_version, "tools": tools}
    return compute_canonical_sha256(projection)


def validate_registry(bundle: Any) -> list[str]:
    """Validate a full tool_registry.json bundle.

    Checks structure, per-record validity, duplicate tool_id rejection, and
    recomputation of the ``registry_sha256`` projection identity.
    """
    errors: list[str] = []
    if not isinstance(bundle, dict):
        return ["registry: expected object bundle"]

    required = {"registry_version", "registry_sha256", "tools"}
    missing = required - set(bundle)
    if missing:
        errors.append(f"registry: required fields missing {sorted(missing)}")
    undeclared = set(bundle) - required
    if undeclared:
        errors.append(f"registry: undeclared fields {sorted(undeclared)}")
    if missing or undeclared:
        return errors

    if not isinstance(bundle["registry_version"], str) or not bundle["registry_version"].strip():
        errors.append("registry.registry_version: expected non-empty string")

    tools = bundle["tools"]
    if not isinstance(tools, list) or not tools:
        return errors + ["registry.tools: expected non-empty array"]

    seen_ids: set[str] = set()
    for index, tool in enumerate(tools):
        field = f"tools[{index}]"
        tool_errors = validate_tool_record(tool, field=field)
        errors.extend(tool_errors)
        if isinstance(tool, dict) and isinstance(tool.get("tool_id"), str):
            if tool["tool_id"] in seen_ids:
                errors.append(f"{field}.tool_id: duplicate tool_id '{tool['tool_id']}'")
            seen_ids.add(tool["tool_id"])

    if not _is_sha256(bundle["registry_sha256"]):
        errors.append("registry.registry_sha256: expected lowercase sha256 hex")
    else:
        expected = compute_registry_identity(bundle["registry_version"], tools)
        if bundle["registry_sha256"] != expected:
            errors.append(
                "registry.registry_sha256: mismatch against projection identity"
                f" (expected {expected})"
            )

    return errors


def find_tool(registry_bundle: Any, tool_id: Any) -> dict[str, Any] | None:
    """Return the registry record with ``tool_id``, or None."""
    if not isinstance(registry_bundle, dict):
        return None
    tools = registry_bundle.get("tools")
    if not isinstance(tools, list):
        return None
    for tool in tools:
        if isinstance(tool, dict) and tool.get("tool_id") == tool_id:
            return tool
    return None
