# E004 Phase A Route Repair / Runtime-Evidence V5 Authority — 2026-08-31

**Spec:** 007 SFT V1  
**Decision owner:** Founder  
**Artifact class:** bounded target-repair and new-runtime-attempt authority  
**Canonical base:** `e7f3bf2e3dee155db35171324d177a6cda91bcef`  
**Canonical V4 result reconciliation:** `specs/007-sft-v1/e004-primary-index-resolution-diagnostic-v4-result-reconciliation-2026-08-31.md`  
**V4 reconciliation merge:** `e7f3bf2e3dee155db35171324d177a6cda91bcef`  
**Authority effect before canonical merge:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Authorize the smallest repair/new-runtime-attempt successor justified by the canonical V4 evidence reconciliation.

V4 directly proved that, for the exact historical target dependency/index/CONNECT configuration evaluated against the exact V4 Ubuntu 24.04 / Python 3.12 runtime subject:

```text
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=OBSERVED_EMPTY
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=OBSERVED_NO_ALLOWLISTED_COMPATIBLE_ROUTE
STATIC_WORKFLOW_DEFECT_PROVEN=YES_EXACT_V4_RUNTIME_CONFIG_ROUTE_POLICY_EXCLUSION
V4_REQUIRED_COMPATIBLE_ROUTE_HOST=download-r2.pytorch.org
V4_REQUIRED_COMPATIBLE_ROUTE_PORT=443
V4_REQUIRED_COMPATIBLE_ROUTE_ALLOWLIST_RESULT=DENY
```

The maximum evidence-backed target repair is therefore exactly one CONNECT allowlist addition:

```text
REPAIR_SCOPE=PHASE_A_CONNECT_ALLOWLIST_ONLY
ADD_HOST=download-r2.pytorch.org
SCHEME=https
PORT=443
PRESERVE_EXISTING_ALLOWLIST=YES
PRESERVE_DENY_BY_DEFAULT=YES
TARGET_WORKFLOW_OTHER_LOGIC_MUTATION=PROHIBITED
```

This authority does not reinterpret the historical failed target job. Historical causality remains unresolved:

```text
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
HISTORICAL_STDERR_RECOVERED=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

## 2. Founder directive and ordering

After the V4 result reconciliation was independently reviewed at exact head `8881f021815d3c1bd541da18e7c1244353898837` with `MATERIAL_BLOCKER=NO` and guarded-merged canonically as `e7f3bf2e3dee155db35171324d177a6cda91bcef`, the Founder directive is:

```text
FOUNDER_DIRECTIVE=go ahead do not stop until finish the project , you have all approvals fro me . DO NOT STOP
FOUNDER_DIRECTIVE_SHA256=7037b7f98e65b324fd478d65c88d49c34483ff37a1a5eb9f380987df0b22d82a
FOUNDER_DIRECTIVE_DATE=2026-08-31
FOUNDER_DIRECTIVE_INTERPRETATION=ORDINARY_AUTHORIZED_WORK_ONLY_SUBJECT_TO_CANONICAL_GATES
```

The directive is interpreted narrowly at the current dependency frontier. It does not waive evidence, provenance, safety, quarantine, review, finance, execution-cardinality, or later lifecycle gates.

## 3. Preserved historical execution state

The prior V2 transport and target execution are complete and consumed:

```text
V2_BOOTSTRAP_RUN=33366850471
V2_BOOTSTRAP_RESULT=PASS
V2_REMEDIATION_ALLOWANCE_REMAINING=0

HISTORICAL_TARGET_RUN_ID=33366859146
HISTORICAL_TARGET_JOB_ID=99409197359
HISTORICAL_TARGET_EVENT=workflow_dispatch
HISTORICAL_TARGET_HEAD_SHA=ef1be50f4a076d9f03abfffee342d2c244b0d199
HISTORICAL_TARGET_RUN_ATTEMPT=1
HISTORICAL_TARGET_CONCLUSION=failure
HISTORICAL_TARGET_RUNTIME_EVIDENCE_ALLOWANCE_REMAINING=0
```

The old allowances are not reopened:

```text
V2_ALLOWANCE_REOPEN_AUTHORITY=NONE
V3_ALLOWANCE_REOPEN_AUTHORITY=NONE
V4_ALLOWANCE_REOPEN_AUTHORITY=NONE
FAILED_HISTORICAL_TARGET_JOB_RERUN_AUTHORITY=NONE
```

The new V5 attempt is a separately authorized attempt justified only by the canonical V4 static-defect evidence and the separately reviewed repair.

## 4. Exact pre-repair target identity

The current canonical target remains byte-identical to the historical target workflow:

```text
TARGET_WORKFLOW=.github/workflows/e004-conversion-runtime-evidence.yml
PRE_REPAIR_TARGET_BLOB_SHA1=591317f1f570480b9ac68e7956d070db8ed5ef45
PRE_REPAIR_TARGET_RAW_SHA256=95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327
PRE_REPAIR_TARGET_HEAD_SHA=ef1be50f4a076d9f03abfffee342d2c244b0d199
TARGET_TRIGGER=workflow_dispatch_only
```

The exact pre-repair allowlist is:

```text
github.com
pypi.org
files.pythonhosted.org
download.pytorch.org
```

## 5. Target repair implementation authority

Only after this authority record is independently reviewed at its exact final head and guarded-merged canonically may one target-repair implementation PR be created from then-current canonical `main`.

That PR may modify exactly one repository path:

```text
.github/workflows/e004-conversion-runtime-evidence.yml
```

The only semantic change authorized in that workflow is:

```python
ALLOWED = {
    "github.com",
    "pypi.org",
    "files.pythonhosted.org",
    "download.pytorch.org",
    "download-r2.pytorch.org",
}
```

Equivalent formatting is acceptable, but no other target behavior may change.

The repair PR MUST preserve byte-for-byte semantic identity of all other target behavior, including at minimum:

- `workflow_dispatch` as the only trigger;
- `permissions: {}`;
- runner label `ubuntu-24.04`;
- timeout;
- tool repository/commit/tree identities;
- dependency requirements and configured indexes;
- Phase A proxy deny-by-default behavior and port `443` restriction;
- source identity checks;
- dependency staging behavior;
- Phase B offline environment behavior;
- local GGUF attestation/rebuild behavior;
- final evidence manifest behavior;
- no model/source-weight acquisition;
- no model conversion or inference;
- no benchmark/device execution;
- no contamination assessment;
- no A15 activation;
- no training;
- no credential use by the target;
- no artifact/cache upload;
- no paid runner or spend.

The repaired target PR must receive fresh independent exact-head review with explicit:

```text
MATERIAL_BLOCKER=NO
```

before guarded canonical merge.

## 6. New target identity requirement

After the reviewed repair is guarded-merged, the exact canonical repair merge SHA and repaired workflow content identities MUST be captured before any transport implementation is created:

```text
V5_TARGET_REPAIR_MERGE_SHA=<exact canonical repair merge SHA>
V5_TARGET_REPAIRED_BLOB_SHA1=<exact Git blob SHA-1>
V5_TARGET_REPAIRED_RAW_SHA256=<exact raw workflow SHA-256>
V5_TARGET_REPAIRED_RAW_BYTES=<exact byte count>
```

No transport implementation may use placeholders for these values in its exact reviewed head.

## 7. New target runtime-evidence attempt authority

After Sections 5–6 are complete, exactly one new zero-spend target runtime-evidence attempt is authorized under the pre-existing E004 scientific boundary:

```text
V5_NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPT_AUTHORITY=AUTHORIZED_BOUNDED
MAX_NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPTS=1
TARGET_WORKFLOW=.github/workflows/e004-conversion-runtime-evidence.yml
TARGET_EVENT=workflow_dispatch
TARGET_RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
TARGET_RUNNER_LABEL=ubuntu-24.04
CURRENT_AUTHORIZED_SPEND_USD=0
AUTOMATIC_RETRY_AUTHORITY=NONE
FAILED_JOB_RERUN_AUTHORITY=NONE
SECOND_V5_TARGET_ATTEMPT_AUTHORITY=NONE
```

This is a new attempt, not a rerun of run `33366859146` and not a reopening of any prior allowance.

## 8. Connected-executor transport authority

The connected executor still exposes no native fresh `workflow_dispatch` creator. Therefore, only after the repaired target is canonically merged and its exact identities are captured, one separately reviewed one-shot transport workflow may be created at a new path:

```text
.github/workflows/e004-runtime-evidence-dispatch-bootstrap-v5.yml
```

The transport may reuse the proven V2 pattern, but it MUST be bound to the new V5 identities and current history rather than reusing V2 state.

Required transport bounds:

```text
TRIGGER=push_to_main_path_scoped_to_exact_v5_bootstrap_file
RUNNER=ubuntu-24.04
MAX_V5_BOOTSTRAP_RUNS=1
MAX_V5_TARGET_DISPATCHES_CREATED=1
MAX_V5_TRANSIENT_BIND_REFS_CREATED=1
V5_BIND_REF_PREFIX=e004-runtime-evidence-v5-bind
TARGET_BIND_SHA=V5_TARGET_REPAIR_MERGE_SHA
TARGET_WORKFLOW_IDENTITY=V5_TARGET_REPAIRED_BLOB_SHA1+V5_TARGET_REPAIRED_RAW_SHA256+V5_TARGET_REPAIRED_RAW_BYTES
AUTHORIZED_SPEND_USD=0
```

The V5 transport may use only the ephemeral repository `GITHUB_TOKEN` with the minimum `actions: write` and `contents: write` permissions required to read public/repository metadata, create exactly one transient binding ref, and create exactly one workflow dispatch. Persistent credential storage is prohibited.

Before creating any ref or dispatch, the transport MUST fail closed unless all of the following are directly reverified:

1. repository is `TheHalfMoon/commandMed`, public, unarchived, default branch `main`;
2. the bootstrap event is `push` to `refs/heads/main`, run attempt `1`;
3. the push predecessor is exactly `V5_TARGET_REPAIR_MERGE_SHA`;
4. the target workflow at `V5_TARGET_REPAIR_MERGE_SHA` matches all captured V5 repaired identities;
5. target workflow metadata reports the expected path and active state;
6. the historical target `workflow_dispatch` history contains exactly the one known prior run `33366859146` before V5 dispatch, with no unknown additional target dispatch run;
7. no V5 target dispatch already exists;
8. the new V5 binding branch name is unique and does not reuse or mutate the V2 binding branch;
9. the new binding ref resolves exactly to `V5_TARGET_REPAIR_MERGE_SHA` before dispatch;
10. re-reading the target workflow through the binding ref reproduces the exact V5 repaired identities immediately before dispatch.

The transport must request one new target `workflow_dispatch` on the new V5 binding ref and then verify:

```text
TARGET_POST_V5_DISPATCH_TOTAL_WORKFLOW_DISPATCH_COUNT=2
HISTORICAL_RUN_33366859146_STILL_PRESENT=YES
NEW_V5_RUN_COUNT=1
NEW_V5_RUN_EVENT=workflow_dispatch
NEW_V5_RUN_HEAD_SHA=V5_TARGET_REPAIR_MERGE_SHA
NEW_V5_RUN_HEAD_BRANCH=<exact V5 binding branch>
NEW_V5_RUN_PATH=.github/workflows/e004-conversion-runtime-evidence.yml
```

The transport itself performs no target scientific work.

## 9. Transport review and merge gate

The V5 bootstrap implementation must be independently reviewed at its exact final head with explicit:

```text
MATERIAL_BLOCKER=NO
```

It may be guarded-merged only while canonical `main` is still exactly `V5_TARGET_REPAIR_MERGE_SHA`, so its path-scoped merge-triggered execution has the exact repaired target as predecessor.

A later matching push, rerun, altered predecessor, alternate trigger, or second bootstrap execution has no authority. The implementation MUST mechanically fail closed on such conditions before ref creation or target dispatch.

## 10. New target run evidence boundary

The one authorized V5 target run executes the same evidence workflow as the historical target except for the one proven CONNECT allowlist repair.

It may perform the already-reviewed target workflow operations needed to establish runtime evidence, including public source/dependency staging and offline environment/rebuild evidence. It may download the same public dependency artifact bodies required by the frozen target workflow. It may not download or load model source weights or execute model conversion/inference.

The target run remains subject to its frozen exclusions:

```text
MODEL_SOURCE_WEIGHT_ACQUISITION=PROHIBITED
MODEL_WEIGHT_LOADING=PROHIBITED
MODEL_CONVERSION=PROHIBITED
MODEL_INFERENCE=PROHIBITED
BENCHMARK_PAYLOAD_ACCESS=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
DEVICE_QUALIFICATION=PROHIBITED
CONTAMINATION_ASSESSMENT=PROHIBITED
SELECTION_SUITE_CONSTRUCTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING=PROHIBITED
PRIVATE_GOLD_OR_PHI_ACCESS=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
EXTERNAL_REVIEWER_OUTREACH=PROHIBITED
PROVIDER_GENERATION=PROHIBITED
CREDENTIAL_USE_BY_TARGET=PROHIBITED
ARTIFACT_UPLOAD=PROHIBITED
CACHE_UPLOAD=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
PAID_OR_LARGER_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 11. Result interpretation discipline

The V5 target run must be reconciled from retained direct evidence regardless of outcome.

If Phase A passes after the one-line repair, that is direct evidence that the repaired target can stage its exact public source/dependency surface under the V5 runtime subject. It does not retroactively prove the exact cause of historical run `33366859146`.

If Phase B and the final runtime evidence manifest pass, those observations may satisfy only the runtime-evidence component they directly prove. They do not automatically satisfy model conversion, contamination, numeric T1/A2 policy, G1–G4 governance, real resource/personnel/access, A1–A14, A15, E004 as a whole, E005, winner selection, or training gates.

If the V5 target run fails at any point, the single V5 attempt is still consumed. No rerun is authorized.

Preserve in every outcome:

```text
HISTORICAL_PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

## 12. Repository mutation boundary

Authorized repository mutation is limited to:

1. this authority record;
2. exactly one reviewed one-line target repair PR;
3. exactly one reviewed V5 bootstrap workflow PR;
4. one transient V5 binding ref created by the reviewed bootstrap runtime.

The V5 bootstrap may not mutate repository file contents, existing refs, releases, issues, pull requests, or workflow files. It must not modify or delete the historical V2 binding branch.

```text
FORCE_PUSH=PROHIBITED
HISTORY_REWRITE=PROHIBITED
TARGET_FILE_MUTATION_BY_BOOTSTRAP=PROHIBITED
OTHER_WORKFLOW_MUTATION_BY_BOOTSTRAP=PROHIBITED
```

## 13. Required lifecycle

```text
V5_AUTHORITY_EXACT_HEAD_REVIEW_AND_CANONICAL_MERGE
-> ONE_LINE_TARGET_REPAIR_FROM_THEN_CURRENT_MAIN
-> TARGET_REPAIR_EXACT_HEAD_REVIEW
-> GUARDED_TARGET_REPAIR_CANONICAL_MERGE
-> CAPTURE_EXACT_REPAIRED_TARGET_IDENTITIES
-> CREATE_V5_ONE_SHOT_TRANSPORT_FROM_EXACT_REPAIR_MAIN
-> V5_TRANSPORT_EXACT_HEAD_REVIEW
-> GUARDED_V5_TRANSPORT_MERGE_WHILE_MAIN_IS_EXACT_REPAIR_MERGE
-> EXACTLY_ONE_V5_BOOTSTRAP_EXECUTION
-> EXACTLY_ONE_NEW_V5_TARGET_WORKFLOW_DISPATCH_OR_FAIL_CLOSED
-> TERMINAL_V5_TARGET_RUN_EVIDENCE_CAPTURE
-> CANONICAL_V5_RESULT_RECONCILIATION
```

No lifecycle edge may be skipped.

## 14. State while this authority record is under review

```text
V5_AUTHORITY_STATE=CANDIDATE_UNTIL_CANONICAL_MERGE
TARGET_WORKFLOW_REPAIR_AUTHORITY=NONE
NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPT_AUTHORITY=NONE
V5_TRANSPORT_IMPLEMENTATION_AUTHORITY=NONE
V5_TRANSPORT_EXECUTION_AUTHORITY=NONE

STATIC_WORKFLOW_DEFECT_PROVEN=YES_EXACT_V4_RUNTIME_CONFIG_ROUTE_POLICY_EXCLUSION
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
COMPONENT_RUNTIME_EVIDENCE=FAILED_PHASE_A_HISTORICAL_WITH_STATIC_ROUTE_DEFECT_PROVEN_BY_V4
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

## 15. Canonical-merge effect

If and only if this exact authority record receives fresh exact-head independent review with `MATERIAL_BLOCKER=NO` and is guarded-merged canonically, it authorizes creation and qualification of the one-line target repair in Section 5.

It does not authorize target repair before its own canonical merge, does not authorize the transport before the repaired target is independently reviewed and canonically merged, and does not authorize target execution before the transport implementation is independently reviewed and guarded-merged under the exact predecessor requirement.

## 16. Required review gate

Before canonical merge, an independent reviewer must verify at least:

- the V4 result reconciliation is canonical at `e7f3bf2e3dee155db35171324d177a6cda91bcef`;
- the static defect conclusion is represented no more broadly than V4 evidence supports;
- historical causality remains unresolved;
- the repair scope is exactly one allowlist host addition and no other target logic change;
- the old V2/target/V3/V4 allowances remain consumed and are not reopened;
- the new V5 target attempt is separately one-shot and zero-spend;
- the transport binds exact repaired target identities and requires exactly one known historical target dispatch before creating exactly one new dispatch;
- the transport uses a distinct binding ref and does not mutate the old V2 binding ref;
- exact-head independent review and guarded merge are required separately for both repair and transport implementations;
- no model/conversion/inference, benchmark, contamination, A15, training, Private Gold/PHI, gated asset, provider generation, persistent credential, artifact/cache, procurement/payment, paid runner, or spend authority is created;
- E004 remains incomplete and E005 remains not reached.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```
