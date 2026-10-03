#!/usr/bin/env python3
"""Bind only V5 development/calibration cases before future confirmatory sampling."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from src.commandmed.reliability_v5.case_generator import cases_from_state_indices
from src.commandmed.reliability_v5.quarantine import (
    CALIBRATION_COUNT,
    DEVELOPMENT_COUNT,
    MIN_FUTURE_CANDIDATE_SPACE,
    prefreeze_state_partition,
)

PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "riskcalcs-rule-oracle-final-candidate-v5.json"
OUT = PACKET / "quarantine-commitments-v5.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_values(values: list[object] | tuple[object, ...]) -> str:
    payload = json.dumps(list(values), separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> int:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    selected = source.get("selected", [])
    if len(selected) != 64:
        raise SystemExit(f"expected 64 selected calculators, found {len(selected)}")

    rows = []
    development_ids: list[str] = []
    calibration_ids: list[str] = []
    for calculator in selected:
        pmid = str(calculator["pmid"])
        calculator_id = f"pmid:{pmid}"
        total = int(calculator["prospective_case_space"])
        if total < MIN_FUTURE_CANDIDATE_SPACE:
            raise SystemExit(f"PMID {pmid}: case space {total} below quarantine minimum")
        partition = prefreeze_state_partition(calculator_id, total)
        development = cases_from_state_indices(
            calculator_id,
            calculator["domain_constants"],
            partition["development"],
        )
        calibration = cases_from_state_indices(
            calculator_id,
            calculator["domain_constants"],
            partition["calibration"],
        )
        development_case_ids = [str(case["case_id"]) for case in development]
        calibration_case_ids = [str(case["case_id"]) for case in calibration]
        development_ids.extend(development_case_ids)
        calibration_ids.extend(calibration_case_ids)
        rows.append(
            {
                "pmid": pmid,
                "candidate_state_space": total,
                "development_state_indices_sha256": sha256_values(partition["development"]),
                "calibration_state_indices_sha256": sha256_values(partition["calibration"]),
                "development_case_ids_sha256": sha256_values(development_case_ids),
                "calibration_case_ids_sha256": sha256_values(calibration_case_ids),
                "unselected_state_count_before_future_sampling": (
                    total - DEVELOPMENT_COUNT - CALIBRATION_COUNT
                ),
            }
        )

    payload = {
        "status": "PREFREEZE_DEV_CAL_COMMITTED_FUTURE_CONFIRMATORY_UNMATERIALIZED",
        "source_manifest": SOURCE.name,
        "source_manifest_sha256": sha256_file(SOURCE),
        "quarantine_mechanics": "src/commandmed/reliability_v5/quarantine.py",
        "quarantine_mechanics_sha256": sha256_file(
            ROOT / "src/commandmed/reliability_v5/quarantine.py"
        ),
        "calculator_count": len(rows),
        "minimum_candidate_state_space": MIN_FUTURE_CANDIDATE_SPACE,
        "development_cases_per_calculator": DEVELOPMENT_COUNT,
        "calibration_cases_per_calculator": CALIBRATION_COUNT,
        "development_case_ids_sha256": sha256_values(development_ids),
        "calibration_case_ids_sha256": sha256_values(calibration_ids),
        "confirmatory_assignment_materialized": False,
        "reserve_assignment_materialized": False,
        "future_sampling_rule": (
            "after a clean implementation freeze, derive a seed from the first valid "
            "future NIST Beacon 2.0 pulse and rank only state indices not used by "
            "development or calibration"
        ),
        "rows": rows,
    }
    OUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"DEVELOPMENT={len(development_ids)}")
    print(f"CALIBRATION={len(calibration_ids)}")
    print("CONFIRMATORY_MATERIALIZED=False")
    print(f"OUT={OUT}")
    print(f"OUT_SHA256={sha256_file(OUT)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
