# E004 Aya Local Candidate Construction Evidence — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical base at bounded-pass closeout:** `21a00936f38b11adfc9141bc7cf83dff70b4d3bc`  
**Artifact class:** repository-safe bounded execution evidence  
**Authority effect:** NONE  
**Admission effect:** NONE  
**Training effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Record the repository-safe results of the exact Aya public-data candidate-construction pass authorized by the already-canonical Founder decisions without persisting raw Aya payload bytes, raw record text, annotator identifiers, or an admitted curriculum.

This evidence records what actually occurred. It does not infer rights, privacy clearance, contamination cleanliness, admission, DatasetSnapshot eligibility, model execution, A15 activation, or training authority.

## 2. Controlling authority

The bounded pass remained within these canonical decisions:

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B
FOUNDER_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION=E004_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION_B
CURRENT_AUTHORIZED_SPEND_USD=0
```

The GitHub transport-bridge Founder decision became canonical through PR #196 / merge `5be3205d79c14633973c8f745659e0b6490bb7f6` before any hosted payload download was executed.

## 3. Exact byte subject

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
SOURCE_FILE_SIZE_BYTES=137195800
```

No alternate Aya file, revision, mirror, converted dataset, demographics configuration, OASST1 source, Dolly source, gated asset, credentialed asset, paid route, or substitute source was used.

## 4. Transport execution and byte verification

PR #197 / merge `d4ab43d359e3820f6d7d3514f1f22ceba3710de4` introduced the bounded one-shot transport workflow only after the bridge decision was canonical.

GitHub Actions run `33760893301`, job `100666636213`, completed successfully. The job:

1. verified the standard GitHub-hosted runner and public repository context;
2. rechecked the exact Aya `main` head, published pointer SHA-256/size, Xet hash, and unauthenticated public route;
3. downloaded only the exact authorized file;
4. computed the hosted SHA-256 and required exact equality;
5. published the verified bytes as transient artifact `9895384385` / `E004_AYA_EXACT_PAYLOAD_TRANSPORT_BRIDGE` with one-day retention;
6. removed the runner-local payload.

The transferred artifact was materialized into the local execution environment. Before any Parquet parsing, the local payload was verified:

```text
LOCAL_FILE_SIZE_BYTES=137195800
LOCAL_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
LOCAL_POSTTRANSPORT_BYTE_VERIFICATION=PASS
PARSE_BEFORE_LOCAL_SHA256_MATCH=NO
```

The first artifact-cleanup implementation failed before deletion because its JSON identity guard depended on compact formatting. The failure was retained as audit truth and no deletion was claimed. PR #199 / merge `a9097b4700fb035768afeb095d018c5992a67818` repaired the guard with typed `jq` equality. Cleanup run `33761433144`, job `100668465648`, then succeeded, and the original bridge run subsequently exposed zero artifacts.

PR #200 / merge `07ff80c78872c5445b8e3f7336a8e7d8d1e9a7dc` removed the completed Aya transport and payload-cleanup workflows from `main`.

## 5. Local Parquet tooling boundary

The local runtime initially had no Parquet parser and its direct outbound package-download route was unavailable. A separate one-shot workflow therefore transported only a public parsing-tool wheel; it never received Aya content.

Exact tooling subject:

```text
TOOL=pyarrow
TOOL_VERSION=25.0.1
WHEEL=pyarrow-25.0.1-cp313-cp313-manylinux_2_28_x86_64.whl
PUBLISHED_WHEEL_SHA256=0befcf816e45a1af33ac775a9970b749e4868a230c7372f0ae5e932bee27039f
```

PR #201 / merge `da3b46bc1a6985ef046269d3d9df6ad77b2818bd` ran the tooling bootstrap. Run `33762143729` succeeded. The wheel SHA-256 was verified locally before installation and installation used `--no-index`.

The transient tooling artifact `9895921509` was later deleted by the one-shot cleanup introduced through PR #202 / merge `21a00936f38b11adfc9141bc7cf83dff70b4d3bc`; cleanup run `33763407701` completed successfully and the bootstrap run subsequently exposed zero artifacts.

```text
AYA_CONTENT_SENT_TO_TOOLING_WORKFLOW=NO
EXTERNAL_RECORD_PROCESSING=NO
USER_MANAGED_CREDENTIAL_USED=NO
INCREMENTAL_SPEND_USD=0
```

## 6. Exact pinned schema and annotation semantics

Parsing occurred locally only after the mandatory local SHA-256 match.

The exact pinned Parquet schema is:

```text
inputs:string
targets:string
language:string
language_code:string
annotation_type:string
user_id:string
```

Exact row count:

```text
SOURCE_ROWS=202362
```

The exact `annotation_type` value universe and counts from the pinned bytes are:

```text
original-annotations=137092
re-annotations=65270
ANNOTATION_TYPE_NULLS=0
```

Only those two annotation classes were observed. This resolves the prior hyphen/underscore naming ambiguity for this exact revision and establishes `original-annotations` as the executable original-human class for this pass.

A prior public-research artifact recorded a documented/source-card original count of `138844`. The exact pinned bytes instead contain `137092` `original-annotations` rows. This pass does not silently reconcile the difference:

```text
PRIOR_DOCUMENTED_ORIGINAL_COUNT=138844
EXACT_PINNED_BYTE_ORIGINAL_COUNT=137092
COUNT_DISCREPANCY=1752
CONTROLLING_COUNT_FOR_THIS_BYTE_SUBJECT=137092
```

The byte-derived count governs this exact file identity. The earlier documented value remains historical public-source metadata rather than exact-byte evidence.

## 7. Data-minimization and privacy boundary

The filter implementation intentionally never read the `user_id` column. The schema field was observed only as part of schema validation.

```text
USER_ID_COLUMN_READ=NO
USER_ID_PERSISTED=NO
USER_ID_IN_CANDIDATE_REPRESENTATION=NO
DEMOGRAPHICS_CONFIGURATION_USED=NO
RAW_RECORD_TEXT_PERSISTED_TO_REPOSITORY=NO
RAW_RECORD_TEXT_SENT_TO_EXTERNAL_MODEL_PROVIDER_OR_API=NO
```

Because ChatGPT itself is an external model/provider boundary, raw Aya records were not surfaced to the assistant for manual semantic or privacy judgment. The authorized human-inspection option therefore was not represented as completed.

```text
DETERMINISTIC_LOCAL_PRIVACY_RISK_SCREENING_PERFORMED=YES
BOUNDED_HUMAN_RECORD_INSPECTION_PERFORMED=NO
FINAL_PRIVACY_CLEARANCE_CREATED=NO
PRIVACY_STATE_FOR_PROVISIONAL_CANDIDATES=UNRESOLVED
```

Records matching deterministic privacy-risk patterns were excluded. Any content requiring non-deterministic judgment was excluded fail closed rather than sent to an external model/provider.

## 8. Frozen bounded filter implementation

Repository-safe implementation:

```text
FILTER_ID=AYA_SP007_RO_001_CANDIDATE_FILTER_V1
FILTER_IMPLEMENTATION=scripts/e004_aya_candidate_pass.py
EXECUTED_LOCAL_SCRIPT_SHA256=12ecee629f5558bb347ad0f14ff75cea9f3b00d90030ad19513d4e87bd566f8f
```

The script:

- requires the exact expected source size and SHA-256 before parsing;
- requires the exact six-field schema;
- never reads `user_id`;
- retains `original-annotations` only;
- excludes every `re-annotations` row;
- admits only exact `eng`/`English` and `arb`/`Standard Arabic` lanes for this conservative V1 pass;
- excludes other languages and Arabic varieties rather than inferring equivalence;
- applies local deterministic clinical-scope exclusion patterns in English and Arabic;
- applies local deterministic privacy-risk patterns;
- accepts only deterministically recognized non-clinical task families;
- excludes unclassifiable records fail closed;
- creates canonical content hashes and source-row-bound candidate record identities;
- deduplicates by canonical content SHA-256;
- marks every surviving candidate `BLOCKED`, with rights/privacy unresolved and contamination not assessed;
- emits no record text.

The executed local script passed `py_compile` and bounded synthetic-only checks for English/Arabic task classification, clinical exclusion, and privacy-risk matching. Synthetic tests contained no Aya record text.

## 9. Aggregate candidate-construction result

Exact deterministic result:

```text
SOURCE_ROWS=202362
EXCLUDE_NON_ADMITTED_LANGUAGE=132172
EXCLUDE_REANNOTATION=65270
EXCLUDE_SCOPE_NOT_DETERMINISTICALLY_ENFORCEABLE=2623
EXCLUDE_CLINICAL_SCOPE=2131
EXCLUDE_PRIVACY_PATTERN=24
EXCLUDE_INVALID_TEXT_SHAPE=4
EXCLUDE_DUPLICATE_CONTENT=3
PROVISIONAL_CANDIDATES=135
COUNT_RECONCILIATION=PASS
```

The reason-coded result accounts for every source row exactly once.

Provisional candidate language counts:

```text
eng=88
arb=47
```

Task-family counts are preserved in `e004-aya-candidate-pass-summary-v1.json`.

These 135 records are not an admitted dataset, DatasetSnapshot, curriculum, quarantine PASS, privacy PASS, rights PASS, or contamination PASS.

## 10. Repository-safe identity roots

A full local hash-only candidate manifest was constructed to establish immutable identities without persisting record text. To minimize repository persistence of per-record lookup material, the full 135-record hash list is not committed. Repository persistence is limited to aggregate evidence and identity roots.

```text
LOCAL_FULL_HASH_MANIFEST_CANONICAL_SHA256=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
LOCAL_FULL_HASH_MANIFEST_FILE_SHA256=bbc7188613f242b428b4ac4cad0297c9dfb31403f6fab146a1a8491a106b2d6e
CANDIDATE_RECORD_ID_SET_SHA256=d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83
CANDIDATE_CONTENT_SHA256_SET_SHA256=ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64
CANDIDATE_COUNT=135
```

See:

- `e004-aya-candidate-hash-roots-v1.json`;
- `e004-aya-candidate-pass-summary-v1.json`.

The local full hash-only manifest is transient verification material, not canonical repository content.

## 11. Raw/transient cleanup

After candidate construction, the exact local source SHA-256 and size were rechecked once more before deletion. The raw Parquet and the prior Aya transient workspace were then removed.

```text
PREDELETE_SOURCE_SHA256_MATCH=PASS
PREDELETE_SOURCE_SIZE_MATCH=PASS
RAW_AYA_PARQUET_DELETED=YES
TRANSIENT_AYA_WORKSPACE_REMOVED=YES
RAW_OR_TRANSIENT_AYA_PAYLOAD_REMAINING=NO
REMOTE_AYA_TRANSPORT_ARTIFACT_REMAINING=NO
REMOTE_TOOLING_ARTIFACT_REMAINING=NO
```

No raw Aya byte payload remains in canonical repository source or in the bounded local workspace.

## 12. Fail-closed admission state

Every candidate remains non-admitted:

```text
AYA_CANDIDATE_CONSTRUCTION_PERFORMED=YES_NON_ADMITTING
PROVISIONAL_CANDIDATE_COUNT=135
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_CREATED=NO
CURRICULUM_RECORDS_CREATED=NO
RIGHTS_STATE=UNRESOLVED
PRIVACY_STATE=UNRESOLVED
CONTAMINATION_STATE=NOT_ASSESSED
QUARANTINE_PASS=NO
LICENSE_COMPATIBILITY_ADMISSION_PASS=NO
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
```

No caller-controlled or inferred `ELIGIBLE` state is created.

## 13. Downstream authorities remain closed

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE
TRAINING_AUTHORITY=NONE
SFT_AUTHORITY=NONE
CPT_AUTHORITY=NONE
LORA_QLORA_AUTHORITY=NONE
DISTILLATION_AUTHORITY=NONE
DPO_RL_GRPO_AUTHORITY=NONE
QAT_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 14. Dependency effect

This pass resolves the former local-byte-materialization and original-annotation-schema blockers. It does not satisfy the first live component dependency, because the exact provisional candidate set still lacks independently authorized and evidence-bound rights/license, final privacy, split/quarantine, contamination, and Spec 003 admission dispositions.

The existing A11 contamination-assessment authority template concerns the separately frozen tournament selection-suite/candidate-corpus assessment sequence. It is not treated as authority for Aya curriculum admission or as an activatable substitute at this frontier.

```text
FORMER_LOCAL_BYTE_MATERIALIZATION_BLOCKER=RESOLVED
ORIGINAL_HUMAN_ANNOTATION_SEMANTICS=RESOLVED_FOR_EXACT_PIN
NON_ADMITTING_CANDIDATE_IDENTITY_SET=CREATED
FIRST_COMPONENT_DEPENDENCY_FULLY_SATISFIED=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

The next dependency-safe repository action is to reconcile the current frontier and, only after that state is canonical, prepare the exact narrow authority surface required for further qualification/admission evidence over this fixed 135-candidate identity set. No such authority is inferred by this evidence record.
