# Spec 005 — Session 7 Q5 Primary-Selection Contamination Consequence

**Lifecycle:** CLARIFY ONLY  
**Accepted question:** Session 7 — Q5  
**Exact predecessor head:** `ed2fc244f312b8f1b8595c581d38ef4004c40b7d`  
**Canonical metadata base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`  
**Purpose:** freeze the tournament-level consequence of contamination PASS/FAIL/BLOCKED/INCOMPLETE for a future required primary-selection slice without freezing the exact slice manifest, opening payloads, or authorizing execution.

> This artifact is documentation/governance only. No benchmark payload, contamination-assessment payload, candidate corpus, model weight, provider/API, Private Gold, PHI/restricted data, or gated asset was accessed. No model, benchmark, device, conversion, contamination scan, or training execution occurred. This Q5 does not authorize `PLAN`, Ready, merge, model access, benchmark access, contamination-assessment access, or tournament execution.

## Canonical tournament basis

Spec 004 already freezes the distinction between **decisive failure** and **incomplete evidence**:

- an observed safety hard-gate `FAIL` is decisively `DISQUALIFIED`; other complete candidates may remain selectable;
- lineage `PROHIBITED` or `REFERENCE_ONLY` may be decisively `DISQUALIFIED`;
- lineage `BLOCKED`, insufficient safety evidence, manifest mismatch, missing comparison evidence, or other unresolved/invalid evidence is `INCOMPLETE`;
- **any declared candidate that is `INCOMPLETE` forces tournament-level `NO_SELECTION`**;
- a decisively `DISQUALIFIED` candidate does not itself make other complete candidates incomplete;
- the harness must never choose from a subset created by missing evidence.

Session 7 Q4 separately froze contamination adjudication:

```text
ASSESSED_CLEAN -> PASS_CONTAMINATION_GATE_ONLY
OVERLAP_OR_HIGH_RISK -> FAIL_CONTAMINATION_GATE
BLOCKED -> BLOCKED_CONTAMINATION_GATE
PENDING / NOT_ASSESSED -> INCOMPLETE_CONTAMINATION_GATE
INVALID_EVIDENCE -> INVALID_EVIDENCE_INCOMPLETE
```

Q5 binds these two contracts without changing either one.

## Accepted policy

`DECISIVE_CONTAMINATION_FAIL_DISQUALIFIES_UNRESOLVED_FORCES_NO_SELECTION` is frozen:

```text
PRIMARY_SELECTION_CONTAMINATION_CONSEQUENCE_POLICY=
DECISIVE_CONTAMINATION_FAIL_DISQUALIFIES_UNRESOLVED_FORCES_NO_SELECTION

POLICY_APPLIES_ONLY_TO_FUTURE_MANIFEST_SLICES_MARKED_REQUIRED_PRIMARY_SELECTION=YES
EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
PRIMARY_SELECTION_MANIFEST_FREEZE_REMAINS_REQUIRED=YES

REQUIRED_PRIMARY_SLICE_CONTAMINATION_PASS=
CONTAMINATION_PREREQUISITE_SATISFIED_ONLY
REQUIRED_PRIMARY_SLICE_CONTAMINATION_FAIL=
CANDIDATE_DISQUALIFIED
REQUIRED_PRIMARY_SLICE_CONTAMINATION_BLOCKED=
CANDIDATE_INCOMPLETE
REQUIRED_PRIMARY_SLICE_CONTAMINATION_INCOMPLETE=
CANDIDATE_INCOMPLETE
REQUIRED_PRIMARY_SLICE_CONTAMINATION_INVALID_EVIDENCE=
CANDIDATE_INCOMPLETE

ANY_DECLARED_CANDIDATE_INCOMPLETE_ON_REQUIRED_PRIMARY_SLICE=
TOURNAMENT_NO_SELECTION
DECISIVELY_DISQUALIFIED_CANDIDATE_ALONE_FORCES_NO_SELECTION=NO
ALL_DECLARED_CANDIDATES_DISQUALIFIED=
TOURNAMENT_NO_SELECTION
ZERO_QUALIFIED_CANDIDATES=
TOURNAMENT_NO_SELECTION

OTHER_COMPLETE_CANDIDATES_MAY_REMAIN_SELECTABLE_AFTER_DECISIVE_CONTAMINATION_FAIL=YES
SELECTION_AFTER_DECISIVE_DISQUALIFICATION_REQUIRES_ALL_REMAINING_TOURNAMENT_GATES=YES

CANDIDATE_SPECIFIC_SUBSTITUTE_PRIMARY_SLICE=PROHIBITED
CANDIDATE_SPECIFIC_PRIMARY_MANIFEST=PROHIBITED
REQUIRED_SLICE_REMOVAL_AFTER_CONTAMINATION_RESULT=PROHIBITED
REQUIRED_SLICE_DOWNGRADE_TO_SECONDARY_AFTER_CONTAMINATION_RESULT=PROHIBITED
POST_RESULT_PRIMARY_MANIFEST_EDIT=PROHIBITED
POST_RESULT_PURPOSE_REMAPPING=PROHIBITED

SAME_REQUIRED_PRIMARY_SLICE_SET_ACROSS_CANDIDATES=YES
SAME_CONTAMINATION_ADJUDICATION_POLICY_ACROSS_CANDIDATES=YES
DECISIVE_OUTCOME_MAY_DIFFER_BY_CANDIDATE_ONLY_FROM_BOUND_EVIDENCE=YES

CONTAMINATION_FAIL_IS_DECISIVE_ONLY_WHEN_Q4_ADJUDICATION_RETURNS_FAIL=YES
BLOCKED_OR_INCOMPLETE_MUST_NOT_BE_COERCED_TO_DISQUALIFIED=YES
BLOCKED_OR_INCOMPLETE_MUST_NOT_BE_COERCED_TO_PASS=YES
MISSING_EVIDENCE_MUST_NOT_CREATE_A_SMALLER_SELECTABLE_CANDIDATE_SUBSET=YES

CONTAMINATION_PASS_GRANTS_BENCHMARK_PAYLOAD_ACCESS=NO
CONTAMINATION_PASS_GRANTS_CONTAMINATION_ASSESSMENT_ACCESS=NO
CONTAMINATION_PASS_GRANTS_BENCHMARK_EXECUTION=NO
CONTAMINATION_PASS_GRANTS_MODEL_EXECUTION=NO
CONTAMINATION_PASS_GRANTS_TOURNAMENT_EXECUTION=NO

BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
```

## Deterministic consequence mapping

For each candidate and each slice that the future frozen manifest marks as `REQUIRED_PRIMARY_SELECTION`:

```text
IF contamination_gate=PASS_CONTAMINATION_GATE_ONLY
THEN candidate_slice_state=CONTAMINATION_PREREQUISITE_SATISFIED
AND no new authority is created

ELSE IF contamination_gate=FAIL_CONTAMINATION_GATE
THEN candidate_state=DISQUALIFIED
AND that candidate cannot enter primary ranking

ELSE IF contamination_gate=BLOCKED_CONTAMINATION_GATE
OR contamination_gate=INCOMPLETE_CONTAMINATION_GATE
OR contamination_gate=INVALID_EVIDENCE_INCOMPLETE
THEN candidate_state=INCOMPLETE
AND tournament_state=NO_SELECTION
```

Once a candidate is decisively `DISQUALIFIED`, additional ranking evidence for that candidate cannot restore selectability. A disqualified candidate also cannot be replaced by another benchmark slice or removed from the manifest after results are known.

If one or more candidates are decisively disqualified but every non-disqualified declared candidate has complete evidence and passes all other frozen gates, the remaining complete candidates may be compared under the frozen tournament rules. If no candidate remains qualified, the result is `NO_SELECTION`.

If **any** candidate remains `INCOMPLETE` on a required primary slice, the tournament cannot select from the smaller complete subset; it must return `NO_SELECTION` until the missing/blocked evidence is resolved or a separately governed pre-result policy change is canonically adopted before execution. Post-result policy repair is prohibited.

## Why FAIL and INCOMPLETE differ

A Q4 contamination `FAIL` is a complete adverse scientific conclusion: exact overlap was found and/or semantic risk was assessed high under the predeclared evidence-bound rule. It is therefore analogous to a complete safety hard-gate failure: decisive evidence exists and the candidate can be disqualified.

`BLOCKED`, `PENDING`, `NOT_ASSESSED`, or invalid/missing evidence do not prove an adverse scientific conclusion. Treating them as disqualification would silently shrink the candidate set because evidence was absent; Spec 004 explicitly forbids winner selection from such an incomplete subset. They therefore remain `INCOMPLETE` and force `NO_SELECTION`.

## Manifest boundary

Q5 deliberately does **not** freeze the exact primary-selection slice manifest.

The current metadata establishes only that MedXpertQA `Text/dev.jsonl` has `CHECKPOINT_SELECTION` purpose and is potentially primary-selection eligible if every other gate passes. HealthBench and PubMedQA purpose mappings remain unresolved. Therefore declaring MedXpertQA as the sole primary slice here would be premature and would convert an unresolved scientific design choice into policy without evidence.

Before any real tournament selection execution, a later clarification must freeze:

- the exact ordered/set identity of all required primary-selection slices;
- exact immutable artifact identities;
- metric mapping for each slice;
- purpose/quarantine binding;
- any applicable semantic contamination method/threshold policy;
- the rule that the same required slice set applies to every candidate.

That later manifest freeze must occur before candidate results can influence the choice and may not be changed to rescue a candidate after contamination results.

## Current MedXpertQA consequence

No real tournament is active, and MedXpertQA `Text/dev.jsonl` is not yet frozen as a required primary-selection manifest member. Its current contamination evidence remains:

```text
MEDXPERTQA_TEXT_DEV_CONTAMINATION_DISPOSITION=INHERITED_CATALOG_NOT_ASSESSED
MEDXPERTQA_TEXT_DEV_SPLIT_SPECIFIC_CONTAMINATION_EVIDENCE=NONE
MEDXPERTQA_TEXT_DEV_CONTAMINATION_GATE=INCOMPLETE
MEDXPERTQA_TEXT_DEV_SELECTION_ELIGIBILITY=NO_WHILE_CONTAMINATION_GATE_INCOMPLETE
```

Q5 therefore produces **no candidate disqualification and no tournament result**. It freezes only how a future required-primary slice outcome will propagate once the primary manifest and evidence exist.

## Session 7 closeout

Acceptance of Q5 completes only bounded Session 7:

```text
CLARIFICATION_SESSION_7=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_7_STATUS=COMPLETE_BOUNDED_SESSION

PRIMARY_SELECTION_CONTAMINATION_CONSEQUENCE_POLICY=
DECISIVE_CONTAMINATION_FAIL_DISQUALIFIES_UNRESOLVED_FORCES_NO_SELECTION

CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Completion of Session 7 does **not** complete the overall CLARIFY lifecycle and does not authorize transition to `PLAN`.

## Remaining clarification scope

Remaining work includes the exact primary-selection slice manifest and metric mapping; any separately authorized contamination-assessment-only payload access route; actual candidate-specific contamination evidence; HealthBench/PubMedQA purpose binding if canonically supportable; clinical/statistical threshold freeze; exact component rights/privacy/license evidence; exact llama.cpp/build/tokenizer/instrumentation identities; numeric performance thresholds; thermal/energy/failure-signal details; secondary ranking order; exact-head independent review; and final clarification lifecycle closure.
