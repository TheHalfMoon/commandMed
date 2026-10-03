# V5 capability-retention task admission

Status: `ADMITTED_WITH_NARROW_CLAIM_AND_RIGHTS_CONTROLS`.

## Identity

- Dataset: `rajpurkar/squad` (SQuAD v1.1)
- Hugging Face revision: `7b6d24c440a36b6815f21b70d25016731768db1f`
- Revision retrieval check: HTTP `200` on the pinned README path on 2026-10-03.
- Task: extractive reading-comprehension retention control.
- Planned split: validation only (`10,570` examples in the pinned metadata record).
- Paper: Rajpurkar et al., *SQuAD: 100,000+ Questions for Machine Comprehension of Text*, arXiv:1606.05250 / EMNLP 2016.

## Rights posture

The Hugging Face dataset metadata labels `rajpurkar/squad` as `cc-by-sa-4.0`. The upstream `SQuAD-explorer` repository software has an MIT license; that software license is **not** used as a substitute for the dataset/content license.

CommandMed will not vendor SQuAD passages, questions, or answer text into this repository. Evaluation retrieves the pinned dataset separately, and publication artifacts expose source IDs/hashes, configuration, aggregate metrics and attribution rather than redistributing the source payload.

Any redistribution beyond that narrow plan requires a separate CC BY-SA 4.0 compliance review.

## Scientific role

SQuAD is admitted only as a **paired nonmedical extractive-QA retention control** for parameter-changing interventions such as C1/C2. It does not establish broad general intelligence, clinical ability, or uncontaminated generalization.

The retention estimand is the paired before/after change on the same pinned validation examples using a frozen prompting/decoding/scoring contract. Exact Match and token-level F1 are reported separately; no single composite score can compensate for a primary medical assurance failure.

Because SQuAD is a long-public benchmark and may have appeared in pretraining corpora, absolute performance is contamination-prone. The paper therefore interprets it only as a within-model retained-capability check and states that contamination can mask degradation.

## Access rule

No SQuAD output may be used to select medical intervention hyperparameters, checkpoints, prompts, margins or confirmatory claims. For learned interventions, SQuAD evaluation occurs after the implementation freeze. If developers inspect SQuAD outcomes and then change the model-facing implementation, those outcomes become development evidence and a fresh retention boundary is required.

## Claim boundary

Allowed wording if executed: "retained SQuAD v1.1 extractive-QA performance under the declared intervention." Forbidden extrapolation: "general capability preserved" or "no catastrophic forgetting" without broader independently admitted evidence.

## S1 development partition amendment — 2026-10-03

The Founder-authorized V5 S1 development grain uses only the already admitted pinned SQuAD v1.1 validation split, but separates C2 maintenance from retention evaluation to prevent direct training/evaluation overlap.

Before any model output, identities are ranked deterministically by SHA-256 over the upstream example ID under a frozen namespace. The first 64 identities are `S1_C2_MAINTENANCE`; the next 256 disjoint identities are `S1_RETENTION_EVAL`; all remaining validation identities are unused in S1. The exact source revision remains `7b6d24c440a36b6815f21b70d25016731768db1f`.

`S1_C2_MAINTENANCE` may contribute only the frozen C2 teacher-KL maintenance term. `S1_RETENTION_EVAL` is never used for training, checkpoint selection, prompt changes, medical hyperparameters, margins, or power decisions. Public CommandMed artifacts continue to store source identities/hashes and aggregate metrics rather than SQuAD passages, questions, or answer text.

This amendment narrows the earlier validation-split plan for S1 and does not authorize confirmatory use or a broad capability-preservation claim.
