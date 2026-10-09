# C2 seed 29: complete development evidence

Private Kaggle kernel `abdulazizshehri/commandmed-v5-c2-seed-29-atomic`, version 1, completed frozen C2 seed 29 at source `8576b20ff8fd797a5680497f584b024f0a4bfc5c`, tree `1d55f066225cff7f24d971cf708ddcf6dc7d2e67`. The atomic run completed all 32 medical optimizer steps, the full 16,384-prompt medical matrix, 256 baseline retention evaluations and 256 candidate retention evaluations in 7030.694074897 seconds. The frozen non-adapter parameter identity before and after adaptation is unchanged.

Exact original ZIP SHA-256: `3550c9bcb731ffe88f71a39120472a69742ae06228e415f379b70d5a77947e10`. Original export, allowlisted runtime/hardware records, byte-identical extracted evidence, separate model-free verification receipt, launch-preparation record and live-retrieval receipt are preserved under `artifacts/v5/development/s1-kaggle-c2-adapters/c2-seed-29-v1-2026-10-09/`. Model-free verification passed ZIP CRC and safe unique members, exact source/environment/authority/model/tokenizer/retention-source bindings, all 16,384 ordered medical identities, 256 retention-evaluation identities, finite logits, frozen training identities, and deterministic medical analysis at absolute tolerance 1e-12. It loaded no model weights and performed no scientific replication. The original `durable_export_verified=false` payload is preserved unchanged.

| Partition | Canonical accuracy | Transformed accuracy | Canonical NLL | Transformed NLL | Mean semantic JS |
| --- | ---: | ---: | ---: | ---: | ---: |
| S1_DEV_EVAL | 0.49375 | 0.49375 | 0.7050206452730452 | 0.709061282719384 | 0.0012510550127065904 |
| S1_CAL_EVAL | 0.49557291666666664 | 0.4940104166666667 | 0.7055054236274896 | 0.7099847694772851 | 0.001248359503479463 |

Medical rule-conformance accuracy remains close to one half. Low semantic divergence does not establish correct rule conformance or clinical validity.

Narrow SQuAD v1.1 paired retention results: baseline exact match 0.1953125, candidate exact match 0.1953125; baseline token F1 0.31273046371355107, candidate token F1 0.30947705943105197; paired mean delta exact match 0.0, paired mean delta token F1 -0.003253404282499095. This is a narrow paired SQuAD v1.1 retention control only and is not evidence of general capability preservation.

The parent Kaggle allocation exposed two Tesla T4 devices, while the scientific child used only physical GPU 0 as `cuda:0`; GPU 1 was not used for scientific computation. Exact `Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`, direct BF16, the frozen `ANSWER:\n` interface, A/B token IDs 32/33, frozen C2 LoRA scope/objective/optimizer, exact SQuAD source/hash, no-resume atomic execution and zero incremental Founder spend remained unchanged. Raw SQuAD payload and per-example decoded answers were not exported.

This is development/calibration evidence only. No confirmatory, reserve, clinical-validity, broad-retention, publication or deployment claim is created. C2 seed 47 remains sequentially gated on durable review/commit/push of seed 29. Scientific freeze remains OPEN; PR #320 remains DRAFT/UNMERGED.
