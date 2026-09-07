# E004 Operational Preflight Evidence Implementation V1 — 2026-09-08

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Implementation base:** `b9eb2c8b1b4bebfd4ddc63600d1cf07ba9a2bbea`
**Authority:** `specs/007-sft-v1/e004-operational-preflight-evidence-founder-decision-2026-09-08.md`
**Design:** `specs/007-sft-v1/e004-operational-preflight-evidence-design-2026-09-07.md`
**Artifact class:** review-first bounded implementation record
**Model / evaluation / tournament / A15 / training effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Implement the smallest review-first lane authorized by the exact post-canonical Founder Decision B for E004 operational-preflight evidence.

The implementation PR is static qualification only. It cannot create empirical operational evidence. The empirical lane becomes triggerable only after this implementation is canonically merged and only by one marker-only commit on the exact versioned evidence branch.

## 2. Exact repository surface

This implementation is intentionally limited to:

```text
.github/workflows/e004-operational-preflight-evidence-v1.yml
tests/spec007/test_e004_operational_preflight_evidence_policy.py
specs/007-sft-v1/e004-operational-preflight-evidence-implementation-v1-2026-09-08.md
```

The reserved post-merge marker path is:

```text
.github/e004-operational-preflight-run-v1.txt
```

The marker is absent from the implementation PR and may be created only after the exact implementation merge is canonical.

## 3. Review-first execution separation

The workflow has two mutually exclusive paths:

```text
PULL_REQUEST_PATH=STATIC_QUALIFICATION_ONLY
PUSH_PATH=EXACT_VERSIONED_EVIDENCE_BRANCH_AND_MARKER_ONLY
WORKFLOW_DISPATCH=ABSENT
REPOSITORY_DISPATCH=ABSENT
SCHEDULE=ABSENT
```

The pull-request path performs only repository/static qualification:

- exact-head authority binding;
- focused policy tests;
- Spec 007 regression;
- full repository regression;
- diff whitespace validation.

It does not provision the operational runtime and does not create empirical operational-preflight evidence.

## 4. Single-run marker mechanics

The post-merge evidence run is mechanically constrained to:

```text
EVIDENCE_BRANCH=evidence/e004-operational-preflight-run-v1
EVIDENCE_MARKER=.github/e004-operational-preflight-run-v1.txt
MAX_AUTHORIZED_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
RUN_ATTEMPT_REQUIRED=1
RERUN_AUTHORITY=NONE_BY_DEFAULT
FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

The marker commit must:

1. be a direct child of the exact canonical implementation merge;
2. contain only the marker path;
3. bind that exact merge SHA in `IMPLEMENTATION_CANONICAL_MERGE`;
4. bind the exact Founder decision-token SHA-256;
5. be the only commit above the implementation merge on the evidence branch.

The runtime job also rejects a parent that is not a merge commit.

## 5. Frozen no-model runtime identities

The lane reconstructs only exact runtime identities already established canonically.

### llama.cpp

```text
EXACT_LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
EXACT_LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
EXACT_LLAMA_CPP_TAG=b10621
EXACT_LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
EXACT_LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
EXACT_LLAMA_CLI_SHA256=f0034d9e6959f6c32b40cbb5326f41ccdbac21b77feb27a6f32c0a7465c9ebf7
```

### Transformers / Torch CPU

```text
TRANSFORMERS_VERSION=4.57.6
TRANSFORMERS_COMMIT=753d61104116eefc8ffc977327b441ee0c8d599f
TORCH_RUNTIME_TARGET=2.11.0+cpu
CANONICAL_DEPENDENCY_ARTIFACT_COUNT=27
CANONICAL_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
PYTHON_RUNTIME_SHA256=a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223
CANONICAL_INSTALLED_ENVIRONMENT_MANIFEST_SHA256=54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384
```

Dependency or runner drift fails closed; compatible-version substitution is not accepted.

## 6. Credential, access and network boundaries

The workflow uses repository `contents: read` only and `checkout` with `persist-credentials: false`.

Custom evidence steps explicitly remove known GitHub, Hugging Face and cloud credential variables before public runtime provisioning. The canonical four-candidate bundle set is read only as repository metadata and must show all four candidate bundles as `PUBLIC_UNGATED_EXACT_IDENTITY`.

Provisioning destinations are statically bounded to the exact public runtime sources already required by canonical runtime identity:

```text
LLAMA_RUNTIME_SOURCE_FAMILY=github.com + GitHub release asset hosts
TRANSFORMERS_RUNTIME_SOURCE_FAMILY=pypi.org + files.pythonhosted.org + download.pytorch.org
```

After staging, runtime/static validation is executed under the existing `sudo -n unshare -n` default-deny network-namespace pattern. No model-provider endpoint or evaluation-data endpoint is permitted.

## 7. Host, resource and retention evidence

The evidence lane records only actual operational observations for the exact allocated standard public GitHub-hosted `ubuntu-24.04` runner, including:

- runner image OS/version;
- host OS-release digest;
- kernel and libc identity;
- CPU model and logical CPU count;
- total/available memory;
- root and runner-temp filesystem capacity/free space;
- post-staging runner-temp free space;
- workflow wallclock cap.

The lane creates one synthetic retention sentinel in ephemeral runner storage, removes the entire staging root in an `always()` cleanup step, and requires absence after cleanup. No Actions cache, workflow artifact, release asset or package-registry upload path exists.

## 8. Static qualification gate

Before merge, the exact PR head must prove:

```text
AUTHORITY_PREFLIGHT_TESTS=PASS
NO_MODEL_NO_EVALUATION_PAYLOAD_POLICY_TESTS=PASS
EXACT_RUNTIME_IDENTITY_BINDING_TESTS=PASS
NETWORK_BOUNDARY_POLICY_TESTS=PASS
CREDENTIAL_BOUNDARY_POLICY_TESTS=PASS
RETENTION_CLEANUP_POLICY_TESTS=PASS
TRIGGER_SINGLE_RUN_POLICY_TESTS=PASS
SPEC007_REGRESSION=PASS
FULL_REPOSITORY_REGRESSION=PASS
DIFF_WHITESPACE=PASS
```

Green static CI is implementation qualification only. It must not be represented as empirical operational-preflight evidence.

Independent repository review remains optional by default under constitutional amendment FD-007; the exact-head deterministic qualification above remains mandatory.

## 9. Explicit non-expansion

```text
IMPLEMENTATION_STATE=REVIEW_FIRST_NOT_CANONICAL
OPERATIONAL_PREFLIGHT_EVIDENCE=NOT_RUN_BY_IMPLEMENTATION_PR
CANDIDATE_MODEL_WEIGHT_ACQUISITION=PROHIBITED
MODEL_LOAD=PROHIBITED
MODEL_FORWARD_PASS=PROHIBITED
MODEL_INFERENCE=PROHIBITED
TOKEN_GENERATION=PROHIBITED
EVALUATION_PAYLOAD_ACCESS=PROHIBITED
EVALUATION_PAYLOAD_EXECUTION=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
MODEL_CONVERSION=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
GATED_ASSET_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE
TOURNAMENT_EXECUTION_AUTHORITY_EXPANSION=NONE
A15_AUTHORITY_EXPANSION=NONE
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

## 10. Post-merge transition

Only after an exact qualified implementation head is canonically merged may the next transition occur:

1. create `evidence/e004-operational-preflight-run-v1` from the exact canonical implementation merge;
2. create exactly one marker-only direct-child commit binding that merge and the exact Founder decision-token SHA-256;
3. allow exactly one run attempt;
4. reconcile observed evidence append-only as `PASS`, `INCOMPLETE`, or `FAIL`;
5. only on real PASS may later repository work bind exact environment/resource/access/orchestrator evidence and construct the applicable A1-A14 snapshot;
6. A15 remains a separate later activation decision if it becomes the sole remaining prerequisite;
7. tournament execution, winner selection and training remain outside this implementation authority.
