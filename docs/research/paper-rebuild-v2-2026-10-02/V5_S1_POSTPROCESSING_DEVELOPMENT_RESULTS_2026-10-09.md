# V5 S1 post-processing development results — 2026-10-09

Status: `COMPLETE_DEVELOPMENT_POSTPROCESSING; NOT_CONFIRMATORY`

Run source: `e515e088ed641b6accdb85bf031a593e751e2394`, tree `d070cd1ea82382c4441e747fba7b0370b10c83d6`.

Canonical output: `artifacts/v5/development/s1-postprocessing-results-2026-10-09/development-postprocessing.json`.

Output SHA-256: `51a4f0709620b48995d887fb2956c9c2fe0836ad37b286a2cddfd65e87979893`.

The analysis reads only already-durable development/calibration decision matrices. It performs no model call, training, confirmatory/reserve access, threshold/bin optimization outside the prospectively frozen rules, or claim promotion.

## Frozen tuning results

- A1 temperature scaling selected `T=5.959579947582588` (`log(T)=1.785`) on baseline canonical `S1_CAL_TUNE`; the selected point is not a search-grid boundary.
- A2 display-slot prior is `[0.6607746105018988, 0.3392253894981012]`, fit from all 512 baseline `S1_CAL_TUNE` canonical/transformed displayed-slot rows.
- A2-then-A1 selected the upper temperature-grid boundary `T=403.4287934927351` (`log(T)=6`). This boundary result is preserved as a limitation and the grid is not widened post hoc.
- D1's 5% tuning-risk rule found a nominally feasible threshold `0.8933094060543488` using only 2/256 canonical tuning items: tuning coverage `0.0078125`, tuning risk `0`. The tiny tuning support is explicitly preserved.

## Baseline and post-processing summaries

Canonical development-evaluation results:

| Condition | Accuracy | NLL | Brier | 15-bin calibration gap | Mean semantic JS |
| --- | ---: | ---: | ---: | ---: | ---: |
| BASELINE_V1 | 0.48046875 | 0.7831774818054636 | 0.5799630568176445 | 0.18697185765680754 | 0.0012071127534053162 |
| A1_TS_V1 | 0.48046875 | 0.6979839994373072 | 0.504823580931385 | 0.03289312783155793 | 0.00004075276439938862 |
| A2_SELBIAS_V1 | 0.49661458333333336 | 0.710596755211726 | 0.5164329182649608 | 0.0680904716847975 | 0.0013638881876477415 |
| A1_THEN_A2 | 0.49661458333333336 | 0.6941052320122627 | 0.5009579584826631 | 0.007659849338178296 | 0.00004093986048680588 |
| A2_THEN_A1 | 0.49661458333333336 | 0.6931553356468407 | 0.5000081550904103 | 0.00006717320643589986 | 0.000000008955578187315748 |

Canonical calibration-evaluation results:

| Condition | Accuracy | NLL | Brier | 15-bin calibration gap | Mean semantic JS |
| --- | ---: | ---: | ---: | ---: | ---: |
| BASELINE_V1 | 0.49453125 | 0.7744336625615333 | 0.5720342460601971 | 0.17369189905638835 | 0.0011929065899829062 |
| A1_TS_V1 | 0.49453125 | 0.6965258543589682 | 0.5033695692272169 | 0.023652371043765406 | 0.00004003734708171439 |
| A2_SELBIAS_V1 | 0.49453125 | 0.7096492118433418 | 0.5156392129836458 | 0.07168387165829165 | 0.0013426246301611977 |
| A1_THEN_A2 | 0.49453125 | 0.6939828963946486 | 0.5008361717465654 | 0.006262644530849953 | 0.000040214909133330485 |
| A2_THEN_A1 | 0.49453125 | 0.6931536485221985 | 0.5000064679673031 | 0.00006435919452019156 | 0.000000008796197939398189 |

The post-processing conditions can materially improve proper-score/calibration diagnostics while accuracy remains approximately one half. In particular, A2-then-A1 approaches the uniform binary predictor's NLL/Brier while leaving accuracy near chance. This is development evidence for the protocol's separation between calibration-like diagnostics and useful correspondence; it is not evidence of clinical reliability.

No improve/harm/equivalent label is assigned because native-unit meaningful margins and the frozen confidence procedure are not yet available.

## Selective-control result

The D1 tuning rule does not transport.

- DEV canonical: coverage `0.006510416666666667` (25/3840), accepted-case risk `0.48`, tie-block AURC `0.5256857913947288`.
- DEV transformed: coverage `0.009635416666666667` (37/3840), accepted-case risk `0.5135135135135135`, tie-block AURC `0.5287875715842704`.
- CAL canonical: coverage `0.00546875` (21/3840), accepted-case risk `0.47619047619047616`, tie-block AURC `0.5121829374221482`.
- CAL transformed: coverage `0.008854166666666666` (34/3840), accepted-case risk `0.35294117647058826`, tie-block AURC `0.5133934060318281`.

A zero-error tuning subset of two accepted items therefore does not support a selective-risk claim. Evaluation risk is high and coverage is negligible. Risk and coverage are reported together as required; zero or near-zero coverage is not treated as useful assurance.

## C1 followed by A1

Fresh A1 fits on the three durable C1 seeds selected:

- seed 11: `T=5.900281136319018`;
- seed 29: `T=403.4287934927351`, the upper grid boundary;
- seed 47: `T=4.199645008787926`.

DEV canonical NLL after C1-then-A1 is respectively `0.6960583653101129`, `0.6931460271239722`, and `0.6986609403079362`; corresponding accuracies are `0.4791666666666667`, `0.49973958333333335`, and `0.48072916666666665`.

These remain development-only compositions. The boundary result for seed 29 is preserved rather than repaired by widening the grid after inspection.

## Scientific boundary

These results do not establish meaningful-effect classification, equivalence, noninferiority, clinical validity, broad capability preservation, confirmatory interaction claims, or replication. Unchanged-base repeatability R1/R2, native-unit domain floors, final margins and final power remain separate gates. PR #320 remains OPEN / DRAFT / UNMERGED.
