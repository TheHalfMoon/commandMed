"""Pinned S1 retention identity, prompting and official SQuAD scoring mechanics.

No network or model calls. Source payloads remain external to the repository.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import re
import string
from collections.abc import Mapping, Sequence

SOURCE_REPO = "rajpurkar/squad"
SOURCE_REVISION = "7b6d24c440a36b6815f21b70d25016731768db1f"
SOURCE_FILE = "plain_text/validation-00000-of-00001.parquet"
SOURCE_FILE_SHA256 = "8c6646d36bd5a95061e076788cf3161d11f6f3e7d625dac7a83bbed0a49f69f7"
SOURCE_NAMESPACE = SOURCE_REPO + "@" + SOURCE_REVISION + "/validation"
MAX_ANSWER_TOKENS = 32
MAINTENANCE_GOLD_TOKENS = 8
OFFICIAL_V1_SCORER_PORT_GIT_BLOB = "e60acfd1044319e43a59ffe8db75e63b68785ba7"
QA_PROMPT_TEMPLATE = (
    "Answer the question using a short span from the passage.\n"
    "PASSAGE:\n{context}\nQUESTION:\n{question}\nANSWER:\n"
)


def select_roles(rows: Sequence[Mapping], *, expected_count: int = 10570) -> tuple[list, list]:
    """Protocol section 8: SHA256 of raw upstream ID, within the pinned namespace.

    The namespace identifies the source pool; no unapproved hash suffix is added.
    """
    if len(rows) != expected_count or len(rows) < 320:
        raise ValueError("SQUAD_VALIDATION_CARDINALITY_MISMATCH")
    ids = [row.get("id") for row in rows]
    if any(not isinstance(identity, str) or not identity for identity in ids):
        raise ValueError("SQUAD_INVALID_UPSTREAM_ID")
    if len(set(ids)) != len(ids):
        raise ValueError("SQUAD_DUPLICATE_UPSTREAM_ID")
    ranked = sorted(rows, key=lambda row: (hashlib.sha256(row["id"].encode("utf-8")).hexdigest(), row["id"]))
    return ranked[:64], ranked[64:320]


def render_prompt(row: Mapping) -> str:
    context, question = row.get("context"), row.get("question")
    if not isinstance(context, str) or not context or not isinstance(question, str) or not question:
        raise ValueError("SQUAD_CONTEXT_OR_QUESTION_INVALID")
    return QA_PROMPT_TEMPLATE.format(context=context, question=question)


def gold_answers(row: Mapping) -> list[str]:
    answers = row.get("answers")
    texts = answers.get("text") if isinstance(answers, Mapping) else None
    if not isinstance(texts, (list, tuple)) or not texts or any(not isinstance(text, str) or not text for text in texts):
        raise ValueError("SQUAD_GOLD_ANSWER_INVALID")
    return list(texts)


def prepare_row(row: Mapping, tokenizer, *, maintenance: bool, context_bound: int) -> dict:
    """Validate the complete untruncated prompt and prefix-preserving gold anchor."""
    prompt = render_prompt(row)
    ids = tokenizer.encode(prompt, add_special_tokens=False)
    answers = gold_answers(row)
    record = {"source_id": row["id"], "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(), "prompt_tokens": len(ids)}
    if not ids or len(ids) + MAX_ANSWER_TOKENS > context_bound:
        raise ValueError("SQUAD_MODEL_CONTEXT_BOUND_EXCEEDED")
    if maintenance:
        combined = tokenizer.encode(prompt + answers[0], add_special_tokens=False)
        if combined[:len(ids)] != ids:
            raise ValueError("SQUAD_GOLD_PREFIX_RETOKENIZATION")
        suffix = combined[len(ids):][:MAINTENANCE_GOLD_TOKENS]
        if not suffix:
            raise ValueError("SQUAD_EMPTY_GOLD_TOKEN_ANCHOR")
        record["gold_anchor_tokens"] = len(suffix)
        record["gold_anchor_token_ids_sha256"] = hashlib.sha256(str(suffix).encode("ascii")).hexdigest()
    return record


def normalized_answer(text: str) -> str:
    text = "".join(char for char in text.lower() if char not in string.punctuation)
    return " ".join(re.sub(r"\b(a|an|the)\b", " ", text).split())


def prediction_span(decoded: str) -> str:
    # Fixed before outputs: score the first nonempty completion line only.
    stripped = decoded.strip()
    return stripped.splitlines()[0].strip() if stripped else ""


def score_answer(prediction: str, answers: Sequence[str]) -> tuple[float, float]:
    if not answers:
        raise ValueError("SQUAD_NO_GOLD_FOR_SCORING")
    predicted = normalized_answer(prediction)
    p_tokens = predicted.split()
    em, f1 = 0.0, 0.0
    for answer in answers:
        gold = normalized_answer(answer)
        g_tokens = gold.split()
        em = max(em, float(predicted == gold))
        common = sum((Counter(p_tokens) & Counter(g_tokens)).values())
        # Official v1.1 returns zero when there are no common tokens, including
        # two strings normalized to empty; v2's empty-answer rule is different.
        if common == 0:
            item_f1 = 0.0
        else:
            precision, recall = common / len(p_tokens), common / len(g_tokens)
            item_f1 = 2 * precision * recall / (precision + recall)
        f1 = max(f1, item_f1)
    return em, f1
