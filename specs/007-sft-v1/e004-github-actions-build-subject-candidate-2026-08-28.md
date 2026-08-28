# E004 GitHub Actions Build Subject Candidate — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical parent:** `16e39bdb9d259da43f416934bd80b199ec7a3518`  
**Canonical decision surface:** `e004-build-environment-authority-decision-request-2026-08-28.md`  
**Artifact class:** non-executable workflow-subject candidate  
**Founder environment decision selected:** NO  
**Workflow promotion authority:** NONE  
**Workflow execution authority:** NONE  
**GitHub Actions execution occurred:** NO  
**Model conversion authority:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

This record reduces the next repository-only preparation gap without selecting `BUILD_ENVIRONMENT_DECISION_B` and without creating a live GitHub Actions workflow.

The candidate is intentionally stored outside `.github/workflows`:

```text
CANDIDATE_PATH=specs/007-sft-v1/candidates/e004-github-actions-build-evidence.workflow.yml.example
CANDIDATE_GIT_BLOB_SHA1=050b53d5ca03ed37d40cd20d5d76066852e92bd9
CANDIDATE_SHA256=3731d1383e41c5a0cc3f1af1efaebe6bbe45b6fc610a0f529bc2053676206053
LIVE_WORKFLOW_PATH_CREATED=NO
LIVE_WORKFLOW_TRIGGER_CREATED=NO
WORKFLOW_PROMOTION_AUTHORITY=NONE
WORKFLOW_EXECUTION_AUTHORITY=NONE
```

The candidate must not be copied, renamed, moved, or promoted into `.github/workflows` unless a separate Founder decision explicitly selects the exact environment class and a fresh review qualifies the exact promoted subject.

## 1. Frozen candidate purpose

The candidate does exactly one future technical job if it is ever separately authorized and promoted:

```text
PURPOSE=BUILD_EVIDENCE_ONLY
TOOL_REPOSITORY=ggml-org/llama.cpp
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
BUILD_TARGET=llama-quantize
RUNNER_LABEL=ubuntu-24.04
TRIGGER=workflow_dispatch_only
WORKFLOW_PERMISSIONS={}
MAX_FUTURE_RUNS_IF_SEPARATELY_AUTHORIZED=1
```

It does not invoke `llama-quantize`; it only builds the already-authorized executable target and emits build/toolchain identity evidence to the job log.

## 2. Static upstream basis

At exact upstream commit `c1d0e7a004015f23bc0233470b747b596f29b264`:

- root `CMakeLists.txt` defines explicit controls for tests, tools, examples, server, app, UI, prebuilt UI, OpenSSL, subprocess support, and LLGuidance;
- the embedded `ggml/CMakeLists.txt` defines `GGML_NATIVE`, `GGML_CCACHE`, and `GGML_OPENMP` controls;
- `tools/quantize/CMakeLists.txt` defines target `llama-quantize`, linking through `llama-quantize-impl` to `llama-common` and `llama`.

The candidate therefore predeclares a bounded configuration instead of accepting default optional surfaces that are irrelevant to the build-evidence purpose.

## 3. Exact non-executable YAML properties

The candidate contains:

```text
ON_WORKFLOW_DISPATCH_ONLY=YES
PUSH_TRIGGER=NO
PULL_REQUEST_TRIGGER=NO
SCHEDULE_TRIGGER=NO
REPOSITORY_DISPATCH_TRIGGER=NO
WORKFLOW_RUN_TRIGGER=NO
RUNNER_LABEL=ubuntu-24.04
TIMEOUT_MINUTES=30
PERMISSIONS_EMPTY_MAP=YES
ACTIONS_CHECKOUT_USED=NO
ANY_GITHUB_ACTION_USED=NO
THIRD_PARTY_ACTION_USED=NO
REUSABLE_WORKFLOW_USED=NO
CACHE_STEP_PRESENT=NO
ARTIFACT_UPLOAD_STEP_PRESENT=NO
PACKAGE_INSTALL_STEP_PRESENT=NO
PAID_OR_LARGER_RUNNER_SELECTED=NO
```

No package-manager installation command is present. Missing required tools must fail the future job closed rather than trigger package installation or a new network dependency.

## 4. Credential boundary

The candidate never references:

```text
github.token
secrets.GITHUB_TOKEN
repository secrets
organization secrets
environment secrets
PATs
SSH keys
cloud credentials
package credentials
model-provider credentials
```

The candidate sets top-level:

```yaml
permissions: {}
```

and its public Git fetch explicitly disables Git credential-helper use for the fetch command:

```text
git -C "$SOURCE_DIR" -c credential.helper= fetch --no-tags --depth=1 origin "$TOOL_COMMIT"
```

This is still only a candidate. It does not erase the canonical distinction that a GitHub-hosted job may have a platform-created job-scoped token even when all available permissions are `none` and the workflow never references it.

```text
PLATFORM_TOKEN_PRESENCE_IF_FUTURE_JOB_RUNS=POSSIBLE_EXPECTED
TOKEN_REFERENCE_BY_CANDIDATE=NO
TOKEN_USE_BY_CANDIDATE=NO
CREDENTIALS_NONE_CLAIM=NO
CREDENTIAL_EXCEPTION_AUTHORIZED_NOW=NO
```

## 5. Source identity fail-closed checks

The future candidate fetch is public and unauthenticated by design. After checkout it requires:

```text
git rev-parse HEAD == c1d0e7a004015f23bc0233470b747b596f29b264
git rev-parse HEAD^{tree} == 2255f4747492109298a5c997f374d49c2af3113d
git status --porcelain == EMPTY
```

Any mismatch fails before configure/build.

No branch or tag is used as the source identity.

## 6. Predeclared build configuration

The exact candidate CMake configuration is:

```text
-G Ninja
-DCMAKE_BUILD_TYPE=Release
-DBUILD_SHARED_LIBS=OFF
-DLLAMA_BUILD_COMMON=ON
-DLLAMA_BUILD_TESTS=OFF
-DLLAMA_BUILD_TOOLS=ON
-DLLAMA_BUILD_EXAMPLES=OFF
-DLLAMA_BUILD_SERVER=OFF
-DLLAMA_BUILD_APP=OFF
-DLLAMA_BUILD_UI=OFF
-DLLAMA_USE_PREBUILT_UI=OFF
-DLLAMA_TOOLS_INSTALL=OFF
-DLLAMA_TESTS_INSTALL=OFF
-DLLAMA_OPENSSL=OFF
-DLLAMA_SUBPROCESS=OFF
-DLLAMA_LLGUIDANCE=OFF
-DGGML_NATIVE=OFF
-DGGML_CCACHE=OFF
-DGGML_OPENMP=OFF
```

The future build command is limited to:

```text
cmake --build "$BUILD_DIR" --target llama-quantize --parallel 2 --verbose
```

This may build target dependencies required by CMake (`llama-quantize-impl`, `llama-common`, `llama`, and required ggml/vendor libraries), but it does not authorize or request unrelated executable targets.

## 7. Evidence emitted if a future run is separately authorized

The candidate predeclares log-only evidence for:

```text
runner OS
runner architecture
GitHub image OS/version when exposed by the runner
kernel identity
/etc/os-release
Git version and executable SHA-256
CMake version and executable SHA-256
Ninja version and executable SHA-256
C compiler version and executable SHA-256
C++ compiler version and executable SHA-256
Python version and executable SHA-256
libc identity
exact source commit
exact source tree
CMakeCache.txt SHA-256
compile_commands.json SHA-256
verbose target build log
llama-quantize output path
llama-quantize SHA-256
llama-quantize exact integer bytes
file-format inspection
linked-library inspection
build-evidence manifest SHA-256
```

The manifest itself is written only to runner temporary storage and printed to the job log. The candidate contains no upload, cache, release, package, or persistence step.

## 8. Predeclared fail-closed conditions

A future promoted run must fail without promotion of evidence if any of the following occurs:

```text
REQUIRED_TOOL_MISSING
SOURCE_FETCH_REQUIRES_CREDENTIAL
SOURCE_COMMIT_MISMATCH
SOURCE_TREE_MISMATCH
SOURCE_WORKTREE_DIRTY
CMAKE_CONFIGURE_FAILURE
UNEXPECTED_EXTERNAL_DEPENDENCY_REQUIRED
TARGET_BUILD_FAILURE
EXPECTED_EXECUTABLE_MISSING
ZERO_SPEND_CONDITION_NOT_ESTABLISHED
RUNNER_CLASS_OR_LABEL_DRIFT
ANY_PROHIBITED_ACTION_REQUIRED
```

A failed future run would create failure evidence only; it would not create `BUILD_PASS=YES`.

## 9. Explicit non-authority state

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=ABSENT
BUILD_ENVIRONMENT_DECISION_B_SELECTED=NO
EXTERNAL_BUILD_ENVIRONMENT_AUTHORITY=NONE
GITHUB_ACTIONS_BUILD_EXECUTION_AUTHORITY=NONE
GITHUB_TOKEN_PRESENCE_EXCEPTION_AUTHORIZED=NO
WORKFLOW_PROMOTION_AUTHORITY=NONE
WORKFLOW_EXECUTION_AUTHORITY=NONE
LIVE_WORKFLOW_CREATED=NO
LIVE_TRIGGER_CREATED=NO
BUILD_PASS=NO
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
DEVICE_QUALIFICATION_AUTHORITY_EXPANSION=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

## 10. Promotion boundary

Even if this candidate is independently reviewed and merged, the following sequence remains mandatory:

```text
NON_EXECUTABLE_CANDIDATE_REVIEWED
-> SEPARATE_EXPLICIT_FOUNDER_BUILD_ENVIRONMENT_DECISION
-> EXACT_AUTHORITY_CAPTURE
-> FRESH_PROMOTION_SUBJECT_CREATED_FROM_CANONICAL_MAIN
-> VERIFY_PROMOTED_YAML_BYTE_IDENTITY_AND_SCOPE
-> FRESH_EXACT_HEAD_REVIEW
-> LIVE_WORKFLOW_PROMOTION_ONLY_IF_AUTHORIZED
-> AT_MOST_ONE_MANUAL_RUN_ONLY_IF_AUTHORIZED
-> CAPTURE_REAL_BUILD_EVIDENCE_OR_FAIL_CLOSED
```

Review/merge of this candidate cannot satisfy any later arrow automatically.

## Exclusions

This candidate and record perform no GitHub Actions run, live workflow creation, source download in a hosted runner, package installation, model/source-weight acquisition, model conversion, model-weight quantization, model loading, inference, benchmark access/execution, device qualification, contamination assessment, selection-suite construction, Private Gold/PHI/gated access, credential or secret access, provider generation, training, procurement, personnel engagement, payment, or spend.

## Exit Evidence

Repository-level closure of this candidate-preparation artifact requires:

```text
CANDIDATE_STORED_OUTSIDE_DOT_GITHUB_WORKFLOWS=YES
CANDIDATE_SHA256_BOUND=YES
EXACT_SOURCE_COMMIT_AND_TREE_CHECKS_PRESENT=YES
NO_PACKAGE_INSTALLATION_PRESENT=YES
NO_GITHUB_ACTION_OR_CHECKOUT_PRESENT=YES
NO_TOKEN_OR_SECRET_REFERENCE_PRESENT=YES
NO_CACHE_OR_ARTIFACT_UPLOAD_PRESENT=YES
BUILD_TARGET_LIMITED_TO_LLAMA_QUANTIZE=YES
LOG_ONLY_EVIDENCE_POLICY_PRESENT=YES
PROMOTION_AUTHORITY_REMAINS_NONE=YES
EXECUTION_AUTHORITY_REMAINS_NONE=YES
BUILD_PASS_REMAINS_NO=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

This is repository preparation only, not operational authorization.