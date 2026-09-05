#!/usr/bin/env python3
"""Emit the bounded deterministic SP007-RO-001 nonce-repair bundle.

The repair is authority-bound to canonical Founder nonce-repair Decision B. For
each case/probe it changes the nonce field plus only the first exact full-nonce
embedding in prompt/input text. It also carries one narrow validator correction:
the exact descriptor ``non-clinical`` is not treated as positive clinical content,
while standalone ``clinical`` and every other frozen marker remain prohibited.
No model execution, device access, training, protected-data access, winner
selection, network access, or spend occurs.
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
import src.commandmed.spec007.research_tournament_assets as asset_module

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "specs" / "007-sft-v1"
DECISION = SPEC / "e004-research-component-evaluation-nonce-repair-founder-decision-2026-09-05.md"
ASSET_SET_PATH = SPEC / "e004-research-component-tournament-evaluation-assets-v1.json"
PROVENANCE_PATH = SPEC / "e004-research-component-evaluation-asset-provenance-instrument-v1.json"
SOURCE_PATH = SPEC / "e004-research-component-evaluation-asset-source-verification-v1.json"
PRIVACY_PATH = SPEC / "e004-research-component-evaluation-asset-privacy-classification-v1.json"
PROTOCOL_PATH = SPEC / "e004-research-component-tournament-protocol-v1.json"
LINEAGE_PATH = ROOT / "data" / "lineage" / "lineage_contract.json"
ASSET_CODE_PATH = ROOT / "src/commandmed/spec007/research_tournament_assets.py"
ASSET_EVIDENCE_CODE_PATH = ROOT / "src/commandmed/spec007/research_tournament_asset_evidence.py"
QUALIFICATION_CODE_PATH = ROOT / "src/commandmed/spec007/research_tournament_qualification.py"
ASSET_TEST_PATH = ROOT / "tests/spec007/test_research_tournament_assets.py"

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

OLD_CLINICAL_VALIDATOR = '''def _contains_clinical_content(value: str) -> bool:\n    lowered = value.lower()\n    return any(marker in lowered for marker in _FORBIDDEN_CLINICAL_SUBSTRINGS)\n'''
NEW_CLINICAL_VALIDATOR = '''def _contains_clinical_content(value: str) -> bool:\n    # The frozen asset vocabulary explicitly uses "non-clinical" to mark\n    # research-only content. Remove only that exact negative descriptor before\n    # applying the unchanged positive clinical-marker denylist.\n    lowered = value.lower().replace("non-clinical", "")\n    return any(marker in lowered for marker in _FORBIDDEN_CLINICAL_SUBSTRINGS)\n'''


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def self_hash(record: Mapping[str, Any], field: str) -> str:
    projected = dict(record)
    projected.pop(field, None)
    return compute_canonical_sha256(projected)


def expected_nonce(metric_family: str, index: int) -> str:
    raw = f"{asset_module.ASSET_NAMESPACE_SEED}|{metric_family}|{index}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]


def replace_required_embedding(text: str, old_nonce: str, new_nonce: str, label: str) -> str:
    if old_nonce not in text:
        raise ValueError(f"{label}: old full nonce embedding is absent")
    return text.replace(old_nonce, new_nonce, 1)


def semantic_projection(asset: Mapping[str, Any]) -> dict[str, Any]:
    projected = copy.deepcopy(dict(asset))
    projected.pop("asset_sha256", None)
    kind = projected.get("asset_kind")
    if kind == "MULTIPLE_CHOICE_CONDITIONAL_LIKELIHOOD":
        for record in projected.get("cases", []):
            nonce = record.get("case_nonce")
            prompt = record.get("prompt")
            if not isinstance(nonce, str) or not isinstance(prompt, str):
                raise ValueError("semantic projection requires string case nonce/prompt")
            record["prompt"] = replace_required_embedding(
                prompt, nonce, "<NONCE>", str(record.get("case_id"))
            )
            record["case_nonce"] = "<NONCE>"
    elif kind == "RESOURCE_MEASUREMENT_PROTOCOL":
        for record in projected.get("probes", []):
            nonce = record.get("probe_nonce")
            text = record.get("input_text")
            if not isinstance(nonce, str) or not isinstance(text, str):
                raise ValueError("semantic projection requires string probe nonce/input_text")
            record["input_text"] = replace_required_embedding(
                text, nonce, "<NONCE>", str(record.get("probe_id"))
            )
            record["probe_nonce"] = "<NONCE>"
    else:
        raise ValueError(f"unsupported asset kind: {kind}")
    return projected


def repair_asset(asset: Mapping[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    original = copy.deepcopy(dict(asset))
    repaired = copy.deepcopy(dict(asset))
    family = str(repaired.get("metric_family"))
    edits: list[dict[str, Any]] = []
    kind = repaired.get("asset_kind")

    if kind == "MULTIPLE_CHOICE_CONDITIONAL_LIKELIHOOD":
        records = repaired.get("cases")
        expected_count = 12
        nonce_field, text_field = "case_nonce", "prompt"
    elif kind == "RESOURCE_MEASUREMENT_PROTOCOL":
        records = repaired.get("probes")
        expected_count = 8
        nonce_field, text_field = "probe_nonce", "input_text"
    else:
        raise ValueError(f"unsupported asset kind: {kind}")
    if not isinstance(records, list) or len(records) != expected_count:
        raise ValueError(f"{repaired.get('asset_id')}: exact record count required")

    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError("evaluation record must be object")
        old_nonce = record.get(nonce_field)
        text = record.get(text_field)
        record_id = str(record.get("case_id") or record.get("probe_id"))
        if not isinstance(old_nonce, str) or not isinstance(text, str):
            raise ValueError(f"{record_id}: nonce/text must be strings")
        new_nonce = expected_nonce(family, index)
        record[text_field] = replace_required_embedding(text, old_nonce, new_nonce, record_id)
        record[nonce_field] = new_nonce
        edits.append(
            {
                "record_id": record_id,
                "field": f"{nonce_field}+first_{text_field}_full_nonce_embedding",
                "old_nonce": old_nonce,
                "new_nonce": new_nonce,
            }
        )

    if semantic_projection(original) != semantic_projection(repaired):
        raise ValueError(f"{repaired.get('asset_id')}: unauthorized semantic payload change")
    repaired["asset_sha256"] = asset_module.compute_research_component_evaluation_asset_sha256(repaired)
    return repaired, edits


def replace_exact_identity(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected one identity occurrence, got {count}")
    return text.replace(old, new, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit-bundle", required=True)
    args = parser.parse_args()

    decision_text = DECISION.read_text(encoding="utf-8")
    present = {line.strip() for line in decision_text.splitlines()}
    missing = sorted(REQUIRED_DECISION_LINES - present)
    if missing:
        raise SystemExit("Missing canonical nonce-repair authority: " + "; ".join(missing))

    asset_code = ASSET_CODE_PATH.read_text(encoding="utf-8")
    if asset_code.count(OLD_CLINICAL_VALIDATOR) != 1:
        raise SystemExit("Expected exact pre-repair clinical validator implementation not found")
    repaired_asset_code = asset_code.replace(OLD_CLINICAL_VALIDATOR, NEW_CLINICAL_VALIDATOR, 1)

    # Exercise the exact proposed validator semantics in this construction run.
    def bounded_clinical_content(value: str) -> bool:
        lowered = value.lower().replace("non-clinical", "")
        return any(marker in lowered for marker in asset_module._FORBIDDEN_CLINICAL_SUBSTRINGS)

    asset_module._contains_clinical_content = bounded_clinical_content
    if asset_module._contains_clinical_content("non-clinical research object"):
        raise SystemExit("Bounded validator must allow exact non-clinical descriptor")
    if not asset_module._contains_clinical_content("clinical research object"):
        raise SystemExit("Bounded validator must still reject positive clinical descriptor")
    if not asset_module._contains_clinical_content("patient diagnosis"):
        raise SystemExit("Bounded validator must preserve other clinical markers")

    original_set = load_json(ASSET_SET_PATH)
    repaired_set = copy.deepcopy(original_set)
    assets = repaired_set.get("asset_records")
    if not isinstance(assets, list) or len(assets) != 7:
        raise SystemExit("Exact seven-asset subject required")

    old_hashes: dict[str, str] = {}
    new_hashes: dict[str, str] = {}
    repaired_assets: list[dict[str, Any]] = []
    edits: list[dict[str, Any]] = []
    for asset in assets:
        if not isinstance(asset, dict):
            raise SystemExit("Every asset must be an object")
        asset_id = str(asset.get("asset_id"))
        old_hashes[asset_id] = str(asset.get("asset_sha256"))
        repaired, asset_edits = repair_asset(asset)
        repaired_assets.append(repaired)
        edits.extend(asset_edits)
        new_hashes[asset_id] = str(repaired["asset_sha256"])
    if len(edits) != 80:
        raise SystemExit(f"Exact 80 nonce records required, got {len(edits)}")

    repaired_set["asset_records"] = repaired_assets
    old_set_sha = str(original_set.get("asset_set_sha256"))
    repaired_set["asset_set_sha256"] = asset_module.compute_research_component_evaluation_asset_set_sha256(repaired_set)
    new_set_sha = str(repaired_set["asset_set_sha256"])

    lineage = load_json(LINEAGE_PATH)
    admissions = [asset_module.evaluate_research_component_asset_admission(asset, lineage) for asset in repaired_assets]
    if any(result.get("state") != "ELIGIBLE" for result in admissions):
        diagnostics = [
            {
                "asset_id": repaired_assets[index]["asset_id"],
                "admission": result,
                "asset_errors": asset_module.validate_research_component_evaluation_asset(repaired_assets[index]),
            }
            for index, result in enumerate(admissions)
        ]
        raise SystemExit(f"Repaired Spec003 admission failed closed: {diagnostics}")

    provenance = load_json(PROVENANCE_PATH)
    old_provenance_sha = str(provenance.get("instrument_sha256"))
    provenance["asset_set_sha256"] = new_set_sha
    provenance["instrument_sha256"] = self_hash(provenance, "instrument_sha256")
    new_provenance_sha = str(provenance["instrument_sha256"])

    source = load_json(SOURCE_PATH)
    old_source_sha = str(source.get("instrument_sha256"))
    source["asset_set_sha256"] = new_set_sha
    source["provenance_instrument_sha256"] = new_provenance_sha
    source["instrument_sha256"] = self_hash(source, "instrument_sha256")
    new_source_sha = str(source["instrument_sha256"])

    privacy = load_json(PRIVACY_PATH)
    old_privacy_sha = str(privacy.get("instrument_sha256"))
    privacy["asset_set_sha256"] = new_set_sha
    privacy["instrument_sha256"] = self_hash(privacy, "instrument_sha256")
    new_privacy_sha = str(privacy["instrument_sha256"])

    protocol = load_json(PROTOCOL_PATH)
    old_protocol_sha = str(protocol.get("protocol_sha256"))
    protocol["evaluation_asset_manifests"] = [asset_module.build_protocol_asset_manifest(asset) for asset in repaired_assets]
    protocol["protocol_sha256"] = compute_research_component_tournament_protocol_sha256(protocol)
    new_protocol_sha = str(protocol["protocol_sha256"])

    evidence_code = ASSET_EVIDENCE_CODE_PATH.read_text(encoding="utf-8")
    evidence_code = replace_exact_identity(evidence_code, old_set_sha, new_set_sha, "ASSET_SET_SHA256")
    evidence_code = replace_exact_identity(evidence_code, old_provenance_sha, new_provenance_sha, "PROVENANCE_INSTRUMENT_SHA256")
    evidence_code = replace_exact_identity(evidence_code, old_source_sha, new_source_sha, "SOURCE_VERIFICATION_INSTRUMENT_SHA256")

    qualification_code = QUALIFICATION_CODE_PATH.read_text(encoding="utf-8")
    qualification_code = replace_exact_identity(qualification_code, old_privacy_sha, new_privacy_sha, "PRIVACY_INSTRUMENT_SHA256")

    asset_tests = ASSET_TEST_PATH.read_text(encoding="utf-8")
    insertion_point = "    def test_protocol_manifest_drift_fails_closed(self):\n"
    regression = '''    def test_non_clinical_descriptor_does_not_trigger_positive_clinical_marker(self):\n        english = next(\n            asset\n            for asset in ASSET_SET["asset_records"]\n            if asset["metric_family"] == "GENERAL_ENGLISH_LANGUAGE"\n        )\n        self.assertEqual(validate_research_component_evaluation_asset(english), [])\n        bad = copy.deepcopy(english)\n        bad["cases"][0]["prompt"] = bad["cases"][0]["prompt"].replace(\n            "non-clinical", "clinical", 1\n        )\n        bad["asset_sha256"] = compute_research_component_evaluation_asset_sha256(bad)\n        errors = validate_research_component_evaluation_asset(bad)\n        self.assertTrue(any("clinical content is prohibited" in e for e in errors))\n\n'''
    if asset_tests.count(insertion_point) != 1:
        raise SystemExit("Expected asset-test insertion point not found")
    repaired_asset_tests = asset_tests.replace(insertion_point, regression + insertion_point, 1)

    permanent_evidence = {
        "schema_version": "1",
        "evidence_id": "E004_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_EVIDENCE_V1",
        "founder_decision_token": DECISION_TOKEN,
        "repair_formula": 'SHA256(f"{fixture_namespace_seed}|{metric_family}|{index}")[:16]',
        "repair_indexing": "ONE_BASED_DECIMAL_UNPADDED",
        "repair_embedding_rule": "FIRST_EXACT_FULL_NONCE_OCCURRENCE_ONLY",
        "validator_repair": "ALLOW_EXACT_NON_CLINICAL_NEGATIVE_DESCRIPTOR_ONLY",
        "fixture_namespace_seed": asset_module.ASSET_NAMESPACE_SEED,
        "nonce_record_count": len(edits),
        "semantic_payload_change": False,
        "semantic_projection_proof": "PASS",
        "caller_controlled_eligible_state": False,
        "original_asset_set_sha256": old_set_sha,
        "repaired_asset_set_sha256": new_set_sha,
        "asset_hash_rebindings": [
            {"asset_id": asset_id, "old_asset_sha256": old_hashes[asset_id], "new_asset_sha256": new_hashes[asset_id]}
            for asset_id in old_hashes
        ],
        "provenance_sha256_rebinding": {"old": old_provenance_sha, "new": new_provenance_sha},
        "source_verification_sha256_rebinding": {"old": old_source_sha, "new": new_source_sha},
        "privacy_sha256_rebinding": {"old": old_privacy_sha, "new": new_privacy_sha},
        "protocol_sha256_rebinding": {"old": old_protocol_sha, "new": new_protocol_sha},
        "spec003_admissions": [
            {"asset_id": repaired_assets[index]["asset_id"], "state": result.get("state"), "reason_codes": result.get("reason_codes", [])}
            for index, result in enumerate(admissions)
        ],
        "model_execution_performed": False,
        "tournament_execution_performed": False,
        "winner_selected": False,
        "training_performed": False,
        "private_gold_accessed": False,
        "phi_accessed": False,
        "authorized_spend_usd": 0,
        "nonce_edits": edits,
    }

    files = {
        ASSET_SET_PATH.relative_to(ROOT).as_posix(): dump_json(repaired_set),
        PROVENANCE_PATH.relative_to(ROOT).as_posix(): dump_json(provenance),
        SOURCE_PATH.relative_to(ROOT).as_posix(): dump_json(source),
        PRIVACY_PATH.relative_to(ROOT).as_posix(): dump_json(privacy),
        PROTOCOL_PATH.relative_to(ROOT).as_posix(): dump_json(protocol),
        ASSET_CODE_PATH.relative_to(ROOT).as_posix(): repaired_asset_code,
        ASSET_EVIDENCE_CODE_PATH.relative_to(ROOT).as_posix(): evidence_code,
        QUALIFICATION_CODE_PATH.relative_to(ROOT).as_posix(): qualification_code,
        ASSET_TEST_PATH.relative_to(ROOT).as_posix(): repaired_asset_tests,
        "specs/007-sft-v1/e004-research-component-evaluation-nonce-repair-evidence-v1.json": dump_json(permanent_evidence),
    }
    bundle = {
        "schema_version": "1",
        "result": "PASS",
        "founder_decision_token": DECISION_TOKEN,
        "semantic_projection_proof": "PASS",
        "validator_repair_proof": "PASS",
        "nonce_record_count": len(edits),
        "all_spec003_admissions_eligible": True,
        "original_asset_set_sha256": old_set_sha,
        "repaired_asset_set_sha256": new_set_sha,
        "old_protocol_sha256": old_protocol_sha,
        "new_protocol_sha256": new_protocol_sha,
        "files": files,
    }
    Path(args.emit_bundle).write_text(dump_json(bundle), encoding="utf-8")

    print(f"NONCE_RECORD_COUNT={len(edits)}")
    print("REPAIR_EMBEDDING_RULE=FIRST_EXACT_FULL_NONCE_OCCURRENCE_ONLY")
    print("SEMANTIC_PROJECTION_PROOF=PASS")
    print("VALIDATOR_REPAIR_PROOF=PASS")
    print(f"ORIGINAL_ASSET_SET_SHA256={old_set_sha}")
    print(f"REPAIRED_ASSET_SET_SHA256={new_set_sha}")
    for asset_id in old_hashes:
        print(f"ASSET_HASH_REBINDING={asset_id}|old={old_hashes[asset_id]}|new={new_hashes[asset_id]}")
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
