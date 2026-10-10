#!/usr/bin/env python3
"""Fail-closed, model-free provenance gate for a V5 development-only manuscript addendum.

This is a read-only evidence audit, not a clinical, inferential, peer-review, or
publication qualification. Its SHA bindings are a dated snapshot: changing the
inputs requires a separately reviewed update rather than silent reinterpretation.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEV = "artifacts/v5/development/"
RUNS = DEV + "s1-kaggle-repeatability-runs/"
DOC = "docs/research/paper-rebuild-v2-2026-10-02/"
RISKCALCS_SHA256 = "00a7a0089afffb66f2f32903bad94a5a2ea842841defb2d78e0686b0a5eb9ab9"
FROZEN_BINDINGS_RELATIVE = DOC + "V5_S1_KAGGLE_RUNTIME_AMENDMENT_BINDINGS_2026-10-08.json"
FROZEN_BINDINGS_SHA256 = "c33e603e531b5f3957a0fbe5fa63d45f070e21e2243b268af232516990dd428f"

# The immutable receipts, scientific metrics, frozen floor and reporting text are
# locked to the 2026-10-09 evidence state plus the 2026-10-10 dated ICC crosswalk update.
LOCKED_SOURCES: dict[str, tuple[str, str]] = {
    "r1_receipt": (RUNS + "repeat-1-v1-2026-10-09/export-verification-receipt.json", "b445406380ea967ce8bb8bc7a61efe1cd48ade50e03f6c0eabba6e559d58eb53"),
    "r2_receipt": (RUNS + "repeat-2-v1-2026-10-09/export-verification-receipt.json", "f55e1b0271918538c16d347a1e91b0aeeece47acb84aa4314f3cc3169e45b4a2"),
    "paired": (RUNS + "paired-r1-r2-repeatability95-2026-10-09.json", "f6ace697d61de05c470c1260dafc7b54f13524b0dd2960e45c268c46bb7e64be"),
    "margins": (RUNS + "final-development-benchmark-margins-2026-10-09.json", "361ad34e0c2deb0ca7646cfb9dd9346bb63471296a003e9ef12a858743f6917f"),
    "floors": (DEV + "domain-floor-freeze-2026-10-09/domain-floors.json", "8c284a98f504c8529a4da5d9bb1e265465af66b10d0c3b0414505dcebc9c7ca7"),
    "sd_inventory": (DEV + "s1-paired-sd-inventory-2026-10-09/development-paired-sd.json", "b1edf781b61d3f5ce227c08908ca43ad9864c0b398a7318c33895951af37bacd"),
    "synthesis": (DEV + "s1-development-synthesis-2026-10-09/final-synthesis.json", "76b7f7503a743991fd81f4e1758d5710cc646a0a665c1e3e2128d1e533ea2e82"),
    "crosswalk": (DOC + "V5_MANUSCRIPT_DEVELOPMENT_RESULTS_CROSSWALK_2026-10-09.md", "7ff52c5b616543c7d85a44e6ecbf9b982a95b2a58531cc17a66e002367d04c41"),
}
ORIGINAL_ARCHIVES = {
    1: (RUNS + "repeat-1-v1-2026-10-09/original-export.zip", "dfb35b0216369bbb87bcec75c5715df974bb9f736c0db0af98148cea91d99dac"),
    2: (RUNS + "repeat-2-v1-2026-10-09/original-export.zip", "73f24c06f2d54e34cc20f2137f06b0728f02cccfc0d96c346f619d73184e4216"),
}
METRICS = ("canonical_accuracy", "canonical_nll", "canonical_brier", "semantic_js")
SECONDARY = ("transformed_accuracy", "transformed_nll", "transformed_brier")
SPLITS = ("S1_DEV_EVAL", "S1_CAL_EVAL")


class ManuscriptEvidenceAuditError(ValueError):
    """Fail-closed when a source identity, result or reporting bound changes."""


def _check(condition: bool, code: str) -> None:
    if not condition:
        raise ManuscriptEvidenceAuditError(code)


def _digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(part)
    return digest.hexdigest()


def _locked_file(root: Path, relative: str, expected: str) -> Path:
    path = root / relative
    _check(path.resolve().is_relative_to(root.resolve()), "SOURCE_ESCAPES_REPOSITORY")
    _check(path.is_file(), "MISSING_LOCKED_SOURCE:" + relative)
    _check(_digest(path) == expected, "SOURCE_SHA256_MISMATCH:" + relative)
    return path


def _finite_number(value: Any) -> bool:
    return type(value) in (int, float) and math.isfinite(value)


def assert_development_semantics(records: dict[str, Any]) -> dict[str, Any]:
    """Inspect already SHA-locked payloads; never infer clinical/power approval."""
    r1, r2 = records["r1_receipt"], records["r2_receipt"]
    for index, receipt in ((1, r1), (2, r2)):
        _check(receipt.get("repeat") == index and type(receipt.get("repeat")) is int, "WRONG_REPEAT_IDENTITY")
        _check(receipt.get("status") == "PASS_MODEL_FREE_REPEATABILITY_EXPORT_VERIFICATION", "REPEAT_NOT_INDEPENDENTLY_VERIFIED")
        _check(receipt.get("ordered_rows_verified") == 16384 and receipt.get("source_task_count_verified") == 8192, "INCOMPLETE_REPEAT_MATRIX")
        _check(receipt.get("riskcalcs_sha256") == RISKCALCS_SHA256, "REPEAT_SOURCE_DRIFT")
        _check(receipt.get("durable_export_verified") is True and receipt.get("model_weights_loaded") is False, "REPEAT_EVIDENCE_INVALID")
        _check(receipt.get("confirmatory") is False and receipt.get("reserve") is False and receipt.get("clinical_validity") is False, "REPEAT_SCOPE_ESCALATION")
        _check(receipt.get("scientific_replication") is False and receipt.get("spend_usd") == 0, "REPEAT_SCOPE_ESCALATION")
        _check(receipt.get("kernel") == f"abdulazizshehri/commandmed-v5-base-repeatability-r{index}", "REPEAT_KERNEL_PROVENANCE_MISMATCH")
        _check(receipt.get("kernel_version") == 1, "KERNEL_VERSION_MISMATCH")

    pair = records["paired"]
    _check(pair.get("scope") == "DEVELOPMENT_CALIBRATION_ONLY", "PAIRED_SCOPE")
    _check(pair.get("confirmatory") is False and pair.get("reserve") is False, "PAIRED_SCOPE")
    _check(pair.get("repeat_count") == 2 and pair.get("eval_task_count") == 7680, "PAIRED_SAMPLE_MISMATCH")
    _check(tuple(pair.get("primary_metrics", ())) == METRICS and tuple(pair.get("secondary_metrics", ())) == SECONDARY, "PAIRED_METRIC_DRIFT")
    for name in METRICS + SECONDARY:
        val = pair["metrics"][name]["repeatability95"]
        _check(_finite_number(val) and val == 0.0, "PAIRED_REPEATABILITY_CHANGED:" + name)

    floors, margins = records["floors"], records["margins"]
    _check(floors.get("status") == "FROZEN_PROSPECTIVELY_BEFORE_REPEATABILITY_OUTPUT", "FLOORS_NOT_PROSPECTIVE")
    _check(floors.get("clinical_tolerance") is False and floors.get("derived_from_observed_intervention_effects") is False, "FLOOR_CLINICAL_OR_POSTHOC")
    _check(margins.get("scope") == "DEVELOPMENT_ONLY" and margins.get("clinical_validity") is False, "MARGINS_CLINICAL_SCOPE")
    _check(margins.get("confirmatory") is False and margins.get("reserve") is False and margins.get("publication_authorized") is False, "MARGINS_SCOPE_ESCALATION")
    _check(margins.get("power_plan_status") == "PENDING_PAIRED_SD_AND_FROZEN_PRIMARY_NON_TARGET_FAMILY_SIZE", "POWER_CLAIM_UNQUALIFIED")
    _check(set(margins["metrics"]) == set(METRICS) == set(floors["metrics"]), "MARGIN_FAMILY_DRIFT")
    for name in METRICS:
        floor = floors["metrics"][name]["domain_floor"]
        m = margins["metrics"][name]
        _check(_finite_number(floor) and floor > 0, "INVALID_FLOOR:" + name)
        _check(m.get("frozen_benchmark_scale_domain_floor") == floor and m.get("meaningful_margin") == floor, "MARGIN_POSTHOC_DRIFT:" + name)
        _check(m.get("verified_repeatability95") == 0 and m.get("clinical_tolerance") is False, "MARGIN_SCOPE_ESCALATION:" + name)

    inventory, synthesis = records["sd_inventory"], records["synthesis"]
    _check(inventory.get("confirmatory") is False and inventory.get("reserve") is False and inventory.get("confirmatory_power_claim") is False, "SD_FALSE_CONFIRMATORY")
    _check(inventory.get("primary_non_target_family_size") is None, "POSTHOC_FAMILY_SIZE")
    _check(inventory.get("training_seed_uncertainty_not_included_in_paired_item_sd") is True, "SD_SEED_UNCERTAINTY_ERASED")
    _check(tuple(inventory.get("primary_metrics", ())) == METRICS, "SD_METRIC_DRIFT")
    interventions = inventory.get("intervention_results")
    _check(isinstance(interventions, dict) and set(interventions) == {f"{prefix}_{seed}" for prefix in ("B1", "C1", "C2") for seed in (11,29,47)}, "SD_INTERVENTION_SET_DRIFT")
    cells = 0
    for intervention in interventions.values():
        _check(set(intervention["splits"]) == set(SPLITS), "SD_SPLIT_DRIFT")
        for split in SPLITS:
            _check(set(intervention["splits"][split]) == set(METRICS), "SD_CELL_SET_DRIFT")
            for name in METRICS:
                cell = intervention["splits"][split][name]
                _check(cell["task_count"] == 3840 and _finite_number(cell["paired_source_task_sample_sd"]) and cell["paired_source_task_sample_sd"] >= 0, "INVALID_SD_CELL")
                cells += 1
    _check(cells == 72, "INCOMPLETE_72_CELL_INVENTORY")
    _check(synthesis.get("confirmatory") is False and synthesis.get("reserve") is False, "SYNTHESIS_SCOPE_ESCALATION")
    _check(synthesis.get("claim_promotion") in (False, "NONE"), "UNAUTHORIZED_CLAIM_PROMOTION")
    return {
        "status": "PASS_DEVELOPMENT_ONLY_EVIDENCE_ADMISSION",
        "original_repeatability_runs_verified": 2,
        "ordered_rows_per_run": 16384,
        "paired_source_eval_tasks": 7680,
        "descriptive_sd_cells": cells,
        "frozen_primary_metrics": len(METRICS),
        "repeatability95_all_seven_zero": True,
        "clinical_validity": False,
        "confirmatory": False,
        "reserve": False,
        "power_adequacy": "NOT_QUALIFIED",
        "publication_authority": False,
        "independent_peer_review": False,
    }


def audit(root: Path = ROOT) -> dict[str, Any]:
    root = root.resolve()
    records: dict[str, Any] = {}
    for name, (relative, digest) in LOCKED_SOURCES.items():
        path = _locked_file(root, relative, digest)
        if name != "crosswalk":
            try:
                records[name] = json.loads(path.read_text(encoding="utf-8"))
            except (UnicodeError, ValueError) as exc:
                raise ManuscriptEvidenceAuditError("INVALID_JSON_SOURCE:" + name) from exc
    for index, (relative, digest) in ORIGINAL_ARCHIVES.items():
        path = _locked_file(root, relative, digest)
        _check(records[f"r{index}_receipt"].get("archive_sha256") == digest, "ARCHIVE_RECEIPT_MISMATCH")
    result = assert_development_semantics(records)

    # Recheck each original frozen entry directly. Never silently edit the
    # prospective paper/manuscript/claim ledger to match this addendum.
    # The manifest is *not* among its own 307 entries. Pin its original SHA
    # separately or a coordinated manifest+source rewrite could falsely pass.
    binding = _locked_file(root, FROZEN_BINDINGS_RELATIVE, FROZEN_BINDINGS_SHA256)
    b = json.loads(binding.read_text(encoding="utf-8"))
    frozen = b["unchanged_entry_files"]
    _check(len(frozen) == 307, "FROZEN_ENTRY_COUNT_CHANGED")
    _check(len({row["path"] for row in frozen}) == 307, "DUPLICATE_FROZEN_ENTRY_PATH")
    for row in frozen:
        _locked_file(root, row["path"], row["sha256"])
    result.update(frozen_source_files_verified=307, locked_evidence_sources=len(LOCKED_SOURCES),
                  original_archives_verified=len(ORIGINAL_ARCHIVES))
    return result


def main() -> int:
    print(json.dumps(audit(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
