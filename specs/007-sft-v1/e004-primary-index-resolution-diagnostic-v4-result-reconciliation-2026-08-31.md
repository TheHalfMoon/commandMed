# E004 Primary-Index / Combined-Resolution Diagnostic V4 Result Reconciliation — 2026-08-31

**Spec:** 007 SFT V1  
**Artifact class:** execution-result reconciliation  
**Canonical V4 parent authority merge:** `782775c495b0638a8dfd8f39b1ffec01a0fa0152`  
**Canonical V4 identity-binding addendum merge:** `78c0cb66460f00e0a7c5c9381fdc1c3a08cebeae`  
**Canonical reusable-enforcer merge:** `fcb84a483d62cde9aeb506c3469498b494b5086d`  
**Reviewed successor caller head:** `be00751b549b99e9c7a384d46c77b6edc7c04120`  
**Canonical successor caller merge:** `97492acf6982c59a7118f5884dee84e55a0ccc82`  
**V4 caller workflow:** `.github/workflows/e004-primary-index-resolution-diagnostic-v4.yml`  
**V4 reusable enforcer:** `.github/workflows/e004-primary-index-resolution-enforcer-v4.yml@fcb84a483d62cde9aeb506c3469498b494b5086d`  
**Historical target workflow:** `.github/workflows/e004-conversion-runtime-evidence.yml` at `ef1be50f4a076d9f03abfffee342d2c244b0d199`  
**Training authority:** NONE  
**Spend authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Reconcile the single authorized V4 diagnostic execution against the canonical V4 parent authority and identity-binding addendum.

The V4 evidence resolves the two questions intentionally left open by V3:

```text
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION
```

This record distinguishes three separate propositions that MUST NOT be conflated:

1. what the V4 runtime directly observed from the exact configured primary and extra indexes;
2. what those observations prove about the historical target workflow's static CONNECT policy under the exact V4 runtime subject; and
3. what remains unknown about the exact causal mechanism of historical failed target job `99409197359`.

This record is evidence reconciliation only. It does not mutate or repair the target workflow, does not dispatch or rerun the target workflow, does not reopen V2/V3/V4 allowances, and creates no model, conversion, inference, benchmark, contamination, A15, training, credential, upload, procurement, payment, or spend authority.

## 2. Completed V4 lifecycle and one-shot consumption

The authorized V4 lifecycle reached its one execution exactly once:

```text
V4_PARENT_AUTHORITY_MERGE=782775c495b0638a8dfd8f39b1ffec01a0fa0152
V4_IDENTITY_ADDENDUM_MERGE=78c0cb66460f00e0a7c5c9381fdc1c3a08cebeae
V4_ENFORCER_REVIEW=COMPLETE_MATERIAL_BLOCKER_NO
V4_ENFORCER_MERGE=fcb84a483d62cde9aeb506c3469498b494b5086d
V4_SUCCESSOR_PR=156
V4_SUCCESSOR_REVIEWED_HEAD=be00751b549b99e9c7a384d46c77b6edc7c04120
V4_SUCCESSOR_REVIEW=MATERIAL_BLOCKER_NO
V4_SUCCESSOR_GUARDED_MERGE=97492acf6982c59a7118f5884dee84e55a0ccc82
V4_DIAGNOSTIC_EXECUTION_COUNT=1
V4_DIAGNOSTIC_ALLOWANCE_REMAINING=0
V4_AUTOMATIC_RETRY_USED=NO
V4_FAILED_JOB_RERUN_USED=NO
```

No V4 rerun, later matching-push diagnostic body, alternate trigger, or second V4 execution is authorized after this point.

## 3. Exact retained V4 execution identity

GitHub Actions directly records:

```text
V4_RUN_ID=33429294549
V4_RUN_NUMBER=1
V4_RUN_ATTEMPT=1
V4_RUN_EVENT=push
V4_RUN_HEAD_BRANCH=main
V4_RUN_HEAD_SHA=97492acf6982c59a7118f5884dee84e55a0ccc82
V4_RUN_HEAD_TREE_SHA=9a0cc279eb91906ce180b2d3b4109ee6df6d8e10
V4_RUN_STATUS=completed
V4_RUN_CONCLUSION=success
V4_JOB_ID=99610442620
V4_JOB_NAME=diagnose / enforce-and-diagnose
V4_JOB_CONCLUSION=success
V4_WORKFLOW_ID=346894675
V4_CHECK_SUITE_ID=90583576411
V4_REFERENCED_ENFORCER_SHA=fcb84a483d62cde9aeb506c3469498b494b5086d
```

The canonical caller merge has the required merge-commit parents:

```text
V4_MERGE_PARENT_1=fcb84a483d62cde9aeb506c3469498b494b5086d
V4_MERGE_PARENT_2=be00751b549b99e9c7a384d46c77b6edc7c04120
```

The retained job logs additionally record:

```text
V4_LOCAL_EVENT_GATE=PASS
V4_EXPECTED_PREDECESSOR_SHA=fcb84a483d62cde9aeb506c3469498b494b5086d
V4_SUCCESSOR_PR_NUMBER=156
V4_PUSH_HEAD_SHA=97492acf6982c59a7118f5884dee84e55a0ccc82
V4_RUN_ATTEMPT=1
V4_AUTHORIZED_SPEND_USD=0
```

## 4. Identity-binding evidence

Before either package-index metadata request, the reusable enforcer completed the bounded public-GitHub provenance gate:

```text
V4_GITHUB_IDENTITY_GATE=PASS
V4_GITHUB_IDENTITY_REQUEST_COUNT=3
V4_SUCCESSOR_PR_HEAD_SHA=be00751b549b99e9c7a384d46c77b6edc7c04120
V4_MERGE_TREE_SHA=9a0cc279eb91906ce180b2d3b4109ee6df6d8e10
V4_PULL_HEAD_TREE_SHA=9a0cc279eb91906ce180b2d3b4109ee6df6d8e10
V4_PULL_METADATA_BYTES=18693
V4_PULL_METADATA_SHA256=fb0c4a3dec9e2a7a2554aa2712f109580ed0459fa70e0ff705df468791796496
V4_MERGE_METADATA_BYTES=6448
V4_MERGE_METADATA_SHA256=77c534ab302a2c3c21ed393b6e3bf48815cd182e0929250e5088e124f997310f
V4_HEAD_METADATA_BYTES=4498
V4_HEAD_METADATA_SHA256=7ecaf8f1318670dac4f0dfd96583a59d2f7cb494a7138cbb16b9bce03ed4c5a9
V4_GITHUB_IDENTITY_AUTHENTICATION=NONE
V4_GITHUB_IDENTITY_REDIRECTS=NONE
```

Therefore the retained V4 index observations are bound to the exact independently reviewed caller tree and exact pinned reusable enforcer used by the one-shot merge-triggered execution.

## 5. Exact diagnostic subject

The V4 job ran on the authorized standard public runner lane:

```text
RUNNER_IMAGE=ubuntu-24.04
RUNNER_OS_RELEASE=Ubuntu_24.04.4_LTS
RUNNER_IMAGE_VERSION=20260823.283.1
PYTHON_VERSION=3.12.3
DIAGNOSTIC_MACHINE=x86_64
DIAGNOSTIC_COMPATIBLE_TAG_COUNT=1067
DIAGNOSTIC_COMPATIBLE_TAG_SET_SHA256=5a4a42b93cab233312da9ad22e8222e41cf127e458f367082af8db70059fa85a
AUTHORIZED_SPEND_USD=0
```

The frozen dependency/index subject was:

```text
EXACT_REQUIREMENT=torch==2.11.0+cpu
PRIMARY_INDEX=https://pypi.org/simple/torch/
EXTRA_INDEX=https://download.pytorch.org/whl/cpu/torch/
HISTORICAL_TARGET_HEAD_SHA=ef1be50f4a076d9f03abfffee342d2c244b0d199
HISTORICAL_TARGET_WORKFLOW_BLOB_SHA1=591317f1f570480b9ac68e7956d070db8ed5ef45
HISTORICAL_TARGET_WORKFLOW_RAW_SHA256=95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327
HISTORICAL_TARGET_ALLOWLIST=github.com,pypi.org,files.pythonhosted.org,download.pytorch.org
```

## 6. Direct primary-index observations

The V4 run directly retrieved the configured PyPI Simple metadata endpoint and observed:

```text
PRIMARY_METADATA_ROUTE_DECISION={"host":"pypi.org","port":443,"result":"ALLOW","scheme":"https"}
PRIMARY_INDEX_HTTP_STATUS=200
PRIMARY_INDEX_REDIRECT_COUNT=0
PRIMARY_INDEX_FINAL_ROUTE=https://pypi.org/simple/torch/
PRIMARY_INDEX_FINAL_HOST=pypi.org
PRIMARY_INDEX_METADATA_BYTES=468930
PRIMARY_INDEX_METADATA_SHA256=33ef7f2cd5f8e07e775af9665ed78f19a53a6fd40cec9a2a4692835dc88b4de3
PRIMARY_INDEX_LINK_COUNT=911
PRIMARY_EXACT_VERSION_CANDIDATE_COUNT=0
PRIMARY_EXACT_WHEEL_COUNT=0
PRIMARY_COMPATIBLE_WHEEL_COUNT=0
PRIMARY_EXACT_SDIST_COUNT=0
PRIMARY_VIABLE_SDIST_COUNT=0
PRIMARY_ALLOWLISTED_VIABLE_ROUTE_COUNT=0
PRIMARY_DENIED_VIABLE_ROUTE_COUNT=0
PRIMARY_UNRESOLVED_EXACT_LIKE_COUNT=0
PRIMARY_INVALID_REQUIRES_PYTHON_COUNT=0
```

Because the exact-version candidate count is zero and both ambiguity counters are zero, the supported primary-index reconciliation is:

```text
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=OBSERVED_EMPTY
```

This is a direct V4 observation for the retrieved metadata identity above. It is not inferred from V3.

## 7. Direct extra-index observations

The V4 run directly re-observed the configured PyTorch CPU Simple endpoint:

```text
EXTRA_METADATA_ROUTE_DECISION={"host":"download.pytorch.org","port":443,"result":"ALLOW","scheme":"https"}
EXTRA_INDEX_HTTP_STATUS=200
EXTRA_INDEX_REDIRECT_COUNT=0
EXTRA_INDEX_FINAL_ROUTE=https://download.pytorch.org/whl/cpu/torch/
EXTRA_INDEX_FINAL_HOST=download.pytorch.org
EXTRA_INDEX_METADATA_BYTES=376117
EXTRA_INDEX_METADATA_SHA256=62638a0c649220f60dcebdc6d7745316b43f815f81743fc3203ac4beee62eb46
EXTRA_INDEX_LINK_COUNT=1137
EXTRA_EXACT_VERSION_CANDIDATE_COUNT=28
EXTRA_EXACT_WHEEL_COUNT=28
EXTRA_COMPATIBLE_WHEEL_COUNT=1
EXTRA_EXACT_SDIST_COUNT=0
EXTRA_VIABLE_SDIST_COUNT=0
EXTRA_ALLOWLISTED_VIABLE_ROUTE_COUNT=0
EXTRA_DENIED_VIABLE_ROUTE_COUNT=1
EXTRA_UNRESOLVED_EXACT_LIKE_COUNT=0
EXTRA_INVALID_REQUIRES_PYTHON_COUNT=0
```

Exactly one exact-version wheel is viable for the V4 Ubuntu/Python tag subject:

```text
V4_COMPATIBLE_EXACT_CANDIDATE_BASENAME=torch-2.11.0+cpu-cp312-cp312-manylinux_2_28_x86_64.whl
V4_COMPATIBLE_EXACT_CANDIDATE_HOST=download-r2.pytorch.org
V4_COMPATIBLE_EXACT_CANDIDATE_SCHEME=https
V4_COMPATIBLE_EXACT_CANDIDATE_PORT=443
V4_COMPATIBLE_EXACT_CANDIDATE_WHEEL_TAG_COMPATIBLE=true
V4_COMPATIBLE_EXACT_CANDIDATE_PYTHON_COMPATIBLE=true
V4_COMPATIBLE_EXACT_CANDIDATE_YANKED=false
V4_COMPATIBLE_EXACT_CANDIDATE_ALLOWLIST_RESULT=DENY
```

The V4 workflow did not fetch that distribution artifact body.

## 8. Combined configured-index conclusion

The two configured indexes were observed in the same exact V4 run. Their deterministic aggregate is:

```text
COMBINED_EXACT_VERSION_CANDIDATE_COUNT=28
COMBINED_ALLOWLISTED_VIABLE_ROUTE_COUNT=0
COMBINED_DENIED_VIABLE_ROUTE_COUNT=1
COMBINED_UNRESOLVED_EXACT_LIKE_COUNT=0
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=OBSERVED_NO_ALLOWLISTED_COMPATIBLE_ROUTE
```

All four evidence conditions in the V4 parent authority Section 6 are satisfied:

1. the primary index has zero exact `torch==2.11.0+cpu` candidates, with no unresolved exact-like or invalid `Requires-Python` ambiguity;
2. the extra-index candidate set was directly observed in V4;
3. the combined configured-index set has exactly one viable candidate for the V4 runtime subject and that route is denied by the exact historical CONNECT allowlist;
4. no dependency artifact body was downloaded and the target workflow was not executed.

The resulting bounded static finding is:

```text
STATIC_WORKFLOW_DEFECT_PROVEN=YES_EXACT_V4_RUNTIME_CONFIG_ROUTE_POLICY_EXCLUSION
V4_REQUIRED_COMPATIBLE_ROUTE_HOST=download-r2.pytorch.org
V4_REQUIRED_COMPATIBLE_ROUTE_PORT=443
V4_REQUIRED_COMPATIBLE_ROUTE_ALLOWLIST_RESULT=DENY
```

Meaning: for the exact historical target workflow dependency/index/CONNECT configuration evaluated against the exact V4 runner/Python compatibility subject, the static CONNECT policy excludes the only compatible route available across the two configured indexes for `torch==2.11.0+cpu`.

This is a static workflow/configuration defect conclusion. It is not a claim that the retained historical failed job emitted a deny for this host.

## 9. Historical causal boundary remains unresolved

The V4 run was not a rerun of historical target job `99409197359`. It did not recover that job's missing historical stderr or an exact historical CONNECT deny line.

The historical target evidence remains:

```text
TARGET_RUN_ID=33366859146
TARGET_JOB_ID=99409197359
TARGET_HEAD_SHA=ef1be50f4a076d9f03abfffee342d2c244b0d199
TARGET_RUN_ATTEMPT=1
TARGET_CONCLUSION=failure
RUNNER_PREFLIGHT=PASS
PHASE_A_ALLOWLISTED_PUBLIC_SOURCE_AND_DEPENDENCY_STAGING=FAIL
PHASE_B_OFFLINE_ENVIRONMENT_LOCAL_GGUF_ATTESTATION_AND_REBUILD=SKIPPED
FINAL_RUNTIME_EVIDENCE_MANIFEST=SKIPPED
HISTORICAL_STDERR_RECOVERED=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

Therefore this reconciliation MUST preserve:

```text
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

The supported statement is narrower: V4 proves a static route-policy defect that is sufficient to prevent the exact V4 runtime subject from obtaining a compatible `torch==2.11.0+cpu` distribution through the historical target workflow's frozen CONNECT policy. It does not retroactively prove the exact causal line of the historical failure.

## 10. Safety and authority boundary satisfied

The retained V4 job logs record:

```text
V4_DIAGNOSTIC_COMPLETED=YES
TARGET_WORKFLOW_EXECUTED=NO
TARGET_WORKFLOW_MUTATED=NO
PIP_DOWNLOAD_EXECUTED=NO
PIP_INSTALL_EXECUTED=NO
DEPENDENCY_ARTIFACT_BODY_DOWNLOADED=NO
MODEL_WEIGHT_DOWNLOADED=NO
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
```

No V4 evidence creates broader scientific or execution authority.

## 11. Evidence-backed minimum repair candidate

Because the static defect is now proven for the exact V4 runtime/config subject, a later separately authorized repair candidate may be considered.

The maximum evidence-backed repair surface presently justified is:

```text
REPAIR_CANDIDATE_SCOPE=PHASE_A_CONNECT_ALLOWLIST_ONLY
REPAIR_CANDIDATE_ADD_HOST=download-r2.pytorch.org
REPAIR_CANDIDATE_SCHEME=https
REPAIR_CANDIDATE_PORT=443
REPAIR_CANDIDATE_PRESERVE_EXISTING_ALLOWLIST=YES
REPAIR_CANDIDATE_PRESERVE_DENY_BY_DEFAULT=YES
TARGET_WORKFLOW_OTHER_LOGIC_MUTATION=PROHIBITED
```

That candidate is justified because the V4 primary index is observed empty for the exact requirement, while the sole V4-compatible combined-index route is `download-r2.pytorch.org:443` and the historical CONNECT policy excludes it.

This section identifies the smallest technically justified candidate only. It does **not** grant repair authority and does **not** authorize a new target runtime-evidence attempt.

## 12. Post-reconciliation authority state

Until this record is independently reviewed at its exact final head and guarded-merged canonically, it is only a candidate interpretation of the retained V4 evidence.

If this exact record becomes canonical with `MATERIAL_BLOCKER=NO`, it may support creation of a **separate founder-authorized target-repair/new-runtime-attempt authority candidate** limited to the evidence-backed scope in Section 11.

That later authority, if separately reviewed and canonically merged, may at most authorize:

1. the minimum CONNECT allowlist repair proven by V4;
2. exact new target-workflow content identity after the repair;
3. independent exact-head review of that repair implementation;
4. guarded canonical merge;
5. exactly one new zero-spend standard public `ubuntu-24.04` target runtime-evidence attempt under the pre-existing E004 scientific boundaries;
6. retained runtime evidence and a separate result reconciliation.

No such later authority exists merely because this reconciliation is written or merged.

```text
V4_DIAGNOSTIC_EXECUTION_STATE=CONSUMED_COMPLETE
V4_DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=OBSERVED_EMPTY
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=OBSERVED_NO_ALLOWLISTED_COMPATIBLE_ROUTE
STATIC_WORKFLOW_DEFECT_PROVEN=YES_EXACT_V4_RUNTIME_CONFIG_ROUTE_POLICY_EXCLUSION
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
HISTORICAL_STDERR_RECOVERED=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO

TARGET_WORKFLOW_REPAIR_AUTHORITY=NONE
NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPT_AUTHORITY=NONE
V2_ALLOWANCE_REOPEN_AUTHORITY=NONE
V3_ALLOWANCE_REOPEN_AUTHORITY=NONE
V4_ALLOWANCE_REOPEN_AUTHORITY=NONE
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

COMPONENT_RUNTIME_EVIDENCE=FAILED_PHASE_A_HISTORICAL_WITH_STATIC_ROUTE_DEFECT_PROVEN_BY_V4
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PENDING_V4_RESULT_RECONCILIATION_AND_SEPARATE_REPAIR_AUTHORITY
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## 13. Required merge-exit gate

This reconciliation may become canonical only after a fresh exact-head independent repository review verifies at least:

- exact V4 run/job/head/attempt and pinned-enforcer identities;
- V4 local event and public-GitHub identity gates passed;
- the V4 one-shot allowance is consumed and not reopened;
- the primary PyPI exact candidate set is directly observed empty with no unresolved exact-like ambiguity;
- the PyTorch CPU extra-index candidate set is directly re-observed in V4;
- exactly one combined-index candidate is compatible with the V4 runtime subject and its route is `download-r2.pytorch.org:443`;
- that route is denied by the exact historical CONNECT allowlist;
- no compatible allowlisted route exists across the two configured indexes;
- `STATIC_WORKFLOW_DEFECT_PROVEN=YES_EXACT_V4_RUNTIME_CONFIG_ROUTE_POLICY_EXCLUSION` is no broader than the retained evidence;
- the historical target-job causal boundary remains `PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE` and no exact historical deny line is claimed;
- Section 11 is only a repair candidate, not repair authority;
- no target repair/new target attempt, model, conversion, inference, benchmark, contamination, A15, training, credential, upload, procurement/payment, or spend authority is created.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```

Only after guarded canonical merge of that exact reviewed head may a separate repair/new-runtime-attempt authority candidate be created.
