# Spec 005 — Candidate Admission Evidence

**Lifecycle:** CLARIFY ONLY
**Evidence capture date:** 2026-08-23
**Canonical repository base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`
**Purpose:** read-only public-source candidate admission reconciliation for Spec 005.

> This document is evidence capture, not an execution manifest, winner selection, model-access authorization, weight-download authorization, benchmark authorization, or permission to accept gated terms. No model weights were downloaded, no model was executed, no benchmark payload was opened, and no gated terms were accepted while producing this artifact.

## 1. Frozen clarification policies relevant to this evidence

```text
BASE_ONLY_PRIMARY
COMMON_CORE_PRIMARY_RANKING
FULLY_ADMITTED_PRIMARY_ONLY
DUAL_BUILD_BASELINE_AND_DEPLOYABLE
QUALITY_FLOOR_THEN_SIZE_FIRST
SUB_700MB_MASS_REACH
GGUF_LLAMA_CPP_CANONICAL
Q4_FLOOR_SMALLEST_PASSING
```

Mass-reach boundaries currently frozen by clarification:

```text
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_HARD_CEILING=700_MiB
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_ENGINEERING_TARGET=600_MiB_OR_LESS
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_STRETCH_TARGET=500_MiB_OR_LESS_IF_HARD_GATES_PASS
PEAK_WORKING_RAM_ENGINEERING_TARGET=2_GiB_OR_LESS_AT_FROZEN_SHORT_CONTEXT
LOW_RESOURCE_PHONE_TEST_ENVELOPE=4_GB_CLASS
CANONICAL_MINIMUM_DISTRIBUTION_ARTIFACT=GGUF
CANONICAL_RUNTIME_FAMILY=LLAMA_CPP
SUB4BIT_PRIMARY_CANONICAL_RELEASE=PROHIBITED
```

## 2. Tier A ultra-compact candidates

### 2.1 `swiss-ai/Apertus-v1.1-0.5B`

**Admission role:** ultra-compact `PRIMARY` admission candidate; current package-size leader for admission research.

**Public observation:**

```text
UPSTREAM_REPOSITORY=swiss-ai/Apertus-v1.1-0.5B
OBSERVED_UPSTREAM_REVISION=1b7276176e564fc0cc7d7c3b991a8d653c8b8792
MODEL_STATUS=BASE_PRETRAINED_NO_SFT_OR_ALIGNMENT
LICENSE_METADATA=Apache-2.0
PUBLIC_ACCESS_OBSERVATION=UNGATED_PUBLIC_REPOSITORY
MODEL_CARD_NOMINAL_FAMILY_SIZE=0.5B
MODEL_CARD_COMPUTE_STORAGE_PARAMETERS=0.4B/0.4B
```

The official model card describes Apertus-v1.1 as a 0.5–4B family designed for highly constrained hardware, created using pre-training distillation from Apertus-8B-2509. The 0.5B artifact is explicitly described as a base model that has not undergone SFT or alignment. The card also states open weights, open data, training details, and Apache-2.0 licensing metadata.

**Observed GGUF feasibility evidence:**

```text
COMMUNITY_GGUF_REPOSITORY=NonMiFrega/Apertus-v1.1-0.5B-Q4_K_M-GGUF
SOURCE_MODEL=swiss-ai/Apertus-v1.1-0.5B
QUANTIZATION=Q4_K_M
OBSERVED_MODEL_SIZE=306_MB
LLAMA_CPP_USAGE_DOCUMENTED=YES
```

This conversion is evidence that a Q4-class llama.cpp-compatible artifact can fit comfortably below the 700 MiB hard package ceiling. It is not commandMed's canonical future conversion and does not prove medical quality, safety, RAM, latency, thermal, battery, or compression-regression qualification.

**Admission disposition:**

```text
BASE_GATE=PUBLICLY_SUPPORTED
LICENSE_METADATA_GATE=PUBLICLY_SUPPORTED_APACHE_2_0
PUBLIC_ACCESS_GATE=PUBLICLY_UNGATED_AT_OBSERVATION
GGUF_SIZE_FEASIBILITY=STRONG
MEDICAL_QUALITY_GATE=UNRESOLVED
SAFETY_GATE=UNRESOLVED
SPEC003_LINEAGE_DISPOSITION=UNRESOLVED
TOKENIZER_EXACT_BINDING=PARTIAL_SAME_REPOSITORY_REVISION
DEVICE_EXECUTION_EVIDENCE=UNRESOLVED
PRIMARY_ADMISSION=NOT_YET_COMPLETE
```

### 2.2 `Qwen/Qwen3.5-0.8B-Base`

**Admission role:** ultra-compact `PRIMARY` admission candidate; current capability/ecosystem lead for admission research.

**Public observation:**

```text
UPSTREAM_REPOSITORY=Qwen/Qwen3.5-0.8B-Base
OBSERVED_UPSTREAM_REVISION=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
MODEL_STATUS=PRETRAINED_ONLY_BASE
LICENSE_METADATA=Apache-2.0
PUBLIC_ACCESS_OBSERVATION=UNGATED_PUBLIC_REPOSITORY
MODEL_SIZE_CLASS=0.8B
```

The official model card states that this repository contains weights and configuration for the pre-trained-only model. The current repository exposes an Apache-2.0 `LICENSE` file at the observed revision.

**Exact base GGUF feasibility evidence:**

A previous clarification note used size evidence from `bartowski/Qwen_Qwen3.5-0.8B-GGUF`, which is not the exact `-Base` artifact. That evidence is superseded here by an exact-base conversion from `ggml-org`.

```text
GGUF_REPOSITORY=ggml-org/Qwen3.5-0.8B-Base-GGUF
SOURCE_MODEL=Qwen/Qwen3.5-0.8B-Base
OBSERVED_QUANTIZATION=Q4_0
OBSERVED_FILE=Qwen3.5-0.8B-Base-Q4_0.gguf
OBSERVED_SIZE=563_MB
OBSERVED_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
LLAMA_CPP_USAGE_DOCUMENTED=YES
```

The same exact-base GGUF repository also exposes BF16 and Q8_0 variants. The Q4_0 artifact is below both the 700 MiB hard ceiling and the <=600 MiB engineering target. It is feasibility evidence only; the final commandMed quantization ladder, converter revision, llama.cpp revision, conversion flags, optional imatrix/calibration policy, and commandMed-produced artifact identity remain unresolved.

**Admission disposition:**

```text
BASE_GATE=PUBLICLY_SUPPORTED
LICENSE_METADATA_GATE=PUBLICLY_SUPPORTED_APACHE_2_0
PUBLIC_ACCESS_GATE=PUBLICLY_UNGATED_AT_OBSERVATION
GGUF_SIZE_FEASIBILITY=STRONG
MEDICAL_QUALITY_GATE=UNRESOLVED
SAFETY_GATE=UNRESOLVED
SPEC003_LINEAGE_DISPOSITION=UNRESOLVED
TOKENIZER_PROCESSOR_EXACT_BINDING=PARTIAL_SAME_REPOSITORY_REVISION
DEVICE_EXECUTION_EVIDENCE=UNRESOLVED
PRIMARY_ADMISSION=NOT_YET_COMPLETE
```

## 3. Medical reference/control

### `google/medgemma-4b-pt`

**Role:** medical quality reference/control; not a current V1 `PRIMARY` mass-distribution candidate.

**Public observation:**

```text
UPSTREAM_REPOSITORY=google/medgemma-4b-pt
OBSERVED_PUBLIC_README_REVISION=1b7b4a7e462da7ab2bc40591ec86ca449edc388a
MODEL_STATUS=PRETRAINED_MEDICAL_BASE
LICENSE_METADATA=health-ai-developer-foundations
ACCESS_STATUS=GATED_TERMS_REQUIRED
BASE_MODEL=google/gemma-3-4b-pt
```

The official Hugging Face page states that repository files/content require review and acceptance of Health AI Developer Foundations terms. Spec 005 clarification does not authorize accepting those terms or retrieving the weights.

The official card reports that MedGemma 4B is available in pre-trained and instruction-tuned variants and has medical training/evaluation across medical text and imaging tasks. This makes it scientifically valuable as a medical reference even though it is not eligible for the current mass-distribution `PRIMARY` role.

**Observed GGUF size evidence from a public community conversion:**

```text
REFERENCE_GGUF_REPOSITORY=mradermacher/medgemma-4b-pt-GGUF
Q2_K_APPROX=1.73_GB
IQ4_XS_APPROX=2.28_GB
Q4_K_S_APPROX=2.38_GB
Q4_K_M_APPROX=2.49_GB
OPTIONAL_MMPROJ_Q8_APPROX=0.7_GB
OPTIONAL_MMPROJ_F16_APPROX=1.0_GB
```

Even the observed Q2-class artifact is far above the frozen 700 MiB hard ceiling, and Spec 005 separately prohibits sub-4-bit artifacts as the V1 `PRIMARY` canonical release. Therefore MedGemma 4B cannot satisfy the present V1 mass-distribution package contract.

**Reference disposition:**

```text
MEDICAL_REFERENCE_VALUE=HIGH
PRIMARY_BASE_STATUS=BASE_CHECKPOINT_EXISTS
FD001_PERMISSIVE_RELEASE_ALIGNMENT=NOT_PROVEN
GATED_ACCESS=YES
MASS_REACH_700_MiB_GATE=FAIL_BY_PUBLIC_SIZE_FEASIBILITY
V1_PRIMARY_ROLE=INELIGIBLE_UNDER_CURRENT_CONTRACT
REFERENCE_CONTROL_ROLE=RETAIN
ACCESS_OR_EXECUTION_AUTHORITY=NONE
```

### `google/medgemma-1.5-4b-it`

The current MedGemma 1.5 release is explicitly described by Google as available only as a 4B multimodal instruction-tuned variant. It therefore fails `BASE_ONLY_PRIMARY` independently of its gated Health AI Developer Foundations access terms and size. It remains useful only as a separately authorized reference/control artifact.

## 4. Current comparative admission picture

| Candidate | Base eligible? | Public license metadata | Public gate | Exact/base GGUF feasibility observed | Current role |
|---|---|---|---|---|---|
| `swiss-ai/Apertus-v1.1-0.5B` | Yes | Apache-2.0 | No gate observed | Q4_K_M ~306 MB community conversion | Tier A PRIMARY admission candidate / size leader |
| `Qwen/Qwen3.5-0.8B-Base` | Yes | Apache-2.0 | No gate observed | Exact-base Q4_0 563 MB; SHA-256 captured | Tier A PRIMARY admission candidate / capability-ecosystem lead |
| `google/medgemma-4b-pt` | Base exists | Health AI Developer Foundations | Gated | Q4_K_M ~2.49 GB; Q2 ~1.73 GB | Medical reference/control |
| `google/medgemma-1.5-4b-it` | No (`-it` only for 1.5) | Health AI Developer Foundations | Gated | Multi-GB family | Reference/control only |

No row in this table is a winner selection. Apertus and Qwen remain incomplete until all admission gates, medical/safety floors, Spec 003 lineage disposition, exact tokenizer/processor binding, contamination/quarantine evidence, and authorized device/runtime evidence are complete.

## 5. Why Apertus and Qwen both remain necessary

The current evidence supports a two-anchor ultra-compact tournament rather than premature selection:

- **Apertus 0.5B** establishes the strongest current public package-size opportunity. Its ~306 MB Q4_K_M conversion is substantially below the stretch target, leaving headroom for tokenizer/config/metadata and potentially for future application packaging.
- **Qwen3.5 0.8B Base** establishes the stronger current ecosystem/capability hypothesis while still fitting the frozen package envelope with an exact-base 563 MB Q4_0 conversion.
- **MedGemma 4B PT** provides a medical-specialization reference that the eventual commandMed model should be compared against where protocol and access are separately authorized, but it cannot satisfy the current V1 mass-distribution contract.

The tournament must answer whether Apertus retains enough medical capability after commandMed's later authorized specialization, or whether the larger Qwen backbone is required to clear the same frozen medical/safety floor. Package size alone cannot answer that question.

## 6. Public sources captured

Primary/official sources:

- https://huggingface.co/swiss-ai/Apertus-v1.1-0.5B
- https://huggingface.co/swiss-ai/Apertus-v1.1-0.5B/commit/1b7276176e564fc0cc7d7c3b991a8d653c8b8792
- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base
- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/commit/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
- https://huggingface.co/google/medgemma-4b-pt
- https://huggingface.co/google/medgemma-1.5-4b-it

Read-only conversion/feasibility sources:

- https://huggingface.co/NonMiFrega/Apertus-v1.1-0.5B-Q4_K_M-GGUF
- https://huggingface.co/ggml-org/Qwen3.5-0.8B-Base-GGUF
- https://huggingface.co/ggml-org/Qwen3.5-0.8B-Base-GGUF/blob/main/Qwen3.5-0.8B-Base-Q4_0.gguf
- https://huggingface.co/mradermacher/medgemma-4b-pt-GGUF

## 7. Remaining admission work

The following remain unresolved and must be completed before a future frozen `PRIMARY` manifest can exist:

1. exact Spec 003 lineage disposition for each intended use;
2. exact tokenizer/processor artifact binding and notices at the chosen immutable candidate revision;
3. complete license/NOTICE/attribution obligations for source, tokenizer, converter, runtime, and final derivative;
4. contamination/quarantine proof;
5. frozen minimum medical-quality and safety gates;
6. exact benchmark/metric slices and access mechanism;
7. exact reference precision and deployable Q5/Q4 ladder;
8. immutable GGUF converter and llama.cpp revisions plus flags;
9. named iPhone, Android, 4-GB-class phone/resource, and weak-laptop evidence environments;
10. exact context/KV/RAM/latency/throughput/energy/thermal protocols;
11. independent exact-head review before any execution-activation proposal.

```text
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```
