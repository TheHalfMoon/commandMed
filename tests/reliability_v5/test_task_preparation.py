"""Regression checks for fail-closed frozen answer-prefix token qualification."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

PATH = Path(__file__).resolve().parents[2] / "docs/research/paper-rebuild-v2-2026-10-02/execution_tools/prepare_s1_tasks.py"
SPEC = importlib.util.spec_from_file_location("v5_prepare_s1_tasks", PATH)
assert SPEC is not None and SPEC.loader is not None
PREPARE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PREPARE)


class FixtureTokenizer:
    def __init__(self, prefix_ids, full_ids, prefix="ANSWER: "):
        self.prefix_ids = prefix_ids
        self.full_ids = full_ids
        self.prefix = prefix

    def __call__(self, text, *, add_special_tokens):
        assert not add_special_tokens
        return {"input_ids": self.prefix_ids if text == self.prefix else self.full_ids}


def test_retokenized_prefix_is_rejected_even_with_one_suffix_token():
    tokenizer = FixtureTokenizer([100, 200, 300], [100, 200, 357])
    check = PREPARE.candidate_token_check(tokenizer, "ANSWER: ", "A")
    assert check["suffix_ids"] == [357]
    assert check["prefix_preserved"] is False
    assert check["valid"] is False
    with pytest.raises(SystemExit, match="CANDIDATE_TOKEN_NOT_SINGLE"):
        PREPARE.candidate_suffix_id(tokenizer, "ANSWER: ", "A")


@pytest.mark.parametrize("full_ids", [[100, 200], [100, 200, 357, 358]])
def test_empty_or_multiple_candidate_tokens_are_rejected(full_ids):
    tokenizer = FixtureTokenizer([100, 200], full_ids)
    with pytest.raises(SystemExit, match="CANDIDATE_TOKEN_NOT_SINGLE"):
        PREPARE.candidate_suffix_id(tokenizer, "ANSWER: ", "A")


def test_preserved_prefix_and_single_candidate_are_admitted():
    tokenizer = FixtureTokenizer([100, 200], [100, 200, 357])
    assert PREPARE.candidate_suffix_id(tokenizer, "ANSWER: ", "A") == 357


@pytest.mark.parametrize("label, token", [("A", 32), ("B", 33)])
def test_approved_newline_preserves_prefix_and_candidate(label, token):
    prefix_ids = [11355, 38050, 25, 198]
    tokenizer = FixtureTokenizer(prefix_ids, prefix_ids + [token], prefix="ANSWER:\n")
    assert PREPARE.candidate_suffix_id(tokenizer, "ANSWER:\n", label) == token


def test_failed_candidate_checks_are_persisted_and_main_returns_failure(monkeypatch, tmp_path):
    source = tmp_path / "source.json"
    source.write_bytes(b"fixture")
    manifest = tmp_path / "manifest.json"
    manifest.write_text("{}", encoding="utf-8")
    model = tmp_path / "model"
    model.mkdir()
    for name in ("tokenizer.json", "tokenizer_config.json", "vocab.json", "merges.txt"):
        (model / name).write_text("fixture", encoding="utf-8")
    tokenizer = FixtureTokenizer([100, 200, 300], [100, 200, 357], prefix="ANSWER:\n")
    def from_pretrained(path, *, local_files_only):
        assert path == model and local_files_only
        return tokenizer
    monkeypatch.setitem(sys.modules, "transformers", SimpleNamespace(AutoTokenizer=SimpleNamespace(from_pretrained=from_pretrained)))
    monkeypatch.setattr(PREPARE, "MANIFEST_PATH", manifest)
    monkeypatch.setattr(PREPARE, "OUT_DIR", tmp_path / "evidence")
    monkeypatch.setattr(PREPARE, "EXPECTED_SPLITS", {"S1_TRAIN": 1})
    monkeypatch.setattr(PREPARE.importlib.metadata, "version", lambda name: "fixture")
    monkeypatch.setattr(PREPARE, "bind_selected_rules", lambda **kwargs: ("fixture-rule",))
    example = SimpleNamespace(task_id="a" * 64, pmid="12345678", split="S1_TRAIN", canonical_prompt="canonical", transformed_prompt="transformed", target_label="A", proposal_matches=True)
    monkeypatch.setattr(PREPARE, "materialize_development_examples", lambda rules: (example,))
    monkeypatch.setattr(sys, "argv", [str(PATH), "--riskcalcs-source", str(source), "--model-dir", str(model)])
    assert PREPARE.main() == 2
    evidence = json.loads((tmp_path / "evidence/task-preparation-evidence.json").read_text())
    assert evidence["status"] == "FAILED_PRE_MODEL_INTERFACE"
    assert evidence["candidate_token_failures"] == ["A", "B"]
    assert evidence["tokenizer_candidate_ids"] == {"A": None, "B": None}
    assert evidence["overlength_count"] == 0
    assert evidence["model_loaded"] is False
