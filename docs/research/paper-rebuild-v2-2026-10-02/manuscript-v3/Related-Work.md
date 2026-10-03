# 2. Related Work

## 2.1 Medical LLM evaluation and probability quality

Medical LLM evaluation has historically emphasized question-answer accuracy, while calibration, uncertainty and deployment behavior remain comparatively under-measured [@bedi2025evaluation]. Gu et al. show that explicit verbal probabilities can underperform implicit label-token probabilities in medical prediction tasks [@gu2024probabilistic]. Savage et al. compare confidence elicitation, token-level probability and sample-consistency proxies and distinguish calibration from discrimination [@savage2025uncertainty]. Griot et al. demonstrate missing-answer and metacognitive failures in medical reasoning [@griot2025metacognition]. These works motivate probability-level evaluation but also mean that uncertainty awareness or missing-answer testing cannot be claimed as new in isolation.

## 2.2 Selective prediction and calibration

Calibration and selective prediction have deep prior foundations. Temperature scaling is a strong post-hoc calibration baseline [@arxiv170604599]. SelectiveNet and later risk-control work formalize prediction under rejection or coverage constraints [@arxiv190109192; @arxiv220802814]. Distribution shift can invalidate otherwise favorable calibration behavior [@arxiv190602530]. CommandMed therefore treats NLL/Brier, risk-coverage and shift behavior as separate endpoints and does not infer reliability from accuracy alone.
## 2.3 Selection bias and permutation-aware decision making

LLMs can change answers when multiple-choice options are reordered, and option-ID/token priors contribute to this selection bias [@pezeshkpour2024order; @zheng2024pride]. PriDe estimates and removes an option-ID prior at inference time. Set-LLM modifies attention and position representations to guarantee permutation invariance for set-text inputs [@egressy2025setllm]. EMBER uses a permutation-equivariant network to exploit and control positional effects [@jiao2026ember]. PA-GRPO explicitly trains cross-permutation consistency [@zheng2026pagrpo]. These are mandatory conceptual and experimental controls for our E1/E2 transformations.

## 2.4 Typed decisions and candidate semantics

Dyad represents candidate action semantics explicitly and scores them against a state representation [@arxiv260936116]. Chinese-Jev and related System-One models demonstrate efficient typed interfaces in specialized domains [@arxiv260936965]. Visual Jev provides an especially important warning: a matched typed-head control need not yield an independent accuracy advantage [@arxiv260925845]. Other work shows that a type-safe output can remain semantically wrong when option names are rebound to rubrics [@arxiv260926758]. Accordingly, CRDI is not justified by “typed output” alone; its claim must arise from the full contract behavior under matched controls.

## 2.5 Metamorphic testing and semantic invariance

Metamorphic testing evaluates relations among outputs under controlled transformations when exact output oracles are difficult. Recent LLM work applies semantic-preserving transformations directly [@decurto2025metamorphic], while LGMT grounds transformations in formal logical equivalence [@zhou2026lgmt]. Our framework uses this lineage but differs in its target observable: a machine-consumable probability distribution over candidate meanings, paired with a deliberately non-invariant family of evidence interventions. The distinction itself is prospective and must survive empirical and literature falsification.