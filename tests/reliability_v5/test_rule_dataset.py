from __future__ import annotations

import hashlib
import json

import pytest

from src.commandmed.reliability_v5.contracts import ReliabilityContractError
from src.commandmed.reliability_v5 import rule_dataset


def _fixture_source(code: str) -> bytes:
    payload = {
        "12345678": {
            "title": "Synthetic deterministic score",
            "computation": f"```python\n{code}\n```",
        }
    }
    return json.dumps(payload, sort_keys=True).encode("utf-8")


def _fixture_code() -> str:
    return """def synthetic_score(a, b, c, d, e):
    score = 0
    if a > 1:
        score += 1
    if b > 2:
        score += 1
    if c > 3:
        score += 1
    if d > 4:
        score += 1
    if e > 5:
        score += 1
    return score"""


def _fixture_manifest(source: bytes, code: str) -> dict[str, object]:
    return {
        "source_bytes_sha256": hashlib.sha256(source).hexdigest(),
        "selected": [
            {
                "pmid": "12345678",
                "title": "Synthetic deterministic score",
                "function_name": "synthetic_score",
                "code_sha256": hashlib.sha256(code.encode("utf-8")).hexdigest(),
                "domain_constants": {
                    "a": [1],
                    "b": [2],
                    "c": [3],
                    "d": [4],
                    "e": [5],
                },
                "prospective_case_space": 3125,
            }
        ],
    }


def _bind_fixture(monkeypatch: pytest.MonkeyPatch):
    code = _fixture_code()
    source = _fixture_source(code)
    manifest = _fixture_manifest(source, code)
    monkeypatch.setattr(rule_dataset, "FROZEN_SOURCE_SHA256", hashlib.sha256(source).hexdigest())
    return rule_dataset.bind_selected_rules(
        source_bytes=source,
        selection_manifest=manifest,
        require_count=1,
    )


def test_bind_selected_rules_requires_exact_source_and_code(monkeypatch: pytest.MonkeyPatch) -> None:
    rules = _bind_fixture(monkeypatch)
    assert len(rules) == 1
    assert rules[0].pmid == "12345678"
    assert rules[0].function_name == "synthetic_score"


def test_source_hash_mismatch_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    code = _fixture_code()
    source = _fixture_source(code)
    manifest = _fixture_manifest(source, code)
    monkeypatch.setattr(rule_dataset, "FROZEN_SOURCE_SHA256", "0" * 64)
    with pytest.raises(ReliabilityContractError, match="source SHA-256 mismatch"):
        rule_dataset.bind_selected_rules(
            source_bytes=source,
            selection_manifest=manifest,
            require_count=1,
        )


def test_unexpected_call_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    code = """def synthetic_score(a, b, c, d, e):
    return abs(a)"""
    source = _fixture_source(code)
    manifest = _fixture_manifest(source, code)
    monkeypatch.setattr(rule_dataset, "FROZEN_SOURCE_SHA256", hashlib.sha256(source).hexdigest())
    with pytest.raises(ReliabilityContractError, match="only np.exp calls are allowed"):
        rule_dataset.bind_selected_rules(
            source_bytes=source,
            selection_manifest=manifest,
            require_count=1,
        )


def test_materialization_uses_only_development_and_calibration(monkeypatch: pytest.MonkeyPatch) -> None:
    rules = _bind_fixture(monkeypatch)
    examples = rule_dataset.materialize_development_examples(rules)
    assert rule_dataset.split_counts(examples) == {
        "S1_CAL_EVAL": 60,
        "S1_CAL_TUNE": 4,
        "S1_DEV_EVAL": 60,
        "S1_TRAIN": 4,
    }
    assert len(examples) == 128
    assert all("CONFIRMATORY" not in example.split for example in examples)
    assert all("RESERVE" not in example.split for example in examples)

    by_split: dict[str, list[rule_dataset.RuleVerificationExample]] = {}
    for example in examples:
        by_split.setdefault(example.split, []).append(example)
        assert example.canonical_prompt != example.transformed_prompt
        assert example.target_label in {"A", "B"}
        assert example.option_a_semantic != example.option_b_semantic

    for rows in by_split.values():
        assert sum(example.proposal_matches for example in rows) == len(rows) // 2
        assert sum(example.option_a_semantic == "MATCH" for example in rows) == len(rows) // 2


def test_rule_execution_reference_and_perturbation_are_distinct(monkeypatch: pytest.MonkeyPatch) -> None:
    rules = _bind_fixture(monkeypatch)
    examples = rule_dataset.materialize_development_examples(rules)
    positives = [example for example in examples if example.proposal_matches]
    negatives = [example for example in examples if not example.proposal_matches]
    assert positives and negatives
    assert all(example.reference_output == example.proposed_output for example in positives)
    assert all(example.reference_output != example.proposed_output for example in negatives)
