#!/usr/bin/env python3
"""Generate only pre-freeze V5 development/calibration case-identity bindings."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from src.commandmed.reliability_v5.case_generator import cases_from_state_indices
from src.commandmed.reliability_v5.quarantine import prefreeze_state_partition

PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "riskcalcs-rule-oracle-final-candidate-v5.json"
OUT = PACKET / "rule-oracle-case-index-v5.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_json(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> int:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    selected = source.get("selected", [])
    if len(selected) != 64:
        raise SystemExit(f"expected 64 selected calculators, found {len(selected)}")

    records = []
    all_development_ids: list[str] = []
    all_calibration_ids: list[str] = []
    for calculator in selected:
        pmid = str(calculator["pmid"])
        calculator_id = f"pmid:{pmid}"
        total = int(calculator["prospective_case_space"])
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
        dev_ids = [str(case["case_id"]) for case in development]
        cal_ids = [str(case["case_id"]) for case in calibration]
        all_development_ids.extend(dev_ids)
        all_calibration_ids.extend(cal_ids)
        records.append(
            {
                "pmid": pmid,
                "title": calculator["title"],
                "candidate_state_space": total,
                "code_sha256": calculator["code_sha256"],
                "development_case_ids_sha256": sha256_json(dev_ids),
                "calibration_case_ids_sha256": sha256_json(cal_ids),
            }
        )

    payload = {
        "status": "PREFREEZE_DEV_CAL_CASE_IDENTITY_INDEX_FUTURE_TEST_UNMATERIALIZED",
        "source_manifest": SOURCE.name,
        "source_manifest_sha256": sha256_file(SOURCE),
        "case_generator_path": "src/commandmed/reliability_v5/case_generator.py",
        "case_generator_sha256": sha256_file(
            ROOT / "src/commandmed/reliability_v5/case_generator.py"
        ),
        "calculator_count": len(records),
        "development_case_count": len(all_development_ids),
        "calibration_case_count": len(all_calibration_ids),
        "development_case_ids_sha256": sha256_json(all_development_ids),
        "calibration_case_ids_sha256": sha256_json(all_calibration_ids),
        "confirmatory_case_identities_materialized": False,
        "reserve_case_identities_materialized": False,
        "calculators": records,
    }
    OUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"CALCULATORS={payload['calculator_count']}")
    print(f"DEVELOPMENT_CASES={payload['development_case_count']}")
    print(f"CALIBRATION_CASES={payload['calibration_case_count']}")
    print("FUTURE_TEST_MATERIALIZED=False")
    print(f"OUT={OUT}")
    print(f"OUT_SHA256={sha256_file(OUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
