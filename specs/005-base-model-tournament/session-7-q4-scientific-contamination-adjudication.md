# Spec 005 — Session 7 Q4 Scientific Contamination Adjudication

**Lifecycle:** CLARIFY ONLY  
**Accepted question:** Session 7 — Q4  
**Exact predecessor head:** `433763604a89cb76880a1fd1ce82725017b4c824`  
**Canonical metadata base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`  
**Purpose:** freeze a candidate-neutral, evidence-bound scientific adjudication rule for benchmark contamination without opening any benchmark payload, candidate corpus, model weight, provider, or execution surface.

> This artifact is documentation/governance only. No benchmark payload, candidate training corpus, private Gold, model weight, provider/API, PHI/restricted data, or gated asset was accessed. No model, benchmark, device, conversion, or training execution occurred. This Q4 does not authorize `PLAN`, Ready, merge, benchmark payload access, contamination-assessment payload access, model access, model execution, or tournament execution.

## Canonical contract basis

Spec 001 deliberately separates exact-content contamination from semantic contamination. Its exact-match vocabulary includes `CHECKED_CLEAN` and `OVERLAP_FOUND`; its semantic vocabulary includes `ASSESSED_LOW_RISK` and `ASSESSED_HIGH_RISK`. Substantive states require resolved evidence artifacts, while `NOT_ASSESSED` and `PENDING` may remain evidence-free metadata states.

Session 7 Q3 established that Spec 001 record validation is not itself a scientific PASS rule.

Canonical Spec 003 then supplies the project-level contamination state vocabulary:

```text
NOT_ASSESSED
PENDING
ASSESSED_CLEAN
OVERLAP_OR_HIGH_RISK
BLOCKED
NOT_APPLICABLE
```

Spec 003 also freezes the fail-closed principle that unresolved contamination cannot be laundered into a clean-required use, and states that for a use requiring clean separation only `ASSESSED_CLEAN` (or evidence-backed `NOT_APPLICABLE` when truly outside the condition) may contribute to `ELIGIBLE`.

For Spec 005 public benchmark checkpoint selection, the contamination condition is inherently applicable; therefore `NOT_APPLICABLE` is not a valid shortcut for a candidate-vs-benchmark selection assessment.

## External scientific evidence basis

This Q4 uses external literature only to choose a conservative adjudication policy; it does not import benchmark payloads or execute any model.

1. Yang et al., **Rethinking Benchmark and Contamination for Language Models with Rephrased Samples** (arXiv:2311.04850), show that string/n-gram matching can miss paraphrased or translated benchmark contamination and motivate stronger semantic decontamination checks.
2. Deng et al., **Investigating Data Contamination in Modern Benchmarks for Large Language Models** (NAACL 2024, DOI `10.18653/v1/2024.naacl-long.482`), use both retrieval-based overlap investigation and model-behavior probing, supporting the need for more than one contamination signal when model training data are not fully transparent.
3. Singh et al., **Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?** (arXiv:2411.03923), report that contamination measurement is sensitive to method and hyperparameter choice and that model/benchmark-specific analysis improves specificity. This argues against inventing one universal numeric similarity threshold in this clarification.
4. Spiesberger et al., **Soft Contamination Means Benchmarks Test Shallow Generalization** (arXiv:2602.12413), report that semantic duplicates can remain after exact-match-style filtering and can affect benchmark performance, reinforcing a separate semantic-risk axis.

These sources support a fail-closed dual-axis rule. They do not establish a universal percentage threshold, so Q4 does not invent one.

## Accepted policy

`DUAL_AXIS_EVIDENCE_BOUND_FAIL_CLOSED_ADJUDICATION` is frozen:

```text
CONTAMINATION_ADJUDICATION_POLICY=DUAL_AXIS_EVIDENCE_BOUND_FAIL_CLOSED_ADJUDICATION

EXACT_AXIS_PASS_STATE=CHECKED_CLEAN
SEMANTIC_AXIS_PASS_STATE=ASSESSED_LOW_RISK

CONTAMINATION_GATE_PASS_REQUIRES_EXACT_AXIS_PASS=YES
CONTAMINATION_GATE_PASS_REQUIRES_SEMANTIC_AXIS_PASS=YES
CONTAMINATION_GATE_PASS_REQUIRES_RESOLVED_EVIDENCE=YES
CONTAMINATION_GATE_PASS_REQUIRES_EXACT_SLICE_BINDING=YES
CONTAMINATION_GATE_PASS_REQUIRES_EXACT_CANDIDATE_OR_CORPUS_BINDING=YES
CONTAMINATION_GATE_PASS_REQUIRES_REPRODUCIBLE_METHOD_IDENTITY=YES

CHECKED_CLEAN_PLUS_ASSESSED_LOW_RISK=ASSESSED_CLEAN_IF_ALL_EVIDENCE_REQUIREMENTS_PASS
ASSESSED_CLEAN_CONTAMINATION_GATE_OUTCOME=PASS_CONTAMINATION_GATE_ONLY

EXACT_OVERLAP_FOUND_OUTCOME=FAIL_CONTAMINATION_GATE
SEMANTIC_ASSESSED_HIGH_RISK_OUTCOME=FAIL_CONTAMINATION_GATE
KNOWN_ADVERSE_CONTAMINATION_COMPOSITE_STATE=OVERLAP_OR_HIGH_RISK

ANY_BLOCKED_WITHOUT_KNOWN_ADVERSE_STATE=BLOCKED_CONTAMINATION_GATE
ANY_PENDING_WITHOUT_KNOWN_ADVERSE_OR_BLOCKED_STATE=INCOMPLETE_CONTAMINATION_GATE
ANY_NOT_ASSESSED_WITHOUT_KNOWN_ADVERSE_OR_BLOCKED_OR_PENDING_STATE=INCOMPLETE_CONTAMINATION_GATE

SUBSTANTIVE_STATE_WITH_MISSING_OR_UNRESOLVED_EVIDENCE=INVALID_EVIDENCE_INCOMPLETE
NOT_APPLICABLE_FOR_PUBLIC_BENCHMARK_SELECTION=PROHIBITED

EXACT_CLEAN_ALONE_IS_PASS=NO
SEMANTIC_LOW_RISK_ALONE_IS_PASS=NO
VALID_RECORD_ALONE_IS_PASS=NO
MODEL_BEHAVIOR_PROBE_ALONE_CAN_PROVE_EXACT_CHECKED_CLEAN=NO

EXACT_MATCH_METHOD_MUST_DECLARE_COVERAGE=YES
EXACT_MATCH_METHOD_MUST_BIND_CORPUS_OR_AUTHORITATIVE_DECONTAMINATION_EVIDENCE=YES
PARTIAL_OR_UNKNOWN_TRAINING_CORPUS_COVERAGE_CAN_PROVE_CHECKED_CLEAN=NO

SEMANTIC_METHOD_MUST_BE_PREDECLARED=YES
SEMANTIC_METHOD_THRESHOLD_POLICY_MUST_BE_PREDECLARED=YES
UNIVERSAL_NUMERIC_SEMANTIC_THRESHOLD_FROZEN_BY_Q4=NO
BENCHMARK_SLICE_SPECIFIC_THRESHOLD_ALLOWED_IF_PREDECLARED_AND_JUSTIFIED=YES
CANDIDATE_SPECIFIC_THRESHOLD=PROHIBITED
POST_RESULT_THRESHOLD_CHANGE=PROHIBITED

ADJUDICATION_PRECEDENCE=KNOWN_ADVERSE_THEN_BLOCKED_THEN_PENDING_THEN_NOT_ASSESSED_THEN_ASSESSED_CLEAN

SAME_ADJUDICATION_RULE_ACROSS_CANDIDATES=REQUIRED
CANDIDATE_SPECIFIC_POLICY_EXCEPTION=PROHIBITED
EVIDENCE_BOUND_CANDIDATE_SPECIFIC_OUTCOME=ALLOWED
POST_RESULT_CONTAMINATION_RULE_CHANGE=PROHIBITED

CONTAMINATION_PASS_GRANTS_PAYLOAD_ACCESS=NO
CONTAMINATION_PASS_GRANTS_BENCHMARK_EXECUTION=NO
CONTAMINATION_PASS_GRANTS_MODEL_EXECUTION=NO
CONTAMINATION_PASS_GRANTS_CHECKPOINT_SELECTION_EXECUTION=NO
CONTAMINATION_PASS_SATISFIES_ONE_PREREQUISITE_ONLY=YES

BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
```

## Deterministic status-pair mapping

The following mapping is policy, not a claim about any current candidate:

```text
IF exact_match_status=OVERLAP_FOUND
OR semantic_overlap_status=ASSESSED_HIGH_RISK
THEN composite=OVERLAP_OR_HIGH_RISK
AND contamination_gate=FAIL

ELSE IF exact_match_status=BLOCKED
OR semantic_overlap_status=BLOCKED
THEN composite=BLOCKED
AND contamination_gate=BLOCKED

ELSE IF exact_match_status=PENDING
OR semantic_overlap_status=PENDING
THEN composite=PENDING
AND contamination_gate=INCOMPLETE

ELSE IF exact_match_status=NOT_ASSESSED
OR semantic_overlap_status=NOT_ASSESSED
THEN composite=NOT_ASSESSED
AND contamination_gate=INCOMPLETE

ELSE IF exact_match_status=CHECKED_CLEAN
AND semantic_overlap_status=ASSESSED_LOW_RISK
AND all evidence-binding requirements pass
THEN composite=ASSESSED_CLEAN
AND contamination_gate=PASS_CONTAMINATION_GATE_ONLY

ELSE
composite=BLOCKED
contamination_gate=INCOMPLETE_FAIL_CLOSED
```

A substantive status without its required evidence is evaluated as `INVALID_EVIDENCE_INCOMPLETE` before the pair mapping can produce PASS or FAIL.

## Evidence semantics

### Exact axis

`CHECKED_CLEAN` means only that the declared exact-overlap method found no disqualifying overlap within its explicitly bound coverage. It is not a metaphysical claim that no contamination exists anywhere.

For Spec 005, a model-output memorization probe alone cannot establish `CHECKED_CLEAN`, because the canonical Spec 001 exact-match interface is about overlap against candidate pretraining/SFT material. Exact-clean evidence must therefore bind either:

- the relevant immutable candidate training/adaptation corpus coverage being scanned; or
- an authoritative decontamination evidence artifact whose exact model, benchmark slice, method, corpus coverage, and immutable evidence identity are all resolved.

If material candidate training/adaptation corpus coverage is unknown or partial, `CHECKED_CLEAN` cannot be claimed from that direct-corpus route.

### Semantic axis

`ASSESSED_LOW_RISK` requires a reproducible, predeclared semantic-risk method and evidence artifact. The method may use a justified similarity/retrieval or contamination-detection protocol, but Q4 intentionally does not invent a universal numeric cutoff. Any future numeric threshold or calibration rule must be frozen before candidate results and applied identically across candidates for the same benchmark slice.

### Adverse evidence

A resolved `OVERLAP_FOUND` exact result or `ASSESSED_HIGH_RISK` semantic result is sufficient to fail the contamination gate for that candidate/slice. A known adverse finding is not diluted by an unresolved second axis.

A `BLOCKED`, `PENDING`, or `NOT_ASSESSED` state without known adverse evidence remains non-passing and non-unblocking.

## Selection consequences

For a primary-selection slice:

```text
FAIL_CONTAMINATION_GATE => CANDIDATE_SLICE_NOT_SELECTION_ELIGIBLE
BLOCKED_CONTAMINATION_GATE => CANDIDATE_SLICE_NOT_SELECTION_ELIGIBLE
INCOMPLETE_CONTAMINATION_GATE => CANDIDATE_SLICE_NOT_SELECTION_ELIGIBLE
PASS_CONTAMINATION_GATE_ONLY => CONTAMINATION_PREREQUISITE_SATISFIED_ONLY
```

Because prior policy requires an identical primary-selection slice manifest across candidates, a candidate may not receive a candidate-specific substitute benchmark merely because its contamination outcome is adverse or incomplete. Any tournament-level consequence of a missing required primary slice remains to be frozen with the exact primary-selection manifest; Q4 does not silently disqualify or select any current candidate.

## Current MedXpertQA state

Q4 changes the rule, not the evidence. The canonical evidence remains:

```text
MEDXPERTQA_TEXT_DEV_PURPOSE=CHECKPOINT_SELECTION
MEDXPERTQA_TEXT_DEV_CONTAMINATION_DISPOSITION=INHERITED_CATALOG_NOT_ASSESSED
MEDXPERTQA_TEXT_DEV_SPLIT_SPECIFIC_CONTAMINATION_EVIDENCE=NONE
MEDXPERTQA_TEXT_DEV_CONTAMINATION_GATE=INCOMPLETE
MEDXPERTQA_TEXT_DEV_SELECTION_ELIGIBILITY=NO_WHILE_CONTAMINATION_GATE_INCOMPLETE
MEDXPERTQA_TEXT_DEV_PAYLOAD_ACCESS_ELIGIBILITY=NO
MEDXPERTQA_TEXT_DEV_EXECUTION_ELIGIBILITY=NO
```

No MedXpertQA payload was opened and no candidate contamination assessment was performed.

## Session 7 progress

Acceptance of Q4 advances only bounded Session 7:

```text
CLARIFICATION_SESSION_7=4_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_7_STATUS=IN_PROGRESS

CONTAMINATION_ADJUDICATION_POLICY=DUAL_AXIS_EVIDENCE_BOUND_FAIL_CLOSED_ADJUDICATION
EXACT_CONTAMINATION_SELECTION_PASS_RULE=FROZEN_BY_SESSION_7_Q4
MEDXPERTQA_TEXT_DEV_CONTAMINATION_GATE=INCOMPLETE

CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

This Q4 does not complete Session 7, does not complete the full CLARIFY lifecycle, and does not authorize transition to `PLAN`.

## Remaining clarification scope

Remaining work includes the exact primary-selection slice manifest and tournament consequence when a required slice is contamination-failed/incomplete; any future contamination evidence acquisition/assessment-only access authority; HealthBench/PubMedQA purpose binding if canonically supportable; concrete MedXpertQA candidate-specific contamination evidence; clinical/statistical threshold freeze; exact component rights/privacy/license evidence; exact llama.cpp/build/tokenizer/instrumentation values; numeric performance thresholds; thermal/energy/failure-signal details; secondary ranking order; exact-head independent review; and final clarification lifecycle closure.
