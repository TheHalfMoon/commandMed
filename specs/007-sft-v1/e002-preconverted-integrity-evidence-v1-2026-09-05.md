# E002 Exact Preconverted Artifact Integrity Evidence V1 — 2026-09-05

**Spec:** 007 SFT V1
**Scope:** exact E002 preconverted allowlist only
**Canonical base at branch creation:** `2a5ef156ae2606d36d8d6e817c35c7879a8fe22b`
**Artifact class:** inert workflow definition and pre-execution evidence plan
**Authority source:** `specs/007-sft-v1/e002-model-access-authorization-2026-08-27.md`
**Model execution:** PROHIBITED
**Conversion:** PROHIBITED
**Credentials:** PROHIBITED
**Artifact upload/cache:** PROHIBITED
**Current authorized spend:** USD 0

## Purpose

Create one bounded byte-integrity lane for the exact two preconverted artifacts already enumerated by canonical E002 authority. The workflow is inert for byte acquisition during pull-request review. After canonical merge, one exact evidence-branch marker push may materialize each file ephemerally, recompute its integer byte count and SHA-256, inspect only the four-byte GGUF container magic, and emit repository-safe evidence to workflow logs.

## Exact authorized artifacts

```text
QWEN06_REPOSITORY=Antigma/Qwen3-0.6B-Base-GGUF
QWEN06_REVISION=f457544766bcdc72afd3514439eb3d422d4434dc
QWEN06_FILENAME=qwen3-0.6b-base-q4_k_m.gguf
QWEN06_BYTES=396704512
QWEN06_SHA256=218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492

QWEN35_REPOSITORY=ggml-org/Qwen3.5-0.8B-Base-GGUF
QWEN35_REVISION=1bd44f68963429437d08bc12f465716eb31ba6e5
QWEN35_FILENAME=Qwen3.5-0.8B-Base-Q4_0.gguf
QWEN35_BYTES=563035840
QWEN35_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
```

No adjacent repository file, different quantization, different revision, or other preconverted artifact is admitted.

## Pull-request qualification boundary

On `pull_request`, only the `static-qualification` job is eligible. It binds the exact PR head to the canonical E002 authority, verifies both allowlist identities, verifies the no-load/no-conversion/no-credential/no-spend policy strings, and runs `git diff --check`.

```text
PULL_REQUEST_BYTE_ACQUISITION=PROHIBITED_BY_JOB_CONDITION
PULL_REQUEST_MODEL_LOAD=NO
PULL_REQUEST_MODEL_EXECUTION=NO
PULL_REQUEST_CONVERSION=NO
```

## Post-merge execution boundary

Byte acquisition jobs are eligible only for:

```text
BRANCH=evidence/e002-preconverted-integrity-run-v1
MARKER=.github/e002-preconverted-integrity-run-v1.txt
EVENT=push
```

Each job must:

1. unset `HF_TOKEN`, `HUGGING_FACE_HUB_TOKEN`, `GH_TOKEN`, and `GITHUB_TOKEN` inside the acquisition shell;
2. download only the exact immutable-revision file through public HTTPS;
3. recompute integer bytes and SHA-256;
4. require exact equality with the canonical E002 values;
5. require static container magic `GGUF`;
6. upload/cache nothing;
7. load or execute no model or runtime;
8. perform no conversion, benchmark access, winner selection, training, credential use, procurement, payment, or spend.

## Evidence semantics

A successful post-merge run may establish only:

```text
EXACT_PRECONVERTED_BYTE_INTEGRITY=PASS_ON_EPHEMERAL_RUNNER
STATIC_CONTAINER_MAGIC=GGUF
PERSISTENT_ARTIFACT_PRESENT=NO
RUNTIME_COMPATIBILITY_PASS=NO
MODEL_EXECUTION_PASS=NO
RESOURCE_PREFLIGHT_PASS=NO
A15_PASS=NO
TOURNAMENT_PASS=NO
WINNER_SELECTED=NO
```

The exact runtime and complete execution subject remain separate dependencies.
