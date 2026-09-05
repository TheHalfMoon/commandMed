#!/usr/bin/env python3
"""Emit a fail-closed deterministic SP007-RO-001 nonce-repair bundle.

This temporary construction utility is authority-bound to the canonical Founder
nonce-repair Decision B. It changes only case/probe nonce fields and the exact
full-nonce occurrence in the corresponding prompt/input text, then recomputes
identities derived from those bytes. It performs no model loading, inference,
device access, training, protected-data access, winner selection, network access,
or spend.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.research_tournament import (
    compute_research_component_tournament_protocol_sha256,
)
from src.commandmed.spec007.research_tournament_assets import (
    ASSET_NAMESPACE_SEED,
    build_protocol_asset_manifest,
    compute_research_component_evaluation_asset_set_sha256,
    compute_research_component_evaluation_asset_sha256,
    evaluate_research_component_asset_admission,
)

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "specs" / "007-sft-v1"
DECISION = SPEC / "e004-research-component-evaluation-nonce-repair-founder-decision-2026-09-05.md"
ASSET_SET_PATH = SPEC / "e004-research-component-tournament-evaluation-assets-v1.json"
PROVENANCE_PATH = SPEC / "e004-research-component-evaluation-asset-provenance-instrument-v1.json"
SOURCE_PATH = SPEC / "e004-research-component-evaluation-asset-source-verification-v1.json"
PRIVACY_PATH = SPEC / "e004-research-component-evaluation-asset-privacy-classification-v1.json"
PROTOCOL_PATH = SPEC / "e004-research-component-tournament-protocol-v1.json"
LINEAGE_PATH = ROOT / "data" / "lineage" / "lineage_contract.json"
ASSET_EVIDENCE_CODE_PATH = ROOT / "src" / "commandmed" / "spec007" / "research_tournament_asset_evidence.py"
QUALIFICATION_CODE_PATH = ROOT / "src" / "commandmed" / "spec007" / "research_tournament_qualification.py"

DECISION_TOKEN = (
    "FOUNDER_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION="
    "E004_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION_B"
)
REQUIRED_DECISION_LINES = {
    DECISION_TOKEN,
    "EVAL_NONCE_REPAIR_AUTHORITY=AUTHORIZED_PREEXISTING_VALIDATOR_METHOD_ONLY",
    "EVAL_NONCE_REPAIR_INDEXING=ONE_BASED_DECIMAL_UNPADDED",
    "EVAL_NONCE_EMBEDDING_REPAIR_AUTHORITY=AUTHORIZED_EXACT_NONCE_FIELDS_AND_REQUIRED_PROMPT_INPUT_EMBEDDINGS_ONLY",
    "EVAL_NONCE_SEMANTIC_PAYLOAD_REWRITE_AUTHORITY=NONE",
    "EVAL_DERIVED_ASSET_HASH_REBIND_AUTHORITY=AUTHORIZED_DETERMINISTIC_RECOMPUTATION_ONLY",
    "EVAL_DERIVED_ASSET_SET_HASH_REBIND_AUTHORITY=AUTHORIZED_DETERMINISTIC_RECOMPUTATION_ONLY",
    "EVAL_DERIVED_PROVENANCE_BINDING_REBIND_AUTHORITY=AUTHORIZED_NEW_ASSET_SET_HASH_ONLY",
    "EVAL_DERIVED_SOURCE_VERIFICATION_REBIND_AUTHORITY=AUTHORIZED_NEW_ASSET_SET_HASH_ONLY",
    "EVAL_DERIVED_PRIVACY_BINDING_REBIND_AUTHORITY=AUTHORIZED_NEW_ASSET_SET_HASH_ONLY",
    "EVAL_DERIVED_PROTOCOL_MANIFEST_REBIND_AUTHORITY=AUTHORIZED_ONLY_AFTER_ALL_REPAIRED_ASSETS_COMPUTE_ELIGIBLE",
    "EVAL_DERIVED_PROTOCOL_HASH_REBIND_AUTHORITY=AUTHORIZED_DETERMINISTIC_RECOMPUTATION_ONLY",
    "CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED",
    "CURRENT_AUTHORIZED_SPEND_USD=0",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def self_hash(record: Mapping[str, Any], identity_field: str) -> str:
    projection = dict(record)
    projection.pop(identity_field, None)
    return compute_canonical_sha256(projection)


def expected_nonce(metric_family: str, index: int) -> str:
    raw = f"{ASSET_NAMESPACE_SEED}|{metric_family}|{index}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]


def normalized_asset_for_semantic_compare(asset: Mapping[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(dict(asset))
    if out.get("asset_kind") == "MULTIPLE_CHOICE_CONDITIONAL_LIKELIHOOD":
        for case in out.get("cases", []):
            nonce = case.get("case_nonce")
            prompt = case.get("prompt")
            if not isinstance(nonce, str) or not isinstance(prompt, str):
                raise ValueError("semantic projection requires string case nonce/prompt")
            if prompt.count(nonce) != 1:
                raise ValueError("semantic projection requires exactly one full case nonce embedding")
            case["prompt"] = prompt.replace(nonce, "<NONCE>", 1)
            case["case_nonce"] = "<NONCE>"
    elif out.get("asset_kind") == "RESOURCE_MEASUREMENT_PROTOCOL":
        for probe in out.get("probes", []):
            nonce = probe.get("probe_nonce")
            text = probe.get("input_text")
            if not isinstance(nonce, str) or not isinstance(text, str):
                raise ValueError("semantic projection requires string probe nonce/input_text")
            if text.count(nonce) != 1:
                raise ValueError("semantic projection requires exactly one full probe nonce embedding")
            probe["input_text"] = text.replace(nonce, "<NONCE>", 1)
            probe["probe_nonce"] = "<NONCE>"
    else:
        raise ValueError(f"unsupported asset kind: {out.get('asset_kind')}")
    out.pop("asset_sha256", None)
    return out


def repair_asset(asset: Mapping[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    original = copy.deepcopy(dict(asset))
    repaired = copy.deepcopy(dict(asset))
    family = str(repaired.get("metric_family"))
    edits: list[dict[str, Any]] = []

    if repaired.get("asset_kind") == "MULTIPLE_CHOICE_CONDITIONAL_LIKELIHOOD":
        cases = repaired.get("cases")
        if not isinstance(cases, list) or len(cases) != 12:
            raise ValueError(f"{repaired.get('asset_id')}: exact 12-case subject required")
        for index, case in enumerate(cases, start=1):
            if not isinstance(case, dict):
                raise ValueError("case must be object")
            old_nonce = case.get("case_nonce")
            prompt = case.get("prompt")
            if not isinstance(old_nonce, str) or not isinstance(prompt, str):
                raise ValueError("case nonce/prompt must be strings")
            if prompt.count(old_nonce) != 1:
                raise ValueError(
                    f"{case.get('case_id')}: exact old full nonce must occur once in prompt"
                )
            new_nonce = expected_nonce(family, index)
            case["case_nonce"] = new_nonce
            case["prompt"] = prompt.replace(old_nonce, new_nonce, 1)
            edits.append(
                {
                    "record_id": case.get("case_id"),
                    "field": "case_nonce+prompt_full_nonce_embedding",
                    "old_nonce": old_nonce,
                    "new_nonce": new_nonce,
                }
            )
    elif repaired.get("asset_kind") == "RESOURCE_MEASUREMENT_PROTOCOL":
        probes = repaired.get("probes")
        if not isinstance(probes, list) or len(probes) != 8:
            raise ValueError(f"{repaired.get('asset_id')}: exact 8-probe subject required")
        for index, probe in enumerate(probes, start=1):
            if not isinstance(probe, dict):
                raise ValueError("probe must be object")
            old_nonce = probe.get("probe_nonce")
            text = probe.get("input_text")
            if not isinstance(old_nonce, str) or not isinstance(text, str):
                raise ValueError("probe nonce/input_text must be strings")
            if text.count(old_nonce) != 1:
                raise ValueError(
                    f"{probe.get('probe_id')}: exact old full nonce must occur once in input_text"
                )
            new_nonce = expected_nonce(family, index)
            probe["probe_nonce"] = new_nonce
            probe["input_text"] = text.replace(old_nonce, new_nonce, 1)
            edits.append(
                {
                    "record_id": probe.get("probe_id"),
                    "field": "probe_nonce+input_text_full_nonce_embedding",
                    "old_nonce": old_nonce,
                    "new_nonce": new_nonce,
                }
            )
    else:
        raise ValueError(f"unsupported asset kind: {repaired.get('asset_kind')}")

    original_projection = normalized_asset_for_semantic_compare(original)
    repaired_projection = normalized_asset_for_semantic_compare(repaired)
    if original_projection != repaired_projection:
        raise ValueError(f"{repaired.get('asset_id')}: unauthorized semantic payload change")

    repaired["asset_sha256"] = compute_research_component_evaluation_asset_sha256(repaired)
    return repaired, edits


def replace_exact(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected exactly one old identity occurrence, found {count}")
    return text.replace(old, new, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit-bundle", required=True)
    args = parser.parse_args()

    decision_text = DECISION.read_text(encoding="utf-8")
    present = {line.strip() for line in decision_text.splitlines()}
    missing = sorted(REQUIRED_DECISION_LINES - present)
    if missing:
        raise SystemExit("Missing canonical nonce-repair authority lines: " + "; ".join(missing))

    original_asset_set = load_json(ASSET_SET_PATH)
    repaired_asset_set = copy.deepcopy(original_asset_set)
    assets = repaired_asset_set.get("asset_records")
    if not isinstance(assets, list) or len(assets) != 7:
        raise SystemExit("Exact seven-asset subject required")

    original_asset_hashes: dict[str, str] = {}
    repaired_asset_hashes: dict[str, str] = {}
    edit_log: list[dict[str, Any]] = []
    repaired_assets: list[dict[str, Any]] = []
    for asset in assets:
        if not isinstance(asset, dict):
            raise SystemExit("Every asset must be an object")
        asset_id = str(asset.get("asset_id"))
        original_asset_hashes[asset_id] = str(asset.get("asset_sha256"))
        repaired, edits = repair_asset(asset)
        repaired_asset_hashes[asset_id] = repaired["asset_sha256"]
        repaired_assets.append(repaired)
        edit_log.extend(edits)

    if len(edit_log) != 80:
        raise SystemExit(f"Exact 80 nonce records required, got {len(edit_log)}")

    repaired_asset_set["asset_records"] = repaired_assets
    original_asset_set_sha = str(original_asset_set.get("asset_set_sha256"))
    repaired_asset_set["asset_set_sha256"] = (
        compute_research_component_evaluation_asset_set_sha256(repaired_asset_set)
    )
    repaired_asset_set_sha = repaired_asset_set["asset_set_sha256"]

    lineage_contract = load_json(LINEAGE_PATH)
    admissions = [
        evaluate_research_component_asset_admission(asset, lineage_contract)
        for asset in repaired_assets
    ]
    if any(result.get("state") != "ELIGIBLE" for result in admissions):
        raise SystemExit(f"Repaired Spec003 admission failed closed: {admissions}")

    provenance = load_json(PROVENANCE_PATH)
    old_provenance_sha = str(provenance.get("instrument_sha256"))
    provenance["asset_set_sha256"] = repaired_asset_set_sha
    provenance["instrument_sha256"] = self_hash(provenance, "instrument_sha256")
    new_provenance_sha = provenance["instrument_sha256"]

    source = load_json(SOURCE_PATH)
    old_source_sha = str(source.get("instrument_sha256"))
    source["asset_set_sha256"] = repaired_asset_set_sha
    source["provenance_instrument_sha256"] = new_provenance_sha
    source["instrument_sha256"] = self_hash(source, "instrument_sha256")
    new_source_sha = source["instrument_sha256"]

    privacy = load_json(PRIVACY_PATH)
    old_privacy_sha = str(privacy.get("instrument_sha256"))
    privacy["asset_set_sha256"] = repaired_asset_set_sha
    privacy["instrument_sha256"] = self_hash(privacy, "instrument_sha256")
    new_privacy_sha = privacy["instrument_sha256"]

    protocol = load_json(PROTOCOL_PATH)
    old_protocol_sha = str(protocol.get("protocol_sha256"))
    protocol["evaluation_asset_manifests"] = [
        build_protocol_asset_manifest(asset) for asset in repaired_assets
    ]
    protocol["protocol_sha256"] = compute_research_component_tournament_protocol_sha256(protocol)
    new_protocol_sha = protocol["protocol_sha256"]

    evidence_code = ASSET_EVIDENCE_CODE_PATH.read_text(encoding="utf-8")
    evidence_code = replace_exact(
        evidence_code,
        original_asset_set_sha,
        repaired_asset_set_sha,
        "asset evidence ASSET_SET_SHA256",
    )
    evidence_code = replace_exact(
        evidence_code,
        old_provenance_sha,
        new_provenance_sha,
        "asset evidence PROVENANCE_INSTRUMENT_SHA256",
    )
    evidence_code = replace_exact(
        evidence_code,
        old_source_sha,
        new_source_sha,
        "asset evidence SOURCE_VERIFICATION_INSTRUMENT_SHA256",
    )

    qualification_code = QUALIFICATION_CODE_PATH.read_text(encoding="utf-8")
    qualification_code = replace_exact(
        qualification_code,
        old_privacy_sha,
        new_privacy_sha,
        "qualification PRIVACY_INSTRUMENT_SHA256",
    )

    repair_evidence = {
        "schema_version": "1",
        "evidence_id": "E004_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_EVIDENCE_V1",
        "founder_decision_token": DECISION_TOKEN,
        "repair_formula": 'SHA256(f"{fixture_namespace_seed}|{metric_family}|{index}")[:16]',
        "repair_indexing": "ONE_BASED_DECIMAL_UNPADDED",
        "fixture_namespace_seed": ASSET_NAMESPACE_SEED,
        "nonce_record_count": len(edit_log),
        "semantic_payload_change": False,
        "semantic_projection_proof": "PASS",
        "caller_controlled_eligible_state": False,
        "original_asset_set_sha256": original_asset_set_sha,
        "repaired_asset_set_sha256": repaired_asset_set_sha,
        "asset_hash_rebindings": [
            {
                "asset_id": asset_id,
                "old_asset_sha256": original_asset_hashes[asset_id],
                "new_asset_sha256": repaired_asset_hashes[asset_id],
            }
            for asset_id in original_asset_hashes
        ],
        "provenance_sha256_rebinding": {
            "old": old_provenance_sha,
            "new": new_provenance_sha,
        },
        "source_verification_sha256_rebinding": {
            "old": old_source_sha,
            "new": new_source_sha,
        },
        "privacy_sha256_rebinding": {
            "old": old_privacy_sha,
            "new": new_privacy_sha,
        },
        "protocol_sha256_rebinding": {
            "old": old_protocol_sha,
            "new": new_protocol_sha,
        },
        "spec003_admissions": [
            {
                "asset_id": repaired_assets[index]["asset_id"],
                "state": result.get("state"),
                "reason_codes": result.get("reason_codes", []),
            }
            for index, result in enumerate(admissions)
        ],
        "model_execution_performed": False,
        "tournament_execution_performed": False,
        "winner_selected": False,
        "training_performed": False,
        "private_gold_accessed": False,
        "phi_accessed": False,
        "authorized_spend_usd": 0,
        "nonce_edits": edit_log,
    }

    files = {
        ASSET_SET_PATH.relative_to(ROOT).as_posix(): dump_json(repaired_asset_set),
        PROVENANCE_PATH.relative_to(ROOT).as_posix(): dump_json(provenance),
        SOURCE_PATH.relative_to(ROOT).as_posix(): dump_json(source),
        PRIVACY_PATH.relative_to(ROOT).as_posix(): dump_json(privacy),
        PROTOCOL_PATH.relative_to(ROOT).as_posix(): dump_json(protocol),
        ASSET_EVIDENCE_CODE_PATH.relative_to(ROOT).as_posix(): evidence_code,
        QUALIFICATION_CODE_PATH.relative_to(ROOT).as_posix(): qualification_code,
        "specs/007-sft-v1/e004-research-component-evaluation-nonce-repair-evidence-v1.json": dump_json(repair_evidence),
    }

    bundle = {
        "schema_version": "1",
        "result": "PASS",
        "founder_decision_token": DECISION_TOKEN,
        "semantic_projection_proof": "PASS",
        "nonce_record_count": len(edit_log),
        "all_spec003_admissions_eligible": True,
        "original_asset_set_sha256": original_asset_set_sha,
        "repaired_asset_set_sha256": repaired_asset_set_sha,
        "old_protocol_sha256": old_protocol_sha,
        "new_protocol_sha256": new_protocol_sha,
        "files": files,
    }
    output = Path(args.emit_bundle)
    output.write_text(dump_json(bundle), encoding="utf-8")

    print(f"NONCE_REPAIR_DECISION={DECISION_TOKEN}")
    print(f"NONCE_RECORD_COUNT={len(edit_log)}")
    print("SEMANTIC_PROJECTION_PROOF=PASS")
    print(f"ORIGINAL_ASSET_SET_SHA256={original_asset_set_sha}")
    print(f"REPAIRED_ASSET_SET_SHA256={repaired_asset_set_sha}")
    for asset_id in original_asset_hashes:
        print(
            "ASSET_HASH_REBINDING="
            f"{asset_id}|old={original_asset_hashes[asset_id]}|new={repaired_asset_hashes[asset_id]}"
        )
    print(f"PROVENANCE_SHA256={new_provenance_sha}")
    print(f"SOURCE_VERIFICATION_SHA256={new_source_sha}")
    print(f"PRIVACY_SHA256={new_privacy_sha}")
    print(f"PROTOCOL_SHA256={new_protocol_sha}")
    print("SPEC003_ELIGIBLE_COUNT=7")
    print("MODEL_EXECUTION_PERFORMED=NO")
    print("TOURNAMENT_EXECUTION_PERFORMED=NO")
    print("WINNER_SELECTED=NO")
    print("TRAINING_PERFORMED=NO")
    print("CURRENT_AUTHORIZED_SPEND_USD=0")
    print("RESULT=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
