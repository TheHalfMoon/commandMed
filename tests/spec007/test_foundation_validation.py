"""I003-I004 RED tests for strict Spec 007 record parsing and validation."""

from __future__ import annotations

import unittest

from src.commandmed.spec007 import (
    is_canonical_sha256,
    parse_json_object,
    validate_canonical_sha256,
    validate_closed_object,
    validate_role_class,
)


class TestStrictJsonParsing(unittest.TestCase):
    def test_malformed_json_rejected(self):
        parsed, errors = parse_json_object('{"role_class":')
        self.assertIsNone(parsed)
        self.assertEqual(["record: malformed JSON"], errors)

    def test_non_object_json_rejected(self):
        parsed, errors = parse_json_object('["PATIENT_CAREGIVER"]')
        self.assertIsNone(parsed)
        self.assertEqual(["record: expected JSON object"], errors)

    def test_duplicate_object_key_rejected(self):
        parsed, errors = parse_json_object('{"role_class":"PATIENT_CAREGIVER","role_class":"CLINICAL_PROFESSIONAL"}')
        self.assertIsNone(parsed)
        self.assertEqual(["record: duplicate JSON object key 'role_class'"], errors)

    def test_nested_duplicate_object_key_rejected(self):
        parsed, errors = parse_json_object('{"language_profile":{"primary_language":"ar","primary_language":"en"}}')
        self.assertIsNone(parsed)
        self.assertEqual(["record: duplicate JSON object key 'primary_language'"], errors)

    def test_python_object_is_not_implicitly_serialized(self):
        parsed, errors = parse_json_object({"role_class": "PATIENT_CAREGIVER"})
        self.assertIsNone(parsed)
        self.assertEqual(["record: expected JSON text string"], errors)


class TestClosedValidation(unittest.TestCase):
    def test_missing_and_undeclared_fields_are_rejected_deterministically(self):
        errors = validate_closed_object(
            {"role_class": "PATIENT_CAREGIVER", "extra": "not declared"},
            required_fields=("role_class", "content_sha256"),
        )
        self.assertEqual(
            [
                "record: required fields missing ['content_sha256']",
                "record: undeclared fields ['extra']",
            ],
            errors,
        )

    def test_non_object_record_rejected(self):
        self.assertEqual(
            ["record: expected object record"],
            validate_closed_object("not-an-object", required_fields=("role_class",)),
        )

    def test_unknown_role_and_non_string_role_rejected(self):
        self.assertEqual(["role_class: unsupported value 'PHYSICIAN'"], validate_role_class("PHYSICIAN"))
        self.assertEqual(["role_class: expected role-class string"], validate_role_class(1))

    def test_lowercase_sha256_only(self):
        valid = "a" * 64
        self.assertTrue(is_canonical_sha256(valid))
        self.assertEqual([], validate_canonical_sha256(valid, "content_sha256"))
        for invalid in ("A" * 64, "a" * 63, 7, True):
            self.assertFalse(is_canonical_sha256(invalid))
            self.assertEqual(
                ["content_sha256: expected lowercase sha256 hex"],
                validate_canonical_sha256(invalid, "content_sha256"),
            )


if __name__ == "__main__":
    unittest.main()
