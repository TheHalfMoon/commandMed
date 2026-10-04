# V5 S1 prospective model integration freeze - 2026-10-04

Status: `PROSPECTIVE_IMPLEMENTATION_BEFORE_MEDICAL_TRAINING_OR_RETENTION_OUTPUTS`.

This implements the already approved S1 protocol. It changes no existing medical interface, task identity, partition, optimizer, seed, parameter budget or stop rule. Historical resource and negative evidence remains unchanged. Each new stage repeats the current exact artifact, all medical preparation, dependency, model-load, smoke, synthetic LoRA and duration gates before further model execution. Full matrices cannot be replaced by timing samples. Execution remains interactive, zero spend, without checkpoint/resume, confirmatory/reserve, publication or merge.

## Baseline and B1 implementation

`scripts/v5_s1_b1_development.py` admits one complete baseline/B1 stage only. The base model is bfloat16, in eval mode, with every backbone parameter frozen. Each of the existing 8,192 tasks contributes its unchanged canonical and transformed prompt. A single native forward produces the final answer-marker hidden representation and A/B candidate logits. No batching, truncation, altered kernel, precision fallback or prompt change is introduced. Raw feature hashes bind each reused representation; base parameter identities before and after must match.

The typed Linear head includes bias and maps its two components to the existing A/B labels; the per-example MATCH/MISMATCH mapping remains bound in raw rows. Training and checkpoint-selection use only the canonical representations of the existing 256 S1_TRAIN / 256 S1_CAL_TUNE identities. Evaluation uses both forms of all tasks. This does not add transformed training examples or tune on evaluation identities. Three fresh bfloat16 heads use seeds 11/29/47, AdamW lr 1e-2, weight decay 1e-4, batch 32, and 40 epochs. Seeded permutations change order only. Lowest calibration-tuning NLL selects the in-memory head; earliest epoch wins exact ties. No state is resumed across runtimes. NLL uses the existing objective probability floor 1e-15. Full paired logits and development-only accuracy/NLL/Brier/semantic-JS analyses are persisted. These measurements do not by themselves qualify the full assurance matrix, margins or power.

Before actual head fitting, a separate mechanical bfloat16 256-by-hidden-size fixture times the same bounded 40-epoch head procedure. It is resource evidence only. The complete stage projection combines the declared medical matrix estimate and three buffered head fits, reserves time for export, and must fit the newly observed runtime window. Actual feature extraction updates the remaining duration projection prospectively. A partial matrix or resource interruption is never accepted as complete B1 development.

## Retention metadata and model-facing contract

`src/commandmed/reliability_v5/retention_dataset.py` and `scripts/v5_s1_retention_preparation.py` implement protocol section 8 without model calls. The exact public validation Parquet SHA-256 is `8c6646d36bd5a95061e076788cf3161d11f6f3e7d625dac7a83bbed0a49f69f7`; the resolved source remains rajpurkar/squad@7b6d24c440a36b6815f21b70d25016731768db1f. No train split is used. The source namespace identifies that pinned validation pool. Consistent with the executable protocol's raw-upstream-ID wording, ranking hashes only the UTF-8 upstream ID; no new hash salt/suffix is invented. Exactly the first 64 / next 256 IDs define disjoint maintenance / retention roles. All 10,570 IDs must be unique and source cardinality must match.

The previously unimplemented QA interface is frozen here before any SQuAD model output:

```text
Answer the question using a short span from the passage.
PASSAGE:
{context}
QUESTION:
{question}
ANSWER:
```

The final colon has one newline. No gold answer appears in the prompt. Full passages/questions remain untruncated; source payload is not vendored. The existing 768-token maximum applies to medical prompts as specified in protocol section 9; it is unchanged. Retention prompt plus its separately specified answer bound must fit the exact checkpoint's declared text context. Greedy retention decoding has max_new_tokens=32, no sampling, and the exact checkpoint EOS. The fixed scoring span is the first nonempty completion line. Official SQuAD lowercasing, ASCII punctuation/article removal, whitespace normalization, maximum Exact Match / token F1 over gold annotations are used. No SQuAD score changes this contract or medical hyperparameters. Only IDs/hashes and aggregate metrics may leave ephemeral dataset storage.

Maintenance uses the first upstream gold annotation and at most its first eight continuation tokens. Metadata preparation must verify that appending the complete annotation preserves the prompt token prefix; a mismatch stops before SQuAD model use. This record freezes metadata/prompt/decoding/scoring mechanics only. C2 teacher-KL integration, resource timing and paired retention evaluation remain required and separately gated. B1 makes no SQuAD call.
