# E004 GitHub Actions Authority-Safe Successor Recapture — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `c6a6427447ed38d93a52d381db1a8a6ae4296131`  
**Canonical controlling authority:** `specs/007-sft-v1/e004-github-actions-exact-authority-capture-2026-08-28.md` at `c6a6427447ed38d93a52d381db1a8a6ae4296131`  
**Predecessor candidate recapture:** PR #95  
**Abandoned promotion:** PR #96 / CLOSED_UNMERGED  
**Founder environment decision:** `BUILD_ENVIRONMENT_DECISION_B`  
**Authority class:** successor exact-subject recapture after validation, privilege-purpose, and tool-identity defects  
**Runtime/model authority expansion:** NONE  
**Live workflow on canonical main:** NO  
**Build execution occurred:** NO  
**Build pass:** NO  
**Current authorized spend:** USD 0

## 1. PR #96 incident

PR #96 placed the then-qualified non-live subject at:

```text
.github/workflows/e004-llama-quantize-build-evidence.yml
```

PR #96 was never merged. GitHub nevertheless created provider run `33153171634` on exact head `3ad3ca3ca35f799cb0d4b8ba704e16196b2ca9c2`.

```text
RUN_ID=33153171634
RUN_EVENT=push
RUN_STATUS=completed
RUN_CONCLUSION=failure
RUN_ATTEMPT=1
RUN_JOBS=0
PR96_MERGED=NO
WORKFLOW_JOB_EXECUTED=NO
BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
```

The earlier PR #96 claim that no workflow run existed is superseded. The zero-job provider record is not build evidence and creates no runtime, model, benchmark, training, procurement, or spend authority.

## 2. Defect A — invalid workflow-level `runner` context

The PR #95 candidate referenced `${{ runner.temp }}` in workflow-level `env`. GitHub Actions context-availability rules do not permit the `runner` context there and do permit it at `jobs.<job_id>.steps.env`.

Primary source:

```text
https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#context-availability
```

The successor moves the same runner-derived path bindings into step-level `env` only.

```text
WORKFLOW_LEVEL_RUNNER_CONTEXT_REFERENCES=0
RUNNER_TEMP_REFERENCES_OUTSIDE_STEP_ENV=0
```

The PR #96 zero-job failed `push` run is consistent with pre-job workflow validation failure. No more specific provider error is fabricated because no job or job log exists.

## 3. Defect B — root execution outside the authorized purpose

The predecessor candidate contained:

```text
sudo -n true
```

The canonical controlling authority states:

```text
ROOT_PRIVILEGE_PURPOSE=NETWORK_NAMESPACE_CREATION_ONLY
```

The probe therefore created unnecessary root execution outside the sole authorized root purpose. It is removed. Passwordless sudo and namespace capability are now exercised only by the authorized operation itself:

```text
<exact-sudo-path> -n <exact-unshare-path> --net -- ...
```

If that operation is unavailable, execution fails closed before configure/build.

```text
SUDO_TRUE_PREFLIGHT_PRESENT=NO
ROOT_EXECUTION_OUTSIDE_NAMESPACE_CREATION=NO_BY_SUBJECT
ROOT_PRIVILEGE_PURPOSE=NETWORK_NAMESPACE_CREATION_ONLY
```

## 4. Defect C — post-reset tool identity was not guaranteed

Canonical authority requires both environment reset and path/version/SHA-256 evidence for the shell/core tools, Git, CMake, Ninja, C/C++ compilers, Python, sudo, unshare, and setpriv.

`setpriv --reset-env` resets `PATH`. Upstream util-linux documentation states that the reset PATH is reconstructed from `/etc/login.defs` or a built-in default rather than preserving the caller PATH:

```text
https://man7.org/linux/man-pages/man1/setpriv.1.html
```

Therefore preflight hashes alone did not prove that name-based commands resolved after `--reset-env` were the same executables that had been measured before the boundary.

The successor now:

1. resolves exact absolute paths before the privilege/reset boundary;
2. invokes absolute paths for `sudo`, `unshare`, `setpriv`, `env`, `bash`, `id`, and CMake;
3. passes the exact Git, Ninja, C/C++, Python, and SHA-256 tool paths through the boundary;
4. reconstructs an explicit post-reset `PATH` only from directories of those already-resolved tools;
5. asserts the post-reset `PATH` exactly matches that bounded value;
6. pins `CMAKE_MAKE_PROGRAM`, `CMAKE_C_COMPILER`, and `CMAKE_CXX_COMPILER` to the measured absolute paths; and
7. records the actual build-time tool paths and SHA-256 values inside the hashed security-evidence record.

```text
POST_RESET_TOOL_SELECTION=EXACT_PATH_BOUND
POST_RESET_PATH=EXPLICIT_FROM_PREMEASURED_TOOL_DIRECTORIES
CMAKE_MAKE_PROGRAM=EXACT_PREMEASURED_NINJA_PATH
CMAKE_C_COMPILER=EXACT_PREMEASURED_CC_PATH
CMAKE_CXX_COMPILER=EXACT_PREMEASURED_CXX_PATH
BUILD_TIME_TOOL_IDENTITY_EVIDENCE=BOUND_IN_SECURITY_EVIDENCE
```

This is reproducibility/evidence hardening. It does not add a package, executable target, external endpoint, model operation, persistence mechanism, or authority.

## 5. Fail-closed probe hardening

The predecessor used version probes such as `command --version | head -n 1` under `set -o pipefail`. A producer can receive a closed pipe when `head` exits early, causing an avoidable false failure unrelated to tool availability.

The successor emits the full `ldd --version` and `sudo --version` outputs instead. This changes no authority or build behavior; it removes an unnecessary one-shot failure mode.

## 6. Final successor candidate identity

```text
CANDIDATE_PATH=specs/007-sft-v1/candidates/e004-github-actions-build-evidence.workflow.yml.example
PREDECESSOR_PR95_GIT_BLOB_SHA1=b9ebaa40fa48d41bc2dfecab57368e0fe5647d4a
PREDECESSOR_PR95_SHA256=b422568fa535a29f6887cad2b158c3bbad059c8bbb4999c3ca5a75e5e840332f
RUNNER_CONTEXT_ONLY_INTERMEDIATE_GIT_BLOB_SHA1=c5bc77cce1cdf23cb4fe5c4adc4f12713072eca7
RUNNER_CONTEXT_ONLY_INTERMEDIATE_SHA256=55d28ec4e9c6319482bf0b3147797ace6b525c3cbd5e85f43f8741819cdb663a
ROOT_PURPOSE_FIXED_INTERMEDIATE_GIT_BLOB_SHA1=e8f1a069f88037d2ba139c697bbdffaf6b43ef2a
ROOT_PURPOSE_FIXED_INTERMEDIATE_SHA256=2cc172dfb09efff239ec8e87bfe03adcbe4fdb340e1c229c87561ece4d40f202
ROOT_PURPOSE_FIXED_INTERMEDIATE_DIGEST_SOURCE=CODERABBIT_EXACT_HEAD_RECOMPUTE
FINAL_SUCCESSOR_GIT_BLOB_SHA1=fec1f5908f6b0ec3a87b52af9f3e7f0d4d07f4ca
FINAL_SUCCESSOR_SHA256=NEEDS_FRESH_INDEPENDENT_EXACT_HEAD_HASH
INTENDED_LIVE_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
```

Any further candidate-byte change invalidates the final identity and requires fresh exact-head review.

## 7. Pinned llama.cpp checks

Frozen source identity remains:

```text
TOOL_REPOSITORY_URL=https://github.com/ggml-org/llama.cpp.git
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
BUILD_TARGET=llama-quantize
```

Exact pinned-source review confirms:

- root `CMakeLists.txt` already contains `set(CMAKE_EXPORT_COMPILE_COMMANDS ON)`;
- `tools/quantize/CMakeLists.txt` defines executable target `llama-quantize`.

A temporary PR #98 revision that added `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON` was redundant and is absent from the final subject.

```text
PINNED_SOURCE_ALREADY_EXPORTS_COMPILE_COMMANDS=YES
LLAMA_QUANTIZE_TARGET_PRESENT_AT_PINNED_COMMIT=YES
TEMPORARY_COMPILE_COMMAND_OVERRIDE_IN_FINAL_SUBJECT=NO
```

## 8. Runtime/security invariants preserved

```text
PROVIDER=GitHub_Actions
RUNNER_LABEL=ubuntu-24.04
TRIGGER=workflow_dispatch_only
WORKFLOW_PERMISSIONS={}
BUILD_TARGET=llama-quantize
TIMEOUT_MINUTES=30
PAID_OR_LARGER_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

The successor retains:

```text
PUBLIC_SOURCE_FETCH_ONLY
NO_PACKAGE_INSTALLATION
CONFIGURE_BUILD_NETWORK_NAMESPACE_ISOLATION
ROOT_PRIVILEGE_FOR_NAMESPACE_CREATION_ONLY
NONROOT_CONFIGURE_BUILD
SUPPLEMENTARY_GROUPS_CLEARED
LINUX_CAPABILITIES_DROPPED
NO_NEW_PRIVS_REQUIRED
INHERITED_ENVIRONMENT_RESET
SENSITIVE_PLATFORM_ENVIRONMENT_REJECTED
NO_ACTIONS_CACHE
NO_ARTIFACT_UPLOAD
NO_RELEASE_OR_PACKAGE_PUBLICATION
NO_MODEL_OPERATION
NO_BENCHMARK_OR_DEVICE_OPERATION
NO_CONTAMINATION_ASSESSMENT
NO_SELECTION_SUITE_CONSTRUCTION
NO_TRAINING
NO_PROCUREMENT
```

No static candidate claim is runtime PASS evidence. Tool availability, sudo/namespace behavior, compiler/build behavior, and all emitted identities remain runtime evidence requirements.

## 9. PR #96 run-allowance disposition and exact source attribution

The controlling source for this disposition is not the PR #95 location-neutral recapture. It is the canonical exact authority record:

```text
SOURCE_PATH=specs/007-sft-v1/e004-github-actions-exact-authority-capture-2026-08-28.md
SOURCE_CANONICAL_COMMIT=c6a6427447ed38d93a52d381db1a8a6ae4296131
```

That record explicitly states that it binds conditions under which promotion and **at most one manual run** may become exercisable. Its environment/run envelope contains:

```text
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TRIGGER=workflow_dispatch_only
```

Its fail-closed conditions explicitly contain:

```text
AUTOMATIC_OR_UNEXPECTED_TRIGGER
```

Its promotion/execution section states that the **at-most-one manual build-evidence run** becomes exercisable only after post-merge verification proves the live canonical workflow is byte-identical to the qualified subject and all pre-run conditions remain satisfied.

PR #96 run `33153171634` occurred before canonical promotion, used event `push` rather than `workflow_dispatch`, contained zero jobs, and executed no build.

Therefore:

```text
AUTHORIZED_MANUAL_RUN_EXECUTED=NO
UNEXPECTED_ZERO_JOB_RUN_OBSERVED=YES
AUTHORIZED_RUN_ALLOWANCE_CONSUMPTION_DISPOSITION=DOES_NOT_CONSUM_AUTHORIZED_MANUAL_ALLOWANCE
AUTHORIZED_MANUAL_RUN_ALLOWANCE_REMAINING=1_CONDITIONAL_NOT_YET_EXERCISABLE
FUTURE_MANUAL_DISPATCH_EXERCISABLE=NO
```

This interprets already-canonical exact authority and creates no second run or new authority. Fresh independent exact-head review must verify both the source attribution and disposition.

## 10. Promotion sequence after qualification

```text
FINAL_SUCCESSOR_SHA256_INDEPENDENTLY_RECOMPUTED_AND_BOUND
-> THIS_RECAPTURE_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> THIS_RECAPTURE_CANONICAL
-> FRESH_PROMOTION_BRANCH_FROM_THEN_CURRENT_CANONICAL_MAIN
-> PROMOTED_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
-> PROMOTED_WORKFLOW_BYTES_EQUAL_QUALIFIED_SUCCESSOR_BYTES=YES
-> PROMOTION_PUSH_CREATES_UNEXPECTED_WORKFLOW_RUN=NO
-> FRESH_PROMOTION_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> CANONICAL_PROMOTION_MERGE
-> POST_MERGE_BYTE_VERIFICATION
-> ALL_PRE_RUN_CONDITIONS_STILL_PASS
-> AT_MOST_ONE_AUTHORIZED_MANUAL_WORKFLOW_DISPATCH_RUN
```

The connected GitHub action surface still does not expose workflow-dispatch initiation. If that remains true after canonical promotion, it is an execution-tooling blocker rather than execution evidence or authority revocation.

## 11. Current state

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
SUCCESSOR_EXACT_AUTHORITY_RECAPTURE=PENDING_FINAL_SHA256_AND_EXACT_HEAD_REVIEW
FINAL_SUCCESSOR_GIT_BLOB_SHA1=fec1f5908f6b0ec3a87b52af9f3e7f0d4d07f4ca
FINAL_SUCCESSOR_SHA256=NEEDS_FRESH_INDEPENDENT_EXACT_HEAD_HASH
LIVE_WORKFLOW_ON_CANONICAL_MAIN=NO
BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
CONVERSION_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Raw GitHub Actions API must report zero runs for the final exact PR head before canonical merge.

## Exit evidence required

Fresh exact-head review must independently confirm:

```text
PR96_INCIDENT_EVIDENCE_BOUND=YES
RUNNER_CONTEXT_DEFECT_REPAIRED=YES
UNAUTHORIZED_SUDO_TRUE_PREFLIGHT_REMOVED=YES
ROOT_PRIVILEGE_PURPOSE_MATCHES_CANONICAL_AUTHORITY=YES
POST_RESET_TOOL_SELECTION_IS_EXACT_PATH_BOUND=YES
POST_RESET_PATH_IS_EXPLICIT_AND_BOUNDED=YES
BUILD_TIME_TOOL_IDENTITIES_ARE_EVIDENCE_BOUND=YES
PIPEFAIL_VERSION_PROBE_FALSE_FAILURE_REMOVED=YES
FINAL_SUCCESSOR_GIT_BLOB_MATCHES=YES
FINAL_SUCCESSOR_SHA256_RECOMPUTED_AND_BOUND=YES
PINNED_SOURCE_COMPILE_COMMAND_SETTING_CONFIRMED=YES
LLAMA_QUANTIZE_TARGET_PRESENT_AT_PINNED_COMMIT=YES
RUN_ALLOWANCE_SOURCE_ATTRIBUTION_IS_EXACT=YES
RUN_ALLOWANCE_DISPOSITION_VERIFIED=YES
NO_LIVE_WORKFLOW_CREATED_BY_THIS_RECAPTURE=YES
NO_WORKFLOW_RUN_CREATED_BY_THIS_RECAPTURE=YES
NO_DOWNSTREAM_AUTHORITY_EXPANSION=YES
BUILD_PASS_REMAINS_NO=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Any material finding must be repaired before canonical merge.
