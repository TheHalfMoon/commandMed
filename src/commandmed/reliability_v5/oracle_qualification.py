"""Development/calibration execution qualification for V5 deterministic rule oracles.

This module never materializes confirmatory or reserve identities. It executes only
already static-admitted calculator code through the fail-closed BoundRule compiler
and only on the deterministic development/calibration states defined by the V5
quarantine mechanics.
"""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from .case_generator import case_space_size, cases_from_state_indices
from .contracts import ReliabilityContractError
from .quarantine import CALIBRATION_COUNT, DEVELOPMENT_COUNT, prefreeze_state_partition
from .rule_dataset import BoundRule, _normalize_json_value, _perturb_output, compile_bound_rule


@dataclass(frozen=True)
class RuleExecutionQualification:
    qualified: bool
    development_cases_checked: int
    calibration_cases_checked: int
    failure_role: str | None = None
    failure_state_index: int | None = None
    failure_case_id: str | None = None
    failure_type: str | None = None
    failure_message: str | None = None


def _validate_task_output(value: object) -> None:
    """Require the exact serialization and perturbation contract used by S1."""
    normalized = _normalize_json_value(value)
    perturbed = _perturb_output(normalized)
    if normalized == perturbed:
        raise ReliabilityContractError("rule output: perturbation must change the output")


def _failure(
    *,
    development_checked: int,
    calibration_checked: int,
    role: str,
    state_index: int | None,
    case_id: str | None,
    exc: BaseException,
) -> RuleExecutionQualification:
    message = " ".join(str(exc).split())[:240]
    return RuleExecutionQualification(
        qualified=False,
        development_cases_checked=development_checked,
        calibration_cases_checked=calibration_checked,
        failure_role=role,
        failure_state_index=state_index,
        failure_case_id=case_id,
        failure_type=type(exc).__name__,
        failure_message=message,
    )


def qualify_bound_rule_execution(rule: BoundRule) -> RuleExecutionQualification:
    """Execute exactly the pre-frozen development/calibration states for one rule.

    Any compile, state-space, runtime, serialization, or perturbation-contract
    failure rejects the calculator before model access. No failing state is
    skipped or repaired.
    """
    development_checked = 0
    calibration_checked = 0
    calculator_id = f"pmid:{rule.pmid}"

    try:
        observed_space = case_space_size(rule.domain_constants)
        if observed_space != rule.prospective_case_space:
            raise ReliabilityContractError(
                "rule qualification: prospective case-space identity mismatch"
            )
        partition = prefreeze_state_partition(calculator_id, observed_space)
        calculator = compile_bound_rule(rule)
    except Exception as exc:  # fail closed and preserve the exact rejection class
        return _failure(
            development_checked=0,
            calibration_checked=0,
            role="QUALIFICATION_SETUP",
            state_index=None,
            case_id=None,
            exc=exc,
        )

    for role, indices in (
        ("RULE_ORACLE_DEVELOPMENT", partition["development"]),
        ("RULE_ORACLE_CALIBRATION", partition["calibration"]),
    ):
        cases = cases_from_state_indices(calculator_id, rule.domain_constants, indices)
        for case in cases:
            try:
                inputs = case["inputs"]
                if not isinstance(inputs, Mapping):
                    raise ReliabilityContractError("rule qualification: inputs must be a mapping")
                _validate_task_output(calculator(**dict(inputs)))
            except Exception as exc:  # upstream calculator failure is negative evidence
                return _failure(
                    development_checked=development_checked,
                    calibration_checked=calibration_checked,
                    role=role,
                    state_index=int(case["state_index"]),
                    case_id=str(case["case_id"]),
                    exc=exc,
                )
            if role == "RULE_ORACLE_DEVELOPMENT":
                development_checked += 1
            else:
                calibration_checked += 1

    if development_checked != DEVELOPMENT_COUNT or calibration_checked != CALIBRATION_COUNT:
        return _failure(
            development_checked=development_checked,
            calibration_checked=calibration_checked,
            role="QUALIFICATION_COUNT",
            state_index=None,
            case_id=None,
            exc=ReliabilityContractError("rule qualification: incomplete execution coverage"),
        )

    return RuleExecutionQualification(
        qualified=True,
        development_cases_checked=development_checked,
        calibration_cases_checked=calibration_checked,
    )
