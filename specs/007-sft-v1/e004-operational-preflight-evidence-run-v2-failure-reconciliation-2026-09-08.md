# E004 Operational Preflight Evidence Run V2 Failure Reconciliation — 2026-09-08

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical corrective decision:** `specs/007-sft-v1/e004-operational-preflight-corrective-attempt-founder-decision-2026-09-08.md`
**Canonical V2 implementation merge:** `a1bc59ca4fa7ab9d3e0dc92346093eb444b504b0`
**V2 evidence run:** `34176481565`
**V2 evidence job:** `101906795703`
**V2 evidence head:** `225d0ebe280a4ae2305dcc84dd5795ba90d198d0`
**Artifact class:** append-only observed-evidence reconciliation
**Authority effect:** NONE
**Execution effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Record the exact terminal result of the single authorized V2 operational-preflight evidence attempt without rerunning, retrying, replaying, or reclassifying it.

The V2 allowance is consumed by run attempt 1 regardless of conclusion. This record preserves the failure as observed evidence and creates no new empirical execution authority.

## 2. Exact run identity and one-shot consumption

```text
V2_EVIDENCE_RUN_ID=34176481565
V2_EVIDENCE_JOB_ID=101906795703
V2_EVIDENCE_RUN_NUMBER=3
V2_EVIDENCE_RUN_ATTEMPT=1
V2_EVIDENCE_RUN_HEAD=225d0ebe280a4ae2305dcc84dd5795ba90d198d0
V2_IMPLEMENTATION_CANONICAL_MERGE=a1bc59ca4fa7ab9d3e0dc92346093eb444b504b0
V2_EVIDENCE_RUN_CONCLUSION=failure
V2_AUTHORIZED_RUNS_EXECUTED=1
V2_AUTHORIZED_RUNS_REMAINING=0
V2_RERUN_AUTHORITY=NONE
V2_RETRY_AUTHORITY=NONE
V2_REPLAY_AUTHORITY=NONE
```

The successful marker/authority guard proved that the evidence commit was the one marker-only direct child of the exact canonical V2 implementation merge and that the run was attempt 1.

## 3. Terminal disposition

The run progressed beyond the V1 failure frontier, successfully establishing the one-shot authority guard, public/ungated access boundary, runner/resource observations, and exact llama.cpp runtime reconstruction. It then failed closed during the exact Transformers/Torch dependency-set reconstruction.

```text
OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_FAIL_CLOSED_TRANSFORMERS_DEPENDENCY_SET_DRIFT
CHECKOUT_EXACT_EVIDENCE_HEAD=PASS
ONE_RUN_MARKER_AND_CANONICAL_AUTHORITY_GUARD=PASS
CREDENTIAL_AND_PUBLIC_UNGATED_ACCESS_BOUNDARY=PASS
HOST_RESOURCE_CAPTURE=PASS
LLAMA_RUNTIME_RECONSTRUCTION=PASS
TRANSFORMERS_RUNTIME_RECONSTRUCTION=FAIL
POST_STAGING_DEFAULT_DENY_NETWORK_PROOF=NOT_EXECUTED
RETENTION_CLEANUP_STATE=PASS
SUCCESS_DISPOSITION=skipped
```

No operational-preflight PASS may be inferred from the successful preceding steps.

## 4. Exact dependency-set failure

The V2 workflow froze the previously canonical dependency-set evidence at:

```text
EXPECTED_DEPENDENCY_ARTIFACT_COUNT=27
EXPECTED_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
TRANSFORMERS_VERSION=4.57.6
TRANSFORMERS_COMMIT=753d61104116eefc8ffc977327b441ee0c8d599f
TORCH_RUNTIME_TARGET=2.11.0+cpu
```

The live resolver downloaded 28 wheel artifacts into the bounded wheelhouse. The exact failing gate was:

```bash
test "$(wc -l < "$manifest" | tr -d ' ')" = "$DEPENDENCY_ARTIFACT_COUNT"
```

Observed disposition:

```text
OBSERVED_DEPENDENCY_ARTIFACT_COUNT=28
DEPENDENCY_ARTIFACT_COUNT_GATE=FAIL
ACTUAL_DEPENDENCY_SET_MANIFEST_SHA256=NOT_CAPTURED
TRANSFORMERS_RUNTIME_RECONSTRUCTION=FAILED_BEFORE_VENV_INSTALL
```

The process terminated with exit code 1 at the artifact-count check. Because that check precedes the manifest-digest comparison, virtual-environment creation, offline installation, installed-environment hash verification, Python-runtime hash verification, and offline Transformers/Torch static imports, none of those later checks executed.

The current evidence supports only the statement that the live resolver output drifted from the frozen 27-artifact contract. A specific package-level causal explanation is not established by the captured evidence and must not be treated as proven.

## 5. Provisioning-host boundary observed before failure

The bounded host validation for the dependency download completed successfully before the artifact-count gate:

```text
TRANSFORMERS_PROVISIONING_HOSTS=download.pytorch.org,files.pythonhosted.org,pypi.org
UNEXPECTED_TRANSFORMERS_PROVISIONING_HOSTS=NONE_OBSERVED
```

This does not establish exact dependency identity because the artifact-count gate failed immediately afterward.

## 6. Exact runner and resource observations

The V2 run observed:

```text
PROVIDER=GitHub_Actions
RUNNER_LABEL=ubuntu-24.04
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_OS=Linux
RUNNER_ARCH=X64
IMAGE_OS=ubuntu24
IMAGE_VERSION=20260831.293.1
HOST_OS_RELEASE_SHA256=3f6200a08adc2d23bff81c7ae5087e43ec6e087a82e80ef25cc1819e7af3dbd7
KERNEL_IDENTITY=Linux 6.11.0-1018-azure x86_64 #18~24.04.1-Ubuntu SMP Fri Jun 13 21:37:23 UTC 2025
LIBC_IDENTITY=glibc 2.39
CPU_MODEL_IDENTITY=AMD EPYC 7763 64-Core Processor
LOGICAL_CPU_COUNT=4
TOTAL_MEMORY_BYTES=16795222016
AVAILABLE_MEMORY_BYTES_AT_START=15411064832
ROOT_FILESYSTEM_TOTAL_BYTES=91377852416
ROOT_FILESYSTEM_FREE_BYTES_AT_START=74527748096
RUNNER_TEMP_FILESYSTEM_FREE_BYTES_AT_START=74527748096
EXPECTED_MAX_WALLCLOCK_SECONDS=3600
PAID_OR_LARGER_RUNNER=PROHIBITED
SELF_HOSTED_RUNNER=PROHIBITED
GPU_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

These are observations from this failed V2 run only. They do not by themselves satisfy the complete successor preflight.

## 7. Credential and access boundary evidence

The V2 run successfully observed:

```text
CANDIDATE_BUNDLE_COUNT=4
EXECUTION_SUBJECT_ACCESS_CLASS=PUBLIC_UNGATED_ONLY
CREDENTIALS_REQUIRED_FOR_EXECUTION=NO
PRIVATE_OR_GATED_ASSET_ACCESS=NO
PRIVATE_GOLD_ACCESS=NO
PHI_ACCESS=NO
CREDENTIAL_BOUNDARY_STATE=PASS_NO_CUSTOM_STEP_CREDENTIALS
CHECKOUT_PERSIST_CREDENTIALS=false
WORKFLOW_REPOSITORY_PERMISSION=CONTENTS_READ_ONLY
```

Known GitHub, Hugging Face, AWS, Google, and Azure credential environment variables were explicitly removed before bounded runtime provisioning.

## 8. Exact llama.cpp reconstruction evidence

The V2 run successfully reconstructed the frozen no-model llama.cpp runtime from the bounded GitHub release host family.

```text
LLAMA_PROVISIONING_EFFECTIVE_HOST=release-assets.githubusercontent.com
EXACT_LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
EXACT_LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
EXACT_LLAMA_CPP_TAG=b10621
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LLAMA_CLI_SHA256=f0034d9e6959f6c32b40cbb5326f41ccdbac21b77feb27a6f32c0a7465c9ebf7
LLAMA_RUNTIME_IDENTITY_STATE=PASS_EXACT_CANONICAL_RECONSTRUCTION
LLAMA_MODEL_FILE_ACQUIRED=NO
LLAMA_MODEL_LOAD_PERFORMED=NO
```

`llama-cli --version` completed under the offline network namespace. No model bytes were acquired or loaded.

## 9. Checks not reached after the fail-closed dependency gate

Because the dependency-set count gate failed before environment installation, these downstream validations did not execute:

```text
DEPENDENCY_SET_MANIFEST_SHA256_COMPARISON=NOT_EXECUTED
VIRTUAL_ENVIRONMENT_CREATION=NOT_EXECUTED
OFFLINE_DEPENDENCY_INSTALL=NOT_EXECUTED
INSTALLED_ENVIRONMENT_MANIFEST_SHA256_COMPARISON=NOT_EXECUTED
PYTHON_RUNTIME_SHA256_COMPARISON=NOT_EXECUTED
TRANSFORMERS_TORCH_OFFLINE_STATIC_IMPORT=NOT_EXECUTED
POST_STAGING_DEFAULT_DENY_NETWORK_PROOF=NOT_EXECUTED
RUNNER_TEMP_FILESYSTEM_FREE_BYTES_AFTER_RUNTIME_STAGING=NOT_CAPTURED
```

No value may be inferred for those fields.

## 10. Retention and persistence evidence

The `always()` cleanup step executed after the failure and passed:

```text
RETENTION_CLEANUP_STATE=PASS
RETENTION_SENTINEL_ABSENT_AFTER_CLEANUP=YES
RUNTIME_STAGING_ABSENT_AFTER_CLEANUP=YES
GITHUB_ACTIONS_CACHE_UPLOAD=NO
WORKFLOW_ARTIFACT_UPLOAD=NO
RELEASE_ASSET_UPLOAD=NO
PACKAGE_REGISTRY_UPLOAD=NO
WORKFLOW_ARTIFACT_COUNT=0
```

## 11. Explicit non-actions

```text
MODEL_WEIGHT_ACQUISITION_PERFORMED=NO
MODEL_LOAD_PERFORMED=NO
MODEL_FORWARD_PASS_PERFORMED=NO
MODEL_INFERENCE_PERFORMED=NO
GENERATION_PERFORMED=NO
EVALUATION_PAYLOAD_ACCESS_PERFORMED=NO
EVALUATION_PAYLOAD_EXECUTION_PERFORMED=NO
BENCHMARK_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
A15_ACTIVATION_PERFORMED=NO
TRAINING_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
GATED_ASSET_ACCESSED=NO
PAID_COMPUTE_USED=NO
PROCUREMENT_PERFORMED=NO
PAYMENT_PERFORMED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 12. Authority after terminal V2 failure

The canonical corrective Decision B explicitly made the first V2 run attempt consumptive regardless of PASS, INCOMPLETE, FAIL, infrastructure failure, or guard failure.

Therefore:

```text
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_RERUN_AUTHORITY=NONE
V2_FAILED_JOB_RERUN_AUTHORITY=NONE
V2_SECOND_MARKER_AUTHORITY=NONE
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TOURNAMENT_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PROJECT_FINISHED=NO
```

Any future empirical operational-preflight attempt requires a separate new canonical authority after this failure is reconciled. Generic continuation language or earlier Founder approvals cannot reopen the consumed V2 allowance.