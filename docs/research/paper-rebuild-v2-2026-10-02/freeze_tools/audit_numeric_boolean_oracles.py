#!/usr/bin/env python3
"""Stricter static selector: boolean/numeric-threshold RiskCalcs only; no code execution."""
from __future__ import annotations

import hashlib
import json
import math
import urllib.request
from pathlib import Path

from select_riskcalcs_manifest import SOURCE_URL, SOURCE_REV, SOURCE_BLOB, SALT, extract_function
from audit_discrete_rule_oracles import audit_discrete

OUT = Path(__file__).resolve().parents[1] / "riskcalcs-rule-oracle-final-candidate-v5.json"
SELECT_COUNT = 64
MAX_ARGS = 8


def prospective_case_space(domains: dict[str, list[object]]) -> int:
    total = 1
    for values in domains.values():
        if all(isinstance(v, bool) for v in values):
            total *= 2
        else:
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
    return prospective_case_space(domains) >= 64

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
        key = hashlib.sha256(f"{pmid}|{SALT}|RULE_ORACLE_NUMBOOL".encode()).hexdigest()
        eligible.append({
            "pmid": str(pmid),
            "title": str(record.get("title", "")).strip(),
            "function_name": function_name,
            "arg_count": arg_count,
            "domain_constants": domains,
            "prospective_case_space": prospective_case_space(domains),
            "code_sha256": hashlib.sha256(code.encode()).hexdigest(),
            "selection_key": key,
        })

    eligible.sort(key=lambda row: (row["selection_key"], row["pmid"]))
    selected = eligible[:SELECT_COUNT]
    if len(selected) < SELECT_COUNT:
        raise SystemExit(f"numeric/boolean oracle gate failed: only {len(selected)} eligible")
    manifest = {
        "status": "STATIC_NUMERIC_BOOLEAN_RULE_ORACLE_CANDIDATE_NO_FUNCTION_EXECUTION",
        "source_revision": SOURCE_REV,
        "source_blob": SOURCE_BLOB,
        "source_bytes_sha256": hashlib.sha256(raw).hexdigest(),
        "selector_salt": f"{SALT}|RULE_ORACLE_NUMBOOL",
        "eligibility": "one safe parsed function; <=8 args; every input used only as boolean/simple numeric comparison; no string domains; no input arithmetic/calls/subscripts/attributes; prospective generated input space >=64",
        "static_eligible_count": len(eligible),
        "selected_count": len(selected),
        "selected": selected,
    }
    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"STATIC_NUMBOOL_ORACLES={len(eligible)}")
    print(f"SELECTED={len(selected)}")
    print(f"OUT={OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
