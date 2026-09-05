"""Evidence-bound qualification tests for the SP007-RO-001 asset freeze."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.spec007.research_tournament_asset_evidence import (
    ASSET_SET_SHA256,
    PROVENANCE_INSTRUMENT_SHA256,
    SOURCE_VERIFICATION_INSTRUMENT_SHA256,
    validate_frozen_research_component_evaluation_package,
    validate_research_component_provenance_instrument,
    validate_research_component_source_verification_instrument,
)

ROOT = Path(__file__).resolve().parents[2]
SPEC = ROOT / "specs" / "007-sft-v1"


def load_json(name: str):
    return json.loads((SPEC / name).read_text(encoding="utf-8"))


PROVENANCE = load_json(
    "e004-research-component-evaluation-asset-provenance-instrument-v1.json"
)
SOURCE_VERIFICATION = load_json(
    "e004-research-component-evaluation-asset-source-verification-v1.json"
)
RIGHTS = load_json(
    "e004-research-component-evaluation-asset-rights-instrument-v1.json"
)
CONTAMINATION = load_json(
    "e004-research-component-evaluation-asset-contamination-method-v1.json"
)
ASSET_SET = load_json(
    "e004-research-component-tournament-evaluation-assets-v1.json"
)
PROTOCOL = load_json("e004-research-component-tournament-protocol-v1.json")
LINEAGE_CONTRACT = json.loads(
    (ROOT / "data" / "lineage" / "lineage_contract.json").read_text(encoding="utf-8")
)


class ResearchComponentEvaluationEvidenceTests(unittest.TestCase):
    def test_provenance_instrument_is_exact(self):
        self.assertEqual(validate_research_component_provenance_instrument(PROVENANCE), [])
        self.assertEqual(PROVENANCE["instrument_sha256"], PROVENANCE_INSTRUMENT_SHA256)
        self.assertEqual(PROVENANCE["asset_set_sha256"], ASSET_SET_SHA256)
        self.assertFalse(PROVENANCE["external_payloads_used"])
        self.assertFalse(PROVENANCE["candidate_outputs_observed_before_freeze"])
        self.assertFalse(PROVENANCE["adaptive_generation_from_candidate_outputs"])

    def test_source_verification_instrument_is_exact(self):
        self.assertEqual(
            validate_research_component_source_verification_instrument(
                SOURCE_VERIFICATION
            ),
            [],
        )
        self.assertEqual(
            SOURCE_VERIFICATION["instrument_sha256"],
            SOURCE_VERIFICATION_INSTRUMENT_SHA256,
        )
        self.assertEqual(SOURCE_VERIFICATION["asset_set_sha256"], ASSET_SET_SHA256)
        self.assertTrue(SOURCE_VERIFICATION["all_asset_self_hashes_required"])
        self.assertTrue(SOURCE_VERIFICATION["all_cases_or_probes_nonce_bound"])
        self.assertFalse(SOURCE_VERIFICATION["private_gold_present"])

    def test_complete_evaluation_package_is_valid(self):
        errors = validate_frozen_research_component_evaluation_package(
            provenance_instrument=PROVENANCE,
            source_verification_instrument=SOURCE_VERIFICATION,
            rights_instrument=RIGHTS,
            contamination_method=CONTAMINATION,
            asset_set=ASSET_SET,
            protocol=PROTOCOL,
            lineage_contract=LINEAGE_CONTRACT,
        )
        self.assertEqual(errors, [])

    def test_provenance_cannot_claim_candidate_output_adaptation(self):
        bad = copy.deepcopy(PROVENANCE)
        bad["candidate_outputs_observed_before_freeze"] = True
        self.assertTrue(validate_research_component_provenance_instrument(bad))

    def test_source_verification_cannot_drop_self_hash_requirement(self):
        bad = copy.deepcopy(SOURCE_VERIFICATION)
        bad["all_asset_self_hashes_required"] = False
        self.assertTrue(
            validate_research_component_source_verification_instrument(bad)
        )

    def test_source_verification_cannot_rebind_asset_set(self):
        bad = copy.deepcopy(SOURCE_VERIFICATION)
        bad["asset_set_sha256"] = "0" * 64
        self.assertTrue(
            validate_research_component_source_verification_instrument(bad)
        )

    def test_complete_package_fails_if_protocol_does_not_bind_frozen_asset_set(self):
        bad = copy.deepcopy(PROTOCOL)
        bad["evaluation_asset_manifests"][0]["content_sha256"] = "0" * 64
        errors = validate_frozen_research_component_evaluation_package(
            provenance_instrument=PROVENANCE,
            source_verification_instrument=SOURCE_VERIFICATION,
            rights_instrument=RIGHTS,
            contamination_method=CONTAMINATION,
            asset_set=ASSET_SET,
            protocol=bad,
            lineage_contract=LINEAGE_CONTRACT,
        )
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
