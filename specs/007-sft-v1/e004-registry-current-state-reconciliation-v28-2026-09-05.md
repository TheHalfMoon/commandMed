# E004 Registry Current-State Reconciliation V28 — 2026-09-05

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** global E004 preflight plus `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Reconciliation class:** append-only current-state overlay
**Supersedes as current view:** `e004-registry-current-state-reconciliation-v27-2026-09-04.md`
**Canonical base:** `142b324d471744aa99c8cf6a573b6df7335f7631`
**Authority effect:** NONE
**Execution effect:** NONE
**Training authority:** NONE
**Spend authority:** NONE

## 1. Purpose

Reconcile the exact live E004 state after PR #244 canonically closed the Aya-43 DatasetSnapshot/quarantine dependency and then re-evaluate the global Spec 005 A1–A15 preconstruction path in dependency order.

This record creates no reviewer-outreach authority, reviewer appointment, scientific disposition, threshold, statistical design, contamination assessment, model conversion, A15 activation, model inference, tournament execution, winner selection, training, credential access, procurement, payment, or spend authority.

## 2. Canonical post-PR-244 state

PR #244 merged as:

```text
CANONICAL_MAIN=142b324d471744aa99c8cf6a573b6df7335f7631
PR244_FINAL_HEAD=ac9e7ed1b1a6b6298cfba088cb08d014b0cddc78
PR244_MERGE=142b324d471744aa99c8cf6a573b6df7335f7631
PR244_FINAL_DATASET_WORKFLOW_RUN=33926726324
PR244_FINAL_DATASET_WORKFLOW_JOB=101196755617
PR244_FINAL_SENTINEL_WORKFLOW_RUN=33926726279
PR244_FINAL_SENTINEL_WORKFLOW_JOB=101196755334
```

The exact final PR head freshly validated the committed safe bundle, focused fail-closed tests, non-execution/privacy boundary, diff whitespace, and safe artifact publication before guarded expected-head merge.

## 3. Exact Aya-43 DatasetSnapshot remains canonical

```text
FINAL_CURRICULUM_RECORD_COUNT=43
FINAL_CURRICULUM_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
AYA_43_PERSISTED_BUNDLE_SHA256=f12f70a754e39d395c4d5999fcae1d6718640b1a97931fd9f48321469b87be03
DUPLICATE_REPORT_DISPOSITION=PASS
DUPLICATE_REPORT_CANONICAL_SHA256=562c3f3726538d27f2d40e2f20a762764b9f21c3675a3621672755c7cbc9d6b0
DATASET_SNAPSHOT_ID=e004-aya-43-research-component-dataset-snapshot-v1
DATASET_SNAPSHOT_RECORD_COUNT=43
DATASET_SNAPSHOT_SHA256=c81da713b01d5ed9470ae9853834087bb6166f8f628d426371643a75064c1117
QUARANTINE_VERIFICATION_ID=e004-aya-43-train-quarantine-verification-v1
QUARANTINE_VERIFICATION_STATUS=PASS
QUARANTINE_MATRIX_SHA256=e2b2fd52e2eef007935ffe497fb50656960fa4ab82caac45138e117594475477
QUARANTINE_PURPOSE=TRAIN
QUARANTINE_SOURCE_ID=VERIFIED_SFT_CURRICULUM_DATA
QUARANTINE_ALLOWED=true
QUARANTINE_CAN_TRAIN=true
QUARANTINE_CAN_SELECT_MODEL=false
```

The DatasetSnapshot work does not create a model winner, BaseCheckpointBinding, A15 activation, or tournament evidence pack.

## 4. Component lane after DatasetSnapshot

The research-component dependency ordering remains:

```text
DEPENDENCY_1_EXACT_ADMITTED_GRADIENT_CONTENT=EVIDENCED_EXACT_AYA_43_ONLY
DEPENDENCY_2_CONTENT_SCOPE_VERIFICATION_IDENTITIES=EVIDENCED_EXACT_AYA_43_ONLY
DEPENDENCY_3_EXACT_SEVEN_SENTINEL_FIXTURE_IDENTITIES=CONSTRUCTED_FROZEN_VALIDATED_EXACT_SUBJECT
DEPENDENCY_4_DATASET_SNAPSHOT_AND_QUARANTINE_IDENTITY=EVIDENCED_EXACT_AYA_43_ONLY
DEPENDENCY_5_BASE_CHECKPOINT_BINDING=BLOCKED_BY_REQUIRED_UPSTREAM_WINNER_MODEL_DECISION
```

```text
NEXT_COMPONENT_DEPENDENCY=BASE_CHECKPOINT_BINDING
UPSTREAM_WINNER_MODEL_DECISION=ABSENT
MODEL_WINNER_SELECTED=NO
BASE_CHECKPOINT_BINDING=ABSENT
```

No component-only work may manufacture the upstream winner/model decision or skip to E005.

## 5. Global E004 A1–A15 preconstruction ordering

The canonical Spec 005 activation validator requires PASS, non-stale evidence for all of:

```text
R1=A1_METRICS_V2
T1=A2_THRESHOLD_MARGIN_POLICY
D34=A3_A4_STATISTICAL_DESIGN_ALLOCATION
G1=A5_RIGHTS_INSTRUMENT
G2=A6_NON_PHI_POLICY
G3=A8_AUTHORING_REVIEW_PROTOCOL
G4=A12_CHANGE_CONTROL
S1=A10_EXACT_SOURCE_ROUTE
P1=A9_PROVENANCE_BINDINGS
C1=A11_CONTAMINATION_PLAN
H1=A7_PERSONNEL_ROSTER_NONEXPOSURE
I1=A13_ACCESS_FIREWALL
F1=A14_SPEND_ENGAGEMENT
J1=FRESH_A1_TO_A14_READINESS_RECHECK
ACT=A15_SEPARATE_ACTIVATION
```

A15 is not eligible merely because E003 model/tournament execution authority exists. The real preconstruction snapshot must first compute `READY_FOR_SEPARATE_ACTIVATION_NOT_AUTHORIZED` with every required gate PASS and non-stale.

## 6. Earliest unresolved global gate

`R1/A1` remains structurally/canonically complete through the metrics-v2 control plane. The earliest unresolved scientific gate remains `T1/A2`.

Current repository truth does not contain a qualified real clinical/statistical review disposition freezing the exact numeric threshold/margin policy required by T1.

```text
R1_A1=PASS_FOR_PRECONSTRUCTION_DEPENDENCY
T1_A2=INCOMPLETE
D34_A3_A4=BLOCKED_BY_T1
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
NUMERIC_THRESHOLD_MARGIN_POLICY=NOT_FROZEN
A15_PRECONSTRUCTION_SNAPSHOT=NOT_READY_TO_CONSTRUCT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
```

Static literature, repository bots, LLM review, Founder self-attestation, or the Aya-43 DatasetSnapshot cannot substitute for the domain-qualified clinical/statistical evidence required by this gate.

## 7. Controlling reviewer-outreach decision surface remains unresolved

The existing canonical controlling decision surface is:

`specs/007-sft-v1/e004-founder-reviewer-outreach-reauthorization-decision-request-2026-08-30.md`

That request explicitly preserves PR #117 unless the Founder supplies an attributable, verifiable, post-surface exact selection. No later canonical record selects either decision class.

Current state therefore remains:

```text
FOUNDER_OUTREACH_DECISION=ABSENT
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
INITIAL_PRESCREEN_MESSAGES_AUTHORIZED_NOW=0
FOLLOW_UP_MESSAGES_AUTHORIZED_NOW=0
REVIEWER_CANDIDATE_CONTACT_EXECUTION=PROHIBITED
REVIEWER_APPOINTMENT_AUTHORITY=NONE
SCIENTIFIC_REVIEW_AUTHORITY=NONE
```

The canonical request recommends the bounded zero-spend Decision B pre-screen route but does not authorize it.

The exact operative token for that route is:

```text
FOUNDER_OUTREACH_DECISION=E004_OUTREACH_DECISION_B
```

A generic continuation instruction, including a generic instruction supplied after this reconciliation, is not rewritten into that token. The separately required Founder identity/source/content/timestamp/ordering provenance must also be canonically capturable before Decision B becomes effective.

## 8. No A15 request is dependency-safe yet

A15 requires a real current PASS snapshot over A1–A14. Since T1 remains incomplete, requesting or granting A15 now would bypass the canonical dependency DAG.

```text
A15_REQUEST_ELIGIBLE=NO
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
MODEL_INFERENCE_ELIGIBLE_UNDER_GLOBAL_PREFLIGHT=NO
TOURNAMENT_EXECUTION_ELIGIBLE_UNDER_GLOBAL_PREFLIGHT=NO
```

E003 remains a necessary but not sufficient execution authority.

## 9. Later boundaries remain closed

```text
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
MODEL_WINNER_SELECTED=NO
BASE_CHECKPOINT_BINDING=ABSENT
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
SENTINEL_GUARD_PASS_CREATED=NO
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
USER_MANAGED_CREDENTIAL_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 10. Privacy and cleanup truth

```text
RAW_AYA_TEXT_REPOSITORY_PERSISTED=NO
MATCHED_NGRAM_PERSISTED=NO
USER_ID_READ=NO
MODEL_INFERENCE_USED=NO
TRAINING_PERFORMED=NO
CURRENT_LOCAL_TRANSIENT_CLEANUP_VERIFICATION=UNVERIFIED
LOCAL_TRANSIENT_CLEANUP_COMPLETE=NOT_CLAIMED
```

This reconciliation does not access or persist raw Aya text.

## 11. Immediate frontier

The exact dependency-safe frontier is not E005 and not A15. It is the already-canonical reviewer-outreach Founder decision surface needed to make even the minimum T1 reviewer-prescreen path executable.

```text
NEXT_GLOBAL_DEPENDENCY=T1_A2_THRESHOLD_MARGIN_POLICY
NEXT_GOVERNANCE_SURFACE=E004_FOUNDER_REVIEWER_OUTREACH_REAUTHORIZATION_DECISION_REQUEST
NEXT_OPERATIVE_DECISION_REQUIRED=FOUNDER_OUTREACH_DECISION
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
NEXT_ELIGIBLE_REPOSITORY_ONLY_REAL_GATE_TRANSITION=NONE
```

No repository-only continuation can create the missing domain-qualified reviewer evidence.

## 12. Project state

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 13. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is optional by default for this bounded documentation-only current-state reconciliation. Deterministic live-state verification, exact base/head/diff checks, unresolved review-thread checks, branch/ruleset verification, and guarded expected-head merge remain required. This reconciliation claims no independent review PASS.