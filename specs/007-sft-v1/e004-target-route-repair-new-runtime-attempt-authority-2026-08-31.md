# E004 Target Route Repair and New Runtime-Evidence Attempt Authority — 2026-08-31

**Spec:** 007 SFT V1  
**Decision owner:** Founder  
**Artifact class:** bounded target-repair and new-runtime-attempt authority  
**Canonical base:** `e7f3bf2e3dee155db35171324d177a6cda91bcef`  
**Canonical evidence basis:** `specs/007-sft-v1/e004-primary-index-resolution-diagnostic-v4-result-reconciliation-2026-08-31.md`  
**Historical target workflow:** `.github/workflows/e004-conversion-runtime-evidence.yml`  
**Historical target workflow blob SHA-1:** `591317f1f570480b9ac68e7956d070db8ed5ef45`  
**Historical target workflow raw SHA-256:** `95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327`  
**Training authority:** NONE  
**Spend authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Authorize the smallest evidence-backed repair of the E004 conversion-runtime evidence target workflow and exactly one new zero-spend target runtime-evidence attempt after the canonical V4 reconciliation proved a static route-policy defect for the exact V4 runtime/config subject.

This authority does not reinterpret the historical failed target run. It does not claim that `download-r2.pytorch.org` was the exact historical deny line or causal mechanism. It authorizes a forward repair because current direct evidence proves that the frozen historical CONNECT policy excludes the sole compatible route observed across the configured primary and extra indexes for `torch==2.11.0+cpu` on the exact V4 runtime subject.

This record grants no model conversion, model inference, benchmark execution, contamination assessment, A15 activation, training, Private Gold/PHI access, gated-asset access, provider generation, paid runner, procurement, payment, or spend authority.

## 2. Founder directive and ordering

After canonical V4 result reconciliation was independently reviewed and guarded-merged as `e7f3bf2e3dee155db35171324d177a6cda91bcef`, the Founder issued:

```text
FOUNDER_DIRECTIVE=go ahead do not stop until finish the project , you have all approvals fro me . DO NOT STOP
FOUNDER_DIRECTIVE_SHA256=7037b7f98e65b324fd478d65c88d49c34483ff37a1a5eb9f380987df0b22d82a
FOUNDER_DIRECTIVE_DATE=2026-08-31
FOUNDER_DIRECTIVE_ORDERING=AFTER_V4_RESULT_RECONCILIATION_CANONICAL
```

The directive is interpreted narrowly at the current E004 dependency frontier. It authorizes only the evidence-backed repair and one new target runtime-evidence attempt defined here. It does not waive any other E004 gate or advance E005.

## 3. Canonical evidence basis

The canonical V4 reconciliation establishes:

```text
V4_DIAGNOSTIC_EXECUTION_STATE=CONSUMED_COMPLETE
V4_DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=OBSERVED_EMPTY
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=OBSERVED_NO_ALLOWLISTED_COMPATIBLE_ROUTE
STATIC_WORKFLOW_DEFECT_PROVEN=YES_EXACT_V4_RUNTIME_CONFIG_ROUTE_POLICY_EXCLUSION
V4_REQUIRED_COMPATIBLE_ROUTE_HOST=download-r2.pytorch.org
V4_REQUIRED_COMPATIBLE_ROUTE_PORT=443
V4_REQUIRED_COMPATIBLE_ROUTE_ALLOWLIST_RESULT=DENY
```

The same reconciliation preserves the historical causal boundary:

```text
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
HISTORICAL_STDERR_RECOVERED=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

No historical claim may be strengthened by this authority.

## 4. Maximum authorized target repair

After this authority record is independently reviewed and canonically merged, a separate implementation PR may modify exactly one logical target-workflow policy surface:

```text
TARGET_WORKFLOW=.github/workflows/e004-conversion-runtime-evidence.yml
REPAIR_SCOPE=PHASE_A_CONNECT_ALLOWLIST_ONLY
REPAIR_ADD_HOST=download-r2.pytorch.org
REPAIR_ADD_PORT=443
REPAIR_ADD_SCHEME=https
REPAIR_PRESERVE_EXISTING_ALLOWLIST=YES
REPAIR_PRESERVE_DENY_BY_DEFAULT=YES
TARGET_WORKFLOW_OTHER_LOGIC_MUTATION=PROHIBITED
```

The only authorized source-content change is to add `download-r2.pytorch.org` to the existing Phase A Python `ALLOWED` host set. No dependency requirement, index URL, source identity, tool commit/tree, runner label, timeout, Phase B behavior, evidence-manifest logic, permissions, trigger, concurrency, environment, model/conversion prohibition, benchmark prohibition, contamination prohibition, A15 prohibition, training prohibition, credential prohibition, upload prohibition, or spend boundary may be changed by that repair PR.

The repair PR must record the exact new target workflow Git blob SHA-1, raw SHA-256, and raw byte length and must receive fresh exact-head independent review before guarded canonical merge.

## 5. New target runtime-evidence attempt authority

The historical target runtime-evidence allowance was consumed by failed run `33366859146`; it is not reopened.

This record creates one **new and separate** target runtime-evidence attempt allowance, effective only after:

1. this authority record is independently reviewed and canonically merged;
2. the bounded target repair implementation is independently reviewed and canonically merged;
3. the exact repaired target workflow content identity is known and frozen from canonical `main`;
4. a separate connected-executor transport implementation is independently reviewed and canonically admitted.

```text
NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPT_AUTHORITY=AUTHORIZED_BOUNDED_AFTER_PREREQUISITES
MAX_NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPTS=1
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
TARGET_TRIGGER=workflow_dispatch_only
CURRENT_AUTHORIZED_SPEND_USD=0
AUTOMATIC_RETRY=PROHIBITED
FAILED_JOB_RERUN=PROHIBITED
ALTERNATE_TARGET_TRIGGER=PROHIBITED
```

A failed or partial new target run still consumes this new allowance. No rerun is implied by failure.

## 6. Connected-executor transport boundary

The connected surface currently exposes no native fresh `workflow_dispatch` creator. Therefore, after the repaired target workflow is canonically merged and identity-frozen, one separate transport implementation may be created using the already-canonical V2 transport pattern, updated only as required to bind the repaired target identity and current run cardinality.

The transport implementation must:

1. use a separate new workflow path and one-shot path-scoped `push` trigger;
2. run only on standard public `ubuntu-24.04`;
3. use only the ephemeral repository `GITHUB_TOKEN` with the minimum `actions: write` and `contents: write` permissions needed for metadata/ref/dispatch operations;
4. verify live repository visibility remains `public`, repository is not archived, and default branch remains `main`;
5. verify canonical `main` equals the transport run `GITHUB_SHA` before mutation or dispatch;
6. verify the repaired target workflow at canonical `main` exactly matches the frozen repaired blob SHA-1, raw SHA-256, raw byte length, path, active state, and `workflow_dispatch` trigger identity;
7. preserve the historical target run `33366859146` as consumed history and require zero prior `workflow_dispatch` runs for the **new repaired target subject identity** before creating the new dispatch;
8. create at most one new uniquely named transient SHA-bound branch resolving exactly to the verified canonical `main` SHA;
9. re-read the repaired target workflow through that binding ref and require exact repaired identity equality;
10. re-read the binding ref immediately before dispatch and require exact SHA equality;
11. create at most one new target `workflow_dispatch` request using explicit current GitHub dispatch semantics;
12. require the returned target run ID, URL, `head_sha`, `head_branch`, event, and workflow path to match the verified new subject;
13. verify post-dispatch cardinality contains exactly one run for the new repaired subject identity and returned run ID;
14. emit transport evidence to logs only;
15. perform no repository file-content mutation and no model, conversion, inference, benchmark, contamination, A15, training, provider-generation, procurement, payment, or spend action.

The old V2 bootstrap allowance remains consumed and is not reused or reopened. The old V2 transient binding branch is historical state and must not be reused as the new binding ref.

## 7. New target-run scientific boundary

The one new target runtime-evidence attempt is limited to the already-defined E004 conversion-runtime evidence workflow after the single allowlist repair.

It may execute exactly what that repaired workflow already defines:

- runner preflight;
- Phase A allowlisted public source and dependency staging;
- Phase B offline environment/local-GGUF attestation and rebuild if Phase A passes;
- final runtime evidence manifest if prior phases pass.

It remains prohibited from:

```text
MODEL_SOURCE_WEIGHT_ACQUISITION
MODEL_WEIGHT_LOADING
MODEL_CONVERSION
MODEL_WEIGHT_QUANTIZATION
MODEL_INFERENCE
BENCHMARK_PAYLOAD_ACCESS
BENCHMARK_EXECUTION
DEVICE_QUALIFICATION
CONTAMINATION_ASSESSMENT
SELECTION_SUITE_CONSTRUCTION
A15_ACTIVATION
PRIVATE_GOLD_OR_PHI_ACCESS
GATED_ASSET_ACCESS
EXTERNAL_REVIEWER_OUTREACH
PROVIDER_GENERATION
TRAINING
PROCUREMENT
PAYMENT
PAID_OR_LARGER_RUNNER
```

`CURRENT_AUTHORIZED_SPEND_USD=0` remains binding.

## 8. Evidence interpretation boundary

A PASS from the new target run may establish only the runtime-evidence facts explicitly emitted by the repaired workflow. It does not satisfy unrelated E004 blockers and does not advance E005 automatically.

A failure must be reconciled as observed. No failed step may be inferred to have passed, and no missing log may be reconstructed.

Regardless of the new run result, the historical run remains:

```text
HISTORICAL_TARGET_RUN_ID=33366859146
HISTORICAL_TARGET_JOB_ID=99409197359
HISTORICAL_TARGET_CONCLUSION=failure
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

## 9. Required dependency-ordered lifecycle

```text
THIS_AUTHORITY_RECORD_EXACT_HEAD_REVIEW
-> THIS_AUTHORITY_RECORD_GUARDED_CANONICAL_MERGE
-> MINIMUM_TARGET_ALLOWLIST_REPAIR_IMPLEMENTATION
-> REPAIRED_TARGET_IDENTITY_CAPTURE
-> REPAIR_EXACT_HEAD_INDEPENDENT_REVIEW
-> REPAIR_GUARDED_CANONICAL_MERGE
-> FRESH_TRANSPORT_IMPLEMENTATION_BOUND_TO_REPAIRED_TARGET_IDENTITY
-> TRANSPORT_EXACT_HEAD_INDEPENDENT_REVIEW
-> TRANSPORT_GUARDED_CANONICAL_MERGE
-> EXACTLY_ONE_NEW_TRANSPORT_RUN
-> EXACTLY_ONE_NEW_TARGET_WORKFLOW_DISPATCH_OR_FAIL_CLOSED
-> TERMINAL_NEW_TARGET_RUN_EVIDENCE_CAPTURE
-> SEPARATE_RESULT_RECONCILIATION
```

No step may be skipped because continuation approval is broad.

## 10. State before execution

Canonical merge of this authority record alone does not repair or execute anything:

```text
TARGET_WORKFLOW_REPAIRED=NO
NEW_TARGET_RUNTIME_EVIDENCE_EXECUTION_OCCURRED=NO
NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPTS_USED=0
NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPTS_REMAINING=1_AFTER_ALL_PREREQUISITES
COMPONENT_RUNTIME_EVIDENCE=FAILED_PHASE_A_HISTORICAL_WITH_STATIC_ROUTE_DEFECT_PROVEN_BY_V4
COMPONENT_E004=INCOMPLETE
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_CONVERSION_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 11. Required merge-exit review

This authority record may become canonical only after fresh exact-head independent repository review verifies at least:

- the Founder directive is bound after canonical V4 result reconciliation;
- V4 evidence is represented without strengthening historical causality;
- the repair is limited to adding `download-r2.pytorch.org:443` to the Phase A CONNECT allowlist;
- all other target workflow logic is prohibited from mutation by the repair unit;
- the historical target allowance remains consumed and no historical rerun is authorized;
- exactly one new, separate target runtime-evidence attempt is created only after repair and transport qualification prerequisites;
- the transport pattern is separate, one-shot, identity-bound, and cannot reuse the old V2 allowance or old transient binding ref;
- failure consumes the new allowance and creates no automatic retry;
- no model conversion, inference, benchmark, contamination, A15, training, credential persistence, paid runner, procurement/payment, or spend authority is created;
- E004 remains incomplete and E005 remains not reached until subsequent evidence says otherwise.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```

Only after guarded canonical merge of the exact reviewed authority head may the bounded target repair implementation begin.
