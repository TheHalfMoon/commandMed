# E004 Successor-Scope Execution Authorization Decision Request — 2026-09-02

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical base:** `af4662c4f8fdddf8b0a6d50b109a230f725b52f6`  
**Artifact class:** Founder decision request only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**Model execution performed:** NO  
**Tournament execution performed:** NO  
**Training performed:** NO  
**Spend:** USD 0

## 1. Purpose

Resolve one exact authority gap identified by canonical component reconciliation without silently broadening historical E003 authority.

Controlling records:

- `e003-live-tournament-execution-authorization-2026-08-27.md`
- `e004-founder-research-only-no-external-reviewer-decision-2026-08-31.md`
- `e004-research-only-safety-policy-successor-2026-08-31.md`
- `e004-registry-current-state-reconciliation-v8-2026-08-31.md`
- `e004-registry-current-state-reconciliation-v12-2026-09-02.md`
- `e004-registry-current-state-reconciliation-v13-2026-09-02.md`
- `e004-research-component-execution-preflight-blocker-packet-2026-09-02.md`

V8 explicitly preserves historical E003 authority while requiring exact reconciliation or separate authority for the materially different successor qualification scope:

```text
HISTORICAL_E003_AUTHORITY_RETAINED=YES
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY_INFERRED_FROM_E003=NO
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=NEEDS_EXACT_RECONCILIATION_OR_SEPARATE_AUTHORITY
```

This decision request creates no authority by itself.

## 2. Frozen candidate boundary inherited from E001/E002

Any Decision B authority would remain limited to the exact already-frozen E001 candidate identities and E002 public/ungated access boundary.

### PRIMARY

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
```

### CONTROL

```text
Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_WINNER_ELIGIBLE=NO
CONTROL_PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
```

No candidate or revision is added by this surface.

## 3. Decision classes

The Founder must select exactly one decision class after this decision surface becomes canonical.

### `E004_SUCCESSOR_EXECUTION_DECISION_A` — preserve current authority state

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_A
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=NONE
SUCCESSOR_SCOPE_MODEL_EXECUTION_AUTHORITY=NONE
SUCCESSOR_SCOPE_TOURNAMENT_EXECUTION_AUTHORITY=NONE
SUCCESSOR_SCOPE_DEVICE_EXECUTION_AUTHORITY=NONE
```

Effect: component E004 remains blocked on successor-scope execution authority in addition to every other unresolved preflight prerequisite.

### `E004_SUCCESSOR_EXECUTION_DECISION_B` — authorize bounded research-only evidence execution after PASS preflight

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
SUCCESSOR_SCOPE_MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E001_FROZEN_CANDIDATES_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_FROZEN_NONCLINICAL_PROTOCOL_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_ONLY_WHERE_REQUIRED_BY_EXACT_FROZEN_COMPONENT_QUALIFICATION_AFTER_PASS_PREFLIGHT
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B would authorize **evidence-producing model execution only** for the exact `SP007-RO-001` research-engineering component after all applicable preflight gates are actually PASS.

It would not make those gates PASS and would not authorize execution while any applicable prerequisite remains `BLOCKED`, `INCOMPLETE`, `NEEDS_EVIDENCE`, stale, mismatched, or unauthorized.

## 4. Decision B exact execution boundary

Decision B would permit only the following after an exact PASS preflight:

- load an already E002-authorized exact frozen candidate artifact whose identity is bound before use;
- execute model inference required by the frozen `SP007-RO-001` non-clinical research-component qualification protocol;
- execute the exact seven identity-bound research-component policy/sentinel fixtures;
- execute public/ungated non-clinical evaluation assets whose exact provenance/license/quarantine/contamination identities have already passed the applicable gates;
- capture raw outputs and deterministic evaluator records needed by the component evidence pack;
- compute frozen non-clinical component metrics and guard dispositions;
- execute exact zero-spend device/runtime qualification only when required by the frozen component protocol and separately bound resource preflight;
- produce immutable identity-bound component evidence records.

Decision B does not authorize a favorable result. Any applicable failure remains a hard fail under the canonical successor policy.

## 5. Non-clinical claim boundary

Decision B would remain constrained by `SP007-RO-001`:

```text
SUCCESSOR_SCOPE_ID=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
SUCCESSOR_SCOPE_CLAIM_CLASS=NON_CLINICAL_RESEARCH_ENGINEERING_ONLY
ADMITTED_ROLE_CLASSES=LEARNER_RESEARCHER
PATIENT_CAREGIVER_ROLE_ADMITTED=NO
CLINICAL_PROFESSIONAL_ROLE_ADMITTED=NO
COMPONENT_EXTERNAL_CLINICAL_REVIEW_REQUIRED=NO
COMPONENT_EXTERNAL_STATISTICAL_REVIEW_REQUIRED=NO
```

Decision B cannot create or support patient-facing, clinical-professional, clinical-grade, clinical-safety, deployment, release, or patient-benefit claims.

## 6. Decision B does not authorize conversion

Historical E003 did not authorize model conversion. This successor decision surface does not infer conversion authority either.

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
QUANTIZATION_AUTHORITY=NONE
REQUANTIZATION_AUTHORITY=NONE
MERGE_OR_ADAPTER_APPLICATION_AUTHORITY=NONE
```

If an exact E002-authorized artifact cannot execute without conversion or another weight transformation, execution remains blocked until a separate exact conversion authority exists and all of its prerequisites are satisfied.

## 7. Decision B does not authorize data admission or contamination execution

```text
DATA_DOWNLOAD_AUTHORITY_CREATED_BY_DECISION_B=NONE
DATA_ADMISSION_AUTHORITY_CREATED_BY_DECISION_B=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY_CREATED_BY_DECISION_B=NONE
CONTAMINATION_EVIDENCE_CREATED_BY_DECISION_B=NO
```

Every evaluation or guard asset used under Decision B must already have exact source, revision/content identity, license/provenance, split, quarantine, contamination, and scope-purpose evidence required by the controlling contracts.

The public candidate research record created after PR #180 is source research only and cannot be treated as admitted curriculum/evaluation data.

## 8. Decision B does not authorize training

```text
TRAINING_AUTHORITY=NONE
SFT_AUTHORITY=NONE
CPT_AUTHORITY=NONE
LORA_QLORA_AUTHORITY=NONE
DISTILLATION_AUTHORITY=NONE
DPO_RL_GRPO_AUTHORITY=NONE
QAT_AUTHORITY=NONE
```

A later gradient-bearing run requires a separately explicit training authority bound to the exact RunManifest after every applicable prerequisite is PASS.

## 9. Decision B does not authorize protected or paid resources

```text
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

If execution would require a credential, gated asset, paid compute, paid provider, procurement, reimbursement, contract, or any incremental spend, Decision B does not authorize that action.

## 10. Mandatory preflight remains fail closed

Decision B would be necessary but not sufficient.

Before first model execution under the successor scope, the exact subject must satisfy the controlling base and component preflight, including as applicable:

- exact successor scope identity and scope-binding hash;
- exact E001/E002 candidate and artifact identity;
- exact non-clinical evaluation/guard asset identities;
- source/license/provenance PASS;
- privacy/non-PHI evidence where applicable;
- quarantine PASS;
- contamination PASS for every selection-bearing input;
- exact frozen evaluation protocol;
- exact runtime/environment/device identity;
- exact finance/resource/access bindings;
- exact component guard-snapshot evidence required at the relevant transition;
- A1-A14-equivalent applicable PASS snapshot;
- separately authorized A15 activation if required by the controlling execution contract;
- this exact successor execution authority identity.

No Founder authorization converts failed evidence into PASS.

## 11. Relationship to E004 and E005

Decision B would remove only the successor-scope execution-authority blocker once canonically captured.

```text
E004_COMPLETE_FROM_DECISION_B=NO
COMPONENT_E004_COMPLETE_FROM_DECISION_B=NO
TOURNAMENT_EVIDENCE_PACK_CREATED_FROM_DECISION_B=NO
BACKBONE_WINNER_SELECTED_FROM_DECISION_B=NO
E005_STARTED_FROM_DECISION_B=NO
```

Any evidence actually produced later must be reconciled under the canonical dependency order before E005 can become reachable.

## 12. ChatGPT recommendation for Founder review

```text
CHATGPT_SUCCESSOR_EXECUTION_POSITION=RECOMMEND_E004_SUCCESSOR_EXECUTION_DECISION_B
RATIONALE_1=FOUNDER_ALREADY_SELECTED_RESEARCH_ONLY_ADAPTATION_AS_THE_CURRENT_NO_EXTERNAL_REVIEWER_DIRECTION
RATIONALE_2=SP007_RO_001_IS_CANONICAL_AND_DEFINES_A_NARROW_NONCLINICAL_SCOPE
RATIONALE_3=V8_EXPLICITLY_REFUSES_TO_INFER_SUCCESSOR_EXECUTION_AUTHORITY_FROM_HISTORICAL_E003
RATIONALE_4=DECISION_B_REOPENS_ONLY_EVIDENCE_EXECUTION_AND_PRESERVES_CONVERSION_TRAINING_CONTAMINATION_PROTECTED_DATA_AND_SPEND_GATES
```

This recommendation is not a Founder decision.

## 13. Exact Founder response required

To preserve current authority:

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_A
```

To authorize the bounded Decision B scope:

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
```

A broad continuation instruction, generic approval, repository merge, or statement that all ordinary approvals are granted is not substituted for this exact model-execution authority decision.

The operative response must occur after this decision surface is canonical and must be captured in a separate decision record before any Decision B execution is treated as authorized.

## 14. Current state until an operative decision is canonical

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=ABSENT
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=NONE
SUCCESSOR_SCOPE_MODEL_EXECUTION_AUTHORITY=NONE
SUCCESSOR_SCOPE_TOURNAMENT_EXECUTION_AUTHORITY=NONE
SUCCESSOR_SCOPE_DEVICE_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 15. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded decision-request artifact. Before merge, verify exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation.
