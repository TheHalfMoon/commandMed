# E004 Repaired-Target Runtime-Evidence Result Reconciliation — 2026-09-01

**Spec:** 007 SFT V1  
**Artifact class:** append-only repaired-target runtime-evidence result reconciliation  
**Canonical base:** `3b216174af530d78f71f0d54a9f468cbdd7d8d8c`  
**Repaired target canonical merge:** `becf6282a4bd0fa99408c49ddcc65cd8ac6540b9`  
**Controlling bounded authority:** `specs/007-sft-v1/e004-target-route-repair-runtime-attempt-authority-2026-08-31.md`  
**Authority effect:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation:** ABSENT_NOT_AUTHORIZED  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose and claim boundary

Reconcile the terminal evidence from the exactly one newly authorized repaired-target E004 conversion-runtime evidence attempt after the bounded Phase A CONNECT allowlist repair was independently qualified, merged canonically, identity-bound, and dispatched through the one-shot transport bootstrap.

This record may state only what the repaired run, job metadata, retained job logs, workflow bytes, and artifact listing directly prove. It does not reinterpret the earlier failed historical target run, does not infer the exact historical failure mechanism, and creates no new model, conversion, benchmark, contamination, A15, training, credential, provider, paid-runner, procurement, payment, or spend authority.

```text
REPAIRED_TARGET_RUNTIME_EVIDENCE_RESULT=PASS
REPAIRED_TARGET_RUNTIME_EVIDENCE_ATTEMPT_ALLOWANCE_REMAINING=0
AUTOMATIC_TARGET_RETRY_AUTHORITY=NONE
FAILED_TARGET_JOB_RERUN_AUTHORITY=NONE
SECOND_NEW_TARGET_ATTEMPT_AUTHORITY=NONE
COMPONENT_E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
```

## 2. Historical observation remains immutable and separate

The prior historical target observation remains:

```text
HISTORICAL_TARGET_RUN_ID=33366859146
HISTORICAL_TARGET_JOB_ID=99409197359
HISTORICAL_TARGET_EVENT=workflow_dispatch
HISTORICAL_TARGET_HEAD_SHA=ef1be50f4a076d9f03abfffee342d2c244b0d199
HISTORICAL_TARGET_RUN_ATTEMPT=1
HISTORICAL_TARGET_CONCLUSION=failure
HISTORICAL_RUNNER_PREFLIGHT=PASS
HISTORICAL_PHASE_A_ALLOWLISTED_PUBLIC_SOURCE_AND_DEPENDENCY_STAGING=FAIL
HISTORICAL_PHASE_B_OFFLINE_ENVIRONMENT_LOCAL_GGUF_ATTESTATION_AND_REBUILD=SKIPPED
HISTORICAL_FINAL_RUNTIME_EVIDENCE_MANIFEST=SKIPPED
HISTORICAL_STDERR_RECOVERED=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
HISTORICAL_PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
```

The new repaired run is a later successful observation under repaired target bytes. It does not prove that the historical failure was caused by the exact route now admitted.

```text
HISTORICAL_RUN=FAILED_HISTORICAL_OBSERVATION_WITH_CAUSE_NEEDS_EVIDENCE
REPAIRED_RUN=NEW_SUCCESSFUL_OBSERVATION_AFTER_SEPARATELY_PROVEN_STATIC_ROUTE_REPAIR
HISTORICAL_CAUSAL_REINTERPRETATION=PROHIBITED
```

## 3. Exact repaired run and job identity

GitHub Actions records the repaired target execution as:

```text
RUN_ID=33434874024
RUN_ATTEMPT=1
RUN_EVENT=workflow_dispatch
RUN_HEAD_BRANCH=e004-runtime-evidence-route-repair-bind-becf6282a4bd0fa99408c49ddcc65cd8ac6540b9
RUN_HEAD_SHA=becf6282a4bd0fa99408c49ddcc65cd8ac6540b9
RUN_WORKFLOW_PATH=.github/workflows/e004-conversion-runtime-evidence.yml
RUN_STATUS=completed
RUN_CONCLUSION=success
JOB_ID=99628745384
JOB_NAME=runtime-evidence
JOB_CONCLUSION=success
RUN_ARTIFACT_COUNT=0
```

The job started at `2026-08-31T20:13:46Z` and completed at `2026-08-31T20:17:47Z`. Every substantive workflow step completed successfully:

```text
FAIL_CLOSED_RUNNER_PREFLIGHT=success
PHASE_A_ALLOWLISTED_PUBLIC_SOURCE_AND_DEPENDENCY_STAGING=success
PHASE_B_OFFLINE_ENVIRONMENT_LOCAL_GGUF_ATTESTATION_AND_REBUILD=success
EMIT_RUNTIME_EVIDENCE_MANIFEST_TO_LOGS_ONLY=success
```

The one authorized repaired-target attempt was consumed when run `33434874024` was created. Its success does not reopen that allowance.

## 4. Runner and resolver evidence emitted by the job

The retained logs emitted:

```text
RUN_ID=33434874024
RUN_ATTEMPT=1
RUN_HEAD_SHA=becf6282a4bd0fa99408c49ddcc65cd8ac6540b9
RUNNER_OS=Linux
RUNNER_ARCH=X64
ImageOS=ubuntu24
ImageVersion=20260823.283.1
AVAILABLE_KB=89704008
RESOLVER_NAME=pip
RESOLVER_VERSION=24.0
RESOLVER_MODULE_PATH=/usr/lib/python3/dist-packages/pip/__init__.py
RESOLVER_MODULE_SHA256=a009359c5a4b994552e4b9fb371bcda06527e55927e851908cf68d0dff10f299
```

The runner metadata also reported runner agent version `2.337.0` and Hosted Compute Agent version `20260819.586`.

## 5. Phase A exact source and dependency evidence

Phase A completed successfully and emitted:

```text
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
TORCH_RUNTIME_TARGET=2.11.0+cpu
CONVERTER_ENTRYPOINT_SHA256=e38975e1c68d98ac1664dfd530616eb35c72294382a4dd873d4746b23f27779f
CANONICAL_DEPENDENCY_REQUIREMENT_SURFACE_SHA256=4e973aa513a628244ad686230a779896502d184d28bd4ce2769b70bcf502bd6d
SOURCE_MANIFEST_SHA256=015862c648877b86a9b2b7a420eefeb49e352267a03ccb3e22edcce51c413aad
DEPENDENCY_ARTIFACT_COUNT=27
DEPENDENCY_SET_MANIFEST_SHA256=ebfd3c49dc83c35b3ad00e0d4d8b903502a8951fd65da80186b6677007bbfd3f
PIP_DOWNLOAD_LOG_SHA256=7c7926fb5b2c81ffe2ebde0050bb0fcdcb20c9f25e506128996cf888ecc2e364
PHASE_A_ALLOWLIST_PROXY_LOG_SHA256=bea5172290d023aabccde7898ee444e47fcca70bdcf45e911c4b6e1beec395a2
PHASE_A_CREDENTIAL_USE=NO
```

The complete dependency artifact set is identity-bound by the exact count and manifest SHA-256 above. The resolver reported successful download of the exact requested dependency closure before Phase A completed.

### Phase A CONNECT proxy behavior

The emitted proxy log contained these exact successful CONNECT observations:

```text
ALLOW host=github.com port=443
ALLOW host=pypi.org port=443
ALLOW host=download.pytorch.org port=443
ALLOW host=download-r2.pytorch.org port=443
ALLOW host=files.pythonhosted.org port=443
```

The workflow fails immediately if the proxy log contains any line beginning with `DENY `. That fail-closed check passed, Phase A completed successfully, and the emitted proxy log contained only the five `ALLOW` observations above.

```text
PHASE_A_PROXY_UNEXPECTED_DENY_OBSERVED=NO
PHASE_A_REPAIRED_ROUTE_OBSERVED_ALLOW=YES
PHASE_A_REPAIRED_ROUTE=download-r2.pytorch.org:443
```

This is evidence about the repaired run only. It is not an invented historical deny line and does not change `HISTORICAL_PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE`.

## 6. Phase B offline isolation and rebinding evidence

Phase B completed inside the workflow's default-deny network namespace and emitted:

```text
PHASE_B_NETWORK_POLICY=DEFAULT_DENY_NETWORK_NAMESPACE
PHASE_B_UID=1001
CapInh=0000000000000000
CapPrm=0000000000000000
CapEff=0000000000000000
CapBnd=0000000000000000
CapAmb=0000000000000000
NoNewPrivs=1
SENSITIVE_PLATFORM_ENV_PRESENT=NO
NO_LOCAL_GGUF_STATE=UNSET
```

The exact source and dependency manifests were recomputed inside the isolated Phase B boundary and matched the immutable Phase A manifests.

```text
SOURCE_RECOMPUTED_MANIFEST_SHA256=015862c648877b86a9b2b7a420eefeb49e352267a03ccb3e22edcce51c413aad
DEPENDENCY_RECOMPUTED_MANIFEST_SHA256=ebfd3c49dc83c35b3ad00e0d4d8b903502a8951fd65da80186b6677007bbfd3f
OFFLINE_INSTALL_LOG_SHA256=0309d76d7c40708831004c91b41e8d1fc4bf6cc17dd95c3d82a5cfcacfdca9ac
INSTALLED_ENVIRONMENT_MANIFEST_SHA256=694ff5fcf55413072218982371c350c1e37a21d034b498acc83a501a3d908a85
```

### Local GGUF attestation

The isolated environment imported `gguf` only from the exact local `llama.cpp/gguf-py` source tree and emitted:

```text
GGUF_IMPORTED_FILE_PATH=/home/runner/work/_temp/e004-runtime-evidence/llama.cpp/gguf-py/gguf/__init__.py
GGUF_IMPORTED_SOURCE_IDENTITY=/home/runner/work/_temp/e004-runtime-evidence/llama.cpp/gguf-py
GGUF_IMPORTED_FILE_SHA256=3ccfc0104cd7ea88c6028743b7bf3f2c89b5f474425de03a217a6072320d7c2f
NO_LOCAL_GGUF_UNSET_ATTESTATION=PASS
GGUF_ATTESTATION_SHA256=250e591881b14560bb5de592ef77e649542ab4c6c70fc1c4de0ff541645168cf
```

### Rebuild and toolchain identity

The build manifest emitted:

```text
PYTHON_RUNTIME_PATH=/usr/bin/python3.12
PYTHON_RUNTIME_VERSION=Python 3.12.3
VENV_PIP_VERSION=pip 24.0 from /home/runner/work/_temp/e004-runtime-evidence/venv/lib/python3.12/site-packages/pip (python 3.12)
TORCH_RUNTIME_TARGET=2.11.0+cpu
SOURCE_REBIND_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
SOURCE_REBIND_TREE=2255f4747492109298a5c997f374d49c2af3113d
CMAKE_CONFIG=Release_Ninja_static_llama_quantize_only
BUILD_ARGV=cmake --build <build_dir> --target llama-quantize --parallel 2 --verbose
LLAMA_QUANTIZE_PATH=/home/runner/work/_temp/e004-runtime-evidence/llama.cpp-build/bin/llama-quantize
PYTHON_RUNTIME_SHA256=1643dacd9feaedc58f3cc581e4d22577dfe25c09b10282936186ccf0f2e61118
LLAMA_QUANTIZE_SHA256=18ff27aab20ab7b4e239ac847be7636fb8e182ac9d1474efa7c4cfc915bbb4fc
CMAKE_CACHE_SHA256=5a2f8b139183dfba6d422db476cd8ad1b69388749199d909055744c082532bc3
BUILD_MANIFEST_SHA256=dd7a23f7ccc4aa03365caa1bfafe0713cd1f37c9da50e45a30ed2ae6a60a8122
LLAMA_QUANTIZE_INTEGER_BYTES=6513680
```

The rebuilt `llama-quantize` executable was evidence output only. No model weights were acquired, loaded, converted, quantized, or inferred by this workflow.

## 7. Final runtime-evidence manifest

The job emitted the final manifest with:

```text
RUNTIME_EVIDENCE_MANIFEST_SHA256=6f3e91fd162db6fd764a5915d34b50254cc91a07906eb602f833b02ff6dfb25d
AUTHORITY=E004_CONVERSION_RUNTIME_EVIDENCE_AUTHORITY_AUTHORIZED_BOUNDED
TOOL_REPOSITORY=ggml-org/llama.cpp
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
TORCH_RUNTIME_TARGET=2.11.0+cpu
CONVERTER_ENTRYPOINT_SHA256=e38975e1c68d98ac1664dfd530616eb35c72294382a4dd873d4746b23f27779f
CANONICAL_DEPENDENCY_REQUIREMENT_SURFACE_SHA256=4e973aa513a628244ad686230a779896502d184d28bd4ce2769b70bcf502bd6d
LOCAL_GGUF_SOURCE_MODE=REQUIRED
NO_LOCAL_GGUF_MUST_BE_UNSET=YES
REMOTE_HF_CONVERSION_MODE=PROHIBITED
SOURCE_MANIFEST_SHA256=015862c648877b86a9b2b7a420eefeb49e352267a03ccb3e22edcce51c413aad
SOURCE_RECOMPUTED_MANIFEST_SHA256=015862c648877b86a9b2b7a420eefeb49e352267a03ccb3e22edcce51c413aad
DEPENDENCY_SET_MANIFEST_SHA256=ebfd3c49dc83c35b3ad00e0d4d8b903502a8951fd65da80186b6677007bbfd3f
PHASE_A_ALLOWLIST_PROXY_LOG_SHA256=bea5172290d023aabccde7898ee444e47fcca70bdcf45e911c4b6e1beec395a2
SECURITY_EVIDENCE_SHA256=e957873641db7e2bd2b9a140daee530d8fa7fcdd52293b228427bf1f48391dfe
INSTALLED_ENVIRONMENT_MANIFEST_SHA256=694ff5fcf55413072218982371c350c1e37a21d034b498acc83a501a3d908a85
GGUF_ATTESTATION_SHA256=250e591881b14560bb5de592ef77e649542ab4c6c70fc1c4de0ff541645168cf
BUILD_MANIFEST_SHA256=dd7a23f7ccc4aa03365caa1bfafe0713cd1f37c9da50e45a30ed2ae6a60a8122
LLAMA_QUANTIZE_SHA256=18ff27aab20ab7b4e239ac847be7636fb8e182ac9d1474efa7c4cfc915bbb4fc
LLAMA_QUANTIZE_INTEGER_BYTES=6513680
```

## 8. Explicit negative-operation and authority evidence

The final manifest directly emitted:

```text
MODEL_SOURCE_WEIGHT_ACQUISITION_OCCURRED=NO
MODEL_LOADING_OCCURRED=NO
MODEL_CONVERSION_OCCURRED=NO
MODEL_INFERENCE_OCCURRED=NO
BENCHMARK_EXECUTION_OCCURRED=NO
DEVICE_QUALIFICATION_OCCURRED=NO
CONTAMINATION_ASSESSMENT_OCCURRED=NO
TRAINING_OCCURRED=NO
CREDENTIAL_USE_OCCURRED=NO
ARTIFACT_UPLOAD_OCCURRED=NO
CACHE_UPLOAD_OCCURRED=NO
PAID_OR_LARGER_RUNNER_USED=NO
AUTHORIZED_SPEND_USD=0
PROVIDER_BILLING_LEDGER_ROW_EXPOSED_TO_WORKFLOW=NO
INFERRED_HIDDEN_BILLING_VALUE=PROHIBITED
```

The preflight also emitted the controlling prohibitions:

```text
MODEL_SOURCE_WEIGHT_ACQUISITION=PROHIBITED
MODEL_CONVERSION=PROHIBITED
MODEL_INFERENCE=PROHIBITED
BENCHMARK_ACCESS=PROHIBITED
CONTAMINATION_ASSESSMENT=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING=PROHIBITED
EXTERNAL_REVIEWER_OUTREACH=PROHIBITED
CREDENTIAL_USE=PROHIBITED
ARTIFACT_UPLOAD=PROHIBITED
CACHE_UPLOAD=PROHIBITED
PAID_OR_LARGER_RUNNER=PROHIBITED
SPEND_USD=0
```

The terminal job output further emitted:

```text
RUNTIME_EVIDENCE_PASS_EQUALS_MODEL_CONVERSION_AUTHORITY=NO
RUNTIME_EVIDENCE_PASS_EQUALS_E004_TOURNAMENT_START=NO
RUNTIME_EVIDENCE_PASS_EQUALS_A15_ACTIVATION=NO
RUNTIME_EVIDENCE_PASS_EQUALS_TRAINING_AUTHORITY=NO
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

These emitted boundaries are controlling for interpretation of this successful evidence run.

## 9. Artifact and persistence observation

The live GitHub Actions artifact listing for run `33434874024` is empty.

```text
RUN_ARTIFACT_COUNT=0
ARTIFACT_UPLOAD_OCCURRED=NO
CACHE_UPLOAD_OCCURRED=NO
EVIDENCE_PERSISTENCE_SURFACE=RETAINED_JOB_LOGS_ONLY
```

No artifact or cache persistence is inferred beyond the retained GitHub job logs.

## 10. E004 consequence

This repaired run resolves only the bounded conversion-runtime evidence prerequisite represented by the repaired workflow. It does not complete the E004 tournament evidence pack.

At this reconciliation base, the independently unresolved E004 categories remain fail-closed unless later canonical evidence proves otherwise, including:

- persistent conversion subject/workspace completion and separate model-conversion authority;
- contamination-assessment payload-access/execution authority and retained contamination evidence;
- T1/A2 numeric policy plus qualified clinical/statistical review;
- G1-G4 real governance evidence;
- runtime/device/personnel/access resource bindings and finance/resource evidence outside the exact bounded public standard-runner lane;
- a real A1-A14 PASS snapshot;
- separate A15 activation;
- any other blocker still present in the then-current canonical Spec 007 task/current-state chain.

Therefore:

```text
COMPONENT_RUNTIME_EVIDENCE=PASS_REPAIRED_TARGET_RUN_33434874024
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

## 11. Required review gate

Before this reconciliation becomes canonical, a fresh independent exact-head reviewer must verify at least:

- run `33434874024`, job `99628745384`, repaired head `becf6282a4bd0fa99408c49ddcc65cd8ac6540b9`, event, branch, attempt, and successful terminal state are recorded exactly;
- all four substantive job steps are successful and no run artifact exists;
- runner/resolver/source/dependency identities match the retained logs;
- Phase A proxy observations contain the five exact `ALLOW` hosts and no unexpected `DENY` survived the fail-closed guard;
- Phase B network/capability/environment isolation evidence is recorded exactly;
- local GGUF attestation and rebuild identities match the retained logs;
- final runtime manifest hashes and negative-operation fields are recorded exactly;
- the repaired-run result is not used to rewrite historical run `33366859146` or invent an exact historical deny line;
- the repaired-target attempt allowance is consumed and no retry/rerun/second attempt is authorized;
- no model conversion, contamination assessment, A15, training, E005, credential, paid-runner, or spend authority is created;
- E004 remains incomplete and E005 remains `NOT_REACHED`.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```

Only guarded canonical merge of the exact independently reviewed reconciliation head may make this result reconciliation canonical.