"""I001-I002 RED tests for the Spec 007 deterministic foundation."""

from __future__ import annotations

import hashlib
import unittest

from src.commandmed.eval_contract.canonical import canonical_json_dumps as repository_canonical_json_dumps
from src.commandmed.spec007 import ROLE_CLASSES, canonical_json_dumps, compute_canonical_sha256


class TestCanonicalReuse(unittest.TestCase):
    def test_spec007_reuses_repository_canonical_serializer(self):
        self.assertIs(canonical_json_dumps, repository_canonical_json_dumps)

    def test_canonical_serialization_is_deterministic(self):
        left = {"roles": ["PATIENT_CAREGIVER", "CLINICAL_PROFESSIONAL"], "meta": {"b": 2, "a": 1}}
        right = {"meta": {"a": 1, "b": 2}, "roles": ["CLINICAL_PROFESSIONAL", "PATIENT_CAREGIVER"]}
        self.assertEqual(canonical_json_dumps(left), canonical_json_dumps(right))

    def test_canonical_sha256_is_identity_of_canonical_utf8(self):
        record = {"b": 2, "a": "hello"}
        canonical = canonical_json_dumps(record)
        expected = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        self.assertEqual(expected, compute_canonical_sha256(record))


class TestFrozenVocabulary(unittest.TestCase):
    def test_three_role_vocabulary_is_exact(self):
        self.assertEqual(
            frozenset({"PATIENT_CAREGIVER", "CLINICAL_PROFESSIONAL", "LEARNER_RESEARCHER"}),
            ROLE_CLASSES,
        )


if __name__ == "__main__":
    unittest.main()
