# E004 / E002 Preconverted Byte-Integrity Run Evidence — 2026-09-05

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Authority used:** canonical E002 exact preconverted-artifact allowlist only  
**Canonical workflow merge:** `6d328b9a64a420bcb43fcd08f82745fd2604d47c`  
**Workflow path:** `.github/workflows/e002-preconverted-integrity-evidence-v1.yml`  
**Execution branch:** `evidence/e002-preconverted-integrity-run-v1`  
**Execution marker head:** `76a2c71ab08ca91d6ed74ae7dcd10aa23a407e1d`  
**Workflow run:** `33972164617`  
**Run conclusion:** `success`  
**Model load performed:** NO  
**Model execution performed:** NO  
**Model conversion performed:** NO  
**Benchmark/evaluation access performed:** NO  
**Artifact upload performed:** NO  
**Credential use performed:** NO  
**Training performed:** NO  
**Spend:** USD 0

## 1. Purpose and authority boundary

This record captures real byte-integrity evidence for the exact two preconverted artifacts already enumerated by canonical E002 authority. The run materialized only those exact public/ungated files on ephemeral standard GitHub-hosted runners, recomputed integer byte count and SHA-256, and checked the static four-byte `GGUF` container magic.

It did not import a model runtime, load weights, execute inference, convert or quantize weights, access evaluation payloads, select a winner, train, use credentials, upload artifacts, or spend money.

```text
E002_SCOPE=EXACT_PRECONVERTED_ALLOWLIST_ONLY
MODEL_LOAD=PROHIBITED
MODEL_EXECUTION=PROHIBITED
CONVERSION=PROHIBITED
BENCHMARK_ACCESS=PROHIBITED
CREDENTIAL_USE=PROHIBITED
ARTIFACT_UPLOAD=PROHIBITED
TRAINING=PROHIBITED
SPEND_USD=0
```

## 2. Exact workflow and runner identity

```text
RUN_ID=33972164617
RUN_EVENT=push
RUN_BRANCH=evidence/e002-preconverted-integrity-run-v1
RUN_HEAD_SHA=76a2c71ab08ca91d6ed74ae7dcd10aa23a407e1d
RUN_CONCLUSION=success
RUNNER_VERSION=2.337.0
RUNNER_OS=Linux
RUNNER_ARCH=X64
RUNNER_IMAGE=ubuntu-24.04
RUNNER_IMAGE_VERSION=20260831.293.1
OPERATING_SYSTEM=Ubuntu_24.04.4_LTS
```

The workflow had three jobs. On this push, `static-qualification` was intentionally skipped and only the exact byte-integrity jobs executed:

```text
QWEN06_JOB_ID=101322479750
QWEN06_JOB_NAME=qwen06-integrity
QWEN06_JOB_CONCLUSION=success
QWEN35_JOB_ID=101322479829
QWEN35_JOB_NAME=qwen35-integrity
QWEN35_JOB_CONCLUSION=success
```

The run artifact endpoint returned an empty list.

```text
WORKFLOW_ARTIFACT_COUNT=0
ACTIONS_ARTIFACT_PERSISTENCE_OCCURRED=NO
```

## 3. Qwen3 0.6B PRIMARY preconverted integrity

The exact E002 allowlist entry is:

```text
CANDIDATE_ID=Qwen/Qwen3-0.6B-Base
CANDIDATE_REVISION=da87bfb608c14b7cf20ba1ce41287e8de496c0cd
ARTIFACT_REPOSITORY=Antigma/Qwen3-0.6B-Base-GGUF
ARTIFACT_REVISION=f457544766bcdc72afd3514439eb3d422d4434dc
ARTIFACT_FILENAME=qwen3-0.6b-base-q4_k_m.gguf
EXPECTED_BYTES=396704512
EXPECTED_SHA256=218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492
E001_LABEL=EXACT_BASE_DERIVATIVE_FEASIBILITY_ONLY_NOT_FINAL_RELEASE_BINDING
```

The successful job emitted the same observed byte identity:

```text
ARTIFACT_BYTES=396704512
ARTIFACT_SHA256=218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492
STATIC_CONTAINER_MAGIC=GGUF
BYTE_INTEGRITY=PASS
MODEL_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
ARTIFACT_UPLOAD_PERFORMED=NO
CREDENTIAL_USE_PERFORMED=NO
SPEND_USD=0
```

Therefore the provider-bound E002 byte identity now also has commandMed-governed ephemeral recomputation evidence. This does not change the frozen E001 feasibility label and does not by itself make the artifact the final tournament execution binding.

## 4. Qwen3.5 0.8B PRIMARY preconverted integrity

The exact E002 allowlist entry is:

```text
CANDIDATE_ID=Qwen/Qwen3.5-0.8B-Base
CANDIDATE_REVISION=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
ARTIFACT_REPOSITORY=ggml-org/Qwen3.5-0.8B-Base-GGUF
ARTIFACT_REVISION=1bd44f68963429437d08bc12f465716eb31ba6e5
ARTIFACT_FILENAME=Qwen3.5-0.8B-Base-Q4_0.gguf
EXPECTED_BYTES=563035840
EXPECTED_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
E001_LABEL=DIRECT_DIGEST_PUBLIC_METADATA
```

The successful job emitted:

```text
ARTIFACT_BYTES=563035840
ARTIFACT_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
STATIC_CONTAINER_MAGIC=GGUF
BYTE_INTEGRITY=PASS
MODEL_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
ARTIFACT_UPLOAD_PERFORMED=NO
CREDENTIAL_USE_PERFORMED=NO
SPEND_USD=0
```

This closes the local ephemeral byte-recomputation gap only. Runtime compatibility, complete executable-bundle identity, environment identity, resource/access binding, A1-A14 applicable snapshot, A15 activation, and exact live execution-subject authorization remain separate gates.

## 5. Negative evidence and retention boundary

Both jobs explicitly unset `HF_TOKEN`, `HUGGING_FACE_HUB_TOKEN`, `GH_TOKEN`, and `GITHUB_TOKEN` inside the acquisition shell and used direct public HTTPS only.

```text
MODEL_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
MODEL_CONVERSION_PERFORMED=NO
BENCHMARK_ACCESS_PERFORMED=NO
EVALUATION_EXECUTION_PERFORMED=NO
WINNER_SELECTION_PERFORMED=NO
TRAINING_PERFORMED=NO
CREDENTIAL_USE_PERFORMED=NO
ARTIFACT_UPLOAD_PERFORMED=NO
CACHE_UPLOAD_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
PAID_OR_LARGER_RUNNER_USED=NO
SPEND_USD=0
RETENTION=EPHEMERAL_RUNNER_ONLY
```

No model bytes are persisted by this evidence record or by the run.

## 6. Exact current interpretation

```text
QWEN06_PRECONVERTED_BYTE_INTEGRITY=PASS_ON_RUN_33972164617
QWEN35_PRECONVERTED_BYTE_INTEGRITY=PASS_ON_RUN_33972164617
QWEN06_STATIC_GGUF_CONTAINER_IDENTITY=PASS
QWEN35_STATIC_GGUF_CONTAINER_IDENTITY=PASS
QWEN06_FINAL_TOURNAMENT_RUNTIME_BINDING=NOT_YET_CANONICAL
QWEN35_FINAL_TOURNAMENT_RUNTIME_BINDING=NOT_YET_CANONICAL
COMPLETE_FOUR_CANDIDATE_EXECUTION_ARTIFACT_SET=INCOMPLETE
SUCCESSOR_PASS_PREFLIGHT=NO
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

This evidence supersedes earlier current-state statements that the two E002 GGUFs had provider metadata only. It does not supersede any runtime, resource, access, A15, or execution blocker.