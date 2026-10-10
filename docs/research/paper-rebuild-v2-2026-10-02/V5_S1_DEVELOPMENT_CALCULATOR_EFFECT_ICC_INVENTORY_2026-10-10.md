# V5 S1 calculator-level paired-effect correlation — original development evidence

**Status:** `DEVELOPMENT_ONLY_DESCRIPTION / NOT_APPROVED_FOR_POWER / NO_CONFIRMATORY_AUTHORITY`. This is a transparent additional dependency diagnostic for independent statistical review, **not** a change to frozen endpoints, case allocation, preregistration, or scientific conclusions.

## Source-bound reproduction

- Program: `scripts/v5_s1_development_calculator_icc_inventory.py`
- Machine-readable result: `artifacts/v5/development/s1-calculator-icc-inventory-2026-10-10/development-calculator-icc.json`
- Result SHA-256 on the authoring Mac: `37d64c0f6ac14d04cc6420a020e7bb7997fb333e50729f33798b2d403d292370`
- Canonical earlier descriptive SD evidence: `artifacts/v5/development/s1-paired-sd-inventory-2026-10-09/development-paired-sd.json`, **pinned byte SHA-256** `b1edf781b61d3f5ce227c08908ca43ad9864c0b398a7318c33895951af37bacd`
- Original inputs: one unchanged-baseline development decision matrix, an independently verified R1 baseline repeat cross-check, and the **nine original B1/C1/C2 × training seeds 11/29/47** complete development decision matrices. All **11 original source SHA-256** identities are **pinned in the calculator analyzer** and repeated in `input_hashes` of the result. A mismatch fails closed. No new inference, training, held-out/reserve identities, PHI, external APIs or GPU calls.
- Run at repository root: `python3 scripts/v5_s1_development_calculator_icc_inventory.py --output /tmp/v5-calculator-icc-replay-new.json` (choose a **new nonexistent** destination). The CLI uses exclusive-create to preserve any earlier evidence/receipt. The source analyzer refuses incomplete input or mismatched intervention/seed, ordered source cases or canonical/transformed prompt identities.
- Pure synthetic guardrails: `PYTHONPATH=src python3 -m pytest -q tests/reliability_v5/test_development_calculator_icc_inventory.py`. The separate source-bound CI checks a fresh replay against the committed receipt at tolerances to avoid treating cross-platform floating-point last-bit differences as new scientific findings.

## Descriptive ANOVA estimator and scope

For every candidate intervention and seed, source tasks in `S1_DEV_EVAL` and `S1_CAL_EVAL` are paired with unchanged-baseline task/target/prompt/calculator identities. Each split contains **3,840 unique source cases**: exactly **64 selected RiskCalcs calculators** with **60 source cases per calculator** (distinct from **64 per calculator** in the still unmaterialized future 4,096-source-case confirmatory plan). The two nonindependent prompt variants are summarized per source case before calculating the delta. Four original metric definitions are reused without change.

Within a cell, let `d_gi` be candidate-minus-baseline paired metric effect, `g` index calculator, `i` source state, and `K=64`, `m=60`. Define `MS_B = m * Σ_g (mean_g - grand_mean)^2/(K-1)` and `MS_W = Σ_gΣ_i(d_gi-mean_g)^2/[K*(m-1)]`; **descriptive unclipped** method-of-moments `ICC = (MS_B-MS_W)/(MS_B+(m-1)*MS_W)` if denominator positive, or `UNDEFINED_ZERO_TOTAL_VARIANCE`. Finite negative estimates are retained rather than quietly set to zero; they are **not negative population variance components**.

Every computed cell reconstructs its existing saved paired source-task SD from ANOVA components, with fail-closed tolerance and a pinned SHA-256 for the prior SD source. All **72/72 cells reproduced**; maximum absolute floating-point difference `3.552713678800501e-15`.

| Frozen metric | Cells | Observed development ICC min | Median | Max | Nonnegative cells |
|---|---:|---:|---:|---:|---:|
| Canonical accuracy | 18 | -0.012645 | -0.005465 | 0.020549 | 6 |
| Canonical Brier | 18 | 0.002960 | 0.018305 | 0.073701 | 18 |
| Canonical NLL | 18 | 0.001242 | 0.026186 | 0.110407 | 18 |
| Semantic JS | 18 | 0.052526 | 0.190126 | 0.238078 | 18 |
| **Total** | **72** | **-0.012645** | **0.023117** | **0.238078** | **60** |

Highest observed **development** cell: `C2_47 / S1_DEV_EVAL / semantic_js` (`rho ≈ 0.2380777`). Under a **toy equal-size exchangeable calculator cluster sensitivity only**, `DEFF = 1 + 59*rho ≈ 15.0466` and `3840/DEFF ≈ 255.2` case-equivalents for that cell. This is **not a measured confirmatory design effect, transport estimate, or valid N=4096 power calculation**. Different axes can exhibit very different calculator dependence; no single favorable ICC can be reused for the whole Holm family.

Separately, the *sample SD of just three seed-level whole-split descriptive paired-effect means* is given for each intervention/metric/split. Three seeds **do not** support claiming a qualified population stochastic-run covariance or correct 90% power.

## Independent-review decisions still required

1. **Inference target:** effects conditional on these 64 nonrandomly selected calculator rules versus scientific generalization to broader calculators/specialty populations. Source-case identifiers alone establish no random calculator sampling.
2. **Crossed nuisance model:** effect dependency among source cases within calculators, across three stochastic training seeds, shared baselines, missing/failed outputs and coupled endpoints; validation of inference and conservative power under those assumptions.
3. **Prospective complete primary non-target Holm family:** exact applicability, endpoint orientation, effect margins and alpha 0.05/90% power at planned 4,096 source cases; or scientifically reviewed power-failure/redesign as required by the existing frozen protocol.
4. **Governance:** rights, actual independent methodologist and Alibaba OCR code review, verified signing/founder gates and no confirmatory/reserve access until prospective approval.

**Non-claims:** The original near-chance rule-oracle accuracy, unfavorable B1 NLL, all primary negative results and the scientific freeze are preserved unchanged. Neither this new result, successful tests nor a high ICC proves a causal calculator dependency, clinical correctness, real-world transport, effective seed sample size, final familywise power, or permission to publish/merge. All final qualification/authority flags remain `false`.

Issue context: [#326](https://github.com/TheHalfMoon/commandMed/issues/326#issuecomment-6099547179).
