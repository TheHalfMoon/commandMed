# E004 Connected-Executor Dispatch Remediation V2 Authority — 2026-08-31

**Spec:** 007 SFT V1  
**Decision owner:** Founder  
**Artifact class:** bounded execution-transport remediation authority  
**Canonical base:** `07b7441b7dace693697136fea9331a6be95e3b53`  
**Prior component frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v9-2026-08-31.md`  
**Authority effect before canonical merge:** NONE  
**Target runtime-evidence run allowance effect:** NONE — remains exactly one unconsumed target run  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation authority:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Authorize one new, independently reviewed, fail-closed connected-executor transport remediation attempt for the already-authorized E004 conversion-runtime evidence target workflow after a material live-condition change: the repository is now public.

This is a new post-V9 Founder decision. It does not reinterpret the consumed V1 bootstrap allowance, does not rerun failed run `33256775421`, and does not convert the still-unconsumed target runtime-evidence allowance into broader execution authority.

## 2. Founder directive and ordering

After canonical V9 was reverified at `07b7441b7dace693697136fea9331a6be95e3b53`, with no open PRs, Actions total `98`, newest run `33256775421` still failed, target runtime-evidence `workflow_dispatch` count still `0`, and the connected executor still lacking a native fresh-dispatch creator, the Founder issued:

```text
FOUNDER_DIRECTIVE=go ahead do not stop until finish the project , you have all approvals fro me
FOUNDER_DIRECTIVE_SHA256=1b7c31a818ea7b50d0fe1e12b159d328afa11a9b0d74359cca19951e9fd75eab
FOUNDER_DIRECTIVE_DATE=2026-08-31
FOUNDER_DIRECTIVE_ORDERING=AFTER_V9_CANONICAL_AND_FRESH_LIVE_REVERIFICATION
```

The directive is interpreted narrowly at the current dependency frontier. It authorizes the smallest new authority required to remediate the transport blocker. It does not waive scientific, provenance, quarantine, contamination, resource, access, finance, A15, selection, or training gates.

## 3. Live-condition change that permits a new remediation decision

The prior V1 bootstrap failed terminally while the exact platform-level failure reason remained `NEEDS_EVIDENCE`. That historical result remains immutable.

Current live repository metadata now reports:

```text
LIVE_REPOSITORY_VISIBILITY=public
LIVE_REPOSITORY_ARCHIVED=false
```

V7 already established that public visibility supersedes the former private-repository standard-runner finance blocker for the exact standard public GitHub-hosted `ubuntu-24.04` lane while visibility and runner class remain unchanged.

This changed external condition is sufficient to justify a separately authorized remediation attempt. It does not prove the historical failure cause and must not be represented as doing so.

```text
V1_BOOTSTRAP_FAILURE_CAUSE_RECLASSIFIED=NO
V1_BOOTSTRAP_RERUN_AUTHORIZED=NO
V1_FAILED_JOB_RERUN_AUTHORIZED=NO
V1_ALLOWANCE_REOPENED=NO
NEW_V2_REMEDIATION_AUTHORITY_IS_SEPARATE=YES
```

## 4. Bounded V2 remediation authority

After this record is canonically merged and only after a fresh implementation candidate is independently reviewed and canonically admitted, the project may execute exactly one new transport-remediation workflow run with the following bounds:

```text
E004_CONNECTED_EXECUTOR_DISPATCH_REMEDIATION_V2_AUTHORITY=AUTHORIZED_BOUNDED
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
MAX_AUTHORIZED_V2_REMEDIATION_RUNS=1
V2_TRIGGER=push_to_main_path_scoped_to_v2_bootstrap_file
MAX_AUTHORIZED_TARGET_DISPATCHES_CREATED_BY_V2=1
TARGET_WORKFLOW=.github/workflows/e004-conversion-runtime-evidence.yml
TARGET_REQUIRED_GIT_BLOB_SHA1=591317f1f570480b9ac68e7956d070db8ed5ef45
TARGET_REQUIRED_RAW_SHA256=95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327
TARGET_TRIGGER=workflow_dispatch_only
TARGET_RUNTIME_EVIDENCE_RUN_ALLOWANCE_REMAINS=1
CURRENT_AUTHORIZED_SPEND_USD=0
```

The target runtime-evidence workflow itself must remain byte-identical to the existing captured identity. V2 is transport-only.

## 5. Required V2 implementation improvements

The V2 candidate must preserve every V1 identity and cardinality check and add explicit fail-closed handling for current GitHub dispatch semantics.

At minimum it must:

1. require live repository visibility `public` before any ref creation or target dispatch;
2. require the target workflow at then-current canonical `main` to match Git blob `591317f1f570480b9ac68e7956d070db8ed5ef45` and raw SHA-256 `95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327` where the implementation can verify both identities without reconstructing bytes;
3. require zero prior target `workflow_dispatch` runs before dispatch;
4. create at most one transient SHA-named binding branch initially resolving exactly to the verified canonical `main` SHA;
5. re-read the target workflow through that binding ref and require exact identity equality;
6. re-read the binding ref immediately before dispatch and require exact SHA equality;
7. request workflow-dispatch run details explicitly using the current documented dispatch request semantics rather than relying on an implicit response mode;
8. require the returned target run ID, URL, `head_sha`, `head_branch`, event, and workflow path to match the verified dispatch subject;
9. require post-dispatch target `workflow_dispatch` cardinality to equal exactly one and that one run to equal the returned run ID;
10. emit transport evidence to job logs only;
11. perform no model, benchmark, conversion, contamination, A15, device-qualification, training, provider-generation, credential, artifact-upload, cache-upload, procurement, payment, or spend action.

No implementation detail in this record is executable by itself. Exact candidate bytes require fresh review and canonical admission before the one V2 run is allowed.

## 6. Token and repository mutation boundary

The V2 workflow may use only the ephemeral repository `GITHUB_TOKEN` with the minimum permissions required for:

- reading repository/workflow/run/ref metadata;
- creating exactly one transient SHA-named binding ref;
- creating exactly one target workflow dispatch;
- deleting that transient binding ref only during later reviewed cleanup after the target run reaches a terminal state.

The V2 workflow may not mutate repository file contents.

```text
PERSISTENT_CREDENTIAL_STORAGE=PROHIBITED
REPOSITORY_FILE_CONTENT_MUTATION_BY_V2=PROHIBITED
TARGET_WORKFLOW_MUTATION_BY_V2=PROHIBITED
OTHER_WORKFLOW_MUTATION_BY_V2=PROHIBITED
HISTORY_REWRITE=PROHIBITED
FORCE_PUSH=PROHIBITED
```

## 7. Explicit exclusions

```text
MODEL_SOURCE_WEIGHT_ACQUISITION=PROHIBITED_BY_V2
MODEL_WEIGHT_LOADING=PROHIBITED_BY_V2
MODEL_CONVERSION=PROHIBITED_BY_V2
MODEL_WEIGHT_QUANTIZATION=PROHIBITED_BY_V2
MODEL_INFERENCE=PROHIBITED_BY_V2
BENCHMARK_PAYLOAD_ACCESS=PROHIBITED_BY_V2
BENCHMARK_EXECUTION=PROHIBITED_BY_V2
DEVICE_QUALIFICATION=PROHIBITED_BY_V2
CONTAMINATION_ASSESSMENT=PROHIBITED_BY_V2
SELECTION_SUITE_CONSTRUCTION=PROHIBITED_BY_V2
A15_ACTIVATION=PROHIBITED_BY_V2
PRIVATE_GOLD_OR_PHI_ACCESS=PROHIBITED_BY_V2
GATED_ASSET_ACCESS=PROHIBITED_BY_V2
EXTERNAL_REVIEWER_OUTREACH=PROHIBITED_BY_V2
PROVIDER_GENERATION=PROHIBITED_BY_V2
TRAINING=PROHIBITED_BY_V2
PROCUREMENT=PROHIBITED_BY_V2
PAYMENT=PROHIBITED_BY_V2
PAID_OR_LARGER_RUNNER=PROHIBITED_BY_V2
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 8. Scientific and E004 effect

Canonical merge of this record changes only the connected-executor transport authority.

It does not satisfy runtime evidence or any downstream preflight gate:

```text
COMPONENT_REAL_GUARD_EVIDENCE=ABSENT
COMPONENT_RUNTIME_EVIDENCE=NOT_STARTED
COMPONENT_CONVERSION_PREREQUISITES=INCOMPLETE
COMPONENT_CONTAMINATION_PREREQUISITES=INCOMPLETE
COMPONENT_RESOURCE_ACCESS_BINDINGS=INCOMPLETE
COMPONENT_A1_A14_EQUIVALENT_EXACT_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
```

If the V2 transport run fails before creating the exact authorized target dispatch, the V2 remediation allowance is consumed and E004 remains blocked. No automatic V3, rerun, failed-job rerun, or alternate trigger is authorized by this record.

If V2 successfully creates the exact target dispatch, only that returned target run may consume the existing target runtime-evidence allowance. Its terminal evidence must be reconciled before any further authority change.

## 9. Required lifecycle

```text
THIS_FOUNDER_AUTHORITY_RECORD_REVIEW_AND_CANONICAL_MERGE
-> FRESH_V2_BOOTSTRAP_IMPLEMENTATION_FROM_THEN_CURRENT_MAIN
-> FRESH_EXACT_HEAD_INDEPENDENT_REPOSITORY_REVIEW
-> GUARDED_CANONICAL_MERGE
-> EXACTLY_ONE_V2_BOOTSTRAP_RUN
-> EXACT_TARGET_DISPATCH_OR_FAIL_CLOSED
-> TERMINAL_TARGET_RUN_EVIDENCE_RECONCILIATION_OR_TRANSPORT_FAILURE_RECONCILIATION
```

No step may be skipped because the Founder granted continuation approval.

## 10. Exit evidence

This authority record is ready for canonical merge only if fresh exact-head independent repository review confirms:

```text
FOUNDER_DIRECTIVE_BOUND_AFTER_V9=YES
V1_FAILURE_HISTORY_PRESERVED=YES
V1_BOOTSTRAP_ALLOWANCE_REOPENED=NO
PUBLIC_VISIBILITY_RECHECK_BOUND=YES
V2_AUTHORITY_SEPARATE_AND_ONE_SHOT=YES
TARGET_RUNTIME_EVIDENCE_ALLOWANCE_REMAINS_ONE=YES
TARGET_WORKFLOW_IDENTITY_UNCHANGED=YES
TARGET_TRIGGER_REMAINS_WORKFLOW_DISPATCH_ONLY=YES
NO_RUNTIME_EVIDENCE_FABRICATED=YES
NO_MODEL_CONVERSION_AUTHORITY_CREATED=YES
NO_CONTAMINATION_AUTHORITY_CREATED=YES
NO_A15_AUTHORITY_CREATED=YES
NO_TRAINING_AUTHORITY_CREATED=YES
NO_SPEND_AUTHORITY_CREATED=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
E005_REMAINS_NOT_REACHED=YES
MATERIAL_BLOCKER=NO
```
