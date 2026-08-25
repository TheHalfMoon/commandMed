# Spec 005 — Qwen3-0.6B-Base Exact Public Binding Evidence

**Lifecycle:** CLARIFY ONLY
**Evidence capture date:** 2026-08-23
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`
**Candidate:** `Qwen/Qwen3-0.6B-Base`

> Read-only public metadata capture only. No model weights were downloaded, no model was executed, no conversion was performed, and no benchmark payload was accessed.

## 1. Immutable upstream revision

```text
UPSTREAM_REPOSITORY=Qwen/Qwen3-0.6B-Base
UPSTREAM_REVISION=d4e79cdcc24cc3dc566196f5af6ed5782c64e8f1
REVISION_TYPE=IMMUTABLE_GIT_COMMIT
MODEL_STATUS=BASE_PRETRAINED
LICENSE_METADATA=apache-2.0
PARAMETER_CLASS=0.6B
ARCHITECTURE=qwen3
```

The observed current immutable revision is the repository head whose latest commit adds assistant-mask support. The exact tree contains:

```text
README.md
config.json
generation_config.json
merges.txt
model.safetensors
tokenizer.json
tokenizer_config.json
vocab.json
```

The repository is a base/pretrained artifact and is distinct from the post-trained/instruction-capable `Qwen/Qwen3-0.6B` repository.

## 2. Exact weight identity from public metadata

```text
ARTIFACT_PATH=model.safetensors
OBSERVED_REMOTE_SIZE_APPROX=1.19_GB
SHA256=cd2a512003e2f9f3cd3c32a9c3573f820bb28c940f73c57b1ddaa983d9223eba
XET_HASH=2c465b10ceca99084a7d3d8451bd593ac1ea835f3516b7ccc7279b177351021f
```

This content identity was read from public Hugging Face Xet metadata. The weight artifact itself was not downloaded.

## 3. Tokenizer binding state

The exact immutable revision binds `tokenizer.json`, `tokenizer_config.json`, `vocab.json`, and `merges.txt` by repository path and commit identity.

An individual public tokenizer SHA-256 was not reliably captured during this clarification pass, so this artifact does **not** fabricate one.

```text
TOKENIZER_REVISION_BINDING=d4e79cdcc24cc3dc566196f5af6ed5782c64e8f1
TOKENIZER_CONTENT_SHA256=NOT_CAPTURED_YET
TOKENIZER_BINDING_STATUS=IMMUTABLE_REVISION_BOUND_CONTENT_DIGEST_PENDING
```

## 4. License evidence

The repository reports Apache-2.0 and exposes the standard Apache License 2.0 text.

Relevant permission/obligation classes include reproduction, derivative works, and distribution subject to the license's notice/attribution/modification requirements.

```text
LICENSE=Apache-2.0
ADDITIONAL_GATED_TERMS_FLOW_OBSERVED=NO
SPEC003_RIGHTS_RESULT=NOT_SELF_ASSERTED
```

As with Qwen3.5-0.8B, this is strong rights evidence but does not replace a complete Spec 003 exact-use record covering every required component and obligation.

## 5. Exact-base GGUF evidence

Official `ggml-org` conversion evidence:

```text
GGUF_REPOSITORY=ggml-org/Qwen3-0.6B-Base-GGUF
BASE_MODEL=Qwen/Qwen3-0.6B-Base
OBSERVED_VARIANT=Q8_0
FILE=Qwen3-0.6B-Base-Q8_0.gguf
SIZE=639_MB
SHA256=ebb25a17e79b1f43834410fb711ac3dc985364eb875b45914181f55b9993f2d0
XET_HASH=d84beddfc42a177a5290085e2b6f09cbccda72ac8cea4c1f2cefba6f3a67c891
LLAMA_CPP_USAGE_DOCUMENTED=YES
```

The same official conversion repository exposes BF16 at approximately 1.2 GB.

At this evidence-capture point, no exact-base Q5/Q4 artifact was observed in the `ggml-org` repository. Therefore:

- exact-base Q8_0 639 MB is valid feasibility evidence;
- Q4 sizes from `Qwen/Qwen3-0.6B` must **not** be substituted as exact-base evidence;
- commandMed may hypothesize that a later authorized Q5/Q4 conversion could be smaller, but must not record a fabricated size or use it in qualification before exact artifact identity exists.

The remarkable result is that the exact-base Q8_0 artifact already sits below the frozen Spec 005 `700 MiB` hard ceiling.

## 6. Comparative implication versus Qwen3.5-0.8B-Base

Known size evidence is not directly apples-to-apples:

```text
Qwen3-0.6B-Base:
  exact-base public evidence=Q8_0 639 MB

Qwen3.5-0.8B-Base:
  exact-base public evidence=Q4_0 563 MB
```

Therefore Spec 005 must not conclude that the 0.6B candidate has a larger canonical deployable package. It has simply been observed at a higher-bit exact-base quantization. A frozen equal-method Q5/Q4 conversion ladder is required before package-size ranking.

The candidate's smaller parameter class and text-only Qwen3 architecture make it a serious mass-distribution contender, but medical/safety/Arabic capability must decide whether that capacity is sufficient.

## 7. Preliminary Spec 003 mapping

```text
LINEAGE_CONTRACT_IDENTITY=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
```

No canonical evaluator result is asserted.

| Declared use | Clarification evidence state | Remaining blockers |
|---|---|---|
| `DEVELOPMENT_EVALUATION` | plausible path | complete component rights/notices/privacy evidence + evaluator record |
| `REDISTRIBUTION` | plausible path | exact derivative identity + complete redistribution obligations + evaluator record |
| `MODIFICATION_OR_DERIVATION` | blocked pending full evidence | exact rights plus contamination applicability/state and derivation binding |
| `TRAINING_OR_ADAPTATION` | not authorized by Spec 005 | separate lifecycle authority + complete model/data lineage and contamination evidence |

## 8. Current admission disposition

```text
BASE_GATE=PUBLICLY_SUPPORTED
LICENSE_METADATA_GATE=PUBLICLY_SUPPORTED_APACHE_2_0
GATED_ACCESS_OBSERVED=NO
EXACT_WEIGHT_CONTENT_IDENTITY=CAPTURED
TOKENIZER_IMMUTABLE_REVISION_BINDING=CAPTURED
TOKENIZER_CONTENT_DIGEST=NOT_YET_CAPTURED
EXACT_BASE_GGUF_Q8_0_UNDER_700_MiB=YES
EXACT_BASE_Q4_PUBLIC_EVIDENCE=NOT_OBSERVED
MEDICAL_QUALITY_GATE=UNRESOLVED
SAFETY_GATE=UNRESOLVED
ARABIC_CLINICAL_PARITY_GATE=UNRESOLVED
SPEC003_LINEAGE_RESULT=NOT_YET_COMPUTED
PRIMARY_ADMISSION=NOT_YET_COMPLETE
CANDIDATE_SELECTED=NO
```

## 9. Sources

- https://huggingface.co/Qwen/Qwen3-0.6B-Base/tree/d4e79cdcc24cc3dc566196f5af6ed5782c64e8f1
- https://huggingface.co/Qwen/Qwen3-0.6B-Base/blob/main/model.safetensors
- https://huggingface.co/Qwen/Qwen3-0.6B-Base/blame/main/LICENSE
- https://huggingface.co/ggml-org/Qwen3-0.6B-Base-GGUF
- https://huggingface.co/ggml-org/Qwen3-0.6B-Base-GGUF/blob/main/Qwen3-0.6B-Base-Q8_0.gguf

## 10. Authority boundary

```text
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
NEXT_LIFECYCLE_STEP=CLARIFY
```
