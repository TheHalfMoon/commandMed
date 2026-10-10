# V5 manuscript development-results crosswalk — 2026-10-09

Status: `DRAFT_MANUSCRIPT_ADDENDUM; DEVELOPMENT_EVIDENCE_ONLY; NO_CLAIM_PROMOTION`.

## Why this separate addendum exists

The frozen manuscript file `manuscript-v5/Results.md` says that no empirical results are reported in that **prospective confirmatory draft**. That section was accurate when frozen, but the development program has subsequently produced model-inference and descriptive results. The correct current distinction is **development-only empirical observations exist; no confirmatory paper results exist**.

The manuscript `Results.md`, `README.md`, `claim-ledger-v5.md`, `REVIEWER_RED_TEAM_V5.md`, and other original bound entry files must remain **byte-identical** under the existing Kaggle frozen-binding manifest. This is a separate addendum; it does not quietly overwrite the frozen text, alter study endpoints, authorize a publication, or promote V5-C01–V5-C07. Future properly authorized manuscript reconciliation may cite this addendum while keeping the analysis origin and proof level explicit.

## Development-only results eligible for accurate descriptive reporting

| Observation | Retained evidence | Defensible description | Unsupported promotion |
| --- | --- | --- | --- |
| Frozen base rule conformance | `V5_S1_REPEATABILITY_R2_AND_PAIRED_DEVELOPMENT_RESULTS_2026-10-09.md` and independently verified R1/R2 original exports | DEV canonical accuracy 0.48125; CAL canonical accuracy 0.49322916666666666. These are near chance on this binary rule-oracle interface. | No clinical correctness/safety, useful reasoning, intervention superiority, or confirmatory accuracy |
| B1 learned typed intervention (seeds 11/29/47) | `V5_S1_FINAL_DEVELOPMENT_SYNTHESIS_2026-10-09.md` and `artifacts/v5/development/s1-development-synthesis-2026-10-09/final-synthesis.json` | Development canonical accuracy mean 0.4937500000000001 and NLL mean 104.83207465277776; unfavorable and strongly seed-variable. | No equivalence, clinical advantage or competitive learned-intervention baseline |
| C1 learned intervention (seeds 11/29/47) | Same cross-seed synthesis and independently verified full seed archives | Development canonical accuracy mean 0.4875868055555556 and canonical NLL mean 0.732595954195257. | No reliable rule-conformance improvement, superiority or safety |
| C2 learned intervention (seeds 11/29/47) | Same synthesis plus the bounded SQuAD v1.1 retention control | Development canonical accuracy mean 0.4848958333333333 and canonical NLL mean 0.7415694349926284. Narrow retention baseline/candidate EM both 0.1953125; paired token-F1 delta mean 0.00029787291399702154 with mixed signs across seeds. | No general capability retention, noninferiority or broad reliability |
| Base-only same-seed repeatability | `artifacts/v5/development/s1-kaggle-repeatability-runs/paired-r1-r2-repeatability95-2026-10-09.json`; source-bound R1/R2 verification | Two private Kaggle executions, each with 16,384 complete ordered rows over 8,192 source tasks; every ordered decision/logit row matched. For all 4 primary and 3 secondary metrics `repeatability95=0` under the **pre-frozen** paired nearest-rank estimator. | No robustness across different random seeds, model families, hardware, prompts, patient populations or clinical decisions |
| Research-scale meaningful margins | `artifacts/v5/development/s1-kaggle-repeatability-runs/final-development-benchmark-margins-2026-10-09.json` and pre-output `V5_DOMAIN_FLOOR_FREEZE_2026-10-09.md` | `m_accuracy=0.01`; `m_NLL=0.009950330853168092` nats; `m_Brier=0.02`; `m_semantic_JS=0.006931471805599453` nats. These equal the prospectively frozen **nonclinical** benchmark floors because the measured repeatability term is zero. | No clinician-adjudicated minimum important difference or medical deployment tolerance |
| Descriptive paired source-task SDs | `artifacts/v5/development/s1-paired-sd-inventory-2026-10-09/development-paired-sd.json`; seed/source/prompt identity-bound analysis | 72 offline `ddof=1` within-seed source-task SD cells over 9 intervention/seed combinations, 2 evaluation splits and 4 primary metrics. Seed-to-seed variability is material; one favorable cell is not an admissible power input. | No prospective conservative seed-aware variance bound, precise Holm family size, power certificate or confirmatory effect |
| Development calculator-level paired-effect ICC | `V5_S1_DEVELOPMENT_CALCULATOR_EFFECT_ICC_INVENTORY_2026-10-10.md` and `artifacts/v5/development/s1-calculator-icc-inventory-2026-10-10/development-calculator-icc.json` on base draft #323 | 72 original-source descriptive one-way calculator ICC cells: median 0.023117, range −0.012645 to 0.238078; 12 negative finite-sample estimates retained. Each split has 64 fixed selected calculators × 60 source cases (3,840), not 4,096 confirmatory cases. | No qualified population ICC, calculator-generalized inference, crossed source/calculator/seed variance, 90% power certificate or confirmatory authorization |

S1 source-task evaluation counts: DEV 3,840 and CAL 3,840 (7,680 source-task clusters across both splits). The canonical/transformed variants are **not** independent samples. The effect and nuisance estimates in the inventory are paired to the unchanged baseline for descriptive development only, with metric orientation preserved in raw units; no significance is claimed.

## Provenance and reproducibility binding

The following are SHA-256 checks on files **retained in the draft evidence branches**, not on a publication release:

| Immutable source | SHA-256 |
| --- | --- |
| R1 original Kaggle ZIP | `dfb35b0216369bbb87bcec75c5715df974bb9f736c0db0af98148cea91d99dac` |
| R2 original Kaggle ZIP | `73f24c06f2d54e34cc20f2137f06b0728f02cccfc0d96c346f619d73184e4216` |
| Paired repeatability `repeatability95` | `f6ace697d61de05c470c1260dafc7b54f13524b0dd2960e45c268c46bb7e64be` |
| Development-only research-scale margins | `361ad34e0c2deb0ca7646cfb9dd9346bb63471296a003e9ef12a858743f6917f` |
| Descriptive 72-cell source-task SD inventory | `b1edf781b61d3f5ce227c08908ca43ad9864c0b398a7318c33895951af37bacd` |
| Development-only 72-cell calculator-effect ICC inventory | `37d64c0f6ac14d04cc6420a020e7bb7997fb333e50729f33798b2d403d292370` |
| Cross-seed development synthesis | `76b7f7503a743991fd81f4e1758d5710cc646a0a665c1e3e2128d1e533ea2e82` |
| Pre-output frozen domain-floor manifest | `8c284a98f504c8529a4da5d9bb1e265465af66b10d0c3b0414505dcebc9c7ca7` |

Both original Kaggle exports have independently passing model-free source/row/analysis verification receipts. Their external execution status and zero incremental user compute spend are recorded separately. Equal response rows do not by themselves prove independently executed kernel provenance; the separate kernel/run receipts provide that evidence. No model weights were loaded during offline verification and addendum preparation.

## Claim and statistical gate reconciliation

- **V5-C01** remains `PARTIAL_THEORY_ONLY`; theory examples are not a demonstrated clinically consequential empirical contrast.
- **V5-C02–V5-C07** remain `UNPROVEN`; nothing here is a tested Holm-adjusted non-target effect, valid noninferiority claim, compensatory deployment reversal, replicated interaction, cross-backbone generalization or clinically qualified deterministic routing result.
- **V5-C08** remains `CONDITIONALLY_SUPPORTED`, dependent on adequate current prior-art review and eventual valid result/positioning.
- **Final 90% power at 4,096 planned source cases remains unqualified.** A prospectively justified complete primary hard-gate non-target Holm family and family size must be established. The inferential target for 64 selected calculators (fixed-collection effects versus broader calculator generalization), shared baseline, within-calculator source-case dependence, coupling, missingness, and stochastic uncertainty across just three training seeds must be independently specified and reviewed. Neither the 72 descriptive source-task SD cells nor the 72 development-only calculator ICC cells may be cherry-picked or promoted to conservative prospective nuisance bounds, final power or clinical evidence.
- Any final confirmatory/reserve identity, intervention allocation, independent-family replication, manuscript claim promotion, public preprint or release requires its own legitimately recorded authority and all preconditions. Draft evidence PRs cannot be treated as a publication certificate.
- Independent scientific/methodological review, original-source attribution and a valid cryptographic signing/governance route remain open. DCO sign-off does not substitute for a verified Git signature.


## 2026-10-10 source-bound development calculator-dependence follow-up (not a statistical sign-off)

Draft base PR [#323](https://github.com/TheHalfMoon/commandMed/pull/323) introduced a separate **original-source, development-only** calculator-level paired-effect ICC inventory after this crosswalk was first authored. Its checked-in analyzer `scripts/v5_s1_development_calculator_icc_inventory.py` pins the original unchanged baseline, independent R1 cross-check and nine existing B1/C1/C2 matrices for training seeds **11, 29, 47** (11 source input SHA-256 identities). GitHub Actions [run 38068989562](https://github.com/TheHalfMoon/commandMed/actions/runs/38068989562) succeeded at PR #323 head `4a3a86588fccd293792dd3c3ab9a648153c1eefc`. This is source-integrity and software evidence, **not** independent statistical or clinical validation.

For each of nine intervention/seed combinations, two evaluation splits and four frozen metrics, the analyzer calculates a **raw, unclipped, descriptive one-way ANOVA method-of-moments ICC** on candidate-minus-unchanged-baseline *paired source-case effects* grouped by selected calculator. Each split has 64 fixed selected calculators × 60 distinct development source cases, with paired prompt variants already collapsed at source-case level. Across **72/72** cells the observed ICC median was **0.023117**, minimum **−0.012645**, maximum **0.238078**; 12 negative finite-sample estimates remain negative (not negative population variance claims). The highest observed development cell was C2 seed 47 / S1_DEV_EVAL / semantic JS. The analyzer reconstructed the original 72 saved whole-split source-task SD cells with maximum floating-point absolute discrepancy **3.552713678800501e-15**, under a separately pinned source SD SHA-256.

This measured *development* dependence does **not** establish an independent sample of calculators, a confirmatory population ICC, a causal dependence structure, or a validated design effect. Its illustrative balanced-cluster arithmetic with **60** cases per calculator must **not** be substituted for prospective **64 × 64 = 4,096** source cases, treated as effective sample size for final power, or used to ignore three-run stochastic training-seed uncertainty. The reviewer must first decide whether the estimand is conditional on the 64 chosen calculators or generalizes beyond them, then justify dependence and missingness handling across calculators, source cases, shared baseline, training seeds and coupled non-target hypotheses.

The complete primary non-target Holm family, native-unit effect margins, per-primary-effect **90%** power at **FWER alpha 0.05**, and feasibility at planned **4,096** prospective cases remain **NOT_REVIEWED / NOT_APPROVED** under [issue #326](https://github.com/TheHalfMoon/commandMed/issues/326). If the frozen power-failure rule is triggered, only a scientifically and founder-authorized underpowered stop or prospective redesign may proceed. No new case identities, GPU/model runs, manuscript claim promotion, merges of gated drafts, or public clinical/research claims are authorized by this addendum. The original **307** frozen scientific evidence bindings remain outside this change.

## Suggested future manuscript placement (not an authorized manuscript edit)

A future **Development and protocol-qualification observations** subsection can present the table above as developmental, with a visually separate **Confirmatory results** subsection initially stating `NOT_EXECUTED`. The paper's main conclusions must remain conditional on the unexecuted study. The negative B1/C1/C2 results and near-chance rule-conformance results must be retained, not reframed as V5 scientific success.

This addendum is evidence-oriented and deliberately leaves every prospectively frozen manuscript and claim-ledger byte unchanged.
