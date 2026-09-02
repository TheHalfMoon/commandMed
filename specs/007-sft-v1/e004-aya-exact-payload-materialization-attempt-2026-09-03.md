# E004 Aya Exact Payload Materialization Attempt — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Founder decision record:** `specs/007-sft-v1/e004-public-data-payload-access-founder-decision-2026-09-03.md`  
**Canonical decision merge:** `34c89dc710eeaeb1952d76f65c55e30b2eb9462a`  
**Artifact class:** bounded execution-attempt evidence  
**Authority effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Record the first bounded execution attempt after canonical Founder Decision B without overstating data access, byte verification, parsing, screening, candidate construction, admission, contamination, model execution, or training.

## 2. Exact authorized subject

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
```

The exact immutable source identity above is the only payload subject authorized by Decision B.

## 3. Canonical authority at attempt time

```text
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
AYA_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_PIN_ONLY
AYA_PAYLOAD_MATERIALIZATION_AUTHORITY=AUTHORIZED_EPHEMERAL_EXACT_PUBLIC_PIN_ONLY
AYA_CANDIDATE_CONSTRUCTION_AUTHORITY=AUTHORIZED_NON_ADMITTING_SP007_RO_001_ONLY
AYA_PRIVACY_SCREENING_AUTHORITY=AUTHORIZED_LOCAL_DETERMINISTIC_AND_HUMAN_INSPECTION_WITH_NO_EXTERNAL_PROVIDER
AYA_RAW_PAYLOAD_REPOSITORY_PERSISTENCE_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 4. Public source metadata observation

Public source metadata remained consistent with the canonical identity pin at attempt time: the published train parquet identity continued to report the canonical SHA-256 and Xet hash, and source documentation continued to distinguish original human annotations from re-annotations and expose the relevant annotation metadata fields.

These observations are metadata/source-document evidence only. They are not local payload-byte verification and are not promoted into a payload-derived PASS.

## 5. Exact immutable materialization attempt

The execution environment attempted to reach the exact immutable revision-bound payload route required by Decision B.

The current execution tools could not materialize that exact immutable binary subject in the local analysis environment:

- the binary download helper required an exact previously viewable URL and could not consume the immutable route through the available browsing safety boundary;
- direct container networking could not resolve the external host;
- available public browsing surfaces exposed mutable `main` or alternate converted parquet routes rather than a locally materializable exact immutable binary path.

No source-side unavailability is asserted. The blocker is the current execution environment's inability to materialize the exact authorized immutable byte route without substituting an unauthorized path.

```text
MATERIALIZATION_ATTEMPT_RESULT=BLOCKED_FAIL_CLOSED
MATERIALIZATION_BLOCKER=EXACT_PIN_MATERIALIZATION_BLOCKED_BY_EXECUTION_ENVIRONMENT
PINNED_SOURCE_PUBLIC_METADATA_AVAILABLE=YES_OBSERVED
PINNED_SOURCE_DECLARED_UNAVAILABLE=NO
```

## 6. Unauthorized substitutes rejected

The following were explicitly not used as payload substitutes:

```text
MUTABLE_MAIN_PAYLOAD_SUBSTITUTION=REJECTED_NOT_AUTHORIZED
REFS_CONVERT_PARQUET_SUBSTITUTION=REJECTED_NOT_AUTHORIZED
MIRROR_OR_DERIVATIVE_SUBSTITUTION=REJECTED_NOT_AUTHORIZED
ALTERNATE_AYA_FILE_OR_REVISION_SUBSTITUTION=REJECTED_NOT_AUTHORIZED
OASST1_OR_DOLLY_FALLBACK=REJECTED_NOT_AUTHORIZED
```

Observed byte-identity correspondence on an alternate route does not widen Decision B and does not authorize using that route.

## 7. Execution facts

```text
AYA_PAYLOAD_DOWNLOAD_PERFORMED=NO
AYA_PAYLOAD_MATERIALIZED=NO
AYA_PAYLOAD_HASH_VERIFICATION_PERFORMED=NO
AYA_PAYLOAD_PARSED=NO
AYA_SCHEMA_FROM_LOCAL_PAYLOAD_INSPECTED=NO
AYA_RECORD_LEVEL_SCREENING_PERFORMED=NO
AYA_CANDIDATE_CONSTRUCTION_PERFORMED=NO
AYA_PRIVACY_SCREENING_PERFORMED=NO
AYA_HUMAN_INSPECTION_OF_RECORD_CONTENT_PERFORMED=NO
AYA_CANDIDATE_RECORD_IDENTITIES_CREATED=NO
AYA_CANDIDATE_CONTENT_IDENTITIES_CREATED=NO
AYA_RAW_PAYLOAD_REPOSITORY_PERSISTED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

No local SHA-256 was computed because no payload bytes were materialized. The canonical expected SHA-256 remains an identity requirement, not an observed local verification result.

## 8. Source-document semantics retained as metadata evidence only

Published source documentation for the pinned source identifies fields including:

```text
inputs
targets
language
language_code
annotation_type
user_id
```

and distinguishes original annotations from re-annotations. Decision B therefore still requires local exact-payload inspection before freezing any record filter implementation or claiming record-level classification.

```text
ORIGINAL_HUMAN_ANNOTATION_FILTER_FROZEN=NO
REANNOTATION_EXCLUSION_EXECUTED=NO
DEMOGRAPHICS_EXCLUSION_EXECUTED=NO
USER_ID_REMOVAL_FROM_CANDIDATE_REPRESENTATION_EXECUTED=NO
SP007_RO_001_RECORD_SCOPE_FILTER_EXECUTED=NO
```

## 9. Downstream gates remain closed

```text
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
QUARANTINE_PASS=NO
LICENSE_ADMISSION_PASS=NO
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 10. E004 effect

This attempt does not complete E004 and does not create tournament evidence.

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 11. Dependency-safe continuation boundary

The next payload-derived step requires an execution environment capable of materializing the exact immutable authorized subject and computing its SHA-256 before parsing.

This execution-attempt evidence does not authorize widening the source identity, using mutable `main`, using `refs/convert/parquet`, selecting another source, or creating contamination/admission/conversion/A15/training authority.

If a future execution environment can materialize the exact immutable subject under the existing Decision B authority, no new Founder data-access decision is required merely to retry the same exact subject. Any widening of the authorized source/path/revision would require separate canonical authority.
