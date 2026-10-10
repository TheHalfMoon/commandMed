"""Synthetic regressions for original-source V5 case/task pairing audit."""
from __future__ import annotations

from pathlib import Path
import hashlib
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import scripts.v5_s1_source_case_pairing_audit as audit


class Example:
    def __init__(self, task: str = "taskA", case_id: str = "caseA", state: int = 0,
                 split: str = "S1_DEV_EVAL") -> None:
        self.task_id = task
        self.case_id = case_id
        self.state_index = state
        self.calculator_id = "pmid:known"
        self.split = split
        self.target_label = "A"
        self.option_a_semantic = "MATCH"
        self.canonical_prompt = "Canonical A"
        self.transformed_prompt = "Transformed A"


def _rows(ex: Example) -> list[dict]:
    return [{
        "task_id": ex.task_id,
        "calculator_id": ex.calculator_id,
        "split": ex.split,
        "variant": variant,
        "target_index": 0,
        "option_a_semantic": ex.option_a_semantic,
        "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "logits": [1.0, 0.0],
    } for variant, prompt in (("canonical", ex.canonical_prompt),
                             ("transformed", ex.transformed_prompt))]


def test_synthetic_source_and_pairing_accept_original_identity() -> None:
    ex = Example()
    audit.verify_model_output_pairing([ex], _rows(ex))


@pytest.mark.parametrize("field,wrong", [
    ("task_id", "wrong-task"), ("calculator_id", "pmid:other"),
    ("split", "S1_CAL_EVAL"), ("target_index", 1), ("option_a_semantic", "MISMATCH"),
    ("prompt_sha256", "0" * 64), ("variant", "incorrect")
])
def test_reject_changed_task_or_prompt_identity(field: str, wrong: object) -> None:
    ex = Example()
    rows = _rows(ex)
    rows[0][field] = wrong
    with pytest.raises(audit.SourceCaseAuditError, match="SOURCE_TO_PROMPT_BINDING_MISMATCH"):
        audit.verify_model_output_pairing([ex], rows)


def test_reject_duplicate_or_missing_prompt_pair() -> None:
    ex = Example()
    with pytest.raises(audit.SourceCaseAuditError, match="PROMPT_VARIANT_COUNT_MISMATCH"):
        audit.verify_model_output_pairing([ex], _rows(ex)[:1])
    rows = _rows(ex)
    rows[1] = rows[0].copy()
    with pytest.raises(audit.SourceCaseAuditError, match="SOURCE_TO_PROMPT_BINDING_MISMATCH"):
        audit.verify_model_output_pairing([ex], rows)


def test_fail_closed_source_file_identity(tmp_path: Path) -> None:
    path = tmp_path / "source.json"
    path.write_text("not-pinned-content", encoding="utf-8")
    with pytest.raises(audit.SourceCaseAuditError, match="PINNED_SOURCE_SHA_MISMATCH"):
        audit.audit(path)
    with pytest.raises(audit.SourceCaseAuditError, match="PINNED_PUBLIC_SOURCE_REQUIRED"):
        audit.audit(tmp_path / "not-there")


@pytest.mark.parametrize("mutation,reason", [
    ("case_id", "SOURCE_CASE_ID_REUSED"),
    ("task_id", "TASK_ID_REUSED"),
    ("state_index", "CALCULATOR_STATE_REUSED"),
])
def test_source_case_pseudoreplication_is_rejected(mutation: str, reason: str) -> None:
    # Fixed full-case cardinality is checked before collision detection.
    cases = [Example(task=f"task-{i}", case_id=f"case-{i}", state=i)
             for i in range(8192)]
    setattr(cases[-1], mutation, getattr(cases[0], mutation))
    with pytest.raises(audit.SourceCaseAuditError, match=reason):
        audit.verify_unique_case_unit(cases)
