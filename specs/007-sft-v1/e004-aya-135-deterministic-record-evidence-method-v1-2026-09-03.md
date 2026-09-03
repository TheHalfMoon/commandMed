# E004 Aya 135 Deterministic Record Evidence Method V1 — 2026-09-03

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Authority:** `FD-008` / `REMOVE_MANDATORY_AYA_135_LOCAL_HUMAN_REVIEW_GATE`
**Method ID:** `AYA_135_LOCAL_DETERMINISTIC_RECORD_EVIDENCE_V1`
**Artifact class:** pre-result method freeze
**Current authorized spend:** USD 0

## 1. Purpose

Define the exact deterministic, local-only, fail-closed method that may replace mandatory human inspection for the fixed Aya 135 qualification edge.

This document freezes the method before any real-result execution. It does not contain or imply record-level results.

## 2. Exact subject

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_SIZE=137195800
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
FILTER_ID=AYA_SP007_RO_001_CANDIDATE_FILTER_V1
CANDIDATE_COUNT=135
CANDIDATE_MANIFEST_CANONICAL_SHA256=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
CANDIDATE_RECORD_ID_SET_SHA256=d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83
CANDIDATE_CONTENT_SHA256_SET_SHA256=ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64
```

Any mismatch aborts. No candidate-set widening or substitution is permitted.

## 3. Execution boundary

The method is local-only and deterministic.

```text
USER_ID_READ=PROHIBITED
NETWORK_ACCESS=PROHIBITED
EXTERNAL_AI_OR_MODEL_RECORD_PROCESSING=PROHIBITED
EXTERNAL_PROVIDER_SCREENING=PROHIBITED
SEMANTIC_JUDGE=PROHIBITED
RAW_TEXT_OUTPUT=PROHIBITED
RAW_TEXT_REPOSITORY_PERSISTENCE=PROHIBITED
POST_RESULT_RULE_CHANGE=PROHIBITED
```

The implementation reads only `inputs`, `targets`, `language_code`, and `annotation_type` from the exact verified payload. Raw text may exist only transiently in local process memory while a record is classified. Output contains hashes and categorical evidence only.

## 4. Replay identity

For every source row, the method reconstructs the canonical normalized representation:

```text
{
  "annotation_type": <annotation_type>,
  "inputs": <NFC normalized input>,
  "language_code": <language_code>,
  "targets": <NFC normalized target>
}
```

It recomputes `content_sha256` and the row-bound `candidate_record_id` using the canonical source SHA-256 and source row index. Exactly the fixed 135 manifest identities must be recovered once each.

## 5. Privacy classification

Allowed output states:

```text
NO_PHI_KNOWN
RESTRICTED_OR_PHI
UNRESOLVED
```

The classifier uses fixed lexical/structural rules only.

### Strong privacy indicators -> `RESTRICTED_OR_PHI`

Strong indicators include explicit email addresses, phone-like identifiers, SSN-like identifiers, payment-card-like numbers, IP addresses, street-address patterns, and direct first-person identity declarations in English or Arabic.

### Ambiguity indicators -> `UNRESOLVED`

Ambiguity indicators include weak identity/location/account markers, social handles, explicit dates of birth, government/passport/medical-record identifier labels, geocoordinates, and other fixed patterns that are insufficiently specific to assert a safe state.

### Otherwise -> `NO_PHI_KNOWN`

`NO_PHI_KNOWN` means no privacy/PHI indicator is known under this exact deterministic method. It is not a universal proof that no identifying information could exist.

## 6. Embedded-source-risk classification

Allowed output states:

```text
NO_EMBEDDED_SOURCE_RISK_OBSERVED
EMBEDDED_SOURCE_RISK_PRESENT
UNRESOLVED
```

### Explicit source/copyright indicators -> `EMBEDDED_SOURCE_RISK_PRESENT`

Fixed indicators include URLs, DOI/ISBN patterns, copyright/all-rights-reserved/license notices, explicit source/citation/byline markers, lyrics/song/book/article/excerpt/quoted-passage markers, and similar direct signals of third-party source material.

### Transformation task families -> `UNRESOLVED`

The following candidate task families remain rights-ambiguous without independent source provenance even when no explicit source marker is present:

```text
TRANSLATION
SUMMARIZATION
REWRITE_EDIT
FORMATTING_ORGANIZATION
```

These records are not defaulted to rights-supported.

### Narrow generation/language task families

Only the following task families may produce `NO_EMBEDDED_SOURCE_RISK_OBSERVED`, and only when no explicit or ambiguous source marker is detected:

```text
CREATIVE_OR_COMPOSITION
LANGUAGE_LEARNING
```

If the fixed rules cannot classify safely, output `UNRESOLVED`.

## 7. Rights mapping

Dataset-level Aya rights evidence remains the pinned Apache-2.0 metadata already recorded canonically.

For this exact method:

```text
EMBEDDED_SOURCE_RISK_STATE=NO_EMBEDDED_SOURCE_RISK_OBSERVED -> RECORD_LEVEL_RIGHTS_STATE=SUPPORTED
EMBEDDED_SOURCE_RISK_STATE=EMBEDDED_SOURCE_RISK_PRESENT -> RECORD_LEVEL_RIGHTS_STATE=UNRESOLVED
EMBEDDED_SOURCE_RISK_STATE=UNRESOLVED -> RECORD_LEVEL_RIGHTS_STATE=UNRESOLVED
```

This is bounded research-evidence evaluation, not legal advice. A deterministic clear state does not erase the original dataset provenance; it indicates only that this method observed no record-level embedded-source risk beyond the supported dataset-level license evidence.

## 8. Scope verification

Allowed output states:

```text
PASS
FAIL
UNRESOLVED
```

`PASS` requires all of:

- exact manifest identity replay;
- `annotation_type=original-annotations`;
- admitted language code (`eng` or `arb`);
- deterministic task-family recomputation exactly matching the manifest task family;
- no fixed clinical-scope marker in input or target;
- non-empty normalized input and target with no prohibited control characters.

A clinical hit, annotation mismatch, language mismatch, or task-family mismatch yields `FAIL`. If task family cannot be deterministically recomputed, scope is `UNRESOLVED`.

## 9. Admission mapping

The method does not compute `ELIGIBLE`.

Only complete record evidence may be supplied to the canonical Spec 003 evaluator. The evaluator remains authoritative and fail-closed:

```text
CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED
PRIVACY_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
RIGHTS_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
CONTAMINATION_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
SCOPE_FAIL_OR_UNRESOLVED_IS_NOT_ADMITTED=YES
```

Records with privacy `RESTRICTED_OR_PHI`, unresolved privacy, unresolved rights, or failed/unresolved scope remain non-admitted.

## 10. Repository-safe output

Per-record output may include only:

- `candidate_record_id`;
- `content_sha256`;
- `language_code`;
- `task_family`;
- `privacy_state`;
- `embedded_source_risk_state`;
- `record_level_rights_state`;
- `scope_verification`;
- deterministic reason codes.

Aggregate output may include state counts and exact method/source/manifest identities. Raw Aya text and `user_id` are prohibited.

## 11. Implementation binding

The intended implementation path is:

```text
scripts/e004_aya_135_deterministic_record_evidence_v1.py
```

The exact implementation SHA-256 must be recorded after the implementation is canonical and before real-result promotion. Any material rule change requires a new method version and may not reuse V1 result identities.

## 12. Non-authority

This method freeze performs no real Aya record classification and grants no data admission, final curriculum admission, DatasetSnapshot, model conversion, model inference, tournament execution, A15 activation, training, credential use, protected-data access, paid compute, procurement/payment, spend, clinical qualification, release claim, or project-completion authority.
