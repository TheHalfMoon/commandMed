# Spec 005 — Session 8 Q1 Primary-Selection Manifest and Metric Gap

**Lifecycle:** CLARIFY ONLY  
**Accepted question:** Session 8 — Q1  
**Exact predecessor head:** `6eb64c88526f1e522a46f2b2253065365cccd212`  
**Canonical commandMed metadata base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`  
**Purpose:** determine whether an exact primary-selection slice manifest and metric mapping can be frozen now, using canonical commandMed benchmark/metric contracts plus read-only immutable upstream metadata only, without benchmark payload access or execution.

> This artifact is documentation/governance only. No benchmark payload, question, answer key, model weight, contamination-assessment payload, candidate corpus, Private Gold payload, provider/API, PHI/restricted data, or gated asset was opened, downloaded, copied, cached, or executed. No model, benchmark, device, conversion, contamination scan, or training execution occurred. This Q1 does not authorize `PLAN`, Ready, merge, model access, benchmark access, contamination-assessment access, cross-spec metric mutation, or tournament execution.

## 1. Canonical commandMed boundary

Canonical Spec 001 / current Spec 005 clarification state proves:

- the public-development metadata envelope is `healthbench_core`, `healthbench_consensus`, `healthbench_hard`, `healthbench_professional`, `medxpertqa`, and `pubmedqa`;
- `MedXpertQA Text/dev.jsonl` at immutable dataset revision `7e7c465a68eb2b866926bfa59c8c9d17a8daba65` is the only currently established slice with explicit selection-capable split semantics;
- its frozen Spec 005 purpose is `CHECKPOINT_SELECTION`;
- `MedXpertQA Text/test.jsonl` is `PUBLIC_EXTERNAL_EVAL` and cannot select a model;
- MedXpertQA multimodal slices are secondary/non-ranking under `COMMON_CORE_PRIMARY_RANKING`;
- HealthBench and PubMedQA exact purpose mappings remain unresolved and therefore cannot enter an executable/selectable primary manifest yet;
- any future primary-selection manifest must bind exact benchmark/slice identity, purpose, canonical metric IDs/directions, contamination/quarantine disposition, and selection eligibility before execution;
- only canonical Spec 001 metrics may be used; a benchmark-specific metric identity may not be silently repurposed for another benchmark.

Canonical `data/eval/metrics.json` currently contains one MCQ accuracy metric:

```text
metric_id=medqa_usmle_accuracy
name=MedQA USMLE 4-Option Accuracy
description=Standard board-style multiple-choice medical examination accuracy (MedQA USMLE 4-option).
direction=HIGHER_BETTER
is_hard_gate=false
```

That metric is explicitly MedQA/USMLE-specific. It is not a generic medical-MCQ accuracy identity and is not an identity match for MedXpertQA.

## 2. Immutable upstream MedXpertQA metric evidence

Read-only upstream inspection was metadata/code-documentation only.

Official MedXpertQA repository:

```text
repository=TsinghuaC3I/MedXpertQA
reviewed_commit=47b29e17b8d980e03b62a22927cff775016c6afd
reviewed_readme_blob=cdfa3908e32a39996e80633725c7c08b40a90325
```

At that immutable commit, the official README states that `eval.ipynb` calculates **accuracy on each subset**. Therefore the upstream benchmark score semantics are accuracy, not ECE, active-information-acquisition efficiency, citation entailment, or the MedQA-specific metric identity.

Official dataset metadata identifies:

```text
benchmark=MedXpertQA
subset=Text
split=dev
artifact=Text/dev.jsonl
canonical_commandmed_dataset_revision=7e7c465a68eb2b866926bfa59c8c9d17a8daba65
question_format=multiple-choice
label=correct answer choice
```

An immutable earlier official Hugging Face README commit (`763321d51153ef51817a03d0faaf07de6a622059`) explicitly documented each subset dev split as 5 questions and the Text test set as 2,450 questions. The later/current dataset card preserves `dev.jsonl` and `test.jsonl` split identities but no longer states those counts in the prose. commandMed's canonical registry itself does not record a dev-split sample count or statistical-adequacy finding.

Accordingly, Q1 does **not** assert that the current canonical dataset revision's dev payload count was independently re-counted, because payload access is unauthorized. It records only that the official upstream metadata makes the dev split's adequacy for a sole minimum-medical-quality selection floor unproven and requires separate statistical evidence before such a claim could be frozen.

## 3. Material metric-identity gap

The exact upstream score semantics and the canonical commandMed metric identities do not currently align:

```text
UPSTREAM_MEDXPERTQA_SCORE_SEMANTICS=ACCURACY
CANONICAL_SPEC001_GENERIC_MEDICAL_MCQ_ACCURACY_METRIC=NONE
CANONICAL_SPEC001_MEDXPERTQA_ACCURACY_METRIC=NONE
CANONICAL_SPEC001_MEDQA_USMLE_ACCURACY_METRIC=medqa_usmle_accuracy
```

Using `medqa_usmle_accuracy` for MedXpertQA would misstate the benchmark identity and evidence contract. It is prohibited.

Likewise, substituting another existing non-hard-gate metric merely because it is numerically rankable would be invalid:

- `expected_calibration_error` measures calibration, not answer accuracy;
- `active_info_acquisition_efficiency` requires multi-turn information-acquisition evidence, not single-turn MCQ accuracy;
- resource metrics such as `installed_package_bytes` belong to the post-qualification ranking phase and cannot replace the minimum medical-quality evidence;
- hard-gate metrics cannot be repurposed as ranking/accuracy metrics.

## 4. Accepted Q1 policy

`FAIL_CLOSED_PRIMARY_MANIFEST_ON_CANONICAL_METRIC_IDENTITY_GAP` is frozen:

```text
PRIMARY_SELECTION_MANIFEST_POLICY=
FAIL_CLOSED_PRIMARY_MANIFEST_ON_CANONICAL_METRIC_IDENTITY_GAP

CURRENT_ONLY_EXPLICIT_SELECTION_PURPOSE_SLICE=
medxpertqa:Text/dev.jsonl@7e7c465a68eb2b866926bfa59c8c9d17a8daba65

CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_COUNT=1
CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_1_BENCHMARK_ID=medxpertqa
CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_1_ARTIFACT=Text/dev.jsonl
CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_1_SOURCE_REVISION=7e7c465a68eb2b866926bfa59c8c9d17a8daba65
CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_1_MODALITY=TEXT
CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_1_PURPOSE=CHECKPOINT_SELECTION
CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_1_CAN_SELECT_MODEL=YES_IF_ALL_OTHER_GATES_PASS
CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_1_UPSTREAM_SCORE_SEMANTICS=ACCURACY
CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_1_CANONICAL_METRIC_ID=UNRESOLVED
CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_1_CONTAMINATION_GATE=INCOMPLETE
CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_1_PAYLOAD_ACCESS=NOT_AUTHORIZED
CURRENT_PRIMARY_SELECTION_SLICE_CANDIDATE_1_EXECUTION=NOT_AUTHORIZED

MEDXPERTQA_TEXT_TEST_PRIMARY_SELECTION_MEMBERSHIP=PROHIBITED_PUBLIC_EXTERNAL_EVAL
MEDXPERTQA_MM_PRIMARY_SELECTION_MEMBERSHIP=PROHIBITED_COMMON_CORE_PRIMARY_RANKING
HEALTHBENCH_PRIMARY_SELECTION_MEMBERSHIP=BLOCKED_PURPOSE_UNRESOLVED
PUBMEDQA_PRIMARY_SELECTION_MEMBERSHIP=BLOCKED_PURPOSE_UNRESOLVED

CANONICAL_SPEC001_COMPATIBLE_MEDXPERTQA_ACCURACY_METRIC_ID=NONE
PRIMARY_SELECTION_METRIC_MAPPING=UNRESOLVED_CANONICAL_METRIC_IDENTITY_GAP
MEDQA_USMLE_ACCURACY_REUSE_FOR_MEDXPERTQA=PROHIBITED
OTHER_EXISTING_METRIC_SUBSTITUTION_FOR_MEDXPERTQA_ACCURACY=PROHIBITED

FUTURE_MEDXPERTQA_METRIC_SEMANTICS_REQUIRED=EXACT_CHOICE_ACCURACY_COMPATIBLE_WITH_UPSTREAM_SCORING
FUTURE_MEDXPERTQA_METRIC_DIRECTION=HIGHER_BETTER
FUTURE_MEDXPERTQA_CANONICAL_METRIC_ID=UNRESOLVED
FUTURE_METRIC_MUST_HAVE_SEPARATELY_CANONICAL_IDENTITY_AND_EVIDENCE_CONTRACT=YES
FUTURE_METRIC_MUST_BE_FROZEN_BEFORE_PRIMARY_MANIFEST_FREEZE=YES

MEDXPERTQA_TEXT_DEV_STATISTICAL_ADEQUACY_FOR_SOLE_PRIMARY_QUALITY_FLOOR=UNPROVEN
SOLE_PRIMARY_SELECTION_SLICE_REQUIRES_CANDIDATE_INDEPENDENT_STATISTICAL_ADEQUACY_EVIDENCE=YES
MINIMUM_MEDICAL_QUALITY_THRESHOLD=NOT_YET_FROZEN

EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
PRIMARY_SELECTION_MANIFEST_FREEZE_STATUS=BLOCKED
PRIMARY_SELECTION_MANIFEST_FREEZE_BLOCKER_1=NO_CANONICAL_COMPATIBLE_MEDXPERTQA_ACCURACY_METRIC_ID
PRIMARY_SELECTION_MANIFEST_FREEZE_BLOCKER_2=SOLE_EXPLICIT_SELECTION_SLICE_STATISTICAL_ADEQUACY_UNPROVEN

Q1_AUTHORIZES_SPEC001_METRIC_CATALOG_MUTATION=NO
Q1_AUTHORIZES_HEALTHBENCH_PURPOSE_CREATION=NO
Q1_AUTHORIZES_PUBMEDQA_PURPOSE_CREATION=NO
Q1_AUTHORIZES_BENCHMARK_PAYLOAD_ACCESS=NO
Q1_AUTHORIZES_BENCHMARK_EXECUTION=NO
Q1_AUTHORIZES_MODEL_EXECUTION=NO
```

## 5. Consequences

### 5.1 What is frozen

Q1 freezes the **fail-closed manifest-readiness decision**, not an executable primary-selection manifest.

The one current exact selection-purpose slice candidate is now explicit and immutable at the metadata layer:

```text
medxpertqa / Text/dev.jsonl / 7e7c465a68eb2b866926bfa59c8c9d17a8daba65 / CHECKPOINT_SELECTION
```

Its upstream score semantics are accuracy with `HIGHER_BETTER` direction.

### 5.2 What is deliberately not frozen

The exact primary-selection manifest remains unfrozen because a complete row requires a canonical commandMed metric ID and an adequate evidence basis. Neither condition is currently satisfied.

Q1 therefore does not:

- invent `medxpertqa_accuracy` inside Spec 005;
- widen `medqa_usmle_accuracy` to MedXpertQA;
- treat ECE or another metric as a proxy for accuracy;
- declare the five-example historical few-shot dev metadata sufficient for a minimum medical-quality floor;
- move MedXpertQA test into model selection;
- move multimodal MedXpertQA into common-core primary ranking;
- infer HealthBench or PubMedQA selection purpose;
- modify canonical Spec 001 metric/benchmark artifacts.

### 5.3 Required future repair before manifest freeze

Before `EXACT_PRIMARY_SELECTION_SLICE_MANIFEST` may become frozen, a separately authorized and reviewed canonical maintenance/clarification path must establish all of:

1. a canonical metric identity whose semantics exactly cover MedXpertQA Text answer accuracy, with direction/evidence/scoring contract frozen;
2. a candidate-independent statistical-adequacy basis for any slice used as the minimum medical-quality selection floor;
3. the minimum medical-quality threshold or decision rule, frozen before candidate results;
4. complete contamination disposition under Session 7 Q4;
5. unchanged exact artifact/purpose binding;
6. the same finalized manifest for every comparable candidate.

If a broader primary slice set is desired, HealthBench/PubMedQA may enter only after their purpose/split semantics and compatible canonical metric mappings are separately resolved before results.

## 6. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

Zero-cost or public availability does not create execution/access authority.

## 7. Session 8 progress

Acceptance of Q1 advances only bounded Session 8:

```text
CLARIFICATION_SESSION_8=1_QUESTION_ACCEPTED
CLARIFICATION_SESSION_8_STATUS=IN_PROGRESS

PRIMARY_SELECTION_MANIFEST_POLICY=
FAIL_CLOSED_PRIMARY_MANIFEST_ON_CANONICAL_METRIC_IDENTITY_GAP
PRIMARY_SELECTION_MANIFEST_FREEZE_STATUS=BLOCKED
EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
PRIMARY_SELECTION_METRIC_MAPPING=UNRESOLVED_CANONICAL_METRIC_IDENTITY_GAP

CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

This Q1 does not complete Session 8, does not complete the full clarification lifecycle, and does not authorize transition to `PLAN`.

## 8. Remaining clarification scope

The immediate material blocker is now explicit: canonical metric identity/statistical adequacy must be repaired before an exact primary-selection manifest can be frozen. Other unresolved work still includes any separately authorized contamination-assessment-only access route; actual candidate-specific contamination evidence; HealthBench/PubMedQA purpose binding if canonically supportable; minimum medical-quality and clinical/statistical thresholds; exact component rights/privacy/license evidence; exact llama.cpp/build/tokenizer/instrumentation identities; numeric performance values; thermal/energy/failure-signal details; secondary ranking order; exact-head independent review; and final clarification lifecycle closure.
