from __future__ import annotations

import hashlib

from src.commandmed.reliability_v5.oracle_qualification import qualify_bound_rule_execution
from src.commandmed.reliability_v5.rule_dataset import BoundRule
from src.commandmed.reliability_v5.case_generator import case_space_size


def _bound_rule(code: str, *, function_name: str, domains: dict[str, list[object]]) -> BoundRule:
    return BoundRule(
        pmid="99999999",
        title="Synthetic execution-coverage fixture",
        function_name=function_name,
        code=code,
        code_sha256=hashlib.sha256(code.encode("utf-8")).hexdigest(),
        domain_constants=domains,
        prospective_case_space=case_space_size(domains),
    )


def _wide_domains() -> dict[str, list[object]]:
    return {
        "a": [0, 2],
        "b": [1],
        "c": [2],
        "d": [3],
        "e": [4],
    }


def test_execution_qualification_covers_all_prefrozen_dev_cal_states() -> None:
    code = """def synthetic_score(a, b, c, d, e):
    score = 0
    if a > 1:
        score += 1
    if b > 1:
        score += 1
    if c > 2:
        score += 1
    if d > 3:
        score += 1
    if e > 4:
        score += 1
    return score"""
    result = qualify_bound_rule_execution(
        _bound_rule(code, function_name="synthetic_score", domains=_wide_domains())
    )
    assert result.qualified is True
    assert result.development_cases_checked == 64
    assert result.calibration_cases_checked == 64
    assert result.failure_role is None


def test_execution_qualification_preserves_upstream_unbound_local_failure() -> None:
    code = """def synthetic_score(a, b, c, d, e):
    if a < -10:
        a_score = 1
    elif a > 10:
        a_score = 2
    return a_score"""
    result = qualify_bound_rule_execution(
        _bound_rule(code, function_name="synthetic_score", domains=_wide_domains())
    )
    assert result.qualified is False
    assert result.failure_role == "RULE_ORACLE_DEVELOPMENT"
    assert result.failure_type == "UnboundLocalError"
    assert result.failure_state_index is not None
    assert result.failure_case_id is not None


def test_execution_qualification_rejects_case_space_identity_mismatch() -> None:
    code = """def synthetic_score(a, b, c, d, e):
    return 1"""
    rule = _bound_rule(code, function_name="synthetic_score", domains=_wide_domains())
    mismatched = BoundRule(
        pmid=rule.pmid,
        title=rule.title,
        function_name=rule.function_name,
        code=rule.code,
        code_sha256=rule.code_sha256,
        domain_constants=rule.domain_constants,
        prospective_case_space=rule.prospective_case_space + 1,
    )
    result = qualify_bound_rule_execution(mismatched)
    assert result.qualified is False
    assert result.failure_role == "QUALIFICATION_SETUP"
    assert result.failure_type == "ReliabilityContractError"
    assert "case-space identity mismatch" in (result.failure_message or "")


def test_execution_qualification_rejects_unsafe_calls_before_execution() -> None:
    code = """def synthetic_score(a, b, c, d, e):
    return abs(a)"""
    result = qualify_bound_rule_execution(
        _bound_rule(code, function_name="synthetic_score", domains=_wide_domains())
    )
    assert result.qualified is False
    assert result.failure_role == "QUALIFICATION_SETUP"
    assert result.failure_type == "ReliabilityContractError"
    assert "only np.exp calls are allowed" in (result.failure_message or "")


def test_execution_qualification_rejects_unperturbable_output() -> None:
    code = """def synthetic_score(a, b, c, d, e):
    return None"""
    result = qualify_bound_rule_execution(
        _bound_rule(code, function_name="synthetic_score", domains=_wide_domains())
    )
    assert result.qualified is False
    assert result.failure_role == "RULE_ORACLE_DEVELOPMENT"
    assert result.failure_type == "ReliabilityContractError"
    assert "cannot perturb type NoneType" in (result.failure_message or "")
