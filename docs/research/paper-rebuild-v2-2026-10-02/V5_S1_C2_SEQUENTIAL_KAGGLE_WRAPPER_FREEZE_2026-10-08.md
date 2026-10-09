# V5 S1 prospective C2 sequential Kaggle wrapper freeze

Date: 2026-10-08 (Asia/Riyadh).
Status: `PROSPECTIVE_IMPLEMENTATION_BEFORE_ANY_C2_MODEL_OUTPUT`.

This record implements a runtime-only C2 path under the already approved bounded V5 development authority and the prospective zero-cost Kaggle runtime amendment. It does not create new scientific authority. The Founder authorization explicitly permits development-only training of `C2_CRDI_RETAIN_V1` with `SQUAD_RETENTION`, while confirmatory/reserve materialization or execution, PHI/gated data, paid resources, publication and merge remain forbidden.

## Preserved scientific implementation

The frozen scientific runner remains byte-identical:

- `scripts/v5_s1_adapter_development.py`: `c6a35bb1eea9c2392e6cecdb3e6b355f58adfc2aa8da574fe6e3568b6e9a75d1`.

The completed C1 Kaggle implementation is not edited by this C2 extension:

- `scripts/v5_s1_kaggle_preflight.py`: `7a4eb6c3948f29acd462cddbc83180dc7e811b67a69104cc086310c6f61606c9`;
- `scripts/v5_s1_kaggle_adapter_development.py`: `d075bebb1ad7eddf37b283ebc5d36de2ffb85627a5c31ae219598253538c51ea`;
- `scripts/v5_s1_kaggle_atomic_kernel.py`: `9c2b5048535bdec202bcdf98b2f20daab8b67c644fe108ad552e122747765bc6`.

The frozen retention implementation also remains byte-identical:

- `src/commandmed/reliability_v5/retention_dataset.py`: `94ec425cf75a2e495887de4ddbefa888a36cfddf81d3eb7c7836910f1d6f9207`;
- `scripts/v5_s1_retention_preparation.py`: `bb7fd593e009f7cd4632aa97dda4db7f86453349636ed7c6f3fe51dc163844c9`.

No C1 evidence or historical negative/resource record is modified.

## Authorized C2 identity

Only `C2_CRDI_RETAIN_V1` and seeds 11, 29, 47 are admitted, sequentially.

The model remains exactly:

- `Qwen/Qwen3.5-0.8B-Base`;
- revision `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`;
- exact bound 12-file bundle;
- direct bfloat16;
- no quantization, precision fallback, substitute checkpoint, merge, HCF or provider API.

The frozen adapter and optimizer remain unchanged: final text transformer block 23 only, LoRA rank 4, alpha 8, dropout 0, 100,352 trainable bfloat16 parameters, AdamW lr 5e-4, weight decay 0, betas 0.9/0.999, epsilon 1e-8, norm clip 1, micro-batch 1, accumulation 8 and one medical epoch.

The C2 objective remains:

`medical_NLL + 0.1 * semantic_contract_JS + 0.1 * retention_KL`.

No tuning or partial-result selection is introduced.

## Exact retention source and roles

The only admitted retention source is the public SQuAD v1.1 validation parquet:

- repository: `rajpurkar/squad`;
- revision: `7b6d24c440a36b6815f21b70d25016731768db1f`;
- file: `plain_text/validation-00000-of-00001.parquet`;
- SHA-256: `8c6646d36bd5a95061e076788cf3161d11f6f3e7d625dac7a83bbed0a49f69f7`;
- exact source cardinality: 10,570.

The source is acquired anonymously from the exact public revision and hash-verified before any C2 model action. Raw passage/question/answer payload is ephemeral and is never committed or exported by CommandMed.

The frozen identity ranking remains SHA-256 of the raw upstream ID with ID tie-break: first 64 identities are `S1_C2_MAINTENANCE`; next 256 are `S1_RETENTION_EVAL`. Complete metadata qualification occurs before model load. The 64 maintenance examples use the frozen teacher-forced KL contract; the 256 evaluation identities never enter training, checkpoint selection, prompt changes, margin selection or medical hyperparameter selection.

Paired retention interpretation remains narrow SQuAD v1.1 retention only, never general capability preservation.

## C2 Kaggle runtime isolation

New C2-specific files are separate from the completed C1 wrappers:

- `scripts/v5_s1_kaggle_c2_preflight.py`;
- `scripts/v5_s1_kaggle_c2_adapter_development.py`;
- `scripts/v5_s1_kaggle_c2_atomic_kernel.py`.

Every C2 seed requires:

1. exact local and live-remote Git head equality;
2. clean checkout outside its bounded evidence directory;
3. all three C1 seeds committed, model-free verified and reviewed;
4. every earlier C2 seed committed, model-free verified and reviewed;
5. exact frozen Kaggle amendment bindings;
6. exact model/revision/artifact and medical interface reproduction;
7. exact public SQuAD revision/file/hash and 64/256 retention-role metadata;
8. private kernel, legitimate free quota and zero incremental Founder spend;
9. physical GPU inventory recorded while the scientific child exposes only physical GPU 0 as `cuda:0`;
10. direct bfloat16 support and exact runtime/package identities recorded;
11. fresh preflight before each model load/inference/training action;
12. preliminary and then complete C2 atomic duration admission;
13. no resume, session cycling, quota bypass, shortened matrix or multi-GPU execution.

The physical second T4 remains unused for scientific computation. DDP, DataParallel, tensor parallelism and model sharding remain forbidden.

The existing optional TorchAO pre-model removal remains a runtime-only compatibility repair for an unused optional quantization extension. It does not change the direct-bfloat16 scientific path.

## C2 resource and evidence contract

The shared mechanical resource qualification remains non-scientific. The frozen C2 runner then separately measures, before scientific training acceptance:

- greedy retention decoding on the four longest preselected evaluation prompts;
- maintenance teacher/candidate KL backward on the longest preselected maintenance prompt without an optimizer update;
- complete C2 training projection;
- complete 16,384-prompt medical matrix projection;
- paired 256-example base/candidate retention decoding projection;
- the existing completion/export margin and memory/disk safeguards.

A seed is complete only if all 256 medical training identities, 32 optimizer updates, the full 16,384 medical-prompt matrix and all 256 paired retention-evaluation identities finish in one atomic session. Partial C2 evidence remains incomplete and is never promoted.

Only retention source IDs/hashes, configurations, aggregate EM/F1, paired aggregate deltas and aggregate raw-output hashes may leave ephemeral storage. Passage text, questions, gold answers, decoded answers and per-example QA score arrays remain prohibited from export.

## Sequential promotion

C2 seed 11 may start only after this prospective implementation is model-free tested, reviewed, committed and pushed.

C2 seed 29 may start only after seed 11 has a durable exact export, independent model-free verification receipt, validation/review record, ordinary commit and push.

C2 seed 47 has the same gate on both earlier C2 seeds.

Every promoted seed receives fresh V5/full repository tests, compilation, whitespace/binding checks, zero-cost Alibaba OpenCodeReview delegate/rules plus honest host review, ordinary push and a draft PR #320 update. Jev remains `DEFERRED_ZERO_COST_POLICY` unless a genuine compliant zero-cost/local path exists.

Scientific freeze remains OPEN. This record authorizes no confirmatory/reserve materialization or execution, publication, PR merge, PHI/gated/private data, paid API/compute, independent-family replication, HCF or clinical-validity claim.
