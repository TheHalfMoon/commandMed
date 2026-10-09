# V5 S1 complete baseline and B1 development - 2026-10-04

Status: `B1_COMPLETE_DEVELOPMENT`; next C1/C2 admission is `COLAB_RUNTIME_DURATION_BLOCKER`.

The foreground free Colab run used exact reviewed source `848692336c2b8537ee4d559338abed29da0c93d6`. A standard reconnect allocated a fresh T4 after the prior idle VM disconnected before B1 began; no scientific checkpoint or cross-runtime resume was used. Fresh source/model/tokenizer/environment, all 8,192 task identities, 32,768 candidate-token checks, complete prompt lengths and exact-run PREFLIGHT_PASS gates preceded model load. The maximum medical prompt remained 593/768 tokens without truncation. The checkpoint remained direct bfloat16 with its frozen identity and CPU thread restrictions.

All 16,384 baseline prompts and all 16,384 prompts for each of B1 seeds 11, 29 and 47 completed. Each head used the unchanged 256 canonical training examples, 256 calibration-tuning examples, 40 epochs and 320 optimizer updates. Earliest minimum calibration-tuning NLL selected epochs {"11": 1, "29": 1, "47": 1}. Base parameter identities before and after the entire stage are identical. Actual complete-stage wall time was 6246.703 seconds.

Original raw matrices, analyses, per-epoch fitting records, preflights, preparation, resource observations and console are preserved in `artifacts/v5/development/s1-colab-resource-qualification/b1-complete-2026-10-04/`. The original ZIP SHA-256 is `7e6e21ed73d8b672b4cf6836cc199f3450a02fb5ad0ea1d3b157009a431ed913`. Original durability flags remain untouched; a separate receipt confirms exact-byte export outside Colab. Independent model-free verification regenerated all ordered task/case/split/variant/legend/target/prompt identities, verified finite two-class logits and unchanged feature identities, and reconstructed all four analyses within a declared 1e-12 cross-platform floating-point tolerance. This is evidence verification, not an independent scientific replication. Analyses retain every split; development/calibration data do not become confirmatory evidence.

Execution completion does not imply that B1 improved reliability. All three heads selected epoch 1. Their development/calibration NLL values are much higher than the baseline, with accuracy near one half. These negative outcomes are retained without changing the frozen optimizer, budgets, selection rule or data.

| Intervention | Partition | Canonical accuracy | Transformed accuracy | Canonical NLL | Transformed NLL | Mean semantic JS |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Baseline | S1_DEV_EVAL | 0.481250 | 0.478646 | 0.783177 | 0.773748 | 0.00120711 |
| Baseline | S1_CAL_EVAL | 0.493229 | 0.492969 | 0.774434 | 0.764087 | 0.00119291 |
| b1-seed-11 | S1_DEV_EVAL | 0.481250 | 0.481250 | 84.995964 | 84.471615 | -1.39432e-66 |
| b1-seed-11 | S1_CAL_EVAL | 0.493229 | 0.493229 | 83.038021 | 82.540234 | -1.5345e-66 |
| b1-seed-29 | S1_DEV_EVAL | 0.518750 | 0.518750 | 110.451432 | 110.685677 | -6.64497e-95 |
| b1-seed-29 | S1_CAL_EVAL | 0.506771 | 0.506771 | 113.191927 | 113.427865 | -7.83944e-95 |
| b1-seed-47 | S1_DEV_EVAL | 0.481250 | 0.481250 | 119.048828 | 119.853776 | -1.26936e-95 |
| b1-seed-47 | S1_CAL_EVAL | 0.493229 | 0.493229 | 116.296354 | 117.084245 | -1.43653e-95 |

Each displayed evaluation partition has 3,840 canonical and 3,840 transformed observations. Full precision NLL, Brier, accuracy and semantic-JS records for every split remain in the original analyses. Tiny signed semantic-JS residues are floating-point roundoff retained verbatim; near-zero divergence with saturated decisions does not imply correctness. The frozen implementation's fitting/epoch-selection NLL uses float32 softmax and a 1e-15 probability floor; descriptive matrix NLL uses the pure probability scorer without that floor. Both original records and implementation identities are retained; no retrospective metric or optimizer change was made. Metadata-only SQuAD qualification passed at the same run source: 64 maintenance and 256 evaluation identities, maximum 455 prompt tokens, exact pinned public source/tokenizer, no truncation, model load, inference or training; source passages and answers are not exported.

Fresh runtime admission reports 3000 seconds remaining. Using this same run's medical resource projection, the complete C1 seed minimum including its 600-second admission margin is 7048.294 seconds and C2 is 7689.862 seconds even before retention decoding. Both exceed the remaining window. No next-stage model load, C1/C2 medical optimization, or SQuAD model inference was requested. The complete atomic-seed requirement remains binding; no shortened matrix, checkpoint/resume, session cycling, quota bypass or precision fallback was used.

The prospective adapter implementation was separately frozen and reviewed at `625bbe7cd4d162d2cd6e6157e3f52c8b0f8c72eb` before adapter or retention outputs. That head passed 156 V5 and 1,208 repository tests, full tokenizer-only regeneration, deterministic bindings, compile and notebook validation. Alibaba OCR v1.12.11 zero-cost delegate preview/rules informed host-agent exact-head review; no independent external model verdict is claimed. Native CI had no triggered workflow runs.

The authorized account exposes an existing Google AI Pro plan, while Colab reports no recognized subscription and zero compute units. Official Colab guidance says eligible paid Google AI benefits apply automatically, but the discrepancy's cause remains unresolved. This execution used only the actual exposed free allocation. No account identifier, billing details, subscription change, purchase, paid API or incremental Founder spend is included in this record.

Historical SAH, frozen space-prefix, CPU headroom, Colab artifact-order and optional TorchAO-import failures remain preserved. The later successful resource qualification does not erase them. PR #320 remains OPEN / DRAFT / UNMERGED. C1/C2, retention outcomes, confirmatory/reserve, replication, HCF/Qwen-Image, publication and merge remain unexecuted at this frontier. No clinical or thesis-wide success is claimed.
