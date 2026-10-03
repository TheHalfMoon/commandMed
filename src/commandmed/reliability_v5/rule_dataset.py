"""Bounded V5 rule-oracle development/calibration task construction.

This module may execute only identity-bound RiskCalcs functions that pass the
frozen static safety contract. It never selects or materializes confirmatory or
reserve identities.
"""
from __future__ import annotations

import ast
import hashlib
import json
import math
import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Callable

from .case_generator import cases_from_state_indices
from .contracts import ReliabilityContractError
from .quarantine import prefreeze_state_partition

FROZEN_SOURCE_SHA256 = "00a7a0089afffb66f2f32903bad94a5a2ea842841defb2d78e0686b0a5eb9ab9"
TRAIN_NAMESPACE = "CommandMed-V5-S1-TRAIN-v1"
CAL_NAMESPACE = "CommandMed-V5-S1-CAL-v1"
PROPOSAL_NAMESPACE = "CommandMed-V5-S1-PROPOSAL-v1"
OPTION_NAMESPACE = "CommandMed-V5-S1-OPTION-v1"
TRAIN_PER_CALCULATOR = 4
CAL_TUNE_PER_CALCULATOR = 4
_PY_BLOCK = re.compile(r"```python\s*(.*?)```", re.IGNORECASE | re.DOTALL)

_ALLOWED_AST_TYPES = {
    ast.Module,
    ast.FunctionDef,
    ast.arguments,
    ast.arg,
    ast.Import,
    ast.alias,
    ast.Assign,
    ast.AugAssign,
    ast.Expr,
    ast.If,
    ast.IfExp,
    ast.Return,
    ast.BoolOp,
    ast.BinOp,
    ast.UnaryOp,
    ast.Compare,
    ast.Call,
    ast.Attribute,
    ast.Name,
    ast.Load,
    ast.Store,
    ast.Constant,
    ast.List,
    ast.Tuple,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.USub,
    ast.Not,
    ast.And,
    ast.Or,
    ast.Eq,
    ast.Gt,
    ast.GtE,
    ast.Lt,
    ast.LtE,
    ast.In,
}


@dataclass(frozen=True)
class BoundRule:
    pmid: str
    title: str
    function_name: str
    code: str
    code_sha256: str
    domain_constants: Mapping[str, Sequence[object]]
    prospective_case_space: int


@dataclass(frozen=True)
class RuleVerificationExample:
    task_id: str
    calculator_id: str
    pmid: str
    split: str
    case_id: str
    state_index: int
    code_sha256: str
    inputs: Mapping[str, object]
    reference_output: object
    proposed_output: object
    proposal_matches: bool
    option_a_semantic: str
    option_b_semantic: str
    target_label: str
    canonical_prompt: str
    transformed_prompt: str


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_text(payload: str) -> str:
    return _sha256_bytes(payload.encode("utf-8"))


def _rank(case_id: str, namespace: str) -> str:
    return _sha256_text(f"{case_id}|{namespace}")


def _extract_function_code(computation: str) -> str:
    match = _PY_BLOCK.search(computation or "")
    if match is None:
        raise ReliabilityContractError("rule source: missing fenced Python function")
    return match.group(1).strip()


def _validate_safe_rule_ast(code: str, expected_function_name: str) -> ast.Module:
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        raise ReliabilityContractError("rule source: invalid Python syntax") from exc

    body_shape = tuple(type(node) for node in tree.body)
    if body_shape not in ((ast.FunctionDef,), (ast.Import, ast.FunctionDef)):
        raise ReliabilityContractError("rule source: only one function and optional numpy import are allowed")
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef))
    if function.name != expected_function_name:
        raise ReliabilityContractError("rule source: function name mismatch")
    if function.decorator_list:
        raise ReliabilityContractError("rule source: decorators are forbidden")

    for node in ast.walk(tree):
        if type(node) not in _ALLOWED_AST_TYPES:
            raise ReliabilityContractError(f"rule source: unsupported AST node {type(node).__name__}")
        if isinstance(node, ast.Import):
            if len(node.names) != 1 or node.names[0].name != "numpy" or node.names[0].asname != "np":
                raise ReliabilityContractError("rule source: only 'import numpy as np' is allowed")
        if isinstance(node, ast.Call):
            if not (
                isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "np"
                and node.func.attr == "exp"
            ):
                raise ReliabilityContractError("rule source: only np.exp calls are allowed")
        if isinstance(node, ast.Attribute):
            if not (
                isinstance(node.value, ast.Name)
                and node.value.id == "np"
                and node.attr == "exp"
            ):
                raise ReliabilityContractError("rule source: only np.exp attribute access is allowed")
    return tree


def bind_selected_rules(
    *,
    source_bytes: bytes,
    selection_manifest: Mapping[str, object],
    require_count: int | None = 64,
) -> tuple[BoundRule, ...]:
    expected_source = str(selection_manifest.get("source_bytes_sha256", ""))
    observed_source = _sha256_bytes(source_bytes)
    if expected_source != FROZEN_SOURCE_SHA256 or observed_source != expected_source:
        raise ReliabilityContractError("rule source: source SHA-256 mismatch")
    try:
        source = json.loads(source_bytes)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ReliabilityContractError("rule source: invalid JSON") from exc
    if not isinstance(source, dict):
        raise ReliabilityContractError("rule source: expected PMID-keyed object")
    raw_selected = selection_manifest.get("selected")
    if not isinstance(raw_selected, list):
        raise ReliabilityContractError("rule manifest: selected must be a list")
    if require_count is not None and len(raw_selected) != require_count:
        raise ReliabilityContractError(f"rule manifest: expected {require_count} selected calculators")

    bound: list[BoundRule] = []
    for raw in raw_selected:
        if not isinstance(raw, Mapping):
            raise ReliabilityContractError("rule manifest: selected rows must be mappings")
        pmid = str(raw.get("pmid", ""))
        record = source.get(pmid)
        if not isinstance(record, Mapping):
            raise ReliabilityContractError(f"rule source: missing PMID {pmid}")
        code = _extract_function_code(str(record.get("computation", "")))
        code_sha256 = _sha256_text(code)
        if code_sha256 != str(raw.get("code_sha256", "")):
            raise ReliabilityContractError(f"rule source: code SHA-256 mismatch for PMID {pmid}")
        function_name = str(raw.get("function_name", ""))
        _validate_safe_rule_ast(code, function_name)
        domains = raw.get("domain_constants")
        if not isinstance(domains, Mapping) or not domains:
            raise ReliabilityContractError(f"rule manifest: missing domains for PMID {pmid}")
        total = raw.get("prospective_case_space")
        if not isinstance(total, int) or isinstance(total, bool) or total < 1024:
            raise ReliabilityContractError(f"rule manifest: invalid case space for PMID {pmid}")
        bound.append(
            BoundRule(
                pmid=pmid,
                title=str(raw.get("title", "")),
                function_name=function_name,
                code=code,
                code_sha256=code_sha256,
                domain_constants=domains,
                prospective_case_space=total,
            )
        )
    return tuple(bound)


def compile_bound_rule(rule: BoundRule) -> Callable[..., object]:
    """Compile one already-bound rule with a minimal global namespace."""
    tree = _validate_safe_rule_ast(rule.code, rule.function_name)
    function_only = ast.Module(
        body=[node for node in tree.body if isinstance(node, ast.FunctionDef)],
        type_ignores=[],
    )
    ast.fix_missing_locations(function_only)
    globals_dict: dict[str, object] = {"__builtins__": {}}
    if any(isinstance(node, ast.Import) for node in tree.body):
        try:
            import numpy as np  # type: ignore
        except ImportError as exc:
            raise ReliabilityContractError("rule runtime: numpy is required by a bound calculator") from exc
        globals_dict["np"] = np
    locals_dict: dict[str, object] = {}
    exec(compile(function_only, f"riskcalcs:{rule.pmid}", "exec"), globals_dict, locals_dict)
    function = locals_dict.get(rule.function_name)
    if not callable(function):
        raise ReliabilityContractError("rule runtime: bound function did not compile")
    return function


def _normalize_json_value(value: Any) -> object:
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return value
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ReliabilityContractError("rule output: non-finite float")
        return value
    if isinstance(value, tuple):
        return [_normalize_json_value(item) for item in value]
    if isinstance(value, list):
        return [_normalize_json_value(item) for item in value]
    if isinstance(value, Mapping):
        return {str(key): _normalize_json_value(item) for key, item in sorted(value.items())}
    item_method = getattr(value, "item", None)
    if callable(item_method) and type(value).__module__.startswith("numpy"):
        return _normalize_json_value(item_method())
    raise ReliabilityContractError(f"rule output: unsupported type {type(value).__name__}")


def _perturb_output(value: object) -> object:
    if isinstance(value, bool):
        return not value
    if isinstance(value, int) and not isinstance(value, bool):
        return value + 1
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ReliabilityContractError("rule output: cannot perturb non-finite float")
        return value + max(1e-6, abs(value) * 0.01)
    if isinstance(value, str):
        return value + "__ALT__"
    if isinstance(value, list):
        if not value:
            raise ReliabilityContractError("rule output: cannot perturb empty list")
        result = list(value)
        result[0] = _perturb_output(result[0])
        return result
    raise ReliabilityContractError(f"rule output: cannot perturb type {type(value).__name__}")


def _canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def _render_prompt(
    *,
    title: str,
    code: str,
    inputs: Mapping[str, object],
    proposed_output: object,
    option_a_semantic: str,
    option_b_semantic: str,
    transformed: bool,
) -> str:
    normalized_inputs = {str(key): _normalize_json_value(value) for key, value in inputs.items()}
    if transformed:
        items = list(normalized_inputs.items())
        items.reverse()
        input_text = json.dumps(dict(items), indent=2, ensure_ascii=True, allow_nan=False)
    else:
        input_text = _canonical_json(normalized_inputs)
    proposal_text = _canonical_json(_normalize_json_value(proposed_output))
    return (
        "TASK: Verify deterministic rule execution.\n"
        f"CALCULATOR: {title}\n"
        "RULE:\n```python\n"
        f"{code}\n"
        "```\n"
        f"INPUTS: {input_text}\n"
        f"PROPOSED_OUTPUT: {proposal_text}\n"
        f"A = {option_a_semantic}\n"
        f"B = {option_b_semantic}\n"
        "Return only A or B.\n"
        "ANSWER:\n"
    )


def _build_example(
    *,
    rule: BoundRule,
    split: str,
    case: Mapping[str, object],
    proposal_matches: bool,
    a_is_match: bool,
    calculator: Callable[..., object],
) -> RuleVerificationExample:
    inputs = case["inputs"]
    if not isinstance(inputs, Mapping):
        raise ReliabilityContractError("case: inputs must be a mapping")
    raw_reference = calculator(**dict(inputs))
    reference = _normalize_json_value(raw_reference)
    proposed = reference if proposal_matches else _perturb_output(reference)
    option_a = "MATCH" if a_is_match else "MISMATCH"
    option_b = "MISMATCH" if a_is_match else "MATCH"
    target_semantic = "MATCH" if proposal_matches else "MISMATCH"
    target_label = "A" if option_a == target_semantic else "B"
    canonical_prompt = _render_prompt(
        title=rule.title,
        code=rule.code,
        inputs=inputs,
        proposed_output=proposed,
        option_a_semantic=option_a,
        option_b_semantic=option_b,
        transformed=False,
    )
    transformed_prompt = _render_prompt(
        title=rule.title,
        code=rule.code,
        inputs=inputs,
        proposed_output=proposed,
        option_a_semantic=option_a,
        option_b_semantic=option_b,
        transformed=True,
    )
    task_payload = {
        "case_id": case["case_id"],
        "split": split,
        "proposal_matches": proposal_matches,
        "a_is_match": a_is_match,
        "reference": reference,
        "proposed": proposed,
        "code_sha256": rule.code_sha256,
    }
    return RuleVerificationExample(
        task_id=_sha256_text(_canonical_json(task_payload)),
        calculator_id=f"pmid:{rule.pmid}",
        pmid=rule.pmid,
        split=split,
        case_id=str(case["case_id"]),
        state_index=int(case["state_index"]),
        code_sha256=rule.code_sha256,
        inputs=dict(inputs),
        reference_output=reference,
        proposed_output=proposed,
        proposal_matches=proposal_matches,
        option_a_semantic=option_a,
        option_b_semantic=option_b,
        target_label=target_label,
        canonical_prompt=canonical_prompt,
        transformed_prompt=transformed_prompt,
    )


def _partition_cases(cases: Sequence[Mapping[str, object]], *, count: int, namespace: str) -> tuple[list[Mapping[str, object]], list[Mapping[str, object]]]:
    ranked = sorted(cases, key=lambda case: (_rank(str(case["case_id"]), namespace), str(case["case_id"])))
    return ranked[:count], ranked[count:]


def materialize_development_examples(rules: Sequence[BoundRule]) -> tuple[RuleVerificationExample, ...]:
    """Materialize only pre-frozen development/calibration examples for S1."""
    examples: list[RuleVerificationExample] = []
    for rule in rules:
        partition = prefreeze_state_partition(f"pmid:{rule.pmid}", rule.prospective_case_space)
        dev_cases = list(cases_from_state_indices(f"pmid:{rule.pmid}", rule.domain_constants, partition["development"]))
        cal_cases = list(cases_from_state_indices(f"pmid:{rule.pmid}", rule.domain_constants, partition["calibration"]))
        train, dev_eval = _partition_cases(dev_cases, count=TRAIN_PER_CALCULATOR, namespace=TRAIN_NAMESPACE)
        cal_tune, cal_eval = _partition_cases(cal_cases, count=CAL_TUNE_PER_CALCULATOR, namespace=CAL_NAMESPACE)
        calculator = compile_bound_rule(rule)
        for split, rows in (("S1_TRAIN", train), ("S1_DEV_EVAL", dev_eval), ("S1_CAL_TUNE", cal_tune), ("S1_CAL_EVAL", cal_eval)):
            proposal_ranked = sorted(rows, key=lambda case: (_rank(str(case["case_id"]), PROPOSAL_NAMESPACE), str(case["case_id"])))
            option_ranked = sorted(rows, key=lambda case: (_rank(str(case["case_id"]), OPTION_NAMESPACE), str(case["case_id"])))
            proposal_match_ids = {str(case["case_id"]) for index, case in enumerate(proposal_ranked) if index % 2 == 0}
            a_match_ids = {str(case["case_id"]) for index, case in enumerate(option_ranked) if index % 2 == 0}
            for case in rows:
                case_id = str(case["case_id"])
                examples.append(
                    _build_example(
                        rule=rule,
                        split=split,
                        case=case,
                        proposal_matches=case_id in proposal_match_ids,
                        a_is_match=case_id in a_match_ids,
                        calculator=calculator,
                    )
                )
    return tuple(examples)


def split_counts(examples: Sequence[RuleVerificationExample]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for example in examples:
        counts[example.split] = counts.get(example.split, 0) + 1
    return dict(sorted(counts.items()))
