# E004 Registry Current-State Reconciliation V10 — 2026-09-02

**Spec:** 007 SFT V1  
**Task:** E004  
**Artifact class:** append-only post-policy current-state reconciliation  
**Canonical base:** `071cf1ca92f7f1d7d4cea3c0bccd478f4208e2c1`  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation:** ABSENT_NOT_AUTHORIZED  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Reconcile the exact E004 current view after canonical merge of PR #172 / `071cf1ca92f7f1d7d4cea3c0bccd478f4208e2c1`.

Older E004 registry/task narrative predates later canonical source-integrity, build-evidence, repaired-runtime, rebuild-diagnostic, result-reconciliation, and policy-disposition evidence. This record supersedes only stale **current-state narrative**. It does not alter historical records, change the E004 task checkbox, create execution authority, or convert absent scientific, governance, personnel, resource, contamination, activation, or training evidence into PASS.

```text
E001=CLOSED_CANONICAL
E002=CLOSED_CANONICAL
E003=CLOSED_CANONICAL
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
PROJECT_FINISHED=NO
```

## 2. Completed canonical E004 evidence transitions

The current view MUST NOT describe the following transitions as `NOT_STARTED`, and MUST NOT restore an already consumed execution allowance.

### 2.1 E002 local source-integrity evidence

Controlling evidence:

`specs/007-sft-v1/e004-e002-local-source-integrity-run-evidence-2026-08-28.md`

```text
E002_SOURCE_INTEGRITY_RUN=33183096268
GRANITE_LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_EPHEMERAL_EVIDENCE_ON_RUN_33183096268
QWEN_LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_EPHEMERAL_EVIDENCE_ON_RUN_33183096268
LOCAL_SELECTED_NON_WEIGHT_INPUT_SHA256_SET=RECOMPUTED_AND_MATCHED_ON_RUN_33183096268
LOCAL_SOURCE_DIRECTORY_BASENAME_ATTESTATION=PASS_ON_RUN_33183096268
PERSISTENT_LOCAL_SOURCE_BUNDLE_PRESENT=NO
```

The validated source bytes were ephemeral and were intentionally not persisted.

### 2.2 Bounded llama-quantize build evidence

Controlling build evidence and later canonical policy retain:

```text
HISTORICAL_BUILD_RUN_ID=33187438094
HISTORICAL_BUILD_JOB_ID=98903988417
E004_BOUNDED_BUILD_EVIDENCE=PASS_ON_RUN_33187438094
AUTHORIZED_BUILD_MANUAL_RUN_ALLOWANCE_REMAINING=0
HISTORICAL_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
HISTORICAL_LLAMA_QUANTIZE_INTEGER_BYTES=6513680
HISTORICAL_CMAKE_CACHE_SHA256=0b499b1dfa63d0f3fcf80cb3c0f45b25b95de2b5cd128574cc3d1e5f49ad0599
HISTORICAL_COMPILE_COMMANDS_SHA256=567ad70c6090af9fcce508c41eddba51681669f1079e52e6c285c5cc471d713e
```

No build-evidence rerun is authorized by this reconciliation.

### 2.3 Repaired target runtime evidence

Controlling evidence:

`specs/007-sft-v1/e004-repaired-target-runtime-evidence-result-reconciliation-2026-09-01.md`

and the later runtime reconstruction reconciliation/policy.

```text
REPAIRED_TARGET_RUNTIME_EVIDENCE_RESULT=PASS
REPAIRED_TARGET_RUNTIME_EVIDENCE_ATTEMPT_ALLOWANCE_REMAINING=0
REPAIRED_RUNTIME_RUN_ID=33434874024
REPAIRED_RUNTIME_JOB_ID=99628745384
REPAIRED_LLAMA_QUANTIZE_SHA256=18ff27aab20ab7b4e239ac847be7636fb8e182ac9d1474efa7c4cfc915bbb4fc
REPAIRED_LLAMA_QUANTIZE_INTEGER_BYTES=6513680
REPAIRED_CMAKE_CACHE_SHA256=5a2f8b139183dfba6d422db476cd8ad1b69388749199d909055744c082532bc3
RUNTIME_EVIDENCE_MANIFEST_SHA256=6f3e91fd162db6fd764a5915d34b50254cc91a07906eb602f833b02ff6dfb25d
AUTOMATIC_TARGET_RETRY_AUTHORITY=NONE
FAILED_TARGET_JOB_RERUN_AUTHORITY=NONE
SECOND_NEW_TARGET_ATTEMPT_AUTHORITY=NONE
```

This PASS proves the bounded ephemeral runtime-evidence attempt only. It does not create a persistent conversion subject or conversion-execution authority.

### 2.4 Consumed one-shot rebuild reproducibility diagnostic

Controlling authority and result reconciliation:

- `specs/007-sft-v1/e004-rebuild-reproducibility-diagnostic-authority-2026-09-01.md`
- `specs/007-sft-v1/e004-rebuild-reproducibility-diagnostic-result-reconciliation-2026-09-01.md`

```text
DIAGNOSTIC_RUN_ID=33507754943
DIAGNOSTIC_RUN_ATTEMPT=1
DIAGNOSTIC_JOB_ID=99855785119
DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
SECOND_DIAGNOSTIC_EXECUTION_AUTHORITY=NONE
A1_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
A2_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
B1_LLAMA_QUANTIZE_SHA256=1f5c96a6763656d439455fdd331097cd73e607031c19f465dedf0dd4cfadeca6
B2_LLAMA_QUANTIZE_SHA256=1f5c96a6763656d439455fdd331097cd73e607031c19f465dedf0dd4cfadeca6
A1_A2_BYTE_DIFFERENCE_COUNT=0
B1_B2_BYTE_DIFFERENCE_COUNT=0
A_B_BYTE_DIFFERENCE_COUNT=760129
HISTORICAL_TWO_HASH_SPLIT_REPRODUCED=NO
DIAGNOSTIC_DISPOSITION=ABSOLUTE_PATH_CONTEXT_AFFECTS_BYTES_BUT_DOES_NOT_REPRODUCE_HISTORICAL_SPLIT
REBUILD_BINARY_REPRODUCIBILITY_AGAINST_HISTORICAL_REPAIRED_HASH=NOT_PROVEN
REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
```

PR #168 canonically reconciled this consumed diagnostic. No second diagnostic occurred and none is authorized.

## 3. PR #172 policy is canonical but does not create conversion authority

Controlling policy:

`specs/007-sft-v1/e004-execution-time-identity-binding-policy-disposition-2026-09-02.md`

```text
POLICY_ID=E004-EXECUTION-TIME-IDENTITY-BINDING-V1
EXECUTION_TIME_IDENTITY_BINDING_POLICY_DISPOSITION=ACCEPTED_FAIL_CLOSED_FOR_FUTURE_SEPARATELY_AUTHORIZED_CONVERSION
HISTORICAL_REPAIRED_HASH_RECONSTRUCTION_AS_MANDATORY_PRECONDITION=REMOVED_BY_POLICY
FUTURE_CONVERSION_TOOL_IDENTITY_MODE=SAME_SUBJECT_DOUBLE_BUILD_THEN_BIND
```

The accepted policy removes reconstruction of the historical repaired binary hash as a mandatory future execution precondition. It does **not** prove the historical mismatch cause, historical binary equivalence, or general build reproducibility.

Any future separately authorized conversion subject adopting the policy must freeze its exact execution-subject bindings and satisfy the fail-closed same-subject double-build, build-environment/build-manifest equality, pre-use identity, and post-use completion gates required by that policy before its result can be accepted.

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 4. Persistent operational conversion-subject prerequisites remain unresolved

The completed ephemeral evidence does not create a persistent future conversion subject.

```text
PERSISTENT_LOCAL_SOURCE_BUNDLE_PRESENT=NO
EXACT_FUTURE_CONVERSION_SOURCE_DIRECTORY=NEEDS_EVIDENCE
EXACT_FUTURE_OUTPUT_DIRECTORY=NEEDS_EVIDENCE
EXACT_FUTURE_CONVERSION_ARGV=NEEDS_EVIDENCE
EXACT_FUTURE_QUANTIZE_ARGV=NEEDS_EVIDENCE
EXACT_STORAGE_BOUNDARY_IDENTITY=NEEDS_EVIDENCE
RETENTION_ENFORCEMENT_IDENTITY=NEEDS_EVIDENCE
EXACT_COMPUTE_RESOURCE_IDENTITY=NEEDS_EVIDENCE
RESOURCE_AUTHORIZATION_BASIS=NEEDS_EVIDENCE
EXPECTED_CPU_RAM_DISK_ENVELOPE=NEEDS_EVIDENCE
EXPECTED_MAX_WALLCLOCK=NEEDS_EVIDENCE
ZERO_INCREMENTAL_SPEND_DISPOSITION=NEEDS_EVIDENCE
CONVERSION_PHASE_NETWORK_BOUNDARY=NEEDS_EXACT_FUTURE_SUBJECT_BINDING
CONVERSION_PHASE_CREDENTIAL_ATTESTATION=NEEDS_EXACT_FUTURE_SUBJECT_BINDING
```

Those identities cannot be fabricated from historical ephemeral paths or generic continuation approval.

## 5. Scientific T1/A2 remains incomplete

The dependency-ordered scientific chain remains:

```text
R1_A1 -> T1_A2 -> D34_A3_A4 -> H1_A7 -> F1_A14
```

Canonical preparation exists, but no repository-only substitute closes T1/A2:

```text
A2_PUBLIC_RESEARCH=PREPARED
A2_STATISTICAL_METHOD_PACKET=CANONICAL_PREPARED
A2_REVIEW_GOVERNANCE_PROFILE=CANONICAL_PREPARED
EXACT_APPOINTED_REVIEWER_IDENTITIES=UNRESOLVED
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
BENIGN_CASE_OVER_TRIAGE_NUMERIC_THRESHOLD=NEEDS_CLINICAL_STATISTICAL_EVIDENCE
NUMERIC_THRESHOLD_OR_MARGIN_FREEZE=NO
NUMERIC_N_FREEZE=NO
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1
```

Repository bots, LLMs, static research, CodeRabbit, Qodo, Cubic, or Founder self-attestation do not satisfy the required qualified clinical/statistical reviewer functions.

## 6. Reviewer outreach decision remains unselected

Controlling decision surface:

`specs/007-sft-v1/e004-founder-reviewer-outreach-reauthorization-decision-request-2026-08-30.md`

The surface requires an explicit, attributable, post-canonical Founder selection of exactly one decision class:

```text
FOUNDER_OUTREACH_DECISION=E004_OUTREACH_DECISION_A
```

or

```text
FOUNDER_OUTREACH_DECISION=E004_OUTREACH_DECISION_B
```

No such operative selection is currently canonical. Generic continuation, approval, or an instruction to finish the project is explicitly non-operative for this decision surface.

```text
FOUNDER_OUTREACH_DECISION=ABSENT_POST_CANONICAL_SURFACE
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
INITIAL_PRESCREEN_MESSAGES_AUTHORIZED_NOW=0
FOLLOW_UP_MESSAGES_AUTHORIZED_NOW=0
REVIEWER_CANDIDATE_CONTACT_EXECUTION=PROHIBITED
```

No reviewer appointment or scientific-review authority is inferred.

## 7. G1-G4 real governance evidence remains absent

Existing candidate prose and repository review do not equal operational governance adoption.

```text
G1_A5_REAL_GATE_PASS=NO
G2_A6_REAL_GATE_PASS=NO
G3_A8_REAL_GATE_PASS=NO
G4_A12_REAL_GATE_PASS=NO
COMPONENT_REAL_GUARD_EVIDENCE=ABSENT
```

Required real evidence includes, as applicable, independent governance/privacy review, canonical policy adoption, rights acceptance, non-PHI attestations, real author/reviewer assignments and dispositions, and operational change-control bindings. Repository bot review cannot impersonate those functions.

## 8. Contamination, exact A1-A14 PASS snapshot, and A15 remain downstream

```text
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
COMPONENT_A1_A14_EQUIVALENT_EXACT_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
```

No contamination assessment may be moved earlier merely to create progress. The canonical dependency graph remains fail closed.

## 9. Connected GitHub execution surface recheck

The currently connected GitHub surface exposes repository/PR/workflow reads and ordinary repository mutation operations, but no fresh `workflow_dispatch` initiation action was exposed by connector discovery on 2026-09-02.

```text
CONNECTED_GITHUB_FRESH_WORKFLOW_DISPATCH_ACTION_AVAILABLE=NO
HISTORICAL_RERUN_AS_SUBSTITUTE=PROHIBITED
ALTERNATE_TRIGGER_AS_SUBSTITUTE=PROHIBITED
```

This does not invalidate completed source-integrity/build/runtime/diagnostic evidence. It matters only if a later separately authorized action requires an exact fresh workflow dispatch unavailable on the connected surface.

## 10. Current dependency-safe frontier

After the completed internal evidence chain and accepted execution-time identity-binding policy, no remaining repository-only action can truthfully transition an E004 real prerequisite from incomplete to PASS under current governance.

A real E004 transition requires at least one dependency-correct change such as:

1. an exact post-canonical Founder selection on the reviewer-outreach decision surface, followed only by the separately bounded contact steps that selection authorizes;
2. qualified clinical/statistical review evidence sufficient to support the required numeric T1/A2 policy under the frozen governance profile;
3. real G1-G4 governance/rights/privacy/personnel/change-control evidence through an authorized path;
4. other exact canonical evidence that independently satisfies the same frozen gates without weakening them.

A future conversion execution-subject authority remains downstream of the applicable scientific, governance, contamination, A1-A14, and A15 prerequisites and is not created here.

```text
FURTHEST_CURRENT_INTERNAL_ONLY_STATE=E004_BLOCKED_PREFLIGHT_POST_POLICY
NO_ELIGIBLE_REPOSITORY_ONLY_REAL_GATE_TRANSITION_AVAILABLE=YES
E004_COMPLETE=NO
TOURNAMENT_EVIDENCE_PACK=NOT_PRODUCED
E005_REACHABLE=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
PROJECT_FINISHED=NO
```

## 11. Supersession boundary

This V10 record supersedes only stale **current-state narrative** in earlier E004 frontier/registry/task descriptions where they describe source-integrity, build-evidence, repaired runtime evidence, the rebuild diagnostic, or the execution-time identity-binding policy as not yet completed.

Historical statements remain evidence of the state at their canonical bases. V10 neither edits their historical meaning nor changes task completion/authority.

## 12. Explicit exclusions

This reconciliation performs or authorizes none of the following:

- model/source-weight download, loading, conversion, quantization, or inference;
- benchmark or tournament execution;
- any rerun/retry of historical build/runtime/diagnostic jobs;
- a second rebuild diagnostic or binary-localization experiment;
- contamination assessment;
- A15 activation;
- training, gradient updates, distillation, DPO, RL, or QAT;
- Private Gold, PHI, restricted, or gated asset access;
- credential use or provider generation;
- external reviewer outreach, appointment, engagement, or scientific review;
- paid/larger runner use, procurement, payment, or spend;
- clinical, deployment, release, superiority, SOTA, or safety claims.

## 13. Merge-exit evidence

This record may become canonical only after fresh independent exact-head review verifies at least:

```text
EXACT_CANONICAL_BASE_MATCHES_BRANCH_CREATION_MAIN=YES
COMPLETED_E002_SOURCE_INTEGRITY_EVIDENCE_RETAINED_EXACTLY=YES
COMPLETED_BUILD_EVIDENCE_RETAINED_EXACTLY=YES
COMPLETED_REPAIRED_RUNTIME_EVIDENCE_RETAINED_EXACTLY=YES
CONSUMED_DIAGNOSTIC_IDENTITY_AND_NO_RERUN_BOUNDARY_RETAINED_EXACTLY=YES
PR168_RECONCILIATION_EFFECT_RETAINED_EXACTLY=YES
PR172_POLICY_EFFECT_RETAINED_EXACTLY=YES
HISTORICAL_REBUILD_MISMATCH_CAUSE_REMAINS_NEEDS_EVIDENCE=YES
OUTREACH_DECISION_REMAINS_ABSENT_POST_CANONICAL_SURFACE=YES
GENERIC_CONTINUATION_NOT_TREATED_AS_OUTREACH_DECISION=YES
T1_A2_REAL_REVIEW_AND_NUMERIC_POLICY_REMAIN_INCOMPLETE=YES
G1_G4_REAL_GOVERNANCE_EVIDENCE_REMAINS_ABSENT=YES
CONTAMINATION_AUTHORITY_CREATED=NO
A15_AUTHORITY_CREATED=NO
MODEL_CONVERSION_AUTHORITY_CREATED=NO
TRAINING_AUTHORITY_CREATED=NO
SPEND_AUTHORITY_CREATED=NO
E004_REMAINS_UNCHECKED_BLOCKED_PREFLIGHT=YES
E005_REMAINS_NOT_REACHED=YES
PROJECT_FINISHED_REMAINS_NO=YES
CHANGED_PATH_COUNT=1
MATERIAL_BLOCKER=NO
```

Any material blocker must be repaired on a new exact head and independently re-reviewed. Self-review is not sufficient.