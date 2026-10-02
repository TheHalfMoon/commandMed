# Problem selection

Medical forced-choice correctness, probability quality and ability to generate useful language are different observables. PubMedQA asks biomedical research questions; MedQA and MedMCQA derive from examinations. None directly establishes patient benefit [@arxiv190906146; @arxiv200913081; @arxiv220314371]. A benchmark improvement therefore cannot answer whether a decision-oriented adaptation damages the language capabilities of the same model.

The scientific problem is to separate the effect of the output mechanism from the effect of decision supervision and maintenance losses. Existing typed-head and LM-head studies are strong baselines. They motivate a controlled clinical-domain experiment but do not prove that such an experiment would be novel or valuable [@arxiv260925845; @arxiv260936116; @arxiv260936965].

We prefer a focused factorial study to all-in-one HCF because its failure can be interpreted: the head may be unnecessary, supervision may explain an apparent gain, or improvement may cost retained competence. The desired contribution is a replicated finding that changes architecture choice. A broad consolidation demo would leave too many explanations unidentified. The selected backbone is an experimental factor and cost constraint, not the scientific motivation.
