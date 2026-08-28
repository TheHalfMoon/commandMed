# E004 Decision B Conversion Normalization / Metadata Policy — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `6a74b8284d9fc26342ce6c90aad5417dc3bcafb9`  
**Founder decision:** `ARTIFACT_DECISION_B` preparation-only  
**Artifact class:** non-executing static normalization / metadata policy  
**Authority effect:** NONE beyond already-canonical Decision B preparation scope  
**Package installation performed:** NO  
**Python/converter execution performed:** NO  
**Model/source-weight local materialization performed:** NO  
**Conversion/quantization performed:** NO  
**Model execution performed:** NO  
**Spend:** USD 0

This record freezes the commandMed policy for how the two Decision B conversion subjects may treat source bytes, source-directory naming, converter metadata heuristics, tokenizer/config metadata, and optional converter overrides if conversion is ever separately authorized. It does not create an executable environment and does not grant conversion authority.

```text
POLICY_ID=E004-DECISION-B-CONVERSION-NORMALIZATION-METADATA-V1
POLICY_STATE=STATIC_POLICY_PREPARED
ARTIFACT_DECISION_B_SCOPE=GRANITE_PRIMARY_PLUS_QWEN3_4B_CONTROL
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Controlling exact source identities

```text
CONVERSION_TOOL_REPOSITORY=ggml-org/llama.cpp
CONVERSION_TOOL_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
CONVERSION_TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
CONVERSION_ENTRYPOINT=convert_hf_to_gguf.py
CONVERSION_ENTRYPOINT_GIT_BLOB=78ad26c6563062e2a801c9f76f77a7ce196dd195
MODEL_BASE_SOURCE=conversion/base.py
MODEL_BASE_GIT_BLOB=56547ace009fd4d719a641f910e3f0890587d9b9
GGUF_METADATA_SOURCE=gguf-py/gguf/metadata.py
GGUF_METADATA_GIT_BLOB=d5836cc68d7a96cd267e70800994bb3cc7bfcad0
SPECIAL_VOCAB_SOURCE=gguf-py/gguf/vocab.py
SPECIAL_VOCAB_GIT_BLOB=d93b94f2d792147276be21db004dbd8d4edef82c
GRANITE_CONVERTER_SOURCE=conversion/granite.py
GRANITE_CONVERTER_GIT_BLOB=796d37cca269a71e014759cb0f6c5c1342c7615b
QWEN_CONVERTER_SOURCE=conversion/qwen.py
QWEN_CONVERTER_GIT_BLOB=cdba8a63e9c919232e2ec80e88b01afec7967dc4
MAMBA_CONVERTER_SOURCE=conversion/mamba.py
MAMBA_CONVERTER_GIT_BLOB=8a2a4637529a4f8140836ab089654684f85f96c9
```

Canonical runtime-dependency reconciliation remains controlling for runtime resolution:

```text
LOCAL_GGUF_SOURCE_MODE=REQUIRED
NO_LOCAL_GGUF_MUST_BE_UNSET=YES
EXTERNAL_GGUF_CODE_AS_SELECTED_RUNTIME=PROHIBITED
UPSTREAM_FULLY_RESOLVED_DEPENDENCY_LOCK_PRESENT=NO
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
```

This policy does not convert source-code identity into installed-runtime identity.

## 2. Frozen Decision B source subjects

```text
GRANITE_SOURCE_REPOSITORY=ibm-granite/granite-4.0-350m-base
GRANITE_SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
GRANITE_REQUIRED_DIRECTORY_BASENAME=granite-4.0-350m-base

QWEN_SOURCE_REPOSITORY=Qwen/Qwen3-4B-Base
QWEN_SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
QWEN_REQUIRED_DIRECTORY_BASENAME=Qwen3-4B-Base
```

Provider-side non-weight identities are already bound canonically by PR #106 plus the correction in PR #107. Those provider-side bindings do not equal commandMed local source-bundle integrity.

```text
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
```

## 3. Source-byte normalization policy

commandMed may not rewrite source bytes before conversion.

```text
SOURCE_FILE_PREPROCESSING_BY_COMMANDMED=PROHIBITED
SOURCE_METADATA_REWRITE_BY_COMMANDMED=PROHIBITED
TOKENIZER_FILE_REWRITE_BY_COMMANDMED=PROHIBITED
CONFIG_REWRITE_BY_COMMANDMED=PROHIBITED
MODEL_CARD_REWRITE_BY_COMMANDMED=PROHIBITED
GENERATION_CONFIG_REWRITE_BY_COMMANDMED=PROHIBITED
WEIGHT_FILE_REWRITE_BY_COMMANDMED=PROHIBITED
SOURCE_SHARD_REPACKING_BY_COMMANDMED=PROHIBITED
SOURCE_FILENAME_RENAMING_AFTER_SUBJECT_FREEZE=PROHIBITED
SOURCE_DIRECTORY_BASENAME_MUTATION_AFTER_SUBJECT_FREEZE=PROHIBITED
```

If the pinned converter cannot consume the exact frozen source subject under this policy, the conversion attempt must fail closed. The repository may not modify source bytes merely to make the converter succeed.

```text
CONVERTER_FAILURE_AUTHORIZES_SOURCE_PATCH=NO
CONVERTER_FAILURE_AUTHORIZES_REVISION_SUBSTITUTION=NO
CONVERTER_FAILURE_AUTHORIZES_MODEL_SUBSTITUTION=NO
```

## 4. Selected converter mode and prohibited overrides

The prepared Decision B subject is local-directory conversion. The following metadata-affecting or source-mode switches are not selected:

```text
REMOTE_HF_MODE_SELECTED=NO
METADATA_OVERRIDE_FILE_SELECTED=NO
MODEL_NAME_OVERRIDE_SELECTED=NO
MISTRAL_FORMAT_SELECTED=NO
MMProj_MODE_SELECTED=NO
MTP_MODE_SELECTED=NO
DSPARK_MODE_SELECTED=NO
TARGET_MODEL_DIRECTORY_SELECTED=NO
SENTENCE_TRANSFORMERS_DENSE_MODULES_SELECTED=NO
```

Therefore a future exact conversion argv, if separately authorized, must preserve:

```text
REMOTE_HF_MODEL_ID=NONE
METADATA_OVERRIDE_FILE=NONE
MODEL_NAME_OVERRIDE=NONE
TARGET_MODEL_DIR=NONE
```

The following are prohibited for these Decision B subjects unless a later reviewed policy amendment explicitly changes the subject before execution:

```text
--remote=PROHIBITED
--metadata=PROHIBITED
--model-name=PROHIBITED
--mistral-format=PROHIBITED
--mmproj=PROHIBITED
--mtp=PROHIBITED
--dspark=PROHIBITED
--target-model-dir=PROHIBITED
```

This freezes policy only; it does not create executable argv authority.

## 5. Converter-internal metadata parsing is permitted, source mutation is not

The pinned `gguf.Metadata.load(...)` path reads, when present:

```text
README.md
config.json
generation_config.json
```

It then applies converter-internal parsing and heuristics. Those in-memory transformations are part of the pinned converter behavior and are permitted only because the exact source revision is frozen.

The pinned model-card parser performs two explicit in-memory parse normalizations before YAML decoding:

```text
MODEL_CARD_INTERNAL_PARSE_NORMALIZATION_1=replace '- no\n' with '- "no"\n'
MODEL_CARD_INTERNAL_PARSE_NORMALIZATION_2=replace tab with two spaces
```

Policy:

```text
PINNED_CONVERTER_INTERNAL_PARSE_NORMALIZATION=PERMITTED
COMMANDMED_REIMPLEMENTATION_OF_PARSE_NORMALIZATION=PROHIBITED
COMMANDMED_PRE_EDIT_TO_MATCH_CONVERTER_NORMALIZATION=PROHIBITED
SOURCE_BYTES_ON_DISK_MUST_REMAIN_UNCHANGED=YES
```

The distinction is mandatory: converter-internal parsing may normalize an in-memory representation; commandMed may not normalize the source files themselves.

## 6. Config resolution policy

Pinned `ModelBase.load_hparams(...)` first attempts local `AutoConfig.from_pretrained(dir_model, trust_remote_code=False)` and falls back to local `config.json` parsing when required by the pinned implementation.

```text
TRUST_REMOTE_CODE=FALSE_REQUIRED
REMOTE_CODE_EXECUTION=PROHIBITED
LOCAL_CONFIG_SOURCE_REVISION=FROZEN
CONFIG_FALLBACK_BEHAVIOR=PINNED_CONVERTER_IMPLEMENTATION_ONLY
```

Because the exact installed Transformers/Python runtime is not yet bound, this policy does not claim that the exact resolved in-memory config dictionary is already known.

```text
EXACT_CONFIG_RUNTIME_RESOLUTION=NEEDS_EXECUTION_ENVIRONMENT_EVIDENCE
CONFIG_POLICY_STATE=FROZEN_STATIC_RUNTIME_ATTESTATION_REQUIRED
```

No runtime-dependent observation may be back-projected into the source files.

## 7. Directory-basename metadata policy

The pinned metadata heuristic consumes `model_path.name`, and the converter may also fall back to `self.dir_model.name`. The local source-directory basename is therefore a semantic input.

```text
DIRECTORY_BASENAME_IS_SEMANTIC_INPUT=YES
GRANITE_REQUIRED_DIRECTORY_BASENAME=granite-4.0-350m-base
QWEN_REQUIRED_DIRECTORY_BASENAME=Qwen3-4B-Base
DIRECTORY_BASENAME_NORMALIZATION=PROHIBITED
HASH_DIRECTORY_AS_DIRECT_MODEL_DIRECTORY=PROHIBITED
RANDOM_TEMP_BASENAME_AS_DIRECT_MODEL_DIRECTORY=PROHIBITED
REPOSITORY_LEAF_BASENAME_REQUIRED=YES
```

The parent storage path remains unresolved and may vary only if the final basename and exact frozen bytes remain unchanged and the future storage boundary is separately identity-bound.

```text
EXACT_LOCAL_SOURCE_DIRECTORY_PARENT=NEEDS_EVIDENCE
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
```

## 8. Model-card metadata policy

When `README.md` exists, the pinned parser reads YAML frontmatter and may derive authorship, license, language, tags, datasets, model naming, and related GGUF metadata through pinned heuristics.

```text
MODEL_CARD_METADATA_SOURCE=EXACT_FROZEN_README_BYTES
MODEL_CARD_METADATA_OVERRIDE_BY_COMMANDMED=PROHIBITED
MODEL_CARD_FIELD_INVENTION_BY_COMMANDMED=PROHIBITED
MODEL_CARD_PARSE_FAILURE_POLICY=PINNED_CONVERTER_BEHAVIOR_ONLY
```

No commandMed-authored metadata override may repair or replace provider model-card metadata during conversion.

## 9. Generation-config metadata policy

When `generation_config.json` exists, the pinned metadata path may derive sampler metadata such as top-k, top-p, temperature, repetition penalty, and related fields.

```text
GENERATION_METADATA_SOURCE=EXACT_FROZEN_GENERATION_CONFIG_BYTES
GENERATION_METADATA_MANUAL_OVERRIDE=PROHIBITED
GENERATION_METADATA_MANUAL_NORMALIZATION=PROHIBITED
```

If a field is absent, commandMed may not invent a value merely to populate GGUF metadata.

```text
ABSENT_GENERATION_METADATA_FIELD=LEAVE_TO_PINNED_CONVERTER_DEFAULT_BEHAVIOR
INVENTED_SAMPLER_METADATA=PROHIBITED
```

## 10. Tokenizer / vocabulary metadata policy

Canonical Decision B provider evidence binds the selected tokenizer/config files and merge surfaces. The converter may parse those exact local files according to the pinned `conversion` and local `gguf-py` implementation.

```text
TOKENIZER_SOURCE_BYTES=EXACT_FROZEN_PROVIDER_IDENTITIES
TOKENIZER_SOURCE_REWRITE=PROHIBITED
TOKENIZER_SPECIAL_TOKEN_MANUAL_EDIT=PROHIBITED
TOKENIZER_MERGE_MANUAL_EDIT=PROHIBITED
TOKENIZER_CHAT_TEMPLATE_MANUAL_EDIT=PROHIBITED
PINNED_SPECIAL_VOCAB_BEHAVIOR=PERMITTED
EXTERNAL_TOKENIZER_NORMALIZATION_LAYER=PROHIBITED
```

Exact runtime-dependent tokenizer resolution remains subject to the future installed-runtime attestation. This static policy does not claim successful tokenizer loading.

## 11. Tensor-derived metadata policy

The pinned conversion path may derive metadata from the actual indexed source tensors and converter state, including parameter counts, inferred file type behavior where applicable, and size-label heuristics.

For the prepared Decision B conversion proposal, `--outtype f16` is selected explicitly rather than `auto`.

```text
PROPOSED_CONVERSION_OUTTYPE=f16
AUTO_OUTTYPE_SELECTED=NO
TENSOR_DERIVED_METADATA=PINNED_CONVERTER_BEHAVIOR_ONLY
COMMANDMED_MANUAL_PARAMETER_COUNT=PROHIBITED_AS_OUTPUT_METADATA_SOURCE
COMMANDMED_MANUAL_SIZE_LABEL=PROHIBITED_AS_OUTPUT_METADATA_SOURCE
```

Because tensor-derived metadata is execution-derived, exact output metadata cannot be truthfully frozen before a separately authorized conversion run.

```text
EXACT_OUTPUT_GGUF_METADATA=NEEDS_POST_CONVERSION_EVIDENCE
PRECOMPUTED_OUTPUT_METADATA_CLAIM=PROHIBITED
```

## 12. Output metadata attestation requirement

If conversion is later separately authorized and completes, the output must not become a tournament runtime artifact until a post-conversion metadata attestation is independently reviewed.

The future attestation must bind at least:

```text
output_sha256
output_exact_integer_bytes
conversion_log_sha256
conversion_environment_identity
exact_conversion_argv
exact_source_bundle_identity
exact_source_directory_basename
pinned_converter_source_identity
installed_runtime_identity
extracted_gguf_metadata_evidence_identity
metadata_policy_id
metadata_policy_conformance_disposition
```

The attestation must distinguish metadata derived from:

```text
SOURCE_MODEL_CARD
SOURCE_CONFIG
SOURCE_GENERATION_CONFIG
SOURCE_TOKENIZER_ASSETS
SOURCE_DIRECTORY_BASENAME
TENSOR_DERIVED_CONVERTER_STATE
PINNED_CONVERTER_CONSTANT_OR_HEURISTIC
```

Any unexplained metadata field, unexpected override, source mutation, runtime drift, or subject-name drift must fail closed.

```text
UNEXPLAINED_OUTPUT_METADATA=FAIL_CLOSED
METADATA_OVERRIDE_DETECTED=FAIL_CLOSED
SOURCE_BYTE_MUTATION_DETECTED=FAIL_CLOSED
SOURCE_BASENAME_DRIFT_DETECTED=FAIL_CLOSED
CONVERTER_SOURCE_DRIFT_DETECTED=FAIL_CLOSED
INSTALLED_RUNTIME_DRIFT_DETECTED=FAIL_CLOSED
```

## 13. Relationship to runtime and execution boundaries

This policy composes with the already-canonical records:

```text
RUNTIME_DEPENDENCY_RECONCILIATION=specs/007-sft-v1/e004-converter-runtime-dependency-reconciliation-2026-08-28.md
CONVERSION_EXECUTION_BOUNDARY=specs/007-sft-v1/e004-conversion-execution-boundary-preparation-2026-08-28.md
METADATA_INPUT_CORRECTION=specs/007-sft-v1/e004-decision-b-metadata-input-correction-2026-08-28.md
```

It does not supersede any of them.

```text
NETWORK_BOUNDARY_RUNTIME_ENFORCEMENT=NEEDS_EVIDENCE
CREDENTIAL_STATE_RUNTIME_ATTESTATION=NEEDS_EVIDENCE
EXACT_STORAGE_BOUNDARY_IDENTITY=NEEDS_EVIDENCE
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
```

## 14. Policy closure semantics

This record is intended to close the **static policy-definition** portion of the Decision B `NORMALIZATION_OR_METADATA_POLICY` field, not the operational execution preflight.

```text
NORMALIZATION_OR_METADATA_POLICY=STATIC_POLICY_DEFINED_PENDING_EXACT_HEAD_REVIEW
NORMALIZATION_OR_METADATA_POLICY_ID=E004-DECISION-B-CONVERSION-NORMALIZATION-METADATA-V1
NORMALIZATION_OR_METADATA_POLICY_REQUIRES_RUNTIME_ATTESTATION=YES
NORMALIZATION_OR_METADATA_POLICY_REQUIRES_POST_CONVERSION_ATTESTATION=YES_IF_CONVERSION_LATER_AUTHORIZED
```

Even after canonical review/merge of this policy:

```text
CONVERSION_EXECUTION_AUTHORITY=NONE
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 15. Review questions

Fresh exact-head review must independently verify:

1. The policy is within Decision B preparation authority and grants no execution authority.
2. Pinned source/blob identities match the exact `llama.cpp` revision.
3. `README.md`, `config.json`, `generation_config.json`, tokenizer assets, and directory basename are treated consistently with the pinned selected path.
4. commandMed source mutation and manual metadata overrides are prohibited.
5. `--metadata`, `--model-name`, and `--remote` remain unselected/prohibited for these subjects.
6. Converter-internal model-card parse normalization is distinguished from source-byte mutation.
7. `trust_remote_code=False` is preserved for config resolution.
8. Runtime-dependent and tensor-derived metadata remain future evidence rather than precomputed claims.
9. Post-conversion metadata attestation is required if conversion is later authorized.
10. Local source-bundle integrity, exact runtime identity, execution authority, E004 PASS, E005, training, and spend remain unchanged.

## Exclusions

This artifact performs no package installation, Python import execution, model/source-weight download or local materialization, converter build, conversion, quantization, model loading, inference, benchmark/device execution, contamination assessment, storage provisioning, credential use, provider generation, Private Gold/PHI access, personnel engagement, procurement, payment, training, or spend. It creates no workflow and consumes no authorized workflow run.
