# FOUNDER AUTHORIZATION — V5 S1 ZERO-COST COLAB RUNTIME AMENDMENT

Status: `APPROVED`

Date: `2026-10-04`

I explicitly authorize a prospective runtime-only amendment to the bounded CommandMed V5 S1 development protocol.

This amendment is issued after the existing local CPU/bfloat16 resource qualification encountered the frozen `1.5 GiB` system-memory-headroom stop condition, and before any model inference, backward benchmark, optimizer step, B1/C1/C2 training, calibration analysis, selective-risk analysis, margin estimation, or power estimation.

The local resource failure remains valid negative execution evidence and must be preserved.

## 1. Authorized runtime change

The previously frozen requirement that S1 model-facing development execution occur only on the Founder-owned local `Abdulaziz` CPU runtime is amended.

The bounded S1 development execution may instead run on a **Google Colab managed runtime operating entirely within the free-of-charge tier**.

The Colab runtime may use an available GPU accelerator if and only if the exact-run runtime qualification below passes.

No local model execution is required for the remaining S1 development grain.

## 2. Zero-cost boundary

The following remain prohibited:

- Colab Pro;
- Colab Pro+;
- Pay As You Go;
- purchased compute units;
- GCP Marketplace;
- Colab Enterprise;
- paid GPU or TPU resources;
- paid cloud VMs;
- paid inference endpoints;
- paid APIs;
- paid OpenRouter;
- paid Jev/JevSearch;
- RunPod paid resources;
- any other Founder-billed compute.

The run must record that expected Founder spend is exactly zero before the first model call.

If the requested Colab resource requires payment, positive compute-unit balance, upgrade, or purchase, the run must stop.

## 3. Interactive Colab boundary

Use the normal Google Colab notebook execution interface.

Do not attempt to bypass Colab free-tier restrictions through:

- SSH;
- remote desktop;
- background distributed workers;
- external remote-control infrastructure;
- mechanisms intended to evade Colab usage limits.

Normal notebook execution, notebook cells, public artifact download, package installation required by the frozen environment, and repository/artifact verification are permitted.

## 4. Exact model remains unchanged

The only authorized model remains:

`Qwen/Qwen3.5-0.8B-Base`

Exact revision:

`dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`

The existing exact 12-file artifact identity and bundle hash must be verified again within the Colab run before model use.

No alternate:

- revision;
- instruct checkpoint;
- quantized checkpoint;
- converted checkpoint;
- smaller model;
- larger model;
- provider-hosted endpoint;
- merged model;
- Qwen-Image model;
- HCF path;

is authorized.

## 5. Precision remains unchanged

The currently authorized model dtype remains:

`bfloat16`

No automatic fallback is authorized.

In particular, do not silently change to:

- float16;
- float32;
- int8;
- int4;
- NF4;
- GPTQ;
- AWQ;
- bitsandbytes quantization;
- mixed precision differing from the frozen contract.

The Colab runtime must first determine and record whether the assigned accelerator/runtime can execute the exact authorized bfloat16 model path correctly.

If the assigned Colab accelerator does not support the required bfloat16 execution contract, stop prospectively.

A precision change would require a separate Founder amendment before any model output is observed under that changed interface.

## 6. Hardware is not preselected

Do not preregister or assume a specific Colab GPU model.

At the beginning of every candidate run, record the actually assigned runtime, including at minimum:

- accelerator presence;
- accelerator manufacturer/model;
- CUDA availability;
- CUDA runtime version;
- GPU memory total/free where applicable;
- system RAM total/available;
- CPU identity;
- Python version;
- PyTorch version;
- Transformers version;
- PEFT version;
- NumPy version;
- tokenizer identity;
- model artifact identity;
- filesystem free space;
- notebook/runtime identifier sufficient for the evidence record without exposing account secrets.

The scientific protocol must depend on measured capabilities, not an assumed Colab GPU name.

## 7. Environment binding

Before the first model call, create a fresh Colab environment manifest.

Bind the exact run to:

- current Git HEAD;
- exact authority identities;
- this Colab amendment;
- exact Qwen repository/revision;
- exact model bundle hash;
- exact tokenizer hashes;
- exact package versions;
- exact assigned hardware;
- exact accelerator capability;
- exact dtype;
- exact data roles;
- exact intervention;
- zero paid resources;
- no PHI;
- no private/gated clinical data;
- no confirmatory identities;
- no reserve identities.

Every real model call continues to require a fresh:

`PREFLIGHT_PASS`

for that exact Colab run.

## 8. Existing scientific design remains frozen

This amendment changes only the permitted execution environment.

It does NOT change:

- the V5 research question;
- the 64 selected calculators;
- source identities;
- calculator code;
- 8,192 development/calibration tasks;
- proposal generation;
- A/B balancing;
- `MATCH` / `MISMATCH` semantics;
- amended `ANSWER:\n` marker;
- A/B token identities where the exact tokenizer reproduces them;
- partitions;
- S1_TRAIN identities;
- S1_DEV_EVAL identities;
- S1_CAL_TUNE identities;
- S1_CAL_EVAL identities;
- semantic transformation;
- sequence limit;
- no-truncation rule;
- intervention definitions;
- B1 architecture;
- C1 architecture;
- C2 architecture;
- LoRA rank;
- LoRA alpha;
- dropout;
- target-layer scope;
- optimizer;
- learning rates;
- weight decay;
- gradient clipping;
- microbatch;
- gradient accumulation;
- epochs;
- seeds `11`, `29`, `47`;
- objective weights;
- SQuAD source/revision;
- maintenance identities;
- retention-evaluation identities;
- statistics protocol;
- multiplicity procedure;
- claim ledger;
- confirmatory quarantine.

## 9. Preparation must be reverified

Before model load on Colab, reverify the existing amended preparation artifacts.

Require all of the following to reproduce:

- 64 selected calculators;
- 8,192 development/calibration examples;
- 32,768 full-prompt A/B candidate checks;
- candidate token `A = 32`;
- candidate token `B = 33`;
- maximum medical prompt length no greater than the frozen `768` tokens;
- no truncation;
- no task deletion;
- no changed label;
- no changed case identity.

If the Colab tokenizer/environment produces different tokenizer identities or candidate-token behavior, stop.

Do not reinterpret the discrepancy as acceptable.

## 10. Replacement resource qualification

The prior local `1.5 GiB` system-memory-headroom blocker applies to the historical local runtime and remains preserved as evidence.

The Colab run must perform a new resource qualification appropriate to the assigned runtime before full training.

Execute in this order:

1. artifact integrity verification;
2. environment/hardware binding;
3. fresh exact-run preflight;
4. exact model load;
5. post-load resource observation;
6. one mechanical text-only smoke inference;
7. structural discovery of the exact final text transformer block;
8. one synthetic 256-token LoRA forward/backward step;
9. measured wall-time and memory observation;
10. projection of the bounded B1/C1/C2 development workload.

No full B1/C1/C2 run may begin before this sequence passes.

## 11. Colab resource stop rules

The run must stop if any of the following occurs:

- exact model identity mismatch;
- tokenizer identity mismatch;
- package/environment identity cannot be recorded;
- bfloat16 execution is unsupported;
- accelerator/runtime allocation fails;
- insufficient RAM or VRAM for safe execution;
- OOM;
- CUDA allocation failure;
- unrecoverable kernel/runtime failure;
- model cannot remain within the assigned resource envelope;
- exact final text block cannot be isolated;
- unexpected base parameters would need to become trainable;
- paid resource becomes necessary;
- Colab terminates the runtime;
- an incomplete run cannot be resumed with exact evidence integrity;
- the runtime would require weakening a scientific or resource gate.

Do not treat a Colab disconnect as scientific failure.

Record it as:

`RUNTIME_INTERRUPTION`

and repeat only from a clean fresh preflight/run boundary.

## 12. Timing rule

The historical local CPU-specific `12 hour per seed` projection rule was designed as a local feasibility/resource guard.

For the Colab path, do not silently reinterpret it.

Measure the synthetic step and projected workload.

If the existing canonical protocol can apply the same 12-hour bound unchanged to the Colab run, retain it.

If Colab's externally imposed runtime lifetime makes the planned deterministic run impossible even though computation is otherwise feasible, stop and record:

`COLAB_RUNTIME_DURATION_BLOCKER`

Do not split a scientifically atomic seed across unbound runtimes merely to evade platform limits.

Any checkpoint/resume mechanism not already frozen must receive prospective approval before use.

## 13. B1 / C1 / C2

Only after the exact Colab resource qualification passes may the already-authorized development execution continue.

B1, C1, and C2 remain development/calibration only.

Preserve the exact frozen seeds and optimization protocol.

Do not perform hyperparameter search.

Do not select favorable seeds.

Do not alter training parameters based on observed outcomes.

## 14. Evidence persistence

Colab runtimes are ephemeral.

Therefore all evidence needed to support a scientific claim must be persisted outside ephemeral VM storage before treating a run as completed.

Persist at minimum:

- run manifest;
- preflight;
- Git SHA/tree;
- environment manifest;
- hardware manifest;
- model/tokenizer hashes;
- configuration;
- seed;
- wall times;
- peak/available memory measurements where measurable;
- trainable parameter identities/count;
- raw-result hashes;
- aggregate-result hashes;
- stop/completion state;
- notebook/script identity.

Do not persist secrets, tokens, or Google account credentials.

Do not claim a completed run if the runtime disappears before required evidence is durably saved.

## 15. Existing negative results must remain preserved

The following prior results remain canonical historical evidence:

1. SAH rule-oracle execution failure;
2. frozen `ANSWER: ` prefix tokenizer failure;
3. local CPU model-load memory-headroom failure.

Moving to Colab does not erase or supersede those observations.

They remain part of the reproducibility and negative-results record.

## 16. Confirmatory quarantine remains unchanged

This amendment authorizes DEVELOPMENT / CALIBRATION execution only.

It does NOT authorize:

- confirmatory identity materialization;
- reserve identity materialization;
- confirmatory execution;
- reserve execution;
- confirmatory inspection;
- tuning on confirmatory data;
- tuning on reserve data.

Those boundaries remain intact.

## 17. Still outside scope

This amendment does NOT authorize:

- publication;
- PR merge;
- independent-family replication;
- HCF;
- Qwen-Image;
- model merging;
- PHI;
- private clinical data;
- gated clinical data;
- paid resources;
- production deployment;
- clinical-validity claims.

PR #320 must remain:

`OPEN / DRAFT / UNMERGED`

## 18. Review and verification

Before accepting any Colab result:

- run relevant V5 tests;
- verify deterministic preparation;
- verify artifact hashes;
- verify exact Git head;
- run compile validation;
- run whitespace/diff validation;
- run Alibaba Open Code Review under the existing zero-cost policy;
- use Jev only under the existing zero-cost/local-compatible policy;
- perform exact-head review;
- preserve all evidence.

No fabricated external reviewer verdict is permitted.

## 19. Current authorization transition

The prior state:

`RESOURCE_BLOCKED_MODEL_LOAD_MEMORY_HEADROOM`

may transition prospectively to:

`COLAB_RESOURCE_QUALIFICATION_AUTHORIZED`

This authorization does not itself establish:

- resource qualification;
- successful inference;
- successful training;
- scientific validity;
- V5 support.

Those must be measured.

## 20. Founder decision

I explicitly approve this runtime amendment.

`FOUNDER_V5_S1_COLAB_RUNTIME_AMENDMENT = APPROVED`

Authorized target:

`GOOGLE_COLAB_FREE_TIER_ONLY`

Founder-paid compute:

`ZERO`

Model:

`Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`

Precision:

`BFLOAT16_ONLY_UNLESS_SEPARATELY_AMENDED`

Development/calibration:

`AUTHORIZED`

Confirmatory/reserve:

`FORBIDDEN`

Publication:

`NOT_AUTHORIZED`

Merge:

`NOT_AUTHORIZED`

Proceed autonomously with the prospective Colab resource qualification and, only after it passes, continue the already-approved bounded V5 development execution. Stop at any genuine scientific, runtime, cost, privacy, or governance boundary.