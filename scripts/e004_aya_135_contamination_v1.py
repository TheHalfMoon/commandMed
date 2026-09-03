#!/usr/bin/env python3
"""Deterministic local-only curriculum contamination assessment for exact Aya 135."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

SOURCE_SHA256 = "51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06"
SOURCE_SIZE = 137195800
EXPECTED_CANDIDATE_COUNT = 135
EXPECTED_MANIFEST_CANONICAL_SHA256 = "dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99"
EXPECTED_RECORD_ID_SET_SHA256 = "d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83"
EXPECTED_CONTENT_SHA256_SET_SHA256 = "ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64"
EXPECTED_UNIVERSE_CANONICAL_SHA256 = "e473b2607b28467f3bd055fb34a1e1092fc15f87558185e989d8e4c483c0e98e"
METHOD_ID = "AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1"
NGRAM_N = 13
TOKEN_RE = re.compile(r"\w+", re.UNICODE)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def set_root(values: Iterable[str]) -> str:
    ordered = sorted(values)
    return hashlib.sha256(("\n".join(ordered) + "\n").encode("ascii")).hexdigest()


def normalize_candidate_text(value: str | None) -> str:
    text = unicodedata.normalize("NFC", value or "")
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def tokenize(value: str) -> list[str]:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return TOKEN_RE.findall(normalized)


def ngram_digests(value: str) -> Iterable[bytes]:
    tokens = tokenize(value)
    if len(tokens) < NGRAM_N:
        return
    for i in range(len(tokens) - NGRAM_N + 1):
        gram = "\x1f".join(tokens[i : i + NGRAM_N]).encode("utf-8")
        yield hashlib.sha256(gram).digest()


def string_leaves(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from string_leaves(item)
    elif isinstance(value, dict):
        for key in sorted(value):
            yield from string_leaves(value[key])


def json_values(path: Path) -> Iterable[Any]:
    if path.suffix.lower() == ".jsonl":
        with path.open("r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, 1):
                if not line.strip():
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError as exc:
                    raise SystemExit(f"COMPARISON_JSONL_PARSE_ERROR:{path.name}:{line_number}:{exc.msg}") from exc
    else:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"COMPARISON_JSON_PARSE_ERROR:{path.name}:{exc.msg}") from exc
        yield payload


def verify_transport(universe: dict[str, Any], transport: dict[str, Any], comparison_dir: Path) -> dict[str, dict[str, Any]]:
    if transport.get("schema_version") != "1":
        raise SystemExit("TRANSPORT_MANIFEST_SCHEMA_MISMATCH")
    observed = {item["comparison_id"]: item for item in transport.get("entries", [])}
    if set(observed) != {item["comparison_id"] for item in universe["entries"]}:
        raise SystemExit("TRANSPORT_MANIFEST_UNIVERSE_MISMATCH")

    verified: dict[str, dict[str, Any]] = {}
    for item in universe["entries"]:
        cid = item["comparison_id"]
        obs = observed[cid]
        for field in ("source_repository", "source_revision", "path", "local_filename"):
            if obs.get(field) != item.get(field):
                raise SystemExit(f"TRANSPORT_IDENTITY_MISMATCH:{cid}:{field}")
        path = comparison_dir / item["local_filename"]
        if not path.is_file():
            raise SystemExit(f"COMPARISON_FILE_MISSING:{cid}")
        actual_size = path.stat().st_size
        actual_sha = sha256_file(path)
        if obs.get("observed_size_bytes") != actual_size or obs.get("observed_sha256") != actual_sha:
            raise SystemExit(f"TRANSPORT_LOCAL_BYTE_MISMATCH:{cid}")
        if item["binding_state"] == "DIRECT_SHA256":
            if actual_sha != item["expected_sha256"] or actual_size != item["expected_size_bytes"]:
                raise SystemExit(f"COMPARISON_DIRECT_BINDING_MISMATCH:{cid}")
        if item["binding_state"] == "IMMUTABLE_REVISION_LOCATOR_AND_GIT_BLOB":
            if git_blob_sha1(path) != item["expected_git_blob_sha1"]:
                raise SystemExit(f"COMPARISON_GIT_BLOB_MISMATCH:{cid}")
        verified[cid] = {"sha256": actual_sha, "size_bytes": actual_size}
    return verified


def load_exact_candidates(parquet_path: Path, manifest: dict[str, Any]) -> tuple[dict[str, dict[str, str]], dict[bytes, set[str]]]:
    import pyarrow.parquet as pq

    if parquet_path.stat().st_size != SOURCE_SIZE or sha256_file(parquet_path) != SOURCE_SHA256:
        raise SystemExit("AYA_SOURCE_BYTE_IDENTITY_MISMATCH")
    if hashlib.sha256(canonical_bytes(manifest)).hexdigest() != EXPECTED_MANIFEST_CANONICAL_SHA256:
        raise SystemExit("CANDIDATE_MANIFEST_CANONICAL_SHA256_MISMATCH")
    records = manifest.get("records")
    if not isinstance(records, list) or len(records) != EXPECTED_CANDIDATE_COUNT:
        raise SystemExit("CANDIDATE_COUNT_MISMATCH")
    ids = [str(r["candidate_record_id"]) for r in records]
    content_hashes = [str(r["content_sha256"]) for r in records]
    if set_root(ids) != EXPECTED_RECORD_ID_SET_SHA256:
        raise SystemExit("CANDIDATE_RECORD_ID_SET_SHA256_MISMATCH")
    if set_root(content_hashes) != EXPECTED_CONTENT_SHA256_SET_SHA256:
        raise SystemExit("CANDIDATE_CONTENT_SHA256_SET_SHA256_MISMATCH")

    by_content = {str(r["content_sha256"]): str(r["candidate_record_id"]) for r in records}
    if len(by_content) != EXPECTED_CANDIDATE_COUNT:
        raise SystemExit("CANDIDATE_CONTENT_HASH_NOT_UNIQUE")

    found: dict[str, dict[str, str]] = {}
    gram_to_candidates: dict[bytes, set[str]] = defaultdict(set)
    pqf = pq.ParquetFile(parquet_path)
    row_index = 0
    columns = ["inputs", "targets", "language_code", "annotation_type"]
    for rg in range(pqf.num_row_groups):
        table = pqf.read_row_group(rg, columns=columns)
        for prompt_raw, target_raw, language_code, annotation_type in zip(
            table["inputs"].to_pylist(), table["targets"].to_pylist(),
            table["language_code"].to_pylist(), table["annotation_type"].to_pylist(), strict=True
        ):
            prompt = normalize_candidate_text(prompt_raw)
            target = normalize_candidate_text(target_raw)
            representation = {
                "annotation_type": annotation_type,
                "inputs": prompt,
                "language_code": language_code,
                "targets": target,
            }
            content_sha = hashlib.sha256(canonical_bytes(representation)).hexdigest()
            candidate_id = by_content.get(content_sha)
            if candidate_id is not None:
                recomputed_id = hashlib.sha256(f"{SOURCE_SHA256}:{row_index}:{content_sha}".encode("ascii")).hexdigest()
                if recomputed_id != candidate_id:
                    raise SystemExit("CANDIDATE_RECORD_ID_REPLAY_MISMATCH")
                if candidate_id in found:
                    raise SystemExit("CANDIDATE_REPLAY_DUPLICATE_MATCH")
                found[candidate_id] = {"content_sha256": content_sha}
                for field_text in (prompt, target):
                    for digest in ngram_digests(field_text):
                        gram_to_candidates[digest].add(candidate_id)
            row_index += 1

    if set(found) != set(ids):
        raise SystemExit("CANDIDATE_REPLAY_INCOMPLETE")
    return found, gram_to_candidates


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--aya-parquet", required=True, type=Path)
    parser.add_argument("--candidate-manifest", required=True, type=Path)
    parser.add_argument("--universe", required=True, type=Path)
    parser.add_argument("--transport-manifest", required=True, type=Path)
    parser.add_argument("--comparison-dir", required=True, type=Path)
    parser.add_argument("--out-results", required=True, type=Path)
    parser.add_argument("--out-summary", required=True, type=Path)
    args = parser.parse_args()

    manifest = json.loads(args.candidate_manifest.read_text(encoding="utf-8"))
    universe = json.loads(args.universe.read_text(encoding="utf-8"))
    if hashlib.sha256(canonical_bytes(universe)).hexdigest() != EXPECTED_UNIVERSE_CANONICAL_SHA256:
        raise SystemExit("COMPARISON_UNIVERSE_IDENTITY_MISMATCH")
    transport = json.loads(args.transport_manifest.read_text(encoding="utf-8"))
    verified_comparison = verify_transport(universe, transport, args.comparison_dir)
    candidates, gram_to_candidates = load_exact_candidates(args.aya_parquet, manifest)

    overlap_counts: Counter[str] = Counter()
    overlap_assets: dict[str, set[str]] = defaultdict(set)
    files_processed = 0
    string_leaves_processed = 0
    comparison_windows_processed = 0

    for entry in universe["entries"]:
        cid = entry["comparison_id"]
        path = args.comparison_dir / entry["local_filename"]
        files_processed += 1
        for value in json_values(path):
            for text in string_leaves(value):
                string_leaves_processed += 1
                for digest in ngram_digests(text):
                    comparison_windows_processed += 1
                    candidate_ids = gram_to_candidates.get(digest)
                    if not candidate_ids:
                        continue
                    for candidate_id in candidate_ids:
                        overlap_counts[candidate_id] += 1
                        overlap_assets[candidate_id].add(cid)

    results = []
    state_counts: Counter[str] = Counter()
    for candidate_id in sorted(candidates):
        state = "OVERLAP_OR_HIGH_RISK" if overlap_counts[candidate_id] else "ASSESSED_CLEAN"
        state_counts[state] += 1
        results.append({
            "candidate_record_id": candidate_id,
            "content_sha256": candidates[candidate_id]["content_sha256"],
            "contamination_state": state,
            "overlap_comparison_ids": sorted(overlap_assets[candidate_id]),
            "overlap_13_token_window_count": overlap_counts[candidate_id],
        })

    summary = {
        "schema_version": "1",
        "artifact_id": "e004-aya-135-contamination-assessment-v1",
        "method_id": METHOD_ID,
        "candidate_count": len(results),
        "universe_canonical_sha256": EXPECTED_UNIVERSE_CANONICAL_SHA256,
        "comparison_file_count": files_processed,
        "comparison_files_verified": len(verified_comparison),
        "comparison_string_leaves_processed": string_leaves_processed,
        "comparison_13_token_windows_processed": comparison_windows_processed,
        "state_counts": dict(sorted(state_counts.items())),
        "semantic_judge_used": False,
        "model_inference_used": False,
        "private_gold_used": False,
        "gated_or_credentialed_asset_used": False,
        "raw_text_emitted": False,
        "post_result_threshold_change": False,
        "post_result_universe_change": False,
        "comparison_observed_byte_identities": verified_comparison,
    }
    args.out_results.write_text(json.dumps({"summary": summary, "records": results}, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    args.out_summary.write_text(json.dumps(summary, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
