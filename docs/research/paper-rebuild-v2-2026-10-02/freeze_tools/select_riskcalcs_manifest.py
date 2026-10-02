#!/usr/bin/env python3
"""Static, non-executing selector for CommandMed V5 RiskCalcs candidates."""
from __future__ import annotations

import ast
import hashlib
import json
import re
import urllib.request
from pathlib import Path

SOURCE_URL = (
    "https://raw.githubusercontent.com/ncbi-nlp/Clinical-Tool-Learning/"
    "d474a95128e128623933c9be0d389ff7d82ef782/"
    "riskqa_evaluation/tools/riskcalcs.json"
)
SOURCE_REV = "d474a95128e128623933c9be0d389ff7d82ef782"
SOURCE_BLOB = "118474a6286ad78896a7c15682a53b68261a2330"
SALT = "CommandMed-V5"
SELECT_COUNT = 64
OUT = Path(__file__).resolve().parents[1] / "riskcalcs-manifest-v5.json"

BANNED_MODULES = {"os", "sys", "subprocess", "random", "time", "socket", "urllib", "requests", "pathlib"}
BANNED_CALLS = {"eval", "exec", "open", "input", "compile", "__import__"}
PY_BLOCK = re.compile(r"```python\s*(.*?)```", re.IGNORECASE | re.DOTALL)

def extract_function(computation: str):
    match = PY_BLOCK.search(computation or "")
    if not match:
        return None
    code = match.group(1).strip()
    if len(code) > 5000:
        return None
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None
    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    if len(funcs) != 1:
        return None
    func = funcs[0]
    if func.decorator_list or not (1 <= len(func.args.args) <= 12):
        return None
    if not any(isinstance(n, ast.Return) for n in ast.walk(func)):
        return None
    if any(isinstance(n, (ast.AsyncFunctionDef, ast.Await, ast.Yield, ast.YieldFrom)) for n in ast.walk(tree)):
        return None
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name.split(".")[0] for a in getattr(node, "names", [])] if isinstance(node, ast.Import) else [str(node.module or "").split(".")[0]]
            if any(name in BANNED_MODULES for name in names):
                return None
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in BANNED_CALLS:
            return None
    return code, func.name, len(func.args.args)

def main() -> int:
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "CommandMed-research"})
    with urllib.request.urlopen(req, timeout=30) as response:
        raw = response.read()
    data = json.loads(raw)
    candidates = []
    for pmid, record in data.items():
        if not all(str(record.get(k, "")).strip() for k in ("title", "eligibility", "interpretation", "computation")):
            continue
        extracted = extract_function(str(record["computation"]))
        if extracted is None:
            continue
        code, function_name, arg_count = extracted
        selection_key = hashlib.sha256(f"{pmid}|{SALT}".encode()).hexdigest()
        candidates.append({
            "pmid": str(pmid),
            "title": str(record["title"]).strip(),
            "function_name": function_name,
            "arg_count": arg_count,
            "code_sha256": hashlib.sha256(code.encode()).hexdigest(),
            "selection_key": selection_key,
        })
    candidates.sort(key=lambda row: (row["selection_key"], row["pmid"]))
    selected = candidates[:SELECT_COUNT]
    if len(selected) != SELECT_COUNT:
        raise SystemExit(f"eligibility gate failed: only {len(selected)} static candidates")
    manifest = {
        "status": "STATIC_SELECTION_ONLY_NO_FUNCTION_EXECUTION",
        "source_url": SOURCE_URL,
        "source_revision": SOURCE_REV,
        "source_blob": SOURCE_BLOB,
        "source_bytes_sha256": hashlib.sha256(raw).hexdigest(),
        "selector_salt": SALT,
        "static_candidate_count": len(candidates),
        "selected_count": len(selected),
        "selection_rule": "AST-parse one fenced Python function; required metadata; no banned modules/calls; SHA-256 deterministic ordering",
        "selected": selected,
    }
    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"STATIC_CANDIDATES={len(candidates)}")
    print(f"SELECTED={len(selected)}")
    print(f"OUT={OUT}")
    print(f"SOURCE_SHA256={manifest['source_bytes_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
