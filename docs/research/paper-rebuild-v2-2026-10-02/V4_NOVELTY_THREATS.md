# V4 novelty threats

Status: ADVERSARIAL REVIEW; no firstness claim.

## Threat 1 — multidimensional medical evaluation already exists

Wang et al., *A novel evaluation benchmark for medical LLMs illuminating safety and effectiveness in clinical domains*, npj Digital Medicine 9:91 (2026), DOI `10.1038/s41746-025-02277-8`, defines a clinically expert-built framework with 30 criteria, a safety gate, and an effectiveness gate. V4 cannot claim that medical LLMs were previously evaluated only with one metric.

MedCheck, *Beyond the Leaderboard: Rethinking Medical Benchmarks for Large Language Models*, ACL 2026, audits dozens of medical benchmarks with 46 lifecycle criteria. V4 cannot claim that benchmark governance or multidimensional trustworthiness checklists are new.

The 2026 pharmacotherapy-simulation study in npj Digital Medicine (`10.1038/s41746-026-02626-1`) explicitly uses non-compensatory thresholds for clinical accuracy/safety and reasoning fidelity. V4 therefore cannot claim invention of non-compensatory medical gating.

## Threat 2 — calibration is already known to be insufficient

Xia et al., arXiv `2601.08064`, evaluate robustness, semantic stability, and sensitivity in addition to calibration/discrimination. Matta et al., arXiv `2607.19367`, formalize structural coherence, faithfulness, and usefulness and show calibration can be orthogonal to probabilistic validity. V4 must go beyond the slogan “calibration is not enough.”
## Threat 3 — semantic stability and evidence response already have direct precedents

Dixon, *Calibrating Semantic Uncertainty from Observable Language-Model Probabilities*, arXiv `2607.17447`, explicitly targets application-state probabilities that remain stable under information-equivalent rewording and respond to altered evidence.

Weng, Feng and Xie, *Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges*, arXiv `2605.06161`, separates certified-equivalent rewrites from meaningful policy-threshold changes and evaluates invariance versus responsiveness.

Mohri, Schneider and Wu, *Coherence Mechanisms for Provable Self-Improvement*, arXiv `2511.08440`, provides a formal framework for coherence under task-preserving transformations with projection mechanisms and theoretical guarantees.

Therefore V4 cannot claim semantic invariance or task-preserving coherence as new.

## Threat 4 — decision utility and selective control already have principled frameworks

Wu et al., *BAS: A Decision-Theoretic Approach to Evaluating Large Language Model Confidence*, arXiv `2604.03216`, links confidence to abstention-aware decision utility and shows that similar conventional calibration behavior need not imply similar decision usefulness.

Jin, Moon and Zitnik, *Act or Defer: Error-Controlled Decision Policies for Medical Foundation Models*, medRxiv 2026, DOI `10.64898/2026.02.23.26346927`, provides explicit false-discovery control for acted-on patients and conditional coverage for deferred cases. V4 cannot present selective error control as a new assurance axis or method.
## Threat 5 — deterministic clinical calculators are already a mature research direction

Jin et al., *AgentMD: Empowering language agents for risk prediction with large-scale clinical tool learning*, Nature Communications 16:9377 (2025), DOI `10.1038/s41467-025-64430-x`, curates and applies 2,164 executable clinical calculators. The accompanying `ncbi-nlp/Clinical-Tool-Learning` repository uses a U.S. Government public-domain notice for its software/database. V4 cannot claim novelty from using clinical calculators as deterministic oracles.

Other 2025–2026 studies explicitly separate LLM extraction from deterministic cardiovascular risk-score computation and evaluate LLM calculation of CHA2DS2-VASc, HAS-BLED, Wells and other scores. V4 must use calculator logic as an oracle substrate, not as its scientific contribution.

## Threat 6 — counterfactual/behavioral medical testing already exists

DeVisE and MEDEQUALQA use controlled counterfactual changes to probe medical-model behavior. MedGuideX derives factual and counterfactual supervision from executable clinical guidelines. Medical dialogue and adversarial-patient benchmarks already study graded robustness and interactions.

V4 therefore cannot claim counterfactual medical testing itself as new.

## Surviving candidate contribution

The bounded search has not yet found one work combining: (a) explicit formal non-implication witnesses among decision-reliability obligations; (b) a theorem quantifying when compensatory weighted scoring permits total failure of a named assurance axis; (c) a non-compensatory assurance region; (d) mechanically exact, rule-grounded medical metamorphic oracles; and (e) an empirical intervention study showing which model/post-training/calibration methods move which assurance coordinates and which trade-offs are hidden by aggregate scores.

This is a **candidate gap**, not proof of novelty. A final search must target this exact combination before freezing V4.