# E004 Successor Candidate-Artifact Bundle Binding V1 — 2026-09-06

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v35-2026-09-06.md`
**Canonical base at branch creation:** `407c296092ee5759ee494dc7a44be10fdefd157e`
**Artifact class:** deterministic non-executing control-plane binding
**Authority effect:** none beyond the dependency-safe non-executing continuation directed by the Founder
**Model execution effect:** NONE
**A15 effect:** NONE
**Training authority:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Close only the V35 candidate-artifact `complete_bundle_sha256` / `complete_bundle_bytes` dependency using exact byte identities already established by canonical E002 and subject-metadata evidence.

This unit does not claim runtime-format compatibility, runtime argv, execution-plan identity, resource/access/environment PASS, A1-A14 PASS, A15 activation, a live pre-execution subject, model execution, tournament execution, winner selection, or training authority.

## 2. Identity semantics

`complete_bundle_sha256` is defined as the semantic canonical SHA-256 of one closed candidate file-manifest record after removing its own `complete_bundle_sha256` field.

```text
COMPLETE_BUNDLE_SEMANTICS=CANONICAL_FILE_MANIFEST_SHA256_V1
BUNDLE_SET_ID=SP007_RO_001_CANDIDATE_ARTIFACT_BUNDLE_SET_V1
BUNDLE_SET_SHA256=ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd
```

The digest is not represented as a monolithic archive-byte SHA when no such canonical archive exists. `complete_bundle_bytes` is the exact integer sum of the manifest's listed files.

Runtime archive/package identity remains separate because the canonical pre-execution subject already carries independent runtime artifact, executable, source revision, build-toolchain, compatibility, execution-plan, and argv fields. The PRIMARY 700 MiB hard cap therefore remains a candidate-package reach constraint and is not silently redefined to include an external runtime installation.

## 3. Exact candidate bundle bindings

```text
QWEN06_COMPLETE_BUNDLE_SHA256=8b207e94ad7c5937dceced686603294ae5f150022ac2b355fee9997a408fc415
QWEN06_COMPLETE_BUNDLE_BYTES=408195248
QWEN06_PRIMARY_HARD_CAP_MARGIN_BYTES=325807952

QWEN35_COMPLETE_BUNDLE_SHA256=682ef5c8fb914feb5346d5153e26b83e6bb3bb834aa1313cba240b61c0657592
QWEN35_COMPLETE_BUNDLE_BYTES=585938673
QWEN35_PRIMARY_HARD_CAP_MARGIN_BYTES=148064527

GRANITE_COMPLETE_BUNDLE_SHA256=90c8061eefbe53328a9eb217d1163941a16387d5a078dc789dbccb159c0b41db
GRANITE_COMPLETE_BUNDLE_BYTES=714515562
GRANITE_PRIMARY_HARD_CAP_MARGIN_BYTES=19487638

CONTROL_COMPLETE_BUNDLE_SHA256=9d4e39cdff26b357a698371b4096167a7b70f07975d016460e4b7996399170b9
CONTROL_COMPLETE_BUNDLE_BYTES=8056508630
CONTROL_PRIMARY_HARD_CAP_APPLIES=NO
```

The two Qwen GGUF bundles combine the exact byte-verified preconverted model artifact with the exact frozen upstream config/tokenizer surface captured by the subject-metadata evidence lane. Granite and CONTROL preserve the exact selected source-file sets previously materialized and rehashed by canonical run `33183096268`.

## 4. CONTROL composite model-artifact identity

The CONTROL source model is physically represented by three safetensors weight shards rather than one weight file. The pre-execution subject still requires one `model_artifact_sha256` and one `model_artifact_bytes` identity.

For this bounded binding, the CONTROL model-artifact identity is therefore a deterministic canonical manifest over only the exact weight-shard tuples `{path, bytes, sha256}`:

```text
CONTROL_MODEL_ARTIFACT_IDENTITY_KIND=CANONICAL_WEIGHT_SHARD_MANIFEST_SHA256_V1
CONTROL_MODEL_ARTIFACT_SHA256=d7daa1f7a5f70276b29b71838f8e2c830a61f06b4e70c04de0987bd8c5b4a397
CONTROL_MODEL_ARTIFACT_BYTES=8044982000
CONTROL_WEIGHT_SHARD_COUNT=3
```

This does not invent a byte digest for a nonexistent concatenated file and does not claim that the model index `total_size` equals physical container bytes.

## 5. Fail-closed invariants

The validator requires:

- the exact frozen E001 four-candidate set and deterministic order;
- exact PRIMARY/CONTROL roles and winner eligibility;
- closed fields with no runtime/execution fields admitted into this artifact schema;
- exact public/ungated artifact access state;
- safe unique POSIX-relative file paths in deterministic order;
- positive integer byte sizes with booleans rejected;
- lowercase SHA-256 file identities;
- exact tokenizer-config binding to one listed `TOKENIZER_CONFIG` file;
- exact single-file or canonical multi-shard model-artifact identity;
- exact `complete_bundle_bytes == sum(files[].bytes)`;
- exact canonical bundle self-hash and exact canonical four-bundle set self-hash;
- noncompensable PRIMARY `734003200` byte hard cap;
- CONTROL exemption from only that PRIMARY hard cap.

## 6. Explicit exclusions

```text
MODEL_LOAD=PROHIBITED_BY_THIS_UNIT
MODEL_INFERENCE=PROHIBITED_BY_THIS_UNIT
TOURNAMENT_EXECUTION=PROHIBITED_BY_THIS_UNIT
MODEL_CONVERSION=PROHIBITED_BY_THIS_UNIT
RUNTIME_FORMAT_COMPATIBILITY_PASS=NOT_CREATED
RUNTIME_ARGV=NOT_DEFINED
EXECUTION_PLAN_SHA256=NOT_DEFINED
RESOURCE_BINDING_PASS=NOT_CREATED
ACCESS_BINDING_PASS=NOT_CREATED
ENVIRONMENT_BINDING_PASS=NOT_CREATED
A1_A14_PASS_SNAPSHOT=NOT_CREATED
A15_ACTIVATION=NOT_AUTHORIZED
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
WINNER_SELECTION=NOT_PERFORMED
TRAINING_AUTHORITY=NONE
CREDENTIAL_USE=NO
PRIVATE_GOLD_ACCESS=NO
PHI_ACCESS=NO
SPEND_USD=0
```

Generic continuation authority must not be interpreted as A15 activation.

## 7. Qualification

This implementation extends the existing E004 research-component control-plane workflow rather than introducing a second qualification framework. Exact-head qualification must include:

```text
COMPILE_CHANGED_PYTHON=PASS_REQUIRED
FOCUSED_CANDIDATE_BUNDLE_TESTS=PASS_REQUIRED
FOCUSED_TOURNAMENT_TESTS=PASS_REQUIRED
FOCUSED_PREEXECUTION_TESTS=PASS_REQUIRED
SPEC007_REGRESSION=PASS_REQUIRED
FULL_REPOSITORY_REGRESSION=PASS_REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
```

Independent repository review is optional by default under FD-007 unless a later exact bounded authority requires it. No silent or skipped review is substantive review PASS.

## 8. Successor effect after qualified canonical merge

A later current-state reconciliation may close only:

```text
EXACT_COMPLETE_BUNDLE_SHA256_PER_CANDIDATE
EXACT_COMPLETE_BUNDLE_BYTES_PER_CANDIDATE
EXACT_CONTROL_COMPOSITE_MODEL_ARTIFACT_IDENTITY
```

All later V35 blockers remain fail closed until separately and genuinely satisfied.
