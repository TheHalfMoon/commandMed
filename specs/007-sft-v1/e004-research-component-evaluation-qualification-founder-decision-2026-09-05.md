# E004 Research-Component Evaluation Qualification Founder Decision — 2026-09-05

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Decision owner:** Founder  
**Decision source surface:** `e004-research-component-evaluation-qualification-founder-decision-request-2026-09-05.md`  
**Canonical base before capture:** `72ca6085356c3a92b1df29ea83ba2a9e5be81c46`  
**Current authorized spend:** USD 0

## 1. Exact Founder selection

The Founder supplied the exact post-canonical selection required by the decision-request surface:

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION=E004_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION_B
```

This record captures that exact selection and only the bounded authority defined by Decision B.

## 2. Effective bounded authority

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION=E004_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION_B
RESEARCH_COMPONENT_EVAL_ASSET_CONSTRUCTION_AUTHORITY=AUTHORIZED_EXACT_DECLARED_SET_ONLY
RESEARCH_COMPONENT_EVAL_RIGHTS_EVALUATION_AUTHORITY=AUTHORIZED_PROJECT_AUTHORED_INTERNAL_SELECTION_ONLY
RESEARCH_COMPONENT_EVAL_PROVENANCE_VERIFICATION_AUTHORITY=AUTHORIZED_EXACT_DECLARED_SET_ONLY
RESEARCH_COMPONENT_EVAL_PRIVACY_CLASSIFICATION_AUTHORITY=AUTHORIZED_EXACT_DECLARED_FIXTURES_ONLY_NO_EXTERNAL_PROVIDER
RESEARCH_COMPONENT_EVAL_QUARANTINE_EVIDENCE_AUTHORITY=AUTHORIZED_EXACT_DECLARED_SET_CHECKPOINT_SELECTION_ONLY
RESEARCH_COMPONENT_EVAL_CONTAMINATION_ASSESSMENT_AUTHORITY=AUTHORIZED_EXACT_DECLARED_SET_NONEXPOSURE_METHOD_ONLY
RESEARCH_COMPONENT_EVAL_SPEC003_ADMISSION_AUTHORITY=AUTHORIZED_EXACT_DECLARED_SET_EVALUATOR_ONLY
RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_FREEZE_AUTHORITY=AUTHORIZED_ONLY_IF_ALL_EXACT_ASSET_GATES_PASS
CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

The authority is limited to the exact subject declared by the canonical request surface:

```text
PROPOSED_ASSET_SET_ID=SP007_RO_001_NONCLINICAL_EVALUATION_ASSET_SET_V1
PROPOSED_FIXTURE_NAMESPACE_SEED=b85f140192a511cfbfe190476bdb3f6baf784b4d
PROPOSED_NONCE_METHOD=SHA256_NAMESPACE_SEED_METRIC_FAMILY_CASE_INDEX
PROPOSED_ASSET_COUNT=7
PROPOSED_MCQ_CASE_COUNT=72
PROPOSED_RESOURCE_PROBE_COUNT=8
EXTERNAL_PAYLOADS_USED=NO
CANDIDATE_OUTPUTS_OBSERVED_BEFORE_FREEZE=NO
ADAPTIVE_GENERATION_FROM_CANDIDATE_OUTPUTS=NO
OPTIMIZATION_FEEDBACK_ALLOWED_FROM_FIXTURE_CONSTRUCTION=NO
PRIVATE_GOLD_INCLUDED=NO
PHI_INCLUDED=NO
```

## 3. Required execution order

The authorized deterministic qualification path must execute fail closed in this order:

1. reconstruct only the exact seven declared assets from the canonical namespace seed and deterministic nonce method;
2. recompute every asset SHA and aggregate asset-set SHA;
3. evaluate the exact project-authored internal-selection rights instrument;
4. verify exact deterministic provenance and source identity;
5. evaluate non-PHI/privacy classification only for the exact declared project-authored fixtures without external providers;
6. evaluate canonical quarantine policy for `MODEL_SELECTION_DEV_SET × CHECKPOINT_SELECTION`;
7. execute only the exact declared contamination method with narrow exact-fixture non-exposure/non-adaptation semantics;
8. build Spec 003 lineage records and compute admission through the canonical evaluator, never through caller-supplied `ELIGIBLE` state;
9. freeze the exact tournament protocol only if all exact asset gates compute PASS/ELIGIBLE and all identities bind exactly;
10. run exact-head repository qualification before merge;
11. perform a fresh successor preflight after canonical merge before any model or tournament execution.

Any mismatch, unresolved evidence state, unexpected payload, protected-data dependency, credential dependency, external-provider dependency, candidate-output adaptation, or spend requirement fails closed.

## 4. Contamination semantics remain narrow

```text
CONTAMINATION_PASS_SEMANTICS=EXACT_FIXTURE_NONEXPOSURE_AND_NONADAPTIVE_PRE_RESULT_FREEZE_ONLY
SEMANTIC_TASK_NOVELTY_CLAIM=NO
CANDIDATE_PRETRAINING_CORPUS_INSPECTION_CLAIM=NO
PRIVATE_GOLD_COMPARISON=NO
```

Decision B does not authorize a claim that semantically equivalent tasks or concepts were absent from candidate pretraining corpora.

## 5. No execution/training/claim expansion

This decision does not create or expand any of the following:

```text
MODEL_WEIGHT_ACCESS_AUTHORITY_EXPANSION=NONE
MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE
TOURNAMENT_EXECUTION_AUTHORITY_EXPANSION=NONE
DEVICE_EXECUTION_AUTHORITY_EXPANSION=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
SYSTEM_SAFETY_PASS=NO
CLINICAL_SAFETY_PASS=NO
PATIENT_USE_AUTHORITY=NONE
CLINICAL_PROFESSIONAL_USE_AUTHORITY=NONE
RELEASE_READY=NO
SUPERIORITY_CLAIM_AUTHORITY=NONE
SOTA_CLAIM_AUTHORITY=NONE
```

The separately canonical successor execution decision remains controlling and permits model/tournament execution only after a later exact PASS preflight.

## 6. Immediate post-capture state

This decision authorizes deterministic qualification work but does not predetermine its result:

```text
E004=INCOMPLETE
E004_STATE=AUTHORIZED_FOR_EXACT_EVAL_QUALIFICATION_ONLY
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=AUTHORIZED_FOR_EXACT_EVAL_QUALIFICATION_ONLY
E005_STATE=NOT_REACHED
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
MODEL_WINNER_SELECTED=NO
BASE_CHECKPOINT_BINDING=ABSENT
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

## 7. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository/PR review is optional by default for this bounded documentation-only decision capture unless a later exact authority explicitly requires it.

Before merge, verify exact base/head/diff, applicable CI/status state, unresolved review threads, mergeability, branch/ruleset state, absence of a later canonical invalidation, and guarded expected-head merge.
