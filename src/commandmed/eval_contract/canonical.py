"""Deterministic semantic canonical JSON serialization and SHA-256 digest computation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

# Set-like fields whose list elements have no intrinsic order and should be normalized
SET_LIKE_LIST_FIELDS = {
    "languages",
    "roles",
    "modalities",
    "capability_domains",
    "applicable_roles",
    "applicable_modalities",
    "applicable_languages",
    "intended_strata",
    "allowed_access_roles",
    "prohibited_optimization_uses",
    "permitted_scoring_stages",
    "allowed_sources",
    "prohibited_sources",
}

# Known stable ID keys used to sort list of entity records
RECORD_SORT_KEYS = [
    "benchmark_id",
    "metric_id",
    "family_id",
    "purpose",
    "asset_id",
]


def semantic_normalize(obj: Any, parent_key: str = "") -> Any:
    """
    Recursively normalize objects semantically for deterministic hashing:
    - Sort dictionary keys.
    - Sort set-like list fields (e.g. languages, roles, modalities).
    - Sort collections of records by their stable primary keys.
    - Preserve order for genuinely semantic sequences.
    """
    if isinstance(obj, dict):
        return {k: semantic_normalize(v, k) for k, v in sorted(obj.items())}

    if isinstance(obj, list):
        if not obj:
            return []

        # Case 1: Parent key designates a set-like collection of scalar tags/enums
        if parent_key in SET_LIKE_LIST_FIELDS:
            normalized_items = [semantic_normalize(item) for item in obj]
            try:
                return sorted(normalized_items, key=lambda x: str(x))
            except TypeError:
                return normalized_items

        # Case 2: List of dictionary records containing a recognized primary key
        if isinstance(obj[0], dict):
            for sort_key in RECORD_SORT_KEYS:
                if all(isinstance(item, dict) and sort_key in item for item in obj):
                    sorted_records = sorted(obj, key=lambda item: str(item.get(sort_key, "")))
                    return [semantic_normalize(item) for item in sorted_records]

        # Case 3: Standard sequence (order preserved)
        return [semantic_normalize(item) for item in obj]

    return obj


def canonical_json_dumps(obj: Any) -> str:
    """
    Deterministically serialize Python object into semantic canonical JSON format.

    Guarantees:
    - Sorted object keys at all nesting depths.
    - Sorted set-like list fields (roles, modalities, languages, domains, etc.).
    - Sorted entity collections by stable identifier keys.
    - Compact canonical separators `,` and `:`.
    - ensure_ascii=False for clean UTF-8.
    """
    normalized_obj = semantic_normalize(obj)
    return json.dumps(
        normalized_obj,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def compute_canonical_sha256(obj: Any) -> str:
    """Compute SHA-256 hexdigest over semantic canonical JSON representation."""
    canonical_text = canonical_json_dumps(obj)
    canonical_bytes = canonical_text.encode("utf-8")
    return hashlib.sha256(canonical_bytes).hexdigest()


def compute_file_canonical_sha256(file_path: str | Path) -> str:
    """
    Load a JSON file, parse into Python data structure, and compute
    its deterministic semantic canonical SHA-256 digest.
    """
    p = Path(file_path)
    if not p.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    raw_text = p.read_text(encoding="utf-8")
    data = json.loads(raw_text)
    return compute_canonical_sha256(data)
