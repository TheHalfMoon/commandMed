# E004 Target Route Repair and One Runtime-Attempt Authority — 2026-08-31

**Spec:** 007 SFT V1  
**Decision owner:** Founder  
**Artifact class:** bounded target-repair plus one-shot runtime-evidence authority  
**Canonical base:** `e7f3bf2e3dee155db35171324d177a6cda91bcef`  
**Canonical V4 result reconciliation:** `specs/007-sft-v1/e004-primary-index-resolution-diagnostic-v4-result-reconciliation-2026-08-31.md`  
**Canonical V4 result reconciliation merge:** `e7f3bf2e3dee155db35171324d177a6cda91bcef`  
**Authority effect before canonical merge:** NONE  
**Model conversion authority:** NONE  
**Model execution authority:** NONE  
**Benchmark authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation authority:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Authorize the smallest evidence-backed repair of the E004 conversion-runtime evidence workflow after canonical V4 evidence proved a static Phase A route-policy exclusion for the exact V4 runtime/config subject, and authorize at most one new zero-spend target runtime-evidence attempt after that repair is independently qualified and canonically merged.

The proven static defect is narrow:

```text
STATIC_WORKFLOW_DEFECT_PROVEN=YES_EXACT_V4_RUNTIME_CONFIG_ROUTE_POLICY_EXCLUSION
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=OBSERVED_EMPTY
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=OBSERVED_NO_ALLOWLISTED_COMPATIBLE_ROUTE
V4_REQUIRED_COMPATIBLE_ROUTE_HOST=download-r2.pytorch.org
V4_REQUIRED_COMPATIBLE_ROUTE_PORT=443
V4_REQUIRED_COMPATIBLE_ROUTE_ALLOWLIST_RESULT=DENY
```

The historical causal boundary remains unresolved and MUST remain so:

```text
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
HISTORICAL_STDERR_RECOVERED=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

This authority does not reinterpret historical job `99409197359`. It authorizes a prospective repair because the current static configuration defect is independently proven, not because the exact historical failure line is known.

## 2. Founder directive and narrow interpretation

After canonical V4 result reconciliation was merged and live repository truth was reverified, the Founder directed:

```text
FOUNDER_DIRECTIVE=go ahead do not stop until finish the project , you have all approvals fro me . DO NOT STOP
FOUNDER_DIRECTIVE_SHA256=7037b7f98e65b324fd478d65c88d49c34483ff37a1a5eb9f380987df0b22d82a
FOUNDER_DIRECTIVE_DATE=2026-08-31
FOUNDER_DIRECTIVE_ORDERING=AFTER_CANONICAL_V4_RESULT_RECONCILIATION
```

The directive is interpreted narrowly at the current dependency frontier. It authorizes only the bounded repair/runtime-evidence decision class defined by this record. It does not waive independent review, exact identity, fail-closed execution, evidence reconciliation, model/weight, contamination, A15, training, credential, or spend gates.

## 3. Preserved historical and one-shot state

```text
V2_BOOTSTRAP_RUN=33366850471
V2_BOOTSTRAP_RESULT=PASS
V2_REMEDIATION_ALLOWANCE_REMAINING=0
V2_REMEDIATION_ALLOWANCE_REOPENED=NO

HISTORICAL_TARGET_RUN_ID=33366859146
HISTORICAL_TARGET_JOB_ID=99409197359
HISTORICAL_TARGET_HEAD_SHA=ef1be50f4a076d9f03abfffee342d2c244b0d199
HISTORICAL_TARGET_EVENT=workflow_dispatch
HISTORICAL_TARGET_RUN_ATTEMPT=1
HISTORICAL_TARGET_CONCLUSION=failure
HISTORICAL_TARGET_RUNTIME_EVIDENCE_ALLOWANCE_REMAINING=0
FAILED_HISTORICAL_TARGET_JOB_RERUN_AUTHORITY=NONE

V3_DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
V4_DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
V2_ALLOWANCE_REOPEN_AUTHORITY=NONE
V3_ALLOWANCE_REOPEN_AUTHORITY=NONE
V4_ALLOWANCE_REOPEN_AUTHORITY=NONE
```

No previous run, job, bootstrap, diagnostic, or allowance is reopened by this authority.

## 4. Exact historical target identity and prior authority boundary

The repair subject is exactly:

```text
TARGET_WORKFLOW_PATH=.github/workflows/e004-conversion-runtime-evidence.yml
HISTORICAL_TARGET_WORKFLOW_HEAD=ef1be50f4a076d9f03abfffee342d2c244b0d199
HISTORICAL_TARGET_WORKFLOW_GIT_BLOB_SHA1=591317f1f570480b9ac68e7956d070db8ed5ef45
HISTORICAL_TARGET_WORKFLOW_RAW_SHA256=95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327
TARGET_TRIGGER=workflow_dispatch_ONLY
TARGET_RUNNER=ubuntu-24.04
TARGET_WORKFLOW_PERMISSIONS={}
```

The target's original Founder authority remains the scientific execution boundary. The prospective repaired workflow may still perform only the previously authorized runtime-evidence operations:

```text
ACQUIRE_EXACT_LLAMA_CPP_SOURCE=YES
VERIFY_TOOL_COMMIT_AND_TREE=YES
VERIFY_CANONICAL_DEPENDENCY_MANIFEST_GIT_BLOBS=YES
RESOLVE_CONVERTER_PYTHON_DEPENDENCIES=YES
DOWNLOAD_RESOLVED_DEPENDENCY_ARTIFACTS_TO_EPHEMERAL_STAGING=YES
HASH_EVERY_RESOLVED_DEPENDENCY_ARTIFACT_BEFORE_INSTALL=YES
CAPTURE_RESOLVER_IDENTITY_AND_VERSION=YES
CREATE_EPHEMERAL_ISOLATED_PYTHON_ENVIRONMENT=YES
INSTALL_ONLY_FROM_LOCALLY_STAGED_HASHED_DEPENDENCY_ARTIFACTS=YES
BUILD_LLAMA_QUANTIZE_FROM_EXACT_AUTHORIZED_TOOL_SOURCE=YES
HASH_REBUILT_LLAMA_QUANTIZE=YES
IMPORT_LOCAL_GGUF_FOR_PATH_AND_SOURCE_ATTESTATION=YES
IMPORT_CONVERTER_MODEL_OR_ARCHITECTURE_MODULES=NO
LOAD_MODEL_WEIGHTS=NO
CAPTURE_EXACT_RUNTIME_AND_BUILD_MANIFESTS=YES
CAPTURE_EXACT_COMMAND_ARGV=YES
EMIT_EVIDENCE_TO_JOB_LOGS_ONLY=YES
```

This authority does not add any new scientific operation beyond that previously bounded runtime-evidence lane.

## 5. Exact repair authority

After this authority is independently reviewed at exact final head with `MATERIAL_BLOCKER=NO` and guarded-merged canonically, one repair implementation PR may modify exactly one repository path:

```text
.github/workflows/e004-conversion-runtime-evidence.yml
```

The only semantic mutation authorized in that target workflow is:

```text
TARGET_WORKFLOW_REPAIR_SCOPE=PHASE_A_CONNECT_ALLOWLIST_ONLY
AUTHORIZED_HOST_ADDITION=download-r2.pytorch.org
AUTHORIZED_SCHEME=https
AUTHORIZED_PORT=443
PRESERVE_EXISTING_ALLOWLIST=YES
PRESERVE_DENY_BY_DEFAULT=YES
OTHER_TARGET_WORKFLOW_LOGIC_MUTATION=PROHIBITED
```

Concretely, the repair may add exact host `download-r2.pytorch.org` to the Phase A Python CONNECT-proxy `ALLOWED` host set and make no other executable change.

The repair MUST preserve all of the following unchanged except for unavoidable content identities caused solely by that one host addition:

- `workflow_dispatch` as the only target trigger;
- `permissions: {}`;
- `ubuntu-24.04` runner class;
- workflow concurrency behavior;
- exact llama.cpp repository, commit, tree, and source-manifest checks;
- exact package requirements and configured indexes;
- Phase A credential clearing and local CONNECT proxy design;
- Phase B default-deny network isolation;
- local `gguf-py` attestation;
- no model weight access/load/conversion/inference;
- no benchmark, contamination, A15, training, upload, credential, paid-runner, procurement, payment, or spend action;
- evidence persistence to job logs only.

No formatting-only, cleanup, timeout, dependency, command, trigger, permissions, runner, or unrelated workflow mutation is authorized in the same repair PR.

## 6. Repair qualification and identity capture

The repair implementation must proceed as:

```text
CANONICAL_REPAIR_AUTHORITY
-> FRESH_REPAIR_BRANCH_FROM_EXACT_AUTHORITY_MAIN
-> ONE_PATH_ONE_SEMANTIC_CHANGE_TARGET_REPAIR
-> FRESH_EXACT_HEAD_INDEPENDENT_REVIEW
-> MATERIAL_BLOCKER=NO
-> GUARDED_CANONICAL_MERGE
-> POST_MERGE_TARGET_CONTENT_IDENTITY_CAPTURE
```

Before any dispatch transport implementation may be created, the project must capture and retain from canonical `main`:

```text
REPAIRED_TARGET_CANONICAL_MERGE_SHA=<exact repair merge SHA>
REPAIRED_TARGET_GIT_BLOB_SHA1=<exact target blob after repair>
REPAIRED_TARGET_RAW_SHA256=<exact target raw bytes after repair>
```

Any later mutation of the target workflow invalidates those identities and blocks the new runtime attempt until separately reauthorized.

## 7. Connected execution constraint

At authority-drafting time, the connected GitHub surface available to the project exposes no native fresh `workflow_dispatch` creator.

Therefore this authority does not pretend that a direct dispatch tool exists. It permits one separately reviewed one-shot transport bootstrap only after the repaired target is canonical and identity-captured.

The bootstrap must be a new repository path, not a reuse or rerun of V1/V2:

```text
NEW_TRANSPORT_BOOTSTRAP_PATH=.github/workflows/e004-target-runtime-repair-dispatch-v1.yml
NEW_TRANSPORT_BOOTSTRAP_TRIGGER=push_to_main_path_scoped_to_exact_bootstrap_file
NEW_TRANSPORT_BOOTSTRAP_RUNNER=ubuntu-24.04
MAX_AUTHORIZED_NEW_TRANSPORT_BOOTSTRAP_RUNS=1
MAX_AUTHORIZED_NEW_TARGET_DISPATCHES=1
```

The bootstrap implementation is not authorized until Section 6 is complete and must itself pass fresh exact-head independent review with `MATERIAL_BLOCKER=NO` before guarded canonical merge.

If a native connected `workflow_dispatch` creator becomes available before bootstrap implementation begins, the bootstrap MUST NOT be created merely out of habit. The project must use the smaller direct-dispatch mechanism only if it can enforce the same exact repaired-target identity and one-shot cardinality without broadening authority; otherwise it must fail closed and reconcile the transport blocker.

## 8. One-shot transport bootstrap boundary

If the bootstrap path is required, it may use only the ephemeral repository `GITHUB_TOKEN` with minimum permissions necessary to:

- read repository/workflow/run/ref metadata;
- create exactly one new transient binding branch resolving exactly to the repaired target canonical merge SHA;
- create exactly one `workflow_dispatch` for the repaired target workflow at that exact binding ref;
- verify the returned target run identity/cardinality.

The bootstrap may not mutate repository file contents or any workflow bytes.

The transient binding branch must be new and must not reuse the historical V2 binding branch:

```text
HISTORICAL_V2_BINDING_REF_REUSE=PROHIBITED
NEW_BINDING_REF_PREFIX=e004-runtime-evidence-route-repair-bind-
NEW_BINDING_REF_INITIAL_SHA=REPAIRED_TARGET_CANONICAL_MERGE_SHA
MAX_NEW_BINDING_REFS_CREATED=1
```

Before dispatch, the bootstrap must prove:

1. live repository visibility is `public`;
2. the repaired target workflow at canonical `main` matches the exact captured repaired Git blob and raw SHA-256 identities;
3. the new binding ref resolves exactly to the repaired target canonical merge SHA;
4. the target workflow reread through that binding ref has the same exact repaired identities;
5. the historical target run `33366859146` remains the sole pre-existing target `workflow_dispatch` run and is unchanged;
6. no new repaired-target run has already been created;
7. the bootstrap is executing for the first attempt of its one allowed merge-triggered run.

After dispatch, the bootstrap must prove:

1. exactly one new target `workflow_dispatch` run was created;
2. its returned run ID is different from historical run `33366859146`;
3. its `head_sha` equals `REPAIRED_TARGET_CANONICAL_MERGE_SHA`;
4. its `head_branch` equals the exact new binding ref;
5. its event is `workflow_dispatch`;
6. its workflow path is `.github/workflows/e004-conversion-runtime-evidence.yml`;
7. target `workflow_dispatch` cardinality increased from exactly one historical run to exactly two total runs, with the second being the returned repaired-target run.

Transport evidence is job-log-only. No automatic bootstrap retry is authorized.

## 9. New target runtime-evidence attempt authority

This record creates a new allowance only if and after all prior lifecycle gates in Sections 5–8 are satisfied:

```text
NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPT_AUTHORITY=AUTHORIZED_EXACTLY_ONE_AFTER_REPAIR_QUALIFICATION
TARGET_RUNTIME_EVIDENCE_MAX_NEW_ATTEMPTS=1
TARGET_RUNTIME_EVIDENCE_RUNNER=ubuntu-24.04
TARGET_RUNTIME_EVIDENCE_TRIGGER=workflow_dispatch_ONLY
TARGET_RUNTIME_EVIDENCE_SPEND_USD=0
AUTOMATIC_TARGET_RETRY=PROHIBITED
FAILED_TARGET_JOB_RERUN=PROHIBITED
SECOND_NEW_TARGET_ATTEMPT=PROHIBITED
```

The allowance is consumed when the one new target run is created, regardless of success or failure or how early it terminates.

If the new run fails, no rerun, failed-job rerun, V5 diagnostic, alternate trigger, repair widening, or second attempt is implicitly authorized. Its terminal evidence must be reconciled canonically first.

## 10. Phase A network delta and unchanged network boundaries

The prospective repaired Phase A allowlist becomes exactly:

```text
github.com
pypi.org
files.pythonhosted.org
download.pytorch.org
download-r2.pytorch.org
```

and port `443` remains mandatory.

No other host, package index, mirror, model endpoint, provider endpoint, telemetry endpoint, or credentialed route is authorized.

After Phase A staging completes, Phase B remains default-deny network isolation exactly as in the previously authorized target workflow.

## 11. Explicit scientific and operational exclusions

```text
MODEL_SOURCE_WEIGHT_ACQUISITION=PROHIBITED
MODEL_WEIGHT_LOADING=PROHIBITED
MODEL_CONVERSION=PROHIBITED
MODEL_WEIGHT_QUANTIZATION=PROHIBITED
MODEL_INFERENCE=PROHIBITED
TOKEN_GENERATION=PROHIBITED
BENCHMARK_PAYLOAD_ACCESS=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
DEVICE_QUALIFICATION=PROHIBITED
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS=PROHIBITED
CONTAMINATION_ASSESSMENT_EXECUTION=PROHIBITED
SELECTION_SUITE_CONSTRUCTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
PRIVATE_GOLD_OR_PHI_ACCESS=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PROVIDER_GENERATION=PROHIBITED
EXTERNAL_REVIEWER_OUTREACH=PROHIBITED
TRAINING=PROHIBITED
TARGET_WORKFLOW_OTHER_LOGIC_MUTATION=PROHIBITED
REPOSITORY_FILE_CONTENT_MUTATION_BY_RUNTIME=PROHIBITED
ARTIFACT_UPLOAD=PROHIBITED
CACHE_UPLOAD=PROHIBITED
PERSISTENT_CREDENTIAL_STORAGE=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
PAID_OR_LARGER_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

The bootstrap's ephemeral `GITHUB_TOKEN` is transport-only and does not create credential authority for the target workflow. The target workflow itself retains `permissions: {}` and clears token variables before its evidence operations.

## 12. Required lifecycle

```text
THIS_REPAIR_RUNTIME_AUTHORITY_EXACT_HEAD_REVIEW
-> GUARDED_CANONICAL_AUTHORITY_MERGE
-> REREAD_CANONICAL_GOVERNANCE_AND_ACTIVE_SPEC007_AUTHORITY_CHAIN
-> FRESH_TARGET_REPAIR_BRANCH_FROM_EXACT_AUTHORITY_MAIN
-> ADD_ONLY_download-r2.pytorch.org_TO_PHASE_A_CONNECT_ALLOWLIST
-> FRESH_EXACT_HEAD_REPAIR_REVIEW
-> GUARDED_CANONICAL_REPAIR_MERGE
-> CAPTURE_EXACT_REPAIRED_TARGET_IDENTITIES
-> REDISCOVER_CONNECTED_NATIVE_DISPATCH_CAPABILITY
-> IF_NATIVE_EXACT_DISPATCH_AVAILABLE_USE_SMALLEST_AUTHORIZED_PATH_ELSE_CREATE_NEW_ONE_SHOT_BOOTSTRAP
-> IF_BOOTSTRAP_REQUIRED_FRESH_EXACT_HEAD_BOOTSTRAP_REVIEW
-> IF_BOOTSTRAP_REQUIRED_GUARDED_CANONICAL_BOOTSTRAP_MERGE
-> EXACTLY_ONE_NEW_TARGET_workflow_dispatch
-> RETAIN_TERMINAL_TARGET_RUN_AND_JOB_LOG_EVIDENCE
-> CANONICAL_NEW_TARGET_RESULT_RECONCILIATION
```

No later lifecycle stage may be inferred from target-run success alone.

## 13. E004 / E005 effect

Canonical merge of this authority record does not complete E004 and does not advance E005.

Before the new target run:

```text
COMPONENT_RUNTIME_EVIDENCE=FAILED_PHASE_A_HISTORICAL_WITH_STATIC_ROUTE_DEFECT_PROVEN_BY_V4
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=AUTHORIZED_BOUNDED_REPAIR_PENDING_QUALIFICATION
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
```

If the new target run reaches Phase B/final manifest, that result is only one E004 prerequisite evidence unit. Other E004 blockers remain independently fail-closed unless separately proven, including persistent conversion subject/workspace, contamination-assessment authority/evidence, T1/A2 numeric policy plus qualified clinical/statistical review, G1-G4 real governance evidence, resource/access bindings, finance/resource evidence outside the exact bounded runner-minute lane, a real A1-A14 PASS snapshot, and separate A15 activation.

## 14. Required review gate

Before canonical merge, an independent reviewer must verify at least:

- canonical V4 reconciliation merge `e7f3bf2e3dee155db35171324d177a6cda91bcef` exists and proves only the bounded static defect claimed here;
- historical causality remains `NEEDS_EVIDENCE` and no historical deny line is invented;
- V2/V3/V4 allowances remain consumed and are not reopened;
- repair scope is exactly one host addition to the Phase A CONNECT allowlist and no other target executable mutation;
- original conversion-runtime Founder authority boundaries are preserved;
- one new target attempt is created only after exact repaired-target review, canonical merge, identity capture, and exact dispatch transport qualification;
- the absent native connected dispatch creator is handled honestly rather than assumed;
- any bootstrap is new, one-shot, exact-target-bound, and cannot reuse the historical V2 binding ref or allowance;
- no automatic retry, failed-job rerun, second attempt, or alternate trigger is authorized;
- no model, conversion, inference, benchmark, contamination, A15, training, credential expansion, upload, procurement/payment, paid runner, or spend authority is created;
- E004 remains incomplete and E005 remains `NOT_REACHED`.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```

Only guarded canonical merge of the exact reviewed authority head activates the bounded repair/runtime-attempt lifecycle above.
