# E004 Research-Component Evaluation Qualification Founder Decision Request — 2026-09-05

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Decision owner:** Founder  
**Decision state:** `PENDING_EXACT_FOUNDER_SELECTION`  
**Current authorized spend:** USD 0

## 1. Purpose

This decision surface resolves one exact authority gap discovered after the canonical SP007 tournament control plane merged.

The canonical successor execution decision authorizes model/tournament execution only after every applicable preflight prerequisite has already passed, while explicitly preserving:

```text
DATA_ADMISSION_AUTHORITY_CREATED_BY_DECISION_B=NONE
PRIVACY_PII_PHI_SCREENING_AUTHORITY_CREATED_BY_DECISION_B=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY_CREATED_BY_DECISION_B=NONE
CONTAMINATION_EVIDENCE_CREATED_BY_DECISION_B=NO
```

The current repository therefore cannot legitimately promote a newly constructed evaluation asset to contamination `PASS`, Spec 003 `ELIGIBLE`, or selection-bearing tournament input merely because the asset is synthetic, repository-authored, or constructed after candidate freeze.

This request asks the Founder to choose whether to authorize one narrow deterministic qualification path for an exact seven-asset, non-clinical, project-authored evaluation subject.

This request does not itself create that authority.

## 2. Controlling existing boundaries

The following canonical boundaries remain controlling regardless of the selected option:

```text
SUCCESSOR_SCOPE_ID=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
SUCCESSOR_SCOPE_CLAIM_CLASS=NON_CLINICAL_RESEARCH_ENGINEERING_ONLY
ADMITTED_ROLE_CLASSES=LEARNER_RESEARCHER
PATIENT_CAREGIVER_ROLE_ADMITTED=NO
CLINICAL_PROFESSIONAL_ROLE_ADMITTED=NO
COMPONENT_EXTERNAL_CLINICAL_REVIEW_REQUIRED=NO
COMPONENT_EXTERNAL_STATISTICAL_REVIEW_REQUIRED=NO
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The seven SP007 guard/sentinel fixtures remain abort/disqualify-only and cannot become ranking inputs.

## 3. Exact proposed evaluation subject

The proposed subject is repository-authored, deterministic, non-clinical, and external-payload-free.

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

The proposed exact metric-family set is:

```text
GENERAL_INSTRUCTION_FOLLOWING
GENERAL_ENGLISH_LANGUAGE
GENERAL_ARABIC_LANGUAGE_NON_CLINICAL
UNCERTAINTY_AND_ABSTENTION
SYNTHETIC_NON_CLINICAL_TOOL_ROUTING
GENERAL_CAPABILITY_PRESERVATION
RESOURCE_EFFICIENCY
```

The proposed exact asset identities are:

```text
SP007-RO-001-EVAL-INSTRUCTION-V1=5d8c26b329fce0e3482609a7022a77d8fd4ae15dd8fea9147aecebb05e2aa6b7
SP007-RO-001-EVAL-ENGLISH-V1=fcd031071722117af6380d02287df815c81fcea1f9b9e28b0f6bff4f01ab24b5
SP007-RO-001-EVAL-ARABIC-NONCLINICAL-V1=4b5197c6a82be54ded43f790bc440dd0ca69f13c17c3d7f1adf42ebd5770414f
SP007-RO-001-EVAL-UNCERTAINTY-V1=501616fab6d321d3f686e108de04d7b5ecfb985e041a2d205b64fa00d8a8ef52
SP007-RO-001-EVAL-TOOL-ROUTING-V1=4fd249917c2ee40c9c3540e358cfaa0a5def97381694e08bde474b818ea1e030
SP007-RO-001-EVAL-CAPABILITY-V1=8e46855039a004b7486b196e7783b1530f7630429ca303e169ad719fec91eb25
SP007-RO-001-EVAL-RESOURCE-EFFICIENCY-V1=a1ddea12b740886643fc396c62553b1ab954404090d16db499a57e933056a200
PROPOSED_ASSET_SET_SHA256=49d1044ec8c6317136cf69d5b094eb1d4e93a8d6dad938be23254a71a5dfe435
```

These are proposed deterministic construction targets, not current canonical qualification evidence. If Decision B is selected, every identity above must be recomputed from the exact constructed bytes and fail closed on any mismatch.

## 4. Proposed evidence instruments

The proposed deterministic qualification path is additionally bound to these expected identities:

```text
PROPOSED_RIGHTS_INSTRUMENT_ID=E004_RESEARCH_COMPONENT_PROJECT_AUTHORED_EVAL_RIGHTS_V1
PROPOSED_RIGHTS_INSTRUMENT_SHA256=877205412550ac16a074634c6549e3e169bf216ddbb6216646307a05bf2f59d0

PROPOSED_PROVENANCE_INSTRUMENT_ID=E004_RESEARCH_COMPONENT_DETERMINISTIC_FIXTURE_PROVENANCE_V1
PROPOSED_PROVENANCE_INSTRUMENT_SHA256=f00ed7bdb15079ac19b7de30ff88742b2a0e9bbc2d270fc79065660d2444e7bf

PROPOSED_SOURCE_VERIFICATION_INSTRUMENT_ID=E004_RESEARCH_COMPONENT_SOURCE_VERIFICATION_V1
PROPOSED_SOURCE_VERIFICATION_INSTRUMENT_SHA256=af453aa210ac928db413e928bbaff372e0d08ac3487bab37dfb716d68ba6d220

PROPOSED_CONTAMINATION_METHOD_ID=E004_RESEARCH_COMPONENT_POST_FREEZE_SYNTHETIC_NONEXPOSURE_V1
PROPOSED_CONTAMINATION_METHOD_SHA256=190c8107cbf9f2f942cdc404f9cc7a00f185514c9e9a609431645f78261a8b6b

CANONICAL_QUARANTINE_MATRIX_SHA256=e2b2fd52e2eef007935ffe497fb50656960fa4ab82caac45138e117594475477
PROPOSED_QUARANTINE_SPLIT=MODEL_SELECTION_DEV_SET
PROPOSED_QUARANTINE_PURPOSE=CHECKPOINT_SELECTION
```

The proposed contamination method has deliberately narrow semantics:

```text
CONTAMINATION_PASS_SEMANTICS=EXACT_FIXTURE_NONEXPOSURE_AND_NONADAPTIVE_PRE_RESULT_FREEZE_ONLY
SEMANTIC_TASK_NOVELTY_CLAIM=NO
CANDIDATE_PRETRAINING_CORPUS_INSPECTION_CLAIM=NO
PRIVATE_GOLD_COMPARISON=NO
```

Decision B would not authorize a broader statement that the semantic tasks, concepts, templates, or equivalent material were absent from any candidate pretraining corpus.

## 5. Decision A — preserve the current blocker

If the Founder selects:

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION=E004_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION_A
```

then the state remains:

```text
RESEARCH_COMPONENT_EVAL_ASSET_CONSTRUCTION_AUTHORITY=NONE
RESEARCH_COMPONENT_EVAL_RIGHTS_EVALUATION_AUTHORITY=NONE
RESEARCH_COMPONENT_EVAL_PROVENANCE_VERIFICATION_AUTHORITY=NONE
RESEARCH_COMPONENT_EVAL_PRIVACY_CLASSIFICATION_AUTHORITY=NONE
RESEARCH_COMPONENT_EVAL_QUARANTINE_EVIDENCE_AUTHORITY=NONE
RESEARCH_COMPONENT_EVAL_CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
RESEARCH_COMPONENT_EVAL_SPEC003_ADMISSION_AUTHORITY=NONE
RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_FREEZE_AUTHORITY=NONE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

No proposed artifact may be represented as qualified, admitted, contamination-passed, or selection-bearing.

## 6. Decision B — authorize the exact deterministic qualification path

If the Founder selects:

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION=E004_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION_B
```

then, only after the exact decision is captured canonically, the following authority becomes available:

```text
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

Decision B would authorize only deterministic evidence production for the exact proposed subject. It would not predetermine any PASS result.

## 7. Required fail-closed execution order under Decision B

If Decision B becomes canonical, execution must occur in this order:

1. construct only the exact seven proposed assets using the declared namespace seed and deterministic nonce method;
2. recompute every asset SHA and the aggregate asset-set SHA;
3. validate the exact rights instrument for internal research model-selection use only;
4. validate deterministic provenance and source identity against the exact repository-authored subject;
5. evaluate non-PHI/privacy classification only for the exact declared project-authored fixtures, without external providers;
6. evaluate the canonical quarantine matrix for `MODEL_SELECTION_DEV_SET × CHECKPOINT_SELECTION`;
7. execute only the exact declared contamination method and preserve its narrow non-exposure/non-adaptation semantics;
8. build Spec 003 lineage records and compute admission through the canonical evaluator; caller-supplied `ELIGIBLE` is prohibited;
9. freeze the exact tournament protocol only if every exact asset has computed `ELIGIBLE` state and every prerequisite binding matches;
10. run exact-head repository qualification before merge.

Any mismatch, unresolved state, unexpected content, external payload dependency, candidate-output adaptation, protected-data dependency, credential requirement, or spend requirement must fail closed.

## 8. Decision B does not authorize model execution

Even if every exact asset gate passes and the protocol is frozen, this decision does not itself make the successor execution preflight PASS.

Decision B creates no new authority for:

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
```

The already-canonical successor execution decision remains separately controlling and still requires an exact PASS preflight before any model or tournament execution.

## 9. No scientific or product claim expansion

Neither decision option creates:

```text
SYSTEM_SAFETY_PASS=NO
CLINICAL_SAFETY_PASS=NO
PATIENT_USE_AUTHORITY=NONE
CLINICAL_PROFESSIONAL_USE_AUTHORITY=NONE
RELEASE_READY=NO
SUPERIORITY_CLAIM_AUTHORITY=NONE
SOTA_CLAIM_AUTHORITY=NONE
```

The seven proposed ranking assets remain non-clinical research-engineering evidence only.

## 10. Exact Founder response requirement

Generic continuation language does not select either option.

To select Decision A, the Founder must provide exactly:

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION=E004_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION_A
```

To select Decision B, the Founder must provide exactly:

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION=E004_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION_B
```

A generic statement such as `go ahead`, `you have all approvals`, or `finish the project` is project intent but is not an operative selection for this bounded authority surface.

No selected authority is effective until the exact post-canonical Founder response is captured in a separate canonical decision record.

## 11. Current effect of this request

Canonical merge of this request changes no execution state:

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_QUALIFICATION_DECISION=ABSENT
RESEARCH_COMPONENT_EVAL_CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
RESEARCH_COMPONENT_EVAL_SPEC003_ADMISSION_AUTHORITY=NONE
RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_FREEZE_AUTHORITY=NONE
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 12. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository/PR review is optional by default for this bounded documentation-only decision surface unless a later exact authority explicitly requires it.

Before merge, verify exact base/head/diff, applicable CI/status state, unresolved review threads, mergeability, branch/ruleset state, and absence of a later canonical invalidation. Merge only with an exact expected-head guard.
