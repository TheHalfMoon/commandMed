# Spec 005 — Session 7 Q3 Contamination PASS Semantics

**Lifecycle:** CLARIFY ONLY
**Accepted question:** Session 7 — Q3
**Exact predecessor head:** `3377cb66c21a2caa6b620dc385442173a588d14e`
**Canonical metadata base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`
**Purpose:** determine whether canonical Spec 001 validation defines a scientific contamination PASS/unblock combination, without opening benchmark payloads, model weights, or candidate corpora.

> This artifact is metadata-only governance. No benchmark payload was opened, downloaded, copied, cached, or executed. No candidate corpus or model weight was accessed. It does not authorize model access, model-weight retrieval, model conversion, benchmark-payload access/execution, Private Gold access, provider/API generation, PHI/restricted-data access, gated-term acceptance, device execution, training, tournament execution, `PLAN`, Ready, or merge.

## Canonical evidence boundary

Canonical Spec 001 defines contamination as a metadata/evidence interface for later decontamination work. FR-007 explicitly requires metadata and validation rules for exact-content and semantic contamination risk, while stating that Spec 001 does not need to implement a production semantic-overlap model and must instead define the interface/evidence expected from later decontamination work.

The canonical status vocabularies are:

```text
EXACT_MATCH_STATUS_VALUES=
NOT_ASSESSED,PENDING,CHECKED_CLEAN,OVERLAP_FOUND,BLOCKED

SEMANTIC_OVERLAP_STATUS_VALUES=
NOT_ASSESSED,PENDING,ASSESSED_LOW_RISK,ASSESSED_HIGH_RISK,BLOCKED
```

Canonical `validate_contamination_records` enforces:

- valid enum membership;
- record identity and required string fields;
- evidence symmetry for substantive exact-match states `CHECKED_CLEAN`, `OVERLAP_FOUND`, and `BLOCKED`;
- evidence symmetry for substantive semantic states `ASSESSED_LOW_RISK`, `ASSESSED_HIGH_RISK`, and `BLOCKED`.

It does **not** map any exact/semantic status pair to a scientific `PASS`, selection-unblock, payload-access, or execution decision.

The canonical tests make that distinction observable:

- `CHECKED_CLEAN + ASSESSED_LOW_RISK` with a resolved evidence artifact validates successfully;
- `OVERLAP_FOUND + ASSESSED_HIGH_RISK` with a resolved evidence artifact also validates successfully;
- `NOT_ASSESSED` / `PENDING` may validate without an evidence artifact;
- substantive states without a resolved evidence artifact fail validation.

Therefore validator success means that a contamination metadata record is structurally/evidentially valid under Spec 001. It does not mean that the scientific contamination gate has passed.

## Accepted policy

`VALID_CONTAMINATION_RECORD_DOES_NOT_EQUAL_SELECTION_PASS` is frozen:

```text
CONTAMINATION_PASS_SEMANTICS_POLICY=VALID_CONTAMINATION_RECORD_DOES_NOT_EQUAL_SELECTION_PASS

CANONICAL_SPEC001_CONTAMINATION_SCOPE=INTERFACE_AND_EVIDENCE_VALIDATION
CANONICAL_VALIDATOR_DEFINES_SCIENTIFIC_PASS_COMBINATION=NO
CANONICAL_VALIDATOR_DEFINES_SELECTION_UNBLOCK=NO
CANONICAL_VALIDATOR_DEFINES_PAYLOAD_ACCESS_UNBLOCK=NO
CANONICAL_VALIDATOR_DEFINES_EXECUTION_UNBLOCK=NO

CHECKED_CLEAN_PLUS_ASSESSED_LOW_RISK_WITH_RESOLVED_EVIDENCE=
VALID_CONTAMINATION_RECORD
CHECKED_CLEAN_PLUS_ASSESSED_LOW_RISK_IS_SELECTION_PASS=
NOT_ESTABLISHED_BY_CANONICAL_SPEC001

OVERLAP_FOUND_PLUS_ASSESSED_HIGH_RISK_WITH_RESOLVED_EVIDENCE=
VALID_CONTAMINATION_RECORD
OVERLAP_FOUND_PLUS_ASSESSED_HIGH_RISK_IS_SELECTION_PASS=NO_CLAIM

NOT_ASSESSED_OR_PENDING_CAN_BE_EVIDENCE_FREE_VALID_RECORD=YES
NOT_ASSESSED_OR_PENDING_IS_CONTAMINATION_PASS=NO

SUBSTANTIVE_EXACT_MATCH_STATE_REQUIRES_RESOLVED_EVIDENCE_ARTIFACT=YES
SUBSTANTIVE_SEMANTIC_STATE_REQUIRES_RESOLVED_EVIDENCE_ARTIFACT=YES

VALIDATOR_SUCCESS_GRANTS_BENCHMARK_PAYLOAD_ACCESS=NO
VALIDATOR_SUCCESS_GRANTS_BENCHMARK_EXECUTION=NO
VALIDATOR_SUCCESS_GRANTS_CHECKPOINT_SELECTION=NO

EXACT_CONTAMINATION_SELECTION_PASS_RULE=UNRESOLVED
EXACT_CONTAMINATION_ACCESS_UNBLOCK_RULE=UNRESOLVED
SELF_INVENTED_PASS_STATUS_COMBINATION=PROHIBITED
INFERRED_PASS_FROM_ENUM_NAMES=PROHIBITED
INFERRED_PASS_FROM_TEST_RECORD_VALIDITY=PROHIBITED

UNTIL_SEPARATE_CANONICAL_PASS_RULE_EXISTS=
ALL_CONTAMINATION_STATUS_COMBINATIONS_NON_UNBLOCKING_FOR_SPEC005

FUTURE_PASS_RULE_MUST_BE_FROZEN_BEFORE_PAYLOAD_ACCESS=YES
FUTURE_PASS_RULE_MUST_BE_FROZEN_BEFORE_CANDIDATE_RESULTS=YES
FUTURE_PASS_RULE_MUST_BE_CANDIDATE_NEUTRAL=YES
FUTURE_PASS_RULE_MUST_BIND_EXACT_SLICE_IDENTITY=YES
FUTURE_PASS_RULE_MUST_BIND_EXACT_CANDIDATE_OR_CORPUS_IDENTITY=YES
FUTURE_PASS_RULE_MUST_REQUIRE_RESOLVED_EVIDENCE_FOR_SUBSTANTIVE_STATES=YES
FUTURE_PASS_RULE_MUST_DEFINE_TREATMENT_OF_OVERLAP_FOUND=YES
FUTURE_PASS_RULE_MUST_DEFINE_TREATMENT_OF_ASSESSED_LOW_RISK=YES
FUTURE_PASS_RULE_MUST_DEFINE_TREATMENT_OF_ASSESSED_HIGH_RISK=YES
FUTURE_PASS_RULE_MUST_DEFINE_TREATMENT_OF_BLOCKED=YES
FUTURE_PASS_RULE_MUST_DEFINE_TREATMENT_OF_NOT_ASSESSED_AND_PENDING=YES

MEDXPERTQA_TEXT_DEV_CONTAMINATION_DISPOSITION=INHERITED_CATALOG_NOT_ASSESSED
MEDXPERTQA_TEXT_DEV_CONTAMINATION_GATE=INCOMPLETE
MEDXPERTQA_TEXT_DEV_SELECTION_ELIGIBILITY=NO_WHILE_CONTAMINATION_GATE_INCOMPLETE
MEDXPERTQA_TEXT_DEV_PAYLOAD_ACCESS_ELIGIBILITY=NO
MEDXPERTQA_TEXT_DEV_EXECUTION_ELIGIBILITY=NO

BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
```

## Semantics

1. A valid contamination record and a contamination PASS decision are separate governance objects. Spec 001 implements the former, not the latter.
2. The canonical clean-looking pair `CHECKED_CLEAN + ASSESSED_LOW_RISK` is proven only to be validator-acceptable when evidence-bound. This Q3 does not promote it to a scientific PASS or selection-unblocking rule.
3. The canonical tests also accept an evidence-bound `OVERLAP_FOUND + ASSESSED_HIGH_RISK` record, proving that validation success cannot itself represent PASS semantics.
4. `NOT_ASSESSED` and `PENDING` are allowed evidence-free metadata states but remain non-passing for Spec 005 access/selection purposes.
5. Until a separate pre-result canonical decision defines a scientific PASS/unblock rule, no contamination status combination may activate benchmark payload access, execution, or checkpoint selection in Spec 005.
6. Any future PASS rule must be candidate-neutral as policy, while allowing evidence-bound scientific outcomes to differ by candidate/corpus where the evidence actually differs.
7. This Q3 does not assess any candidate corpus, does not create a decontamination report, and does not resolve MedXpertQA `Text/dev.jsonl` contamination.

## Session 7 progress

Acceptance of this question advances only bounded Session 7:

```text
CLARIFICATION_SESSION_7=3_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_7_STATUS=IN_PROGRESS

CONTAMINATION_PASS_SEMANTICS_POLICY=VALID_CONTAMINATION_RECORD_DOES_NOT_EQUAL_SELECTION_PASS
EXACT_CONTAMINATION_SELECTION_PASS_RULE=UNRESOLVED
MEDXPERTQA_TEXT_DEV_CONTAMINATION_GATE=INCOMPLETE

CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

This Q3 does not complete Session 7, does not complete the full clarification lifecycle, and does not authorize transition to `PLAN`.

## Remaining clarification scope

Remaining work includes a separately justified scientific contamination PASS/unblock rule if one is to exist; contamination dispositions for future executable benchmark slices; exact HealthBench/PubMedQA split-purpose binding if canonically supportable; exact primary-selection slice manifest and metric mapping; exact payload access routes and any future access authority; clinical/statistical threshold freeze; exact candidate component rights/privacy/license evidence; exact llama.cpp/build/tokenizer/instrumentation values; numeric performance thresholds; thermal/energy/failure-signal details; secondary ranking order; exact-head independent review; and final clarification lifecycle closure.
