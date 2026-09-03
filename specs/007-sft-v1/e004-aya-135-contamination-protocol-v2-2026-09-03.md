# E004 Aya 135 Curriculum Contamination Protocol V2 — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Authority:** `E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_B`  
**Status:** PRE-RESULT REPLAY REPAIR; SUPERSEDES V1 IMPLEMENTATION ONLY  
**Current authorized spend:** USD 0

## 1. Purpose

Repair a pre-result candidate-replay defect in the V1 implementation without changing the frozen scientific contamination method, comparison universe, candidate subject, thresholds, or authority boundary.

No contamination disposition was produced by V1 before this repair. V1 aborted fail closed with:

```text
CANDIDATE_RECORD_ID_REPLAY_MISMATCH
```

The abort occurred during exact candidate replay, before comparison-universe scanning and before any `ASSESSED_CLEAN` or `OVERLAP_OR_HIGH_RISK` result existed.

## 2. Unchanged exact candidate subject

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
FILTER_ID=AYA_SP007_RO_001_CANDIDATE_FILTER_V1
CANDIDATE_COUNT=135
CANDIDATE_MANIFEST_CANONICAL_SHA256=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
CANDIDATE_RECORD_ID_SET_SHA256=d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83
CANDIDATE_CONTENT_SHA256_SET_SHA256=ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64
```

## 3. Unchanged frozen scientific method

```text
METHOD_ID=AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1
NGRAM_LENGTH_TOKENS=13
NORMALIZATION=UNICODE_NFKC_PLUS_CASEFOLD
TOKENIZATION=PYTHON_UNICODE_WORD_TOKENIZATION
AYA_FIELDS_COMPARED=INPUTS_AND_TARGETS_SEPARATELY
COMPARISON_TEXT=ALL_JSON_STRING_LEAVES
ANY_MATCH_DISPOSITION=OVERLAP_OR_HIGH_RISK
ZERO_MATCH_COMPLETE_VERIFIED_UNIVERSE_DISPOSITION=ASSESSED_CLEAN
SEMANTIC_JUDGE=NONE
MODEL_INFERENCE=NONE
```

The frozen comparison universe remains `e004-aya-135-contamination-comparison-universe-v1` with canonical SHA-256:

```text
UNIVERSE_CANONICAL_SHA256=e473b2607b28467f3bd055fb34a1e1092fc15f87558185e989d8e4c483c0e98e
```

No entry, threshold, normalization rule, tokenization rule, comparison field, or disposition rule changes in V2.

## 4. V1 implementation defect

V1 indexed the manifest by `content_sha256`, then treated the first source row with that content representation as the candidate row before checking the row-bound `candidate_record_id`.

Canonical candidate identity is instead:

```text
SHA256(SOURCE_FILE_SHA256 + ":" + SOURCE_ROW_INDEX + ":" + CONTENT_SHA256)
```

A source row outside the fixed candidate set can therefore share the same content representation while having a different row-bound candidate identity. V1 correctly failed closed rather than silently accepting that ambiguity.

## 5. V2 implementation repair

V2 computes the row-bound candidate ID for every source row first, looks that exact ID up in the fixed manifest, and only then verifies that the manifest content hash equals the recomputed content hash.

```text
METHOD_SCRIPT=scripts/e004_aya_135_contamination_v2.py
METHOD_SCRIPT_SHA256=a77ac21329f175662be7edf24b1fe8ff76a7ae8a90727b73bc11ef5d4c4c0d2a
```

Pre-result replay-only validation established:

```text
REPAIRED_CANDIDATE_REPLAY_COUNT=135
EXPECTED_CANDIDATE_COUNT=135
CONTAMINATION_COMPARISON_EXECUTED_DURING_REPAIR_VALIDATION=NO
CONTAMINATION_RESULT_OBSERVED_BEFORE_V2_CANONICALIZATION=NO
```

The replay-only validation did not open or scan comparison payload files and did not compute candidate contamination dispositions.

## 6. Execution boundary

After this V2 implementation is canonical and qualified, execution may reuse the already-canonical V1 comparison universe and the already-verified transient comparison artifact from workflow run `33778720996`, provided its exact artifact digest and all internal transport identities still verify locally.

All V1 boundaries remain controlling:

```text
REMOTE_AYA_PROCESSING=PROHIBITED
EXTERNAL_MODEL_OR_AI_PROCESSING=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
GATED_OR_CREDENTIALED_ACCESS=PROHIBITED
RAW_MATCHED_TEXT_REPOSITORY_PERSISTENCE=PROHIBITED
RAW_AYA_TEXT_REPOSITORY_PERSISTENCE=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 7. Authority exclusions

This repair creates no rights PASS, privacy PASS, admission PASS, final curriculum authority, DatasetSnapshot authority, model conversion authority, A15 activation, training authority, procurement, payment, or spend authority.

## 8. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded deterministic pre-result implementation repair. Before merge, verify exact base/head/diff, V2 script syntax, V2 script SHA-256, the 135-candidate replay-only validation, unchanged V1 method/universe identity, applicable status/CI, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
