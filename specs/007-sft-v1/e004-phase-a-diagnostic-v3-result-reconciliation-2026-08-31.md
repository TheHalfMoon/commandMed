# E004 Phase A Diagnostic V3 Result Reconciliation — 2026-08-31

**Spec:** 007 SFT V1  
**Artifact class:** execution-result reconciliation  
**Canonical authority merge:** `ff354f76262475d9be9f168731d228b4893223e4`  
**Canonical diagnostic implementation merge:** `1c901e7dba799f20fa679cbb980478deb7e8dce7`  
**Reviewed implementation head:** `acfef9afb656a7aaae515b3294577109454c378c`  
**V3 workflow:** `.github/workflows/e004-phase-a-diagnostic-v3.yml`  
**Historical target workflow:** `.github/workflows/e004-conversion-runtime-evidence.yml` at `ef1be50f4a076d9f03abfffee342d2c244b0d199`  
**Training authority:** NONE  
**Spend authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Reconcile the single authorized E004 Phase A Diagnostic V3 execution against the canonical V3 authority and the historical target workflow without converting a current reproducible route observation into an unsupported claim about the exact historical failure line, historical causal mechanism, or combined pip-index resolution.

This record is evidence reconciliation only. It does not repair, mutate, dispatch, or rerun the target workflow. It creates no model, conversion, inference, benchmark, contamination, A15, training, credential, artifact/cache, procurement, payment, or spend authority.

## 2. Canonical lifecycle completed through V3 execution

The dependency-ordered V3 lifecycle reached the authorized execution exactly once:

```text
V3_AUTHORITY_RECORD_EXACT_HEAD_REVIEW_AND_CANONICAL_MERGE=COMPLETE
V3_AUTHORITY_MERGE=ff354f76262475d9be9f168731d228b4893223e4
V3_IMPLEMENTATION_EXACT_HEAD_REVIEW=COMPLETE
V3_IMPLEMENTATION_REVIEWED_HEAD=acfef9afb656a7aaae515b3294577109454c378c
V3_IMPLEMENTATION_MATERIAL_BLOCKER=NO
V3_IMPLEMENTATION_GUARDED_MERGE=1c901e7dba799f20fa679cbb980478deb7e8dce7
V3_DIAGNOSTIC_EXECUTION_COUNT=1
V3_DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
V3_AUTOMATIC_RETRY_USED=NO
V3_FAILED_JOB_RERUN_USED=NO
```

No V3 rerun, later matching push execution, alternate trigger, or second diagnostic execution is authorized after this point.

## 3. Exact retained execution identity

GitHub Actions directly records:

```text
V3_RUN_ID=33421355449
V3_RUN_NUMBER=1
V3_RUN_ATTEMPT=1
V3_RUN_EVENT=push
V3_RUN_HEAD_BRANCH=main
V3_RUN_HEAD_SHA=1c901e7dba799f20fa679cbb980478deb7e8dce7
V3_RUN_STATUS=completed
V3_RUN_CONCLUSION=success
V3_JOB_ID=99584236750
V3_JOB_NAME=diagnose
V3_JOB_CONCLUSION=success
V3_WORKFLOW_ID=346833274
V3_CHECK_SUITE_ID=90560834319
V3_ARTIFACT_COUNT=0
```

The run started from the exact authority predecessor required by the one-shot guard:

```text
V3_EVENT_BEFORE_SHA=ff354f76262475d9be9f168731d228b4893223e4
V3_AUTHORITY_MERGE_SHA=ff354f76262475d9be9f168731d228b4893223e4
```

The canonical implementation merge itself has ordered parents:

```text
PARENT_1=ff354f76262475d9be9f168731d228b4893223e4
PARENT_2=acfef9afb656a7aaae515b3294577109454c378c
```

## 4. Runtime subject and frozen target bindings

The retained job logs record:

```text
V3_RUNNER_OS=Linux
V3_RUNNER_ARCH=X64
V3_IMAGE_OS=ubuntu24
V3_IMAGE_VERSION=20260823.283.1
RUNNER_OS_RELEASE=Ubuntu_24.04.4_LTS
PYTHON_VERSION=3.12.3
PIP_VERSION=24.0

HISTORICAL_TARGET_HEAD_SHA=ef1be50f4a076d9f03abfffee342d2c244b0d199
HISTORICAL_TARGET_WORKFLOW_BLOB_SHA1=591317f1f570480b9ac68e7956d070db8ed5ef45
HISTORICAL_TARGET_WORKFLOW_RAW_SHA256=95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327
EXACT_REQUIREMENT=torch==2.11.0+cpu
TARGET_ALLOWLIST=github.com,pypi.org,files.pythonhosted.org,download.pytorch.org
EXACT_TARGET_ALLOWLIST_SHA256=00d2283fdbcfedf6e8e6a24991892bd09acc8af58c61a38dadbf3d6d67f87353
```

The historical target workflow's Phase A command is also exact and frozen at that target head:

```text
python3 -m pip download -vv --proxy "$proxy_url" --dest "$wheelhouse" \
  --index-url https://pypi.org/simple \
  --extra-index-url https://download.pytorch.org/whl/cpu \
  "torch==2.11.0+cpu" ...
```

Its embedded CONNECT proxy allows only canonical hosts in:

```text
github.com
pypi.org
files.pythonhosted.org
download.pytorch.org
```

and only on port `443`.

## 5. Direct V3 dependency-route observations

The bounded PyTorch CPU index metadata request completed without redirect:

```text
INDEX_HTTP_STATUS=200
INDEX_REDIRECT_COUNT=0
INDEX_FINAL_ROUTE=https://download.pytorch.org/whl/cpu/torch/
INDEX_FINAL_HOST=download.pytorch.org
INDEX_METADATA_BYTES=376117
INDEX_METADATA_SHA256=b476f1efee2fb57c8f4fba5831bf38359be2b6d691b25cf4ff60b8e8c9b0ab3a
INDEX_EXACT_VERSION_LINK_COUNT=28
```

The live runtime compatibility model was derived from pip's vendored `packaging.tags.sys_tags()` and exact wheel filenames were parsed with `parse_wheel_filename()`:

```text
DIAGNOSTIC_PYTHON_TAG=cp312
DIAGNOSTIC_MACHINE=x86_64
DIAGNOSTIC_COMPATIBLE_TAG_COUNT=1067
DIAGNOSTIC_COMPATIBLE_TAG_SET_SHA256=5a4a42b93cab233312da9ad22e8222e41cf127e458f367082af8db70059fa85a
INVALID_EXACT_WHEEL_FILENAME_COUNT=0
RELEVANT_EXACT_WHEEL_COUNT=1
```

Exactly one `torch==2.11.0+cpu` wheel from that configured PyTorch CPU index was compatible with the live Ubuntu/Python interpreter, ABI, and platform tags:

```text
RELEVANT_WHEEL_1_BASENAME=torch-2.11.0+cpu-cp312-cp312-manylinux_2_28_x86_64.whl
RELEVANT_WHEEL_1_INDEX_ROUTE=https://download-r2.pytorch.org/whl/cpu/torch-2.11.0%2Bcpu-cp312-cp312-manylinux_2_28_x86_64.whl
RELEVANT_WHEEL_1_INITIAL_HOST=download-r2.pytorch.org
```

The exact historical CONNECT decision applied to this observed route is:

```text
ALLOWLIST_DECISION host=download-r2.pytorch.org scheme=https port=443 result=DENY
```

The bounded HEAD-only probe then succeeded directly on that same route:

```text
RELEVANT_WHEEL_1_HEAD_STATUS=200
RELEVANT_WHEEL_1_FINAL_ROUTE=https://download-r2.pytorch.org/whl/cpu/torch-2.11.0%2Bcpu-cp312-cp312-manylinux_2_28_x86_64.whl
RELEVANT_WHEEL_1_FINAL_HOST=download-r2.pytorch.org
HEAD_ROUTE_PROBE_FAILURES=0
```

The final deterministic workflow-emitted observation was:

```text
DISCOVERED_ROUTE_HOSTS=download-r2.pytorch.org,download.pytorch.org
DISCOVERED_DENIED_HOSTS=download-r2.pytorch.org
V3_DIAGNOSTIC_OBSERVATION=DENIED_ROUTE_HOST_OBSERVED
V3_DENIED_REQUIRED_ROUTE_OBSERVED=YES
```

`V3_DENIED_REQUIRED_ROUTE_OBSERVED=YES` is retained as the exact emitted field name from the V3 workflow. This reconciliation does not interpret that field as proof that the route is required by the historical combined-index pip command.

## 6. Reconciliation finding

The retained V3 evidence proves a bounded route observation for the explicitly configured PyTorch CPU extra index, not a complete resolution result for the historical pip command.

The evidence directly establishes:

1. the target workflow requests `torch==2.11.0+cpu` and configures both `https://pypi.org/simple` as the primary index and `https://download.pytorch.org/whl/cpu` as an extra index;
2. V3 read bounded metadata for the PyTorch CPU extra index only;
3. V3 found 28 exact-version links there and, using the live pip wheel-tag model, exactly one link compatible with the live Ubuntu 24.04 / Python 3.12 runtime subject;
4. that observed compatible extra-index route is `download-r2.pytorch.org:443`;
5. the exact historical Phase A CONNECT policy deterministically returns `DENY` for that observed host because it is absent from the allowlist;
6. the HEAD probe succeeded on that route, so the route observation itself was not unresolved.

V3 did **not** enumerate the primary PyPI `torch` index and did **not** retain combined-index pip resolver output. It therefore cannot exclude a compatible allowlisted candidate from the primary index and cannot prove that `download-r2.pytorch.org` was a required download host for the exact historical pip command.

The supported reconciliation is therefore:

```text
PYTORCH_CPU_EXTRA_INDEX_COMPATIBLE_ROUTE_OBSERVED=YES
PYTORCH_CPU_EXTRA_INDEX_COMPATIBLE_ROUTE_HOST=download-r2.pytorch.org
PYTORCH_CPU_EXTRA_INDEX_COMPATIBLE_ROUTE_PORT=443
PYTORCH_CPU_EXTRA_INDEX_COMPATIBLE_ROUTE_ALLOWLIST_RESULT=DENY
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=NEEDS_EVIDENCE
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=NEEDS_EVIDENCE
OBSERVED_REQUIRED_DOWNLOAD_HOST=NEEDS_EVIDENCE
STATIC_WORKFLOW_DEFECT_PROVEN=NO_NEEDS_PRIMARY_INDEX_EVIDENCE
```

No stronger static-defect or required-route conclusion is authorized from V3.

## 7. Historical causal boundary remains unresolved

V3 was not a rerun of historical target job `99409197359`; it did not recover the target job's historical stderr or exact proxy deny line. The historical target remains:

```text
TARGET_RUN_ID=33366859146
TARGET_JOB_ID=99409197359
TARGET_HEAD_SHA=ef1be50f4a076d9f03abfffee342d2c244b0d199
TARGET_CONCLUSION=failure
RUNNER_PREFLIGHT=PASS
PHASE_A_ALLOWLISTED_PUBLIC_SOURCE_AND_DEPENDENCY_STAGING=FAIL
PHASE_B_OFFLINE_ENVIRONMENT_LOCAL_GGUF_ATTESTATION_AND_REBUILD=SKIPPED
FINAL_RUNTIME_EVIDENCE_MANIFEST=SKIPPED
HISTORICAL_STDERR_RECOVERED=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

The current extra-index route observation does not retroactively prove the exact historical causal chain. Preserve:

```text
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

## 8. V3 safety and authority boundary satisfied

The retained run records:

```text
V3_DIAGNOSTIC_COMPLETED=YES
TARGET_WORKFLOW_EXECUTED=NO
TARGET_WORKFLOW_MUTATED=NO
MODEL_WEIGHT_DOWNLOADED=NO
DEPENDENCY_ARTIFACT_BODY_DOWNLOADED=NO
MODEL_EXECUTION=NO
BENCHMARK_EXECUTION=NO
CONTAMINATION_ASSESSMENT_EXECUTION=NO
A15_ACTIVATION=NO
TRAINING_EXECUTION=NO
ARTIFACT_UPLOAD=NO
CACHE_UPLOAD=NO
CREDENTIAL_USE=NO
REPOSITORY_MUTATION_BY_RUNTIME=NO
SPEND_USD=0
V3_ARTIFACT_COUNT=0
```

No evidence in V3 creates any broader scientific or execution authority.

## 9. Post-reconciliation state

Until this reconciliation is independently reviewed and canonically merged, it is only a candidate interpretation of the retained V3 evidence.

If this record becomes canonical with no material review blocker, it may support a **separate later diagnostic-authority candidate** whose maximum purpose is to collect the missing direct evidence needed to resolve the primary-PyPI candidate set and/or the historical command's combined-index resolution behavior without downloading dependency artifact bodies or executing the target workflow.

This reconciliation does not itself grant that diagnostic execution, target repair, or new target-attempt authority. A target-workflow repair remains premature unless later direct evidence proves a specific repairable defect.

```text
V3_DIAGNOSTIC_EXECUTION_STATE=CONSUMED_COMPLETE
V3_DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=NEEDS_EVIDENCE
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=NEEDS_EVIDENCE
STATIC_WORKFLOW_DEFECT_PROVEN=NO_NEEDS_PRIMARY_INDEX_EVIDENCE
COMPONENT_RUNTIME_EVIDENCE=FAILED_PHASE_A_HISTORICAL
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PENDING_V3_RESULT_RECONCILIATION_AND_PRIMARY_INDEX_EVIDENCE
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE

FOLLOW_ON_DIAGNOSTIC_AUTHORITY=NONE
TARGET_WORKFLOW_REPAIR_AUTHORITY=NONE
NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPT_AUTHORITY=NONE
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

## 10. Required merge-exit gate

This record may become canonical only after a fresh exact-head independent repository review verifies at least:

- exact V3 run/job/head/attempt identities;
- the one-shot V3 allowance is consumed and not reopened;
- the target workflow's exact Phase A CONNECT semantics are represented correctly;
- the exact current runtime-subject PyTorch CPU extra-index wheel compatibility evidence is represented correctly;
- the primary PyPI exact candidate set and combined-index resolution remain explicitly unresolved;
- `STATIC_WORKFLOW_DEFECT_PROVEN=NO_NEEDS_PRIMARY_INDEX_EVIDENCE` is preserved;
- the historical failure cause remains `NEEDS_EVIDENCE`;
- no follow-on diagnostic execution, repair, rerun, model, conversion, inference, benchmark, contamination, A15, training, credential, artifact/cache, or spend authority is created.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```

Only after guarded canonical merge of that exact reviewed head may a separate follow-on diagnostic-authority candidate be created.