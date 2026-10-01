# E004 Registry Current-State Reconciliation V52 — 2026-09-09

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Predecessor:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v51-2026-09-08.md`
**Evidence correction:** `specs/007-sft-v1/e004-operational-preflight-v2-evidence-correction-2026-09-09.md`
**Artifact class:** append-only current-state / evidence-correction overlay
**Authority effect:** NONE BEYOND FAIL-CLOSED SUSPENSION OF STALE V3 AUTHORITY
**Execution effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Advance the current E004 view after direct reinspection of the immutable V2 GitHub Actions job log proved that V51 and the V3 decision surfaces inherited a material factual error about the V2 terminal failure frontier.

Historical V1 and V2 runs remain immutable and consumed. The old reconciliation documents remain in repository history, but their contradicted V2 failure interpretation is superseded by the 2026-09-09 evidence correction.

## 2. Corrected V2 terminal evidence

```text
V2_EVIDENCE_RUN_ID=34176481565
V2_EVIDENCE_JOB_ID=101906795703
V2_EVIDENCE_RUN_ATTEMPT=1
V2_EVIDENCE_RUN_HEAD=225d0ebe280a4ae2305dcc84dd5795ba90d198d0
V2_IMPLEMENTATION_CANONICAL_MERGE=a1bc59ca4fa7ab9d3e0dc92346093eb444b504b0
V2_EVIDENCE_RUN_CONCLUSION=failure
```

The exact workflow validates provisioning hosts before constructing the dependency manifest. The retained job log records:

```text
V2_SAVED_DEPENDENCY_ARTIFACT_FILENAME_COUNT=27
V2_SAVED_DEPENDENCY_ARTIFACT_FILENAMES_MATCH_HISTORICAL_27_SET=YES
V2_UNEXPECTED_PROVISIONING_HOST=download-r2.pytorch.org
V2_TERMINAL_FAILURE_GATE=TRANSFORMERS_PROVISIONING_HOST_POLICY
DEPENDENCY_ARTIFACT_COUNT_GATE=NOT_EXECUTED
DEPENDENCY_SET_MANIFEST_SHA256_COMPARISON=NOT_EXECUTED
TRANSFORMERS_RUNTIME_RECONSTRUCTION=FAIL_BEFORE_DEPENDENCY_MANIFEST_CREATION
```

The historical 27-artifact manifest remains independently proven by the earlier successful runtime-binding run:

```text
HISTORICAL_DEPENDENCY_ARTIFACT_COUNT=27
HISTORICAL_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
```

The V2 run did not execute the manifest count or digest equality checks, so no V2 observed manifest digest is claimed.

## 3. Superseded V51 interpretation

The following V51 assertions are not current truth:

```text
OBSERVED_DEPENDENCY_ARTIFACT_COUNT=28
DEPENDENCY_ARTIFACT_COUNT_GATE=FAIL
OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_FAIL_CLOSED_TRANSFORMERS_DEPENDENCY_SET_DRIFT
```

Current replacement:

```text
V2_OBSERVED_SAVED_WHEEL_FILENAME_COUNT=27
V2_DEPENDENCY_COUNT_COMPARISON=NOT_EXECUTED
V2_TERMINAL_FAILURE=UNEXPECTED_PUBLIC_PROVISIONING_HOST_download-r2.pytorch.org
OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_FAIL_CLOSED_TRANSFORMERS_PROVISIONING_HOST_POLICY_MISMATCH
```

## 4. Effect on V3 decision authority

PR #315 canonically captured the exact Founder Decision B token at merge `ce5dc8f4dda49270e5bb4bebc936ce7514a9b9e9`. That decision capture conditions its effect on the canonical V3 decision-request constraints remaining satisfied.

The decision request materially described V2 as a 28-versus-27 dependency-set drift failure. Direct immutable log evidence now disproves that premise. The existing V3 decision token is preserved historically but must fail closed as stale for future implementation/execution authority.

```text
V3_DECISION_CAPTURE_PR=315
V3_DECISION_CAPTURE_MERGE=ce5dc8f4dda49270e5bb4bebc936ce7514a9b9e9
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION_B
V3_DECISION_B_CAPTURE_STATUS=CANONICAL_BUT_MATERIALLY_STALE_AFTER_EVIDENCE_CORRECTION
V3_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=SUSPENDED_PENDING_CORRECTED_FOUNDER_REVALIDATION
V3_OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=SUSPENDED_PENDING_CORRECTED_FOUNDER_REVALIDATION
V3_OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=SUSPENDED_PENDING_CORRECTED_FOUNDER_REVALIDATION
V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=SUSPENDED_PENDING_CORRECTED_FOUNDER_REVALIDATION
V3_EVIDENCE_MARKER_AUTHORITY=NONE
```

No V3 workflow, evidence branch, marker, or empirical attempt exists at this reconciliation point.

## 5. Corrected prospective V3 design facts available for a later revalidation

The repository now has defensible prior evidence for two facts that a corrected V3 proposal may use prospectively if separately reauthorized:

```text
PROVEN_HISTORICAL_DEPENDENCY_ARTIFACT_SET_COUNT=27
PROVEN_HISTORICAL_DEPENDENCY_ARTIFACT_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
PROVEN_REQUIRED_TORCH_PUBLIC_ROUTE_HOST=download-r2.pytorch.org
PROVEN_REQUIRED_TORCH_PUBLIC_ROUTE_PORT=443
```

A later V3 implementation should freeze the exact historical 27-artifact identity explicitly rather than run an unconstrained resolver and should include `download-r2.pytorch.org` only as an explicitly reviewed public provisioning host for the exact frozen Torch artifact. This is a prospective design candidate, not runtime PASS evidence.

## 6. One-shot and safety state

```text
V1_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_RERUN_AUTHORITY=NONE
V2_RETRY_AUTHORITY=NONE
V2_REPLAY_AUTHORITY=NONE
V2_SECOND_MARKER_AUTHORITY=NONE
V3_AUTHORIZED_RUNS_EXECUTED=0
V3_EVIDENCE_RUN_AUTHORITY=NONE_PENDING_REVALIDATION
MODEL_WEIGHT_ACQUISITION=PROHIBITED
MODEL_LOAD=PROHIBITED
MODEL_INFERENCE=PROHIBITED
EVALUATION_PAYLOAD_ACCESS=PROHIBITED
EVALUATION_PAYLOAD_EXECUTION=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING=PROHIBITED
PRIVATE_CREDENTIAL_USE=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 7. Current disposition

```text
CURRENT_GLOBAL_FRONTIER=CORRECTED_POST_CANONICAL_FOUNDER_V3_REVALIDATION_DECISION
V1_OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_TERMINAL_FAILURE
V1_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_FAIL_CLOSED_TRANSFORMERS_PROVISIONING_HOST_POLICY_MISMATCH
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V3_PREVIOUS_DECISION_B=CANONICAL_BUT_MATERIALLY_STALE
V3_IMPLEMENTATION_AUTHORITY=SUSPENDED_PENDING_CORRECTED_FOUNDER_REVALIDATION
V3_EMPIRICAL_ATTEMPT_AUTHORITY=SUSPENDED_PENDING_CORRECTED_FOUNDER_REVALIDATION
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
LIVE_A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

## 8. Dependency-safe next transition

Canonically expose a corrected Founder revalidation decision surface. Generic continuation language and the stale V3 Decision B token do not create corrected authority.
