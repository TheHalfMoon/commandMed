# E001 Final Pre-Freeze Packet — 2026-08-27

**Repository:** `TheHalfMoon/commandMed`
**Bounded authority:** E001 evidence/reconciliation only
**Status:** `FINAL_E001_MANIFEST_READY_FOR_FOUNDER_CHATGPT_FREEZE`
**Stop type:** `FOUNDER_DECISION_REQUIRED`
**Training authority:** `NONE`
**Model-weight access authority:** `NONE`
**Benchmark-payload access authority:** `NONE`
**Model execution authority:** `NONE`
**Model conversion authority:** `NONE`
**Tournament execution authority:** `NONE`
**Device execution authority:** `NONE`
**Spend authority:** `NONE`

This packet is the final E001 pre-freeze decision surface. It does **not** freeze the candidate manifest, does **not** select a backbone winner, and grants no E002/E003 authority.

## 1. Live repository binding at packet preparation

```text
CANONICAL_MAIN_SHA=5c61e3b702270bc9aaaa28cf1a537ea6bf2cd5c4
CANONICAL_MAIN_TREE=033adafc826ac422f398ef4a41c4b02e7f4c9366
PR55_PRE_PACKET_HEAD=be600b3fe6fb3dd2aa49d64f4d6773fddf6c8ed1
PR55_PRE_PACKET_TREE=aeaa602ff208f136e09f0d620bebcbe57d6acd0c
```

The exact final PR #55 head/tree containing this packet and the canonical manifest is qualification evidence recorded outside the self-referential packet content.

## 2. Canonical semantics and supersession

The existing Spec 003 contract already supports the required separation:

```text
MODEL_LINEAGE_ADMISSION
!=
CANDIDATE_X_BENCHMARK_CONTAMINATION
```

For E001 candidate membership:

```text
MODEL_LINEAGE_ADMISSION=ELIGIBLE
=> candidate may enter the proposed frozen candidate manifest
```

For later benchmark use:

```text
CANDIDATE_X_BENCHMARK_CONTAMINATION=INCOMPLETE
=> that exact benchmark slice may NOT participate in selection/ranking
```

Therefore:

```text
BENCHMARK_CONTAMINATION_DOES_NOT_BLOCK_E001_MEMBERSHIP_FREEZE=YES
BENCHMARK_CONTAMINATION_BLOCKS_SELECTION_USE_UNTIL_RESOLVED=YES
```

This packet supersedes any earlier E001 status sentence that says benchmark-selection contamination blocks **candidate membership**. In particular, the historical line `PRIMARY_ADMISSION=BLOCKED_PENDING_BENCHMARK_CONTAMINATION_EVIDENCE` in `admission-evidence-e001-public-metadata-2026-08-27.md` is superseded for membership semantics. The correct split is:

```text
PRIMARY_MODEL_LINEAGE_MEMBERSHIP_ADMISSION=ELIGIBLE
PRIMARY_BENCHMARK_SELECTION_ELIGIBILITY=INCOMPLETE
```

No Spec 003 contract amendment is required.

## 3. Qwen3.5 complete text/Core package accounting

Candidate:

```text
Qwen/Qwen3.5-0.8B-Base
SOURCE_REVISION=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
```

Public metadata only was used. No model or benchmark payload was downloaded, loaded, executed, converted, or measured on a device.

### 3.1 Official GGUF repository contents

Observed official repository:

`ggml-org/Qwen3.5-0.8B-Base-GGUF`

Public repository view contains:

- `.gitattributes`
- `.src_sha`
- `Qwen3.5-0.8B-Base-BF16.gguf`
- `Qwen3.5-0.8B-Base-Q4_0.gguf`
- `Qwen3.5-0.8B-Base-Q8_0.gguf`
- `README.md`
- `convert.log`

No `mmproj`, projector, vision-projector, or other separate multimodal runtime artifact is published in that official GGUF repository.

### 3.2 Q4_0 exact public identity

```text
GGUF_FILE=Qwen3.5-0.8B-Base-Q4_0.gguf
GGUF_REPOSITORY=ggml-org/Qwen3.5-0.8B-Base-GGUF
GGUF_FILE_COMMIT=1bd44f68963429437d08bc12f465716eb31ba6e5
GGUF_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
GGUF_BYTES=563035840
GGUF_MIB=536.9528198242188
```

The exact byte count and SHA-256 are exposed by the public Git LFS pointer metadata; the GGUF bytes themselves were not transferred.

### 3.3 Text versus vision layout

Current `llama.cpp` conversion source registers `Qwen3_5ForConditionalGeneration` / `Qwen3_5ForCausalLM` as a `TextModel`. The `TextModel` conversion path explicitly skips multimodal tensors, including vision/visual tensor namespaces. Therefore the official `Qwen3.5-0.8B-Base-Q4_0.gguf` is the **text/Core language artifact**, not a combined language+vision monolith.

```text
GGUF_CONTAINS_TEXT_CORE=YES
GGUF_CONTAINS_VISION_ENCODER=NO_BY_LLAMA_CPP_TEXTMODEL_CONVERSION
SEPARATE_MMPROJ_IN_OFFICIAL_REPO=NO
MMPROJ_REQUIRED_FOR_TEXT_ONLY_LLAMA_CPP=NO
```

A projector would be needed only for a separately provisioned multimodal/image path. That path is secondary/non-ranking under `COMMON_CORE_PRIMARY_RANKING`.

### 3.4 Runtime-required tokenizer/config/template assets

The official GGUF repository documents direct single-artifact `llama.cpp` invocation. The source model's tokenizer/config identity remains bound at the immutable source revision for provenance, but those source-side files are not separate model-side runtime assets for the canonical text-only GGUF invocation; the necessary GGUF metadata is embedded in the GGUF.

Source-side identity bound at `dc7cdfe...`:

- `config.json`
- `generation_config.json`
- `merges.txt`
- `tokenizer.json`
- `tokenizer_config.json`
- `vocab.json`
- `preprocessor_config.json`
- `processor_config.json`
- `video_preprocessor.json`

Common-Core runtime accounting:

```text
TEXT_CORE_GGUF_BYTES=563035840
EXTERNAL_TEXT_RUNTIME_MODEL_ASSET_BYTES=0
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_BYTES=563035840
OPTIONAL_MULTIMODAL_BUNDLE_BYTES=NOT_PUBLISHED_IN_OFFICIAL_GGML_BASE_REPOSITORY
```

Repository documentation/provenance files such as `.src_sha`, `README.md`, `.gitattributes`, and `convert.log` are not required-to-execute text/Core model assets and are not added to the runtime model bundle.

### 3.5 Static package gates

```text
700_MiB_BYTES=734003200
600_MiB_BYTES=629145600

COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_BYTES=563035840
SUB_700MB_STATIC_GATE=PASS
ENGINEERING_TARGET_LE_600_MiB=PASS
```

This is **static package accounting only**. It proves neither the `2 GiB` peak-RAM gate nor latency, throughput, thermal, energy, or real-device behavior.

## 4. Proposed E001 manifest

Deterministic manifest file:

`specs/007-sft-v1/e001-proposed-candidate-manifest.json`

```text
MANIFEST_VERSION=e001-mass-reach-v1
PROPOSED_MANIFEST_CANONICAL_SHA256=98d586500d12e7904bce199061c48d5ac50e9f66a372de034d9ecba4e2d3cc28
QUARANTINE_MATRIX_IDENTITY=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
```

The SHA-256 is computed using the repository's canonical JSON semantics: recursively sorted object keys, compact separators, UTF-8, and preserved semantic sequence order where no set/record sort rule applies.

### PRIMARY

1. `Qwen/Qwen3-0.6B-Base`
2. `Qwen/Qwen3.5-0.8B-Base`
3. `ibm-granite/granite-4.0-350m-base`

### CONTROL

1. `Qwen/Qwen3-4B-Base`

Control semantics:

```text
candidate_role=CONTROL
winner_eligible=NO
purpose=SCALE_QUALITY_OPPORTUNITY_COST
mass_reach_package_gate_not_required_for_CONTROL_winning=YES
may_win_current_PRIMARY_tournament=NO
```

No fallback 2B/3B/4B candidate is added to PRIMARY.

Frozen E001 manifest policies:

```text
COMMON_CORE_PRIMARY_RANKING=ENFORCED
QUALITY_FLOOR_THEN_SIZE_FIRST=ENFORCED
BASE_ONLY_PRIMARY=ENFORCED
FULLY_ADMITTED_PRIMARY_ONLY=ENFORCED
SUB_700MB_MASS_REACH=ENFORCED
```

## 5. Candidate identity and admission ledger

### Qwen/Qwen3-0.6B-Base

```text
candidate_role=PRIMARY
immutable_revision=da87bfb608c14b7cf20ba1ce41287e8de496c0cd
artifact_binding_state=IMMUTABLE_REVISION_LOCATOR
artifact_identity=https://huggingface.co/Qwen/Qwen3-0.6B-Base/tree/da87bfb608c14b7cf20ba1ce41287e8de496c0cd
model_config_identity=config.json@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
tokenizer_identity=merges.txt+tokenizer.json+tokenizer_config.json+vocab.json@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
special_token_identity=tokenizer_config.json@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
processor_identity=NOT_APPLICABLE
license_identity=Apache-2.0@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
access_state=PUBLIC_UNGATED
spec003_development_evaluation=ELIGIBLE
spec003_modification_derivation=ELIGIBLE
spec003_training_adaptation=ELIGIBLE
spec003_redistribution=ELIGIBLE
native_context=32768
common8k_supported=YES_STATIC_CONTEXT_ONLY
arabic_evidence=FAMILY_SUPPORT_119_LANGUAGES_7_ARABIC_DIALECTS; CHECKPOINT_MEDICAL_ARABIC_NEEDS_EVIDENCE
```

Static exact-base conversion feasibility evidence exists at 396,704,512 bytes for Q4_K_M, but it is a community derivative and is **not** promoted here to the final canonical release artifact. E001 source identity remains the immutable upstream checkpoint revision; final deployable quantization identity remains a later frozen-ladder decision.

### Qwen/Qwen3.5-0.8B-Base

```text
candidate_role=PRIMARY
immutable_revision=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
artifact_binding_state=IMMUTABLE_REVISION_LOCATOR
artifact_identity=https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/tree/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
model_config_identity=config.json@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
tokenizer_identity=merges.txt+tokenizer.json+tokenizer_config.json+vocab.json@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
special_token_identity=tokenizer_config.json@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
processor_identity=preprocessor_config.json+processor_config.json+video_preprocessor.json@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68; OPTIONAL_FOR_TEXT_CORE
license_identity=Apache-2.0@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
access_state=PUBLIC_UNGATED
spec003_development_evaluation=ELIGIBLE
spec003_modification_derivation=ELIGIBLE
spec003_training_adaptation=ELIGIBLE
spec003_redistribution=ELIGIBLE
complete_text_core_bundle_bytes=563035840
sub700mb_static_gate=PASS
engineering_target_le600mib=PASS
native_context=262144
common8k_supported=YES_STATIC_CONTEXT_ONLY
arabic_evidence=FAMILY_SUPPORT_119_LANGUAGES_7_ARABIC_DIALECTS; CHECKPOINT_MEDICAL_ARABIC_NEEDS_EVIDENCE
```

### ibm-granite/granite-4.0-350m-base

```text
candidate_role=PRIMARY
immutable_revision=a50b46cef21c8a86b15f0496cb794487a78a910b
artifact_binding_state=IMMUTABLE_REVISION_LOCATOR
artifact_identity=https://huggingface.co/ibm-granite/granite-4.0-350m-base/tree/a50b46cef21c8a86b15f0496cb794487a78a910b
model_config_identity=config.json@a50b46cef21c8a86b15f0496cb794487a78a910b
tokenizer_identity=merges.txt+special_tokens_map.json+tokenizer.json+tokenizer_config.json+vocab.json@a50b46cef21c8a86b15f0496cb794487a78a910b
special_token_identity=special_tokens_map.json+tokenizer_config.json@a50b46cef21c8a86b15f0496cb794487a78a910b
processor_identity=NOT_APPLICABLE
license_identity=Apache-2.0@a50b46cef21c8a86b15f0496cb794487a78a910b
access_state=PUBLIC_UNGATED
spec003_development_evaluation=ELIGIBLE
spec003_modification_derivation=ELIGIBLE
spec003_training_adaptation=ELIGIBLE
spec003_redistribution=ELIGIBLE
official_q4_k_m_sha256=2c22ed74d6c11791eb017886e1356ae11a6b8207b1ab2c1dfee047370110389a
official_q4_k_m_public_size_display=237_MB
sub700mb_static_gate=PASS
native_context=32768
common8k_supported=YES_STATIC_CONTEXT_ONLY
arabic_evidence=OFFICIAL_SUPPORTED_LANGUAGE_AR; CHECKPOINT_MEDICAL_ARABIC_NEEDS_EVIDENCE
```

The public metadata source exposes the official Granite Q4_K_M digest and a 237 MB size display, which is more than sufficient to establish the static sub-700 MiB feasibility gate. This packet does not fabricate an unsurfaced exact LFS byte count.

### Qwen/Qwen3-4B-Base

```text
candidate_role=CONTROL
winner_eligible=NO
purpose=SCALE_QUALITY_OPPORTUNITY_COST
immutable_revision=906bfd4b4dc7f14ee4320094d8b41684abff8539
artifact_binding_state=IMMUTABLE_REVISION_LOCATOR
artifact_identity=https://huggingface.co/Qwen/Qwen3-4B-Base/tree/906bfd4b4dc7f14ee4320094d8b41684abff8539
model_config_identity=config.json@906bfd4b4dc7f14ee4320094d8b41684abff8539
tokenizer_identity=merges.txt+tokenizer.json+tokenizer_config.json+vocab.json@906bfd4b4dc7f14ee4320094d8b41684abff8539
special_token_identity=tokenizer_config.json@906bfd4b4dc7f14ee4320094d8b41684abff8539
processor_identity=NOT_APPLICABLE
license_identity=Apache-2.0@906bfd4b4dc7f14ee4320094d8b41684abff8539
access_state=PUBLIC_UNGATED
spec003_development_evaluation=ELIGIBLE
spec003_train_family_uses=NOT_EVALUATED_FOR_CONTROL_PURPOSE
native_context=32768
common8k_supported=YES_STATIC_CONTEXT_ONLY
mass_reach_static_gate=FAIL_BY_DESIGN_CONTROL
```

## 6. Benchmark contamination gate

For every candidate × required primary benchmark slice:

```text
PRIMARY_SELECTION_BENCHMARK_CONTAMINATION_STATE=INCOMPLETE
BENCHMARK_CONTAMINATION_DOES_NOT_BLOCK_E001_MEMBERSHIP_FREEZE=YES
BENCHMARK_CONTAMINATION_BLOCKS_SELECTION_USE_UNTIL_RESOLVED=YES
```

Do not claim `ASSESSED_CLEAN`. Do not use `NOT_APPLICABLE` for public benchmark selection. E003/E004 planning must resolve exact candidate × slice contamination evidence before an affected slice participates in selection.

## 7. Core / Mass-Reach / Nano reconciliation

```text
CORE=CAPABILITY_SAFETY_PRODUCT_CONTRACT
MASS_REACH_CORE=CANDIDATE_SATISFYING_CURRENT_FROZEN_SPEC005_CORE_CONTRACT
NANO=FUTURE_SEPARATELY_SCOPED_DERIVED_DISTILLED_COMPRESSED_TIER
NANO_IS_PARAMETER_COUNT_SYNONYM=NO
```

The approximate parameter bands in the additive density strategy are hypotheses, not frozen gates. `reconciliation-core-mass-reach-2026-08-27.md` already determines that the minimal editorial correction belongs in a **separate editorial PR**; PR #55 therefore does not silently broaden its scope. The separate PR must cross-reference this reconciliation.

## 8. Review and qualification requirement

Before this packet is treated as final evidence for the Founder+ChatGPT freeze decision:

1. bind PR #55 to the exact new head/tree containing this packet and the manifest;
2. run the repository's docs-only/deterministic verification applicable to that head;
3. obtain fresh exact-head independent review, or use the repository's documented reviewer-unavailable fallback transparently;
4. repair every valid material finding and repeat qualification if the head changes.

No PASS may be inferred from reviewer silence.

## 9. Freeze decision boundary

The packet is ready only for the following explicit Founder+ChatGPT decision:

```text
FREEZE_PROPOSED_MANIFEST=e001-mass-reach-v1
FREEZE_PROPOSED_MANIFEST_CANONICAL_SHA256=98d586500d12e7904bce199061c48d5ac50e9f66a372de034d9ecba4e2d3cc28
PRIMARY=[
  Qwen/Qwen3-0.6B-Base,
  Qwen/Qwen3.5-0.8B-Base,
  ibm-granite/granite-4.0-350m-base
]
CONTROL=[
  Qwen/Qwen3-4B-Base
]
QUARANTINE_MATRIX_IDENTITY=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
```

Until Founder+ChatGPT explicitly accepts that freeze:

```text
CANDIDATE_MANIFEST_FROZEN=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
E002_AUTHORITY=NONE
E003_AUTHORITY=NONE
```

E001 chooses who may compete. It does not choose who wins.
