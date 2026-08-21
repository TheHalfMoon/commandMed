"""Deterministic canonical JSON serialization and SHA-256 digest computation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def _sort_recursively(obj: Any) -> Any:
    """Recursively sort dictionary keys for deterministic canonicalization."""
    if isinstance(obj, dict):
        return {k: _sort_recursively(v) for k, v in sorted(obj.items())}
    elif isinstance(obj, list):
        return [_sort_recursively(item) for item in obj]
    return obj


def canonical_json_dumps(obj: Any) -> str:
    """
    Deterministically serialize Python object into canonical JSON format.

    Guarantees:
    - Sorted object keys at all nesting depths.
    - No insignificant whitespace (compact separators `,` and `:`).
    - ensure_ascii=False for clean UTF-8.
    - Deterministic across platforms and key insertion orders.
    """
    sorted_obj = _sort_recursively(obj)
    return json.dumps(
        sorted_obj,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def compute_canonical_sha256(obj: Any) -> str:
    """Compute SHA-256 hexdigest over canonical JSON representation."""
    canonical_text = canonical_json_dumps(obj)
    canonical_bytes = canonical_text.encode("utf-8")
    return hashlib.sha256(canonical_bytes).hexdigest()


def compute_file_canonical_sha256(file_path: str | Path) -> str:
    """
    Load a JSON file, parse into Python data structure, and compute
    its deterministic canonical SHA-256 digest.
    """
    p = Path(file_path)
    if not p.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    raw_text = p.read_text(encoding="utf-8")
    data = json.loads(raw_text)
    return compute_canonical_sha256(data)
