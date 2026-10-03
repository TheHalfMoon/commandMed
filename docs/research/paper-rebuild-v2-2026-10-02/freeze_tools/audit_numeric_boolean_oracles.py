#!/usr/bin/env python3
"""Static domain-balanced selector for V5 numeric/Boolean RiskCalcs; no execution."""
from __future__ import annotations

import hashlib
import json
import math
import urllib.request
from collections import defaultdict
from pathlib import Path

from select_riskcalcs_manifest import SOURCE_URL, SOURCE_REV, SOURCE_BLOB, SALT, extract_function
from audit_discrete_rule_oracles import audit_discrete

OUT = Path(__file__).resolve().parents[1] / "riskcalcs-rule-oracle-final-candidate-v5.json"
SELECT_COUNT = 64
MAX_ARGS = 8
MIN_PROSPECTIVE_CASE_SPACE = 1024


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

def main() -> int:
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "CommandMed-research"})
    with urllib.request.urlopen(req, timeout=30) as response:
        raw = response.read()
    data = json.loads(raw)
    eligible = []
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
        eligible.append(
            {
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
        )

    selected = balanced_select(eligible)
    if len(selected) < SELECT_COUNT:
        raise SystemExit(f"numeric/boolean oracle gate failed: only {len(selected)} selected")

    counts: dict[str, int] = {}
    for row in selected:
        specialty = str(row["selection_specialty_stratum"])
        counts[specialty] = counts.get(specialty, 0) + 1

    manifest = {
        "status": "STATIC_DOMAIN_BALANCED_NUMERIC_BOOLEAN_RULE_ORACLE_CANDIDATE_NO_FUNCTION_EXECUTION",
        "source_revision": SOURCE_REV,
        "source_blob": SOURCE_BLOB,
        "source_bytes_sha256": hashlib.sha256(raw).hexdigest(),
        "selector_salt": f"{SALT}|RULE_ORACLE_NUMBOOL",
        "selection_policy": (
            "deterministic round-robin over alphabetically ordered first-listed source specialty strata; "
            "within each specialty candidates are ordered by sha256 selection_key then PMID; "
            "the design targets domain breadth, not clinical prevalence"
        ),
        "eligibility": (
            "one safe parsed function; <=8 args; every input used only as boolean/simple numeric comparison; "
            "no string domains; no input arithmetic/calls/subscripts/attributes; prospective generated input space >=1024"
        ),
        "static_eligible_count": len(eligible),
        "eligible_selection_stratum_count": len({str(row['selection_specialty_stratum']) for row in eligible}),
        "selected_selection_stratum_counts": dict(sorted(counts.items())),
        "selected_count": len(selected),
        "selected": selected,
    }
    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STATIC_NUMBOOL_ORACLES={len(eligible)}")
    print(f"SELECTION_STRATA={manifest['eligible_selection_stratum_count']}")
    print(f"SELECTED={len(selected)}")
    print(f"SELECTED_STRATUM_COUNTS={json.dumps(manifest['selected_selection_stratum_counts'], sort_keys=True)}")
    print(f"OUT={OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
