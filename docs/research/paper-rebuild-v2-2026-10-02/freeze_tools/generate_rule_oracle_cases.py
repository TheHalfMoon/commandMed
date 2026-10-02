#!/usr/bin/env python3
"""Generate compact V5 case-identity bindings without executing calculators."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from src.commandmed.reliability_v5.case_generator import deterministic_cases

PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "riskcalcs-rule-oracle-final-candidate-v5.json"
OUT = PACKET / "rule-oracle-case-index-v5.json"
CASES_PER_CALCULATOR = 64


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
    all_case_ids: list[str] = []
    for calculator in selected:
        pmid = str(calculator["pmid"])
        cases = deterministic_cases(
            f"pmid:{pmid}",
            calculator["domain_constants"],
            count=CASES_PER_CALCULATOR,
        )
        case_ids = [str(case["case_id"]) for case in cases]
        all_case_ids.extend(case_ids)
        records.append(
            {
                "pmid": pmid,
                "title": calculator["title"],
                "code_sha256": calculator["code_sha256"],
                "case_ids_sha256": sha256_json(case_ids),
                "first_case_id": case_ids[0],
                "last_case_id": case_ids[-1],
            }
        )

    payload = {
        "status": "STATIC_CASE_IDENTITY_INDEX_CALCULATORS_NOT_EXECUTED",
        "source_manifest": SOURCE.name,
        "source_manifest_sha256": sha256_file(SOURCE),
        "case_generator_path": "src/commandmed/reliability_v5/case_generator.py",
        "case_generator_sha256": sha256_file(ROOT / "src/commandmed/reliability_v5/case_generator.py"),
        "calculator_count": len(records),
        "cases_per_calculator": CASES_PER_CALCULATOR,
        "total_cases": len(all_case_ids),
        "ordered_case_ids_sha256": sha256_json(all_case_ids),
        "calculators": records,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"CALCULATORS={payload['calculator_count']}")
    print(f"TOTAL_CASES={payload['total_cases']}")
    print(f"ORDERED_CASE_IDS_SHA256={payload['ordered_case_ids_sha256']}")
    print(f"OUT={OUT}")
    print(f"OUT_SHA256={sha256_file(OUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
