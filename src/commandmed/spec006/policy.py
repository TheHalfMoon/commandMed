"""Spec 006 frozen safety policy validation and precedence evaluation.

Implements the frozen ``contracts/safety-rule.schema.json`` contract and the
deterministic evaluation order derived from Spec 002 SP-001..SP-006
(``research.md`` §5). Precedence is a deterministic order, not a clinical
severity ranking. Conflicting equal-precedence outcomes fail closed; safety
outcomes are never averaged. ``BLOCKED`` is a gate result, never a behavioral
state: contradictory or malformed safety state yields terminal ``ABSTAIN``
with reason code ``BLOCKED_SAFETY_STATE``.
"""

from __future__ import annotations

import re
from typing import Any

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.eval_contract.safety import BEHAVIOR_STATES

# Single canonical behavioral-state vocabulary (Spec 002): every spec006
# module references this definition instead of local copies.
BEHAVIORAL_STATES = BEHAVIOR_STATES

REASON_CODES = frozenset(
    {
        "MISSING_CRITICAL_SLOT",
        "TOOL_UNAVAILABLE",
        "TOOL_TIMEOUT",
        "SPOOFED_TOOL_RESULT_REJECTED",
        "CONFLICTING_SAFETY_OUTCOMES",
        "INJECTION_ATTEMPT_SUPPRESSED",
        "EVIDENCE_NOT_RESOLVED",
        "FROZEN_POLICY_EMERGENCY",
        "BLOCKED_SAFETY_STATE",
    }
)

TRIGGER_KINDS = frozenset(
    {"lexical", "semantic_pattern", "tool_result_flag", "missing_slot", "evidence_state"}
)

THRESHOLD_POLICY_CLASSES = frozenset(
    {
        "FROZEN_POLICY_ZERO_TOLERANCE",
        "FROZEN_SENTINEL_ZERO_VIOLATIONS",
        "PENDING_CLINICAL_EVIDENCE",
        "PENDING_FOUNDER_AND_CLINICAL_EVIDENCE",
        "NOT_APPLICABLE_TO_DECLARED_SCOPE",
    }
)

APPLICABLE_SCOPES = frozenset({"SYSTEM_QUALIFICATION", "COMPONENT_QUALIFICATION"})

SHA256_HEX = re.compile(r"^[0-9a-f]{64}$")

RULE_REQUIRED_FIELDS = (
    "rule_id",
    "rule_version",
    "source_policy_sha256",
    "trigger_condition",
    "required_state",
    "precedence",
    "threshold_policy_class",
    "applicable_scope",
    "revoked",
)


def _is_sha256(value: Any) -> bool:
    return isinstance(value, str) and SHA256_HEX.match(value) is not None


def validate_safety_rule(rule: Any, field: str = "rules") -> list[str]:
    """Validate one SafetyRule record against the frozen contract."""
    errors: list[str] = []
    if not isinstance(rule, dict):
        return [f"{field}: expected an object record"]

    for key in RULE_REQUIRED_FIELDS:
        if key not in rule:
            errors.append(f"{field}.{key}: required field missing")
    undeclared = set(rule) - set(RULE_REQUIRED_FIELDS)
    if undeclared:
        errors.append(f"{field}: undeclared fields {sorted(undeclared)}")
    if errors:
        return errors

    for text_key in ("rule_id", "rule_version"):
        value = rule[text_key]
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field}.{text_key}: expected non-empty string")

    if not _is_sha256(rule["source_policy_sha256"]):
        errors.append(f"{field}.source_policy_sha256: expected lowercase sha256 hex")

    trigger = rule["trigger_condition"]
    if not isinstance(trigger, dict):
        errors.append(f"{field}.trigger_condition: expected object")
    else:
        undeclared = set(trigger) - {"kind", "ref", "threshold"}
        if undeclared:
            errors.append(f"{field}.trigger_condition: undeclared fields {sorted(undeclared)}")
        kind = trigger.get("kind")
        if kind not in TRIGGER_KINDS:
            errors.append(f"{field}.trigger_condition.kind: unsupported value '{trigger.get('kind')}'")
        else:
            ref = trigger.get("ref")
            # Per-kind required bindings: a rule without its frozen signal can
            # never fire, which would silently disable a safety behavior.
            if kind in ("lexical", "semantic_pattern", "tool_result_flag"):
                if not isinstance(ref, str) or not ref.strip():
                    errors.append(
                        f"{field}.trigger_condition.ref: required non-empty string for kind '{kind}'"
                    )
            elif kind == "missing_slot":
                if not isinstance(ref, str) or not ref.strip():
                    errors.append(
                        f"{field}.trigger_condition.ref: required non-empty string for kind 'missing_slot'"
                    )
                threshold = trigger.get("threshold")
                if not isinstance(threshold, str) or not threshold.strip():
                    errors.append(
                        f"{field}.trigger_condition.threshold: required non-empty"
                        " gated tool-class list for kind 'missing_slot'"
                    )
            threshold = trigger.get("threshold")
            if threshold is not None and not isinstance(threshold, (str, int, float, bool)):
                errors.append(f"{field}.trigger_condition.threshold: unsupported type")
            if kind == "semantic_pattern" and isinstance(ref, str) and ref.strip():
                try:
                    re.compile(ref)
                except re.error as exc:
                    errors.append(f"{field}.trigger_condition.ref: malformed frozen pattern ({exc})")

    if rule["required_state"] not in BEHAVIORAL_STATES:
        errors.append(f"{field}.required_state: unsupported value '{rule['required_state']}'")

    precedence = rule["precedence"]
    if not isinstance(precedence, int) or isinstance(precedence, bool) or not 1 <= precedence <= 100:
        errors.append(f"{field}.precedence: expected integer within [1, 100]")

    if rule["threshold_policy_class"] not in THRESHOLD_POLICY_CLASSES:
        errors.append(
            f"{field}.threshold_policy_class: unsupported value '{rule['threshold_policy_class']}'"
        )
    if rule["applicable_scope"] not in APPLICABLE_SCOPES:
        errors.append(f"{field}.applicable_scope: unsupported value '{rule['applicable_scope']}'")
    if not isinstance(rule["revoked"], bool):
        errors.append(f"{field}.revoked: expected boolean")

    # SP-001 exact equality: emergency/escalation rules are zero-tolerance.
    if (
        rule["required_state"] in ("EMERGENCY", "ESCALATE")
        and rule["threshold_policy_class"]
        in ("PENDING_CLINICAL_EVIDENCE", "PENDING_FOUNDER_AND_CLINICAL_EVIDENCE")
        and rule["trigger_condition"].get("kind") == "lexical"
        and rule["precedence"] > 3
    ):
        errors.append(
            f"{field}.{rule['rule_id']}: emergency/escalation lexical rules must bind a"
            " zero-tolerance class and top precedence (SP-001)"
        )

    return errors


def compute_policy_identity(policy_version: Any, rules: Any) -> str:
    """Projection bundle identity omitting ``policy_sha256`` itself."""
    projection = {"policy_version": policy_version, "rules": rules}
    return compute_canonical_sha256(projection)


def validate_policy_bundle(bundle: Any) -> list[str]:
    """Validate a full safety_policy.json bundle.

    Checks structure, per-rule validity, unique rule_id, tie-free precedence,
    at least one rule, and recomputation of the ``policy_sha256`` projection.
    """
    errors: list[str] = []
    if not isinstance(bundle, dict):
        return ["policy: expected object bundle"]

    required = {"policy_version", "policy_sha256", "rules"}
    missing = required - set(bundle)
    if missing:
        errors.append(f"policy: required fields missing {sorted(missing)}")
    undeclared = set(bundle) - required
    if undeclared:
        errors.append(f"policy: undeclared fields {sorted(undeclared)}")
    if missing or undeclared:
        return errors

    if not isinstance(bundle["policy_version"], str) or not bundle["policy_version"].strip():
        errors.append("policy.policy_version: expected non-empty string")

    rules = bundle["rules"]
    if not isinstance(rules, list) or len(rules) < 1:
        return errors + ["policy.rules: expected array with minItems 1"]

    seen_ids: set[str] = set()
    precedence_counts: dict[int, int] = {}
    valid_rules: list[dict[str, Any]] = []
    for index, rule in enumerate(rules):
        field = f"rules[{index}]"
        rule_errors = validate_safety_rule(rule, field=field)
        errors.extend(rule_errors)
        if isinstance(rule, dict):
            if isinstance(rule.get("rule_id"), str):
                if rule["rule_id"] in seen_ids:
                    errors.append(f"{field}.rule_id: duplicate rule_id '{rule['rule_id']}'")
                seen_ids.add(rule["rule_id"])
            precedence = rule.get("precedence")
            if isinstance(precedence, int) and not isinstance(precedence, bool):
                precedence_counts[precedence] = precedence_counts.get(precedence, 0) + 1
            if not rule_errors:
                valid_rules.append(rule)

    for precedence, count in sorted(precedence_counts.items()):
        if count > 1:
            errors.append(
                f"policy.rules: duplicate precedence {precedence} across {count} rules;"
                " ties are a validation error"
            )

    if not _is_sha256(bundle["policy_sha256"]):
        errors.append("policy.policy_sha256: expected lowercase sha256 hex")
    else:
        expected = compute_policy_identity(bundle["policy_version"], rules)
        if bundle["policy_sha256"] != expected:
            errors.append(
                f"policy.policy_sha256: mismatch against projection identity (expected {expected})"
            )

    return errors


def evaluate_precedence(fired_rules: list[dict[str, Any]]) -> dict[str, Any]:
    """Resolve fired rules into exactly one terminal behavioral state.

    Deterministic evaluation order per ``research.md`` §5:

    1. revoked or malformed fired rule -> ABSTAIN / BLOCKED_SAFETY_STATE;
    2. otherwise the lowest ``precedence`` number wins (highest priority);
    3. two distinct required states at the same precedence conflict ->
       ESCALATE if either candidate escalates, else ABSTAIN, always with
       reason ``CONFLICTING_SAFETY_OUTCOMES`` (never averaged);
    4. no fired rules -> ANSWER with no triggers.

    Returns ``{"state_after", "reason_codes", "trigger_record_ids"}`` where
    ``trigger_record_ids`` carries the winning rule ids.
    """
    if not isinstance(fired_rules, list):
        return {
            "state_after": "ABSTAIN",
            "reason_codes": ["BLOCKED_SAFETY_STATE"],
            "trigger_record_ids": [],
        }

    active = []
    for candidate in fired_rules:
        if not isinstance(candidate, dict):
            return {
                "state_after": "ABSTAIN",
                "reason_codes": ["BLOCKED_SAFETY_STATE"],
                "trigger_record_ids": [],
            }
        if (
            set(candidate) == {"rule_id", "precedence", "required_state"}
            and isinstance(candidate.get("rule_id"), str)
            and candidate["rule_id"].startswith("SCAFFOLD::")
        ):
            # Internally composed candidate (scaffold tool layer): minimal typed
            # triple under the reserved SCAFFOLD namespace; still fail closed
            # on bad types.
            if (
                not isinstance(candidate["rule_id"], str)
                or not isinstance(candidate["required_state"], str)
                or candidate["required_state"] not in BEHAVIORAL_STATES
                or not isinstance(candidate["precedence"], int)
                or isinstance(candidate["precedence"], bool)
            ):
                return {
                    "state_after": "ABSTAIN",
                    "reason_codes": ["BLOCKED_SAFETY_STATE"],
                    "trigger_record_ids": [],
                }
            active.append(candidate)
            continue
        if validate_safety_rule(candidate, field="fired_rule"):
            return {
                "state_after": "ABSTAIN",
                "reason_codes": ["BLOCKED_SAFETY_STATE"],
                "trigger_record_ids": [],
            }
        if candidate["revoked"]:
            return {
                "state_after": "ABSTAIN",
                "reason_codes": ["BLOCKED_SAFETY_STATE"],
                "trigger_record_ids": [candidate["rule_id"]],
            }
        active.append(candidate)

    if not active:
        return {"state_after": "ANSWER", "reason_codes": [], "trigger_record_ids": []}

    ordered = sorted(active, key=lambda rule: rule["precedence"])
    highest_precedence = ordered[0]["precedence"]
    leaders = [rule for rule in ordered if rule["precedence"] == highest_precedence]
    required_states = {rule["required_state"] for rule in leaders}

    if len(required_states) > 1:
        state = "ESCALATE" if required_states & {"ESCALATE", "EMERGENCY"} else "ABSTAIN"
        return {
            "state_after": state,
            "reason_codes": ["CONFLICTING_SAFETY_OUTCOMES"],
            "trigger_record_ids": [rule["rule_id"] for rule in leaders],
        }

    winner = leaders[0]
    reason_codes: list[str] = []
    if winner["required_state"] == "EMERGENCY":
        reason_codes.append("FROZEN_POLICY_EMERGENCY")
    return {
        "state_after": winner["required_state"],
        "reason_codes": reason_codes,
        "trigger_record_ids": [winner["rule_id"]],
    }
