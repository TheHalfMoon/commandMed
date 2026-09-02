# E004 Registry Current-State Reconciliation V12 — 2026-09-02

**Spec:** 007 SFT V1
**Artifact class:** append-only component current-state reconciliation
**Canonical base:** `cdbdb525992108fc35e62540d297b22717506429`
**Exact component scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Authority effect:** NONE
**Execution effect:** NONE
**Model conversion authority:** NONE
**Contamination assessment authority:** NONE
**A15 activation:** ABSENT_NOT_AUTHORIZED
**Training authority:** NONE
**Current authorized spend:** USD 0

## 1. Purpose and supersession

Reconcile the exact research-component E004 frontier after the later canonical runtime/build evidence chain, execution-time identity-binding policy, build-environment-equality amendment, V10 global current-state reconciliation, and Founder decision `FD-007` removing mandatory independent repository/PR review as a default gate.

For the exact component scope only:

```text
PREVIOUS_COMPONENT_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v9-2026-08-31.md
CURRENT_COMPONENT_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v12-2026-09-02.md
V12_SUPERSEDES_V9_CURRENT_STATE_FOR_COMPONENT=YES
V12_SUPERSEDES_GLOBAL_V10_OR_V11=NO
FULL_MULTI_ROLE_SCOPE_CHANGED=NO
```

Historical evidence remains immutable. V12 updates current-state interpretation only.

## 2. Canonical component policy and enforcement remain complete

The component policy and its offline fail-closed enforcement are already canonical:

```text
SP007_RO_001_PR=142
SP007_RO_001_MERGE=f8e85ed3e0cee3bf41786b2b2eb6c79972153cde
SP007_RO_001_SCOPE=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
SP007_RO_001_ROLE=LEARNER_RESEARCHER
PR144_SCOPE_ENFORCEMENT_MERGE=05c5d4840f868d782c7d36c87970e30986ed3781
PR145_COMPONENT_V9_MERGE=07b7441b7dace693697136fea9331a6be95e3b53
COMPONENT_SCOPE_POLICY_IDENTITY=PASS_CANONICAL
COMPONENT_SCOPE_OFFLINE_ENFORCEMENT=PASS_CANONICAL_IMPLEMENTED
```

The component remains non-clinical research engineering only. Patient/caregiver and clinical-professional positive capabilities remain excluded. Population clinical/statistical PASS is not created by this lane.

## 3. Repository reviewer gate no longer blocks this component

Founder decision `FD-007` and constitutional amendment 0.1.1 are canonical at PR #175 merge `cdbdb525992108fc35e62540d297b22717506429`.

```text
INDEPENDENT_REPOSITORY_REVIEW_REQUIRED_BY_DEFAULT=NO
EXACT_HEAD_REVIEW_REQUIRED_BY_DEFAULT=NO
MATERIAL_BLOCKER_NO_REVIEWER_SENTINEL_REQUIRED_BY_DEFAULT=NO
COMPONENT_EXTERNAL_CLINICAL_REVIEW_REQUIRED=NO
COMPONENT_EXTERNAL_STATISTICAL_REVIEW_REQUIRED=NO
```

The first three lines govern repository/PR qualification. The final two are inherited from canonical `SP007-RO-001` for this exact non-clinical component scope.

This does not remove domain-qualified evidence requirements from any broader clinical/full-system scope.

## 4. Shared runtime/toolchain evidence advanced after V9

V9 recorded the component runtime/toolchain frontier before the later successful repaired-runtime attempt. The canonical shared E004 toolchain evidence now includes:

```text
HISTORICAL_BUILD_RUN_ID=33187438094
HISTORICAL_BUILD_JOB_ID=98903988417
HISTORICAL_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
REPAIRED_TARGET_RUNTIME_EVIDENCE_RESULT=PASS
REPAIRED_RUNTIME_RUN_ID=33434874024
REPAIRED_RUNTIME_JOB_ID=99628745384
REPAIRED_LLAMA_QUANTIZE_SHA256=18ff27aab20ab7b4e239ac847be7636fb8e182ac9d1474efa7c4cfc915bbb4fc
REPAIRED_TARGET_RUNTIME_EVIDENCE_ATTEMPT_ALLOWANCE_REMAINING=0
```

The later one-shot diagnostic was also consumed exactly once:

```text
DIAGNOSTIC_RUN_ID=33507754943
DIAGNOSTIC_RUN_ATTEMPT=1
DIAGNOSTIC_JOB_ID=99855785119
DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
SECOND_DIAGNOSTIC_EXECUTION_AUTHORITY=NONE
HISTORICAL_TWO_HASH_SPLIT_REPRODUCED=NO
REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
```

Therefore the stale V9 state `COMPONENT_RUNTIME_EVIDENCE=NOT_STARTED` is superseded only for the shared E004 conversion-toolchain evidence surface:

```text
COMPONENT_SHARED_TOOLCHAIN_RUNTIME_EVIDENCE=PASS_CANONICAL
COMPONENT_SPECIFIC_EXECUTION_SUBJECT_RUNTIME_BINDING=ABSENT
```

Shared toolchain evidence is not a component execution authorization and is not a real component RunManifest or guard snapshot.

## 5. Historical repaired-hash reconstruction is no longer a future execution prerequisite

The canonical execution-time policy `E004-EXECUTION-TIME-IDENTITY-BINDING-V1` and its build-environment-equality amendment permit a future separately authorized conversion subject to bind a same-subject double-built tool identity instead of reproducing either historical binary hash.

```text
EXECUTION_TIME_IDENTITY_BINDING_POLICY_DISPOSITION=ACCEPTED_FAIL_CLOSED_FOR_FUTURE_SEPARATELY_AUTHORIZED_CONVERSION
HISTORICAL_REPAIRED_HASH_RECONSTRUCTION_AS_MANDATORY_PRECONDITION=REMOVED_BY_POLICY
FUTURE_CONVERSION_TOOL_IDENTITY_MODE=SAME_SUBJECT_DOUBLE_BUILD_THEN_BIND
DOUBLE_BUILD_BUILD_ENVIRONMENT_MANIFEST_EQUAL=YES_REQUIRED
DOUBLE_BUILD_MISMATCH_DISPOSITION=ABORT_BEFORE_MODEL_BYTES
```

This closes the historical-hash reconstruction policy blocker. It does not create a concrete component execution subject.

## 6. Real component execution evidence remains absent

No later canonical record supplies a real live-run component binding or guard snapshot. Repository search at the current base finds only the prior V9 `ABSENT` state for these identities.

```text
REAL_RESEARCH_COMPONENT_SCOPE_BINDING_FOR_LIVE_RUN=ABSENT
REAL_RESEARCH_COMPONENT_CONTENT_SCOPE_VERIFICATIONS=ABSENT
REAL_RESEARCH_COMPONENT_SENTINEL_FIXTURE_SET_FOR_LIVE_RUN=ABSENT
REAL_RESEARCH_COMPONENT_GUARD_SNAPSHOT=ABSENT
COMPONENT_EXACT_RUN_MANIFEST=ABSENT
COMPONENT_SUCCESSOR_EXECUTION_AUTHORITY=NONE
COMPONENT_MODEL_EXECUTION_OCCURRED=NO
COMPONENT_TRAINING_OCCURRED=NO
```

The canonical PR #144 contracts are capable of validating these records once a separately authorized exact execution subject exists; they do not generate or self-certify real evidence.

## 7. Operational execution-subject bindings remain unresolved

The later shared runtime evidence and identity-binding policy do not fabricate the exact future component subject. The following remain unresolved for any future conversion-bearing component execution:

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

These are concrete operational facts. Repository prose cannot truthfully replace them.

## 8. Contamination, A1-A14, A15, winner, and training remain downstream

No new authority or evidence was found that changes the following component state:

```text
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
COMPONENT_RESOURCE_ACCESS_BINDINGS=INCOMPLETE
COMPONENT_A1_A14_EQUIVALENT_EXACT_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
COMPONENT_BACKBONE_WINNER=NEEDS_EVIDENCE
COMPONENT_TRAINING_AUTHORITY=NONE
```

Contamination assessment is not moved earlier: existing canonical ordering requires its own separately satisfied prerequisites and authority. No payload access or execution is inferred from continuation approval.

## 9. Current component state

The genuinely advanced state relative to V9 is limited but material:

```text
COMPONENT_SCOPE_POLICY_IDENTITY=PASS_CANONICAL
COMPONENT_SCOPE_OFFLINE_ENFORCEMENT=PASS_CANONICAL_IMPLEMENTED
COMPONENT_REPOSITORY_REVIEW_GATE=REMOVED_BY_FD_007
COMPONENT_SHARED_TOOLCHAIN_RUNTIME_EVIDENCE=PASS_CANONICAL
COMPONENT_HISTORICAL_HASH_RECONSTRUCTION_POLICY_BLOCKER=REMOVED_BY_CANONICAL_POLICY
COMPONENT_REAL_GUARD_EVIDENCE=ABSENT
COMPONENT_SPECIFIC_EXECUTION_SUBJECT_RUNTIME_BINDING=ABSENT
COMPONENT_CONVERSION_PREREQUISITES=INCOMPLETE
COMPONENT_CONTAMINATION_PREREQUISITES=INCOMPLETE
COMPONENT_RESOURCE_ACCESS_BINDINGS=INCOMPLETE
COMPONENT_SUCCESSOR_EXECUTION_AUTHORITY=NONE
COMPONENT_A15=ABSENT_NOT_AUTHORIZED
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
COMPONENT_E005_STATE=NOT_REACHED
COMPONENT_TRAINING_AUTHORITY=NONE
PROJECT_FINISHED=NO
```

## 10. Dependency-safe next frontier

The next real transition cannot be manufactured by another reviewer or another rebuild diagnostic. The consumed diagnostic remains closed and no repository reviewer is required by default.

The next candidate work must instead satisfy concrete, dependency-correct evidence for the exact component execution subject and applicable A1-A14 prerequisites. Any unit that needs model/source-weight access, conversion, contamination execution, A15 activation, training, credentials, protected data, or spend still requires its separately applicable authority before execution.

Repository-only work remains eligible only where it creates or repairs deterministic contracts, freezes already knowable non-secret identities, or reconciles newly existing evidence without asserting absent operational facts.

## 11. Claims and authority boundary

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
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 12. Repository qualification under FD-007

This reconciliation requires no independent repository reviewer or reviewer `MATERIAL_BLOCKER=NO` sentinel. Before merge, its exact base/head/diff, applicable CI/status checks, unresolved threads, and authority-preservation statements must be reverified directly against live GitHub truth.
