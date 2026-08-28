# E004 GitHub Actions Exact Authority Capture — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `8871aa4b3cda89a2348ace41e166ec878d4633d4`  
**Founder environment decision:** `BUILD_ENVIRONMENT_DECISION_B` / PR #92  
**Authority class:** exact-subject binding under already-selected Decision B  
**Authority effect:** NO NEW ENVIRONMENT OR MODEL AUTHORITY; BIND EXISTING BOUNDED AUTHORITY TO ONE REVIEWABLE SUBJECT  
**Live workflow promotion authority:** CONDITIONAL_NOT_YET_EXERCISABLE  
**Workflow execution authority:** CONDITIONAL_NOT_YET_EXERCISABLE  
**Model conversion authority:** NONE  
**Model execution authority:** NONE  
**Benchmark/device authority expansion:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

PR #92 canonically selected the GitHub Actions environment class but deliberately left workflow promotion and execution separately gated. This record performs the next mandated `EXACT_AUTHORITY_CAPTURE` step by composing already-canonical authorities without widening them:

```text
E004_CONVERSION_TOOLCHAIN_BUILD_AUTHORITY=AUTHORIZED_BOUNDED
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
EXTERNAL_BUILD_ENVIRONMENT_AUTHORITY=AUTHORIZED_GITHUB_ACTIONS_CLASS_ONLY
EXACT_AUTHORITY_CAPTURE=THIS_RECORD_PENDING_REVIEW
```

It binds one exact future workflow subject and the conditions under which its promotion and at most one manual run may become exercisable. No live workflow is created by this record.

## 2. Exact subject identity

The review subject remains outside `.github/workflows`:

```text
CANDIDATE_PATH=specs/007-sft-v1/candidates/e004-github-actions-build-evidence.workflow.yml.example
CANDIDATE_GIT_BLOB_SHA1=abe6b51fc575c5e446ad73e1ad1c2a65f8380e8b
CANDIDATE_SHA256=NEEDS_EVIDENCE_EXACT_HEAD_RECOMPUTE
CANDIDATE_DIGEST_EVIDENCE_SOURCE=PENDING_FRESH_EXACT_HEAD_REVIEW
INTENDED_LIVE_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
LIVE_WORKFLOW_CREATED=NO
LIVE_TRIGGER_CREATED=NO
```

The candidate was hardened before authority capture to make both network and privilege boundaries operationally fail-closed. It permits network only during exact public source materialization. For configure/build, bounded root privilege creates a separate Linux network namespace; `setpriv` then drops to the original runner UID/GID, clears supplementary groups, removes inheritable/ambient/bounding capabilities, enables `no_new_privs`, and resets inherited environment before any CMake or compiler process starts.

The prior candidate digest was invalidated by this final hardening commit and is not inherited. The SHA-256 above must be independently recomputed from exact candidate bytes on the current reviewed head and bound before qualification. Any later candidate-byte change invalidates this capture and requires a new exact authority capture.

## 3. Exact environment and run envelope

```text
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
PURPOSE=E004_LLAMA_QUANTIZE_BUILD_EVIDENCE_ONLY
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TRIGGER=workflow_dispatch_only
TIMEOUT_MINUTES=30
WORKFLOW_PERMISSIONS={}
PAID_OR_LARGER_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

No mutable runner label, automatic trigger, matrix expansion, retry loop, scheduled run, or second manual run is within this authority capture.

## 4. Exact source and build boundary

```text
TOOL_REPOSITORY_URL=https://github.com/ggml-org/llama.cpp.git
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
BUILD_TARGET=llama-quantize
OUTPUT_AUTHORITY=BUILD_EVIDENCE_ONLY
```

The future job must fail before configure/build unless both exact Git identities match. Branches, tags, forks, binary releases, package-manager substitutes, and alternate revisions are prohibited.

## 5. Credential boundary

```text
PLATFORM_MAY_CREATE_JOB_SCOPED_GITHUB_TOKEN=YES
WORKFLOW_PERMISSIONS={}
GITHUB_TOKEN_REFERENCE_BY_STEPS=PROHIBITED
GITHUB_TOKEN_ACCESS_BY_STEPS=PROHIBITED
GITHUB_TOKEN_USE_BY_STEPS=PROHIBITED
OTHER_SECRET_OR_CREDENTIAL_REFERENCE=PROHIBITED
TOKEN_USE_AUTHORITY_CREATED=NO
```

The public source-fetch path additionally sets:

```text
GIT_TERMINAL_PROMPT=0
GIT_CONFIG_NOSYSTEM=1
GIT_ASKPASS=/bin/false
SSH_ASKPASS=/bin/false
credential.helper=EMPTY
http.extraHeader=EMPTY
```

This does not claim that the platform token is absent. It requires that the workflow never reference or use it.

## 6. Network and privilege boundary

The future job has two distinct phases.

### 6.1 Exact public source materialization

Network access by workflow commands is permitted only for unauthenticated public Git transport to:

```text
https://github.com/ggml-org/llama.cpp.git
```

Purpose is limited to fetching exact commit `c1d0e7a004015f23bc0233470b747b596f29b264`.

No model repository, model-provider endpoint, package registry, benchmark source, cloud service, credential endpoint, or unrelated dependency endpoint is authorized.

### 6.2 Configure/build

Root privilege is permitted only to create the Linux network namespace. Before any CMake or compiler process starts, the workflow must execute the equivalent of:

```text
sudo -n unshare --net -- \
  setpriv \
    --reuid <RUNNER_UID> \
    --regid <RUNNER_GID> \
    --clear-groups \
    --inh-caps=-all \
    --ambient-caps=-all \
    --bounding-set=-all \
    --no-new-privs \
    --reset-env \
    -- \
  env HOME=<E004_HOME> TMPDIR=<RUNNER_TEMP> LC_ALL=C LANG=C \
  bash ...
```

The inner script must assert that its effective UID is nonzero before configure/build. The runner/log process remains outside that namespace. The CMake/compiler process tree is unprivileged, has cleared supplementary groups and Linux capability sets, cannot gain new privileges through exec, receives a reset/minimized environment, and has no normal host network interface.

If passwordless `sudo`, `unshare`, `setpriv`, namespace creation, identity drop, capability drop, `no_new_privs`, environment reset, or the nonroot assertion is unavailable, the job fails closed before configure/build.

```text
ROOT_PRIVILEGE_PURPOSE=NETWORK_NAMESPACE_CREATION_ONLY
CONFIGURE_BUILD_PRIVILEGE=UNPRIVILEGED
SUPPLEMENTARY_GROUPS=CLEARED_BEFORE_BUILD
INHERITABLE_CAPABILITIES=NONE
AMBIENT_CAPABILITIES=NONE
BOUNDING_CAPABILITIES=NONE
NO_NEW_PRIVS=REQUIRED
INHERITED_ENVIRONMENT=RESET_BEFORE_BUILD
CONFIGURE_BUILD_NETWORK_EGRESS=TECHNICALLY_ISOLATED_BY_NETWORK_NAMESPACE
UNEXPECTED_CONFIGURE_BUILD_NETWORK_DEPENDENCY=FAIL_CLOSED
PACKAGE_INSTALLATION=PROHIBITED
```

## 7. Tool/runtime preflight

The exact subject requires preinstalled:

```text
bash
env
id
git
cmake
ninja
cc
c++
python3
sha256sum
readlink
ldd
file
stat
sudo
unshare
setpriv
```

Missing tools fail closed. The workflow must not install or download replacements.

Before build, it captures versions/paths and SHA-256 where applicable for shell/core execution tools, Git, CMake, Ninja, C/C++ compilers, Python, sudo, unshare, and setpriv, plus runner/image/kernel/libc identity.

## 8. Bounded build configuration

The exact configuration remains:

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

The only requested executable target is:

```text
cmake --build "$build_dir" --target llama-quantize --parallel 2 --verbose
```

CMake-required libraries/dependencies of that target may build. No unrelated executable target is authorized.

## 9. Storage, persistence, and retention

```text
RUNNER_WORKING_STORAGE=EPHEMERAL_GITHUB_HOSTED_RUNNER_ONLY
EVIDENCE_PERSISTENCE=JOB_LOG_ONLY
ACTIONS_ARTIFACT_UPLOAD=PROHIBITED
CACHE=PROHIBITED
RELEASE_ASSET=PROHIBITED
PACKAGE_PUBLISH=PROHIBITED
MODEL_ARTIFACT_PERSISTENCE=PROHIBITED
```

GitHub provider-managed job-log retention applies. The exact repository-configured retention-day value is not currently observable through the connected GitHub action surface and is therefore not fabricated here.

```text
JOB_LOG_RETENTION_PROVIDER_POLICY=REPOSITORY_CONFIGURED_GITHUB_ACTIONS_LOG_RETENTION
JOB_LOG_RETENTION_EXACT_DAYS=NEEDS_EVIDENCE_CONNECTOR_NOT_EXPOSED
RETENTION_VALUE_INFERENCE=PROHIBITED
```

This unresolved numeric provider setting does not authorize changing repository retention. If exact numeric retention is later determined to be a hard pre-run requirement by review/governance, execution remains blocked until real evidence is supplied.

## 10. Required evidence from the one future run

A successful run must emit or make retrievable evidence sufficient to bind:

```text
workflow_path
workflow_canonical_blob_identity
workflow_sha256
run_id
job_id
run_attempt
trigger_identity
runner_label
runner_os
runner_architecture
runner_image_os
runner_image_version
kernel_identity
libc_identity
bash_path_sha256
env_path_sha256
id_path_sha256
git_path_version_sha256
cmake_path_version_sha256
ninja_path_version_sha256
c_compiler_path_version_sha256
cxx_compiler_path_version_sha256
python_path_version_sha256
sudo_path_version_sha256
unshare_path_version_sha256
setpriv_path_version_sha256
source_repository
source_commit
source_tree
cmake_configuration_argv
build_argv
cmake_cache_sha256
compile_commands_sha256
network_namespace_assertion
configure_build_effective_uid_assertion
privilege_drop_assertion
capability_drop_assertion
no_new_privs_assertion
environment_reset_assertion
llama_quantize_output_path
llama_quantize_executable_sha256
llama_quantize_exact_integer_bytes
file_format_inspection
linked_library_inspection
build_evidence_manifest_sha256
credential_use_assertion
artifact_cache_upload_assertion
spend_usd
```

No missing field may be invented from source metadata.

## 11. Fail-closed conditions

Any of the following means the run does not create `BUILD_PASS=YES`:

```text
RUNNER_LABEL_MISMATCH
RUN_COUNT_EXCEEDED
AUTOMATIC_OR_UNEXPECTED_TRIGGER
NONEMPTY_WORKFLOW_PERMISSION_REQUIRED
TOKEN_OR_SECRET_REFERENCE_REQUIRED
REQUIRED_TOOL_MISSING
PASSWORDLESS_SUDO_UNAVAILABLE
NETWORK_NAMESPACE_UNAVAILABLE
PRIVILEGE_DROP_UNAVAILABLE
CAPABILITY_DROP_UNAVAILABLE
NO_NEW_PRIVS_UNAVAILABLE
ENVIRONMENT_RESET_UNAVAILABLE
CONFIGURE_BUILD_EFFECTIVE_UID_IS_ROOT
SOURCE_FETCH_REQUIRES_CREDENTIAL
SOURCE_COMMIT_MISMATCH
SOURCE_TREE_MISMATCH
SOURCE_WORKTREE_DIRTY
UNEXPECTED_NETWORK_DEPENDENCY_REQUIRED
PACKAGE_INSTALLATION_REQUIRED
CMAKE_CONFIGURE_FAILURE
TARGET_BUILD_FAILURE
EXPECTED_EXECUTABLE_MISSING
PAID_OR_LARGER_RUNNER_REQUIRED
NONZERO_SPEND_REQUIRED
UNAUTHORIZED_PERSISTENCE_REQUIRED
ANY_MODEL_OR_BENCHMARK_OPERATION_REQUIRED
```

A failed run may produce failure evidence only.

## 12. Promotion and execution conditions

This capture does not make promotion or execution immediately exercisable on the branch that contains it.

After this record becomes canonical and only if its exact-head review finds no material authority defect, a fresh promotion branch must be created from then-current canonical `main`.

The intended live workflow may be promoted only when all of the following are true:

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION_B=CANONICAL
EXACT_AUTHORITY_CAPTURE=CANONICAL
QUALIFIED_CANDIDATE_GIT_BLOB_SHA1=NEEDS_EVIDENCE_CURRENT_HEAD
QUALIFIED_CANDIDATE_SHA256=NEEDS_EVIDENCE_CURRENT_HEAD
PROMOTED_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
PROMOTED_WORKFLOW_BYTES_EQUAL_QUALIFIED_CANDIDATE_BYTES=YES
PROMOTED_WORKFLOW_GIT_BLOB_EQUALS_QUALIFIED_CANDIDATE_GIT_BLOB=YES
PROMOTED_WORKFLOW_SHA256_EQUALS_QUALIFIED_CANDIDATE_SHA256=YES
PROMOTION_PR_CHANGED_WORKFLOW_SCOPE_IS_EXACT=YES
FRESH_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
```

Canonical merge of that exact promotion PR is the promotion event. No other workflow path is authorized. Any candidate-byte change requires a new exact authority capture rather than an amendment-by-inference.

The at-most-one manual build-evidence run becomes exercisable only after post-merge verification proves the live workflow on canonical `main` is byte-identical to the qualified subject and all pre-run conditions in this record remain satisfied.

```text
WORKFLOW_PROMOTION_AUTHORITY=CONDITIONAL_ON_EXACT_PROMOTION_REVIEW_AND_BYTE_IDENTITY
WORKFLOW_EXECUTION_AUTHORITY=CONDITIONAL_ON_CANONICAL_PROMOTION_AND_PRE_RUN_VERIFICATION
MAX_AUTHORIZED_WORKFLOW_RUNS=1
```

These conditions operationalize the exact already-selected Decision B subject; they do not authorize a different workflow or a second run.

## 13. Tooling capability boundary

The currently connected GitHub action surface can create/review/merge repository files and inspect workflow runs/jobs/logs, but it does not expose an action to initiate a new `workflow_dispatch` run.

```text
CONNECTED_DISPATCH_ACTION_AVAILABLE=NO
EXECUTION_OCCURRED=NO
TOOLING_LIMITATION_EQUALS_AUTHORITY_REVOCATION=NO
TOOLING_LIMITATION_EQUALS_EXECUTION_EVIDENCE=NO
```

If this limitation still exists after canonical workflow promotion, the executor must record an execution-tooling blocker rather than claim that the authorized run occurred.

## 14. Explicit downstream prohibitions

```text
MODEL_SOURCE_WEIGHT_ACQUISITION_EXPANSION=NONE
MODEL_WEIGHT_LOADING=NONE
MODEL_CONVERSION=NONE
MODEL_WEIGHT_QUANTIZATION=NONE
MODEL_INFERENCE=NONE
BENCHMARK_PAYLOAD_ACCESS_EXPANSION=NONE
BENCHMARK_EXECUTION_EXPANSION=NONE
DEVICE_QUALIFICATION_EXPANSION=NONE
CONTAMINATION_ASSESSMENT=NONE
SELECTION_SUITE_CONSTRUCTION=NONE
PRIVATE_GOLD=NONE
PHI=NONE
GATED_ASSETS=NONE
PROVIDER_GENERATION=NONE
TRAINING=NONE
PROCUREMENT=NONE
BACKBONE_WINNER_SELECTION=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 15. Current state on this branch

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
EXACT_AUTHORITY_CAPTURE=PENDING_FRESH_EXACT_HEAD_REVIEW_AFTER_FINAL_HARDENING
CANDIDATE_GIT_BLOB_SHA1=abe6b51fc575c5e446ad73e1ad1c2a65f8380e8b
CANDIDATE_SHA256=NEEDS_EVIDENCE_EXACT_HEAD_RECOMPUTE
LIVE_WORKFLOW_CREATED=NO
LIVE_TRIGGER_CREATED=NO
WORKFLOW_RUN_EXECUTED=NO
BUILD_PASS=NO
CONVERSION_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Exit Evidence

This authority capture is not qualified until fresh exact-head review independently confirms at minimum:

```text
FOUNDER_DECISION_B_AND_BUILD_AUTHORITY_COMPOSITION_IS_NON_EXPANSIVE=YES
REVISED_CANDIDATE_SHA256_RECOMPUTED_AND_BOUND=YES
REVISED_CANDIDATE_GIT_BLOB_MATCHES=YES
NETWORK_BOUNDARY_IS_FAIL_CLOSED=YES
PRIVILEGE_BOUNDARY_IS_LEAST_PRIVILEGE_FAIL_CLOSED=YES
CAPABILITY_BOUNDARY_IS_FAIL_CLOSED=YES
NO_NEW_PRIVS_BOUNDARY_IS_FAIL_CLOSED=YES
ENVIRONMENT_RESET_BOUNDARY_IS_FAIL_CLOSED=YES
CREDENTIAL_BOUNDARY_IS_FAIL_CLOSED=YES
ONLY_ONE_RUN_CLASS_IS_BOUND=YES
ONLY_ONE_LIVE_WORKFLOW_PATH_IS_BOUND=YES
STORAGE_AND_RETENTION_UNCERTAINTY_IS_NOT_FABRICATED=YES
PROMOTION_AND_EXECUTION_CONDITIONS_DO_NOT_BYPASS_REVIEW=YES
NO_MODEL_OR_DOWNSTREAM_AUTHORITY_EXPANSION=YES
BUILD_PASS_REMAINS_NO=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Any material finding must be repaired before canonical merge.