# E004 Primary-Index / Combined-Resolution Diagnostic V4 Authority — 2026-08-31

**Spec:** 007 SFT V1  
**Decision owner:** Founder  
**Artifact class:** bounded diagnostic-only execution authority  
**Canonical base:** `04eb2bea5a1d825f5599f49224475e4d2ab084a8`  
**Prior reconciliation:** `specs/007-sft-v1/e004-phase-a-diagnostic-v3-result-reconciliation-2026-08-31.md`  
**Prior reconciliation merge:** `04eb2bea5a1d825f5599f49224475e4d2ab084a8`  
**Authority effect before canonical merge:** NONE  
**Model weight authority:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation authority:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Authorize the smallest dependency-ordered successor to the canonical V3 result reconciliation: one independently reviewed, zero-spend, diagnostic-only GitHub Actions execution whose sole purpose is to collect direct retained metadata evidence needed to resolve the two fail-closed questions left by V3:

```text
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=NEEDS_EVIDENCE
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=NEEDS_EVIDENCE
```

The diagnostic is limited to the exact historical Phase A requirement and index configuration:

```text
EXACT_REQUIREMENT=torch==2.11.0+cpu
PRIMARY_INDEX=https://pypi.org/simple
EXTRA_INDEX=https://download.pytorch.org/whl/cpu
HISTORICAL_TARGET_HEAD_SHA=ef1be50f4a076d9f03abfffee342d2c244b0d199
HISTORICAL_TARGET_WORKFLOW_BLOB_SHA1=591317f1f570480b9ac68e7956d070db8ed5ef45
HISTORICAL_TARGET_WORKFLOW_RAW_SHA256=95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327
```

This authority does not repair, mutate, dispatch, or rerun the target runtime-evidence workflow. It does not reopen V2 or V3 allowances. It creates no model, conversion, inference, benchmark, contamination, A15, training, credential, artifact/cache-upload, procurement, payment, or spend authority.

## 2. Founder directive and dependency ordering

After the V3 result reconciliation was independently reviewed at exact head `0062449c2dfe1addd3f1e381b3a2596f99a01b86` with `MATERIAL_BLOCKER=NO`, guarded-merged canonically as `04eb2bea5a1d825f5599f49224475e4d2ab084a8`, and canonical governance plus the active Spec 007 authority chain were re-read, the Founder directive remains:

```text
FOUNDER_DIRECTIVE=go ahead do not stop until finish the project , you have all approvals fro me
FOUNDER_DIRECTIVE_SHA256=1b7c31a818ea7b50d0fe1e12b159d328afa11a9b0d74359cca19951e9fd75eab
FOUNDER_DIRECTIVE_DATE=2026-08-31
FOUNDER_DIRECTIVE_INTERPRETATION=ORDINARY_AUTHORIZED_WORK_ONLY_SUBJECT_TO_CANONICAL_GATES
```

At the current dependency frontier, that directive is interpreted narrowly to authorize creation and qualification of this V4 authority record. It does not waive independent review, evidence, scientific-integrity, provenance, quarantine, safety, finance, execution, or later lifecycle gates.

## 3. Preserved V3 evidence boundary

V4 starts from the canonical V3 reconciliation and must not broaden it:

```text
V3_RUN_ID=33421355449
V3_JOB_ID=99584236750
V3_RUN_ATTEMPT=1
V3_RUN_CONCLUSION=success
V3_DIAGNOSTIC_EXECUTION_STATE=CONSUMED_COMPLETE
V3_DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0

PYTORCH_CPU_EXTRA_INDEX_COMPATIBLE_ROUTE_OBSERVED=YES
PYTORCH_CPU_EXTRA_INDEX_COMPATIBLE_ROUTE_HOST=download-r2.pytorch.org
PYTORCH_CPU_EXTRA_INDEX_COMPATIBLE_ROUTE_PORT=443
PYTORCH_CPU_EXTRA_INDEX_COMPATIBLE_ROUTE_ALLOWLIST_RESULT=DENY

PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=NEEDS_EVIDENCE
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=NEEDS_EVIDENCE
OBSERVED_REQUIRED_DOWNLOAD_HOST=NEEDS_EVIDENCE
STATIC_WORKFLOW_DEFECT_PROVEN=NO_NEEDS_PRIMARY_INDEX_EVIDENCE
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
HISTORICAL_STDERR_RECOVERED=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

The V3 emitted field `V3_DENIED_REQUIRED_ROUTE_OBSERVED=YES` remains an historical workflow-emitted field name only. V4 must not treat it as proof that `download-r2.pytorch.org` was required by the historical combined-index pip command.

## 4. Bounded V4 authority

Only after this authority record is independently reviewed and canonically merged, and only after a separate minimal V4 diagnostic workflow implementation is independently reviewed at its exact final head and canonically merged, the project may execute exactly one V4 diagnostic run under these bounds:

```text
E004_PRIMARY_INDEX_RESOLUTION_DIAGNOSTIC_V4_AUTHORITY=AUTHORIZED_BOUNDED
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
MAX_AUTHORIZED_V4_DIAGNOSTIC_RUNS=1
V4_PURPOSE=COLLECT_PRIMARY_INDEX_AND_COMBINED_CANDIDATE_METADATA_EVIDENCE
V4_TRIGGER=push_to_main_path_scoped_to_exact_v4_diagnostic_workflow_file
V4_AUTOMATIC_RETRY_AUTHORITY=NONE
V4_FAILED_JOB_RERUN_AUTHORITY=NONE
V4_TARGET_WORKFLOW_DISPATCH_AUTHORITY=NONE
TARGET_WORKFLOW_MUTATION_AUTHORITY=NONE
V2_ALLOWANCE_REOPEN_AUTHORITY=NONE
V3_ALLOWANCE_REOPEN_AUTHORITY=NONE
DIAGNOSTIC_EVIDENCE_RETENTION=GITHUB_ACTIONS_JOB_LOGS_ONLY
ARTIFACT_UPLOAD_AUTHORITY=NONE
CACHE_UPLOAD_AUTHORITY=NONE
CREDENTIAL_USE_AUTHORITY=NONE
PRIVATE_SECRET_ACCESS_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The path-scoped push trigger is authorized only as the one-shot execution mechanism for the future V4 diagnostic implementation because the currently connected executor exposes no native fresh `workflow_dispatch` creator. The reviewed implementation merge itself may trigger the single authorized V4 run. A later push, rerun, alternate trigger, or second V4 execution is not authorized by this record.

## 5. Authorized diagnostic evidence surface

The future V4 diagnostic may use only public, ungated network access needed to inspect the exact candidate metadata relevant to the historical Phase A `torch==2.11.0+cpu` requirement. It must use the runner's already-present Python/pip environment and the language standard library plus pip-vendored packaging utilities where useful; it may not install new repository or system dependencies.

The maximum authorized evidence surface is:

1. record exact runner, Python, pip, and compatible wheel-tag identities in job logs;
2. bind the exact historical target workflow identity, exact `torch==2.11.0+cpu` requirement, primary index, extra index, and CONNECT allowlist as diagnostic inputs;
3. retrieve bounded public **index metadata only** for both:
   - `https://pypi.org/simple/torch/`;
   - `https://download.pytorch.org/whl/cpu/torch/`;
4. parse exact-version candidate links from both index metadata responses and classify wheel compatibility against the live runner's pip-compatible tag set;
5. log deterministic candidate-set counts, sanitized routes/hosts, compatibility disposition, and index metadata content identities/hashes;
6. reproduce the historical CONNECT allowlist decision against each exact compatible candidate route discovered from either configured index;
7. derive a combined candidate-set disposition from the two directly observed configured index candidate sets without downloading distribution/package artifact bodies;
8. if implementation requires pip-native candidate-ordering or package-finder semantics to distinguish a remaining ambiguity, it may use only an independently reviewed metadata-only mechanism that proves no distribution/package artifact body is read or written;
9. emit a deterministic summary separating direct observations from any conclusion.

The diagnostic must not use `pip download`, `pip install`, build isolation, wheel installation, source distribution extraction, or any equivalent mechanism that downloads a dependency artifact body. HEAD requests to exact discovered public candidate URLs are permitted only when the reviewed implementation demonstrates they do not read response bodies and they are necessary to establish route identity or reachability.

## 6. Required conclusion discipline

The V4 run may resolve the primary-index and combined-candidate questions only from direct retained evidence.

A bounded static target-workflow route defect may become a **candidate conclusion for a later reconciliation**, not an immediate authority effect, only if the V4 logs directly establish all of the following for the exact V4 runtime subject:

1. the primary PyPI index has no compatible candidate satisfying exact `torch==2.11.0+cpu`, or every such compatible candidate route is independently shown to be unusable under the exact historical CONNECT policy;
2. the extra PyTorch CPU index candidate set is directly re-observed in the same run rather than inferred solely from V3;
3. the combined directly observed compatible candidate set contains no route that satisfies the exact historical CONNECT allowlist/configuration;
4. the evidence mechanism itself did not download a package artifact body or execute the target workflow.

If any one of those conditions is not proven, the run must preserve:

```text
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=NEEDS_EVIDENCE
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=NEEDS_EVIDENCE
STATIC_WORKFLOW_DEFECT_PROVEN=NO
```

Even if all four conditions are proven, V4 must still preserve the historical causal boundary until separately reconciled:

```text
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

The V4 workflow itself must emit only observation-oriented fields plus `NEEDS_RECONCILIATION` for any static-defect conclusion. It may not self-authorize repair.

## 7. Explicit exclusions

```text
TARGET_RUNTIME_EVIDENCE_WORKFLOW_DISPATCH=PROHIBITED
TARGET_RUNTIME_EVIDENCE_WORKFLOW_EXECUTION=PROHIBITED
TARGET_WORKFLOW_REPAIR=PROHIBITED
TARGET_WORKFLOW_MUTATION=PROHIBITED
V2_BOOTSTRAP_RERUN=PROHIBITED
V2_TARGET_RERUN=PROHIBITED
V3_DIAGNOSTIC_RERUN=PROHIBITED
FAILED_HISTORICAL_TARGET_JOB_RERUN=PROHIBITED
PIP_DOWNLOAD=PROHIBITED
PIP_INSTALL=PROHIBITED
DEPENDENCY_ARTIFACT_BODY_DOWNLOAD=PROHIBITED
DEPENDENCY_INSTALLATION=PROHIBITED
MODEL_SOURCE_WEIGHT_ACQUISITION=PROHIBITED
MODEL_WEIGHT_LOADING=PROHIBITED
MODEL_CONVERSION=PROHIBITED
MODEL_WEIGHT_QUANTIZATION=PROHIBITED
MODEL_INFERENCE=PROHIBITED
BENCHMARK_PAYLOAD_ACCESS=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS=PROHIBITED
CONTAMINATION_ASSESSMENT_EXECUTION=PROHIBITED
SELECTION_SUITE_CONSTRUCTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING=PROHIBITED
PRIVATE_GOLD_OR_PHI_ACCESS=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
EXTERNAL_REVIEWER_OUTREACH=PROHIBITED
PROVIDER_GENERATION=PROHIBITED
CREDENTIAL_USE=PROHIBITED
PRIVATE_SECRET_ACCESS=PROHIBITED
ARTIFACT_UPLOAD=PROHIBITED
CACHE_UPLOAD=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
PAID_OR_LARGER_RUNNER=PROHIBITED
AUTOMATIC_RETRY=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 8. Repository mutation boundary

This authority record permits no executable repository mutation by itself.

After this record becomes canonical, a separate implementation PR may add only the smallest V4 diagnostic workflow necessary to execute Section 5. That implementation must be independently reviewed at its exact final head before canonical merge.

The V4 runtime itself may not mutate repository contents, refs, branches, releases, issues, pull requests, target workflows, or any other repository object.

```text
REPOSITORY_CONTENT_MUTATION_BY_V4_RUNTIME=PROHIBITED
REF_MUTATION_BY_V4_RUNTIME=PROHIBITED
TARGET_WORKFLOW_MUTATION_BY_V4=PROHIBITED
HISTORY_REWRITE=PROHIBITED
FORCE_PUSH=PROHIBITED
```

## 9. Required lifecycle

```text
V4_AUTHORITY_RECORD_EXACT_HEAD_REVIEW_AND_CANONICAL_MERGE
-> MINIMAL_V4_DIAGNOSTIC_WORKFLOW_IMPLEMENTATION_FROM_THEN_CURRENT_MAIN
-> FRESH_EXACT_HEAD_INDEPENDENT_REPOSITORY_REVIEW
-> GUARDED_CANONICAL_MERGE
-> EXACTLY_ONE_V4_DIAGNOSTIC_EXECUTION
-> RETAINED_PRIMARY_AND_EXTRA_INDEX_METADATA_EVIDENCE_CAPTURE
-> CANONICAL_V4_RESULT_RECONCILIATION
```

Only after the V4 result reconciliation is independently reviewed and canonically merged may a later authority candidate be considered. If the evidence proves a specific repairable target-workflow defect, that later candidate may be a narrowly scoped repair/new-runtime-attempt authority. If the evidence remains incomplete, the project stays fail-closed and no repair authority exists.

## 10. State while this authority record is under review

```text
V4_AUTHORITY_RECORD_STATE=CANDIDATE_UNTIL_CANONICAL_MERGE
FOLLOW_ON_DIAGNOSTIC_AUTHORITY=NONE
V4_IMPLEMENTATION_AUTHORITY=NONE
V4_EXECUTION_AUTHORITY=NONE
TARGET_WORKFLOW_REPAIR_AUTHORITY=NONE
NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPT_AUTHORITY=NONE
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=NEEDS_EVIDENCE
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=NEEDS_EVIDENCE
STATIC_WORKFLOW_DEFECT_PROVEN=NO_NEEDS_PRIMARY_INDEX_EVIDENCE
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
COMPONENT_E004=INCOMPLETE
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
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

## 11. Canonical-merge effect

If and only if this exact authority record passes fresh exact-head independent review with `MATERIAL_BLOCKER=NO` and is guarded-merged canonically, it authorizes creation and qualification of the separate minimal V4 diagnostic workflow implementation described above. It does not authorize execution before that implementation itself passes fresh exact-head independent review and is guarded-merged.

The reviewed implementation merge may consume the exactly-one V4 execution allowance through the path-scoped push trigger. No other execution path is authorized.

## 12. Required review gate

Before canonical merge, an independent reviewer must verify at least:

- the authority depends on canonical V3 reconciliation merge `04eb2bea5a1d825f5599f49224475e4d2ab084a8`;
- V3 execution allowance remains consumed and is not reopened;
- the only unresolved evidence targeted is primary-PyPI/combined-candidate metadata for exact `torch==2.11.0+cpu` under the frozen historical index configuration;
- metadata/index inspection does not permit dependency artifact-body download;
- no `pip download`, `pip install`, target-workflow dispatch, repair, rerun, model, conversion, inference, benchmark, contamination, A15, training, credential, artifact/cache, or spend authority is created;
- exactly one public `ubuntu-24.04` diagnostic execution is the maximum future allowance after the separate implementation review/merge gate;
- the workflow cannot self-declare repair authority or historical causality;
- all fail-closed states remain explicit.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```

No implementation file may be added and no V4 diagnostic run may occur before guarded canonical merge of this exact reviewed authority record.