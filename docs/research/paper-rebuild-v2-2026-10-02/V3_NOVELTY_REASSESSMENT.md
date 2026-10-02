# V3 novelty reassessment

Status: `PRIMARY_SELECTION_REOPENED`. V3 is preserved as a useful component study, not accepted as the primary paper.

The adversarial refresh after `PAPER_DECISION_GATE_V3.md` found direct prior work that materially narrows the proposed CommandMed Contract thesis.

## Direct novelty threats

1. **Dixon (2026), Calibrating Semantic Uncertainty from Observable Language-Model Probabilities, arXiv:2607.17447.** A prespecified semantic map targets probabilities over declared application states, explicitly tests stability under information-equivalent rewording, and tests response to altered evidence. This overlaps the core V3 distinction between semantic stability and evidence responsiveness.
2. **Xia et al. (2026), Calibration Is Not Enough, arXiv:2601.08064.** Separates robustness to prompt perturbations, stability across semantically equivalent answers, and sensitivity to semantically different answers, and reports that these are largely independent from standard confidence metrics.
3. **Weng et al. (2026), Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges, arXiv:2605.06161.** Explicitly separates certified-equivalent policy rewrites from meaningful threshold shifts and measures both invariance and responsiveness.
4. **Mohri, Schneider & Wu (2025/NeurIPS 2026), Coherence Mechanisms for Provable Self-Improvement, arXiv:2511.08440.** Formalizes coherence under task-preserving transformations and provides projection mechanisms and guarantees.
5. Existing selection-bias, Set-LLM, PA-GRPO, EMBER, metamorphic-testing and typed-decision work already covers major pieces of CRDI.
## Revised assessment

V3 novelty is downgraded from `4/5` to `2/5` as a standalone paper thesis. The exact score is a planning judgment, not a scientific measurement.

The following V3 components survive as valuable substudies:

- distribution-level option/label invariance;
- explicit distinction between meaning-preserving and meaning-changing interventions;
- matched-supervision typed-head controls;
- calibration-transport analysis;
- retained language-capability gates.

The following are no longer defensible as primary novelty claims:

- introducing a semantic decision contract;
- introducing semantic stability plus evidence sensitivity;
- introducing task-preserving coherence regularization;
- claiming generic permutation-aware decision reliability.

`CRDI_STATUS = COMPONENT_METHOD_CANDIDATE`, not primary contribution.

The paper search therefore continues from first principles rather than protecting V3.