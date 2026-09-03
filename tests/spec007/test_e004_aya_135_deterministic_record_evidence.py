from __future__ import annotations

import importlib.util
import inspect
import sys
import types
import unittest
from pathlib import Path

# The focused classifier tests are intentionally stdlib-only. Real local Aya
# execution uses the separately pinned pyarrow tooling, but importing this script
# for pure synthetic classifier tests must not widen the repository test bootstrap.
try:
    import pyarrow.parquet  # noqa: F401
except ModuleNotFoundError:  # pragma: no cover - depends on local test environment
    pyarrow_stub = types.ModuleType("pyarrow")
    pyarrow_stub.__path__ = []  # type: ignore[attr-defined]
    parquet_stub = types.ModuleType("pyarrow.parquet")
    pyarrow_stub.parquet = parquet_stub  # type: ignore[attr-defined]
    sys.modules["pyarrow"] = pyarrow_stub
    sys.modules["pyarrow.parquet"] = parquet_stub

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/e004_aya_135_deterministic_record_evidence_v1.py"
SPEC = importlib.util.spec_from_file_location(
    "e004_aya_135_deterministic_record_evidence_v1",
    SCRIPT,
)
if SPEC is None or SPEC.loader is None:  # pragma: no cover - import machinery guard
    raise RuntimeError("unable to load deterministic Aya evidence script")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TestAyaDeterministicRecordEvidence(unittest.TestCase):
    """Synthetic-only conformance tests for the frozen Aya record-evidence method."""

    def test_strong_privacy_indicator_is_restricted(self):
        state, reasons = MODULE.classify_privacy(
            "Please send the answer to person@example.com."
        )
        self.assertEqual(state, "RESTRICTED_OR_PHI")
        self.assertIn("PRIVACY_STRONG_EMAIL", reasons)

    def test_weak_privacy_indicator_is_unresolved(self):
        state, reasons = MODULE.classify_privacy(
            "The passport field should be copied into the form."
        )
        self.assertEqual(state, "UNRESOLVED")
        self.assertIn("PRIVACY_AMBIGUOUS_IDENTIFIER_LABEL", reasons)

    def test_no_fixed_privacy_indicator_is_clear_under_method(self):
        state, reasons = MODULE.classify_privacy(
            "Write a short fictional story about a lighthouse."
        )
        self.assertEqual(state, "NO_PHI_KNOWN")
        self.assertEqual(reasons, ("PRIVACY_NO_FIXED_INDICATOR_OBSERVED",))

    def test_explicit_url_is_embedded_source_risk(self):
        state, reasons = MODULE.classify_embedded_source_risk(
            "Summarize the page at https://example.org/article.",
            "SUMMARIZATION",
        )
        self.assertEqual(state, "EMBEDDED_SOURCE_RISK_PRESENT")
        self.assertIn("SOURCE_EXPLICIT_URL", reasons)

    def test_transformation_task_remains_rights_unresolved(self):
        state, reasons = MODULE.classify_embedded_source_risk(
            "Translate the provided sentence into Arabic.",
            "TRANSLATION",
        )
        self.assertEqual(state, "UNRESOLVED")
        self.assertEqual(reasons, ("SOURCE_TRANSFORMATION_TASK_TRANSLATION",))
        self.assertEqual(MODULE.map_record_level_rights(state), "UNRESOLVED")

    def test_narrow_creative_task_can_be_clear_under_method(self):
        state, reasons = MODULE.classify_embedded_source_risk(
            "Write a fictional poem about rain on a quiet street.",
            "CREATIVE_OR_COMPOSITION",
        )
        self.assertEqual(state, "NO_EMBEDDED_SOURCE_RISK_OBSERVED")
        self.assertEqual(reasons, ("SOURCE_NO_FIXED_INDICATOR_OBSERVED",))
        self.assertEqual(MODULE.map_record_level_rights(state), "SUPPORTED")

    def test_scope_pass_requires_exact_recomputed_task_family(self):
        state, reasons, task_family = MODULE.verify_scope(
            "Write a fictional story about a lighthouse.",
            "A lighthouse keeper watched the distant horizon.",
            "eng",
            "original-annotations",
            "CREATIVE_OR_COMPOSITION",
        )
        self.assertEqual(state, "PASS")
        self.assertEqual(task_family, "CREATIVE_OR_COMPOSITION")
        self.assertEqual(reasons, ("SCOPE_FIXED_RULES_PASS",))

    def test_scope_fails_on_clinical_marker(self):
        state, reasons, task_family = MODULE.verify_scope(
            "Write a short paragraph about a patient in a hospital.",
            "This is a synthetic target.",
            "eng",
            "original-annotations",
            "CREATIVE_OR_COMPOSITION",
        )
        self.assertEqual(state, "FAIL")
        self.assertEqual(task_family, "CREATIVE_OR_COMPOSITION")
        self.assertIn("SCOPE_CLINICAL_MARKER", reasons)

    def test_scope_is_unresolved_when_task_family_cannot_be_recomputed(self):
        state, reasons, task_family = MODULE.verify_scope(
            "Consider the color blue.",
            "Blue is a color.",
            "eng",
            "original-annotations",
            "LANGUAGE_LEARNING",
        )
        self.assertEqual(state, "UNRESOLVED")
        self.assertIsNone(task_family)
        self.assertEqual(reasons, ("SCOPE_TASK_FAMILY_UNRESOLVED",))

    def test_scope_fails_on_manifest_task_mismatch(self):
        state, reasons, task_family = MODULE.verify_scope(
            "Translate this sentence into Arabic.",
            "جملة اختبارية.",
            "eng",
            "original-annotations",
            "SUMMARIZATION",
        )
        self.assertEqual(state, "FAIL")
        self.assertEqual(task_family, "TRANSLATION")
        self.assertIn("SCOPE_TASK_FAMILY_MISMATCH", reasons)

    def test_candidate_replay_never_reads_user_id(self):
        source = inspect.getsource(MODULE.candidate_rows)
        self.assertNotIn('"user_id"', source)
        self.assertNotIn("'user_id'", source)

    def test_module_has_no_network_client_imports(self):
        source = SCRIPT.read_text(encoding="utf-8")
        prohibited = (
            "import requests",
            "from requests",
            "import urllib",
            "from urllib",
            "import httpx",
            "from httpx",
            "import socket",
            "from socket",
        )
        for marker in prohibited:
            with self.subTest(marker=marker):
                self.assertNotIn(marker, source)

    def test_output_contract_contains_only_categorical_record_fields(self):
        expected_fields = {
            "candidate_record_id",
            "content_sha256",
            "embedded_source_risk_state",
            "language_code",
            "privacy_state",
            "reason_codes",
            "record_level_rights_state",
            "scope_verification",
            "task_family",
        }
        synthetic_record = {
            "candidate_record_id": "a" * 64,
            "content_sha256": "b" * 64,
            "embedded_source_risk_state": "NO_EMBEDDED_SOURCE_RISK_OBSERVED",
            "language_code": "eng",
            "privacy_state": "NO_PHI_KNOWN",
            "reason_codes": ["SYNTHETIC_FIXTURE"],
            "record_level_rights_state": "SUPPORTED",
            "scope_verification": "PASS",
            "task_family": "CREATIVE_OR_COMPOSITION",
        }
        self.assertEqual(set(synthetic_record), expected_fields)
        self.assertNotIn("inputs", synthetic_record)
        self.assertNotIn("targets", synthetic_record)
        self.assertNotIn("user_id", synthetic_record)


if __name__ == "__main__":
    unittest.main()
