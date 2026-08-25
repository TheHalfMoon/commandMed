# Spec 005 — Session 8 Q4 Primary-Selection Evidence-Source Strategy

**Lifecycle:** CLARIFY ONLY  
**Accepted question:** Session 8 — Q4  
**Exact predecessor head:** `d8b84783062030cc072292da05b6ab1f9c60f56d`  
**Canonical metadata base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`  
**Purpose:** freeze a scientifically legitimate source strategy for future primary model-selection evidence without opening or executing benchmark payloads, without promoting public evaluation/test assets into selection, and without creating a new selection dataset in this clarification.

> This artifact grants no model, weight, benchmark-execution, split-generation, dataset-generation, corrective-maintenance implementation, Ready, merge, or PLAN authority.

## Research-boundary exception recorded honestly

During Q4 metadata research, opening the official Hugging Face page for `openai/healthbench-professional` caused the dataset viewer to automatically render example rows in the returned page. This was unintended read-only preview exposure.

```text
Q4_UNINTENDED_PAYLOAD_PREVIEW_OCCURRED=YES
Q4_UNINTENDED_PAYLOAD_PREVIEW_SOURCE=OFFICIAL_HUGGINGFACE_DATASET_VIEWER_HEALTHBENCH_PROFESSIONAL
Q4_PAYLOAD_DOWNLOAD_PERFORMED=NO
Q4_PAYLOAD_COPY_OR_CACHE_CREATED=NO
Q4_PAYLOAD_EXECUTION_PERFORMED=NO
Q4_PAYLOAD_CONTENT_USED_TO_DERIVE_POLICY=NO
Q4_FURTHER_DATASET_VIEWER_PAYLOAD_ACCESS=STOPPED
```

The Q4 policy below is derived only from source-level metadata, repository structure, official split code, and published methodology. It does not rely on any question, rubric, answer, physician response, or other row content returned by that preview.

This exception means Q4 does **not** claim `BENCHMARK_PAYLOAD_ACCESS_OCCURRED=NONE` for the research session. Existing execution/access authority remains unchanged and no future payload access is authorized.

## Canonical commandMed constraints

Canonical Spec 001 quarantine governance defines:

- `CHECKPOINT_SELECTION`: selection-capable only for model-selection dev sets / public benchmark dev splits;
- `PUBLIC_EXTERNAL_EVAL`: public benchmark canonical test splits and `can_select_model=false`;
- public test-set leakage/overfitting prevention as an explicit invariant.

Session 7 additionally froze:

```text
REGISTRY_INTENDED_USE_DEVELOPMENT_IS_NOT_QUARANTINE_PURPOSE=YES
PUBLIC_DEVELOPMENT_LABEL_ALONE_CAN_SELECT_MODEL=NO
EXPLICIT_SPLIT_SEMANTICS_REQUIRED_FOR_SELECTION_CAPABLE_PURPOSE=YES
PUBLIC_CANONICAL_TEST_SPLITS_CAN_SELECT_MODEL=NO
```

Session 8 Q3 further established that MedXpertQA `Text/dev.jsonl` is a five-question few-shot development set and is not scientifically adequate as a primary quality-floor or winner-ranking slice.

## HealthBench source disposition

The canonical commandMed registry currently binds:

- `healthbench_core` → `2025-05-07-06-14-12_oss_eval.jsonl` at official dataset revision `40ee1968852fc57f625934251ac22be47077a8fb`;
- `healthbench_consensus` → `consensus_2025-05-09-20-00-46.jsonl` at the same revision;
- `healthbench_hard` → `hard_2025-05-08-21-00-10.jsonl` at the same revision;
- `healthbench_professional` → `healthbench_professional_eval.jsonl` at official dataset revision `349962fd46dd02343a0d8a606491baf59154ea1a`.

Primary-source semantics consistently identify these as evaluation assets:

- OpenAI describes HealthBench as an evaluation/benchmark that tests how well AI systems perform in realistic health scenarios;
- the official ordinary HealthBench repository names the artifacts `*_eval.jsonl` and states that it contains data for the HealthBench eval;
- later official dataset metadata exposes ordinary HealthBench configs as `test` splits, which is consistent with—not the sole basis for—the primary-source evaluation semantics;
- the official HealthBench Professional dataset describes its released file as the data for the HealthBench Professional eval and exposes the public dataset as a `test` split.

Therefore the broad commandMed registry `intended_use=DEVELOPMENT` label does not make these selection-dev assets.

Accepted HealthBench disposition:

```text
HEALTHBENCH_SPLIT_PURPOSE_POLICY=PUBLIC_EVALUATION_ASSETS_NOT_SELECTION_DEV

HEALTHBENCH_CORE_PURPOSE=PUBLIC_EXTERNAL_EVAL
HEALTHBENCH_CONSENSUS_PURPOSE=PUBLIC_EXTERNAL_EVAL
HEALTHBENCH_HARD_PURPOSE=PUBLIC_EXTERNAL_EVAL
HEALTHBENCH_PROFESSIONAL_PURPOSE=PUBLIC_EXTERNAL_EVAL

HEALTHBENCH_CORE_CAN_SELECT_MODEL=NO
HEALTHBENCH_CONSENSUS_CAN_SELECT_MODEL=NO
HEALTHBENCH_HARD_CAN_SELECT_MODEL=NO
HEALTHBENCH_PROFESSIONAL_CAN_SELECT_MODEL=NO

HEALTHBENCH_SELECTION_OR_CHECKPOINT_TUNING_USE=PROHIBITED
HEALTHBENCH_PROMOTION_TO_CHECKPOINT_SELECTION=PROHIBITED
HEALTHBENCH_PROMOTION_TO_DEV_SELECTION_AFTER_RESULTS=PROHIBITED

SESSION7_HEALTHBENCH_PURPOSE_MAPPING_UNRESOLVED=
SUPERSEDED_BY_SESSION8_Q4_PUBLIC_EXTERNAL_EVAL_MAPPING
```

No HealthBench score may decide the Spec 005 backbone winner under this clarification. HealthBench remains potentially valuable later as public external evaluation subject to all separately frozen access, contamination, metric/grader, and execution gates.

## PubMedQA official split semantics

Canonical commandMed currently binds the official PubMedQA PQA-L source container:

```text
PUBMEDQA_SOURCE_REVISION=1cbae8e92f72f20c8d3747cbb3bf5bc53554d997
PUBMEDQA_BOUND_SOURCE_ARTIFACT=data/ori_pqal.json
PUBMEDQA_BOUND_SOURCE_BLOB=38db7750761c78950ed32303e7545bdaa513390c
```

The pinned official repository contains `data/ori_pqal.json` and `data/test_ground_truth.json`, but does **not** commit generated `pqal_fold*/dev_set.json`, `pqal_fold*/train_set.json`, or `test_set.json` artifacts.

The pinned official `preprocess/split_dataset.py` provides an explicit deterministic PQA-L split protocol:

```text
PUBMEDQA_OFFICIAL_SPLIT_RANDOM_SEED=0
PUBMEDQA_PQAL_TOTAL_LABELED_COUNT=1000
PUBMEDQA_OFFICIAL_TEST_COUNT=500
PUBMEDQA_OFFICIAL_CV_POOL_COUNT=500
PUBMEDQA_OFFICIAL_CV_FOLD_COUNT=10
PUBMEDQA_OFFICIAL_DEV_COUNT_PER_FOLD=50
PUBMEDQA_OFFICIAL_TRAIN_COUNT_PER_FOLD=450
PUBMEDQA_OFFICIAL_SPLIT_STRATIFIES_BY_FINAL_DECISION_LABEL=YES
```

The PubMedQA paper independently states that 500 randomly sampled PQA-L instances are used for 10-fold cross-validation and the remaining 500 form the PubMedQA test set.

Accordingly, `ori_pqal.json` is a **source container from which both selection/development and external-test material are derived**. It must not itself be treated as one monolithic selection payload.

## PubMedQA selection-source policy

PubMedQA provides the only currently reviewed public source in Q4 with an official, explicit development/test separation that can support a future selection component without laundering its test set into selection.

The legitimate future selection source is the official PQA-L **CV half only**, not the 500-item official test half.

```text
PUBMEDQA_PURPOSE_POLICY=OFFICIAL_CV_DEV_ONLY_FOR_FUTURE_SELECTION_TEST_REMAINS_EXTERNAL

PUBMEDQA_CURRENT_BOUND_ORI_PQAL_PURPOSE=MIXED_SOURCE_CONTAINER_NOT_DIRECTLY_EXECUTABLE_FOR_SELECTION
PUBMEDQA_CURRENT_BOUND_ORI_PQAL_CAN_SELECT_MODEL=NO_AS_MONOLITHIC_PAYLOAD

PUBMEDQA_OFFICIAL_TEST_PURPOSE=PUBLIC_EXTERNAL_EVAL
PUBMEDQA_OFFICIAL_TEST_CAN_SELECT_MODEL=NO
PUBMEDQA_OFFICIAL_TEST_TO_SELECTION_REUSE=PROHIBITED

PUBMEDQA_OFFICIAL_CV_POOL_FUTURE_PURPOSE=CHECKPOINT_SELECTION_CANDIDATE
PUBMEDQA_OFFICIAL_CV_DEV_FOLDS_FUTURE_PURPOSE=CHECKPOINT_SELECTION_CANDIDATE

PUBMEDQA_CV_SELECTION_SOURCE_ELIGIBILITY=
CONDITIONAL_PENDING_EXACT_DERIVED_ARTIFACT_BINDING_AND_ALL_OTHER_GATES

PUBMEDQA_CV_DERIVED_ARTIFACTS_CURRENTLY_BOUND=NO
PUBMEDQA_CV_SPLIT_GENERATION_AUTHORITY=NONE
PUBMEDQA_CV_PAYLOAD_ACCESS_AUTHORITY=NONE
PUBMEDQA_CV_EXECUTION_AUTHORITY=NONE
```

No Q4 action runs the split script, reads `ori_pqal.json`, creates generated folds, computes derived payload hashes, or accesses `test_ground_truth.json` content.

A future separately authorized binding step would have to prove exact source revision/blob, exact splitter blob and runtime semantics, deterministic generated artifact identities, strict separation of the official 500-item test half, and quarantine purpose before any candidate execution.

## Scientific role of PubMedQA CV

Even after binding, PubMedQA CV is not broad enough by itself to carry commandMed's entire primary medical-quality claim. PubMedQA evaluates English biomedical research question answering over PubMed abstracts and has `LEARNER_RESEARCHER` role coverage in the canonical registry; it does not by itself establish broad patient, clinician-workflow, Arabic, emergency, abstention, or multimodal quality.

Therefore:

```text
PUBMEDQA_CV_MAY_BE_FUTURE_PRIMARY_SELECTION_COMPONENT=YES_IF_ALL_GATES_PASS
PUBMEDQA_CV_MAY_BE_SOLE_PRIMARY_MEDICAL_QUALITY_FLOOR=NO
PUBMEDQA_CV_MAY_BE_SOLE_WINNER_SELECTION_EVIDENCE=NO
```

This is a pre-result scope/coverage finding, not a candidate-score-derived restriction.

## Accepted primary-selection evidence architecture

Q4 freezes a **multi-source selection-development architecture with no public-test selection**:

```text
PRIMARY_SELECTION_EVIDENCE_SOURCE_POLICY=
MULTI_SOURCE_SELECTION_DEV_NO_PUBLIC_TEST_SELECTION

PRIMARY_SELECTION_REQUIRES_SELECTION_PURPOSE_SOURCES_ONLY=YES
PUBLIC_EXTERNAL_EVAL_AS_PRIMARY_SELECTION_INPUT=PROHIBITED
PRIVATE_GOLD_AS_PRIMARY_SELECTION_INPUT=PROHIBITED

HEALTHBENCH_PRIMARY_SELECTION_COMPONENT=NO
MEDXPERTQA_TEXT_TEST_PRIMARY_SELECTION_COMPONENT=NO
MEDXPERTQA_TEXT_DEV_SCORED_PRIMARY_SELECTION_COMPONENT=NO

PUBMEDQA_OFFICIAL_CV_PRIMARY_SELECTION_COMPONENT=
CONDITIONAL_PENDING_DERIVED_BINDING_AND_ALL_OTHER_GATES

ADDITIONAL_BROAD_SELECTION_DEV_EVIDENCE_REQUIRED=YES
ADDITIONAL_BROAD_SELECTION_DEV_EXACT_SOURCE=NOT_YET_FROZEN
ADDITIONAL_BROAD_SELECTION_DEV_PAYLOAD_CREATION_AUTHORITY=NONE
ADDITIONAL_BROAD_SELECTION_DEV_PROVIDER_GENERATION_AUTHORITY=NONE
ADDITIONAL_BROAD_SELECTION_DEV_EXECUTION_AUTHORITY=NONE
```

The additional broad selection-dev evidence may later be an adequately scoped, immutable, non-Gold development suite or another public benchmark dev split whose source/purpose/coverage can be proven. Q4 does not create, name, generate, or authorize that payload.

Any future dedicated commandMed selection-dev suite must remain logically distinct from Private Gold and from public external evaluation. It must be predeclared before candidate results and satisfy source rights, privacy, provenance, contamination, role/language coverage, metric identity, statistical adequacy, and immutable artifact binding before execution.

## Manifest consequence

Q4 does not freeze an executable primary-selection manifest.

```text
EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
PRIMARY_SELECTION_MANIFEST_FREEZE_STATUS=BLOCKED

PRIMARY_SELECTION_MANIFEST_BLOCKER_1=PUBMEDQA_CV_DERIVED_ARTIFACTS_NOT_BOUND
PRIMARY_SELECTION_MANIFEST_BLOCKER_2=ADDITIONAL_BROAD_SELECTION_DEV_SOURCE_NOT_FROZEN
PRIMARY_SELECTION_MANIFEST_BLOCKER_3=REQUIRED_SELECTION_METRIC_MAPPING_NOT_FROZEN
PRIMARY_SELECTION_MANIFEST_BLOCKER_4=CONTAMINATION_GATES_NOT_RESOLVED
PRIMARY_SELECTION_MANIFEST_BLOCKER_5=PAYLOAD_ACCESS_AND_EXECUTION_NOT_AUTHORIZED

MINIMUM_MEDICAL_QUALITY_THRESHOLD=NOT_YET_FROZEN
```

HealthBench purpose resolution does not authorize its payload access or execution. PubMedQA CV strategy does not authorize split generation, payload access, or execution.

## Corrective-maintenance consequence

Session 8 Q2 remains valid, but Q4 does not authorize metric-catalog maintenance.

```text
MEDXPERTQA_ACCURACY_METRIC_REPAIR_GOVERNANCE=SESSION8_Q2_PRESERVED
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE

PUBMEDQA_METRIC_MAPPING=NOT_YET_FROZEN
PUBMEDQA_METRIC_CATALOG_REPAIR_REQUIRED=UNRESOLVED_UNTIL_LEGITIMATE_METRIC_MAPPING_REVIEW
```

No canonical Spec 001/004 machine-readable artifact is changed by Q4.

## Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PUBMEDQA_SPLIT_GENERATION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

The unintended HealthBench Professional web preview recorded above is a historical Q4 research-boundary exception and does not expand any authority.

## Session 8 progress

Acceptance of Q4 advances only bounded Session 8:

```text
CLARIFICATION_SESSION_8=4_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_8_STATUS=IN_PROGRESS

PRIMARY_SELECTION_EVIDENCE_SOURCE_POLICY=
MULTI_SOURCE_SELECTION_DEV_NO_PUBLIC_TEST_SELECTION

CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Q4 does not complete Session 8, does not complete the overall CLARIFY lifecycle, and does not authorize transition to PLAN.

## Remaining clarification scope

Remaining work includes exact additional broad selection-dev source requirements / minimum medical-quality evidence architecture; PubMedQA CV derived-artifact binding governance and metric mapping; whether any separately governed canonical metric repair is needed; contamination-assessment access and candidate-specific contamination evidence; exact component rights/privacy/license evidence; exact llama.cpp/build/tokenizer/instrumentation identities; numeric performance thresholds; thermal/energy/failure-signal details; secondary ranking order; exact-head independent review; and final clarification lifecycle closure.
