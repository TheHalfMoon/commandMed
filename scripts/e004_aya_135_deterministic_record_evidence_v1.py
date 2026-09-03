#!/usr/bin/env python3
"""Deterministic local-only record evidence for the exact Aya 135 E004 set.

This program implements AYA_135_LOCAL_DETERMINISTIC_RECORD_EVIDENCE_V1.
It is deliberately fail-closed: it performs no network access, never reads
``user_id``, never invokes an AI/model/provider, never emits raw Aya text, and
writes only exact identities plus categorical record-evidence dispositions.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any, Iterable, Iterator

import pyarrow.parquet as pq

SOURCE_REPOSITORY = "CohereLabs/aya_dataset"
SOURCE_REVISION = "f9ea04583f02a8f86404ff6c58bf75fe637df8a2"
SOURCE_FILE = "data/train-00000-of-00001.parquet"
SOURCE_FILE_SHA256 = "51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06"
SOURCE_FILE_SIZE = 137195800
SOURCE_XET_HASH = "3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082"
FILTER_ID = "AYA_SP007_RO_001_CANDIDATE_FILTER_V1"
SCOPE_ID = "SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1"
EXPECTED_COUNT = 135
EXPECTED_MANIFEST_CANONICAL_SHA256 = (
    "dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99"
)
EXPECTED_RECORD_ID_SET_SHA256 = (
    "d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83"
)
EXPECTED_CONTENT_SET_SHA256 = (
    "ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64"
)
METHOD_ID = "AYA_135_LOCAL_DETERMINISTIC_RECORD_EVIDENCE_V1"
ARTIFACT_ID = "e004-aya-135-deterministic-record-evidence-v1"
DATASET_RIGHTS_EVIDENCE_URI = (
    "https://huggingface.co/datasets/CohereLabs/aya_dataset/blob/"
    f"{SOURCE_REVISION}/README.md"
)

ALLOWED_LANGUAGES = frozenset({"eng", "arb"})
EXPECTED_ANNOTATION_TYPE = "original-annotations"
REQUIRED_SOURCE_COLUMNS = frozenset(
    {"inputs", "targets", "language_code", "annotation_type"}
)
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")

EN_TASKS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("TRANSLATION", re.compile(r"\btranslat(?:e|ion|ing)\b", re.I)),
    ("SUMMARIZATION", re.compile(r"\b(?:summari[sz]e|summary|condense)\b", re.I)),
    (
        "REWRITE_EDIT",
        re.compile(
            r"\b(?:rewrite|rephrase|paraphrase|proofread|grammar|grammatical|"
            r"spelling|copyedit|edit this)\b",
            re.I,
        ),
    ),
    (
        "CREATIVE_OR_COMPOSITION",
        re.compile(
            r"\b(?:write|compose|draft|create)\b.{0,80}\b(?:poem|story|letter|"
            r"email|paragraph|essay|dialogue|dialog|speech|caption|description)\b",
            re.I | re.S,
        ),
    ),
    (
        "LANGUAGE_LEARNING",
        re.compile(
            r"\b(?:synonym|antonym|meaning of|define|definition|vocabulary|"
            r"pronunciation|plural of|singular of)\b",
            re.I,
        ),
    ),
    (
        "FORMATTING_ORGANIZATION",
        re.compile(r"\b(?:format|organize|organise|outline|bullet(?:ed)?|list|table)\b", re.I),
    ),
)
AR_TASKS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("TRANSLATION", re.compile(r"(?:ترجم|ترجمة|الترجمة)")),
    ("SUMMARIZATION", re.compile(r"(?:لخ[ّ]?ص|تلخيص|اختصر|ملخص|ملخّص)")),
    (
        "REWRITE_EDIT",
        re.compile(
            r"(?:أعد\s+صياغ|اعد\s+صياغ|إعادة\s+صياغ|اعادة\s+صياغ|صحح|تصحيح|"
            r"دقق|تدقيق|إملاء|املاء|نحو)"
        ),
    ),
    (
        "CREATIVE_OR_COMPOSITION",
        re.compile(
            r"(?:اكتب|أكتب|أنشئ|انشئ|صغ).{0,80}(?:قصيدة|قصة|رسالة|بريد|فقرة|"
            r"مقال|حوار|خطاب|وصف)",
            re.S,
        ),
    ),
    (
        "LANGUAGE_LEARNING",
        re.compile(r"(?:مرادف|مرادفات|ضد|أضداد|اضداد|معنى|تعريف|مفردات|نطق|جمع|مفرد)"),
    ),
    (
        "FORMATTING_ORGANIZATION",
        re.compile(r"(?:نسق|تنسيق|نظم|تنظيم|مخطط|قائمة|جدول|نقاط)"),
    ),
)

CLINICAL_EN = re.compile(
    r"\b(?:health|healthcare|medical|medicine|clinical|patient|caregiver|doctor|"
    r"physician|nurse|pharmacist|hospital|clinic|diagnos(?:is|e|ed|ing)|symptom|"
    r"disease|disorder|syndrome|treat(?:ment|ing)|therapy|medication|drug|dosage|"
    r"dose|prescription|surgery|surgical|emergency|triage|allerg(?:y|ic)|"
    r"drug interaction|infection|infectious|vaccine|vaccination|blood|cancer|"
    r"tumou?r|diabetes|insulin|pregnan(?:cy|t)|pediatric|paediatric|laboratory|"
    r"lab result|kidney|renal|liver|hepatic|heart|cardiac|stroke|seizure|"
    r"depression|anxiety|mental health|psychiatr(?:y|ic)|psychosis|fever|cough|"
    r"pain|antibiotic|virus|bacteria|blood pressure|cholesterol|asthma|fracture|"
    r"wound|injury|dental|dentist)\b",
    re.I,
)
CLINICAL_AR = re.compile(
    r"(?:الصحة|صحي(?:ة)?|طبي(?:ة)?|الطب|سريري|مريض|مرض|طبيب|ممرضة|صيدلي|"
    r"مستشفى|عيادة|تشخيص|أعراض|اعراض|علاج|دواء|أدوية|ادوية|جرعة|وصفة|جراحة|"
    r"طوارئ|حساسية|تفاعل\s*دوائي|عدوى|لقاح|تطعيم|دم|سرطان|ورم|سكري|أنسولين|"
    r"انسولين|حمل|حامل|أطفال|اطفال|مختبر|تحاليل|تحليل\s*دم|كلى|كلية|كبد|"
    r"قلب|سكتة|نوبة|اكتئاب|قلق|نفسي|حمى|ألم|الم|سعال|مضاد\s*حيوي|فيروس|"
    r"بكتيريا|ضغط\s*الدم|كوليسترول|ربو|كسر|جرح|إصابة|اصابة|أسنان|اسنان)"
)

STRONG_PRIVACY_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("EMAIL", re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")),
    ("PHONE", re.compile(r"(?<!\d)(?:\+?\d[\s().-]*){7,15}(?!\d)")),
    ("SSN", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("IP_ADDRESS", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
    ("PAYMENT_CARD", re.compile(r"(?<!\d)(?:\d[ -]?){13,19}(?!\d)")),
    (
        "STREET_ADDRESS_EN",
        re.compile(
            r"(?i)\b\d{1,6}\s+[A-Za-z0-9.'-]+(?:\s+[A-Za-z0-9.'-]+){0,5}\s+"
            r"(?:street|st|road|rd|avenue|ave|boulevard|blvd|lane|ln|drive|dr)\b"
        ),
    ),
    (
        "DIRECT_IDENTITY_EN",
        re.compile(
            r"(?i)\b(?:my name is|my address is|my phone(?: number)? is|"
            r"my email(?: address)? is|i live at)\b"
        ),
    ),
    (
        "DIRECT_IDENTITY_AR",
        re.compile(
            r"(?:اسمي\s+|إسمي\s+|عنواني\s+|رقم\s+هاتفي|بريدي\s+الإلكتروني|"
            r"بريدي\s+الالكتروني)"
        ),
    ),
)

WEAK_PRIVACY_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "IDENTIFIER_LABEL",
        re.compile(
            r"(?i)\b(?:passport|national id|government id|medical record|mrn|"
            r"account number|user id|username)\b"
        ),
    ),
    ("DOB_LABEL", re.compile(r"(?i)\b(?:date of birth|dob|born on)\b")),
    (
        "AR_IDENTIFIER_LABEL",
        re.compile(r"(?:رقم\s+الهوية|هوية\s+وطنية|جواز\s+السفر|رقم\s+الملف|تاريخ\s+الميلاد)"),
    ),
    ("SOCIAL_HANDLE", re.compile(r"(?<!\w)@[A-Za-z0-9_]{2,32}\b")),
    (
        "GEO_COORDINATES",
        re.compile(r"(?<!\d)[+-]?(?:[0-8]?\d(?:\.\d+)?|90(?:\.0+)?)\s*,\s*[+-]?(?:1[0-7]\d(?:\.\d+)?|180(?:\.0+)?|\d?\d(?:\.\d+)?)(?!\d)"),
    ),
    ("DATE_LIKE", re.compile(r"\b(?:19|20)\d{2}[-/]\d{1,2}[-/]\d{1,2}\b")),
)

EXPLICIT_SOURCE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("URL", re.compile(r"(?i)\bhttps?://\S+|\bwww\.\S+")),
    ("DOI", re.compile(r"(?i)\bdoi\s*:\s*10\.\d{4,9}/\S+|\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)),
    ("ISBN", re.compile(r"(?i)\bISBN(?:-1[03])?\s*:?[\s-]*(?:97[89][\s-]*)?\d[\d\s-]{8,16}\b")),
    (
        "COPYRIGHT_NOTICE",
        re.compile(r"(?i)(?:©|copyright|all rights reserved|licensed under|creative commons|CC BY)"),
    ),
    (
        "SOURCE_ATTRIBUTION",
        re.compile(r"(?i)\b(?:source|citation|cited from|according to|written by|author|byline)\s*[:：]"),
    ),
    (
        "COPYRIGHTED_TEXT_MARKER_EN",
        re.compile(
            r"(?i)\b(?:lyrics|song lyrics|book excerpt|article excerpt|excerpt from|"
            r"quoted passage|chapter from|poem by|song by|novel by)\b"
        ),
    ),
    (
        "COPYRIGHTED_TEXT_MARKER_AR",
        re.compile(r"(?:كلمات\s+الأغنية|كلمات\s+اغنية|مقتطف\s+من|اقتباس\s+من|الفصل\s+من|قصيدة\s+لـ|المصدر\s*[:：])"),
    ),
    ("MARKDOWN_BLOCKQUOTE", re.compile(r"(?m)^\s*>\s+\S")),
)

AMBIGUOUS_SOURCE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "GENERIC_PASSAGE_MARKER_EN",
        re.compile(r"(?i)\b(?:the following passage|this passage|the text below|the following text|provided text|source text)\b"),
    ),
    (
        "GENERIC_PASSAGE_MARKER_AR",
        re.compile(r"(?:النص\s+التالي|المقطع\s+التالي|النص\s+أدناه|النص\s+المرفق|المصدر\s+النصي)"),
    ),
    ("LONG_QUOTE_DELIMITER", re.compile(r"(?:\"[^\"]{240,}\"|“[^”]{240,}”|«[^»]{240,}»)", re.S)),
)

TRANSFORMATION_TASKS = frozenset(
    {"TRANSLATION", "SUMMARIZATION", "REWRITE_EDIT", "FORMATTING_ORGANIZATION"}
)
NARROW_CLEARABLE_TASKS = frozenset({"CREATIVE_OR_COMPOSITION", "LANGUAGE_LEARNING"})


def canonical_bytes(value: Any) -> bytes:
    """Serialize using the repository's canonical JSON convention for this evidence path."""
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def sha256_file(path: Path) -> str:
    """Compute a file SHA-256 without loading the file into memory."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def set_root(values: Iterable[str]) -> str:
    """Hash a duplicate-free sorted identity set using the canonical line-root shape."""
    normalized = sorted(values)
    return hashlib.sha256(("\n".join(normalized) + "\n").encode("ascii")).hexdigest()


def normalize_text(value: str | None) -> str:
    """Apply the exact Aya candidate normalization used by the canonical filter."""
    text = unicodedata.normalize("NFC", value or "")
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def classify_task(prompt: str, language_code: str) -> str | None:
    """Recompute the canonical deterministic task family."""
    patterns = EN_TASKS if language_code == "eng" else AR_TASKS if language_code == "arb" else ()
    for task_family, pattern in patterns:
        if pattern.search(prompt):
            return task_family
    return None


def clinical_scope_hit(text: str) -> bool:
    """Return whether the fixed non-clinical scope exclusion matches."""
    return bool(CLINICAL_EN.search(text) or CLINICAL_AR.search(text))


def matched_codes(
    text: str,
    patterns: Iterable[tuple[str, re.Pattern[str]]],
) -> tuple[str, ...]:
    """Return sorted deterministic reason codes for all matching fixed patterns."""
    return tuple(sorted(code for code, pattern in patterns if pattern.search(text)))


def classify_privacy(text: str) -> tuple[str, tuple[str, ...]]:
    """Classify privacy evidence conservatively under the frozen V1 rule set."""
    strong = matched_codes(text, STRONG_PRIVACY_PATTERNS)
    if strong:
        return "RESTRICTED_OR_PHI", tuple(f"PRIVACY_STRONG_{code}" for code in strong)

    weak = matched_codes(text, WEAK_PRIVACY_PATTERNS)
    if weak:
        return "UNRESOLVED", tuple(f"PRIVACY_AMBIGUOUS_{code}" for code in weak)

    return "NO_PHI_KNOWN", ("PRIVACY_NO_FIXED_INDICATOR_OBSERVED",)


def classify_embedded_source_risk(
    text: str,
    task_family: str,
) -> tuple[str, tuple[str, ...]]:
    """Classify embedded/quoted third-party source risk under frozen V1 rules."""
    explicit = matched_codes(text, EXPLICIT_SOURCE_PATTERNS)
    if explicit:
        return (
            "EMBEDDED_SOURCE_RISK_PRESENT",
            tuple(f"SOURCE_EXPLICIT_{code}" for code in explicit),
        )

    ambiguous = matched_codes(text, AMBIGUOUS_SOURCE_PATTERNS)
    if ambiguous:
        return (
            "UNRESOLVED",
            tuple(f"SOURCE_AMBIGUOUS_{code}" for code in ambiguous),
        )

    if task_family in TRANSFORMATION_TASKS:
        return "UNRESOLVED", (f"SOURCE_TRANSFORMATION_TASK_{task_family}",)

    if task_family in NARROW_CLEARABLE_TASKS:
        return "NO_EMBEDDED_SOURCE_RISK_OBSERVED", (
            "SOURCE_NO_FIXED_INDICATOR_OBSERVED",
        )

    return "UNRESOLVED", ("SOURCE_TASK_FAMILY_NOT_CLEARABLE",)


def map_record_level_rights(embedded_source_risk_state: str) -> str:
    """Map bounded source-risk evidence onto the Spec 003 rights state."""
    if embedded_source_risk_state == "NO_EMBEDDED_SOURCE_RISK_OBSERVED":
        return "SUPPORTED"
    return "UNRESOLVED"


def verify_scope(
    prompt: str,
    target: str,
    language_code: str,
    annotation_type: str,
    expected_task_family: str,
) -> tuple[str, tuple[str, ...], str | None]:
    """Recompute SP007-RO-001 scope and fail closed on mismatches or ambiguity."""
    reasons: list[str] = []

    if annotation_type != EXPECTED_ANNOTATION_TYPE:
        reasons.append("SCOPE_ANNOTATION_TYPE_MISMATCH")
    if language_code not in ALLOWED_LANGUAGES:
        reasons.append("SCOPE_LANGUAGE_NOT_ADMITTED")
    if not prompt or not target:
        reasons.append("SCOPE_EMPTY_TEXT")
    if CONTROL_RE.search(prompt) or CONTROL_RE.search(target):
        reasons.append("SCOPE_CONTROL_CHARACTER")

    combined = f"{prompt}\n{target}"
    if clinical_scope_hit(combined):
        reasons.append("SCOPE_CLINICAL_MARKER")

    actual_task_family = classify_task(prompt, language_code)
    if actual_task_family is None:
        if reasons:
            return "FAIL", tuple(sorted(reasons)), None
        return "UNRESOLVED", ("SCOPE_TASK_FAMILY_UNRESOLVED",), None

    if actual_task_family != expected_task_family:
        reasons.append("SCOPE_TASK_FAMILY_MISMATCH")

    if reasons:
        return "FAIL", tuple(sorted(reasons)), actual_task_family

    return "PASS", ("SCOPE_FIXED_RULES_PASS",), actual_task_family


def load_manifest(path: Path) -> dict[str, Any]:
    """Load and validate the exact canonical candidate manifest."""
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if hashlib.sha256(canonical_bytes(manifest)).hexdigest() != EXPECTED_MANIFEST_CANONICAL_SHA256:
        raise SystemExit("CANDIDATE_MANIFEST_IDENTITY_MISMATCH")

    if manifest.get("candidate_count") != EXPECTED_COUNT:
        raise SystemExit("CANDIDATE_COUNT_MISMATCH")
    if manifest.get("filter_id") != FILTER_ID:
        raise SystemExit("FILTER_ID_MISMATCH")
    if manifest.get("scope_id") != SCOPE_ID:
        raise SystemExit("SCOPE_ID_MISMATCH")
    if manifest.get("source_repository") != SOURCE_REPOSITORY:
        raise SystemExit("SOURCE_REPOSITORY_MISMATCH")
    if manifest.get("source_revision") != SOURCE_REVISION:
        raise SystemExit("SOURCE_REVISION_MISMATCH")
    if manifest.get("source_file") != SOURCE_FILE:
        raise SystemExit("SOURCE_FILE_MISMATCH")
    if manifest.get("source_file_sha256") != SOURCE_FILE_SHA256:
        raise SystemExit("SOURCE_SHA256_MISMATCH")
    if manifest.get("source_file_xet_hash") != SOURCE_XET_HASH:
        raise SystemExit("SOURCE_XET_HASH_MISMATCH")

    records = manifest.get("records")
    if not isinstance(records, list) or len(records) != EXPECTED_COUNT:
        raise SystemExit("CANDIDATE_RECORDS_SHAPE_MISMATCH")

    record_ids: list[str] = []
    content_ids: list[str] = []
    for record in records:
        if not isinstance(record, dict):
            raise SystemExit("CANDIDATE_RECORD_SHAPE_MISMATCH")
        record_id = record.get("candidate_record_id")
        content_sha = record.get("content_sha256")
        if not isinstance(record_id, str) or not isinstance(content_sha, str):
            raise SystemExit("CANDIDATE_RECORD_IDENTITY_MISSING")
        record_ids.append(record_id)
        content_ids.append(content_sha)

    if len(record_ids) != len(set(record_ids)):
        raise SystemExit("CANDIDATE_RECORD_ID_DUPLICATE")
    if len(content_ids) != len(set(content_ids)):
        raise SystemExit("CANDIDATE_CONTENT_ID_DUPLICATE")
    if set_root(record_ids) != EXPECTED_RECORD_ID_SET_SHA256:
        raise SystemExit("RECORD_ID_SET_MISMATCH")
    if set_root(content_ids) != EXPECTED_CONTENT_SET_SHA256:
        raise SystemExit("CONTENT_SET_MISMATCH")

    return manifest


def candidate_rows(
    parquet_path: Path,
    manifest: dict[str, Any],
) -> Iterator[tuple[dict[str, Any], str, str, str, str]]:
    """Replay exact manifest identities from exact Aya source rows without user_id."""
    if parquet_path.stat().st_size != SOURCE_FILE_SIZE:
        raise SystemExit("AYA_SOURCE_SIZE_MISMATCH")
    if sha256_file(parquet_path) != SOURCE_FILE_SHA256:
        raise SystemExit("AYA_SOURCE_IDENTITY_MISMATCH")

    parquet = pq.ParquetFile(parquet_path)
    available = set(parquet.schema_arrow.names)
    if not REQUIRED_SOURCE_COLUMNS.issubset(available):
        raise SystemExit("AYA_REQUIRED_SCHEMA_MISSING")

    by_id = {str(record["candidate_record_id"]): record for record in manifest["records"]}
    found: set[str] = set()
    source_row_index = 0

    read_columns = ["inputs", "targets", "language_code", "annotation_type"]
    for row_group_index in range(parquet.num_row_groups):
        table = parquet.read_row_group(row_group_index, columns=read_columns)
        for prompt_raw, target_raw, language_code_raw, annotation_type_raw in zip(
            table["inputs"].to_pylist(),
            table["targets"].to_pylist(),
            table["language_code"].to_pylist(),
            table["annotation_type"].to_pylist(),
            strict=True,
        ):
            prompt = normalize_text(prompt_raw)
            target = normalize_text(target_raw)
            language_code = str(language_code_raw)
            annotation_type = str(annotation_type_raw)
            representation = {
                "annotation_type": annotation_type,
                "inputs": prompt,
                "language_code": language_code,
                "targets": target,
            }
            content_sha256 = hashlib.sha256(canonical_bytes(representation)).hexdigest()
            candidate_record_id = hashlib.sha256(
                f"{SOURCE_FILE_SHA256}:{source_row_index}:{content_sha256}".encode("ascii")
            ).hexdigest()
            source_row_index += 1

            expected = by_id.get(candidate_record_id)
            if expected is None:
                continue
            if candidate_record_id in found:
                raise SystemExit("DUPLICATE_CANDIDATE_MATCH")
            if expected.get("content_sha256") != content_sha256:
                raise SystemExit("CONTENT_REPLAY_MISMATCH")
            if expected.get("language_code") != language_code:
                raise SystemExit("LANGUAGE_REPLAY_MISMATCH")

            found.add(candidate_record_id)
            yield expected, prompt, target, language_code, annotation_type

    if len(found) != EXPECTED_COUNT:
        raise SystemExit("CANDIDATE_REPLAY_INCOMPLETE")


def build_evidence(
    parquet_path: Path,
    manifest_path: Path,
) -> dict[str, Any]:
    """Build repository-safe categorical evidence for the exact Aya 135 set."""
    manifest = load_manifest(manifest_path)
    records: list[dict[str, Any]] = []
    privacy_counts: collections.Counter[str] = collections.Counter()
    source_counts: collections.Counter[str] = collections.Counter()
    rights_counts: collections.Counter[str] = collections.Counter()
    scope_counts: collections.Counter[str] = collections.Counter()
    language_counts: collections.Counter[str] = collections.Counter()
    task_counts: collections.Counter[str] = collections.Counter()

    for manifest_record, prompt, target, language_code, annotation_type in candidate_rows(
        parquet_path,
        manifest,
    ):
        expected_task_family = str(manifest_record.get("task_family", ""))
        combined = f"{prompt}\n{target}"

        privacy_state, privacy_reasons = classify_privacy(combined)
        embedded_state, source_reasons = classify_embedded_source_risk(
            combined,
            expected_task_family,
        )
        rights_state = map_record_level_rights(embedded_state)
        scope_state, scope_reasons, recomputed_task_family = verify_scope(
            prompt,
            target,
            language_code,
            annotation_type,
            expected_task_family,
        )

        reasons = tuple(sorted(set(privacy_reasons + source_reasons + scope_reasons)))
        record = {
            "candidate_record_id": str(manifest_record["candidate_record_id"]),
            "content_sha256": str(manifest_record["content_sha256"]),
            "embedded_source_risk_state": embedded_state,
            "language_code": language_code,
            "privacy_state": privacy_state,
            "reason_codes": list(reasons),
            "record_level_rights_state": rights_state,
            "scope_verification": scope_state,
            "task_family": expected_task_family,
        }
        if recomputed_task_family is not None and recomputed_task_family != expected_task_family:
            record["recomputed_task_family_mismatch"] = True

        records.append(record)
        privacy_counts[privacy_state] += 1
        source_counts[embedded_state] += 1
        rights_counts[rights_state] += 1
        scope_counts[scope_state] += 1
        language_counts[language_code] += 1
        task_counts[expected_task_family] += 1

    if len(records) != EXPECTED_COUNT:
        raise SystemExit("OUTPUT_CANDIDATE_COUNT_MISMATCH")
    if set_root(str(record["candidate_record_id"]) for record in records) != EXPECTED_RECORD_ID_SET_SHA256:
        raise SystemExit("OUTPUT_RECORD_ID_SET_MISMATCH")
    if set_root(str(record["content_sha256"]) for record in records) != EXPECTED_CONTENT_SET_SHA256:
        raise SystemExit("OUTPUT_CONTENT_SET_MISMATCH")

    return {
        "artifact_id": ARTIFACT_ID,
        "candidate_count": EXPECTED_COUNT,
        "candidate_manifest_canonical_sha256": EXPECTED_MANIFEST_CANONICAL_SHA256,
        "candidate_record_id_set_sha256": EXPECTED_RECORD_ID_SET_SHA256,
        "candidate_content_sha256_set_sha256": EXPECTED_CONTENT_SET_SHA256,
        "dataset_level_rights_evidence_uri": DATASET_RIGHTS_EVIDENCE_URI,
        "external_ai_or_model_used": False,
        "external_provider_used": False,
        "filter_id": FILTER_ID,
        "language_counts": dict(sorted(language_counts.items())),
        "method_id": METHOD_ID,
        "network_access_performed": False,
        "privacy_state_counts": dict(sorted(privacy_counts.items())),
        "raw_text_persisted": False,
        "record_level_rights_state_counts": dict(sorted(rights_counts.items())),
        "records": records,
        "schema_version": "1",
        "scope_id": SCOPE_ID,
        "scope_verification_counts": dict(sorted(scope_counts.items())),
        "source_file": SOURCE_FILE,
        "source_file_sha256": SOURCE_FILE_SHA256,
        "source_file_xet_hash": SOURCE_XET_HASH,
        "source_repository": SOURCE_REPOSITORY,
        "source_revision": SOURCE_REVISION,
        "source_risk_state_counts": dict(sorted(source_counts.items())),
        "task_family_counts": dict(sorted(task_counts.items())),
        "user_id_read": False,
    }


def main() -> None:
    """CLI entry point for local exact-subject evidence generation."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--aya-parquet", required=True, type=Path)
    parser.add_argument("--candidate-manifest", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    evidence = build_evidence(args.aya_parquet, args.candidate_manifest)
    args.out.write_bytes(canonical_bytes(evidence) + b"\n")

    summary = {
        "candidate_count": evidence["candidate_count"],
        "method_id": METHOD_ID,
        "output_sha256": sha256_file(args.out),
        "privacy_state_counts": evidence["privacy_state_counts"],
        "record_level_rights_state_counts": evidence[
            "record_level_rights_state_counts"
        ],
        "scope_verification_counts": evidence["scope_verification_counts"],
        "source_risk_state_counts": evidence["source_risk_state_counts"],
    }
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
