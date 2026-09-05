# E004 Research-Component Evaluation Nonce-Repair Founder Decision Request — 2026-09-05

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Decision owner:** Founder  
**Decision state:** `PENDING_EXACT_FOUNDER_SELECTION`  
**Current authorized spend:** USD 0

## 1. Purpose

This decision surface resolves a deterministic contradiction discovered while executing the already-canonical evaluation-qualification Founder Decision B.

Decision B correctly required the proposed seven-asset subject to fail closed if its declared identities could not be recomputed. Exact-head qualification did fail closed. The repository must now choose whether to preserve the inconsistent proposed target bytes and remain blocked, or authorize one narrow deterministic reconstruction repair that preserves the declared asset IDs/scope while replacing only identities derived from the corrected construction.

This request does not itself repair any asset, create a PASS state, or expand model/tournament/training authority.

## 2. Exact contradiction evidence

The evaluation-asset validator was committed first:

```text
VALIDATOR_COMMIT=65cccddae92a8e86828bd394e87ba700ee323ccb
VALIDATOR_PATH=src/commandmed/spec007/research_tournament_assets.py
DECLARED_NONCE_METHOD=SHA256_NAMESPACE_SEED_METRIC_FAMILY_CASE_INDEX
```

That validator implements the declared method as:

```text
SHA256(f"{fixture_namespace_seed}|{metric_family}|{index}")[:16]
```

The asset-set bytes were committed later:

```text
ASSET_FREEZE_COMMIT=6cd3dd6ee638ee6512ad86be8178cf121ee59f18
ASSET_SET_PATH=specs/007-sft-v1/e004-research-component-tournament-evaluation-assets-v1.json
```

For the first frozen instruction case:

```text
FIXTURE_NAMESPACE_SEED=b85f140192a511cfbfe190476bdb3f6baf784b4d
METRIC_FAMILY=GENERAL_INSTRUCTION_FOLLOWING
CASE_INDEX=1
VALIDATOR_EXPECTED_NONCE=9e2b8a36a4170ea4
FROZEN_BYTE_NONCE=0fa98419824fb691
NONCE_MATCH=NO
```

The exact-head PR #254 qualification run then failed:

```text
PR=254
HEAD_SHA=af8a7bc5ede288aaebcd6b15d71b9408dd70e12b
WORKFLOW_RUN_ID=33966361118
JOB_ID=101307083265
AUTHORITY_BIND=PASS
COMPILE=PASS
FOCUSED_ASSET_QUALIFICATION=FAIL
VALIDATION_ERROR_COUNT=162
```

The failures are dominated by `case_nonce mismatch`, `prompt must contain exact case nonce`, `probe_nonce mismatch`, and `input_text must contain exact probe nonce`. Asset self-hashes, aggregate asset-set hash, Spec 003 admissions, and protocol/package validation consequently fail as downstream effects.

This is deterministic evidence of an internal construction contradiction, not an infrastructure failure and not an external-review issue.

## 3. Why existing Decision B cannot be silently stretched

The canonical evaluation-qualification request described the stored asset hashes as proposed deterministic construction targets and required every identity to be recomputed from exact constructed bytes and to fail closed on mismatch.

Therefore the implementation must not silently:

```text
WEAKEN_NONCE_VALIDATION=NO
ACCEPT_NONMATCHING_TARGET_HASHES=NO
MARK_CONTAMINATION_PASS_DESPITE_IDENTITY_FAILURE=NO
MARK_SPEC003_ELIGIBLE_DESPITE_IDENTITY_FAILURE=NO
FREEZE_PROTOCOL_DESPITE_IDENTITY_FAILURE=NO
SELECT_WINNER_DESPITE_IDENTITY_FAILURE=NO
```

A new explicit decision is required before replacing the proposed byte/hash identities with repaired deterministic identities.

## 4. Preserved exact subject boundaries

Both decision options preserve:

```text
ASSET_SET_ID=SP007_RO_001_NONCLINICAL_EVALUATION_ASSET_SET_V1
FIXTURE_NAMESPACE_SEED=b85f140192a511cfbfe190476bdb3f6baf784b4d
NONCE_METHOD=SHA256_NAMESPACE_SEED_METRIC_FAMILY_CASE_INDEX
ASSET_COUNT=7
MCQ_CASE_COUNT=72
RESOURCE_PROBE_COUNT=8
EXTERNAL_PAYLOADS_USED=NO
CANDIDATE_OUTPUTS_OBSERVED_BEFORE_FREEZE=NO
ADAPTIVE_GENERATION_FROM_CANDIDATE_OUTPUTS=NO
OPTIMIZATION_FEEDBACK_ALLOWED=NO
PRIVATE_GOLD_INCLUDED=NO
PHI_INCLUDED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

The exact asset IDs remain:

```text
SP007-RO-001-EVAL-INSTRUCTION-V1
SP007-RO-001-EVAL-ENGLISH-V1
SP007-RO-001-EVAL-ARABIC-NONCLINICAL-V1
SP007-RO-001-EVAL-UNCERTAINTY-V1
SP007-RO-001-EVAL-TOOL-ROUTING-V1
SP007-RO-001-EVAL-CAPABILITY-V1
SP007-RO-001-EVAL-RESOURCE-EFFICIENCY-V1
```

The exact ranking-family set remains unchanged.

## 5. Decision A — preserve proposed identities and remain blocked

If the Founder selects:

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION=E004_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION_A
```

then:

```text
EVAL_NONCE_REPAIR_AUTHORITY=NONE
EVAL_DERIVED_IDENTITY_REBIND_AUTHORITY=NONE
PR254_MERGE_ELIGIBLE=NO
RESEARCH_COMPONENT_EVAL_QUALIFICATION_PASS=NO
RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_FREEZE=BLOCKED
SUCCESSOR_PASS_PREFLIGHT=ABSENT
TOURNAMENT_EXECUTION=NOT_AUTHORIZED_BY_GATE_STATE
E005_STATE=NOT_REACHED
```

PR #254 must remain blocked or be closed without merge.

## 6. Decision B — authorize exact deterministic nonce reconstruction and derived-identity rebinding

If the Founder selects:

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION=E004_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION_B
```

then, only after exact post-canonical capture, the following bounded authority becomes available:

```text
EVAL_NONCE_REPAIR_AUTHORITY=AUTHORIZED_PREEXISTING_VALIDATOR_METHOD_ONLY
EVAL_NONCE_REPAIR_FORMULA=SHA256(f"{fixture_namespace_seed}|{metric_family}|{index}")[:16]
EVAL_NONCE_REPAIR_INDEXING=ONE_BASED_DECIMAL_UNPADDED
EVAL_NONCE_EMBEDDING_REPAIR_AUTHORITY=AUTHORIZED_EXACT_NONCE_FIELDS_AND_REQUIRED_PROMPT_INPUT_EMBEDDINGS_ONLY
EVAL_NONCE_SEMANTIC_PAYLOAD_REWRITE_AUTHORITY=NONE
EVAL_DERIVED_ASSET_HASH_REBIND_AUTHORITY=AUTHORIZED_DETERMINISTIC_RECOMPUTATION_ONLY
EVAL_DERIVED_ASSET_SET_HASH_REBIND_AUTHORITY=AUTHORIZED_DETERMINISTIC_RECOMPUTATION_ONLY
EVAL_DERIVED_PROVENANCE_BINDING_REBIND_AUTHORITY=AUTHORIZED_NEW_ASSET_SET_HASH_ONLY
EVAL_DERIVED_SOURCE_VERIFICATION_REBIND_AUTHORITY=AUTHORIZED_NEW_ASSET_SET_HASH_ONLY
EVAL_DERIVED_PRIVACY_BINDING_REBIND_AUTHORITY=AUTHORIZED_NEW_ASSET_SET_HASH_ONLY
EVAL_DERIVED_PROTOCOL_MANIFEST_REBIND_AUTHORITY=AUTHORIZED_ONLY_AFTER_ALL_REPAIRED_ASSETS_COMPUTE_ELIGIBLE
EVAL_DERIVED_PROTOCOL_HASH_REBIND_AUTHORITY=AUTHORIZED_DETERMINISTIC_RECOMPUTATION_ONLY
CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B authorizes correction of the exact nonce fields plus only the explicit full-nonce embeddings required by the validator in each case prompt or resource-probe input. It does not authorize rewriting unrelated semantic task content, answer choices, clinical scope, ranking families, asset IDs, counts, or source classes.

If any repaired case would require semantic-payload rewriting beyond replacing its explicit full nonce embedding, that case must fail closed and the repair must stop for that asset.

## 7. Required execution order under Decision B

If Decision B becomes canonical, execute in this order:

1. reverify live `main`, the original Decision B capture, this repair decision, and PR #254 state;
2. reconstruct every case/probe nonce from the preexisting validator formula using the exact frozen namespace seed, metric family, and one-based unpadded index;
3. replace only `case_nonce` / `probe_nonce` and the exact full-nonce occurrence required in `prompt` / `input_text`;
4. prove no unrelated semantic payload changed;
5. recompute every asset self-hash from exact repaired bytes;
6. recompute aggregate asset-set self-hash;
7. rebind only downstream evidence records whose exact subject hash is the asset-set hash;
8. rerun rights, provenance/source, bounded privacy, quarantine, narrow contamination, and canonical Spec 003 evaluator admission;
9. require all seven computed admissions to be `ELIGIBLE` without caller override;
10. rebuild/freeze the protocol manifests and protocol self-hash from the repaired admitted set;
11. run focused tests, deterministic verifier, full Spec 007 regression, full repository regression, and diff check on exact head;
12. reconcile any material PR findings/threads;
13. verify zero base drift, rulesets/protection, mergeability, and guarded expected-head merge;
14. after canonical merge, perform a fresh successor preflight before any model/tournament execution.

Any mismatch or semantic change outside the explicitly authorized nonce fields/full-nonce embeddings fails closed.

## 8. No model/tournament/training expansion

Decision B does not create or expand:

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
```

The separately canonical successor execution decision remains controlling and still requires a later exact PASS preflight before model/tournament execution.

## 9. Exact Founder response requirement

Generic continuation language does not select either option.

To select Decision A, the Founder must provide exactly:

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION=E004_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION_A
```

To select Decision B, the Founder must provide exactly:

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION=E004_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION_B
```

No selected repair authority is effective until the exact post-canonical Founder response is captured in a separate canonical decision record.

## 10. Current effect of this request

Canonical merge of this request changes no repair or execution state:

```text
FOUNDER_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION=ABSENT
EVAL_NONCE_REPAIR_AUTHORITY=NONE
EVAL_DERIVED_IDENTITY_REBIND_AUTHORITY=NONE
PR254_STATE=DRAFT_BLOCKED
RESEARCH_COMPONENT_EVAL_QUALIFICATION_PASS=NO
SUCCESSOR_PASS_PREFLIGHT=ABSENT
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

## 11. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository/PR review is optional by default for this documentation-only decision surface unless a later exact authority explicitly requires it.

Before merge, verify exact base/head/diff, applicable CI/status state, unresolved review threads, mergeability, branch/ruleset state, absence of a later canonical invalidation, and guarded expected-head merge.
