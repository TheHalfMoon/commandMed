# V5 — Source-bound descriptive statistical reviewer packet (2026-10-10)

**Status: `REVIEW_PACKET_ONLY / NO_PRIMARY_HOLM_FAMILY_FREEZE / NOT_90_PERCENT_POWER / NO_CONFIRMATORY_AUTHORITY`.**

This is an audit-ready model-free bridge between the 72 original paired source-case SD descriptions and 72 original calculator ANOVA-method-of-moments ICC estimates. It **does not** select non-target hypotheses, treat three independent model-training seeds as 11,520 independent cases, estimate a scientifically adequate crossed source/calculator/seed covariance model, adjust significance thresholds, infer generalization to other calculators, or qualify any effect for confirmatory access.

## Original immutable inputs and bounded reproduction

- Development paired SD source: `artifacts/v5/development/s1-paired-sd-inventory-2026-10-09/development-paired-sd.json` (SHA-256 `b1edf781b61d3f5ce227c08908ca43ad9864c0b398a7318c33895951af37bacd`).
- Original development calculator ICC source: `artifacts/v5/development/s1-calculator-icc-inventory-2026-10-10/development-calculator-icc.json` (SHA-256 `37d64c0f6ac14d04cc6420a020e7bb7997fb333e50729f33798b2d403d292370`).
- Deterministic composite output: `artifacts/v5/development/s1-statistical-review-packet-2026-10-10/reviewer-packet.json` (new additive development-only file, not among the immutable 307). SHA-256: `86a275cb5cd7760f421538df34fea8b6dc452a19d095ddc4f4c6f0e69a87e348`.
- Generator: `scripts/v5_s1_statistical_review_packet.py`; no model weights, network, GPU, PHI, new source-case IDs, or external API calls. From the repository root, run `python3 scripts/v5_s1_statistical_review_packet.py --verify artifacts/v5/development/s1-statistical-review-packet-2026-10-10/reviewer-packet.json`. `--output` writes **only to a previously nonexistent path**; `--verify` never modifies it.
- The generator first executes the full source-bound audit: all 307 frozen entries and 9 locked development sources must have their original hashes. It rejects mismatched source mean effects across independently stored SD and ICC descriptions, missing/duplicate cells, changed seed membership, erased negative ICCs, forged review status, and mismatched three-seed descriptive sample SDs. GitHub CI reruns the audit, generator replay, and mutation tests on the exact PR head.

## What reviewers can now inspect (not an inferential result)

All **24 development groups** are enumerated without selecting favorable effects: three intervention paths `B1_TYPED_V1`, `C1_CRDI_V1`, `C2_CRDI_RETAIN_V1`; two splits `S1_DEV_EVAL`, `S1_CAL_EVAL`; and four measured metrics `canonical_accuracy`, `canonical_nll`, `canonical_brier`, `semantic_js`. Each group includes **three separate seed records** (`11`, `29`, `47`) with the observed raw-orientation paired effect mean, within-seed paired source-case SD, unchanged *unclipped* calculator-effect ICC, and a negative-ICC indicator; the group also includes a descriptive across-three-seed mean-effect sample SD and the minimum/maximum of the three separate within-seed SDs. In total 72 records are cross-checked, including the 12 negative ICC estimates. Every evaluation split retains its 64 selected calculators × 60 source cases = 3,840 source-case identities, distinct from the **unmaterialized** prospective 4,096 cases (64 × 64).

These numbers cannot be combined by an unreviewed arithmetic pooling formula into final 90% power: the covariance of three model-training seeds, source cases nested under selected calculators, shared baselines, coupling across axes, missingness, native metric orientation, fixed-policy settings, and sampling/generalization population must be specified **before** that calculation. `semantic_js`, NLL and Brier are lower-is-better in their original measurement conventions; no signed effect is silently reoriented for hypothesis selection. Negative finite-sample ICC estimates must remain visible and are not negative population variance components.

## Required independent methodological decisions (Issue #326)

1. Enumerate the complete eligible **non-target** primary hard-gate cells, their exact intervention, target and non-target axis, metric orientation, fixed policy, split/inferential population and coupling; calculate the actual Holm family size from that reviewed list. Do not select cells based on this packet's rankings.
2. Decide whether the inference is conditional on the selected 64 calculators or generalizes beyond them. Document source-case clustering and calculator sampling assumptions.
3. Prespecify whether effects average over or condition on seeds; handle shared baselines, crossed case/seed dependence and covariance with only three training seeds. Acknowledge when evidence is insufficient.
4. Prespecify all native-unit noninferiority margins, invalid/missing output and abstention/retention/coupled-axis conventions, separately distinguishing benchmark scales from patient safety tolerances.
5. Re-evaluate 90% power **for every actual primary effect** using the full reviewed Holm family and conservative uncertainty bound at 4,096 source cases; if insufficient, apply the prospective power-failure rule without weakening margins or selecting fewer cells.
6. Obtain actual independent scientific/methodological and code/rights review, cryptographically verified signing and authorized founder compute/science decisions. These are not supplied by reproducible development evidence.

**Non-claims:** No improvement in near-chance rule conformance, no qualified B1 NLL claim, no clinical validity, no independent replication, no completed reviewer certification, no accepted manuscript, no release, no unreviewed confirmatory/reserve access. All authority flags in the machine-readable packet remain `false`, and the exact family count and crossed covariance model remain `null`.
