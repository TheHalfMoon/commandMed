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

## 2. Ultra-compact candidates

### 2.1 `Qwen/Qwen3.5-0.8B-Base`

**Admission role:** current cleanest ultra-compact `PRIMARY` admission lead. This is not a declaration of `ELIGIBLE` and is not a winner selection.

**Public observation:**

```text
UPSTREAM_REPOSITORY=Qwen/Qwen3.5-0.8B-Base
OBSERVED_UPSTREAM_REVISION=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
MODEL_STATUS=PRETRAINED_ONLY_BASE
LICENSE_METADATA=Apache-2.0
PUBLIC_GATE_OBSERVED=NO_EQUIVALENT_TERMS_ACCEPTANCE_FLOW_IDENTIFIED
MODEL_SIZE_CLASS=0.8B
```

The official model card states that this repository contains weights and configuration for the pre-trained-only model. The repository exposes an Apache-2.0 `LICENSE` file at the observed revision. Current read-only inspection has not identified an Apertus/MedGemma-style extra gated terms-acceptance flow for this repository.

Absence of an observed gate is not by itself a complete Spec 003 rights adjudication. Exact component-level rights, tokenizer/processor rights, notices, and declared-use evidence still must be bound before evaluator-owned admission can become `ELIGIBLE`.

**Exact base GGUF feasibility evidence:**

A previous clarification note used size evidence from a non-`-Base` conversion. That evidence is superseded here by an exact-base conversion from `ggml-org`.

```text
GGUF_REPOSITORY=ggml-org/Qwen3.5-0.8B-Base-GGUF
SOURCE_MODEL=Qwen/Qwen3.5-0.8B-Base
OBSERVED_QUANTIZATION=Q4_0
OBSERVED_FILE=Qwen3.5-0.8B-Base-Q4_0.gguf
OBSERVED_SIZE=563_MB
OBSERVED_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
LLAMA_CPP_USAGE_DOCUMENTED=YES
```

The exact-base Q4_0 artifact is below both the 700 MiB hard ceiling and the <=600 MiB engineering target. It is feasibility evidence only; the final commandMed quantization ladder, converter revision, llama.cpp revision, conversion flags, optional imatrix/calibration policy, and commandMed-produced artifact identity remain unresolved.

**Admission disposition:**

```text
BASE_GATE=PUBLICLY_SUPPORTED
LICENSE_METADATA_GATE=PUBLICLY_SUPPORTED_APACHE_2_0
PUBLIC_GATE_OBSERVATION=CLEANER_THAN_APERTUS_AND_MEDGEMMA
GGUF_SIZE_FEASIBILITY=STRONG
MEDICAL_QUALITY_GATE=UNRESOLVED
SAFETY_GATE=UNRESOLVED
SPEC003_LINEAGE_DISPOSITION=NOT_YET_COMPUTED
TOKENIZER_PROCESSOR_EXACT_BINDING=PARTIAL_SAME_REPOSITORY_REVISION
DEVICE_EXECUTION_EVIDENCE=UNRESOLVED
PRIMARY_ADMISSION=NOT_YET_COMPLETE
```

### 2.2 `swiss-ai/Apertus-v1.1-0.5B`

**Admission role:** `CONDITIONAL` ultra-compact package-size comparator; **not eligible for the future frozen `PRIMARY` manifest while its additional terms/access posture is unresolved**.

**Public observation:**

```text
UPSTREAM_REPOSITORY=swiss-ai/Apertus-v1.1-0.5B
OBSERVED_UPSTREAM_REVISION=1b7276176e564fc0cc7d7c3b991a8d653c8b8792
MODEL_STATUS=BASE_PRETRAINED_NO_SFT_OR_ALIGNMENT
LICENSE_METADATA=Apache-2.0
EXTRA_GATED_AUP_TERMS=YES
TERMS_ACCEPTANCE_FIELD=YES
GATED_ASSET_ACCESS_AUTHORITY=NONE
MODEL_CARD_NOMINAL_FAMILY_SIZE=0.5B
MODEL_CARD_COMPUTE_STORAGE_PARAMETERS=0.4B/0.4B
```

The official model card describes Apertus-v1.1 as a 0.5–4B family designed for highly constrained hardware, created using pre-training distillation from Apertus-8B-2509. The 0.5B artifact is explicitly described as a base model that has not undergone SFT or alignment.

A material access/rights correction was discovered after the first evidence capture: although the metadata reports `license: apache-2.0`, official README metadata also includes `extra_gated_prompt` containing the **Apertus LLM Acceptable Use Policy** and `extra_gated_fields` containing an explicit checkbox to accept terms of use. The policy includes additional obligations/conditions beyond the bare Apache-2.0 metadata.

Therefore the previous statement `PUBLIC_ACCESS_OBSERVATION=UNGATED_PUBLIC_REPOSITORY` was incorrect and is superseded by this record. Under Spec 003, conditional or unresolved rights cannot produce `ELIGIBLE`, and `FULLY_ADMITTED_PRIMARY_ONLY` forbids carrying this unresolved candidate into the frozen primary manifest.

No Apertus gated terms were accepted and no Apertus weights were accessed while producing this evidence.

**Observed GGUF feasibility evidence:**

```text
COMMUNITY_GGUF_REPOSITORY=NonMiFrega/Apertus-v1.1-0.5B-Q4_K_M-GGUF
SOURCE_MODEL=swiss-ai/Apertus-v1.1-0.5B
QUANTIZATION=Q4_K_M
OBSERVED_MODEL_SIZE=306_MB
LLAMA_CPP_USAGE_DOCUMENTED=YES
```

This conversion is evidence that a Q4-class llama.cpp-compatible artifact can fit comfortably below the 700 MiB hard package ceiling. It does not remove or supersede upstream terms and is not commandMed's canonical future conversion. It also proves nothing about medical quality, safety, RAM, latency, thermal, battery, or compression-regression qualification.

**Admission disposition:**

```text
BASE_GATE=PUBLICLY_SUPPORTED
LICENSE_METADATA=APACHE_2_0
ADDITIONAL_TERMS=Apertus_LLM_Acceptable_Use_Policy
ACCESS_TERMS_ACCEPTANCE=REQUIRED_BY_OFFICIAL_MODEL_METADATA
RIGHTS_STATE_FOR_PRIMARY_INTENDED_USES=CONDITIONAL
GATED_ASSET_ACCESS_AUTHORITY=NONE
GGUF_SIZE_FEASIBILITY=VERY_STRONG
MEDICAL_QUALITY_GATE=UNRESOLVED
SAFETY_GATE=UNRESOLVED
SPEC003_LINEAGE_DISPOSITION=BLOCKED_PENDING_RIGHTS_RECONCILIATION
DEVICE_EXECUTION_EVIDENCE=UNRESOLVED
PRIMARY_MANIFEST_ELIGIBILITY=NO_WHILE_CONDITIONAL
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

## 4. Canonical Spec 003 implications

Canonical contract:

```text
LINEAGE_CONTRACT_IDENTITY=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
CONTRACT_ID=commandmed-lineage-contract-v1
SCHEMA_VERSION=1.0
```

Relevant exact semantics from `data/lineage/lineage_contract.json` and `src/commandmed/eval_contract/lineage.py`:

- evaluator-owned admission states are `ELIGIBLE`, `REFERENCE_ONLY`, `BLOCKED`, and `PROHIBITED`;
- exact binding is required for all governed uses except `REFERENCE`;
- `rights_state=CONDITIONAL` or `UNRESOLVED` cannot yield `ELIGIBLE`;
- `rights_state=INCOMPATIBLE` yields a prohibited result for the exact use;
- `access_class=REFERENCE_ONLY` prevents non-reference eligibility;
- source verification is distinct from exact artifact binding;
- `MODIFICATION_OR_DERIVATION`, `TRAINING_OR_ADAPTATION`, and `TEACHER_OR_SYNTHETIC_GENERATION` require a resolved clean-contamination state; only `ASSESSED_CLEAN` or an explicit, genuinely justified `NOT_APPLICABLE` may support eligibility;
- MedGemma/Health-AI-Developer-Foundations generator provenance is explicitly prohibited from becoming commandMed training lineage by omission.

### Preliminary intended-use disposition matrix

This table is a **clarification evidence assessment**, not output from the canonical evaluator. No synthetic record is labeled `ELIGIBLE` here.

| Candidate | `DEVELOPMENT_EVALUATION` | `MODIFICATION_OR_DERIVATION` (future quantization) | `REDISTRIBUTION` | Why not final yet |
|---|---|---|---|---|
| Qwen3.5-0.8B-Base | Potential path to eligibility; not yet computed | Blocked pending exact component rights + contamination applicability/state + exact derivation binding | Potential path to eligibility; not yet computed | exact component rights/notices/tokenizer binding/privacy fields and evaluator record remain incomplete |
| Apertus-v1.1-0.5B | `BLOCKED` while additional AUP/terms rights remain conditional | `BLOCKED` while rights are conditional; contamination rules also unresolved | `BLOCKED` while redistribution compatibility with additional AUP/terms is unresolved | official model metadata requires gated AUP terms acceptance; no authority to accept |
| MedGemma-4b-pt | reference/control only until separately authorized access | not eligible for current V1 role | incompatible with current V1 role/package posture | gated HAI-DEF terms + multi-GB package + canonical reference policy |

For Qwen, Apache-2.0 evidence is encouraging but **does not authorize us to self-assert `rights_state=SUPPORTED` for every component and use** without exact rights evidence. The canonical evaluator owns the final admission result.

For quantization, Spec 003 treats `MODIFICATION_OR_DERIVATION` as a use requiring a contamination state. The repository policy permits `NOT_APPLICABLE` only when truly outside the condition; this clarification does not invent that disposition. It remains a required evidence/rationale item before quantization lineage can become eligible.

## 5. Current comparative admission picture

| Candidate | Base eligible? | License/access observation | GGUF feasibility observed | Current role |
|---|---|---|---|---|
| `Qwen/Qwen3.5-0.8B-Base` | Yes | Apache-2.0 evidence; no equivalent gated flow found in current read-only inspection | Exact-base Q4_0 563 MB; SHA-256 captured | Current ultra-compact PRIMARY admission lead, not fully admitted |
| `swiss-ai/Apertus-v1.1-0.5B` | Base yes | Apache-2.0 metadata **plus gated Apertus AUP/terms acceptance** | Q4_K_M ~306 MB community conversion | CONDITIONAL size comparator; outside PRIMARY manifest while unresolved |
| `google/medgemma-4b-pt` | Base exists | HAI-DEF gated terms | Q4_K_M ~2.49 GB; Q2 ~1.73 GB | Medical reference/control |
| `google/medgemma-1.5-4b-it` | No (`-it` only for 1.5) | HAI-DEF gated terms | Multi-GB family | Reference/control only |

No row in this table is a winner selection. Qwen remains incomplete until every admission gate and medical/safety/device requirement is satisfied. Apertus cannot enter the frozen primary manifest while its exact intended-use rights are conditional.

## 6. Runtime compatibility evidence

### Apertus in llama.cpp

Historical upstream architecture support is established by:

```text
LLAMA_CPP_PR=ggml-org/llama.cpp#15852
TITLE=Feat: Apertus model implementation
MERGED_AT=2025-10-02
MERGE_COMMIT=34fcc5a4ace8c69476ef2ea3857f39a60334acc4
```

This proves Apertus architecture support landed upstream. It does not freeze the commandMed runtime revision and does not alter Apertus's conditional access/rights disposition.

### Qwen3.5 in llama.cpp

Current llama.cpp documentation and active upstream issue traffic show Qwen3.5 is an actively supported architecture family. This is ecosystem-feasibility evidence, not device qualification. Recent backend-specific Qwen3.5 regressions/issues reinforce the requirement to bind an immutable reviewed llama.cpp revision and test the exact named iPhone/Android/weak-laptop paths before making device claims.

No llama.cpp binary was installed or executed while producing this evidence.

## 7. Why Qwen leads and Apertus remains useful

The current evidence supports one clean primary-admission lead plus one important conditional size challenger:

- **Qwen3.5 0.8B Base** currently has the cleaner public access/license path and an exact-base 563 MB Q4_0 feasibility artifact, keeping it within the frozen distribution envelope while leaving enough model capacity to plausibly clear a demanding medical-quality floor.
- **Apertus 0.5B** establishes an exceptional ~306 MB Q4-class package-size opportunity and should remain under scrutiny because it could materially improve mass reach. However, its official gated AUP/terms prevent treating it as fully permissive or primary-manifest eligible without separate rights/access reconciliation.
- **MedGemma 4B PT** remains the medical-specialization reference that commandMed should compare against where separately authorized, but it cannot satisfy the current V1 mass-distribution contract.

The tournament must not choose Qwen merely because Apertus is currently conditional. If Apertus's terms become proven compatible and access is separately authorized before manifest freeze, it may be reconsidered under the exact same admission contract. Conversely, no post-result promotion is allowed.

## 8. Public sources captured

Primary/official model sources:

- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base
- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/commit/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
- https://huggingface.co/swiss-ai/Apertus-v1.1-0.5B
- https://huggingface.co/swiss-ai/Apertus-v1.1-0.5B/blame/043a385fa19096fa20dbf9bf52999ea021dedde5/README.md
- https://huggingface.co/google/medgemma-4b-pt
- https://huggingface.co/google/medgemma-1.5-4b-it

Read-only conversion/runtime feasibility sources:

- https://huggingface.co/ggml-org/Qwen3.5-0.8B-Base-GGUF
- https://huggingface.co/ggml-org/Qwen3.5-0.8B-Base-GGUF/blob/main/Qwen3.5-0.8B-Base-Q4_0.gguf
- https://huggingface.co/NonMiFrega/Apertus-v1.1-0.5B-Q4_K_M-GGUF
- https://huggingface.co/mradermacher/medgemma-4b-pt-GGUF
- https://github.com/ggml-org/llama.cpp/pull/15852

Canonical repository sources:

- `data/lineage/lineage_contract.json`
- `src/commandmed/eval_contract/lineage.py`
- `specs/003-data-license-provenance/plan.md`

## 9. Remaining admission work

The following remain unresolved and must be completed before a future frozen `PRIMARY` manifest can exist:

1. exact Spec 003 lineage records/dispositions for Qwen intended uses;
2. exact component-level Qwen license/NOTICE/attribution evidence, including tokenizer/processor artifacts;
3. Apertus AUP/terms compatibility with FD-001 and intended development/derivation/redistribution uses — without accepting terms unless separately authorized;
4. contamination/quarantine proof, including a justified contamination state for future `MODIFICATION_OR_DERIVATION` quantization use;
5. frozen minimum medical-quality and safety gates;
6. exact benchmark/metric slices and access mechanism;
7. exact reference precision and deployable Q5/Q4 ladder;
8. immutable GGUF converter and llama.cpp revisions plus flags;
9. named iPhone, Android, 4-GB-class phone/resource, and weak-laptop evidence environments;
10. exact context/KV/RAM/latency/throughput/energy/thermal protocols;
11. independent exact-head review before any execution-activation proposal.

```text
CURRENT_ULTRA_COMPACT_PRIMARY_ADMISSION_LEAD=Qwen/Qwen3.5-0.8B-Base
APERTUS_ROLE=CONDITIONAL_ULTRA_COMPACT_SIZE_COMPARATOR
APERTUS_RIGHTS=CONDITIONAL_PENDING_AUP_RECONCILIATION
APERTUS_GATED_ASSET_ACCESS_AUTHORITY=NONE
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
