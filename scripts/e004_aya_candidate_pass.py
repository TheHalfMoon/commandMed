#!/usr/bin/env python3
"""Build repository-safe, non-admitting Aya candidate hash evidence for E004.

This script is intentionally local-only. It performs no network access, never
reads the Aya ``user_id`` column, never emits record text, and writes only
hashes plus aggregate metadata. It is scoped to the exact canonical Aya byte
subject and SP007-RO-001 research-engineering component.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import unicodedata
from pathlib import Path

import pyarrow.parquet as pq

SOURCE_REPOSITORY = "CohereLabs/aya_dataset"
SOURCE_REVISION = "f9ea04583f02a8f86404ff6c58bf75fe637df8a2"
SOURCE_FILE = "data/train-00000-of-00001.parquet"
SOURCE_FILE_SHA256 = "51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06"
SOURCE_FILE_SIZE = 137195800
SOURCE_XET_HASH = "3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082"
SCOPE_ID = "SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1"
FILTER_ID = "AYA_SP007_RO_001_CANDIDATE_FILTER_V1"
MANIFEST_ID = "e004-aya-sp007-ro-001-candidate-hash-manifest-v1"
EXPECTED_SCHEMA = ["inputs", "targets", "language", "language_code", "annotation_type", "user_id"]
EXPECTED_ANNOTATION_TYPES = {"original-annotations", "re-annotations"}

ADMITTED_LANGS = {
    "eng": ("English", "GENERAL_ENGLISH_LANGUAGE"),
    "arb": ("Standard Arabic", "GENERAL_ARABIC_LANGUAGE_NON_CLINICAL"),
}

EN_TASKS = [
    ("TRANSLATION", re.compile(r"\btranslat(?:e|ion|ing)\b", re.I)),
    ("SUMMARIZATION", re.compile(r"\b(?:summari[sz]e|summary|condense)\b", re.I)),
    ("REWRITE_EDIT", re.compile(r"\b(?:rewrite|rephrase|paraphrase|proofread|grammar|grammatical|spelling|copyedit|edit this)\b", re.I)),
    ("CREATIVE_OR_COMPOSITION", re.compile(r"\b(?:write|compose|draft|create)\b.{0,80}\b(?:poem|story|letter|email|paragraph|essay|dialogue|dialog|speech|caption|description)\b", re.I | re.S)),
    ("LANGUAGE_LEARNING", re.compile(r"\b(?:synonym|antonym|meaning of|define|definition|vocabulary|pronunciation|plural of|singular of)\b", re.I)),
    ("FORMATTING_ORGANIZATION", re.compile(r"\b(?:format|organize|organise|outline|bullet(?:ed)?|list|table)\b", re.I)),
]
AR_TASKS = [
    ("TRANSLATION", re.compile(r"(?:ترجم|ترجمة|الترجمة)")),
    ("SUMMARIZATION", re.compile(r"(?:لخ[ّ]?ص|تلخيص|اختصر|ملخص|ملخّص)")),
    ("REWRITE_EDIT", re.compile(r"(?:أعد\s+صياغ|اعد\s+صياغ|إعادة\s+صياغ|اعادة\s+صياغ|صحح|تصحيح|دقق|تدقيق|إملاء|املاء|نحو)")),
    ("CREATIVE_OR_COMPOSITION", re.compile(r"(?:اكتب|أكتب|أنشئ|انشئ|صغ).{0,80}(?:قصيدة|قصة|رسالة|بريد|فقرة|مقال|حوار|خطاب|وصف)", re.S)),
    ("LANGUAGE_LEARNING", re.compile(r"(?:مرادف|مرادفات|ضد|أضداد|اضداد|معنى|تعريف|مفردات|نطق|جمع|مفرد)")),
    ("FORMATTING_ORGANIZATION", re.compile(r"(?:نسق|تنسيق|نظم|تنظيم|مخطط|قائمة|جدول|نقاط)")),
]

CLINICAL_EN = re.compile(
    r"\b(?:health|healthcare|medical|medicine|clinical|patient|caregiver|doctor|physician|nurse|pharmacist|hospital|clinic|"
    r"diagnos(?:is|e|ed|ing)|symptom|disease|disorder|syndrome|treat(?:ment|ing)|therapy|medication|drug|dosage|dose|prescription|"
    r"surgery|surgical|emergency|triage|allerg(?:y|ic)|drug interaction|infection|infectious|vaccine|vaccination|blood|cancer|tumou?r|"
    r"diabetes|insulin|pregnan(?:cy|t)|pediatric|paediatric|laboratory|lab result|kidney|renal|liver|hepatic|heart|cardiac|stroke|"
    r"seizure|depression|anxiety|mental health|psychiatr(?:y|ic)|psychosis|fever|cough|pain|antibiotic|virus|bacteria|blood pressure|"
    r"cholesterol|asthma|fracture|wound|injury|dental|dentist)\b",
    re.I,
)
CLINICAL_AR = re.compile(
    r"(?:الصحة|صحي(?:ة)?|طبي(?:ة)?|الطب|سريري|مريض|مرض|طبيب|ممرضة|صيدلي|مستشفى|عيادة|تشخيص|أعراض|اعراض|"
    r"علاج|دواء|أدوية|ادوية|جرعة|وصفة|جراحة|طوارئ|حساسية|تفاعل\s*دوائي|عدوى|لقاح|تطعيم|دم|سرطان|ورم|"
    r"سكري|أنسولين|انسولين|حمل|حامل|أطفال|اطفال|مختبر|تحاليل|تحليل\s*دم|كلى|كلية|كبد|قلب|سكتة|نوبة|"
    r"اكتئاب|قلق|نفسي|حمى|ألم|الم|سعال|مضاد\s*حيوي|فيروس|بكتيريا|ضغط\s*الدم|كوليسترول|ربو|كسر|جرح|إصابة|اصابة|أسنان|اسنان)"
)

EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
PHONE_RE = re.compile(r"(?<!\d)(?:\+?\d[\s().-]*){7,15}(?!\d)")
SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
CARD_RE = re.compile(r"(?<!\d)(?:\d[ -]?){13,19}(?!\d)")
ADDRESS_EN = re.compile(r"(?i)\b\d{1,6}\s+[A-Za-z0-9.'-]+(?:\s+[A-Za-z0-9.'-]+){0,5}\s+(?:street|st|road|rd|avenue|ave|boulevard|blvd|lane|ln|drive|dr)\b")
ADDRESS_AR = re.compile(r"(?:عنواني|عنوان\s+المنزل|أسكن\s+في|اسكن\s+في|شارع\s+\S+)")
IDENT_EN = re.compile(r"(?i)\b(?:my name is|my address is|my phone(?: number)? is|my email(?: address)? is|i live at)\b")
IDENT_AR = re.compile(r"(?:اسمي\s+|إسمي\s+|عنواني\s+|رقم\s+هاتفي|بريدي\s+الإلكتروني|بريدي\s+الالكتروني)")
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
PRIVACY_PATTERNS = (EMAIL_RE, PHONE_RE, SSN_RE, IP_RE, CARD_RE, ADDRESS_EN, ADDRESS_AR, IDENT_EN, IDENT_AR)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_text(value: str | None) -> str:
    text = unicodedata.normalize("NFC", value or "")
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def privacy_risk_hit(text: str) -> bool:
    return any(pattern.search(text) for pattern in PRIVACY_PATTERNS)


def clinical_scope_hit(text: str) -> bool:
    return bool(CLINICAL_EN.search(text) or CLINICAL_AR.search(text))


def classify_task(prompt: str, language_code: str) -> str | None:
    patterns = EN_TASKS if language_code == "eng" else AR_TASKS
    for task_family, pattern in patterns:
        if pattern.search(prompt):
            return task_family
    return None


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def build(parquet_path: Path) -> tuple[dict[str, object], dict[str, object]]:
    if parquet_path.stat().st_size != SOURCE_FILE_SIZE:
        raise SystemExit("SOURCE_SIZE_MISMATCH")
    if file_sha256(parquet_path) != SOURCE_FILE_SHA256:
        raise SystemExit("SOURCE_SHA256_MISMATCH")

    parquet = pq.ParquetFile(parquet_path)
    if parquet.schema_arrow.names != EXPECTED_SCHEMA:
        raise SystemExit("SCHEMA_AMBIGUITY_UNRESOLVED")

    counts: collections.Counter[str] = collections.Counter()
    family_counts: collections.Counter[tuple[str, str]] = collections.Counter()
    language_counts: collections.Counter[str] = collections.Counter()
    annotation_types: set[str] = set()
    seen_content: set[str] = set()
    records: list[dict[str, object]] = []
    source_row_index = 0

    # user_id is intentionally absent from this column list.
    read_columns = ["inputs", "targets", "language", "language_code", "annotation_type"]
    for row_group in range(parquet.num_row_groups):
        table = parquet.read_row_group(row_group, columns=read_columns)
        for prompt_raw, target_raw, language, language_code, annotation_type in zip(
            table["inputs"].to_pylist(),
            table["targets"].to_pylist(),
            table["language"].to_pylist(),
            table["language_code"].to_pylist(),
            table["annotation_type"].to_pylist(),
            strict=True,
        ):
            row_index = source_row_index
            source_row_index += 1
            counts["SOURCE_ROWS"] += 1
            annotation_types.add(annotation_type)

            if annotation_type != "original-annotations":
                counts["EXCLUDE_REANNOTATION"] += 1
                continue

            admitted_language = ADMITTED_LANGS.get(language_code)
            if admitted_language is None or language != admitted_language[0]:
                counts["EXCLUDE_NON_ADMITTED_LANGUAGE"] += 1
                continue

            prompt = normalize_text(prompt_raw)
            target = normalize_text(target_raw)
            if not prompt or not target or CONTROL_RE.search(prompt) or CONTROL_RE.search(target):
                counts["EXCLUDE_INVALID_TEXT_SHAPE"] += 1
                continue

            combined = f"{prompt}\n{target}"
            if clinical_scope_hit(combined):
                counts["EXCLUDE_CLINICAL_SCOPE"] += 1
                continue
            if privacy_risk_hit(combined):
                counts["EXCLUDE_PRIVACY_PATTERN"] += 1
                continue

            task_family = classify_task(prompt, language_code)
            if task_family is None:
                counts["EXCLUDE_SCOPE_NOT_DETERMINISTICALLY_ENFORCEABLE"] += 1
                continue

            candidate_representation = {
                "annotation_type": "original-annotations",
                "inputs": prompt,
                "language_code": language_code,
                "targets": target,
            }
            content_sha256 = hashlib.sha256(canonical_json_bytes(candidate_representation)).hexdigest()
            if content_sha256 in seen_content:
                counts["EXCLUDE_DUPLICATE_CONTENT"] += 1
                continue
            seen_content.add(content_sha256)

            candidate_record_id = hashlib.sha256(
                f"{SOURCE_FILE_SHA256}:{row_index}:{content_sha256}".encode("ascii")
            ).hexdigest()
            capabilities = {admitted_language[1], "GENERAL_INSTRUCTION_FOLLOWING"}
            if task_family in {"SUMMARIZATION", "FORMATTING_ORGANIZATION"}:
                capabilities.add("NON_CLINICAL_RESEARCH_LEARNING_FORMATTING")

            records.append(
                {
                    "admission_state": "BLOCKED",
                    "candidate_record_id": candidate_record_id,
                    "content_sha256": content_sha256,
                    "contamination_state": "NOT_ASSESSED",
                    "language_code": language_code,
                    "privacy_state": "UNRESOLVED",
                    "rights_state": "UNRESOLVED",
                    "task_family": task_family,
                    "verified_target_capability_ids": sorted(capabilities),
                }
            )
            counts["PROVISIONAL_CANDIDATES"] += 1
            language_counts[language_code] += 1
            family_counts[(language_code, task_family)] += 1

    if annotation_types != EXPECTED_ANNOTATION_TYPES:
        raise SystemExit("ORIGINAL_HUMAN_ORIGIN_NOT_ESTABLISHED")
    if sum(counts[key] for key in counts if key != "SOURCE_ROWS") != counts["SOURCE_ROWS"]:
        raise SystemExit("COUNT_RECONCILIATION_FAILED")

    manifest = {
        "candidate_count": len(records),
        "filter_id": FILTER_ID,
        "manifest_id": MANIFEST_ID,
        "records": records,
        "schema_version": "1",
        "scope_id": SCOPE_ID,
        "source_file": SOURCE_FILE,
        "source_file_sha256": SOURCE_FILE_SHA256,
        "source_file_xet_hash": SOURCE_XET_HASH,
        "source_repository": SOURCE_REPOSITORY,
        "source_revision": SOURCE_REVISION,
    }
    manifest_sha256 = hashlib.sha256(canonical_json_bytes(manifest)).hexdigest()
    summary = {
        "annotation_types": sorted(annotation_types),
        "candidate_count": len(records),
        "candidate_manifest_sha256": manifest_sha256,
        "counts": dict(sorted(counts.items())),
        "filter_id": FILTER_ID,
        "human_inspection_performed": False,
        "language_counts": dict(sorted(language_counts.items())),
        "task_family_counts": {
            f"{language_code}:{task_family}": count
            for (language_code, task_family), count in sorted(family_counts.items())
        },
        "user_id_read": False,
    }
    return manifest, summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parquet", required=True, type=Path)
    parser.add_argument("--out-manifest", required=True, type=Path)
    parser.add_argument("--out-summary", required=True, type=Path)
    args = parser.parse_args()

    manifest, summary = build(args.parquet)
    args.out_manifest.write_bytes(canonical_json_bytes(manifest) + b"\n")
    args.out_summary.write_bytes(canonical_json_bytes(summary) + b"\n")
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
