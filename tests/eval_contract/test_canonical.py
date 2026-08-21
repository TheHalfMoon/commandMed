"""Tests for deterministic semantic canonical serialization and SHA-256 identity computation."""

import json
from pathlib import Path
import unittest

from src.commandmed.eval_contract.canonical import (
    canonical_json_dumps,
    compute_canonical_sha256,
    compute_file_canonical_sha256,
)


class TestCanonicalSerialization(unittest.TestCase):
    """Tests for deterministic semantic canonical JSON serialization and SHA-256 digests."""

    def setUp(self) -> None:
        self.data_dir = Path(__file__).resolve().parents[2] / "data" / "eval"

    def test_key_ordering_independence(self) -> None:
        """FR-008 / NFR-001: Equivalent objects with different key insertion orders produce identical canonical output and SHA-256."""
        obj_a = {
            "zebra": 1,
            "apple": {"beta": 2, "alpha": 1},
            "charlie": [3, 2, 1],
        }
        obj_b = {
            "apple": {"alpha": 1, "beta": 2},
            "charlie": [3, 2, 1],
            "zebra": 1,
        }

        canonical_a = canonical_json_dumps(obj_a)
        canonical_b = canonical_json_dumps(obj_b)

        self.assertEqual(canonical_a, canonical_b)
        self.assertEqual(compute_canonical_sha256(obj_a), compute_canonical_sha256(obj_b))

    def test_set_like_field_reordering_semantic_invariance(self) -> None:
        """Finding 6: Reordering set-like list fields (roles, modalities, languages) produces the same semantic digest."""
        benchmark_a = {
            "benchmark_id": "test_bench",
            "roles": ["PATIENT_CAREGIVER", "CLINICAL_PROFESSIONAL"],
            "modalities": ["TEXT", "MULTIMODAL"],
            "languages": ["en", "ar"],
        }
        benchmark_b = {
            "benchmark_id": "test_bench",
            "roles": ["CLINICAL_PROFESSIONAL", "PATIENT_CAREGIVER"],
            "modalities": ["MULTIMODAL", "TEXT"],
            "languages": ["ar", "en"],
        }

        self.assertEqual(canonical_json_dumps(benchmark_a), canonical_json_dumps(benchmark_b))
        self.assertEqual(compute_canonical_sha256(benchmark_a), compute_canonical_sha256(benchmark_b))

    def test_registry_records_reordering_semantic_invariance(self) -> None:
        """Finding 6: Reordering benchmark records in registry produces the same semantic digest."""
        registry_a = [
            {"benchmark_id": "medqa", "canonical_name": "MedQA"},
            {"benchmark_id": "healthbench", "canonical_name": "HealthBench"},
            {"benchmark_id": "pubmedqa", "canonical_name": "PubMedQA"},
        ]
        registry_b = [
            {"benchmark_id": "pubmedqa", "canonical_name": "PubMedQA"},
            {"benchmark_id": "medqa", "canonical_name": "MedQA"},
            {"benchmark_id": "healthbench", "canonical_name": "HealthBench"},
        ]

        self.assertEqual(canonical_json_dumps(registry_a), canonical_json_dumps(registry_b))
        self.assertEqual(compute_canonical_sha256(registry_a), compute_canonical_sha256(registry_b))

    def test_semantic_mutation_changes_digest(self) -> None:
        """FR-008: Any semantic mutation to data changes the SHA-256 digest."""
        base_obj = {"benchmark_id": "medqa", "version": "1.0"}
        mutated_obj = {"benchmark_id": "medqa", "version": "1.1"}

        hash_base = compute_canonical_sha256(base_obj)
        hash_mutated = compute_canonical_sha256(mutated_obj)

        self.assertNotEqual(hash_base, hash_mutated)

    def test_file_canonical_hashes_are_reproducible(self) -> None:
        """Ensure all canonical data/eval files produce valid reproducible SHA-256 digests."""
        for filename in ["benchmarks.json", "metrics.json", "gold_protocols.json", "quarantine.json"]:
            file_path = self.data_dir / filename
            self.assertTrue(file_path.is_file(), f"{filename} missing")

            digest1 = compute_file_canonical_sha256(file_path)
            digest2 = compute_file_canonical_sha256(file_path)

            self.assertEqual(digest1, digest2)
            self.assertEqual(len(digest1), 64)
            int(digest1, 16)


if __name__ == "__main__":
    unittest.main()
