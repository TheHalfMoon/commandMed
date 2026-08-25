# Spec 005 — Session 7 Q2 MedXpertQA Contamination Gate

**Lifecycle:** CLARIFY ONLY
**Accepted question:** Session 7 — Q2
**Exact predecessor head:** `89d3cb23f83637649d1471f3fd0919417fa5d3c6`
**Canonical metadata base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`
**Purpose:** bind the current contamination disposition of the selection-capable MedXpertQA text development slice without opening any benchmark payload or claiming a clean result that canonical evidence does not support.

> This artifact is metadata-only governance. No benchmark payload was opened, downloaded, copied, cached, or executed. No candidate training corpus was accessed. It does not authorize model access, model-weight retrieval, model conversion, benchmark-payload access/execution, Private Gold access, provider/API generation, PHI/restricted-data access, gated-term acceptance, device execution, training, tournament execution, `PLAN`, Ready, or merge.

## Canonical evidence boundary

Session 7 Q1 froze `MedXpertQA/Text/dev.jsonl` as `CHECKPOINT_SELECTION` purpose, while keeping payload access and execution unauthorized.

Canonical Spec 001 currently records the public benchmark contamination catalog as:

```text
CONTAMINATION_RECORD=public_benchmarks_catalog_v1
EVIDENCE_ARTIFACT_ID=NONE
EXACT_MATCH_STATUS=NOT_ASSESSED
SEMANTIC_OVERLAP_STATUS=NOT_ASSESSED
```

The record is an interface-only pre-experimental baseline. It states that formal assessment occurs downstream once candidate corpora are available. Canonical contamination governance also preserves the evidence-symmetry rule: substantive assessment states require a resolved evidence artifact; `NOT_ASSESSED` and `PENDING` are valid evidence-free states but are not proof of cleanliness.

MedXpertQA is canonically registered with `contamination_sensitivity=HIGH`, exact source revision `7e7c465a68eb2b866926bfa59c8c9d17a8daba65`, and exact `Text/dev.jsonl` / `Text/test.jsonl` split identities. Exact benchmark identity therefore exists, but exact contamination evidence for the text development slice does not.

Session 6 Q3 separately froze that contamination disposition is required before benchmark payload access. Therefore the current `NOT_ASSESSED` catalog state cannot be widened into access, execution, or selection eligibility.

## Accepted policy

`EXACT_SLICE_CONTAMINATION_EVIDENCE_REQUIRED_BEFORE_ACCESS_OR_SELECTION` is frozen:

```text
BENCHMARK_CONTAMINATION_GATE_POLICY=EXACT_SLICE_CONTAMINATION_EVIDENCE_REQUIRED_BEFORE_ACCESS_OR_SELECTION

CANONICAL_PUBLIC_BENCHMARK_CONTAMINATION_RECORD=public_benchmarks_catalog_v1
CANONICAL_PUBLIC_BENCHMARK_EXACT_MATCH_STATUS=NOT_ASSESSED
CANONICAL_PUBLIC_BENCHMARK_SEMANTIC_OVERLAP_STATUS=NOT_ASSESSED
CANONICAL_PUBLIC_BENCHMARK_EVIDENCE_ARTIFACT_ID=NONE

MEDXPERTQA_SOURCE_REVISION=7e7c465a68eb2b866926bfa59c8c9d17a8daba65
MEDXPERTQA_TEXT_DEV_ARTIFACT=Text/dev.jsonl
MEDXPERTQA_TEXT_DEV_PURPOSE=CHECKPOINT_SELECTION
MEDXPERTQA_TEXT_DEV_CONTAMINATION_DISPOSITION=INHERITED_CATALOG_NOT_ASSESSED
MEDXPERTQA_TEXT_DEV_SPLIT_SPECIFIC_CONTAMINATION_EVIDENCE=NONE
MEDXPERTQA_TEXT_DEV_CONTAMINATION_GATE=INCOMPLETE

MEDXPERTQA_TEXT_DEV_CHECKPOINT_SELECTION_PURPOSE=PRESERVED_BUT_INACTIVE
MEDXPERTQA_TEXT_DEV_PAYLOAD_ACCESS_ELIGIBILITY=NO
MEDXPERTQA_TEXT_DEV_EXECUTION_ELIGIBILITY=NO
MEDXPERTQA_TEXT_DEV_SELECTION_ELIGIBILITY=NO_WHILE_CONTAMINATION_GATE_INCOMPLETE

NOT_ASSESSED_MEANS_CLEAN=NO
NOT_ASSESSED_MEANS_CONTAMINATED=NO
NOT_ASSESSED_MEANS_INSUFFICIENT_EVIDENCE=YES
CATALOG_LEVEL_NOT_ASSESSED_CAN_BE_SELF_PROMOTED_TO_CLEAN=NO

FUTURE_CONTAMINATION_UNBLOCK_REQUIRES_RESOLVED_EVIDENCE_ARTIFACT=YES
FUTURE_CONTAMINATION_UNBLOCK_REQUIRES_EXACT_BENCHMARK_SLICE_IDENTITY=YES
FUTURE_CONTAMINATION_UNBLOCK_REQUIRES_EXACT_CANDIDATE_OR_CANDIDATE_CORPUS_BINDING=YES
FUTURE_CONTAMINATION_UNBLOCK_REQUIRES_REPRODUCIBLE_METHOD_IDENTITY=YES
FUTURE_CONTAMINATION_UNBLOCK_REQUIRES_CANONICAL_DISPOSITION_BEFORE_PAYLOAD_ACCESS=YES

FUTURE_EXACT_MATCH_AND_SEMANTIC_STATUS_COMBINATION_REQUIRED_FOR_PASS=YES
EXACT_PASS_STATUS_COMBINATION=NOT_YET_FROZEN

SAME_CONTAMINATION_ASSESSMENT_RULES_ACROSS_CANDIDATES=REQUIRED
CANDIDATE_SPECIFIC_EVIDENCE_RESULT=ALLOWED_ONLY_IF_EXACT_EVIDENCE_BOUND
CANDIDATE_SPECIFIC_CONTAMINATION_EXCEPTION=PROHIBITED
POST_RESULT_CONTAMINATION_RECLASSIFICATION_WITHOUT_NEW_CANONICAL_EVIDENCE=PROHIBITED

MEDXPERTQA_TEXT_TEST_PURPOSE=PUBLIC_EXTERNAL_EVAL
MEDXPERTQA_TEXT_TEST_CAN_SELECT_MODEL=NO
MEDXPERTQA_TEXT_TEST_CONTAMINATION_DISPOSITION=NOT_RESOLVED_BY_THIS_Q2

HEALTHBENCH_CONTAMINATION_DISPOSITION=NOT_RESOLVED_BY_THIS_Q2
PUBMEDQA_CONTAMINATION_DISPOSITION=NOT_RESOLVED_BY_THIS_Q2

BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
```

## Semantics

1. The current canonical public-benchmark contamination record is `NOT_ASSESSED` for both exact-match and semantic-overlap dimensions and carries no evidence artifact. This is an absence-of-assessment state, not evidence of cleanliness and not evidence of contamination.
2. MedXpertQA `Text/dev.jsonl` inherits that unresolved catalog state only as the current fail-closed baseline. It does not have a split-specific clean assessment.
3. Q1's `CHECKPOINT_SELECTION` purpose remains the correct purpose mapping, but the slice is not active for selection while the contamination gate is incomplete.
4. Because contamination disposition is a prerequisite to payload access under the already-frozen access policy, no MedXpertQA text-dev payload access may be authorized from the current state.
5. A future unblocking claim must bind a resolved evidence artifact to the exact MedXpertQA slice and the exact candidate or candidate-corpus identity being assessed, using a reproducible methodology identity.
6. This clarification does not invent the final acceptable exact-match/semantic-overlap status combination. That PASS combination remains to be frozen from canonical evidence before any access or execution activation.
7. Candidate-specific scientific results may differ only when exact evidence supports the difference; candidate-specific policy exceptions or unsupported reclassification are prohibited.
8. This Q2 does not resolve MedXpertQA test contamination, HealthBench contamination, or PubMedQA contamination.

## Session 7 progress

Acceptance of this question advances only bounded Session 7:

```text
CLARIFICATION_SESSION_7=2_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_7_STATUS=IN_PROGRESS

BENCHMARK_CONTAMINATION_GATE_POLICY=EXACT_SLICE_CONTAMINATION_EVIDENCE_REQUIRED_BEFORE_ACCESS_OR_SELECTION
MEDXPERTQA_TEXT_DEV_CONTAMINATION_DISPOSITION=INHERITED_CATALOG_NOT_ASSESSED
MEDXPERTQA_TEXT_DEV_CONTAMINATION_GATE=INCOMPLETE
MEDXPERTQA_TEXT_DEV_SELECTION_ELIGIBILITY=NO_WHILE_CONTAMINATION_GATE_INCOMPLETE

CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

This Q2 does not complete Session 7, does not complete the full clarification lifecycle, and does not authorize transition to `PLAN`.

## Remaining clarification scope

Remaining work includes the exact acceptable contamination PASS-status combination; contamination dispositions for any other future executable benchmark slices; exact HealthBench/PubMedQA split-purpose binding if canonically supportable; exact primary-selection slice manifest and metric mapping; exact payload access routes and any future access authority; clinical/statistical threshold freeze; exact candidate component rights/privacy/license evidence; exact llama.cpp/build/tokenizer/instrumentation values; numeric performance thresholds; thermal/energy/failure-signal details; secondary ranking order; exact-head independent review; and final clarification lifecycle closure.
