"""Synthetic tests for the SP007-RO-001 non-clinical tournament contracts.

The fixtures below are metadata-only and are not real evaluation assets, model
results, scientific thresholds, or execution evidence.
"""

from __future__ import annotations

import copy
import unittest

from src.commandmed.spec007.research_scope import (
    RESEARCH_COMPONENT_CLAIM_CLASS,
    RESEARCH_COMPONENT_REQUIRED_GUARDS,
    RESEARCH_COMPONENT_SCOPE_ID,
)
from src.commandmed.spec007.research_tournament import (
    ALLOWED_RANKING_METRIC_FAMILIES,
    CANONICAL_GUARD_FIXTURE_SHA256,
    CONTROL_CANDIDATE,
    PRIMARY_CANDIDATES,
    RESEARCH_COMPONENT_EXECUTION_AUTHORITY_ID,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
    RESEARCH_COMPONENT_TOURNAMENT_PURPOSE,
    SENTINEL_FIXTURE_SET_SHA256,
    SENTINEL_FIXTURE_SHA256_SET_SHA256,
    compute_research_component_tournament_evidence_pack_sha256,
    compute_research_component_tournament_protocol_sha256,
    validate_research_component_tournament_evidence_pack,
    validate_research_component_tournament_protocol,
)


def make_candidate_bindings():
    records = [
        {
            "candidate_id": candidate_id,
            "upstream_revision": revision,
            "candidate_role": "PRIMARY",
            "winner_eligible": True,
            "purpose": "BACKBONE_CANDIDATE",
        }
        for candidate_id, revision in PRIMARY_CANDIDATES
    ]
    records.append(
        {
            "candidate_id": CONTROL_CANDIDATE[0],
            "upstream_revision": CONTROL_CANDIDATE[1],
            "candidate_role": "CONTROL",
            "winner_eligible": False,
            "purpose": "SCALE_QUALITY_OPPORTUNITY_COST",
        }
    )
    return records


def make_assets():
    return [
        {
            "asset_id": f"ASSET-{index:02d}",
            "metric_family": family,
            "source_class": "REPOSITORY_FROZEN_NONCLINICAL",
            "source_authority_id": f"AUTH-{index:02d}",
            "source_license_id": f"LICENSE-{index:02d}",
            "license_validation_status": "PASS",
            "content_sha256": f"{index + 1:x}" * 64,
            "split_id": f"SELECTION-DEV-{index:02d}",
            "provenance_validation_status": "PASS",
            "source_verification_status": "PASS",
            "contamination_status": "PASS",
            "quarantine_can_select_model": True,
            "purpose": "COMPONENT_TOURNAMENT_SELECTION",
        }
        for index, family in enumerate(sorted(ALLOWED_RANKING_METRIC_FAMILIES))
    ]


def make_protocol():
    protocol = {
        "schema_version": "1",
        "protocol_id": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
        "protocol_sha256": None,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "claim_class": RESEARCH_COMPONENT_CLAIM_CLASS,
        "purpose": RESEARCH_COMPONENT_TOURNAMENT_PURPOSE,
        "candidate_bindings": make_candidate_bindings(),
        "ranking_metric_families": sorted(ALLOWED_RANKING_METRIC_FAMILIES),
        "evaluation_asset_manifests": make_assets(),
        "sentinel_fixture_set_sha256": SENTINEL_FIXTURE_SET_SHA256,
        "sentinel_fixture_sha256_set_sha256": SENTINEL_FIXTURE_SHA256_SET_SHA256,
        "sentinel_can_rank": False,
        "private_gold_allowed": False,
        "clinical_metric_ids_allowed": [],
        "candidate_result_visibility_before_freeze": False,
        "winner_selection_performed_by_protocol": False,
        "pre_result_freeze": True,
        "authorized_spend_usd": 0,
    }
    protocol["protocol_sha256"] = compute_research_component_tournament_protocol_sha256(
        protocol
    )
    return protocol


def make_metric_results(protocol):
    return [
        {
            "metric_family": asset["metric_family"],
            "asset_id": asset["asset_id"],
            "value_identity": f"VALUE-{asset['asset_id']}",
            "deterministic_evaluator_id": f"EVAL-{asset['asset_id']}",
        }
        for asset in protocol["evaluation_asset_manifests"]
    ]


def make_evidence_pack(protocol):
    results = []
    for candidate in protocol["candidate_bindings"]:
        results.append(
            {
                "candidate_id": candidate["candidate_id"],
                "upstream_revision": candidate["upstream_revision"],
                "candidate_role": candidate["candidate_role"],
                "metric_results": make_metric_results(protocol),
                "resource_result_ids": [f"RESOURCE-{candidate['candidate_id']}"],
                "qualification_disposition": "PASS",
            }
        )
    guard_results = [
        {
            "guard_id": guard_id,
            "fixture_sha256": CANONICAL_GUARD_FIXTURE_SHA256[guard_id],
            "violation_count": 0,
            "disposition": "PASS",
        }
        for guard_id in sorted(RESEARCH_COMPONENT_REQUIRED_GUARDS)
    ]
    evidence = {
        "schema_version": "1",
        "evidence_pack_id": "SP007-RO-001-TOURNAMENT-EVIDENCE-SYNTHETIC",
        "evidence_pack_sha256": None,
        "protocol_id": protocol["protocol_id"],
        "protocol_sha256": protocol["protocol_sha256"],
        "candidate_results": results,
        "sentinel_guard_results": guard_results,
        "execution_environment_id": "SYNTHETIC-ENVIRONMENT-ONLY",
        "execution_authority_id": RESEARCH_COMPONENT_EXECUTION_AUTHORITY_ID,
        "spend_usd": 0,
        "winner_selected": False,
        "recommendation": "NONE",
    }
    evidence["evidence_pack_sha256"] = (
        compute_research_component_tournament_evidence_pack_sha256(evidence)
    )
    return evidence


def rehash_protocol(protocol):
    protocol["protocol_sha256"] = compute_research_component_tournament_protocol_sha256(
        protocol
    )
    return protocol


def rehash_evidence(evidence):
    evidence["evidence_pack_sha256"] = (
        compute_research_component_tournament_evidence_pack_sha256(evidence)
    )
    return evidence


class ResearchComponentTournamentProtocolTests(unittest.TestCase):
    def test_complete_synthetic_protocol_validates(self):
        self.assertEqual(validate_research_component_tournament_protocol(make_protocol()), [])

    def test_exact_candidate_set_required(self):
        protocol = make_protocol()
        protocol["candidate_bindings"][0]["candidate_id"] = "other/model"
        rehash_protocol(protocol)
        errors = validate_research_component_tournament_protocol(protocol)
        self.assertTrue(any("frozen E001" in error or "primary set" in error for error in errors))

    def test_control_cannot_be_winner_eligible(self):
        protocol = make_protocol()
        protocol["candidate_bindings"][-1]["winner_eligible"] = True
        rehash_protocol(protocol)
        errors = validate_research_component_tournament_protocol(protocol)
        self.assertTrue(any("control must not be winner eligible" in error for error in errors))

    def test_private_gold_source_is_rejected(self):
        protocol = make_protocol()
        protocol["evaluation_asset_manifests"][0]["source_class"] = "PRIVATE_GOLD"
        rehash_protocol(protocol)
        errors = validate_research_component_tournament_protocol(protocol)
        self.assertTrue(any("prohibited for selection" in error for error in errors))

    def test_unknown_source_class_fails_closed(self):
        protocol = make_protocol()
        protocol["evaluation_asset_manifests"][0]["source_class"] = "MYSTERY_SOURCE"
        rehash_protocol(protocol)
        errors = validate_research_component_tournament_protocol(protocol)
        self.assertTrue(any("frozen allowlist" in error for error in errors))

    def test_license_provenance_contamination_and_quarantine_must_pass(self):
        for field, bad_value in (
            ("license_validation_status", "UNKNOWN"),
            ("provenance_validation_status", "UNKNOWN"),
            ("source_verification_status", "UNKNOWN"),
            ("contamination_status", "UNKNOWN"),
            ("quarantine_can_select_model", False),
        ):
            with self.subTest(field=field):
                protocol = make_protocol()
                protocol["evaluation_asset_manifests"][0][field] = bad_value
                rehash_protocol(protocol)
                self.assertTrue(validate_research_component_tournament_protocol(protocol))

    def test_exact_one_asset_per_metric_family_required(self):
        protocol = make_protocol()
        protocol["evaluation_asset_manifests"][1]["metric_family"] = protocol[
            "evaluation_asset_manifests"
        ][0]["metric_family"]
        rehash_protocol(protocol)
        errors = validate_research_component_tournament_protocol(protocol)
        self.assertTrue(any("one-asset-per-ranking-family" in error for error in errors))

    def test_sentinel_identity_is_exactly_bound_and_cannot_rank(self):
        protocol = make_protocol()
        protocol["sentinel_fixture_set_sha256"] = "0" * 64
        protocol["sentinel_can_rank"] = True
        rehash_protocol(protocol)
        errors = validate_research_component_tournament_protocol(protocol)
        self.assertTrue(any("sentinel_fixture_set_sha256 mismatch" in error for error in errors))
        self.assertTrue(any("sentinel_can_rank must be false" in error for error in errors))

    def test_clinical_metric_and_winner_fields_are_closed(self):
        protocol = make_protocol()
        protocol["clinical_metric_ids_allowed"] = ["emergency_miss_rate"]
        protocol["winner_selection_performed_by_protocol"] = True
        rehash_protocol(protocol)
        errors = validate_research_component_tournament_protocol(protocol)
        self.assertTrue(any("clinical_metric_ids_allowed" in error for error in errors))
        self.assertTrue(any("must not select a winner" in error for error in errors))

    def test_pre_result_freeze_and_zero_spend_are_mandatory(self):
        protocol = make_protocol()
        protocol["pre_result_freeze"] = False
        protocol["authorized_spend_usd"] = 1
        rehash_protocol(protocol)
        errors = validate_research_component_tournament_protocol(protocol)
        self.assertTrue(any("pre_result_freeze" in error for error in errors))
        self.assertTrue(any("authorized_spend_usd" in error for error in errors))

    def test_protocol_self_hash_is_enforced(self):
        protocol = make_protocol()
        protocol["protocol_sha256"] = "0" * 64
        errors = validate_research_component_tournament_protocol(protocol)
        self.assertTrue(any("protocol_sha256 mismatch" in error for error in errors))

    def test_malformed_protocol_fails_closed(self):
        for bad in (None, [], "x", 7):
            with self.subTest(value=bad):
                self.assertTrue(validate_research_component_tournament_protocol(bad))


class ResearchComponentTournamentEvidencePackTests(unittest.TestCase):
    def test_complete_synthetic_evidence_pack_validates(self):
        protocol = make_protocol()
        evidence = make_evidence_pack(protocol)
        self.assertEqual(
            validate_research_component_tournament_evidence_pack(evidence, protocol), []
        )

    def test_evidence_pack_cannot_select_or_recommend_winner(self):
        protocol = make_protocol()
        evidence = make_evidence_pack(protocol)
        evidence["winner_selected"] = True
        evidence["recommendation"] = PRIMARY_CANDIDATES[0][0]
        rehash_evidence(evidence)
        errors = validate_research_component_tournament_evidence_pack(evidence, protocol)
        self.assertTrue(any("winner_selected must be false" in error for error in errors))
        self.assertTrue(any("recommendation must equal NONE" in error for error in errors))

    def test_execution_authority_and_zero_spend_are_exact(self):
        protocol = make_protocol()
        evidence = make_evidence_pack(protocol)
        evidence["execution_authority_id"] = "GENERIC_APPROVAL"
        evidence["spend_usd"] = 1
        rehash_evidence(evidence)
        errors = validate_research_component_tournament_evidence_pack(evidence, protocol)
        self.assertTrue(any("execution_authority_id mismatch" in error for error in errors))
        self.assertTrue(any("spend_usd must equal 0" in error for error in errors))

    def test_candidate_result_must_match_frozen_candidate(self):
        protocol = make_protocol()
        evidence = make_evidence_pack(protocol)
        evidence["candidate_results"][0]["upstream_revision"] = "0" * 40
        rehash_evidence(evidence)
        errors = validate_research_component_tournament_evidence_pack(evidence, protocol)
        self.assertTrue(any("outside frozen set" in error for error in errors))

    def test_metric_result_must_bind_protocol_asset(self):
        protocol = make_protocol()
        evidence = make_evidence_pack(protocol)
        evidence["candidate_results"][0]["metric_results"][0]["asset_id"] = "OTHER"
        rehash_evidence(evidence)
        errors = validate_research_component_tournament_evidence_pack(evidence, protocol)
        self.assertTrue(any("asset_id mismatch" in error for error in errors))

    def test_exact_guard_identity_and_fixture_hash_required(self):
        protocol = make_protocol()
        evidence = make_evidence_pack(protocol)
        evidence["sentinel_guard_results"][0]["fixture_sha256"] = "0" * 64
        rehash_evidence(evidence)
        errors = validate_research_component_tournament_evidence_pack(evidence, protocol)
        self.assertTrue(any("fixture_sha256 mismatch" in error for error in errors))

    def test_guard_violation_cannot_be_marked_pass(self):
        protocol = make_protocol()
        evidence = make_evidence_pack(protocol)
        evidence["sentinel_guard_results"][0]["violation_count"] = 1
        evidence["sentinel_guard_results"][0]["disposition"] = "PASS"
        rehash_evidence(evidence)
        errors = validate_research_component_tournament_evidence_pack(evidence, protocol)
        self.assertTrue(any("positive violations require FAIL" in error for error in errors))

    def test_protocol_hash_binding_is_exact(self):
        protocol = make_protocol()
        evidence = make_evidence_pack(protocol)
        evidence["protocol_sha256"] = "0" * 64
        rehash_evidence(evidence)
        errors = validate_research_component_tournament_evidence_pack(evidence, protocol)
        self.assertTrue(any("protocol_sha256 mismatch" in error for error in errors))

    def test_evidence_pack_self_hash_is_enforced(self):
        protocol = make_protocol()
        evidence = make_evidence_pack(protocol)
        evidence["evidence_pack_sha256"] = "0" * 64
        errors = validate_research_component_tournament_evidence_pack(evidence, protocol)
        self.assertTrue(any("evidence_pack_sha256 mismatch" in error for error in errors))

    def test_malformed_evidence_pack_fails_closed(self):
        protocol = make_protocol()
        for bad in (None, [], "x", 7):
            with self.subTest(value=bad):
                self.assertTrue(
                    validate_research_component_tournament_evidence_pack(bad, protocol)
                )


if __name__ == "__main__":
    unittest.main()
