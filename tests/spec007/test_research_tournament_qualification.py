"""Post-Decision-B qualification tests for SP007-RO-001 evaluation assets."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.spec007.research_tournament_qualification import (
    FOUNDER_DECISION_TOKEN,
    PRIVACY_INSTRUMENT_SHA256,
    validate_founder_eval_qualification_decision,
    validate_qualified_research_component_evaluation_package,
    validate_research_component_fixture_privacy,
    validate_research_component_privacy_instrument,
)

ROOT = Path(__file__).resolve().parents[2]
SPEC = ROOT / "specs" / "007-sft-v1"


def load_json(name: str):
    return json.loads((SPEC / name).read_text(encoding="utf-8"))


DECISION_TEXT = (
    SPEC
    / "e004-research-component-evaluation-qualification-founder-decision-2026-09-05.md"
).read_text(encoding="utf-8")
PRIVACY = load_json("e004-research-component-evaluation-asset-privacy-classification-v1.json")
PROVENANCE = load_json("e004-research-component-evaluation-asset-provenance-instrument-v1.json")
SOURCE_VERIFICATION = load_json(
    "e004-research-component-evaluation-asset-source-verification-v1.json"
)
RIGHTS = load_json("e004-research-component-evaluation-asset-rights-instrument-v1.json")
CONTAMINATION = load_json(
    "e004-research-component-evaluation-asset-contamination-method-v1.json"
)
ASSET_SET = load_json("e004-research-component-tournament-evaluation-assets-v1.json")
PROTOCOL = load_json("e004-research-component-tournament-protocol-v1.json")
LINEAGE_CONTRACT = json.loads(
    (ROOT / "data" / "lineage" / "lineage_contract.json").read_text(encoding="utf-8")
)


class ResearchComponentTournamentQualificationTests(unittest.TestCase):
    def test_exact_founder_decision_is_bound(self):
        self.assertIn(FOUNDER_DECISION_TOKEN, DECISION_TEXT)
        self.assertEqual(validate_founder_eval_qualification_decision(DECISION_TEXT), [])

    def test_privacy_instrument_is_exact_and_narrow(self):
        self.assertEqual(validate_research_component_privacy_instrument(PRIVACY), [])
        self.assertEqual(PRIVACY["instrument_sha256"], PRIVACY_INSTRUMENT_SHA256)
        self.assertFalse(PRIVACY["external_provider_used"])
        self.assertFalse(PRIVACY["general_phi_detection_claim"])
        self.assertFalse(PRIVACY["semantic_reidentification_risk_claim"])

    def test_exact_fixture_privacy_scan_passes(self):
        self.assertEqual(validate_research_component_fixture_privacy(ASSET_SET), [])

    def test_complete_post_decision_package_is_valid(self):
        errors = validate_qualified_research_component_evaluation_package(
            founder_decision_text=DECISION_TEXT,
            privacy_instrument=PRIVACY,
            provenance_instrument=PROVENANCE,
            source_verification_instrument=SOURCE_VERIFICATION,
            rights_instrument=RIGHTS,
            contamination_method=CONTAMINATION,
            asset_set=ASSET_SET,
            protocol=PROTOCOL,
            lineage_contract=LINEAGE_CONTRACT,
        )
        self.assertEqual(errors, [])

    def test_generic_approval_cannot_replace_exact_decision(self):
        self.assertTrue(
            validate_founder_eval_qualification_decision(
                "go ahead, follow the plan in repo, do not stop"
            )
        )

    def test_decision_missing_one_authority_line_fails(self):
        bad = DECISION_TEXT.replace(
            "RESEARCH_COMPONENT_EVAL_CONTAMINATION_ASSESSMENT_AUTHORITY="
            "AUTHORIZED_EXACT_DECLARED_SET_NONEXPOSURE_METHOD_ONLY",
            "",
        )
        self.assertTrue(validate_founder_eval_qualification_decision(bad))

    def test_privacy_instrument_cannot_expand_claim(self):
        bad = copy.deepcopy(PRIVACY)
        bad["general_phi_detection_claim"] = True
        self.assertTrue(validate_research_component_privacy_instrument(bad))

    def test_privacy_instrument_cannot_use_external_provider(self):
        bad = copy.deepcopy(PRIVACY)
        bad["external_provider_used"] = True
        self.assertTrue(validate_research_component_privacy_instrument(bad))

    def test_fixture_scan_rejects_direct_identifier_field(self):
        bad = copy.deepcopy(ASSET_SET)
        bad["asset_records"][0]["user_id"] = "synthetic-user"
        errors = validate_research_component_fixture_privacy(bad)
        self.assertTrue(any("direct-identifier field" in error for error in errors))

    def test_fixture_scan_rejects_email_like_value(self):
        bad = copy.deepcopy(ASSET_SET)
        bad["asset_records"][0]["cases"][0]["prompt"] += " test@example.com"
        errors = validate_research_component_fixture_privacy(bad)
        self.assertTrue(any("email-like" in error for error in errors))

    def test_complete_package_fails_without_decision(self):
        errors = validate_qualified_research_component_evaluation_package(
            founder_decision_text="",
            privacy_instrument=PRIVACY,
            provenance_instrument=PROVENANCE,
            source_verification_instrument=SOURCE_VERIFICATION,
            rights_instrument=RIGHTS,
            contamination_method=CONTAMINATION,
            asset_set=ASSET_SET,
            protocol=PROTOCOL,
            lineage_contract=LINEAGE_CONTRACT,
        )
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
