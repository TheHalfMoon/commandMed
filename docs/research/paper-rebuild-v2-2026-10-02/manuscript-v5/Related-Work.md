# 2. Related Work

## 2.1 Multidimensional medical evaluation

MedHELM broadens medical LLM evaluation across clinically grounded task categories and many evaluation suites, while recent surveys emphasize that trustworthiness is multidimensional rather than reducible to accuracy [@bedi2026medhelm; @wang2025trustworthy]. These works make a generic “multidimensional benchmark” contribution insufficiently novel. Our target is instead the *effect of reliability interventions across dimensions* under controlled paired comparisons.

## 2.2 Calibration, coherence and language variation

Medical studies show poor or unstable confidence calibration, and general LLM work demonstrates that calibration alone does not guarantee robustness to semantically equivalent wording or sensitivity to meaning changes [@savage2025uncertainty; @xia2026calibration]. Matta et al. further distinguish structural coherence, faithfulness and usefulness, showing that improvements in calibration need not restore coherent probabilistic beliefs [@matta2026rethinking]. These findings motivate separate axes rather than a single uncertainty score.

## 2.3 Logical consistency and selection bias

Preference and multiple-choice decisions can violate transitivity, negation invariance, permutation invariance and label-order stability [@liu2024logic; @pezeshkpour2024order; @zheng2024pride]. Methods such as PriDe, permutation-aware training, Set-LLM and related architectures explicitly target these defects [@zheng2026pagrpo; @egressy2025setllm]. V5 treats such methods as intervention families and asks whether their gains transfer to calibration, evidence responsiveness or action validity.

## 2.4 Abstention and decision-level confidence

MedQAbstain documents systematic overcommitment under medical uncertainty, while decision-theoretic work formalizes answer-versus-abstain utility and risk-sensitive confidence evaluation [@cocchieri2026medqabstain; @presacan2026silence; @wu2026bas]. Selective behavior is therefore not novel by itself. The V5 question is whether calibration, abstention and other reliability interventions interact or remain modular when evaluated on the same source cases.

## 2.5 Fine-grained medical alignment and deterministic tools

ProMedical explicitly separates safety criteria from general proficiency during medical alignment [@geng2026promedical]. AgentMD and recent clinical-risk-score studies show that deterministic calculator pipelines can outperform unconstrained model arithmetic and improve transparency [@jin2025agentmd; @kara2025riskscores; @roeschl2026pipeline]. These works constrain our claims: deterministic tools are not a novel contribution, but they provide unusually strong action oracles for studying cross-property effects.
