# V5 S1 bounded development execution protocol — 2026-10-03

**Status:** `PROSPECTIVELY_FROZEN_BEFORE_MODEL_OUTPUTS`
**Authority:** `V5_DEVELOPMENT_EXECUTION_AUTHORIZATION_2026-10-03.md`
**Scope:** zero-cost local S1 development/calibration qualification only
**Confirmatory/reserve materialization:** `FORBIDDEN`

This protocol freezes the first executable V5 development grain before observing any model logits, hidden states, generated outputs, training loss, or intervention effect. It does not alter the confirmatory protocol and cannot support a clinical-validity claim.

## 1. Exact model and runtime boundary

Only the following model artifact is admitted:

- repository: `Qwen/Qwen3.5-0.8B-Base`;
- revision: `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`;
- interface: text-only path of the exact authorized multimodal checkpoint;
- runtime dtype: checkpoint-declared float16; no precision fallback is permitted inside this S1 grain;
- CPU execution only with 8 PyTorch intra-op threads and 1 inter-op thread;
- no alternate revision, quantized substitute, converted third-party text-only checkpoint, provider endpoint, merged model, or Qwen-Image/HCF path.

Execution is local on the Founder-owned `Abdulaziz` device with no billed compute. The environment manifest must bind OS, CPU, RAM, Python, PyTorch, Transformers, NumPy, tokenizer files, model files, and their hashes before the first model call.

## 2. Source and oracle boundary

The rule source remains:

- `ncbi-nlp/Clinical-Tool-Learning@d474a95128e128623933c9be0d389ff7d82ef782`;
- `riskqa_evaluation/tools/riskcalcs.json`;
- expected source SHA-256 `00a7a0089afffb66f2f32903bad94a5a2ea842841defb2d78e0686b0a5eb9ab9`;
- selected calculator count `64`;
- every selected calculator code body must match the committed `code_sha256` before execution.

The 2026-10-03 executable-shape audit observed `64/64` code-hash matches. Across the selected code, the only imported module was `numpy`, and the only function call was `np.exp`; all remaining observed AST forms were arithmetic, Boolean logic, comparisons, assignment, branching, and return expressions. Runtime execution must still fail closed if any source/code/hash/AST identity differs.

Rule execution measures deterministic rule conformance only. It does not establish that a historical calculator is clinically appropriate for current care.

## 3. Development/calibration identity use

Only already committed `RULE_ORACLE_DEVELOPMENT` and `RULE_ORACLE_CALIBRATION` state identities may be used.

For each of the 64 selected calculators:

- all 64 committed development identities remain development-only;
- exactly 4 development identities are assigned to `S1_TRAIN` by ascending SHA-256 rank of `case_id|CommandMed-V5-S1-TRAIN-v1`;
- the remaining 60 development identities are `S1_DEV_EVAL`;
- exactly 4 calibration identities are assigned to `S1_CAL_TUNE` by ascending SHA-256 rank of `case_id|CommandMed-V5-S1-CAL-v1`;
- the remaining 60 calibration identities are `S1_CAL_EVAL`.

Therefore the first bounded grain has 256 medical training identities, 3,840 development-evaluation identities, 256 calibration-tuning identities, and 3,840 calibration-evaluation identities. No confirmatory or reserve state index may be selected or materialized.

The large evaluation partitions may be sampled only for resource qualification before a complete development run. Any such sample must be selected by a model-output-independent hash rule and labeled `RESOURCE_QUALIFICATION_ONLY`; it cannot be substituted silently for the full development/calibration matrix.

## 4. Frozen rule-verification task

The S1 medical decision task is a two-class deterministic rule-verification problem.

Each example contains:

1. calculator identity and title;
2. the exact identity-bound calculator function body;
3. one committed Boolean/numeric input state;
4. one proposed calculator output;
5. two answer semantics: `MATCH` and `MISMATCH`.

The deterministic calculator produces the reference output. Proposal correctness is balanced without model output: SHA-256 domain separation over the intrinsic case ID decides whether the proposed output is the exact reference or a deterministic structured perturbation. A separate domain-separated hash decides whether answer label `A` maps to `MATCH` or `MISMATCH`.

The incorrect-output transform is type preserving where possible:

- Boolean: logical negation;
- integer: add one;
- finite float: add `max(1e-6, abs(value) * 0.01)`;
- string: append a fixed `__ALT__` suffix;
- tuple/list: perturb the first recursively perturbable element while preserving container type.

Unsupported/non-finite outputs stop the affected calculator before any model use; they are not coerced after observing model behavior.

The reference and proposed outputs are serialized canonically. The model is never asked to infer clinical validity; it is asked whether the proposed output matches the declared deterministic function for the supplied inputs.

## 5. Frozen semantic transformation

`C1_CRDI_V1` uses one meaning-preserving paired transform per medical training example:

- calculator code is unchanged;
- numeric/Boolean values are unchanged;
- proposed output and MATCH/MISMATCH semantics are unchanged;
- only JSON field order and whitespace/serialization form change.

The validator reconstructs and compares canonical structured values before admitting the pair. If canonical values differ, the transformed example is rejected before model use.

The C1 penalty is Jensen-Shannon divergence between semantic class probabilities after mapping `A/B` back to `MATCH/MISMATCH`.

## 6. Baseline and B1 typed readout

`BASELINE_V1` uses next-token candidate logits for the tokenizer-verified single-token labels `A` and `B`. If the pinned tokenizer does not encode each label as exactly one candidate token under the frozen answer prefix, S1 stops before model inference and the interface must be amended prospectively.

`B1_TYPED_V1` uses the final text hidden representation at the answer marker from the frozen base backbone and a fresh linear `hidden_size -> 2` typed head. The backbone remains frozen. The head is trained from scratch independently for seeds `11`, `29`, and `47` on the identical 256 `S1_TRAIN` medical identities.

Frozen B1 optimization:

- optimizer: AdamW;
- learning rate: `1e-2`;
- weight decay: `1e-4`;
- batch size: `32`;
- maximum epochs: `40`;
- checkpoint selection: lowest `S1_CAL_TUNE` NLL, with earliest epoch winning exact ties;
- no hyperparameter search in this S1 grain.

## 7. C1/C2 parameter budget

`C1_CRDI_V1` and `C2_CRDI_RETAIN_V1` use the same low-rank parameter budget and optimizer. The exact authorized base checkpoint remains frozen.

Adapter contract:

- LoRA rank `4`;
- LoRA alpha `8`;
- adapter dropout `0.0`;
- target scope: every `torch.nn.Linear` projection inside the final text transformer block only;
- LM head, embeddings, vision stack, earlier text blocks, norms, and all other base parameters remain frozen;
- no bias training;
- identical trainable-parameter set for C1 and C2;
- exact module names and trainable-parameter count are recorded after structural discovery and before the first optimization step.

Frozen optimization:

- optimizer: AdamW;
- learning rate: `5e-4`;
- weight decay: `0.0`;
- beta1/beta2: `0.9/0.999`;
- epsilon: `1e-8`;
- gradient norm clip: `1.0`;
- micro-batch size: `1`;
- gradient accumulation: `8`;
- medical epochs: `1`;
- seeds: `11`, `29`, `47`;
- no checkpoint or hyperparameter selection from `S1_DEV_EVAL` or `S1_CAL_EVAL`.

`C1_CRDI_V1` objective:

```text
medical_NLL + 0.1 * semantic_contract_JS
```

`C2_CRDI_RETAIN_V1` objective:

```text
medical_NLL + 0.1 * semantic_contract_JS + 0.1 * retention_KL
```

The weights `0.1` and `0.1` are frozen before model outputs and are not tuned in S1.

## 8. SQuAD maintenance/retention boundary for C2

The only nonmedical source remains `rajpurkar/squad@7b6d24c440a36b6815f21b70d25016731768db1f`, validation split only, under the existing rights admission.

Within that pinned validation split, deterministic SHA-256 ranking over the upstream example ID produces disjoint S1 roles before model use:

- first 64 identities: `S1_C2_MAINTENANCE`;
- next 256 identities: `S1_RETENTION_EVAL`;
- all remaining identities: unused in S1.

No SQuAD passage/question/answer payload is committed to CommandMed. Only source IDs/hashes and aggregate metrics may be persisted.

The C2 maintenance anchor is teacher-forced KL from the frozen base model to the candidate on at most the first 8 gold-answer tokens for the 64 maintenance identities, cycled deterministically across medical optimizer steps. The 256 retention-evaluation identities are never used for training, checkpoint selection, prompt changes, margin selection, or medical hyperparameter selection.

Paired SQuAD Exact Match and token F1 on `S1_RETENTION_EVAL` are reported only after the model-facing implementation is frozen. The permitted interpretation remains narrow paired SQuAD v1.1 retention, not general capability preservation.

## 9. Sequence and decoding contract

- text-only model path;
- maximum encoded medical sequence length: `768` tokens;
- no truncation;
- any over-length admitted medical example stops S1 before model inference for that interface;
- deterministic next-token probability extraction for decision endpoints;
- no sampling for primary endpoints;
- generated retention evaluation uses greedy decoding with a separately recorded maximum-answer-token bound.

Tokenizer candidate-token checks and sequence-length checks are metadata/interface qualification, not empirical model-result inspection.

## 10. Resource qualification and stop rules

Before full S1 training, execute in this order under exact preflight manifests:

1. exact artifact integrity verification;
2. exact environment binding;
3. `MODEL_LOAD` preflight and load;
4. one synthetic/mechanical text-only smoke inference;
5. one 256-token final-block LoRA forward/backward synthetic step;
6. project the bounded 256-example, three-seed C1/C2 training cost from measured wall time and peak memory.

Execution stops and records a resource blocker if any of the following occurs:

- model or tokenizer identity mismatch;
- paid resource or billing requirement;
- disk exhaustion risk below 2 GiB free after artifact acquisition;
- peak process/system memory leaves less than 1.5 GiB operating headroom;
- any out-of-memory, allocation failure, or unrecoverable CPU kernel failure;
- one synthetic 256-token LoRA training step exceeds 180 seconds after one warm-up step;
- projected wall time for one 256-example C1 or C2 seed exceeds 12 hours under the measured local configuration;
- the exact final text block cannot be isolated without changing the authorized checkpoint or training additional base parameters.

These are resource/safety stop rules, not scientific success criteria. They may not be relaxed after observing intervention effects.

## 11. Preflight and evidence contract

Every real model call requires `PREFLIGHT_PASS` from the repository V5 preflight bound to:

- approved Founder authority identity;
- exact model repository/revision;
- exact model-artifact bundle SHA-256;
- exact Git code SHA;
- exact environment SHA-256;
- exact intervention/action/data roles;
- zero paid resource and zero expected spend;
- no PHI/gated/private asset;
- no confirmatory/reserve materialization;
- output under `artifacts/v5/development/`.

Each run records manifest, preflight decision, seed/configuration, raw-output hash, analysis hash, wall time, peak memory, and stop state. Development evidence is never relabeled confirmatory.

## 12. Development-only scientific outputs

If resource qualification passes, S1 may estimate development/calibration repeatability and nuisance quantities and may freeze property-specific meaningful margins and power assumptions under the existing V5 power protocol. Negative or null development results are preserved.

No S1 result proves the V5 thesis. No S1 result authorizes confirmatory execution, future holdout identity materialization, publication, merge, HCF/Qwen-Image work, or clinical-validity language.

## 13. Approved prospective answer-interface amendment - 2026-10-03

Founder approval: `FOUNDER_V5_S1_ANSWER_INTERFACE_AMENDMENT = APPROVED`, recorded in `V5_S1_ANSWER_INTERFACE_AMENDMENT_AUTHORIZATION_2026-10-03.md`. The sole amended terminal answer marker is `ANSWER:\n` (colon followed by one newline), replacing `ANSWER: ` (colon followed by one space). Apply identically in the medical renderer, preparation checker, and model-facing candidate-token qualification. Sections 1-12 and every other scientific/runtime constraint remain binding.

Preserve the original SAH execution failure and the frozen-space-prefix tokenizer failure. Repeat all development/calibration prompt identities, full-prompt candidate-token checks and length checks, deterministic regeneration, tests, compile and exact-head/OCR review; commit/push before a fresh exact-run model-load preflight. Only after every amended pre-model gate passes may existing bounded development authority continue. No model output preceded this amendment.


## 14. Approved Colab runtime and existing Pro entitlement amendment - 2026-10-04

The Founder approved a prospective Colab-managed runtime amendment, then explicitly approved use of the already-owned Colab Pro entitlement under `NO_INCREMENTAL_FOUNDER_SPEND`. See `V5_S1_EXISTING_COLAB_PRO_AUTHORIZATION_2026-10-04.md` and the verbatim source captured with LF line endings `V5_S1_COLAB_FREE_RUNTIME_AUTHORIZATION_SOURCE_2026-10-04.md`. The later Pro approval supersedes only the source's free-tier-only/Pro exclusion. Sections 1-13 remain historical frozen text; local-device/CPU-only placement is amended prospectively for the Colab path, with actual hardware discovered before model use. No specific GPU type is assumed, and no bfloat16 fallback is allowed.

Retain every scientific design, source/case/task, tokenizer/interface, partition, intervention, seed and optimization constraint. Retain the 180-second synthetic-step and 12-hour per-seed projection bounds. Record package/hardware identities and bfloat16 capability, verify the existing exact bundle and all 32,768 full-prompt candidate checks before load, require fresh action preflight, and persist resource/evaluation evidence outside ephemeral storage. No checkpoint/resume mechanism or cross-runtime atomic seed is admitted. Existing Pro resources must be verified as included entitlement without incremental purchase/payment. Unknown entitlement or unsupported hardware stops prospectively.

All three prior negative execution results remain valid and preserved. Confirmatory/reserve, PHI/private/gated clinical data, paid APIs, new compute spend, external paid services, replication, HCF/Qwen-Image, publication and merge remain forbidden. This amendment grants no empirical qualification by itself.

## 15. Founder selection of exposed free Colab resources - 2026-10-04

After the Colab account reported no recognized subscription and zero units, the Founder explicitly selected free resources and prohibited buying anything. See `V5_S1_FREE_COLAB_SELECTION_2026-10-04.md`. This free path does not depend on resolving the Pro entitlement discrepancy. Preserve the discrepancy and all prior authority records. Discover actual hardware and measure the exact authorized bfloat16 path without changing dtype or scientific design. Primitive tensor checks are preliminary only; full artifact, interface, exact-run preflight and resource qualification remain required. No upgrade, purchase, premium resource assumption, or limitation bypass is authorized.
