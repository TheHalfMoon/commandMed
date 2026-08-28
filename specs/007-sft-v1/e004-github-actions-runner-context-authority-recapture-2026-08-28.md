# E004 GitHub Actions Runner-Context Authority Recapture — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `c6a6427447ed38d93a52d381db1a8a6ae4296131`  
**Predecessor exact-subject recapture:** `specs/007-sft-v1/e004-github-actions-location-neutral-authority-recapture-2026-08-28.md` / PR #95  
**Abandoned promotion:** PR #96 / CLOSED_UNMERGED  
**Founder environment decision:** `BUILD_ENVIRONMENT_DECISION_B`  
**Authority class:** successor exact-subject recapture after workflow-validation and evidence-generation defects  
**Runtime/model authority expansion:** NONE  
**Live workflow on canonical main:** NO  
**Build execution occurred:** NO  
**Build pass:** NO  
**Current authorized spend:** USD 0

## 1. Why another successor capture is required

PR #95 canonically qualified location-neutral candidate bytes. PR #96 then attempted exact-byte promotion of that subject to:

```text
.github/workflows/e004-llama-quantize-build-evidence.yml
```

The promotion commit was not merged. GitHub nevertheless created workflow run `33153171634` on PR #96 exact head `3ad3ca3ca35f799cb0d4b8ba704e16196b2ca9c2` when that live-path file was pushed.

Exact provider evidence:

```text
RUN_ID=33153171634
RUN_HEAD_SHA=3ad3ca3ca35f799cb0d4b8ba704e16196b2ca9c2
RUN_EVENT=push
RUN_STATUS=completed
RUN_CONCLUSION=failure
RUN_ATTEMPT=1
RUN_JOBS=0
PR96_MERGED=NO
```

This invalidates the PR #96 claim `WORKFLOW_RUN_EXECUTED=NO`. The run created no job, executed no build step, and produced no build evidence. Therefore:

```text
WORKFLOW_RUN_RECORD_CREATED=YES
WORKFLOW_JOB_EXECUTED=NO
BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
```

No provider run or job created by PR #96 is treated as evidence of toolchain readiness, runtime qualification, model authority, benchmark authority, or spend.

## 2. Defects found before recapture qualification

### 2.1 Invalid workflow-level `runner` context

The PR #95 candidate used the `runner` context inside workflow-level `env`:

```yaml
env:
  SOURCE_DIR: ${{ runner.temp }}/e004-llama.cpp
  BUILD_DIR: ${{ runner.temp }}/e004-llama.cpp-build
  E004_HOME: ${{ runner.temp }}/e004-home
  SECURITY_EVIDENCE: ${{ runner.temp }}/e004-security-boundary.txt
```

GitHub Actions context-availability documentation states that workflow-level `env` permits only:

```text
github
secrets
inputs
vars
```

The same documentation states that `jobs.<job_id>.steps.env` permits the `runner` context.

Primary documentation:

```text
https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#context-availability
```

The observed zero-job failed push run is consistent with workflow validation failing before job scheduling. No stronger provider error message is fabricated because no workflow job/log exists.

### 2.2 Required compile-command evidence was not explicitly generated

The predecessor subject requires both of the following evidence reads:

```text
sha256sum "$BUILD_DIR/compile_commands.json"
compile_commands_sha256=<sha256 of compile_commands.json>
```

However, its exact CMake configure argv did not explicitly enable compile-command database generation.

CMake documentation states that `CMAKE_EXPORT_COMPILE_COMMANDS`, when enabled, generates `compile_commands.json`, and that this is supported by the Ninja generator used by the authorized subject.

Primary documentation:

```text
https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html
```

The successor subject therefore adds exactly:

```text
-DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```

This does not authorize another executable target, package, dependency, network endpoint, model operation, persistence mechanism, or spend. It makes an already-required build-evidence field deterministically generatable under the already-authorized Ninja configure step.

## 3. Corrected exact subject

Candidate path remains non-live:

```text
CANDIDATE_PATH=specs/007-sft-v1/candidates/e004-github-actions-build-evidence.workflow.yml.example
PREDECESSOR_CANDIDATE_GIT_BLOB_SHA1=b9ebaa40fa48d41bc2dfecab57368e0fe5647d4a
PREDECESSOR_CANDIDATE_SHA256=b422568fa535a29f6887cad2b158c3bbad059c8bbb4999c3ca5a75e5e840332f
INTERMEDIATE_RUNNER_CONTEXT_FIXED_BLOB_SHA1=c5bc77cce1cdf23cb4fe5c4adc4f12713072eca7
INTERMEDIATE_RUNNER_CONTEXT_FIXED_SHA256=55d28ec4e9c6319482bf0b3147797ace6b525c3cbd5e85f43f8741819cdb663a
NEW_CANDIDATE_GIT_BLOB_SHA1=15d915aab40e53daf7e6937b01e021ae97ccbbe8
NEW_CANDIDATE_SHA256=47c4c1217f9b56415840ac1475f4a3d8ae24b8f967d9cad702cc9c5e4880357f
DIGEST_BINDING_EVIDENCE=LOCAL_BYTE_LEVEL_CROSSCHECK_MATCHED_GITHUB_GIT_BLOB
INDEPENDENT_DIGEST_RECOMPUTE=PENDING_EXACT_HEAD_REVIEW
INTENDED_LIVE_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
```

The first correction removes all `runner.temp` expressions from workflow-level `env` and binds the same derived paths only in step-level `env`, where the `runner` context is permitted.

Static workflow-level values remain at workflow scope:

```text
TOOL_REPOSITORY_URL
TOOL_COMMIT
TOOL_TREE
GIT_TERMINAL_PROMPT
GIT_CONFIG_NOSYSTEM
GIT_ASKPASS
SSH_ASKPASS
```

Runner-derived path values are step-scoped only:

```text
SOURCE_DIR
BUILD_DIR
E004_HOME
SECURITY_EVIDENCE
HOME
```

The second correction adds only `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON` to the already-bounded CMake configure argv so that the already-required `compile_commands.json` evidence exists under Ninja.

GitHub independently reports the final corrected candidate as Git blob `15d915aab40e53daf7e6937b01e021ae97ccbbe8` on candidate commit `f00f678d2f5818ab288bbfe22d1e238c39b1ed4b`.

A local byte-level reconstruction of the final candidate produced Git blob SHA-1 `15d915aab40e53daf7e6937b01e021ae97ccbbe8`, matching GitHub exactly, and SHA-256 `47c4c1217f9b56415840ac1475f4a3d8ae24b8f967d9cad702cc9c5e4880357f`. Fresh independent exact-head review must recompute and confirm that digest before this recapture can qualify.

## 4. Runtime/security invariants preserved

This recapture does not authorize a new runtime purpose. The intended values and boundaries remain unchanged except for the explicit evidence-only CMake export flag described above:

```text
PROVIDER=GitHub_Actions
RUNNER_LABEL=ubuntu-24.04
TRIGGER=workflow_dispatch_only
WORKFLOW_PERMISSIONS={}
TOOL_REPOSITORY_URL=https://github.com/ggml-org/llama.cpp.git
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
BUILD_TARGET=llama-quantize
CMAKE_EXPORT_COMPILE_COMMANDS=ON
TIMEOUT_MINUTES=30
PAID_OR_LARGER_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

The corrections do not weaken:

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

The corrections are not evidence that the future hosted runner has the required tools, namespace behavior, or build compatibility. Those remain runtime evidence requirements.

## 5. Unexpected-run disposition boundary

The observed PR #96 run was not the authorized future manual build-evidence run:

```text
EXPECTED_AUTHORIZED_TRIGGER=workflow_dispatch
OBSERVED_TRIGGER=push
OBSERVED_JOBS=0
OBSERVED_BUILD_EXECUTION=NO
```

This record does **not** silently decide whether provider creation of the zero-job validation run consumes any previously bounded one-manual-run allowance.

```text
AUTHORIZED_MANUAL_RUN_EXECUTED=NO
UNEXPECTED_ZERO_JOB_RUN_OBSERVED=YES
UNEXPECTED_ZERO_JOB_RUN_ID=33153171634
AUTHORIZED_RUN_ALLOWANCE_CONSUMPTION_DISPOSITION=NEEDS_EXACT_REVIEW
FUTURE_MANUAL_DISPATCH_EXERCISABLE=NO
```

A fresh exact-head review must explicitly confirm an evidence-bound disposition before any future manual dispatch can become exercisable.

## 6. Successor promotion sequence

No live workflow may be created from these final corrected bytes until this recapture becomes canonical after fresh exact-head review.

```text
THIS_RECAPTURE_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> THIS_RECAPTURE_CANONICAL
-> FRESH_PROMOTION_BRANCH_FROM_THEN_CURRENT_CANONICAL_MAIN
-> PROMOTED_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
-> PROMOTED_WORKFLOW_GIT_BLOB_EQUALS_NEW_QUALIFIED_CANDIDATE_BLOB=YES
-> PROMOTED_WORKFLOW_SHA256_EQUALS_NEW_QUALIFIED_CANDIDATE_SHA256=YES
-> PROMOTION_PUSH_CREATES_UNEXPECTED_WORKFLOW_RUN=NO
-> FRESH_PROMOTION_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> CANONICAL_PROMOTION_MERGE
-> POST_MERGE_BYTE_VERIFICATION
-> ALL_PRE_RUN_CONDITIONS_STILL_PASS
-> AUTHORIZED_RUN_ALLOWANCE_CONSUMPTION_DISPOSITION_IS_EXPLICIT
-> AT_MOST_ONE_AUTHORIZED_MANUAL_RUN_IF_STILL_AVAILABLE
```

Any further candidate-byte change requires another exact authority capture.

## 7. Current branch state

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
SUCCESSOR_EXACT_AUTHORITY_RECAPTURE=PENDING_FINAL_EXACT_HEAD_REVIEW
NEW_CANDIDATE_GIT_BLOB_SHA1=15d915aab40e53daf7e6937b01e021ae97ccbbe8
NEW_CANDIDATE_SHA256=47c4c1217f9b56415840ac1475f4a3d8ae24b8f967d9cad702cc9c5e4880357f
INDEPENDENT_DIGEST_RECOMPUTE=PENDING_EXACT_HEAD_REVIEW
LIVE_WORKFLOW_ON_CANONICAL_MAIN=NO
CURRENT_RECAPTURE_BRANCH_WORKFLOW_RUNS=0
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

## Exit evidence required

Fresh exact-head review must independently confirm:

```text
PR96_INCIDENT_EVIDENCE_BOUND=YES
ROOT_CAUSE_RUNNER_CONTEXT_AVAILABILITY_DEFECT_CONFIRMED=YES
WORKFLOW_LEVEL_RUNNER_CONTEXT_REFERENCES=0
ALL_RUNNER_CONTEXT_REFERENCES_ARE_IN_ALLOWED_STEP_SCOPE=YES
COMPILE_COMMANDS_EVIDENCE_IS_REQUIRED=YES
COMPILE_COMMANDS_GENERATION_IS_EXPLICIT=YES
CMAKE_EXPORT_COMPILE_COMMANDS_FLAG_IS_EVIDENCE_ONLY=YES
NEW_CANDIDATE_GIT_BLOB_MATCHES=YES
NEW_CANDIDATE_SHA256_RECOMPUTED_AND_BOUND=YES
CORRECTIONS_ARE_LIMITED_TO_CONTEXT_SCOPE_AND_REQUIRED_EVIDENCE_GENERATION=YES
PREDECESSOR_RUNTIME_SECURITY_LIMITS_UNCHANGED=YES
NO_LIVE_WORKFLOW_CREATED_BY_THIS_RECAPTURE=YES
NO_WORKFLOW_RUN_CREATED_BY_THIS_RECAPTURE=YES
UNEXPECTED_RUN_ALLOWANCE_DISPOSITION_IS_EXPLICIT=YES
NO_DOWNSTREAM_AUTHORITY_EXPANSION=YES
BUILD_PASS_REMAINS_NO=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Any material finding must be repaired before canonical merge.
