# Spec 005 — Session 8 Q3 MedXpertQA Text/dev Scientific Role

**Lifecycle:** CLARIFY ONLY  
**Accepted question:** Session 8 — Q3  
**Exact predecessor head:** `5b2d912b274bcb91bfc8d9837f33741d403711c3`  
**Canonical metadata base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`  
**Purpose:** determine whether MedXpertQA `Text/dev.jsonl` is scientifically adequate to serve as a scored primary-selection / minimum-medical-quality slice in Spec 005, using metadata and published methodology only and without opening benchmark payloads.

> This artifact is governance/research only. No benchmark question, answer key, model weight, candidate corpus, Private Gold payload, PHI/restricted data, gated asset, provider/API, runtime, device, conversion, contamination scan, inference, benchmark execution, or training execution was accessed or performed. It grants no payload-access, execution, corrective-maintenance implementation, Ready, merge, or PLAN authority.

## Evidence reviewed without payload access

The official MedXpertQA paper and official dataset metadata establish the following non-payload facts:

- MedXpertQA contains Text and MM subsets and is designed to assess expert-level medical knowledge/reasoning across 17 medical specialties, 11 body systems, and 3 task categories.
- Each subset is divided into a **few-shot development set with 5 questions** and a larger test set.
- An immutable official Hugging Face dataset-card revision states `Text/dev.jsonl` contains 5 questions and `Text/test.jsonl` contains 2,450 questions.
- The published experiments evaluate models using **zero-shot chain-of-thought prompting unless otherwise specified**, with greedy decoding where available.
- The official repository states that its evaluation script calculates accuracy on each subset.

No payload rows were opened or counted by commandMed in this clarification. The 5-question and 2,450-question counts are upstream metadata claims, not locally derived payload facts.

## Scientific adequacy finding

A five-question few-shot development set is not scientifically adequate to serve as the sole scored primary-selection evidence or the sole minimum-medical-quality floor for commandMed's broad backbone tournament.

This finding does not require an invented numerical power threshold:

1. **Coverage impossibility by cardinality.** Five questions cannot individually represent all 17 declared medical specialties or all 11 declared body systems. Therefore the set cannot itself establish broad specialty/body-system quality coverage.
2. **Extremely coarse accuracy resolution.** If scored by simple item accuracy, five questions permit only six raw accuracy values (`0%`, `20%`, `40%`, `60%`, `80%`, `100%`). That granularity is too coarse for a defensible backbone quality floor or winner-selection comparison.
3. **Upstream role semantics.** The authors explicitly call this a **few-shot development set**, while their benchmark experiments are zero-shot unless otherwise specified. The much larger test split is the benchmark evaluation set; commandMed already freezes canonical test splits as `PUBLIC_EXTERNAL_EVAL` and prohibits using them to select a model.
4. **No candidate-result evidence is needed for this conclusion.** The inadequacy derives from pre-result upstream metadata and declared benchmark design, so the rule can be frozen without observing any candidate score.

## Accepted policy

`FEW_SHOT_DEV_NOT_PRIMARY_QUALITY_FLOOR` is frozen:

```text
MEDXPERTQA_TEXT_DEV_SCIENTIFIC_ROLE_POLICY=
FEW_SHOT_DEV_NOT_PRIMARY_QUALITY_FLOOR

MEDXPERTQA_TEXT_DEV_ARTIFACT=Text/dev.jsonl
MEDXPERTQA_TEXT_DEV_UPSTREAM_ROLE=FEW_SHOT_DEVELOPMENT_SET
MEDXPERTQA_TEXT_DEV_UPSTREAM_QUESTION_COUNT=5
MEDXPERTQA_TEXT_TEST_UPSTREAM_QUESTION_COUNT=2450
UPSTREAM_COUNT_SOURCE=IMMUTABLE_OFFICIAL_DATASET_METADATA
LOCAL_PAYLOAD_COUNT_PERFORMED=NO

MEDXPERTQA_DECLARED_SPECIALTY_COUNT=17
MEDXPERTQA_DECLARED_BODY_SYSTEM_COUNT=11
MEDXPERTQA_TEXT_DEV_CAN_COVER_ALL_DECLARED_SPECIALTIES_BY_CARDINALITY=NO
MEDXPERTQA_TEXT_DEV_CAN_COVER_ALL_DECLARED_BODY_SYSTEMS_BY_CARDINALITY=NO

MEDXPERTQA_TEXT_DEV_SIMPLE_ACCURACY_STEP_PERCENTAGE_POINTS=20
MEDXPERTQA_TEXT_DEV_STATISTICAL_ADEQUACY_FOR_SOLE_PRIMARY_QUALITY_FLOOR=NO
MEDXPERTQA_TEXT_DEV_STATISTICAL_ADEQUACY_FOR_PRIMARY_WINNER_SELECTION_SCORE=NO

MEDXPERTQA_TEXT_DEV_PURPOSE=CHECKPOINT_SELECTION
MEDXPERTQA_TEXT_DEV_QUARANTINE_CAN_SELECT_MODEL=YES
QUARANTINE_CAN_SELECT_MODEL_MEANS_SCIENTIFIC_ADEQUACY=NO

MEDXPERTQA_TEXT_DEV_SPEC005_REQUIRED_PRIMARY_SCORING_SLICE_ELIGIBILITY=NO
MEDXPERTQA_TEXT_DEV_SPEC005_PRIMARY_QUALITY_FLOOR_ELIGIBILITY=NO
MEDXPERTQA_TEXT_DEV_SPEC005_WINNER_RANKING_SCORE_ELIGIBILITY=NO

SESSION7_Q1_PRIMARY_SELECTION_ELIGIBLE_IF_ALL_OTHER_GATES_PASS=
SUPERSEDED_FOR_SCIENTIFIC_SCORING_ROLE_BY_SESSION8_Q3

MEDXPERTQA_TEXT_DEV_MAY_BE_USED_AS_SCORED_PRIMARY_SELECTION_EVIDENCE=NO
MEDXPERTQA_TEXT_DEV_MAY_BE_USED_TO_SET_MINIMUM_MEDICAL_QUALITY_THRESHOLD=NO

MEDXPERTQA_TEXT_DEV_FUTURE_NONSCORING_DEVELOPMENT_SUPPORT=
ALLOWED_ONLY_IF_SEPARATELY_FROZEN_AND_AUTHORIZED
MEDXPERTQA_TEXT_DEV_FUTURE_FEW_SHOT_PROMPT_CONTEXT=
ALLOWED_ONLY_IF_FUTURE_PROMPT_PROTOCOL_EXPLICITLY_REQUIRES_IT_AND_PAYLOAD_ACCESS_IS_SEPARATELY_AUTHORIZED

MEDXPERTQA_TEXT_DEV_CURRENT_PAYLOAD_ACCESS=NOT_AUTHORIZED
MEDXPERTQA_TEXT_DEV_CURRENT_PAYLOAD_EXECUTION=NOT_AUTHORIZED
MEDXPERTQA_TEXT_DEV_CURRENT_CONTAMINATION_GATE=INCOMPLETE

NO_CURRENT_CANONICAL_PUBLIC_SLICE_IS_PROVEN_BOTH_SELECTION_PURPOSE_COMPATIBLE_AND_SCIENTIFICALLY_ADEQUATE_FOR_PRIMARY_QUALITY_FLOOR=YES

EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
PRIMARY_SELECTION_MANIFEST_FREEZE_STATUS=BLOCKED
PRIMARY_SELECTION_MANIFEST_FREEZE_BLOCKER=
NO_CURRENT_CANONICAL_PUBLIC_SLICE_PROVEN_BOTH_SELECTION_PURPOSE_COMPATIBLE_AND_SCIENTIFICALLY_ADEQUATE

MINIMUM_MEDICAL_QUALITY_THRESHOLD=NOT_YET_FROZEN
```

## Quarantine permission versus scientific eligibility

Session 7 Q1 mapped `Text/dev.jsonl` to `CHECKPOINT_SELECTION` because it is an explicit dev split and the canonical quarantine contract permits such a source class to select a model.

Q3 does **not** retroactively relabel that quarantine purpose. Instead it freezes a stricter scientific rule for Spec 005:

```text
quarantine_permission != scientific_evidence_adequacy
```

A slice may be technically allowed inside a selection-purpose quarantine while still being scientifically too small or unrepresentative to carry a required quality floor or winner-ranking score.

Thus:

- `MEDXPERTQA_TEXT_DEV_PURPOSE=CHECKPOINT_SELECTION` remains the canonical quarantine mapping;
- its prior generic selection-capable status is not enough to make it a required scored primary slice;
- Spec 005 now explicitly prohibits using its five-question accuracy as the primary medical-quality floor or primary winner-selection score.

This is a pre-result clarification, not a post-result remapping. No candidate has been executed or scored.

## Consequence for Session 8 Q1/Q2

Q1 identified a missing compatible canonical MedXpertQA accuracy metric. Q2 froze how any corrective maintenance would have to be performed.

Q3 narrows the urgency and legitimate justification for that repair:

```text
MEDXPERTQA_ACCURACY_METRIC_REPAIR_GOVERNANCE=SESSION8_Q2_PRESERVED
MEDXPERTQA_ACCURACY_METRIC_REPAIR_IMPLEMENTATION_AUTHORITY=NONE
MEDXPERTQA_ACCURACY_METRIC_REPAIR_REQUIRED_TO_SCORE_TEXT_DEV_AS_PRIMARY_SELECTION=NO
MEDXPERTQA_ACCURACY_METRIC_REPAIR_ALONE_CAN_MAKE_TEXT_DEV_A_PRIMARY_QUALITY_FLOOR=NO
MEDXPERTQA_ACCURACY_METRIC_REPAIR_ALONE_CAN_MAKE_TEXT_DEV_A_WINNER_SELECTION_SLICE=NO

CORRECTIVE_MAINTENANCE_SHOULD_NOT_BE_JUSTIFIED_SOLELY_BY_PRIMARY_SCORING_OF_TEXT_DEV=YES
FUTURE_METRIC_REPAIR_REQUIRES_A_SEPARATELY_FROZEN_LEGITIMATE_CANONICAL_SCORING_USE=YES
```

A compatible accuracy metric may still be useful in a future separately governed role, for example external evaluation on a legitimately authorized MedXpertQA evaluation slice. Q3 does not decide that later use and does not cancel Q2's repair-governance contract.

## Primary-selection architecture consequence

After Q3, commandMed does **not** currently have a public benchmark slice that is simultaneously proven to satisfy all of the following:

1. exact immutable artifact/split identity;
2. selection-capable canonical purpose;
3. scientifically adequate breadth/sample role for primary medical-quality selection;
4. compatible canonical metric identity;
5. resolved contamination gate;
6. separately authorized payload access/execution.

Accordingly, the exact primary-selection manifest remains blocked. A later clarification must choose a legitimate pre-result evidence architecture rather than laundering a public test split into selection or overloading a five-example few-shot set.

Possible governance paths to evaluate later, without selecting one here, include:

- establish whether an already-registered public development asset such as HealthBench or PubMedQA can receive an explicit, defensible selection-purpose binding;
- define a separately governed dedicated development/selection suite with adequate scope and immutable identity;
- preserve MedXpertQA test strictly as external evaluation while using another predeclared development source for model selection.

No path is authorized by Q3.

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
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

## Session 8 progress

Acceptance of Q3 advances only bounded Session 8:

```text
CLARIFICATION_SESSION_8=3_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_8_STATUS=IN_PROGRESS

MEDXPERTQA_TEXT_DEV_SCIENTIFIC_ROLE_POLICY=
FEW_SHOT_DEV_NOT_PRIMARY_QUALITY_FLOOR

CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Q3 does not complete Session 8, does not complete the overall CLARIFY lifecycle, does not implement corrective maintenance, and does not authorize transition to PLAN.

## Remaining clarification scope

Remaining work includes the legitimate primary-selection evidence-source strategy; HealthBench/PubMedQA purpose and suitability if supportable; the minimum medical-quality evidence architecture and threshold methodology; whether any separately governed canonical metric repair is still needed for a legitimate scoring role; contamination-assessment access route and actual candidate-specific contamination evidence; exact component rights/privacy/license evidence; exact llama.cpp/build/tokenizer/instrumentation identities; numeric performance thresholds; thermal/energy/failure-signal details; secondary ranking order; exact-head independent review; and final clarification lifecycle closure.
