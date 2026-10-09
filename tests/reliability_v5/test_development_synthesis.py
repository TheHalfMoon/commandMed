from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_s1_development_synthesis as synthesis


def _write(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def _analysis(offset: float = 0.0) -> dict:
    partitions = {}
    for split in synthesis.EVAL_SPLITS:
        for variant_index, variant in enumerate(synthesis.VARIANTS):
            partitions[f"{split}/{variant}"] = {
                "count": 3840,
                "accuracy": 0.5 + offset,
                "nll": 0.7 + offset + variant_index * 0.01,
                "brier": 0.5 + offset,
            }
    return {
        "scope": "DEVELOPMENT_CALIBRATION_ONLY",
        "not_confirmatory": True,
        "clinical_validity": False,
        "partitions": partitions,
        "mean_semantic_js_by_split": {split: 0.001 + offset for split in synthesis.EVAL_SPLITS},
    }


def _reviewed_folder(root: Path, name: str, seed: int, intervention: str, offset: float) -> Path:
    folder = root / name
    _write(folder / "export-verification-receipt.json", {
        "seed": seed,
        "intervention": intervention,
        "spend_usd": 0,
        "confirmatory": False,
        "reserve": False,
        "durable_export_verified": True,
    })
    _write(folder / "validation-and-review.json", {
        "spend_usd": 0,
        "confirmatory": False,
        "reserve": False,
        "host_review": "NO_MATERIAL_BLOCKER; fixture",
    })
    _write(folder / "evidence" / "adapter-analysis.json", _analysis(offset))
    return folder


def _fixture_repo(tmp_path: Path) -> Path:
    development = tmp_path / "artifacts" / "v5" / "development"
    b1 = development / "s1-colab-resource-qualification" / "b1-complete-2026-10-04"
    _write(b1 / "baseline-analysis.json", _analysis())
    for index, seed in enumerate(synthesis.SEEDS):
        _write(b1 / f"b1-seed-{seed}-analysis.json", _analysis(0.001 * (index + 1)))

    c1_root = development / "s1-kaggle-adapters"
    c2_root = development / "s1-kaggle-c2-adapters"
    for index, seed in enumerate(synthesis.SEEDS):
        _reviewed_folder(
            c1_root, f"c1-seed-{seed}-v1-2026-10-09", seed, "C1_CRDI_V1", 0.002 * (index + 1)
        )
        c2 = _reviewed_folder(
            c2_root, f"c2-seed-{seed}-v1-2026-10-09", seed, "C2_CRDI_RETAIN_V1", 0.003 * (index + 1)
        )
        _write(c2 / "evidence" / "paired-retention-aggregate.json", {
            "scope": "PAIRED_SQUAD_V1_1_ONLY; NOT_GENERAL_CAPABILITY_PRESERVATION",
            "baseline": {"count": 256, "exact_match": 0.20, "token_f1": 0.31},
            "candidate": {"count": 256, "exact_match": 0.20, "token_f1": 0.30 + index * 0.001},
            "paired_mean_delta": {"exact_match": 0.0, "token_f1": -0.01 + index * 0.001},
        })
    return tmp_path


def test_build_synthesis_is_development_only_and_seed_complete(tmp_path: Path) -> None:
    payload = synthesis.build_synthesis(_fixture_repo(tmp_path))
    assert payload["scope"] == "DEVELOPMENT_CALIBRATION_ONLY"
    assert payload["confirmatory"] is False
    assert payload["reserve"] is False
    assert payload["claim_promotion"] is False
    assert payload["seeds"] == [11, 29, 47]
    c2 = payload["learned_interventions"]["C2_CRDI_RETAIN_V1"]
    assert [row["seed"] for row in c2["records"]] == [11, 29, 47]
    key = "S1_DEV_EVAL/canonical/accuracy"
    assert c2["cross_seed"][key]["values_by_seed"]["11"] == pytest.approx(0.503)
    assert c2["cross_seed"][key]["between_seed_sd"] > 0.0
    assert payload["c2_retention"]["cross_seed"]["delta_token_f1"]["mean"] == pytest.approx(-0.009)


def test_missing_c2_seed_fails_closed(tmp_path: Path) -> None:
    repo = _fixture_repo(tmp_path)
    target = repo / "artifacts" / "v5" / "development" / "s1-kaggle-c2-adapters" / "c2-seed-47-v1-2026-10-09"
    for path in sorted(target.rglob("*"), reverse=True):
        if path.is_file():
            path.unlink()
        else:
            path.rmdir()
    target.rmdir()
    with pytest.raises(synthesis.SynthesisError, match="EXPECTED_ONE_EVIDENCE_FOLDER"):
        synthesis.build_synthesis(repo)


def test_unreviewed_seed_fails_closed(tmp_path: Path) -> None:
    repo = _fixture_repo(tmp_path)
    review = (
        repo / "artifacts" / "v5" / "development" / "s1-kaggle-adapters"
        / "c1-seed-29-v1-2026-10-09" / "validation-and-review.json"
    )
    payload = json.loads(review.read_text(encoding="utf-8"))
    payload["host_review"] = "BLOCKED"
    _write(review, payload)
    with pytest.raises(synthesis.SynthesisError, match="REVIEW_NOT_QUALIFIED"):
        synthesis.build_synthesis(repo)
