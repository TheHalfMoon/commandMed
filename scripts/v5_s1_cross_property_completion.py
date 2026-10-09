#!/usr/bin/env python3
"""Complete development-only V5 S1 cross-property diagnostics.

The analysis consumes already-durable matrices and prospectively frozen
post-processing parameters. It performs no model call and no parameter tuning.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Callable, Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SCRIPTS = REPO_ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import v5_s1_postprocessing_development as post

POSTPROCESSING_REL = Path(
    "artifacts/v5/development/s1-postprocessing-results-2026-10-09/"
    "development-postprocessing.json"
)
POSTPROCESSING_SHA256 = (
    "51a4f0709620b48995d887fb2956c9c2fe0836ad37b286a2cddfd65e87979893"
)
FIXED_D1_THRESHOLD = 0.8933094060543488
SEEDS = (11, 29, 47)


class CrossPropertyError(RuntimeError):
    """Fail-closed cross-property completion error."""


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_json(path: Path) -> Any:
    if not path.is_file():
        raise CrossPropertyError(f"MISSING_REQUIRED_FILE:{path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _complete_rows(path: Path) -> list[dict[str, Any]]:
    payload = _load_json(path)
    try:
        return post.validate_complete_matrix(payload)
    except post.PostprocessingError as exc:
        raise CrossPropertyError(f"INVALID_DECISION_MATRIX:{path}:{exc}") from exc


def _reviewed_seed_folder(
    root: Path,
    *,
    prefix: str,
    seed: int,
    expected_status: str,
    intervention: str,
) -> Path:
    valid: list[Path] = []
    for folder in sorted(root.glob(f"{prefix}-seed-{seed}-v*-*")):
        receipt_path = folder / "export-verification-receipt.json"
        review_path = folder / "validation-and-review.json"
        matrix_path = folder / "evidence" / "adapter-decision-matrix.json"
        if not (receipt_path.is_file() and review_path.is_file() and matrix_path.is_file()):
            continue
        receipt = _load_json(receipt_path)
        review = _load_json(review_path)
        if (
            receipt.get("status") == expected_status
            and receipt.get("seed") == seed
            and receipt.get("intervention") == intervention
            and receipt.get("durable_export_verified") is True
            and review.get("spend_usd") == 0
            and str(review.get("host_review", "")).startswith("NO_MATERIAL_BLOCKER")
        ):
            valid.append(folder)
    if len(valid) != 1:
        raise CrossPropertyError(
            f"EXPECTED_ONE_REVIEWED_{prefix.upper()}_SEED:{seed}:{len(valid)}"
        )
    return valid[0]


def _fixed_d1(
    rows: Sequence[dict[str, Any]],
    transform: Callable[[dict[str, Any]], Sequence[float]],
    *,
    threshold: float,
) -> dict[str, Any]:
    if not math.isfinite(threshold) or threshold != FIXED_D1_THRESHOLD:
        raise CrossPropertyError("D1_THRESHOLD_NOT_FROZEN_VALUE")
    result: dict[str, Any] = {}
    for split in post.EVAL_SPLITS:
        split_result: dict[str, Any] = {}
        for variant in post.VARIANTS:
            chosen = post._rows(rows, split, variant)
            if len(chosen) != post.SPLIT_COUNTS[split]:
                raise CrossPropertyError(f"D1_ROW_COUNT_MISMATCH:{split}:{variant}")
            scores: list[float] = []
            losses: list[float] = []
            for row in chosen:
                display = tuple(float(value) for value in transform(row))
                if len(display) != 2 or any(
                    not math.isfinite(value) or value < 0.0 for value in display
                ):
                    raise CrossPropertyError("D1_NONFINITE_OR_NEGATIVE_PROBABILITY")
                semantic = post._semantic_probabilities(display, row)
                score = max(semantic)
                prediction = 0 if semantic[0] >= semantic[1] else 1
                loss = 0.0 if prediction == post._semantic_target(row) else 1.0
                scores.append(score)
                losses.append(loss)
            accepted_losses = [
                loss for score, loss in zip(scores, losses) if score >= threshold
            ]
            curve = post._aurc_tie_block(scores, losses)
            split_result[variant] = {
                "threshold": threshold,
                "accepted": len(accepted_losses),
                "total": len(chosen),
                "coverage": len(accepted_losses) / len(chosen),
                "risk": (
                    math.fsum(accepted_losses) / len(accepted_losses)
                    if accepted_losses
                    else None
                ),
                "aurc_step_tie_block": curve["aurc_step_tie_block"],
                "risk_coverage_curve": curve["curve"],
            }
        result[split] = split_result
    return result


def _bundle(
    rows: Sequence[dict[str, Any]],
    transform: Callable[[dict[str, Any]], Sequence[float]],
) -> dict[str, Any]:
    return {
        "assurance_summary": post._condition_metrics(rows, transform),
        "fixed_d1": _fixed_d1(rows, transform, threshold=FIXED_D1_THRESHOLD),
    }


def _transforms_from_frozen_artifact(
    payload: dict[str, Any],
) -> dict[str, Callable[[dict[str, Any]], Sequence[float]]]:
    tuning = payload.get("tuning")
    if not isinstance(tuning, dict):
        raise CrossPropertyError("POSTPROCESSING_TUNING_MISSING")

    d1 = tuning.get("D1_DEFER_V1")
    if (
        not isinstance(d1, dict)
        or d1.get("threshold") != FIXED_D1_THRESHOLD
        or d1.get("risk_target") != post.D1_RISK_TARGET
    ):
        raise CrossPropertyError("POSTPROCESSING_D1_BINDING_MISMATCH")

    a1_fit = tuning.get("A1_TS_V1")
    a2_fit = tuning.get("A2_SELBIAS_V1")
    a1a2_fit = tuning.get("A1_THEN_A2")
    a2a1_fit = tuning.get("A2_THEN_A1")
    if not all(isinstance(value, dict) for value in (a1_fit, a2_fit, a1a2_fit, a2a1_fit)):
        raise CrossPropertyError("POSTPROCESSING_TRANSFORM_BINDING_MISSING")

    a1_temperature = float(a1_fit["temperature"])
    a2_prior = tuple(float(value) for value in a2_fit["display_slot_prior"])
    a1a2_prior = tuple(
        float(value) for value in a1a2_fit["display_slot_prior_after_a1"]
    )
    a2a1_temperature = float(a2a1_fit["temperature_after_a2"]["temperature"])
    if (
        len(a2_prior) != 2
        or len(a1a2_prior) != 2
        or any(not math.isfinite(value) or value <= 0.0 for value in (a1_temperature, a2a1_temperature))
    ):
        raise CrossPropertyError("POSTPROCESSING_TRANSFORM_BINDING_INVALID")

    def baseline(row: dict[str, Any]) -> tuple[float, float]:
        return post._baseline_transform(row)

    def a1(row: dict[str, Any]) -> tuple[float, float]:
        return post._a1_display(row, a1_temperature)

    def a2(row: dict[str, Any]) -> tuple[float, float]:
        return post.debias_display_distribution(
            post._baseline_transform(row), a2_prior, epsilon=1e-12
        )

    def a1_then_a2(row: dict[str, Any]) -> tuple[float, float]:
        return post.debias_display_distribution(a1(row), a1a2_prior, epsilon=1e-12)

    def a2_then_a1(row: dict[str, Any]) -> tuple[float, float]:
        corrected = a2(row)
        logs = tuple(math.log(value) for value in corrected)
        return post.softmax(
            (logs[0] / a2a1_temperature, logs[1] / a2a1_temperature)
        )

    return {
        "BASELINE_V1": baseline,
        "A1_TS_V1": a1,
        "A2_SELBIAS_V1": a2,
        "A1_THEN_A2": a1_then_a2,
        "A2_THEN_A1": a2_then_a1,
    }


def _assert_matches_canonical_postprocessing(
    frozen: dict[str, Any],
    condition: str,
    bundle: dict[str, Any],
) -> None:
    expected = frozen.get("results", {}).get(condition)
    if expected is None:
        raise CrossPropertyError(f"CANONICAL_POSTPROCESSING_RESULT_MISSING:{condition}")
    actual = bundle["assurance_summary"]
    if post.json.dumps(actual, sort_keys=True, separators=(",", ":")) != post.json.dumps(
        expected, sort_keys=True, separators=(",", ":")
    ):
        raise CrossPropertyError(f"CANONICAL_POSTPROCESSING_REPRODUCTION_MISMATCH:{condition}")


def analyze(repo: Path) -> dict[str, Any]:
    post_path = repo / POSTPROCESSING_REL
    if _sha(post_path) != POSTPROCESSING_SHA256:
        raise CrossPropertyError("CANONICAL_POSTPROCESSING_HASH_MISMATCH")
    frozen = _load_json(post_path)
    if (
        frozen.get("scope") != "DEVELOPMENT_CALIBRATION_ONLY"
        or frozen.get("confirmatory") is not False
        or frozen.get("reserve") is not False
        or frozen.get("claim_promotion") is not False
    ):
        raise CrossPropertyError("CANONICAL_POSTPROCESSING_SCOPE_MISMATCH")

    baseline_path = (
        repo
        / "artifacts/v5/development/s1-colab-resource-qualification/"
        "b1-complete-2026-10-04/baseline-decision-matrix.json"
    )
    baseline_rows = _complete_rows(baseline_path)
    transforms = _transforms_from_frozen_artifact(frozen)

    deterministic: dict[str, Any] = {}
    for name, transform in transforms.items():
        bundle = _bundle(baseline_rows, transform)
        _assert_matches_canonical_postprocessing(frozen, name, bundle)
        deterministic[name] = bundle

    b1_root = (
        repo
        / "artifacts/v5/development/s1-colab-resource-qualification/"
        "b1-complete-2026-10-04"
    )
    b1: dict[str, Any] = {}
    for seed in SEEDS:
        path = b1_root / f"b1-seed-{seed}-decision-matrix.json"
        rows = _complete_rows(path)
        b1[str(seed)] = {
            "matrix_sha256": _sha(path),
            **_bundle(rows, post._baseline_transform),
        }

    c1_root = repo / "artifacts/v5/development/s1-kaggle-adapters"
    c1: dict[str, Any] = {}
    c1_then_a1: dict[str, Any] = {}
    canonical_c1_a1 = frozen.get("results", {}).get("C1_THEN_A1_BY_SEED")
    if not isinstance(canonical_c1_a1, dict):
        raise CrossPropertyError("CANONICAL_C1_THEN_A1_MISSING")
    for seed in SEEDS:
        folder = _reviewed_seed_folder(
            c1_root,
            prefix="c1",
            seed=seed,
            expected_status="PASS_MODEL_FREE_EXPORT_VERIFICATION",
            intervention="C1_CRDI_V1",
        )
        path = folder / "evidence" / "adapter-decision-matrix.json"
        rows = _complete_rows(path)
        c1[str(seed)] = {
            "matrix_sha256": _sha(path),
            **_bundle(rows, post._baseline_transform),
        }
        canonical_seed = canonical_c1_a1.get(str(seed))
        if not isinstance(canonical_seed, dict):
            raise CrossPropertyError(f"CANONICAL_C1_THEN_A1_SEED_MISSING:{seed}")
        temperature = float(canonical_seed["temperature_fit"]["temperature"])
        if not math.isfinite(temperature) or temperature <= 0.0:
            raise CrossPropertyError(f"CANONICAL_C1_THEN_A1_TEMPERATURE_INVALID:{seed}")

        def transform(
            row: dict[str, Any],
            *,
            fixed_temperature: float = temperature,
        ) -> tuple[float, float]:
            return post._a1_display(row, fixed_temperature)

        bundle = _bundle(rows, transform)
        if post.json.dumps(
            bundle["assurance_summary"], sort_keys=True, separators=(",", ":")
        ) != post.json.dumps(
            canonical_seed["results"], sort_keys=True, separators=(",", ":")
        ):
            raise CrossPropertyError(
                f"CANONICAL_C1_THEN_A1_REPRODUCTION_MISMATCH:{seed}"
            )
        c1_then_a1[str(seed)] = {
            "matrix_sha256": _sha(path),
            "temperature": temperature,
            **bundle,
        }

    c2_root = repo / "artifacts/v5/development/s1-kaggle-c2-adapters"
    c2: dict[str, Any] = {}
    c2_retention: dict[str, Any] = {}
    for seed in SEEDS:
        folder = _reviewed_seed_folder(
            c2_root,
            prefix="c2",
            seed=seed,
            expected_status="PASS_MODEL_FREE_C2_EXPORT_VERIFICATION",
            intervention="C2_CRDI_RETAIN_V1",
        )
        path = folder / "evidence" / "adapter-decision-matrix.json"
        rows = _complete_rows(path)
        c2[str(seed)] = {
            "matrix_sha256": _sha(path),
            **_bundle(rows, post._baseline_transform),
        }
        retention_path = folder / "evidence" / "paired-retention-aggregate.json"
        retention = _load_json(retention_path)
        if retention.get("scope") != "PAIRED_SQUAD_V1_1_ONLY; NOT_GENERAL_CAPABILITY_PRESERVATION":
            raise CrossPropertyError(f"C2_RETENTION_SCOPE_MISMATCH:{seed}")
        c2_retention[str(seed)] = {
            "aggregate_sha256": _sha(retention_path),
            "scope": retention["scope"],
            "baseline": retention["baseline"],
            "candidate": retention["candidate"],
            "paired_mean_delta": retention["paired_mean_delta"],
        }

    return {
        "schema": "commandmed.v5.s1-cross-property-development-completion.v1",
        "scope": "DEVELOPMENT_CALIBRATION_ONLY",
        "confirmatory": False,
        "reserve": False,
        "claim_promotion": False,
        "canonical_postprocessing_sha256": POSTPROCESSING_SHA256,
        "fixed_d1_threshold": FIXED_D1_THRESHOLD,
        "fixed_d1_source": "BASELINE_S1_CAL_TUNE_CANONICAL_5_PERCENT_RISK_TARGET",
        "deterministic_postprocessing_conditions": deterministic,
        "B1_TYPED_V1_BY_SEED": b1,
        "C1_CRDI_V1_BY_SEED": c1,
        "C2_CRDI_RETAIN_V1_BY_SEED": c2,
        "C1_THEN_A1_BY_SEED": c1_then_a1,
        "C2_RETENTION_BY_SEED": c2_retention,
        "assurance_axis_status": {
            "P1_CANONICAL_DECISION": "MEASURED_DEVELOPMENT",
            "P2_CALIBRATION": "MEASURED_DEVELOPMENT_DIAGNOSTIC",
            "P3_COHERENCE": "NOT_APPLICABLE_OR_NOT_INSTANTIATED_IN_S1_RULE_ORACLE",
            "P4_SEMANTIC_STABILITY": "MEASURED_DEVELOPMENT",
            "P5_EVIDENCE_RESPONSIVENESS": "NOT_APPLICABLE_OR_NOT_INSTANTIATED_IN_S1_RULE_ORACLE",
            "P6_RULE_CONFORMANCE": "MEASURED_DEVELOPMENT_MATCH_MISMATCH_ACCURACY",
            "P7_SELECTIVE_CONTROL": "MEASURED_DEVELOPMENT_FIXED_D1_POLICY",
            "P8_CAPABILITY_RETENTION": {
                "B1_TYPED_V1": "BASE_BACKBONE_UNCHANGED_NOT_AN_EMPIRICAL_RETENTION_CLAIM",
                "C1_CRDI_V1": "NOT_MEASURED_DEVELOPMENT",
                "C2_CRDI_RETAIN_V1": "MEASURED_NARROW_PAIRED_SQUAD_V1_1_ONLY",
            },
        },
        "interpretation_boundary": (
            "Development-only cross-property completion. No threshold, temperature, "
            "binning, margin, effect class, confirmatory identity, clinical-validity "
            "claim, broad-retention claim, replication claim, publication or merge authority."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=REPO_ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = analyze(args.repo.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "status": "PASS_CROSS_PROPERTY_DEVELOPMENT_COMPLETION",
                "output": str(args.output),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
