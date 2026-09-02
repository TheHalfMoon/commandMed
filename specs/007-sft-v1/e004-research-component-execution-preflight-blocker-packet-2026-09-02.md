# E004 Research Component Execution Preflight Blocker Packet — 2026-09-02

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Canonical base:** `4ccfe94dbbddcd72ce9874f222d78c3c589e9657`  
**Artifact class:** deterministic non-executing blocker mapping  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE

## 1. Purpose

Bind the current research-component execution frontier to the actual fail-closed reason codes implemented by `src/commandmed/spec007/activation.py` and `src/commandmed/spec007/research_scope.py`.

This packet does not create or imply any missing evidence, model identity, dataset identity, guard result, RunManifest, access authority, finance authority, execution authority, contamination result, A15 activation, or training authority.

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v13-2026-09-02.md
CURRENT_COMPONENT_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v12-2026-09-02.md
SUCCESSOR_SCOPE_POLICY=specs/007-sft-v1/e004-research-only-safety-policy-successor-2026-08-31.md
COMPONENT_SCOPE_ID=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
```

## 2. Synthetic control-plane evidence is not live-run evidence

The canonical implementation includes offline tests in `tests/spec007/test_research_scope.py` that construct `synthetic_fixture_only` RunManifest data, synthetic curriculum records, synthetic sentinel fixtures, content-scope verifications, scope bindings, and guard snapshots.

Those fixtures prove deterministic validator behavior only.

```text
SYNTHETIC_CONTROL_PLANE_FIXTURES=IMPLEMENTED
SYNTHETIC_SCOPE_BINDING_VALIDATION=IMPLEMENTED
SYNTHETIC_SENTINEL_FIXTURE_VALIDATION=IMPLEMENTED
SYNTHETIC_GUARD_SNAPSHOT_VALIDATION=IMPLEMENTED
SYNTHETIC_PREFLIGHT_NEGATIVE_TESTS=IMPLEMENTED
LIVE_COMPONENT_RUN_MANIFEST_CREATED_BY_TESTS=NO
LIVE_COMPONENT_GUARD_EVIDENCE_CREATED_BY_TESTS=NO
LIVE_COMPONENT_EXECUTION_AUTHORITY_CREATED_BY_TESTS=NO
```

Synthetic `PASS` values in tests MUST NOT be promoted into real E004 evidence.

## 3. Base RunManifest preflight blockers

The base preflight in `activation.py` returns fail-closed reason codes including:

```text
RUN_MANIFEST_INVALID_OR_UNRESOLVED
COMPONENT_RECORD_INVALID:<reference_field>
BASE_CHECKPOINT_BINDING_INVALID
BASE_WEIGHT_IDENTITY_MISSING
DATASET_SNAPSHOT_INVALID
DATASET_SNAPSHOT_HASH_MISSING
QUARANTINE_VERIFICATION_NOT_PASS
QUARANTINE_VERIFICATION_IDENTITY_MISMATCH
LICENSE_EVIDENCE_NOT_PASS
LICENSE_EVIDENCE_IDENTITY_MISMATCH
TRAINING_AUTHORITY_NONE
TRAINING_AUTHORITY_STALE_OR_MISMATCH
FINANCE_AUTHORITY_NONE
FINANCE_AUTHORITY_STALE_OR_MISMATCH
ACCESS_AUTHORITY_STALE_OR_MISMATCH
ACCESS_AUTHORITY_UNRESOLVED
MODEL_EXECUTION_AUTHORITY_NONE
WEIGHT_ACCESS_AUTHORITY_NONE
DEVICE_EXECUTION_AUTHORITY_NONE
```

The exact reason set for a future run is data-dependent and may be narrower than this vocabulary. This packet records the validator vocabulary; it does not fabricate a live preflight invocation.

## 4. Research-component-specific preflight blockers

The component preflight adds fail-closed reason codes including:

```text
RESEARCH_COMPONENT_SCOPE_BINDING_INVALID
RESEARCH_COMPONENT_SCOPE_AUTHORITY_MISMATCH
RESEARCH_COMPONENT_SCOPE_BINDING_STALE_OR_MISMATCH
RESEARCH_COMPONENT_RUN_MANIFEST_STALE_OR_MISMATCH
RESEARCH_COMPONENT_EXECUTION_AUTHORITY_NONE
RESEARCH_COMPONENT_GUARD_SNAPSHOT_NOT_PASS
```

A component run can be allowed only when the base preflight and component-specific preflight both return no reason codes for the exact live subject.

## 5. Exact live evidence currently absent

The current canonical frontier does not contain an executable live component bundle satisfying the implemented preflight.

```text
LIVE_COMPONENT_EXACT_RUN_MANIFEST=ABSENT
LIVE_COMPONENT_BASE_CHECKPOINT_BINDING=ABSENT
LIVE_COMPONENT_DATASET_SNAPSHOT=ABSENT
LIVE_COMPONENT_QUARANTINE_PASS_BINDING=ABSENT
LIVE_COMPONENT_LICENSE_PASS_BINDING=ABSENT
LIVE_COMPONENT_SCOPE_BINDING=ABSENT
LIVE_COMPONENT_CONTENT_SCOPE_VERIFICATIONS=ABSENT
LIVE_COMPONENT_SENTINEL_FIXTURE_SET=ABSENT
LIVE_COMPONENT_GUARD_SNAPSHOT_PASS=ABSENT
LIVE_COMPONENT_RESOURCE_FINANCE_BINDINGS=INCOMPLETE
LIVE_COMPONENT_ACCESS_BINDINGS=INCOMPLETE
COMPONENT_SUCCESSOR_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```

No field above may be changed to `PASS`, `AUTHORIZED`, or a concrete identity without corresponding canonical evidence.

## 6. Dependency-safe construction order

If later canonical evidence and separately applicable authority permit progress, the fail-closed dependency order for the component execution subject is:

1. freeze exact admitted gradient-bearing content with provenance, rights/license, privacy, split, verification, and contamination state;
2. freeze exact content-scope verification identities for every gradient-bearing record;
3. freeze the exact seven required sentinel fixture identities and their expected actions without using them as optimization feedback;
4. freeze an exact DatasetSnapshot and quarantine verification identity;
5. bind an exact BaseCheckpointBinding only after the required upstream winner/model decision exists;
6. bind the remaining exact component-store records required by the RunManifest;
7. freeze the exact RunManifest and compute its canonical identity;
8. freeze the exact research-component scope binding to that RunManifest and admitted content;
9. obtain real guard results for the exact sentinel fixture set and bind an exact guard-snapshot identity;
10. bind exact access, finance/resource, model/weight/device, and component execution authorities applicable to that exact subject;
11. run the deterministic base and component preflight and require `allowed=true` with an empty reason-code set before any execution;
12. obtain separate training authority for the exact RunManifest before any gradient-bearing training begins.

This order does not authorize any item. It only records the dependency relationship enforced by current code and governance.

## 7. Non-reviewer component boundary

`SP007-RO-001` remains controlling for the non-clinical component scope:

```text
COMPONENT_EXTERNAL_CLINICAL_REVIEW_REQUIRED=NO
COMPONENT_EXTERNAL_STATISTICAL_REVIEW_REQUIRED=NO
FULL_MULTI_ROLE_CLINICAL_SCOPE_QUALIFIED_BY_COMPONENT=NO
SYSTEM_SAFETY_PASS_CREATED_BY_COMPONENT=NO
```

The component lane therefore does not depend on the full-scope T1/A2 clinical/statistical reviewer gate, but it still depends on its own provenance, license, privacy, quarantine, contamination, exact-subject, resource/access, guard, execution, and training prerequisites.

## 8. Current terminal repository-only state

The repository already contains the deterministic validators, schemas, synthetic fixtures, and current-state reconciliations required to expose the missing live evidence fail closed.

```text
REPOSITORY_CONTROL_PLANE_FOR_COMPONENT_PREFLIGHT=IMPLEMENTED
REPOSITORY_SYNTHETIC_VALIDATION_SURFACE=IMPLEMENTED
REAL_COMPONENT_EXECUTION_SUBJECT=ABSENT
REAL_COMPONENT_EXECUTION_EVIDENCE=ABSENT
NO_ELIGIBLE_REPOSITORY_ONLY_REAL_GATE_TRANSITION_AVAILABLE=YES
COMPONENT_E004_COMPLETE=NO
E005_REACHABLE_FROM_COMPONENT_CURRENT_STATE=NO
PROJECT_FINISHED=NO
```

## 9. Explicit exclusions

This packet performs or authorizes none of the following:

- model or source-weight download, loading, conversion, quantization, or inference;
- benchmark or tournament execution;
- diagnostic/build/runtime rerun;
- contamination assessment;
- A15 activation;
- clinical/statistical reviewer outreach or scientific review;
- training, gradient updates, continued pretraining, SFT, LoRA, QLoRA, full fine-tuning, distillation, DPO, GRPO, RL, or QAT;
- Private Gold, PHI, restricted, or gated asset access;
- credential use or provider generation;
- procurement, payment, or spend.

## 10. Current authority boundary

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
COMPONENT_SUCCESSOR_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
SAFE_FOR_PATIENT_USE=NO
CLINICALLY_VALIDATED=NO
RELEASE_READY=NO
PROJECT_FINISHED=NO
```

## 11. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded documentation-only blocker mapping. Before merge, verify exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation.
