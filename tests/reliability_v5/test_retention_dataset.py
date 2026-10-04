import hashlib

import pytest

from commandmed.reliability_v5 import retention_dataset as retention


def rows():
    return [{"id": str(index), "context": "Public fixture passage", "question": "Fixture question?", "answers": {"text": ["fixture"]}} for index in range(320)]


def test_roles_follow_protocol_raw_id_hash_and_are_order_independent():
    source = rows()
    left = retention.select_roles(source, expected_count=320)
    right = retention.select_roles(source[::-1], expected_count=320)
    ranked = sorted(source, key=lambda row: (hashlib.sha256(row["id"].encode()).hexdigest(), row["id"]))
    assert left == right == (ranked[:64], ranked[64:320])
    assert not ({row["id"] for row in left[0]} & {row["id"] for row in left[1]})


@pytest.mark.parametrize("kind", ["count", "duplicate", "missing"])
def test_invalid_source_pool_fails_closed(kind):
    source = rows()
    if kind == "count":
        source.pop()
    elif kind == "duplicate":
        source[-1]["id"] = source[0]["id"]
    else:
        source[0]["id"] = ""
    with pytest.raises(ValueError):
        retention.select_roles(source, expected_count=320)


def test_prompt_excludes_gold_and_has_fixed_newline_marker():
    source = rows()[0]
    source["answers"]["text"] = ["SHOULD_NOT_LEAK"]
    prompt = retention.render_prompt(source)
    assert "SHOULD_NOT_LEAK" not in prompt and prompt.endswith("ANSWER:\n")


@pytest.mark.parametrize("prediction,answers,expected", [
    ("The U.S.", ["US"], (1, 1)),
    ("red blue", ["blue green", "red blue"], (1, 1)),
    ("red", ["red blue"], (0, 2/3)),
    ("", ["the"], (1, 1)),
    ("other", ["answer"], (0, 0)),
])
def test_official_squad_normalization_and_max_over_annotations(prediction, answers, expected):
    assert retention.score_answer(prediction, answers) == expected


def test_completion_span_is_frozen_first_nonempty_line():
    assert retention.prediction_span("\n short answer\nmore text") == "short answer"
    assert retention.prediction_span("\n ") == ""


def test_context_bound_rejects_complete_prompt_without_truncation():
    class Tokenizer:
        def encode(self, text, **kwargs):
            assert kwargs == {"add_special_tokens": False}
            return list(range(len(text)))
    with pytest.raises(ValueError, match="CONTEXT_BOUND"):
        retention.prepare_row(rows()[0], Tokenizer(), maintenance=False, context_bound=32)


def test_gold_prefix_retokenization_is_rejected():
    class Tokenizer:
        def encode(self, text, **kwargs):
            return [1, 2] if text.endswith("ANSWER:\n") else [3, 4, 5]
    with pytest.raises(ValueError, match="PREFIX_RETOKENIZATION"):
        retention.prepare_row(rows()[0], Tokenizer(), maintenance=True, context_bound=100)
