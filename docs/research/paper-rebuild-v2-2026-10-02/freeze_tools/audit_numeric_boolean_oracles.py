#!/usr/bin/env python3
"""Development/calibration execution-qualified selector for V5 RiskCalcs oracles."""
from __future__ import annotations

import hashlib
import json
import math
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from select_riskcalcs_manifest import SOURCE_URL, SOURCE_REV, SOURCE_BLOB, SALT, extract_function
from audit_discrete_rule_oracles import audit_discrete
from src.commandmed.reliability_v5.oracle_qualification import qualify_bound_rule_execution
from src.commandmed.reliability_v5.rule_dataset import BoundRule

OUT = Path(__file__).resolve().parents[1] / "riskcalcs-rule-oracle-final-candidate-v5.json"
SELECT_COUNT = 64
MAX_ARGS = 8
MIN_PROSPECTIVE_CASE_SPACE = 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha256(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def prospective_case_space(domains: dict[str, list[object]]) -> int:
    total = 1
    for values in domains.values():
        if all(isinstance(v, bool) for v in values):
            total *= 2
            continue
        numeric = [float(v) for v in values if isinstance(v, (int, float)) and not isinstance(v, bool)]
        if not numeric:
            return 0
        expanded = set()
        for value in numeric:
            near = max(1.0, abs(value) * 0.01)
            far = max(5.0, abs(value) * 0.10)
            expanded.update({value - far, value - near, value, value + near, value + far})
        total *= len(expanded)
    return total


def admissible_domains(domains: dict[str, list[object]]) -> bool:
    if not domains or len(domains) > MAX_ARGS:
        return False
    for values in domains.values():
        if not values:
            return False
        for value in values:
            if isinstance(value, str):
                return False
            if isinstance(value, float) and not math.isfinite(value):
                return False
            if isinstance(value, (int, float)) and not isinstance(value, bool) and abs(float(value)) > 1_000_000:
                return False
    return prospective_case_space(domains) >= MIN_PROSPECTIVE_CASE_SPACE


def selection_specialty_stratum(record: dict[str, object]) -> str:
    raw = str(record.get("specialty", "")).strip()
    if not raw:
        return "UNKNOWN"
    return raw.split(",", 1)[0].strip() or "UNKNOWN"


def balanced_select(eligible: list[dict[str, object]]) -> list[dict[str, object]]:
    """Round-robin across first-listed source specialty strata; deterministic within strata."""
    buckets: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in eligible:
        buckets[str(row["selection_specialty_stratum"])].append(row)
    for rows in buckets.values():
        rows.sort(key=lambda row: (str(row["selection_key"]), str(row["pmid"])))

    selected: list[dict[str, object]] = []
    round_index = 0
    specialties = sorted(buckets)
    while len(selected) < SELECT_COUNT:
        added = 0
        for specialty in specialties:
            rows = buckets[specialty]
            if round_index < len(rows):
                selected.append(rows[round_index])
                added += 1
                if len(selected) == SELECT_COUNT:
                    break
        if added == 0:
            break
        round_index += 1
    return selected


def rejection_record(row: dict[str, object], result) -> dict[str, object]:
    return {
        "pmid": row["pmid"],
        "function_name": row["function_name"],
        "code_sha256": row["code_sha256"],
        "selection_specialty_stratum": row["selection_specialty_stratum"],
        "development_cases_checked": result.development_cases_checked,
        "calibration_cases_checked": result.calibration_cases_checked,
        "failure_role": result.failure_role,
        "failure_state_index": result.failure_state_index,
        "failure_case_id": result.failure_case_id,
        "failure_type": result.failure_type,
        "failure_message": result.failure_message,
    }


def mechanics_bindings() -> dict[str, dict[str, str]]:
    paths = {
        "selector": Path(__file__).resolve(),
        "case_generator": ROOT / "src/commandmed/reliability_v5/case_generator.py",
        "quarantine": ROOT / "src/commandmed/reliability_v5/quarantine.py",
        "execution_gate": ROOT / "src/commandmed/reliability_v5/oracle_qualification.py",
        "bound_rule_runtime": ROOT / "src/commandmed/reliability_v5/rule_dataset.py",
    }
    return {
        name: {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(path),
        }
        for name, path in paths.items()
    }


def main() -> int:
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "CommandMed-research"})
    with urllib.request.urlopen(req, timeout=30) as response:
        raw = response.read()
    data = json.loads(raw)

    static_eligible: list[tuple[dict[str, object], str]] = []
    for pmid, record in data.items():
        extracted = extract_function(str(record.get("computation", "")))
        if extracted is None:
            continue
        code, function_name, arg_count = extracted
        domains = audit_discrete(code)
        if domains is None or not admissible_domains(domains):
            continue
        specialty = str(record.get("specialty", "")).strip()
        key = hashlib.sha256(f"{pmid}|{SALT}|RULE_ORACLE_NUMBOOL".encode()).hexdigest()
        row: dict[str, object] = {
            "pmid": str(pmid),
            "title": str(record.get("title", "")).strip(),
            "source_specialty": specialty,
            "selection_specialty_stratum": selection_specialty_stratum(record),
            "function_name": function_name,
            "arg_count": arg_count,
            "domain_constants": domains,
            "prospective_case_space": prospective_case_space(domains),
            "code_sha256": hashlib.sha256(code.encode()).hexdigest(),
            "selection_key": key,
        }
        static_eligible.append((row, code))

    execution_qualified: list[dict[str, object]] = []
    execution_rejections: list[dict[str, object]] = []
    for row, code in static_eligible:
        rule = BoundRule(
            pmid=str(row["pmid"]),
            title=str(row["title"]),
            function_name=str(row["function_name"]),
            code=code,
            code_sha256=str(row["code_sha256"]),
            domain_constants=row["domain_constants"],
            prospective_case_space=int(row["prospective_case_space"]),
        )
        result = qualify_bound_rule_execution(rule)
        if result.qualified:
            execution_qualified.append(row)
        else:
            execution_rejections.append(rejection_record(row, result))

    execution_rejections.sort(key=lambda row: (str(row["pmid"]), str(row["function_name"])))
    selected = balanced_select(execution_qualified)
    counts: dict[str, int] = {}
    for row in selected:
        specialty = str(row["selection_specialty_stratum"])
        counts[specialty] = counts.get(specialty, 0) + 1

    enough = len(selected) == SELECT_COUNT
    manifest = {
        "status": (
            "DEV_CAL_EXECUTION_QUALIFIED_DOMAIN_BALANCED_RULE_ORACLE_CANDIDATE"
            if enough
            else "INSUFFICIENT_DEV_CAL_EXECUTION_QUALIFIED_RULE_ORACLES"
        ),
        "source_revision": SOURCE_REV,
        "source_blob": SOURCE_BLOB,
        "source_bytes_sha256": hashlib.sha256(raw).hexdigest(),
        "selector_salt": f"{SALT}|RULE_ORACLE_NUMBOOL",
        "selection_policy": (
            "first require static numeric/Boolean eligibility; then execute every deterministic "
            "development and calibration state through the fail-closed bound-rule compiler; "
            "preserve every rejection; then round-robin over alphabetically ordered first-listed "
            "source specialty strata, ordering within strata by sha256 selection_key then PMID"
        ),
        "eligibility": (
            "one safe parsed function; <=8 args; every input used only as boolean/simple numeric comparison; "
            "no string domains; no input arithmetic/calls/subscripts/attributes; prospective generated input "
            "space >=1024; exact pre-frozen development/calibration execution coverage must complete without "
            "compile/runtime/serialization/perturbation-contract failure"
        ),
        "execution_coverage": {
            "development_cases_per_candidate": 64,
            "calibration_cases_per_candidate": 64,
            "confirmatory_materialized": False,
            "reserve_materialized": False,
        },
        "mechanics": mechanics_bindings(),
        "static_eligible_count": len(static_eligible),
        "execution_qualified_count": len(execution_qualified),
        "execution_rejected_count": len(execution_rejections),
        "execution_rejection_digest_sha256": canonical_sha256(execution_rejections),
        "execution_rejections": execution_rejections,
        "eligible_selection_stratum_count": len(
            {str(row["selection_specialty_stratum"]) for row in execution_qualified}
        ),
        "selected_selection_stratum_counts": dict(sorted(counts.items())),
        "selected_count": len(selected),
        "selected": selected,
    }
    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STATIC_NUMBOOL_ORACLES={len(static_eligible)}")
    print(f"EXECUTION_QUALIFIED={len(execution_qualified)}")
    print(f"EXECUTION_REJECTED={len(execution_rejections)}")
    print(f"REJECTION_DIGEST={manifest['execution_rejection_digest_sha256']}")
    print(f"SELECTION_STRATA={manifest['eligible_selection_stratum_count']}")
    print(f"SELECTED={len(selected)}")
    print(f"SELECTED_STRATUM_COUNTS={json.dumps(manifest['selected_selection_stratum_counts'], sort_keys=True)}")
    print(f"OUT={OUT}")
    if not enough:
        raise SystemExit(
            f"development/calibration execution-qualified oracle gate failed: only {len(selected)} selected"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
