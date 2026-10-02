# V5 adversarial literature refresh — 2026-10-03

Status: bounded novelty-threat refresh; not a systematic-review completion claim.

## Search objective

Try to falsify the V5 gap by locating work that already combines multidimensional medical-LLM reliability evaluation with targeted interventions, cross-property effects, interaction analysis, noncompensatory safety decisions, deterministic medical rule oracles, and independent-family replication.

Search families included medical LLM calibration, selective prediction, abstention, robustness, multidimensional trustworthiness, intervention trade-offs, construct-valid evaluation, and reliability interactions. Important claims below were traced to primary publisher/proceedings/arXiv records.

Tool state on 2026-10-03:
- public web/publisher/proceedings sources: used;
- Consensus: monthly search allowance exhausted, so no new Consensus evidence was used;
- Scite MCP: requires a paid plan or active trial and remains deferred under the zero-paid-API rule.

## Direct novelty threats

**Wang et al., Trustworthy Medical Question Answering: An Evaluation-Centric Survey.** EMNLP 2025, DOI `10.18653/v1/2025.emnlp-main.1398`. The survey organizes medical QA trustworthiness across factuality, robustness, fairness, safety, explainability, and calibration, and explicitly identifies integrated multidimensional evaluation as an open challenge. This kills any generic claim that trustworthiness is newly recognized as multidimensional.

**Bedi et al., Holistic evaluation of large language models for medical tasks with MedHELM.** Nature Medicine 32, 943–951 (2026), DOI `10.1038/s41591-025-04151-2`. MedHELM provides a clinician-validated taxonomy and 37 evaluations across 121 medical tasks. This kills any generic claim that CommandMed introduces holistic medical-LLM evaluation.

**Wang et al., A novel evaluation benchmark for medical LLMs illuminating safety and effectiveness in clinical domains.** npj Digital Medicine 9, 91 (2026), DOI `10.1038/s41746-025-02277-8`. CSEDB uses 30 expert-consensus metrics and risk-weighted safety/effectiveness scoring. This is a direct comparator for the V5 claim that compensatory weighted aggregation can hide hard-gate failure.
**Agrawal et al., The evaluation illusion of large language models in medicine.** npj Digital Medicine 8, 600 (2025), DOI `10.1038/s41746-025-01963-x`. This argues that benchmark choices of data, tasks, and metrics can produce misleading conclusions about translational impact. It strengthens the requirement that V5 define constructs and oracle semantics before optimization.

**Gu et al., Probabilistic medical predictions of large language models.** npj Digital Medicine 7, 367 (2024), DOI `10.1038/s41746-024-01366-4`. Across six open-source LLMs and five medical datasets, explicit verbalized probabilities underperformed implicit label-token probabilities. This prevents V5 from treating probability extraction as a neutral implementation detail.

**Boie et al., Calibration of Self-Reported Confidence and Accuracy of Large Language Models in Medical Question Answering.** Journal of Medical Systems 50, 103 (2026), DOI `10.1007/s10916-026-02430-0`. Specialty-stratified calibration and confidence-based abstention already exist, including the coverage/withholding trade-off. Calibration plus abstention alone is not a novel V5 contribution.

**Matta, Naphade and Zou, Rethinking Uncertainty Evaluation in Large Language Models.** arXiv `2607.19367` (2026). The paper formalizes structural coherence, faithfulness, and usefulness and reports that interventions reducing calibration error can leave structural violations unchanged. This is the closest general-domain threat to the V5 claim that improving one reliability property need not repair another.

**CURA: Calibrated Uncertainty with Retrieval and Agents for Trustworthy Multimodal Medical Decision Support.** MICCAI 2026. CURA combines calibrated posterior estimation, selective abstention, conformal sets, retrieval, and uncertainty-driven escalation. It narrows any V5 claim based only on combining calibration and selective control. Its reported result that more experts can degrade both accuracy and calibration is also a concrete example of intervention/system trade-offs.

**CALIN, Exposing and Mitigating Calibration Biases and Demographic Unfairness in MLLM Few-Shot In-Context Learning for Medical Image Classification.** MICCAI 2025, DOI `10.1007/978-3-032-04981-0_22`. CALIN jointly studies calibration, subgroup fairness, and utility. This blocks claims that calibration-versus-other-reliability trade-offs are entirely unexplored in medical AI.
## Current novelty boundary

The bounded refresh did **not** identify one study matching the full V5 design: the same medical source cases evaluated under multiple targeted reliability interventions, a paired cross-property causal-effect matrix, preregistered ordered interaction terms, noncompensatory hard-gate certification, exact deterministic medical rule oracles, and independent-family replication.

This is a conditional gap, not a firstness claim. The closest threats show that each ingredient separately has substantial prior art:
- multidimensional medical-LLM evaluation is established;
- calibration and abstention are established;
- calibration can be orthogonal to coherence;
- calibration/fairness and safety/helpfulness trade-offs are established;
- holistic benchmark design and construct-validity critiques are established.

Therefore the manuscript must not sell V5 as a new metric collection. The strongest defensible contribution remains the **controlled intervention-to-assurance effect matrix plus interaction analysis**, with the noncompensatory framework serving as the decision layer rather than the novelty headline.

## Required paper changes after this refresh

1. Cite MedHELM and CSEDB in the opening related-work paragraph and explicitly distinguish evaluation breadth from intervention causality.
2. Cite Matta et al. as the closest conceptual evidence that calibration improvement need not imply probabilistic validity.
3. Treat Gu et al. as the reason probability extraction method is a frozen factor.
4. Treat Boie et al., CURA, and CALIN as baselines/threats for calibration, abstention and cross-property utility/fairness claims.
5. Keep weighted aggregate scores only as a comparator; do not imply weighted clinical-risk evaluation is new.
6. Retain `NOVELTY_NOT_CLEARED_FOR_FIRST_CLAIMS` until a final pre-submission refresh and reviewer-style nearest-neighbor audit are complete.
