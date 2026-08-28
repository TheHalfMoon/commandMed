# E004 Registry Current-State Reconciliation V4 — 2026-08-28

**Spec:** 007 SFT V1  
**Artifact class:** append-only current-state reconciliation  
**Canonical base:** `db2943b0f6da8af74ab4080d0b2f79ebb0b292a0`  
**Canonical base tree:** `a91d9873d70f6c31bd49e84dcc5a9546781646e7`  
**Authority effect:** NONE  
**Execution effect:** records already-completed bounded build-evidence execution only  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## Purpose

Reconcile the live Spec 007 / E004 frontier after the single canonically bounded Decision B GitHub Actions build-evidence allowance was exercised through a fresh manual `workflow_dispatch` run and completed successfully.

Earlier current-state records remain immutable historical evidence. This V4 record supersedes only stale **current-state interpretation** in V3 that said the build-only manual allowance was unconsumed, no authorized manual build run had executed, and no build evidence existed.

```text
HISTORICAL_RECORDS_PRESERVED=YES
V1_V2_V3_REGISTRY_RECONCILIATIONS_PRESERVED=YES
PR123_HISTORY_PRESERVED=YES
E002_LOCAL_INTEGRITY_EVIDENCE_PRESERVED=YES
AUTHORITY_EXPANDED=NO
MODEL_OR_BENCHMARK_EXECUTION_CREATED=NO
MODEL_CONVERSION_AUTHORITY_CREATED=NO
CONTAMINATION_AUTHORITY_CREATED=NO
TRAINING_AUTHORITY_CREATED=NO
```

## Canonical pre-run authority chain

The run was bounded by the canonical Decision B authority chain already present on the exact run head:

```text
RUN_HEAD=db2943b0f6da8af74ab4080d0b2f79ebb0b292a0
RUN_HEAD_TREE=a91d9873d70f6c31bd49e84dcc5a9546781646e7
LIVE_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
LIVE_WORKFLOW_GIT_BLOB_SHA1=710cb4e6ecf1b34e93d3dfa3d59e24c3d60d1d79
LIVE_WORKFLOW_QUALIFIED_SHA256=836175ee057e2a6802b47db00766119d54c2034b63c8487f138dc125285f226b
MAX_AUTHORIZED_WORKFLOW_RUNS=1
AUTHORIZED_TRIGGER=workflow_dispatch_only
AUTHORIZED_RUNNER_LABEL=ubuntu-24.04
AUTHORIZED_PURPOSE=E004_LLAMA_QUANTIZE_BUILD_EVIDENCE_ONLY
PAID_OR_LARGER_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

This record does not reinterpret the build authority as conversion authority. The executable built by the run was evidence material on an ephemeral GitHub-hosted runner only.

## Exact run identity

Live GitHub Actions metadata binds the manual run as:

```text
RUN_ID=33187438094
WORKFLOW_ID=344405846
CHECK_SUITE_ID=89942505201
RUN_NUMBER=3
RUN_ATTEMPT=1
RUN_EVENT=workflow_dispatch
RUN_BRANCH=main
RUN_HEAD_SHA=db2943b0f6da8af74ab4080d0b2f79ebb0b292a0
RUN_STATUS=completed
RUN_CONCLUSION=success
RUN_CREATED_AT=2026-08-28T15:54:50Z
RUN_UPDATED_AT=2026-08-28T15:58:22Z
RUN_PULL_REQUEST_COUNT=0
```

The run therefore matches the sole authorized trigger and exact canonical head that contained the reviewed live workflow.

```text
TRIGGER_IDENTITY_MATCH=YES
RUN_BRANCH_MATCH=YES
RUN_HEAD_MATCH_CANONICAL_PRE_RUN_HEAD=YES
RUN_COUNT_WITH_WORKFLOW_DISPATCH_AFTER_THIS_RUN=1
AUTHORIZED_BUILD_MANUAL_RUN_EXECUTED=YES
AUTHORIZED_BUILD_MANUAL_RUN_ALLOWANCE_REMAINING=0
NO_SECOND_MANUAL_RUN_AUTHORIZED=YES
```

No rerun is authorized merely because the one bounded run has now completed.

## Exact job and step result

The run contained one build-evidence job:

```text
JOB_ID=98903988417
JOB_NAME=build-evidence
JOB_STATUS=completed
JOB_CONCLUSION=success
```

All six job steps completed successfully:

```text
STEP_1_SET_UP_JOB=success
STEP_2_FAIL_CLOSED_RUNNER_PREFLIGHT=success
STEP_3_MATERIALIZE_AND_VERIFY_EXACT_PUBLIC_SOURCE=success
STEP_4_CONFIGURE_AND_BUILD_WITH_EXACT_TOOLS_IN_ISOLATED_NAMESPACE=success
STEP_5_EMIT_BUILD_EVIDENCE_TO_LOG_ONLY=success
STEP_6_COMPLETE_JOB=success
```

GitHub reports no uploaded workflow artifacts:

```text
WORKFLOW_ARTIFACT_COUNT=0
ACTIONS_ARTIFACT_PERSISTENCE_OCCURRED=NO
```

## Runner and runtime identity observed on run 33187438094

The job log records:

```text
RUNNER_VERSION=2.336.0
RUNNER_IMAGE_PROVISIONER_VERSION=20260819.586
RUNNER_OS=Linux
RUNNER_ARCH=X64
RUNNER_IMAGE=ubuntu-24.04
RUNNER_IMAGE_OS=ubuntu24
RUNNER_IMAGE_VERSION=20260823.283.1
OPERATING_SYSTEM=Ubuntu_24.04.4_LTS
KERNEL_IDENTITY=Linux_6.17.0-1022-azure_x86_64
GIT_VERSION=2.55.0
CMAKE_VERSION=3.31.6
NINJA_VERSION=1.13.2
C_COMPILER_VERSION=GNU_13.3.0
CXX_COMPILER_VERSION=GNU_13.3.0
PYTHON_VERSION=3.12.3
GLIBC_VERSION=2.39
SUDO_VERSION=1.9.15p5
UNSHARE_VERSION=util-linux_2.39.3
SETPRIV_VERSION=util-linux_2.39.3
```

The preflight also emitted exact executable hashes:

```text
BASH_PATH=/usr/bin/bash
BASH_SHA256=bc5945feb8bd26203ebfafea5ce1878bb2e32cb8fb50ab7ae395cfb1e1aaaef1
ENV_PATH=/usr/bin/env
ENV_SHA256=0aefff8f912fb75716c5d4de3b6acde93edbe8fa280fc8ee895c1226d3e373ef
ID_PATH=/usr/bin/id
ID_SHA256=9f2e8d80e1c357b889e1b827566e882411ddc6ff45a70196e808f00e62a6c7c5
GIT_PATH=/usr/bin/git
GIT_SHA256=d4d2ba562243015206d4248edfec871a74786499292d00ed072dbca2f5ae8073
CMAKE_PATH=/usr/local/bin/cmake
CMAKE_SHA256=c4b3b237dc7a013590db9e90f70fca2dfdedde09521e920d3339569ea364230a
NINJA_PATH=/usr/local/bin/ninja
NINJA_SHA256=607e668f90dd6cd82e1a42ae572647ad1b1fd43063964295b9547836d8c15d99
C_COMPILER_PATH=/usr/bin/x86_64-linux-gnu-gcc-13
C_COMPILER_SHA256=1b99826121ae6682a634e5efe09bd3e3df58ce58e0b28f849114ab5b89139c26
CXX_COMPILER_PATH=/usr/bin/x86_64-linux-gnu-g++-13
CXX_COMPILER_SHA256=1353e9bdd29a7295c7226bf6c63abccce056d8cac31f112e5cdbecc3f28c2769
PYTHON_PATH=/usr/bin/python3.12
PYTHON_SHA256=1643dacd9feaedc58f3cc581e4d22577dfe25c09b10282936186ccf0f2e61118
SUDO_PATH=/usr/bin/sudo
SUDO_SHA256=136f2e48b0295b9fc595b8259cf2411ac43f27ddbfe02b956649ddaa2e92b9fa
UNSHARE_PATH=/usr/bin/unshare
UNSHARE_SHA256=51bcc77ba5db162c80028f861f0a2770d728c1de80773816d863f28d7a817adb
SETPRIV_PATH=/usr/bin/setpriv
SETPRIV_SHA256=96b083b79c32fd2f0c29657e88e20c7495839349fc64ad5d0503f32d26bf8733
```

## Exact source identity

The workflow fetched only the authorized public tool source and verified both exact Git identities before configure/build:

```text
TOOL_REPOSITORY_URL=https://github.com/ggml-org/llama.cpp.git
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
SOURCE_COMMIT_MATCH=YES
SOURCE_TREE_MATCH=YES
SOURCE_WORKTREE_DIRTY=NO_BY_FAIL_CLOSED_STEP_SUCCESS
```

No model repository or model weight was fetched by this build-evidence run.

## Configure/build security boundary

The run executed configure/build inside the exact bounded isolation mechanism required by the canonical authority record.

Observed assertions include:

```text
CONFIGURE_BUILD_UID=1001
CONFIGURE_BUILD_GID=1001
CAP_INHERITABLE=0000000000000000
CAP_PERMITTED=0000000000000000
CAP_EFFECTIVE=0000000000000000
CAP_BOUNDING=0000000000000000
CAP_AMBIENT=0000000000000000
NO_NEW_PRIVS=1
CONFIGURE_BUILD_HOME=/home/runner/work/_temp/e004-home
CONFIGURE_BUILD_TMPDIR=/home/runner/work/_temp
CONFIGURE_BUILD_PATH=/usr/local/bin:/usr/bin
CONFIGURE_BUILD_LC_ALL=C
CONFIGURE_BUILD_LANG=C
SENSITIVE_PLATFORM_ENV_PRESENT=NO
CONFIGURE_BUILD_NETWORK_NAMESPACE=isolated
CONFIGURE_BUILD_PRIVILEGE=unprivileged_no_new_privs_no_capabilities
```

The CMake binding observed after configuration was:

```text
CMAKE_GENERATOR=Ninja
CMAKE_MAKE_PROGRAM=/usr/local/bin/ninja
CMAKE_C_COMPILER=/usr/bin/cc
CMAKE_CXX_COMPILER=/usr/bin/c++
```

The bounded build configuration and target were the already-authorized exact subject. The target completed all 254 build steps and linked the expected executable.

## Build evidence identity

The successful job emitted:

```text
SECURITY_EVIDENCE_SHA256=950f9e63c8b2418d07f1de3876ae4cec7e2dedd5ba8477c3eb3d1aabbf3096c3
CMAKE_CACHE_SHA256=0b499b1dfa63d0f3fcf80cb3c0f45b25b95de2b5cd128574cc3d1e5f49ad0599
COMPILE_COMMANDS_SHA256=567ad70c6090af9fcce508c41eddba51681669f1079e52e6c285c5cc471d713e
LLAMA_QUANTIZE_EPHEMERAL_PATH=/home/runner/work/_temp/e004-llama.cpp-build/bin/llama-quantize
LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
LLAMA_QUANTIZE_INTEGER_BYTES=6513680
LLAMA_QUANTIZE_FORMAT=ELF_64_BIT_LSB_PIE_X86_64_GNU_LINUX_DYNAMIC
LLAMA_QUANTIZE_BUILD_ID_SHA1=c3b1ffcb29aa0b069380b8aaf7aef6e4928f5738
BUILD_EVIDENCE_MANIFEST_SHA256=84f4915eee7b577feb71ea7daf57a6d16fdf86b1ac2771234599cf52ca6032c8
```

Linked-library inspection was emitted in the job log and showed the expected dynamic runtime linkage, including `libstdc++.so.6`, `libm.so.6`, `libgcc_s.so.1`, `libc.so.6`, and the GNU/Linux dynamic loader.

## Credential, persistence, and spend interpretation

The exact workflow uses `permissions: {}`, prohibits token/secret references by workflow steps, resets inherited environment before configure/build, and the runtime assertion reported:

```text
SENSITIVE_PLATFORM_ENV_PRESENT=NO
```

The run used the canonical standard GitHub-hosted public-repository runner class. No larger/paid runner, package installation, cache upload, artifact upload, release asset, or package publication was required or observed.

The workflow does not emit a standalone billing statement from GitHub's billing system. Therefore this record does not fabricate a provider billing ledger row. It records the bounded authority and observable execution facts separately:

```text
AUTHORIZED_SPEND_USD=0
PAID_OR_LARGER_RUNNER_USED=NO
NONZERO_SPEND_REQUIRED_BY_RUN=NO
PROVIDER_BILLING_LEDGER_ROW_EXPOSED_TO_CONNECTED_EXECUTOR=NO
INFERRED_HIDDEN_BILLING_VALUE=PROHIBITED
```

No later work may use this run to create spend authority.

## Build-only lane current interpretation

The prior V3 build state is superseded by the exact live run evidence above.

Historical V3 state:

```text
WORKFLOW_DISPATCH_RUN_COUNT=0
AUTHORIZED_BUILD_MANUAL_RUN_EXECUTED=NO
AUTHORIZED_BUILD_MANUAL_RUN_ALLOWANCE_REMAINING=1
BUILD_EXECUTION_OCCURRED_ON_GITHUB_ACTIONS_PATH=NO
BUILD_PASS=NO
```

Observed state after run `33187438094`:

```text
WORKFLOW_DISPATCH_RUN_COUNT=1
AUTHORIZED_BUILD_MANUAL_RUN_EXECUTED=YES
AUTHORIZED_BUILD_MANUAL_RUN_ALLOWANCE_REMAINING=0
BUILD_EXECUTION_OCCURRED_ON_GITHUB_ACTIONS_PATH=YES
BUILD_RUN_CONCLUSION=success
BUILD_FAIL_CLOSED_STEPS_ALL_SUCCESS=YES
BUILD_REQUIRED_EXECUTABLE_EMITTED=YES_EPHEMERAL
BUILD_EVIDENCE_LANE_RESULT=PASS_CANDIDATE_PENDING_THIS_RECORD_EXACT_HEAD_QUALIFICATION
```

This record deliberately does not self-qualify its own final head. `BUILD_PASS=YES` becomes canonical current-state language only if the exact final record head is independently checked against run `33187438094`, the canonical authority chain, the one-run count, and the unchanged one-file append-only diff, with no material blocker, and this exact record is then merged canonically.

```text
FINAL_RECORD_EXACT_HEAD_REVIEW_REQUIRED=YES
FINAL_RECORD_EXACT_HEAD_REVIEW_MUST_REQUERY_RUN_33187438094=YES
FINAL_RECORD_EXACT_HEAD_REVIEW_MUST_REQUERY_WORKFLOW_DISPATCH_COUNT=YES
FINAL_RECORD_EXACT_HEAD_REVIEW_MUST_VERIFY_CHANGED_PATH_COUNT_ONE=YES
BUILD_PASS_CANONICAL_CLAIM_BEFORE_QUALIFIED_MERGE=PROHIBITED
```

## Ephemeral build evidence is not a persistent conversion workspace

The built binary and source checkout existed only on the ephemeral GitHub-hosted runner. No workflow artifact was uploaded.

```text
PERSISTENT_LLAMA_QUANTIZE_EXECUTABLE_PRESENT=NO
PERSISTENT_BUILD_DIRECTORY_PRESENT=NO
PERSISTENT_EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
FUTURE_CONVERSION_TIME_SOURCE_PATH=NEEDS_EVIDENCE
FUTURE_CONVERSION_TIME_LLAMA_QUANTIZE_PATH=NEEDS_EVIDENCE
EXACT_LOCAL_OUTPUT_DIRECTORY=NEEDS_EVIDENCE
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS=NEEDS_EVIDENCE
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_EXECUTION_OCCURRED=NO
```

The known ephemeral executable SHA-256 proves the build-evidence subject that existed on run `33187438094`; it does not prove that those bytes are available for a later conversion run.

## Scientific/governance frontier remains unchanged

The build-only run does not satisfy human scientific, governance, personnel, access, finance, contamination, or A15 gates.

```text
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1
G1_A5_REAL_GATE_PASS=NO
G2_A6_REAL_GATE_PASS=NO
G3_A8_REAL_GATE_PASS=NO
G4_A12_REAL_GATE_PASS=NO
REAL_PERSONNEL_ACCESS_FINANCE_EVIDENCE=INCOMPLETE
REAL_A1_TO_A14_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
```

Repository/AI review cannot impersonate the required qualified clinical/statistical review, independent governance/privacy/rights evidence, real personnel/access/finance evidence, or A15 activation. The no-outreach boundary remains active.

## Contamination ordering remains unchanged

```text
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION=NOT_STARTED
A11_ORDERING_PRESERVED=YES
D34_H1_I1_F1_J1_A15_DEPENDENCY_ORDER_PRESERVED=YES
```

No contamination assessment is authorized or implied by successful build evidence.

## E004 tournament execution remains blocked

This build-evidence run compiled a conversion utility only. It did not acquire model weights, load a model, convert model weights, quantize model weights, access benchmark payloads, run inference, run the tournament, perform device qualification, or select a backbone.

```text
E004_BUILD_EVIDENCE_EXECUTION_OCCURRED=YES
E004_TOURNAMENT_EXECUTION_OCCURRED=NO
MODEL_WEIGHT_LOADING_OCCURRED=NO
MODEL_CONVERSION_OCCURRED=NO
MODEL_WEIGHT_QUANTIZATION_OCCURRED=NO
MODEL_INFERENCE_OCCURRED=NO
BENCHMARK_EXECUTION_OCCURRED=NO
DEVICE_QUALIFICATION_OCCURRED=NO
BACKBONE_SELECTION_OCCURRED=NO
```

Therefore E004 cannot be checked complete and E005 cannot begin.

## Proposed authoritative current state after exact-head qualification and canonical merge

Subject to the exact-head and post-merge requirements above, the current state represented by this record is:

```text
SPEC007_LIFECYCLE=AUTHORIZED_TO_START
E001=CLOSED_CANONICAL
E002=CLOSED_CANONICAL
E003=CLOSED_CANONICAL
E002_EPHEMERAL_LOCAL_INTEGRITY_EVIDENCE=PASS
E004_BOUNDED_BUILD_EVIDENCE=PASS_ON_RUN_33187438094
BUILD_PASS=YES_BOUNDED_BUILD_EVIDENCE_LANE_ONLY
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_TOURNAMENT_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Any older current-state statement that says the Decision B build allowance remains unconsumed, no authorized manual build run has executed, or no `llama-quantize` build evidence exists must now be interpreted through run `33187438094` and this later reconciliation once canonically qualified.

## Current frontier after the bounded build-evidence transition

The bounded build-evidence transition resolves only the build-only lane. The remaining real frontier is still blocked by independently governed prerequisites.

```text
LATEST_REAL_TRANSITION=E004_BOUNDED_BUILD_EVIDENCE_SUCCESS_ON_RUN_33187438094
FURTHEST_CURRENT_STATE=E004_BLOCKED_PREFLIGHT_AFTER_LOCAL_INTEGRITY_AND_BUILD_EVIDENCE
```

Remaining blockers include, at minimum:

1. no persistent conversion-time model source workspace or exact executable path;
2. no model conversion authority and no exact executable conversion argv;
3. T1/A2 real numeric policy and qualified review remain incomplete;
4. downstream D34/A3/A4 and G1-G4 real governance gates remain unresolved;
5. real personnel/access/finance evidence remains incomplete;
6. contamination assessment authority remains absent and A11 has not executed;
7. no real A1-A14 PASS snapshot exists;
8. A15 activation remains absent and separately unauthorized;
9. no E004 tournament model/benchmark/device execution evidence pack exists.

The successful build-only run does not collapse or bypass these dependencies.

## Dependency-safe next work

After this record is canonically qualified, further ordinary work may proceed only if a remaining prerequisite becomes genuinely executable under then-current authority. In particular:

1. no second build `workflow_dispatch` or rerun is authorized;
2. persistent conversion/runtime preparation requires separately bounded then-current authority before execution;
3. real scientific/governance/personnel/access/finance evidence must come through a permitted path and cannot be fabricated by repository/AI review;
4. contamination authority must become separately canonical before A11 execution;
5. A15 may only be reached in the required dependency order after a real A1-A14 PASS snapshot and separate activation authority;
6. E005 remains unreachable until the complete frozen E004 tournament evidence pack exists.

Generic continuation approval does not create any separately gated authority above.

## Capture state

```text
CANONICAL_BASE_AT_CAPTURE=db2943b0f6da8af74ab4080d0b2f79ebb0b292a0
CANONICAL_TREE_AT_CAPTURE=a91d9873d70f6c31bd49e84dcc5a9546781646e7
E002_INTEGRITY_RUN=33183096268
E004_BUILD_EVIDENCE_RUN=33187438094
E004_BUILD_EVIDENCE_JOB=98903988417
E004_BUILD_EVIDENCE_RUN_EVENT=workflow_dispatch
E004_BUILD_EVIDENCE_RUN_CONCLUSION=success
E004_BUILD_WORKFLOW_ARTIFACT_COUNT=0
AUTHORIZED_BUILD_MANUAL_RUN_ALLOWANCE_REMAINING=0

REGISTRY_CURRENT_STATE=V4_CANDIDATE_AFTER_BOUNDED_BUILD_EVIDENCE_RUN
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```
