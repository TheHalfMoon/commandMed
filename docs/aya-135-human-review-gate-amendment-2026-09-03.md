# Aya 135 Human Review Gate Amendment — 2026-09-03

**Decision class:** Founder bounded scientific-governance amendment  
**Decision ID:** `FD-008`  
**Decision:** `REMOVE_MANDATORY_AYA_135_LOCAL_HUMAN_REVIEW_GATE`  
**Effective when:** this amendment and the aligned current-state/task edits are canonically merged  
**Scope:** exact fixed Aya 135 candidate qualification line in Spec 007 / E004 only  
**Current authorized spend:** USD 0

## Operative Founder direction

On 2026-09-03 the Founder explicitly directed that the current Aya human-review requirement is not needed and that work should continue according to the repository plan.

This record treats that direction as a separate bounded amendment to the Aya 135 qualification evidence mechanism. It does not infer a broader removal of human evidence from patient-facing, clinical, statistical, human-factor, release, or other scientific gates.

## Current rule

The current E004 Aya 135 boundary requires a real local human to inspect every exact candidate and provide record-level privacy, embedded-source-risk, and `SP007-RO-001` scope dispositions before the canonical Spec 003 evaluator can admit any record.

```text
AYA_135_HUMAN_REVIEW_REQUIRED=YES
AI_ASSISTANT_SUBSTITUTES_FOR_HUMAN_REVIEW=NO
PRIVACY_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
RIGHTS_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
```

## Replacement rule

For the exact fixed Aya 135 subject only, human inspection is no longer a mandatory evidence mechanism.

Record-level privacy, embedded-source-risk, and scope evidence may instead be supplied by a predeclared, deterministic, reproducible, local-only method that:

- is bound to the exact canonical Aya source bytes and exact 135 candidate identities;
- reads no `user_id`;
- performs no network request;
- sends no record content to an AI model, external semantic judge, API, or third-party provider;
- emits no raw Aya prompt/target text;
- keeps raw payload material transient and local;
- records exact method and implementation identities before using results for admission;
- remains fail-closed for any ambiguous or unclassified record;
- leaves the canonical Spec 003 evaluator as the sole component allowed to compute `ELIGIBLE`.

```text
AYA_135_HUMAN_REVIEW_REQUIRED=NO
AYA_135_DETERMINISTIC_RECORD_EVIDENCE_ALLOWED=YES
DEFAULT_PRIVACY_PASS=PROHIBITED
DEFAULT_RIGHTS_PASS=PROHIBITED
DEFAULT_SCOPE_PASS=PROHIBITED
CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED
PRIVACY_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
RIGHTS_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
CONTAMINATION_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
```

Removing the human-review mechanism does not itself convert any existing `UNRESOLVED` state into `SUPPORTED`, `NO_PHI_KNOWN`, `PASS`, or `ELIGIBLE`.

## Rights and privacy preservation

The commandMed Constitution Principle III remains unchanged: unclear rights remain a blocker. Dataset-level Apache-2.0 evidence does not automatically prove embedded or quoted third-party rights for every record.

The existing deterministic candidate filter's privacy-pattern exclusions remain valid evidence, but they do not automatically clear all remaining records. A successor deterministic method must explicitly define conservative record-level privacy and embedded-source-risk rules before execution. Ambiguous cases remain blocked or are excluded.

No PHI access, restricted dataset access, external provider screening, remote AI record processing, or legal-advice claim is created by this amendment.

## Affected governance

This amendment prospectively supersedes only the mandatory-human-inspection requirement for the exact Aya 135 qualification line encoded in:

- `specs/007-sft-v1/e004-aya-135-local-human-review-boundary-2026-09-03.md`;
- `specs/007-sft-v1/e004-registry-current-state-reconciliation-v20-2026-09-03.md`;
- the current E004 narrative in `specs/007-sft-v1/tasks.md`;
- earlier Aya 135 records only to the extent they are read prospectively as requiring a human reviewer for this exact qualification edge.

Historical records remain valid audit history and are not rewritten.

This amendment does not change:

- Constitution Principle II clinical safety hard gates;
- Constitution Principle III provenance/licensing/data-lineage requirements;
- Constitution Principle VIII holdout quarantine;
- Constitution Principle IX identity-bound reproducibility;
- Decision `D-010` requiring human evidence for patient-facing benefit/safety claims;
- `FD-003` clinician/Arabic/human-factor budget decision;
- any later explicit clinical, statistical, human-factor, or release-human-evidence requirement.

## Comparability and evidence preservation

All prior Aya candidate construction, contamination, Spec 003, transport, cleanup, and hash evidence remains comparable under its original identities.

The prior human-review script and boundary remain historical artifacts. `HUMAN_REVIEW_EXECUTED=NO` remains true and is not rewritten into a completed review; it simply ceases to be the blocking mechanism for this exact Aya qualification edge after this amendment becomes canonical.

## Authority created

```text
FD008_DECISION=REMOVE_MANDATORY_AYA_135_LOCAL_HUMAN_REVIEW_GATE
AYA_135_HUMAN_REVIEW_REQUIRED=NO
AYA_135_DETERMINISTIC_RECORD_EVIDENCE_AUTHORITY=AUTHORIZED_EXACT_FIXED_SET_LOCAL_ONLY
AYA_135_REMOTE_MODEL_OR_AI_RECORD_PROCESSING_AUTHORITY=NONE
AYA_135_EXTERNAL_PROVIDER_SCREENING_AUTHORITY=NONE
AYA_135_USER_ID_READ_AUTHORITY=NONE
DATA_ADMISSION_AUTHORITY=UNCHANGED_EXACT_SPEC003_EVALUATOR_ONLY
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Non-authority

This amendment does not claim that the 135 records are rights-cleared, privacy-cleared, in-scope, admitted, training-ready, or safe. It grants no model/weight access expansion, conversion, quantization, inference, tournament execution, A15 activation, training, credential use, protected-data access, paid compute, procurement, payment, spend, clinical qualification, release claim, or project-completion authority.
