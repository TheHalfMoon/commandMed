# V5 novelty threats — cross-property reliability interference

Status: ADVERSARIAL REVIEW; no novelty clearance.

## Existing trade-off evidence

Xia et al., *Calibration Is Not Enough* (arXiv `2601.08064`), already show that confidence methods trade off robustness, stability and sensitivity and that conventional calibration does not determine these properties.

Matta, Naphade and Zou, *Rethinking Uncertainty Evaluation in Large Language Models* (arXiv `2607.19367`), already show that calibration can remain disconnected from structural coherence and probabilistic validity.

Jawad and Caragea, *CaliDist* (ICML 2026), explicitly use behavioral robustness to improve calibration. V5 therefore cannot claim that robustness and calibration have never been studied jointly.

Liu et al., *The trade-off between robustness and reliability in Chinese legal large language models* (Artificial Intelligence and Law, 2026), report an inverted-U effect where excessive robustness-oriented data injection weakens legally salient sensitivity. This directly threatens any generic “robustness can hurt sensitivity” claim.
Zhao et al., *On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs* (ICML 2026), show accuracy–faithfulness and robustness–consistency trade-offs under RL/adversarial interventions. V5 cannot claim discovery that post-training may improve one capability while degrading another.

CRS-Bench (arXiv `2608.22059`) evaluates medical image encoders across discrimination, calibration, label efficiency and robustness using Pareto-aware reliability profiles. V5 cannot claim first multi-axis reliability profiling or Pareto analysis in medical AI.

Xu et al., *Calibration Data Trade-offs Across Capability Dimensions* (arXiv `2606.03328`), show opposite-sign retention effects across capability dimensions under pruning calibration-source choices. V5 cannot claim first intervention-by-capability trade-off matrix in LLMs generally.

## Existing medical robustness/evidence studies

Clinical robustness studies already probe missing, misleading, contradictory or adversarial information. A 2026 Journal of Medical Systems scoping review found that much medical LLM robustness testing lacks clinical plausibility, which motivates but does not establish V5 novelty.

MetaMedQA, CLEAR, CliniCARE, MedConf, SURE-RAG, MedDialBench and related studies already cover pieces of missing-information recognition, evidence sufficiency, contradiction handling, calibration and robustness.

## Surviving candidate gap

The bounded search has not identified one medical foundation-model study that deliberately applies **multiple reliability-targeted interventions to the same base systems under matched budgets, estimates the full intervention-by-assurance cross-effect matrix, tests selected intervention interactions, combines this with explicit non-implication/non-compensation analysis, and uses mechanically exact medical decision oracles plus independent-backbone replication**.

That exact combination is the candidate contribution. It remains killable by further literature or by null experiments.## 2026-10-02 adversarial refresh

MedHELM (Nature Medicine 2026, DOI `10.1038/s41591-025-04151-2`) makes broad multidimensional medical evaluation a mature baseline rather than a novelty claim. V5 must therefore distinguish intervention effects from benchmark breadth.

Wang et al. (EMNLP 2025, DOI `10.18653/v1/2025.emnlp-main.1398`) explicitly organize trustworthy medical QA across multiple trust dimensions and identify integrated multidimensional evaluation as an open problem. This supports importance but weakens any generic “trustworthiness is multidimensional” claim.

MedQAbstain (ACL 2026, DOI `10.18653/v1/2026.acl-long.1365`) and Presacan et al. (npj Digital Medicine 2026, DOI `10.1038/s41746-026-02882-1`) make medical abstention and answer-versus-refuse trade-offs established prior art. Selective prediction cannot carry V5 novelty alone.

ProMedical (ACL 2026, DOI `10.18653/v1/2026.acl-long.1714`) explicitly disentangles safety constraints from general proficiency during medical alignment. V5 cannot claim first multi-criteria medical alignment or first separation of safety and capability.

AgentMD (Nature Communications 2025, DOI `10.1038/s41467-025-64430-x`), Kara and Gunel (Journal of Medical Systems 2025, DOI `10.1007/s10916-025-02261-5`), and Roeschl et al. (European Heart Journal - Digital Health 2026, DOI `10.1093/ehjdh/ztag124`) establish deterministic clinical-calculator execution as strong prior art. V5 uses deterministic rules as an oracle substrate, not as a novelty claim.

Current novelty position: **conditional survival**. The candidate gap remains the matched, multi-intervention, cross-property *causal effect matrix* plus preregistered interaction tests and noncompensatory certification on the same medical source cases. A later paper with this same study design would kill or sharply narrow V5.
