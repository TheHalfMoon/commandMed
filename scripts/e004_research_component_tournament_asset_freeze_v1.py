#!/usr/bin/env python3
"""Validate the frozen SP007-RO-001 non-clinical tournament subject.

This command reads repository-authored metadata and synthetic non-clinical
fixtures only. It never loads model weights, executes inference, opens devices,
starts training, accesses protected data, or selects a winner.
"""

from __future__ import annotations

import json
from pathlib import Path

from src.commandmed.spec007.research_tournament import (
    compute_research_component_tournament_protocol_sha256,
)
from src.commandmed.spec007.research_tournament_asset_evidence import (
    validate_frozen_research_component_evaluation_package,
)
from src.commandmed.spec007.research_tournament_assets import (
    compute_contamination_method_sha256,
    compute_research_component_evaluation_asset_set_sha256,
    compute_research_component_evaluation_asset_sha256,
    compute_rights_instrument_sha256,
    evaluate_research_component_asset_admission,
)

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "specs" / "007-sft-v1"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    provenance = load_json(
        SPEC / "e004-research-component-evaluation-asset-provenance-instrument-v1.json"
    )
    source_verification = load_json(
        SPEC / "e004-research-component-evaluation-asset-source-verification-v1.json"
    )
    rights = load_json(
        SPEC / "e004-research-component-evaluation-asset-rights-instrument-v1.json"
    )
    contamination = load_json(
        SPEC / "e004-research-component-evaluation-asset-contamination-method-v1.json"
    )
    asset_set = load_json(
        SPEC / "e004-research-component-tournament-evaluation-assets-v1.json"
    )
    protocol = load_json(
        SPEC / "e004-research-component-tournament-protocol-v1.json"
    )
    lineage_contract = load_json(ROOT / "data" / "lineage" / "lineage_contract.json")

    assets = asset_set.get("asset_records", [])
    admissions = [
        evaluate_research_component_asset_admission(asset, lineage_contract)
        for asset in assets
        if isinstance(asset, dict)
    ]
    errors = validate_frozen_research_component_evaluation_package(
        provenance_instrument=provenance,
        source_verification_instrument=source_verification,
        rights_instrument=rights,
        contamination_method=contamination,
        asset_set=asset_set,
        protocol=protocol,
        lineage_contract=lineage_contract,
    )

    mcq_case_count = sum(
        len(asset.get("cases", []))
        for asset in assets
        if isinstance(asset, dict)
        and asset.get("asset_kind") == "MULTIPLE_CHOICE_CONDITIONAL_LIKELIHOOD"
    )
    resource_probe_count = sum(
        len(asset.get("probes", []))
        for asset in assets
        if isinstance(asset, dict)
        and asset.get("asset_kind") == "RESOURCE_MEASUREMENT_PROTOCOL"
    )

    print(f"PROVENANCE_INSTRUMENT_SHA256={provenance.get('instrument_sha256')}")
    print(
        "SOURCE_VERIFICATION_INSTRUMENT_SHA256="
        f"{source_verification.get('instrument_sha256')}"
    )
    print(f"RIGHTS_INSTRUMENT_SHA256={rights.get('instrument_sha256')}")
    print(f"RIGHTS_INSTRUMENT_COMPUTED_SHA256={compute_rights_instrument_sha256(rights)}")
    print(f"CONTAMINATION_METHOD_SHA256={contamination.get('method_sha256')}")
    print(
        "CONTAMINATION_METHOD_COMPUTED_SHA256="
        f"{compute_contamination_method_sha256(contamination)}"
    )
    print(f"ASSET_SET_SHA256={asset_set.get('asset_set_sha256')}")
    print(
        "ASSET_SET_COMPUTED_SHA256="
        f"{compute_research_component_evaluation_asset_set_sha256(asset_set)}"
    )
    for asset in assets:
        if not isinstance(asset, dict):
            continue
        print(
            "ASSET_IDENTITY="
            f"{asset.get('asset_id')}|claimed={asset.get('asset_sha256')}|"
            f"computed={compute_research_component_evaluation_asset_sha256(asset)}"
        )
    print(f"ASSET_COUNT={len(assets) if isinstance(assets, list) else 0}")
    print(f"MCQ_CASE_COUNT={mcq_case_count}")
    print(f"RESOURCE_PROBE_COUNT={resource_probe_count}")
    print(
        "SPEC003_LINEAGE_ELIGIBLE_COUNT="
        f"{sum(1 for result in admissions if result.get('state') == 'ELIGIBLE')}"
    )
    print(f"PROTOCOL_SHA256={protocol.get('protocol_sha256')}")
    print(
        "PROTOCOL_COMPUTED_SHA256="
        f"{compute_research_component_tournament_protocol_sha256(protocol)}"
    )
    print("MODEL_EXECUTION_PERFORMED=NO")
    print("TRAINING_PERFORMED=NO")
    print("WINNER_SELECTED=NO")
    print("CURRENT_AUTHORIZED_SPEND_USD=0")

    if errors:
        for error in errors:
            print(f"ERROR={error}")
        print("RESULT=FAIL")
        return 1

    if len(assets) != 7 or mcq_case_count != 72 or resource_probe_count != 8:
        print("ERROR=Frozen asset cardinality mismatch")
        print("RESULT=FAIL")
        return 1
    if len(admissions) != 7 or any(
        result.get("state") != "ELIGIBLE" for result in admissions
    ):
        print("ERROR=Spec003 lineage admission mismatch")
        print("RESULT=FAIL")
        return 1

    print("RESULT=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
