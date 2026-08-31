# E004 Phase A Diagnostic V3 Authority — 2026-08-31

**Spec:** 007 SFT V1  
**Decision owner:** Founder  
**Artifact class:** bounded diagnostic-only execution authority  
**Canonical base:** `c7dd451b14e90c1d1e7c41dd1c58a0951beab932`  
**Prior reconciliation:** `specs/007-sft-v1/e004-runtime-evidence-v2-terminal-failure-reconciliation-2026-08-31.md`  
**Prior reconciliation merge:** `c7dd451b14e90c1d1e7c41dd1c58a0951beab932`  
**Authority effect before canonical merge:** NONE  
**Model weight authority:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation authority:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Authorize the smallest dependency-ordered successor to the canonical V2 terminal-failure reconciliation: one independently reviewed, zero-spend, diagnostic-only GitHub Actions execution whose sole purpose is to collect and retain direct Phase A evidence sufficient to determine the current reproducible failure mechanism, including evaluation of the existing dependency/artifact-host/network-route hypothesis without presuming that hypothesis is causal.

This authority does not repair or execute the E004 conversion-runtime evidence target workflow. It does not reopen any consumed V2 allowance and does not create model, conversion, inference, benchmark, contamination, A15, training, credential, artifact/cache-upload, procurement, payment, or spend authority.

## 2. Founder directive and ordering

After PR #148 was independently reviewed at exact head `6ba9ec70aeb1e6f689823c6511fa8d0c8e30717e` with `MATERIAL_BLOCKER=NO`, merged canonically as `c7dd451b14e90c1d1e7c41dd1c58a0951beab932`, and the canonical governance plus active Spec 007 authority chain were re-read, the Founder issued:

```text
FOUNDER_DIRECTIVE=fix that go ahead do not stop until finish the project , you have all approvals fro me
FOUNDER_DIRECTIVE_SHA256=0e83ba56d0b4163360ed5c6090bfc67822505298b850eae1b6fc6f29579bbdad
FOUNDER_DIRECTIVE_DATE=2026-08-31
FOUNDER_DIRECTIVE_ORDERING=AFTER_PR148_CANONICAL_AND_FRESH_GOVERNANCE_REREAD
```

The directive is interpreted narrowly at the current dependency frontier. It authorizes creation and qualification of this V3 authority record only. It does not waive independent review, evidence, scientific, provenance, quarantine, safety, finance, execution, or later lifecycle gates.

## 3. Preserved historical evidence boundary

V3 starts from the canonical observed record and must not reinterpret it:

```text
V2_BOOTSTRAP_RUN=33366850471
V2_BOOTSTRAP_RESULT=PASS
TARGET_RUN_ID=33366859146
TARGET_JOB_ID=99409197359
TARGET_EVENT=workflow_dispatch
TARGET_HEAD_SHA=ef1be50f4a076d9f03abfffee342d2c244b0d199
TARGET_RUN_ATTEMPT=1
TARGET_CONCLUSION=failure

RUNNER_PREFLIGHT=PASS
PHASE_A_ALLOWLISTED_PUBLIC_SOURCE_AND_DEPENDENCY_STAGING=FAIL
PHASE_B_OFFLINE_ENVIRONMENT_LOCAL_GGUF_ATTESTATION_AND_REBUILD=SKIPPED
FINAL_RUNTIME_EVIDENCE_MANIFEST=SKIPPED

HISTORICAL_STDERR_RECOVERED=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
STATIC_WORKFLOW_DEFECT_PROVEN=NO
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
```

The current diagnostic hypothesis remains exactly that: a hypothesis. `download-r2.pytorch.org` is a concrete candidate host already recorded by the canonical reconciliation, not a proven historical failure cause.

## 4. Bounded V3 authority

Only after this authority record is independently reviewed and canonically merged, and only after a separate minimal V3 diagnostic workflow implementation is independently reviewed and canonically merged, the project may execute exactly one diagnostic run under these bounds:

```text
E004_PHASE_A_DIAGNOSTIC_V3_AUTHORITY=AUTHORIZED_BOUNDED
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
MAX_AUTHORIZED_V3_DIAGNOSTIC_RUNS=1
V3_PURPOSE=COLLECT_DIRECT_RETAINED_PHASE_A_DIAGNOSTIC_EVIDENCE
V3_TRIGGER=push_to_main_path_scoped_to_exact_v3_diagnostic_workflow_file
V3_AUTOMATIC_RETRY_AUTHORITY=NONE
V3_FAILED_JOB_RERUN_AUTHORITY=NONE
V3_TARGET_WORKFLOW_DISPATCH_AUTHORITY=NONE
TARGET_WORKFLOW_MUTATION_AUTHORITY=NONE
V2_ALLOWANCE_REOPEN_AUTHORITY=NONE
DIAGNOSTIC_EVIDENCE_RETENTION=GITHUB_ACTIONS_JOB_LOGS_ONLY
ARTIFACT_UPLOAD_AUTHORITY=NONE
CACHE_UPLOAD_AUTHORITY=NONE
CREDENTIAL_USE_AUTHORITY=NONE
PRIVATE_SECRET_ACCESS_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The path-scoped push trigger is authorized only as a one-shot execution mechanism for the future V3 diagnostic implementation because the currently connected executor exposes no native fresh `workflow_dispatch` creation action. The implementation merge itself may trigger the single authorized V3 diagnostic run. A later push, rerun, alternate trigger, or second execution is not authorized by this record.

If a native fresh-dispatch mechanism becomes available before implementation, the implementation may use a separately reviewed one-shot trigger only if it preserves or narrows every cardinality and exclusion in this record; no trigger choice may execute the target E004 runtime-evidence workflow.

## 5. Authorized diagnostic evidence surface

The future V3 diagnostic may use only public, ungated network access needed to inspect and reproduce the Phase A dependency-routing decision. The smallest intended evidence surface is:

1. record exact runner, Python, and pip identities in job logs;
2. bind the exact Phase A CONNECT allowlist from the failed target workflow as diagnostic input;
3. retrieve public PyTorch CPU index metadata needed to identify current links for the exact `torch==2.11.0+cpu` requirement;
4. parse and log the relevant artifact URL hostnames without downloading model weights or package artifact bodies;
5. reproduce the exact allowlist decision against the discovered host or hosts and retain direct `ALLOW` / `DENY` evidence in job logs;
6. if technically necessary to distinguish routing behavior, perform only bounded metadata/CONNECT/HEAD-style network probes that do not download the dependency artifact body;
7. emit a deterministic summary that distinguishes observation from conclusion.

The diagnostic must be designed to prove, falsify, or leave unresolved the current dependency/artifact-host/network-route hypothesis. It must not encode `download-r2.pytorch.org` as the expected answer and must not classify a workflow defect as proven merely because that hostname appears.

A specific target-workflow defect may be classified as proven only if direct retained evidence establishes that the exact required dependency route cannot satisfy the target workflow's exact Phase A allowlist/configuration for the relevant runtime subject and no observed compliant route satisfies that exact requirement. Otherwise:

```text
STATIC_WORKFLOW_DEFECT_PROVEN=NO
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
```

remain fail-closed.

## 6. Explicit exclusions

```text
TARGET_RUNTIME_EVIDENCE_WORKFLOW_DISPATCH=PROHIBITED
V2_BOOTSTRAP_RERUN=PROHIBITED
V2_TARGET_RERUN=PROHIBITED
FAILED_TARGET_JOB_RERUN=PROHIBITED
TARGET_WORKFLOW_REPAIR=PROHIBITED
TARGET_WORKFLOW_MUTATION=PROHIBITED
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

The diagnostic may not clone or stage the full conversion toolchain merely to imitate the target workflow when narrower dependency-route evidence is sufficient. It may not install new repository dependencies or persist generated evidence in caches/artifacts.

## 7. Repository mutation boundary

This authority record permits no executable repository mutation by itself.

After this record becomes canonical, a separate implementation PR may add only the smallest diagnostic workflow surface necessary to execute Section 5. That implementation must be independently reviewed at its exact final head before canonical merge.

The V3 diagnostic workflow itself may not mutate repository contents, refs, branches, releases, issues, pull requests, or the target runtime-evidence workflow.

```text
REPOSITORY_CONTENT_MUTATION_BY_V3_RUNTIME=PROHIBITED
REF_MUTATION_BY_V3_RUNTIME=PROHIBITED
TARGET_WORKFLOW_MUTATION_BY_V3=PROHIBITED
HISTORY_REWRITE=PROHIBITED
FORCE_PUSH=PROHIBITED
```

## 8. Required lifecycle

```text
V3_AUTHORITY_RECORD_EXACT_HEAD_REVIEW_AND_CANONICAL_MERGE
-> MINIMAL_V3_DIAGNOSTIC_WORKFLOW_IMPLEMENTATION_FROM_THEN_CURRENT_MAIN
-> FRESH_EXACT_HEAD_INDEPENDENT_REPOSITORY_REVIEW
-> GUARDED_CANONICAL_MERGE
-> EXACTLY_ONE_V3_DIAGNOSTIC_EXECUTION
-> RETAINED_DIRECT_PHASE_A_EVIDENCE_CAPTURE
-> CANONICAL_V3_RESULT_RECONCILIATION
```

No step may be skipped because the Founder granted continuation approval.

## 9. Result-state rule

The V3 diagnostic result does not itself authorize a repair or another target run.

If direct retained diagnostic evidence does not prove a specific workflow defect, E004 remains fail-closed and no target repair or runtime-evidence attempt is authorized.

Only if direct retained evidence proves a specific defect may a later separate founder-authorized, independently reviewed, canonically merged authority decide whether to permit all of the following narrowly and explicitly:

1. the exact minimal target-workflow repair;
2. a new exact target-workflow identity;
3. exactly one new target runtime-evidence attempt;
4. zero spend; and
5. preservation of all scientific and execution exclusions not expressly changed by that later authority.

This V3 authority does not pre-authorize any item in that later list.

## 10. Scientific and component state effect

Canonical merge of this record changes only the future diagnostic authority. It does not complete E004 or advance E005:

```text
COMPONENT_RUNTIME_EVIDENCE=FAILED_PHASE_A
COMPONENT_CONVERSION_PREREQUISITES=INCOMPLETE
COMPONENT_CONTAMINATION_PREREQUISITES=INCOMPLETE
COMPONENT_RESOURCE_ACCESS_BINDINGS=INCOMPLETE
COMPONENT_A1_A14_EQUIVALENT_EXACT_PASS_SNAPSHOT=ABSENT
COMPONENT_A15=ABSENT_NOT_AUTHORIZED
COMPONENT_BACKBONE_WINNER=NEEDS_EVIDENCE
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_RUNTIME_DIAGNOSTIC_EVIDENCE
COMPONENT_E005_STATE=NOT_REACHED
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

## 11. Exit evidence

This V3 authority record is eligible for canonical merge only when fresh exact-head independent repository review confirms:

```text
PR148_RECONCILIATION_CANONICAL=YES
HISTORICAL_FAILURE_BOUNDARY_PRESERVED=YES
PHASE_A_FAILURE_CAUSE_REMAINS_NEEDS_EVIDENCE=YES
STATIC_WORKFLOW_DEFECT_PROVEN_REMAINS_NO=YES
V2_ALLOWANCES_REOPENED=NO
V3_AUTHORITY_IS_DIAGNOSTIC_ONLY=YES
MAX_V3_DIAGNOSTIC_RUNS=1
TARGET_WORKFLOW_DISPATCH_AUTHORITY_CREATED=NO
TARGET_WORKFLOW_REPAIR_AUTHORITY_CREATED=NO
MODEL_WEIGHT_AUTHORITY_CREATED=NO
MODEL_CONVERSION_AUTHORITY_CREATED=NO
BENCHMARK_AUTHORITY_CREATED=NO
CONTAMINATION_AUTHORITY_CREATED=NO
A15_AUTHORITY_CREATED=NO
TRAINING_AUTHORITY_CREATED=NO
CREDENTIAL_AUTHORITY_CREATED=NO
ARTIFACT_OR_CACHE_UPLOAD_AUTHORITY_CREATED=NO
SPEND_AUTHORITY_CREATED=NO
E004_REMAINS_INCOMPLETE=YES
E005_REMAINS_NOT_REACHED=YES
MATERIAL_BLOCKER=NO
```
