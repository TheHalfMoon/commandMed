# E004 Registry Current-State Reconciliation V13 — 2026-09-02

**Spec:** 007 SFT V1  
**Task:** E004  
**Artifact class:** append-only global current-state reconciliation  
**Canonical base:** `c6cec35200b1a50638eab33dc722b6f3505a6ef1`  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation:** ABSENT_NOT_AUTHORIZED  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose and supersession

Reconcile the global E004 current view after canonical merge of PR #177 / `c6cec35200b1a50638eab33dc722b6f3505a6ef1`, which repaired the live Spec 007 task-ledger narrative to match already-canonical V10/V11 global evidence and the V12 research-engineering component frontier.

This record supersedes stale **current-state** narrative in `specs/README.md` and earlier registry/task summaries where they still describe the target runtime-evidence lane as `NOT_STARTED`, preserve the obsolete V7 frontier pointer as current, or imply that repository independent review remains a default gate.

Historical records remain immutable evidence of the state at their own canonical bases.

```text
PREVIOUS_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v11-2026-09-02.md
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v13-2026-09-02.md
COMPONENT_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v12-2026-09-02.md
V13_SUPERSEDES_V10_V11_ONLY_FOR_LATER_CURRENT_STATE=YES
V13_SUPERSEDES_V12_COMPONENT_STATE=NO
TASK_LEDGER_RECONCILIATION_PR=177
TASK_LEDGER_RECONCILIATION_MERGE=c6cec35200b1a50638eab33dc722b6f3505a6ef1
```

## 2. Completed canonical evidence must remain completed

The current view MUST preserve all of the following already-canonical transitions:

```text
E001=CLOSED_CANONICAL
E002=CLOSED_CANONICAL
E003=CLOSED_CANONICAL
E002_SOURCE_INTEGRITY_RUN=33183096268
E002_LOCAL_SOURCE_INTEGRITY=PASS_EPHEMERAL_EVIDENCE_ONLY
PERSISTENT_LOCAL_SOURCE_BUNDLE_PRESENT=NO

HISTORICAL_BUILD_RUN_ID=33187438094
HISTORICAL_BUILD_JOB_ID=98903988417
E004_BOUNDED_BUILD_EVIDENCE=PASS_ON_RUN_33187438094
AUTHORIZED_BUILD_MANUAL_RUN_ALLOWANCE_REMAINING=0
HISTORICAL_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0

REPAIRED_TARGET_RUNTIME_EVIDENCE_RESULT=PASS
REPAIRED_RUNTIME_RUN_ID=33434874024
REPAIRED_RUNTIME_JOB_ID=99628745384
REPAIRED_TARGET_RUNTIME_EVIDENCE_ATTEMPT_ALLOWANCE_REMAINING=0
REPAIRED_LLAMA_QUANTIZE_SHA256=18ff27aab20ab7b4e239ac847be7636fb8e182ac9d1474efa7c4cfc915bbb4fc

DIAGNOSTIC_RUN_ID=33507754943
DIAGNOSTIC_RUN_ATTEMPT=1
DIAGNOSTIC_JOB_ID=99855785119
DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
SECOND_DIAGNOSTIC_EXECUTION_AUTHORITY=NONE
A1_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
A2_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
B1_LLAMA_QUANTIZE_SHA256=1f5c96a6763656d439455fdd331097cd73e607031c19f465dedf0dd4cfadeca6
B2_LLAMA_QUANTIZE_SHA256=1f5c96a6763656d439455fdd331097cd73e607031c19f465dedf0dd4cfadeca6
HISTORICAL_TWO_HASH_SPLIT_REPRODUCED=NO
DIAGNOSTIC_DISPOSITION=ABSOLUTE_PATH_CONTEXT_AFFECTS_BYTES_BUT_DOES_NOT_REPRODUCE_HISTORICAL_SPLIT
REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
```

No rerun or retry is created by this reconciliation.

## 3. Execution-time identity-binding policy remains controlling

The accepted canonical policy and build-environment-equality amendment remain the future fail-closed mechanism for any separately authorized conversion subject:

```text
POLICY_ID=E004-EXECUTION-TIME-IDENTITY-BINDING-V1
EXECUTION_TIME_IDENTITY_BINDING_POLICY_DISPOSITION=ACCEPTED_FAIL_CLOSED_FOR_FUTURE_SEPARATELY_AUTHORIZED_CONVERSION
HISTORICAL_REPAIRED_HASH_RECONSTRUCTION_AS_MANDATORY_PRECONDITION=REMOVED_BY_POLICY
FUTURE_CONVERSION_TOOL_IDENTITY_MODE=SAME_SUBJECT_DOUBLE_BUILD_THEN_BIND
DOUBLE_BUILD_BUILD_ENVIRONMENT_MANIFEST_EQUAL=YES_REQUIRED
DOUBLE_BUILD_MISMATCH_DISPOSITION=ABORT_BEFORE_MODEL_BYTES
AUTOMATIC_RETRY_AFTER_MISMATCH=PROHIBITED
ALTERNATE_ENVIRONMENT_AFTER_MISMATCH=PROHIBITED
```

This resolves the historical-hash reconstruction policy blocker only. It creates no conversion subject, conversion authority, contamination authority, A15 activation, tournament execution, or training authority.

## 4. Repository review policy after FD-007

Founder decision `FD-007` and constitutional amendment 0.1.1 remain canonical.

```text
INDEPENDENT_REPOSITORY_REVIEW_REQUIRED_BY_DEFAULT=NO
EXACT_HEAD_REVIEW_REQUIRED_BY_DEFAULT=NO
MATERIAL_BLOCKER_NO_REVIEWER_SENTINEL_REQUIRED_BY_DEFAULT=NO
```

Deterministic repository qualification remains required where applicable:

```text
LIVE_BASE_HEAD_VERIFICATION=REQUIRED
BOUNDED_DIFF_VERIFICATION=REQUIRED
CI_AND_STATUS_CHECKS=REQUIRED_WHEN_APPLICABLE
UNRESOLVED_REVIEW_THREADS=REQUIRED_ZERO_WHEN_THREADS_EXIST
EVIDENCE_DEPENDENT_GATES=REMAIN_REQUIRED
EXECUTION_AUTHORITY_GATES=REMAIN_REQUIRED
```

FD-007 does not remove domain-qualified scientific, clinical, statistical, privacy, rights, governance, human-factor, or patient-facing human evidence requirements.

## 5. Founder reviewer-outreach decision remains unselected

The canonical decision surface remains:

`specs/007-sft-v1/e004-founder-reviewer-outreach-reauthorization-decision-request-2026-08-30.md`

No canonical record or attributable post-surface Founder response currently binds either exact decision class:

```text
FOUNDER_OUTREACH_DECISION=ABSENT_POST_CANONICAL_SURFACE
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
INITIAL_PRESCREEN_MESSAGES_AUTHORIZED_NOW=0
FOLLOW_UP_MESSAGES_AUTHORIZED_NOW=0
REVIEWER_CANDIDATE_CONTACT_EXECUTION=PROHIBITED
```

Generic continuation language, broad approval, repository mutation, or an instruction to finish the project is non-operative for this exact decision surface. PR #117 therefore remains controlling until a separately valid decision or another separately permitted evidence path changes that state.

## 6. Global scientific and governance blockers remain real

No later canonical evidence supplies PASS for the required T1/A2 clinical/statistical evidence or G1-G4 real governance evidence.

```text
EXACT_APPOINTED_REVIEWER_IDENTITIES=UNRESOLVED
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
BENIGN_CASE_OVER_TRIAGE_NUMERIC_THRESHOLD=NEEDS_CLINICAL_STATISTICAL_EVIDENCE
NUMERIC_THRESHOLD_OR_MARGIN_FREEZE=NO
NUMERIC_N_FREEZE=NO
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1

G1_A5_REAL_GATE_PASS=NO
G2_A6_REAL_GATE_PASS=NO
G3_A8_REAL_GATE_PASS=NO
G4_A12_REAL_GATE_PASS=NO
```

Repository bots, LLMs, static research, Founder self-attestation, or current-state reconciliation cannot impersonate these required evidence functions.

## 7. Persistent operational execution-subject bindings remain unresolved

Completed ephemeral source/build/runtime evidence does not create a persistent future conversion subject.

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
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
```

These are operational facts and separately gated authorities. They cannot be truthfully replaced by repository prose or generic approval.

## 8. Contamination, A1-A14, A15, E005, and training remain downstream

```text
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
A1_A14_EXACT_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
PROJECT_FINISHED=NO
```

No contamination assessment may be moved earlier merely to create progress. No E005 winner may be selected without the frozen tournament evidence required by the canonical ordering.

## 9. Research-engineering component frontier remains V12

For the exact bounded `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1` scope, V12 remains the component-specific current-state authority.

```text
COMPONENT_SCOPE_POLICY_IDENTITY=PASS_CANONICAL
COMPONENT_SCOPE_OFFLINE_ENFORCEMENT=PASS_CANONICAL_IMPLEMENTED
COMPONENT_REPOSITORY_REVIEW_GATE=REMOVED_BY_FD_007
COMPONENT_SHARED_TOOLCHAIN_RUNTIME_EVIDENCE=PASS_CANONICAL
COMPONENT_HISTORICAL_HASH_RECONSTRUCTION_POLICY_BLOCKER=REMOVED_BY_CANONICAL_POLICY
COMPONENT_EXTERNAL_CLINICAL_REVIEW_REQUIRED=NO
COMPONENT_EXTERNAL_STATISTICAL_REVIEW_REQUIRED=NO
COMPONENT_REAL_GUARD_EVIDENCE=ABSENT
COMPONENT_SPECIFIC_EXECUTION_SUBJECT_RUNTIME_BINDING=ABSENT
COMPONENT_CONVERSION_PREREQUISITES=INCOMPLETE
COMPONENT_CONTAMINATION_PREREQUISITES=INCOMPLETE
COMPONENT_RESOURCE_ACCESS_BINDINGS=INCOMPLETE
COMPONENT_SUCCESSOR_EXECUTION_AUTHORITY=NONE
COMPONENT_A15=ABSENT_NOT_AUTHORIZED
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
```

The component lane cannot be used to bypass its own exact execution-subject, contamination, resource, A1-A14-equivalent, A15, or separately applicable execution-authority prerequisites.

## 10. Repository convergence after PR #177

PR #177 repaired the live `specs/007-sft-v1/tasks.md` E004 narrative so that it no longer describes the repaired runtime evidence as `NOT_STARTED` and no longer points only to V7 as the live frontier.

`specs/README.md` still contains an older current-state block that predates V10/V11/V12 and PR #177. That block is now explicitly superseded for current E004 interpretation by V13 and the live task ledger. It remains historical text and must not be used to restore consumed execution allowances, obsolete runtime state, or superseded repository-review requirements.

```text
LIVE_TASK_LEDGER_E004_NARRATIVE=RECONCILED_BY_PR_177
README_STALE_E004_CURRENT_STATE_BLOCK=SUPERSEDED_FOR_CURRENT_INTERPRETATION
HISTORICAL_README_TEXT_DELETED=NO
AUTHORITY_EXPANSION_FROM_SUPERSESSION=NONE
```

## 11. Dependency-safe frontier

After PR #177 and this reconciliation, no currently available repository-only action can truthfully change a remaining real E004 prerequisite from incomplete to PASS under the controlling governance.

A real next transition requires new valid evidence or separately applicable authority, such as:

1. a valid post-canonical Founder selection on the reviewer-outreach decision surface, if that path is chosen;
2. qualified clinical/statistical review evidence sufficient for T1/A2 under the frozen governance profile;
3. real G1-G4 governance/rights/privacy/personnel/change-control evidence;
4. exact operational conversion-subject/resource bindings under a separately applicable authority path;
5. separately authorized contamination assessment and resulting evidence in dependency order;
6. a real exact A1-A14 PASS snapshot and separately authorized A15 activation before tournament execution.

None of those states may be inferred from generic continuation approval.

```text
NO_ELIGIBLE_REPOSITORY_ONLY_REAL_GATE_TRANSITION_AVAILABLE=YES
E004_COMPLETE=NO
TOURNAMENT_EVIDENCE_PACK=NOT_PRODUCED
E005_REACHABLE=NO
PROJECT_FINISHED=NO
```

## 12. Explicit exclusions

This reconciliation performs or authorizes none of the following:

- model/source-weight download, loading, conversion, quantization, or inference;
- benchmark or tournament execution;
- build/runtime/diagnostic rerun or retry;
- contamination assessment;
- A15 activation;
- external reviewer outreach, appointment, engagement, or scientific work;
- training, continued pretraining, SFT, LoRA, QLoRA, full fine-tuning, distillation, DPO, GRPO, RL, or QAT;
- Private Gold, PHI, restricted, or gated asset access;
- credential use or provider generation;
- procurement, payment, or spend.

## 13. Current authority boundary

```text
SAFE_FOR_PATIENT_USE=NO
CLINICALLY_VALIDATED=NO
CLINICAL_GRADE=NO
CLINICALLY_SUPERIOR=NO
DEPLOYMENT_READY=NO
RELEASE_READY=NO
PATIENT_BENEFIT_PROVEN=NO
SYSTEM_SAFETY_PASS=NO
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 14. Repository qualification under FD-007

Independent repository review is not required by default for this bounded current-state reconciliation. Before merge, verify exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation.
