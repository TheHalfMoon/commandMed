# E004 Aya 135 Curriculum Contamination Protocol V1 — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Authority source:** `E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_B`  
**Artifact class:** pre-result contamination method and comparison-universe freeze  
**Execution effect before canonical merge:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE

## 1. Purpose

Freeze the exact comparison universe and deterministic local method for the curriculum-specific contamination assessment authorized for the already-fixed Aya 135-candidate identity set.

This protocol is deliberately canonical **before** any comparison payload is materialized or assessed. It does not change the candidate set, admit data, freeze a DatasetSnapshot, repurpose tournament A11, access Private Gold, use a semantic judge, run a model, or authorize training.

## 2. Exact candidate subject

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

No candidate identity, source, language lane, scope, or filter widening is permitted.

## 3. Frozen canonical benchmark registry

The universe is derived from the canonical registry bound at protocol creation:

```text
REGISTRY_REPOSITORY=TheHalfMoon/commandMed
REGISTRY_COMMIT=70f683927f2f5cec53b8fe0adf2815986845c441
REGISTRY_PATH=data/eval/benchmarks.json
REGISTRY_GIT_BLOB_SHA1=db0ccd74e65493a0777572cd2da6fdaeae50ebc4
```

The inclusion predicate is frozen before results:

```text
REQUIRE_ACCESS_CLASS=PUBLIC
REQUIRE_VERIFICATION_STATUS=VERIFIED
REQUIRE_EXECUTABLE_IDENTITY_BOUND_ASSET=YES
REQUIRE_TEXT_BEARING_PAYLOAD=YES
REQUIRE_CANONICAL_REGISTRY_MEMBERSHIP=YES
REFERENCE_ONLY_UNBOUND_ASSETS=EXCLUDED
MIXED_GATED_PRIVATE_ASSETS=EXCLUDED
PRIVATE_GOLD=PROHIBITED
POST_RESULT_UNIVERSE_CHANGE=PROHIBITED
```

For an included multi-file benchmark, every text-bearing file named by the bound artifact identity is included. Non-text binary payloads are excluded only because the frozen method is a text-token overlap method and cannot compare binary image bytes to text candidates.

## 4. Frozen comparison universe

Machine-readable universe:

```text
UNIVERSE_ARTIFACT=specs/007-sft-v1/e004-aya-135-contamination-comparison-universe-v1.json
UNIVERSE_ENTRY_COUNT=9
UNIVERSE_CANONICAL_SHA256=e473b2607b28467f3bd055fb34a1e1092fc15f87558185e989d8e4c483c0e98e
```

Included assets are:

1. `openai/healthbench@40ee1968852fc57f625934251ac22be47077a8fb:2025-05-07-06-14-12_oss_eval.jsonl`
2. `openai/healthbench@40ee1968852fc57f625934251ac22be47077a8fb:consensus_2025-05-09-20-00-46.jsonl`
3. `openai/healthbench@40ee1968852fc57f625934251ac22be47077a8fb:hard_2025-05-08-21-00-10.jsonl`
4. `openai/healthbench-professional@349962fd46dd02343a0d8a606491baf59154ea1a:healthbench_professional_eval.jsonl`
5. `TsinghuaC3I/MedXpertQA@7e7c465a68eb2b866926bfa59c8c9d17a8daba65:Text/dev.jsonl`
6. `TsinghuaC3I/MedXpertQA@7e7c465a68eb2b866926bfa59c8c9d17a8daba65:Text/test.jsonl`
7. `TsinghuaC3I/MedXpertQA@7e7c465a68eb2b866926bfa59c8c9d17a8daba65:MM/dev.jsonl`
8. `TsinghuaC3I/MedXpertQA@7e7c465a68eb2b866926bfa59c8c9d17a8daba65:MM/test.jsonl`
9. `pubmedqa/pubmedqa@1cbae8e92f72f20c8d3747cbb3bf5bc53554d997:data/ori_pqal.json`

The machine-readable universe preserves direct SHA-256/Xet identities where canonical public metadata establishes them and uses immutable revision+locator binding where that is the canonical identity mechanism. PubMedQA additionally binds the canonical Git blob SHA-1 recorded by the registry.

## 5. Predeclared exclusions

The following exclusions are fixed before assessment and may not be changed after results:

- MedXpertQA `images.zip`: non-text binary payload, non-comparable under this text-only method;
- HealthBench `2025-05-07-06-14-12_oss_meta_eval.jsonl`: not a separately registered canonical benchmark asset in the bound commandMed registry;
- MedQA USMLE, MedMCQA, MedQAbstain, MedAbstain, and MedHELM family records: executable payload identity is unbound/unresolved, mixed, component-specific, or reference-only under the bound registry;
- all Private Gold, gated, credentialed, private, or paid assets: prohibited by the controlling Founder decision.

No excluded asset may be added after observing assessment results without a new pre-result canonical protocol.

## 6. Frozen deterministic method

```text
METHOD_ID=AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1
METHOD_SCRIPT=scripts/e004_aya_135_contamination_v1.py
METHOD_SCRIPT_SHA256=ab93c6277ae132b6f9119f482449491d3723878de8a7342b73fc78f71a23bf05
NGRAM_LENGTH_TOKENS=13
NORMALIZATION=UNICODE_NFKC_CASEFOLD
TOKENIZATION=PYTHON_UNICODE_REGEX_WORD_TOKENS
CANDIDATE_FIELDS_COMPARED=INPUTS_AND_TARGETS_SEPARATELY
COMPARISON_TEXT=ALL_JSON_STRING_LEAVES
ANY_13_TOKEN_EXACT_MATCH=OVERLAP_OR_HIGH_RISK
ZERO_MATCH_ACROSS_COMPLETE_VERIFIED_UNIVERSE=ASSESSED_CLEAN_FOR_THIS_DECLARED_METHOD
SEMANTIC_JUDGE=NONE
MODEL_INFERENCE=NONE
POST_RESULT_THRESHOLD_CHANGE=PROHIBITED
POST_RESULT_METHOD_CHANGE=PROHIBITED
```

The implementation hashes 13-token windows in memory and never emits the matched text or n-gram. Candidate prompt/target text is used only inside the local deterministic process after exact Aya byte and fixed-candidate identity verification.

`ASSESSED_CLEAN` means only that the exact candidate has no 13-token exact overlap under this frozen method across the complete verified comparison universe above. It is not a claim of semantic independence from all possible data in existence.

## 7. Comparison transport boundary

Comparison payload materialization may occur only after this protocol is canonical. The one-shot transport workflow bundled with this protocol may:

- use a standard GitHub-hosted runner in this public repository;
- fetch only the exact public immutable comparison locators above;
- verify the predeclared direct SHA-256/size or Git-blob identities where supplied;
- compute observed SHA-256 and size for every exact locator;
- publish the exact comparison files plus a hash-only transport manifest as a one-day transient artifact;
- delete runner-local comparison bytes after publication.

It may not receive Aya bytes, parse Aya records, perform the contamination comparison remotely, use model/AI processing, use user-managed credentials, access gated/private data, or incur incremental spend.

## 8. Local assessment preconditions

The local assessment aborts fail closed unless all are true:

```text
AYA_SOURCE_SHA256_MATCH=REQUIRED
AYA_CANDIDATE_MANIFEST_SHA256_MATCH=REQUIRED
AYA_CANDIDATE_COUNT_135=REQUIRED
AYA_RECORD_ID_SET_ROOT_MATCH=REQUIRED
AYA_CONTENT_HASH_SET_ROOT_MATCH=REQUIRED
COMPARISON_UNIVERSE_SHA256_MATCH=REQUIRED
ALL_9_COMPARISON_FILES_PRESENT=REQUIRED
TRANSPORT_MANIFEST_IDENTITY_MATCH=REQUIRED
DIRECT_SHA256_AND_SIZE_MATCH_WHERE_DECLARED=REQUIRED
PUBMEDQA_GIT_BLOB_MATCH=REQUIRED
```

Any mismatch aborts the assessment without substitution, universe reduction, filter repair, threshold change, or alternate asset.

## 9. Repository-safe result boundary

Permitted persistent result evidence includes only:

- method/universe identities;
- comparison byte hashes and sizes;
- candidate record/content hashes;
- per-candidate contamination state;
- comparison asset IDs associated with any overlap;
- aggregate counts and execution metadata.

Raw Aya text, comparison benchmark text, matched 13-token windows, `user_id`, Private Gold, credentials, or transient payload files must not be committed.

## 10. Admission effect

This protocol itself creates no PASS. After a completed assessment, the exact per-candidate contamination state may be supplied to the canonical Spec 003 evaluator together with independently justified rights, privacy, split/quarantine, source, origin, and scope evidence.

```text
CONTAMINATION_PROTOCOL_CAN_CREATE_ELIGIBLE=NO
RIGHTS_GATE_UNCHANGED=YES
PRIVACY_GATE_UNCHANGED=YES
HUMAN_PRIVACY_EVIDENCE_REQUIREMENT_UNCHANGED=YES
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 11. Repository qualification

Under constitutional amendment 0.1.1, independent repository/PR review is optional by default and no current bounded authority separately requires it for this protocol. Deterministic validation remains mandatory.

Before merge verify exact base/head/diff, JSON validity, script syntax, exact comparison identities against the canonical benchmark registry and public source metadata, applicable status/CI, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
