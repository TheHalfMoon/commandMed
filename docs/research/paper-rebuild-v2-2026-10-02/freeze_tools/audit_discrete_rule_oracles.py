#!/usr/bin/env python3
"""Static AST audit for discrete/threshold RiskCalcs; never executes calculator code."""
from __future__ import annotations

import ast
import hashlib
import json
import urllib.request
from pathlib import Path

from select_riskcalcs_manifest import SOURCE_URL, SOURCE_REV, SOURCE_BLOB, SALT, extract_function

OUT = Path(__file__).resolve().parents[1] / "riskcalcs-rule-oracle-manifest-v5.json"
SELECT_COUNT = 64


def names_in(node: ast.AST) -> set[str]:
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}


def constant_values(node: ast.AST):
    if isinstance(node, ast.Constant) and isinstance(node.value, (bool, int, float, str)):
        return [node.value]
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        vals = []
        for elt in node.elts:
            if not isinstance(elt, ast.Constant) or not isinstance(elt.value, (bool, int, float, str)):
                return None
            vals.append(elt.value)
        return vals
    return None

def audit_discrete(code: str):
    tree = ast.parse(code)
    func = next(n for n in tree.body if isinstance(n, ast.FunctionDef))
    args = [a.arg for a in func.args.args]
    argset = set(args)
    domains = {a: set() for a in args}
    seen = {a: False for a in args}

    for node in ast.walk(func):
        if isinstance(node, ast.BinOp) and names_in(node) & argset:
            return None
        if isinstance(node, (ast.Subscript, ast.Attribute)) and names_in(node) & argset:
            return None
        if isinstance(node, ast.Call) and names_in(node) & argset:
            return None
        if isinstance(node, ast.For) and names_in(node.iter) & argset:
            return None

        if isinstance(node, ast.If):
            if isinstance(node.test, ast.Name) and node.test.id in argset:
                domains[node.test.id].update({False, True}); seen[node.test.id] = True
            if isinstance(node.test, ast.UnaryOp) and isinstance(node.test.op, ast.Not) and isinstance(node.test.operand, ast.Name) and node.test.operand.id in argset:
                domains[node.test.operand.id].update({False, True}); seen[node.test.operand.id] = True

        if isinstance(node, ast.Compare):
            parts = [node.left, *node.comparators]
            for idx, part in enumerate(parts):
                if not isinstance(part, ast.Name) or part.id not in argset:
                    continue
                seen[part.id] = True
                others = [p for j, p in enumerate(parts) if j != idx]
                vals = []
                for other in others:
                    cvals = constant_values(other)
                    if cvals is None:
                        return None
                    vals.extend(cvals)
                domains[part.id].update(vals)

    for node in ast.walk(func):
        if isinstance(node, ast.If):
            test_names = names_in(node.test) & argset
            for name in test_names:
                if not seen[name]:
                    domains[name].update({False, True})
                    seen[name] = True

    if not all(seen.values()):
        return None
    normalized = {}
    for name, vals in domains.items():
        if not vals:
            vals = {False, True}
        normalized[name] = sorted(vals, key=lambda v: (type(v).__name__, repr(v)))
    return normalized


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
        if domains is None:
            continue
        key = hashlib.sha256(f"{pmid}|{SALT}|RULE_ORACLE".encode()).hexdigest()
        eligible.append({
            "pmid": str(pmid),
            "title": str(record.get("title", "")).strip(),
            "function_name": function_name,
            "arg_count": arg_count,
            "domain_constants": domains,
            "code_sha256": hashlib.sha256(code.encode()).hexdigest(),
            "selection_key": key,
        })

    eligible.sort(key=lambda row: (row["selection_key"], row["pmid"]))
    selected = eligible[:SELECT_COUNT]
    if len(selected) < SELECT_COUNT:
        raise SystemExit(f"rule-oracle gate failed: only {len(selected)} eligible")
    manifest = {
        "status": "STATIC_RULE_ORACLE_CANDIDATE_ONLY_NO_FUNCTION_EXECUTION",
        "source_revision": SOURCE_REV,
        "source_blob": SOURCE_BLOB,
        "source_bytes_sha256": hashlib.sha256(raw).hexdigest(),
        "selector_salt": f"{SALT}|RULE_ORACLE",
        "static_rule_oracle_count": len(eligible),
        "selected_count": SELECT_COUNT,
        "selection_rule": "Inputs used only as booleans or simple constant comparisons; no input arithmetic/calls/subscripts/attributes; deterministic SHA-256 ordering",
        "selected": selected,
    }
    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"STATIC_RULE_ORACLES={len(eligible)}")
    print(f"SELECTED={len(selected)}")
    print(f"OUT={OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
