# Spec 005 — Session 7 Q1 Benchmark Purpose Mapping

**Lifecycle:** CLARIFY ONLY
**Accepted question:** Session 7 — Q1
**Exact predecessor head:** `eaafb5d7099c8030cb4e03e91615e0249cc6440c`
**Canonical metadata base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`
**Purpose:** freeze only the benchmark-purpose/selection mapping that is supportable from canonical Spec 001 quarantine and benchmark metadata without opening any benchmark payload.

> This artifact is metadata-only governance. No benchmark payload was opened, downloaded, copied, cached, or executed. It does not authorize model access, model-weight retrieval, model conversion, benchmark-payload access/execution, Private Gold access, provider/API generation, PHI/restricted-data access, gated-term acceptance, device execution, training, tournament execution, `PLAN`, Ready, or merge.

## Canonical evidence boundary

The canonical Spec 001 quarantine contract distinguishes purpose from registry `intended_use`:

- `CHECKPOINT_SELECTION` may select a model and accepts `MODEL_SELECTION_DEV_SET` and `PUBLIC_BENCHMARK_DEV_SPLITS`;
- `DEV` may select a model and accepts `VERIFIED_DEV_SPLIT` and held-out synthetic pilot cases;
- `PUBLIC_EXTERNAL_EVAL` cannot select a model and accepts public benchmark canonical test splits;
- registry `intended_use=DEVELOPMENT` is a benchmark-registry classification and is not by itself proof that an exact artifact is a canonical dev split.

The canonical benchmark registry currently proves:

- MedXpertQA is bound to exact Text/MM dev+test artifacts at immutable dataset revision `7e7c465a68eb2b866926bfa59c8c9d17a8daba65`;
- its `Text/dev.jsonl` is explicitly a dev split and `Text/test.jsonl` is explicitly a test split;
- the registry states that test splits are evaluation-only and any dev-split use for selection must enter the `DEV`/`CHECKPOINT_SELECTION` quarantine boundary;
- HealthBench Core, Consensus, Hard, and Professional are exact bound public `DEVELOPMENT` artifacts, but the canonical registry does not identify those exact artifacts as `VERIFIED_DEV_SPLIT`, `PUBLIC_BENCHMARK_DEV_SPLIT`, or canonical test splits;
- PubMedQA `data/ori_pqal.json` is an exact bound public `DEVELOPMENT` artifact, but the canonical registry does not identify that exact artifact as a `VERIFIED_DEV_SPLIT`, `PUBLIC_BENCHMARK_DEV_SPLIT`, or canonical test split.

Because Spec 005 is selecting a backbone, the explicit MedXpertQA text dev split maps to the selection-specific `CHECKPOINT_SELECTION` purpose rather than relying on the more generic `DEV` purpose. HealthBench and PubMedQA remain fail-closed until their exact split/purpose semantics are separately canonically bound; the registry word `DEVELOPMENT` is not widened into selection authority.

## Accepted policy

`SELECTION_PURPOSE_REQUIRES_EXPLICIT_SPLIT_SEMANTICS` is frozen:

```text
BENCHMARK_SELECTION_MAPPING_POLICY=SELECTION_PURPOSE_REQUIRES_EXPLICIT_SPLIT_SEMANTICS

REGISTRY_INTENDED_USE_DEVELOPMENT_IS_NOT_QUARANTINE_PURPOSE=YES
PUBLIC_DEVELOPMENT_LABEL_ALONE_CAN_SELECT_MODEL=NO
EXPLICIT_SPLIT_SEMANTICS_REQUIRED_FOR_SELECTION_CAPABLE_PURPOSE=YES
PURPOSE_AMBIGUITY=FAIL_CLOSED_NOT_EXECUTABLE

MEDXPERTQA_SOURCE_REVISION=7e7c465a68eb2b866926bfa59c8c9d17a8daba65
MEDXPERTQA_TEXT_DEV_ARTIFACT=Text/dev.jsonl
MEDXPERTQA_TEXT_DEV_PURPOSE=CHECKPOINT_SELECTION
MEDXPERTQA_TEXT_DEV_CAN_SELECT_MODEL=YES
MEDXPERTQA_TEXT_DEV_SELECTION_ROLE=PRIMARY_SELECTION_ELIGIBLE_IF_ALL_OTHER_GATES_PASS
MEDXPERTQA_TEXT_DEV_PAYLOAD_ACCESS=NOT_AUTHORIZED
MEDXPERTQA_TEXT_DEV_PAYLOAD_EXECUTION=NOT_AUTHORIZED

MEDXPERTQA_TEXT_TEST_ARTIFACT=Text/test.jsonl
MEDXPERTQA_TEXT_TEST_PURPOSE=PUBLIC_EXTERNAL_EVAL
MEDXPERTQA_TEXT_TEST_CAN_SELECT_MODEL=NO

MEDXPERTQA_MM_PURPOSE=SECONDARY_NON_RANKING_IF_SEPARATELY_AUTHORIZED
MEDXPERTQA_MM_CAN_SELECT_PRIMARY=NO

HEALTHBENCH_CORE_ARTIFACT=2025-05-07-06-14-12_oss_eval.jsonl
HEALTHBENCH_CONSENSUS_ARTIFACT=consensus_2025-05-09-20-00-46.jsonl
HEALTHBENCH_HARD_ARTIFACT=hard_2025-05-08-21-00-10.jsonl
HEALTHBENCH_PROFESSIONAL_ARTIFACT=healthbench_professional_eval.jsonl
HEALTHBENCH_REGISTRY_INTENDED_USE=DEVELOPMENT
HEALTHBENCH_PURPOSE_MAPPING=UNRESOLVED
HEALTHBENCH_SELECTION_ELIGIBILITY=NO_UNTIL_EXPLICIT_CANONICAL_SPLIT_PURPOSE_BINDING
HEALTHBENCH_EXECUTION_ELIGIBILITY=NO_WHILE_PURPOSE_UNRESOLVED

PUBMEDQA_ARTIFACT=data/ori_pqal.json
PUBMEDQA_ARTIFACT_BLOB=38db7750761c78950ed32303e7545bdaa513390c
PUBMEDQA_REGISTRY_INTENDED_USE=DEVELOPMENT
PUBMEDQA_PURPOSE_MAPPING=UNRESOLVED
PUBMEDQA_SELECTION_ELIGIBILITY=NO_UNTIL_EXPLICIT_CANONICAL_SPLIT_PURPOSE_BINDING
PUBMEDQA_EXECUTION_ELIGIBILITY=NO_WHILE_PURPOSE_UNRESOLVED

HEALTHBENCH_OR_PUBMEDQA_AUTOMATIC_DEV_MAPPING=PROHIBITED
HEALTHBENCH_OR_PUBMEDQA_AUTOMATIC_CHECKPOINT_SELECTION_MAPPING=PROHIBITED
HEALTHBENCH_OR_PUBMEDQA_AUTOMATIC_EXTERNAL_EVAL_MAPPING=PROHIBITED

SAME_PURPOSE_MAPPING_ACROSS_CANDIDATES=REQUIRED
CANDIDATE_SPECIFIC_PURPOSE_MAPPING=PROHIBITED
POST_RESULT_PURPOSE_PROMOTION_OR_REMAPPING=PROHIBITED

EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
```

## Semantics

1. MedXpertQA `Text/dev.jsonl` has explicit canonical dev-split semantics. Because Spec 005 uses it, if eventually authorized, to select a backbone, its Spec 005 quarantine purpose is `CHECKPOINT_SELECTION`. This purpose is selection-capable by canonical contract but grants no current payload access or execution authority.
2. MedXpertQA `Text/test.jsonl` remains `PUBLIC_EXTERNAL_EVAL` and cannot select a model.
3. MedXpertQA multimodal assets remain secondary non-ranking under `COMMON_CORE_PRIMARY_RANKING` and cannot select the primary backbone.
4. HealthBench Core/Consensus/Hard/Professional remain verified public development assets, but their exact artifacts are not canonically identified as dev splits or canonical test splits. Therefore this clarification does not guess `DEV`, `CHECKPOINT_SELECTION`, or `PUBLIC_EXTERNAL_EVAL`; their purpose remains unresolved and they are not executable/selectable while unresolved.
5. PubMedQA PQA-L remains a verified public development asset with exact artifact identity, but its canonical metadata likewise does not prove a dev/test split class compatible with the quarantine matrix. Its purpose remains unresolved and it is not executable/selectable while unresolved.
6. A future clarification may resolve HealthBench/PubMedQA only from explicit canonical split semantics or a separately reviewed canonical purpose binding made before payload access and before candidate results. It may not infer selection authority from `intended_use=DEVELOPMENT` alone.
7. No purpose may be changed per candidate or after observing results.

## Session 7 progress

Acceptance of this question advances only bounded Session 7:

```text
CLARIFICATION_SESSION_7=1_QUESTION_ACCEPTED
CLARIFICATION_SESSION_7_STATUS=IN_PROGRESS

BENCHMARK_SELECTION_MAPPING_POLICY=SELECTION_PURPOSE_REQUIRES_EXPLICIT_SPLIT_SEMANTICS
MEDXPERTQA_TEXT_DEV_PURPOSE=CHECKPOINT_SELECTION
HEALTHBENCH_PURPOSE_MAPPING=UNRESOLVED
PUBMEDQA_PURPOSE_MAPPING=UNRESOLVED

CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

This Q1 does not complete Session 7, does not complete the full clarification lifecycle, and does not authorize transition to `PLAN`.

## Remaining clarification scope

Remaining work includes the exact HealthBench/PubMedQA split-purpose binding if a canonical evidence basis can be established; exact primary-selection slice manifest and metric mapping; per-slice contamination dispositions; exact payload access routes and any future access authority; clinical/statistical threshold freeze; exact candidate component rights/privacy/license evidence; exact runtime/build/tokenizer/instrumentation values; numeric performance thresholds; thermal/energy/failure-signal details; secondary ranking order; exact-head independent review; and final clarification lifecycle closure.
