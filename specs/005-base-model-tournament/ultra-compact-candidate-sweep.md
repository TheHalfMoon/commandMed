# Spec 005 — Ultra-Compact Base Candidate Sweep

**Lifecycle:** CLARIFY ONLY
**Evidence capture date:** 2026-08-23
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`

> Read-only public discovery only. This artifact does not authorize model access, weight retrieval, gated-term acceptance, model conversion, inference, benchmark execution, training, or winner selection.

## 1. Purpose

Spec 005 has a frozen universal-low-resource objective and a `700 MiB` complete minimum text/core bundle ceiling. Before freezing the primary candidate manifest, commandMed must not assume that the best sub-1B choice is already known.

This sweep checks materially relevant base/pretrained candidates below 1B parameters against the current admission priorities:

1. base/pretrained checkpoint availability;
2. permissive/open release posture where publicly supportable;
3. no unresolved gated access for `PRIMARY` admission;
4. GGUF/llama.cpp feasibility;
5. realistic path below the frozen 700 MiB package ceiling without sub-4-bit release;
6. multilingual/Arabic plausibility because Arabic clinical parity is a canonical hard-gate metric;
7. no model popularity signal is used as a scientific ranking metric.

## 2. Material new finding — `Qwen/Qwen3-0.6B-Base`

`Qwen/Qwen3-0.6B-Base` is materially relevant and must be carried into admission reconciliation.

### Public exact identity

```text
UPSTREAM_REPOSITORY=Qwen/Qwen3-0.6B-Base
OBSERVED_CURRENT_REVISION=d4e79cdcc24cc3dc566196f5af6ed5782c64e8f1
MODEL_CLASS=BASE_PRETRAINED
MODEL_FAMILY=Qwen3
PARAMETER_CLASS=0.6B
LICENSE_METADATA=apache-2.0
PUBLIC_GATE_OBSERVED=NO_ADDITIONAL_TERMS_ACCEPTANCE_FLOW_IDENTIFIED
ARCHITECTURE=qwen3
```

The immutable revision tree contains the expected base artifact set including `model.safetensors`, `tokenizer.json`, `tokenizer_config.json`, `vocab.json`, `merges.txt`, configuration files, and the model card.

### Public exact weight content evidence

Current public Xet metadata for the base weight artifact reports:

```text
ARTIFACT_PATH=model.safetensors
REMOTE_SIZE_APPROX=1.19_GB
SHA256=cd2a512003e2f9f3cd3c32a9c3573f820bb28c940f73c57b1ddaa983d9223eba
XET_HASH=2c465b10ceca99084a7d3d8451bd593ac1ea835f3516b7ccc7279b177351021f
```

The hash was captured from public metadata. The weight artifact was not downloaded.

### Exact-base GGUF feasibility

Official `ggml-org` conversion evidence exists:

```text
GGUF_REPOSITORY=ggml-org/Qwen3-0.6B-Base-GGUF
BASE_MODEL=Qwen/Qwen3-0.6B-Base
Q8_0_SIZE=639_MB
Q8_0_SHA256=ebb25a17e79b1f43834410fb711ac3dc985364eb875b45914181f55b9993f2d0
Q8_0_XET_HASH=d84beddfc42a177a5290085e2b6f09cbccda72ac8cea4c1f2cefba6f3a67c891
BF16_SIZE=1.2_GB
LLAMA_CPP_USAGE_DOCUMENTED=YES
```

At the time of this read-only sweep, the official `ggml-org` exact-base conversion repository exposes BF16 and Q8_0, but no exact-base Q4 file was observed in that repository tree. This absence must not be filled by substituting Q4 evidence from the instruction/post-trained `Qwen/Qwen3-0.6B` artifact.

The exact-base **Q8_0 already fits below the frozen 700 MiB hard ceiling**, which is unusually strong feasibility evidence. A later authorized commandMed conversion may plausibly produce a much smaller Q5/Q4-class artifact, but that size must not be claimed before an exact conversion identity exists.

### Admission consequence

```text
BASE_GATE=PUBLICLY_SUPPORTED
LICENSE_METADATA_GATE=PUBLICLY_SUPPORTED_APACHE_2_0
GATED_ACCESS_OBSERVED=NO
EXACT_BASE_GGUF_Q8_0_UNDER_700_MiB=YES
Q4_EXACT_BASE_PUBLIC_EVIDENCE=NOT_OBSERVED_IN_GGML_ORG_REPO
MEDICAL_QUALITY_GATE=UNRESOLVED
ARABIC_CLINICAL_PARITY_GATE=UNRESOLVED
SAFETY_GATE=UNRESOLVED
SPEC003_LINEAGE_RESULT=NOT_YET_COMPUTED
PRIMARY_ADMISSION=NOT_YET_COMPLETE
```

**Disposition:** add as a top-tier `PRIMARY` admission candidate. It may ultimately be a stronger mass-distribution backbone than Qwen3.5-0.8B if it clears the same medical/safety/Arabic floor; no such conclusion is made in clarification.

## 3. `Qwen/Qwen3.5-0.8B-Base`

Existing exact-binding evidence is retained in `qwen-exact-binding-evidence.md`.

Current comparative facts:

```text
UPSTREAM_REVISION=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
PARAMETER_CLASS=0.8B
LICENSE_METADATA=apache-2.0
EXACT_BASE_Q4_0_SIZE=563_MB
EXACT_BASE_Q4_0_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
```

**Disposition:** retain as a top-tier `PRIMARY` admission candidate, especially as the current capability/newer-architecture challenger. Spec 005 must not choose between Qwen3 0.6B and Qwen3.5 0.8B using parameter count or public reputation alone.

## 4. `HuggingFaceTB/SmolLM2-360M`

### Public exact identity

```text
UPSTREAM_REPOSITORY=HuggingFaceTB/SmolLM2-360M
OBSERVED_REVISION=f8027fd0eaeea54caa13c31d31b9fdc459c38b49
MODEL_CLASS=BASE_PRETRAINED
PARAMETER_CLASS=360M
LICENSE_METADATA=apache-2.0
PRIMARY_LANGUAGE_METADATA=English
ARCHITECTURE=llama
```

The official model card describes SmolLM2 as an on-device-oriented compact family and explicitly states that the models **primarily understand and generate content in English**.

### GGUF feasibility

Multiple public exact-base conversions show a very small GGUF path. Representative community evidence:

```text
Q4_K_M_APPROX=271_MB
Q4_K_S_APPROX=260_MB
Q5_K_M_APPROX=290_MB
Q8_0_APPROX=386_MB
```

This is excellent package-size feasibility, but current commandMed admission is not size-only.

### Admission consequence

Canonical metrics include the hard gate `arabic_clinical_parity_gap`. Because the upstream model is explicitly English-primary, SmolLM2-360M must not be promoted into the frozen PRIMARY manifest merely for its 260–290 MB Q4/Q5 footprint.

```text
SIZE_FEASIBILITY=EXCELLENT
LICENSE_METADATA=APACHE_2_0
BASE_STATUS=YES
ARABIC_CLINICAL_PARITY_PRIOR=HIGH_RISK_UNRESOLVED
MEDICAL_QUALITY_GATE=UNRESOLVED
PRIMARY_ADMISSION=NOT_YET_SUPPORTED
ROLE=ULTRA_SMALL_CONTROL_OR_CONDITIONAL_COMPARATOR
```

It remains scientifically useful as a lower-bound size/control candidate and as evidence of how small a technically runnable base can be.

## 5. `google/gemma-3-270m`

Public metadata confirms a 270M pretrained Gemma 3 artifact, but the Hugging Face repository requires review/acceptance of Google's usage license before file/content access.

```text
UPSTREAM_REPOSITORY=google/gemma-3-270m
PARAMETER_CLASS=270M
MODEL_CLASS=PRETRAINED
LICENSE_METADATA=gemma
GATED_TERMS_ACCEPTANCE=YES
PUBLIC_WEIGHT_PREVIEW_SIZE=536_MB
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

A related QAT Q4_0 repository remains under the same gated access posture.

**Disposition:** `CONDITIONAL`; exclude from the frozen PRIMARY manifest while gated/license compatibility is unresolved. Do not accept terms merely to investigate it.

## 6. `swiss-ai/Apertus-v1.1-0.5B`

Apertus remains the strongest observed pure package-size challenger at approximately 306 MB Q4_K_M in public community conversion evidence. However, the official repository metadata includes the Apertus Acceptable Use Policy and a terms-acceptance field.

**Disposition:** `CONDITIONAL` size comparator; not eligible for frozen PRIMARY admission while rights/access remain conditional.

## 7. Current ultra-compact field after sweep

| Candidate | Size class | Base | Public license/access posture | Strongest package evidence currently captured | Current Spec 005 role |
|---|---:|---|---|---:|---|
| `Qwen/Qwen3-0.6B-Base` | 0.6B | Yes | Apache-2.0; no extra gate found | exact-base Q8_0 639 MB | Top-tier PRIMARY admission candidate |
| `Qwen/Qwen3.5-0.8B-Base` | 0.8B | Yes | Apache-2.0; no extra gate found | exact-base Q4_0 563 MB | Top-tier PRIMARY admission candidate |
| `HuggingFaceTB/SmolLM2-360M` | 0.36B | Yes | Apache-2.0 | Q4_K_M ~271 MB | Ultra-small control/conditional due English-primary limitation |
| `swiss-ai/Apertus-v1.1-0.5B` | 0.5B | Yes | Apache-2.0 metadata + gated AUP terms | Q4_K_M ~306 MB | CONDITIONAL size comparator |
| `google/gemma-3-270m` | 0.27B | Yes | Gemma license + gated acceptance | upstream weight preview 536 MB | CONDITIONAL; no gated access authorized |

### Key clarification conclusion

There is **no defensible single winner yet**.

The cleanest current mass-distribution primary competition is at least:

```text
PRIMARY_ADMISSION_FRONTIER=
  Qwen/Qwen3-0.6B-Base
  Qwen/Qwen3.5-0.8B-Base
```

SmolLM2-360M is too important to ignore for size engineering but has an explicit English-primary limitation that directly conflicts with commandMed's Arabic hard-gate ambitions. Apertus and Gemma 270M remain conditional due additional gated/license terms.

## 8. Sources

- https://huggingface.co/Qwen/Qwen3-0.6B-Base/tree/d4e79cdcc24cc3dc566196f5af6ed5782c64e8f1
- https://huggingface.co/Qwen/Qwen3-0.6B-Base/blob/main/model.safetensors
- https://huggingface.co/Qwen/Qwen3-0.6B-Base/blame/main/LICENSE
- https://huggingface.co/ggml-org/Qwen3-0.6B-Base-GGUF
- https://huggingface.co/ggml-org/Qwen3-0.6B-Base-GGUF/blob/main/Qwen3-0.6B-Base-Q8_0.gguf
- https://huggingface.co/HuggingFaceTB/SmolLM2-360M/tree/f8027fd0eaeea54caa13c31d31b9fdc459c38b49
- https://huggingface.co/QuantFactory/SmolLM2-360M-GGUF
- https://huggingface.co/google/gemma-3-270m
- https://huggingface.co/swiss-ai/Apertus-v1.1-0.5B

## 9. Authority boundary

```text
CANDIDATE_SELECTED=NO
PRIMARY_MANIFEST_FROZEN=NO
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
NEXT_LIFECYCLE_STEP=CLARIFY
```
