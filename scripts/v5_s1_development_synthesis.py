#!/usr/bin/env python3
"""Development-only cross-seed synthesis for CommandMed V5 S1.

This module reads only durable development/calibration evidence already admitted
by the repository. It performs descriptive cross-seed aggregation only. It does
not select margins, access confirmatory/reserve identities, fit interventions,
or promote scientific claims.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from statistics import fmean, stdev
from typing import Any, Iterable

SEEDS = (11, 29, 47)
EVAL_SPLITS = ("S1_DEV_EVAL", "S1_CAL_EVAL")
VARIANTS = ("canonical", "transformed")
METRICS = ("accuracy", "nll", "brier")


class SynthesisError(RuntimeError):
    """Fail-closed synthesis contract error."""


def _read_json(path: Path) -> Any:
    if not path.is_file():
        raise SynthesisError(f"MISSING_REQUIRED_EVIDENCE:{path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _finite(value: Any, label: str) -> float:
    number = float(value)
    if not math.isfinite(number):
        raise SynthesisError(f"NONFINITE_VALUE:{label}")
    return number


def _review_ok(folder: Path, seed: int, intervention: str) -> None:
    receipt = _read_json(folder / "export-verification-receipt.json")
    review = _read_json(folder / "validation-and-review.json")
    required = {
        "seed": seed,
        "intervention": intervention,
        "spend_usd": 0,
        "confirmatory": False,
        "reserve": False,
    }
    if any(receipt.get(k) != v for k, v in required.items()):
        raise SynthesisError(f"INVALID_RECEIPT:{folder.name}")
    if receipt.get("durable_export_verified") is not True:
        raise SynthesisError(f"UNVERIFIED_EXPORT:{folder.name}")
    if review.get("spend_usd") != 0:
        raise SynthesisError(f"INVALID_REVIEW_BOUNDARY:{folder.name}")
    if "confirmatory" in review and review.get("confirmatory") is not False:
        raise SynthesisError(f"INVALID_REVIEW_BOUNDARY:{folder.name}")
    if "reserve" in review and review.get("reserve") is not False:
        raise SynthesisError(f"INVALID_REVIEW_BOUNDARY:{folder.name}")
    if not str(review.get("host_review", "")).startswith("NO_MATERIAL_BLOCKER"):
        raise SynthesisError(f"REVIEW_NOT_QUALIFIED:{folder.name}")


def _analysis_record(intervention: str, seed: int | None, analysis: dict[str, Any]) -> dict[str, Any]:
    if analysis.get("scope") != "DEVELOPMENT_CALIBRATION_ONLY" or analysis.get("not_confirmatory") is not True:
        raise SynthesisError(f"ANALYSIS_SCOPE_MISMATCH:{intervention}:{seed}")
    partitions = analysis.get("partitions")
    js = analysis.get("mean_semantic_js_by_split")
    if not isinstance(partitions, dict) or not isinstance(js, dict):
        raise SynthesisError(f"ANALYSIS_STRUCTURE_MISMATCH:{intervention}:{seed}")
    metrics: dict[str, float] = {}
    for split in EVAL_SPLITS:
        for variant in VARIANTS:
            row = partitions.get(f"{split}/{variant}")
            if not isinstance(row, dict) or int(row.get("count", -1)) != 3840:
                raise SynthesisError(f"PARTITION_MISMATCH:{intervention}:{seed}:{split}:{variant}")
            for metric in METRICS:
                metrics[f"{split}/{variant}/{metric}"] = _finite(
                    row.get(metric), f"{intervention}:{seed}:{split}:{variant}:{metric}"
                )
        metrics[f"{split}/semantic_js"] = _finite(
            js.get(split), f"{intervention}:{seed}:{split}:semantic_js"
        )
    return {"intervention": intervention, "seed": seed, "metrics": metrics}


def _unique_folder(root: Path, pattern: str) -> Path:
    candidates = sorted(root.glob(pattern))
    if len(candidates) != 1:
        raise SynthesisError(f"EXPECTED_ONE_EVIDENCE_FOLDER:{pattern}:{len(candidates)}")
    return candidates[0]


def _summarize_seeded(records: Iterable[dict[str, Any]]) -> dict[str, Any]:
    rows = list(records)
    if [row["seed"] for row in rows] != list(SEEDS):
        raise SynthesisError("SEED_SET_MISMATCH")
    keys = sorted(rows[0]["metrics"])
    if any(sorted(row["metrics"]) != keys for row in rows):
        raise SynthesisError("METRIC_SET_MISMATCH")
    summary: dict[str, Any] = {}
    for key in keys:
        values = [_finite(row["metrics"][key], key) for row in rows]
        summary[key] = {
            "mean": fmean(values),
            "min": min(values),
            "max": max(values),
            "between_seed_sd": stdev(values),
            "values_by_seed": {str(seed): value for seed, value in zip(SEEDS, values)},
        }
    return summary


def _retention_record(folder: Path, seed: int) -> dict[str, float]:
    payload = _read_json(folder / "evidence" / "paired-retention-aggregate.json")
    if payload.get("scope") != "PAIRED_SQUAD_V1_1_ONLY; NOT_GENERAL_CAPABILITY_PRESERVATION":
        raise SynthesisError(f"RETENTION_SCOPE_MISMATCH:{seed}")
    baseline = payload.get("baseline", {})
    candidate = payload.get("candidate", {})
    delta = payload.get("paired_mean_delta", {})
    if baseline.get("count") != 256 or candidate.get("count") != 256:
        raise SynthesisError(f"RETENTION_COUNT_MISMATCH:{seed}")
    return {
        "baseline_exact_match": _finite(baseline.get("exact_match"), f"retention:{seed}:baseline_em"),
        "candidate_exact_match": _finite(candidate.get("exact_match"), f"retention:{seed}:candidate_em"),
        "delta_exact_match": _finite(delta.get("exact_match"), f"retention:{seed}:delta_em"),
        "baseline_token_f1": _finite(baseline.get("token_f1"), f"retention:{seed}:baseline_f1"),
        "candidate_token_f1": _finite(candidate.get("token_f1"), f"retention:{seed}:candidate_f1"),
        "delta_token_f1": _finite(delta.get("token_f1"), f"retention:{seed}:delta_f1"),
    }


def build_synthesis(repo: Path) -> dict[str, Any]:
    development = repo / "artifacts" / "v5" / "development"
    b1_root = development / "s1-colab-resource-qualification" / "b1-complete-2026-10-04"
    baseline = _analysis_record("BASELINE_V1", None, _read_json(b1_root / "baseline-analysis.json"))

    b1_records = [
        _analysis_record("B1_TYPED_V1", seed, _read_json(b1_root / f"b1-seed-{seed}-analysis.json"))
        for seed in SEEDS
    ]

    c1_root = development / "s1-kaggle-adapters"
    c1_records = []
    for seed in SEEDS:
        folder = _unique_folder(c1_root, f"c1-seed-{seed}-v*-*")
        _review_ok(folder, seed, "C1_CRDI_V1")
        c1_records.append(
            _analysis_record("C1_CRDI_V1", seed, _read_json(folder / "evidence" / "adapter-analysis.json"))
        )

    c2_root = development / "s1-kaggle-c2-adapters"
    c2_records = []
    retention = []
    for seed in SEEDS:
        folder = _unique_folder(c2_root, f"c2-seed-{seed}-v*-*")
        _review_ok(folder, seed, "C2_CRDI_RETAIN_V1")
        c2_records.append(
            _analysis_record("C2_CRDI_RETAIN_V1", seed, _read_json(folder / "evidence" / "adapter-analysis.json"))
        )
        retention.append({"seed": seed, **_retention_record(folder, seed)})

    retention_summary: dict[str, Any] = {}
    for key in [k for k in retention[0] if k != "seed"]:
        values = [_finite(row[key], f"retention:{key}") for row in retention]
        retention_summary[key] = {
            "mean": fmean(values),
            "min": min(values),
            "max": max(values),
            "between_seed_sd": stdev(values),
            "values_by_seed": {str(seed): value for seed, value in zip(SEEDS, values)},
        }

    return {
        "schema": "commandmed.v5.s1-development-synthesis.v1",
        "scope": "DEVELOPMENT_CALIBRATION_ONLY",
        "confirmatory": False,
        "reserve": False,
        "claim_promotion": False,
        "seeds": list(SEEDS),
        "baseline": baseline,
        "learned_interventions": {
            "B1_TYPED_V1": {"records": b1_records, "cross_seed": _summarize_seeded(b1_records)},
            "C1_CRDI_V1": {"records": c1_records, "cross_seed": _summarize_seeded(c1_records)},
            "C2_CRDI_RETAIN_V1": {"records": c2_records, "cross_seed": _summarize_seeded(c2_records)},
        },
        "c2_retention": {"records": retention, "cross_seed": retention_summary},
        "interpretation_boundary": (
            "Descriptive development-only synthesis. Between-seed SD is a training-randomness nuisance "
            "summary, not unchanged-base repeatability95, not a meaningful-effect margin, and not confirmatory inference."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = build_synthesis(args.repo.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": "PASS_DEVELOPMENT_SYNTHESIS", "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
