# Spec 005 — Qwen3.5-0.8B-Base Exact Public Binding Evidence

**Lifecycle:** CLARIFY ONLY
**Evidence capture date:** 2026-08-23
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`
**Candidate:** `Qwen/Qwen3.5-0.8B-Base`

> Read-only public metadata capture only. No model weights were downloaded, no model was executed, no benchmark payload was accessed, and no provider/gated action was performed.

## 1. Immutable upstream revision

```text
UPSTREAM_REPOSITORY=Qwen/Qwen3.5-0.8B-Base
UPSTREAM_REVISION=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
REVISION_TYPE=IMMUTABLE_GIT_COMMIT
MODEL_STATUS=PRETRAINED_ONLY_BASE
LICENSE_METADATA=apache-2.0
```

The exact revision tree exposes the model weights/configuration, tokenizer artifacts, processor configuration, and a root `LICENSE` file. No root `NOTICE` file was observed in the exact revision tree during this capture.

## 2. Exact model-weight content identity

Public Hugging Face Xet metadata for the base safetensors file reports:

```text
ARTIFACT_PATH=model.safetensors-00001-of-00001.safetensors
ARTIFACT_REVISION=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
SHA256=c2b1e5a17d9c1e27685d92ed9b382911ebb99955ecd89052d1721241adfbab6c
XET_HASH=0a75fae984a2baafa5ee5b256274748f8589e950f788b1f877ec6d2da891aa67
INDEX_METADATA_TOTAL_SIZE_BYTES=1746882752
```

The model index at the same revision maps model and visual components to this exact safetensors artifact. The content hash was read from public metadata; the weight file itself was not downloaded.

## 3. Exact tokenizer identity

Public Hugging Face Xet metadata at the same immutable revision reports:

```text
ARTIFACT_PATH=tokenizer.json
ARTIFACT_REVISION=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
SHA256=fe000e3ed39ed12b8d2481d527d44f93c65d37e87645d2dcc80d1bf9d50d2927
XET_HASH=59036b7ec9c1c130de9dd3716f37308a51038389ae6fb9ba62e87c246696707a
REMOTE_SIZE_APPROX=12.8_MB
```

The exact revision also contains:

```text
config.json
tokenizer_config.json
preprocessor_config.json
video_preprocessor_config.json
vocab.json
merges.txt
model.safetensors.index.json
```

Those paths are bound by the immutable revision locator even where an individual content digest has not yet been captured in this clarification artifact.

## 4. License evidence at the exact revision

```text
LICENSE_PATH=LICENSE
LICENSE_REVISION=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
LICENSE=Apache-2.0
ROOT_NOTICE_FILE_OBSERVED=NO
```

The exact revision contains the standard Apache License 2.0 text. Relevant permission/obligation classes include:

- reproduce and prepare derivative works;
- distribute the work or derivative works in source or object form;
- provide recipients a copy of the license;
- mark modified files with prominent change notices;
- retain applicable copyright, patent, trademark, and attribution notices;
- propagate a NOTICE file if the upstream work includes one.

No root `NOTICE` file was observed in the exact revision tree. This does **not** prove that no attribution or third-party notice obligations exist elsewhere in the repository or dependency/toolchain lineage; component-level review remains required.

## 5. Model-card intended-use observation

The official model card explicitly describes this repository as the **pre-trained only** model. It states intended use cases including fine-tuning, in-context learning experiments, and other research/development purposes rather than direct interaction.

This is useful admission context but does not replace the license, Spec 003 declared-use adjudication, safety qualification, or future commandMed release claims review.

## 6. Exact-base GGUF feasibility evidence

A public exact-base GGUF conversion exists at `ggml-org/Qwen3.5-0.8B-Base-GGUF`.

```text
SOURCE_MODEL=Qwen/Qwen3.5-0.8B-Base
GGUF_FILE=Qwen3.5-0.8B-Base-Q4_0.gguf
QUANTIZATION=Q4_0
OBSERVED_SIZE=563_MB
SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
```

This is feasibility evidence that an exact-base Q4-class GGUF path can fit below the frozen `700 MiB` hard ceiling and `<=600 MiB` engineering target. It is **not** the future commandMed canonical conversion, does not establish Q4 quality/safety equivalence, and does not authorize model conversion or execution.

## 7. Preliminary Spec 003 mapping

Canonical commandMed lineage identity:

```text
LINEAGE_CONTRACT_IDENTITY=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
```

Read-only evidence now supports strong exact-binding inputs for the upstream revision, base weight artifact, tokenizer artifact, and Apache-2.0 license text. However, **no canonical lineage evaluator result is asserted here**.

Remaining blockers by intended use:

| Declared use | Clarification status | Remaining blockers |
|---|---|---|
| `DEVELOPMENT_EVALUATION` | plausible path to eligibility | complete exact rights/component record, required privacy/evidence fields, canonical evaluator result |
| `REDISTRIBUTION` | plausible path to eligibility | complete component/notices/attribution record, exact derivative artifact binding, canonical evaluator result |
| `MODIFICATION_OR_DERIVATION` | blocked pending full evidence | all redistribution/component evidence plus resolved contamination state/applicability and exact derivation binding |
| `TRAINING_OR_ADAPTATION` | not authorized by Spec 005 | separate lifecycle authority plus full lineage/contamination/data evidence |

Under Spec 003, `CONDITIONAL` or `UNRESOLVED` rights cannot produce `ELIGIBLE`, and exact-use eligibility is evaluator-owned. This document therefore records evidence inputs only.

## 8. Sources

- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/tree/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/blob/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68/LICENSE
- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/blob/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68/tokenizer.json
- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/blob/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68/model.safetensors.index.json
- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/blob/main/model.safetensors-00001-of-00001.safetensors
- https://huggingface.co/ggml-org/Qwen3.5-0.8B-Base-GGUF
- https://huggingface.co/ggml-org/Qwen3.5-0.8B-Base-GGUF/blob/main/Qwen3.5-0.8B-Base-Q4_0.gguf

## 9. Authority boundary

```text
CANDIDATE_SELECTED=NO
PRIMARY_ADMISSION=NOT_YET_COMPLETE
LINEAGE_EVALUATOR_RESULT=NOT_YET_COMPUTED
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
NEXT_LIFECYCLE_STEP=CLARIFY
```
