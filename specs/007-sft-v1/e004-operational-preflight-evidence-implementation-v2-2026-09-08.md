# E004 Operational Preflight Evidence Implementation V2 — 2026-09-08

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Implementation base:** `846807332c69c64ace242a492e900491a58f020a`
**Authority:** `specs/007-sft-v1/e004-operational-preflight-corrective-attempt-founder-decision-2026-09-08.md`
**Canonical decision request:** `specs/007-sft-v1/e004-operational-preflight-corrective-attempt-founder-decision-request-2026-09-08.md`
**Artifact class:** review-first bounded corrective implementation record
**Model / evaluation / tournament / A15 / training effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Implement the smallest versioned corrective operational-preflight lane authorized by the exact post-canonical Founder Decision B after the V1 one-shot allowance was consumed by terminal pre-provisioning failure.

V2 is prospective only. It does not rerun, retry, replay, amend, reinterpret, or reclassify V1.

The implementation PR performs static qualification only. The empirical V2 lane may become triggerable only after this implementation is canonically merged and only through one marker-only direct-child commit on the exact V2 evidence branch.

## 2. Exact repository surface

This implementation is intentionally limited to:

```text
.github/workflows/e004-operational-preflight-evidence-v2.yml
tests/spec007/test_e004_operational_preflight_evidence_v2_policy.py
specs/007-sft-v1/e004-operational-preflight-evidence-implementation-v2-2026-09-08.md
```

The reserved post-merge evidence surface is:

```text
EVIDENCE_BRANCH=evidence/e004-operational-preflight-run-v2
EVIDENCE_MARKER=.github/e004-operational-preflight-run-v2.txt
```

The marker is absent from the implementation PR.

## 3. Review-first execution separation

```text
PULL_REQUEST_PATH=STATIC_QUALIFICATION_ONLY
PUSH_PATH=EXACT_VERSIONED_V2_EVIDENCE_BRANCH_AND_MARKER_ONLY
WORKFLOW_DISPATCH=ABSENT
REPOSITORY_DISPATCH=ABSENT
SCHEDULE=ABSENT
```

The pull-request path is limited to:

- exact-head decision-authority binding;
- focused V2 policy tests;
- Spec 007 regression;
- full repository regression;
- diff whitespace validation.

It does not provision the empirical runtime and cannot create operational-preflight evidence.

## 4. Corrective one-shot mechanics

The exact V2 controls are:

```text
MAX_AUTHORIZED_CORRECTIVE_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
CORRECTIVE_RUN_ATTEMPT_REQUIRED=1
CORRECTIVE_RERUN_AUTHORITY=NONE_BY_DEFAULT
CORRECTIVE_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
ANCESTRY_GUARD_CHECKOUT_FETCH_DEPTH=0
```

The marker commit must:

1. be a direct child of the exact canonical V2 implementation merge;
2. change only `.github/e004-operational-preflight-run-v2.txt`;
3. bind the exact implementation merge SHA in `IMPLEMENTATION_CANONICAL_MERGE`;
4. bind the exact corrective Founder token SHA-256 `774f35983f70ba560b2e0bd9174a7f2f76c92c1617e76851e1123dcc7d39780e`;
5. be the only commit above that implementation merge on the V2 evidence branch.

The runtime guard uses full history, verifies that the marker parent is a merge commit, verifies the exact one-commit/one-path relationship, and verifies that the V2 workflow and canonical corrective decision record already exist in the parent merge.

## 5. Frozen public runtime identities

V2 may reconstruct only exact runtime identities already bound canonically.

### llama.cpp

```text
EXACT_LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
EXACT_LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
EXACT_LLAMA_CPP_TAG=b10621
EXACT_LLAMA_RUNTIME_ARCHIVE_BYTES=16291771
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

Compatible substitution is not accepted. Identity or dependency drift fails closed.

## 6. Credential, access, network, and retention boundary

The workflow uses repository `contents: read` only and checkout with `persist-credentials: false`.

Known GitHub, Hugging Face, AWS, Google Cloud, and Azure credential variables are removed from custom empirical steps. Candidate bundle metadata must remain exactly `PUBLIC_UNGATED_EXACT_IDENTITY` for all four frozen candidate bundles.

Provisioning is restricted to the exact public runtime source families already required by the canonical runtime identities:

```text
LLAMA_RUNTIME_SOURCE_FAMILY=github.com + GitHub release asset hosts
TRANSFORMERS_RUNTIME_SOURCE_FAMILY=pypi.org + files.pythonhosted.org + download.pytorch.org
```

After runtime staging, validation uses `sudo -n unshare -n` and proves the isolated network namespace has no default route.

The lane uses only ephemeral runner storage. It creates a synthetic V2 retention sentinel, removes the complete V2 staging root in an `always()` cleanup step, and verifies absence. There is no Actions cache, workflow artifact, release asset, or package-registry upload path.

## 7. Host/resource evidence boundary

The V2 empirical lane may observe only the allocated standard public GitHub-hosted `ubuntu-24.04` runner and the already-authorized runtime reconstruction state, including:

- image OS/version;
- OS-release digest;
- kernel and libc identity;
- CPU model and logical CPU count;
- total and available memory;
- root and runner-temp filesystem capacity/free space;
- post-staging runner-temp free space;
- wallclock cap;
- cleanup state;
- zero-spend runner class.

```text
PROVIDER=GitHub_Actions
RUNNER_LABEL=ubuntu-24.04
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
PAID_OR_LARGER_RUNNER=PROHIBITED
SELF_HOSTED_RUNNER=PROHIBITED
GPU_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 8. Static qualification gate

Before guarded merge, the exact PR head must prove:

```text
CORRECTIVE_DECISION_BINDING_TESTS=PASS
V2_TRIGGER_SINGLE_RUN_POLICY_TESTS=PASS
V2_ANCESTRY_GUARD_POLICY_TESTS=PASS
V1_NON_REUSE_POLICY_TESTS=PASS
NO_MODEL_NO_EVALUATION_PAYLOAD_POLICY_TESTS=PASS
EXACT_RUNTIME_IDENTITY_BINDING_TESTS=PASS
NETWORK_BOUNDARY_POLICY_TESTS=PASS
CREDENTIAL_BOUNDARY_POLICY_TESTS=PASS
RETENTION_CLEANUP_POLICY_TESTS=PASS
SPEC007_REGRESSION=PASS
FULL_REPOSITORY_REGRESSION=PASS
DIFF_WHITESPACE=PASS
```

Green static CI is implementation qualification only and must not be represented as empirical V2 evidence.

Independent repository review remains optional by default under constitutional amendment FD-007 unless a narrower live authority requires it.

## 9. Explicit non-expansion

```text
IMPLEMENTATION_STATE=REVIEW_FIRST_NOT_CANONICAL
OPERATIONAL_PREFLIGHT_EVIDENCE_V2=NOT_RUN_BY_IMPLEMENTATION_PR
V1_EVIDENCE_AUTHORITY=CONSUMED_UNCHANGED
V1_RERUN=PROHIBITED
V1_FAILED_JOB_RERUN=PROHIBITED
V1_REPLAY=PROHIBITED
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

Only after this exact implementation head passes its static qualification and is guarded-merged canonically may the next transition occur:

1. verify the exact V2 implementation merge on canonical `main`;
2. create `evidence/e004-operational-preflight-run-v2` from that exact merge;
3. create exactly one marker-only direct-child commit binding that merge and the exact corrective Founder token SHA-256;
4. allow exactly one empirical V2 workflow run at attempt 1;
5. treat that first run as consuming the complete V2 allowance regardless of conclusion;
6. never rerun or retry V2 absent a later separate exact authority;
7. reconcile observed evidence append-only as `PASS`, `INCOMPLETE`, or `FAIL`;
8. only on actual PASS may later dependency-ordered work use those observed fields toward a live applicable A1-A14 snapshot;
9. A15 activation, tournament execution, winner selection, and training remain separate downstream authorities.
