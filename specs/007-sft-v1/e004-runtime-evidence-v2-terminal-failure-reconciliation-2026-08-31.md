# E004 Runtime-Evidence V2 Terminal Failure Reconciliation — 2026-08-31

**Spec:** 007 SFT V1  
**Artifact class:** observed execution-evidence reconciliation  
**Canonical base:** `ef1be50f4a076d9f03abfffee342d2c244b0d199`  
**V2 authority:** `specs/007-sft-v1/e004-connected-executor-dispatch-remediation-v2-authority-2026-08-31.md`  
**V2 authority merge:** `8199eb1684b40e917bcc004fb282018005f9afd6`  
**V2 implementation merge:** `ef1be50f4a076d9f03abfffee342d2c244b0d199`  
**Training authority:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation authority:** NONE  
**Spend authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Reconcile the terminal evidence from the one V2 transport remediation and the one target E004 conversion-runtime evidence run that it successfully created. This record preserves the observed failure, records the strongest currently reviewable Phase A diagnostic hypothesis without promoting it to proven historical cause, consumes the V2/target allowances exactly as executed, and leaves all downstream scientific and execution gates fail-closed.

This record is evidence reconciliation only. It creates no V3 authority, rerun authority, model/conversion authority, contamination authority, A15 authority, training authority, or spend authority.

## 2. Canonical V2 transport result

The V2 transport remediation was canonically admitted through PR #147 and executed once after merge. It successfully created the exact authorized target `workflow_dispatch` run.

```text
V2_BOOTSTRAP_RUN=33366850471
V2_BOOTSTRAP_RESULT=PASS
V2_REMEDIATION_ALLOWANCE_REMAINING=0
V2_TARGET_DISPATCH_CREATED=YES
```

The target run identity is:

```text
TARGET_RUN_ID=33366859146
TARGET_WORKFLOW=.github/workflows/e004-conversion-runtime-evidence.yml
TARGET_EVENT=workflow_dispatch
TARGET_HEAD_BRANCH=e004-runtime-evidence-v2-bind-ef1be50f4a076d9f03abfffee342d2c244b0d199
TARGET_HEAD_SHA=ef1be50f4a076d9f03abfffee342d2c244b0d199
TARGET_RUN_ATTEMPT=1
TARGET_CONCLUSION=failure
TARGET_RUNTIME_EVIDENCE_RUN_ALLOWANCE_REMAINING=0
```

The transient V2 binding branch still exists at reconciliation time:

```text
V2_TRANSIENT_BINDING_BRANCH=e004-runtime-evidence-v2-bind-ef1be50f4a076d9f03abfffee342d2c244b0d199
V2_TRANSIENT_BINDING_BRANCH_CLEANUP=NOT_YET_AUTHORIZED_OR_EXECUTED
```

## 3. Observed target job evidence

GitHub Actions job `99409197359` reports the following terminal step sequence:

```text
RUNNER_LABEL=ubuntu-24.04
RUNNER_PREFLIGHT=PASS
PHASE_A_ALLOWLISTED_PUBLIC_SOURCE_AND_DEPENDENCY_STAGING=FAIL
PHASE_B_OFFLINE_ENVIRONMENT_LOCAL_GGUF_ATTESTATION_AND_REBUILD=SKIPPED
FINAL_RUNTIME_EVIDENCE_MANIFEST=SKIPPED
```

Therefore the run produced no Phase B evidence and no final runtime evidence manifest. No inference may be made that conversion prerequisites passed.

## 4. Phase A static diagnostic hypothesis

The exact target workflow executed at `ef1be50f4a076d9f03abfffee342d2c244b0d199` defines the Phase A CONNECT proxy allowlist as:

```text
github.com
pypi.org
files.pythonhosted.org
download.pytorch.org
```

The same Phase A command requires:

```text
TORCH_REQUIREMENT=torch==2.11.0+cpu
TORCH_INDEX=https://download.pytorch.org/whl/cpu
```

During reconciliation, one connected public-source inspection returned PyTorch CPU-index entries whose `torch-2.11.0+cpu` Linux x86_64 artifact links used `download-r2.pytorch.org`. However the independent exact-head repository reviewer could not reproduce or retain authoritative evidence sufficient to accept that artifact-host route as canonical proof of the historical job failure.

Accordingly this record does not promote the host mismatch to proven cause.

```text
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
PHASE_A_DIAGNOSTIC_HYPOTHESIS=DEPENDENCY_ARTIFACT_HOST_MISSING_FROM_EXACT_ALLOWLIST
PHASE_A_DIAGNOSTIC_CANDIDATE_HOST=download-r2.pytorch.org
PYTORCH_ARTIFACT_ROUTE_CANONICAL_PROOF=ABSENT
```

The upstream llama.cpp commit bound by the workflow remains publicly resolvable with the exact expected tree:

```text
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
TOOL_COMMIT_AVAILABILITY=PASS_PUBLIC_GITHUB
```

That source-commit availability does not prove that source staging completed in the failed run.

## 5. Evidence precision boundary

The connector available during reconciliation did not expose a retained per-command stderr/log payload for historical job `99409197359`. Therefore this record does **not** claim that a particular historical dependency-resolution error or `DENY` log line was recovered from that job.

The admitted evidence is narrower:

1. GitHub observed Phase A fail after runner preflight passed.
2. Phase B and final manifest were skipped.
3. The exact executed workflow requires `torch==2.11.0+cpu` through its bounded proxy/index configuration.
4. `download-r2.pytorch.org` is a concrete diagnostic candidate because it was observed during connected public-source inspection, but the independent reviewer did not establish it as canonical historical cause.
5. A successor must collect direct, retained diagnostic evidence before changing the target workflow or authorizing another target runtime-evidence attempt on this hypothesis.

```text
HISTORICAL_STDERR_RECOVERED=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
STATIC_WORKFLOW_DEFECT_PROVEN=NO
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
```

## 6. Authority and state effect

V2 explicitly provided no automatic V3, rerun, failed-job rerun, or alternate trigger after terminal failure. The target run itself occurred, so its one-run allowance is consumed even though it failed before Phase B.

```text
V2_BOOTSTRAP_RERUN_AUTHORITY=NONE
V2_TARGET_RERUN_AUTHORITY=NONE
FAILED_JOB_RERUN_AUTHORITY=NONE
TARGET_RUNTIME_EVIDENCE_RUN_ALLOWANCE_REMAINING=0
V3_REMEDIATION_AUTHORITY=NONE
V3_TARGET_RUN_AUTHORITY=NONE
LOCAL_EXECUTION_SUBSTITUTE_AUTHORITY=NONE
```

No downstream authority is changed:

```text
MODEL_SOURCE_WEIGHT_ACQUISITION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 7. Current component frontier

The real E004 component remains incomplete. This failure is genuine runtime evidence of a failure during Phase A, not evidence that any scientific prerequisite passed.

```text
COMPONENT_RUNTIME_EVIDENCE=FAILED_PHASE_A
COMPONENT_CONVERSION_PREREQUISITES=INCOMPLETE
COMPONENT_CONTAMINATION_PREREQUISITES=INCOMPLETE
COMPONENT_RESOURCE_ACCESS_BINDINGS=INCOMPLETE
COMPONENT_A1_A14_EQUIVALENT_EXACT_PASS_SNAPSHOT=ABSENT
COMPONENT_A15=ABSENT_NOT_AUTHORIZED
COMPONENT_BACKBONE_WINNER=NEEDS_EVIDENCE
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_RUNTIME_DIAGNOSTIC_EVIDENCE
COMPONENT_E005_STATE=NOT_REACHED
COMPONENT_TRAINING_AUTHORITY=NONE
```

## 8. Next dependency-ordered unit

The smallest technically justified successor is a **separate founder-authorized diagnostic-only V3 unit** that, if canonically admitted, may execute exactly one zero-spend public-runner diagnostic intended only to identify and retain the Phase A dependency-resolution/network route responsible for failure.

Such a diagnostic must not execute the target runtime-evidence workflow, consume or reopen the exhausted V2 target allowance, download or load model weights, perform model conversion or inference, access benchmark payloads, perform contamination assessment, activate A15, train, use private credentials, upload artifacts/caches, or authorize spend.

Only after direct retained diagnostic evidence exists may a later separately reviewed authority decide whether a target-workflow repair and a new target runtime-evidence attempt are justified.

This record does not create that successor authority.

## 9. Exit evidence

This reconciliation is eligible for canonical merge only when exact-head review confirms:

```text
V2_TERMINAL_RUN_IDENTITIES_BOUND=YES
OBSERVED_PHASE_A_FAILURE_PRESERVED=YES
PHASE_B_AND_FINAL_MANIFEST_SKIPPED_PRESERVED=YES
PHASE_A_FAILURE_CAUSE_REMAINS_NEEDS_EVIDENCE=YES
DIAGNOSTIC_HOST_HYPOTHESIS_NOT_PROMOTED_TO_PROOF=YES
HISTORICAL_STDERR_NOT_FABRICATED=YES
V2_ALLOWANCES_REOPENED=NO
V3_AUTHORITY_CREATED=NO
MODEL_CONVERSION_AUTHORITY_CREATED=NO
CONTAMINATION_AUTHORITY_CREATED=NO
A15_AUTHORITY_CREATED=NO
TRAINING_AUTHORITY_CREATED=NO
SPEND_AUTHORITY_CREATED=NO
E004_REMAINS_INCOMPLETE=YES
E005_REMAINS_NOT_REACHED=YES
MATERIAL_BLOCKER=NO
```
