# Candidate paper theses

Eight candidates were compared before choosing a model. Scores are provisional ordinal judgments. A literature gap is not proven by a bounded search. T5 leads under equal, science-focused and resource-focused weighting; T7 is a complementary question, not automatically a separate paper. T2 has better immediate feasibility but fails the generic novelty gate.

| Thesis | novelty | importance | falsifiability | reproducibility | baselines | zero_cost_feasibility | meaningful_negative_result | publication_strength | concurrent_differentiation | phd_portfolio_value | artifact_value | Mean | Science | Resource |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T5 Medical Readouts under Matched Supervision: Calibration, Selective Risk, and Capability Interference | 3 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 3 | 5 | 5 | 4.455 | 4.2 | 4.75 |
| T7 Evidence-Conditioned Calibration Transport under Medical Source Failures | 2 | 5 | 5 | 4 | 5 | 3 | 5 | 3 | 2 | 4 | 4 | 3.818 | 3.8 | 4.0 |
| T8 Calibration-preserving merging under noncompensable medical constraints | 3 | 5 | 4 | 2 | 5 | 2 | 5 | 3 | 3 | 4 | 4 | 3.636 | 4.0 | 3.25 |
| T2 Native calibrated medical decision head | 1 | 4 | 5 | 4 | 5 | 4 | 4 | 2 | 1 | 3 | 4 | 3.364 | 3.0 | 4.25 |
| T4 Medical capability per byte and joule | 2 | 4 | 4 | 3 | 4 | 2 | 4 | 3 | 2 | 4 | 5 | 3.364 | 3.2 | 3.5 |
| T6 Arabic/English medical selective calibration | 2 | 5 | 4 | 2 | 4 | 2 | 4 | 3 | 2 | 4 | 4 | 3.273 | 3.4 | 3.0 |
| T3 Semantic encoder replacement for understanding and image generation | 2 | 4 | 4 | 2 | 4 | 1 | 4 | 3 | 2 | 4 | 4 | 3.091 | 3.2 | 2.75 |
| T1 Single-checkpoint heterogeneous capability fusion | 1 | 4 | 3 | 2 | 3 | 1 | 3 | 2 | 1 | 3 | 3 | 2.364 | 2.4 | 2.25 |


## T5 — Medical Readouts under Matched Supervision: Calibration, Selective Risk, and Capability Interference

Separates readout, decision supervision and maintenance objective with same-backbone probes and cross-family replication. Visual Jev, Dyad, Uni-Med and Med-MoE-LoRA may reduce the contribution to replication; no new paradigm is claimed.

Disposition: PRIMARY_CONDITIONAL. Threats: [@arxiv260925845], [@arxiv260936116], [@arxiv240917508], [@arxiv260107935].

## T7 — Evidence-Conditioned Calibration Transport under Medical Source Failures

Study transfer of a fixed calibration map across clinically valid source failures. CLEAR, CliniCARE, MemSafe, Visual Jev, SURE-RAG and RULE cover most primitives; a generic evidence-aware head or benchmark is rejected as novelty.

Disposition: SECONDARY_CONDITIONAL. Threats: [@arxiv260916301], [@arxiv260807796], [@arxiv260932269], [@arxiv260925845], [@arxiv260503534], [@arxiv240705131].

## T8 — Calibration-preserving merging under noncompensable medical constraints

OptMerge, Expert Merging, uncertainty-aware merging and safety degradation already threaten merging novelty. Requires compatible lawfully usable experts and clinically defensible hard gates; zero-cost feasibility is low.

Disposition: DEFERRED. Threats: [@arxiv250519892], [@arxiv250925712], [@arxiv240614563].

## T2 — Native calibrated medical decision head

Dyad, Chinese-Jev and Visual Jev directly threaten native-head novelty. Visual Jev reports no consistent typed-head advantage under a matched control. A head alone is not a contribution.

Disposition: REJECT_GENERIC_NOVELTY. Threats: [@arxiv260936116], [@arxiv260936965], [@arxiv260925845].

## T4 — Medical capability per byte and joule

Parameter count is an inadequate systems endpoint. Hardware energy measurement and medical retention margins are not available. A static byte estimate cannot establish a Pareto frontier.

Disposition: DEFERRED. Threats: [@arxiv260925845].

## T6 — Arabic/English medical selective calibration

BiMediX, MedAraBench, MedArabiQ, Chinese-Jev and cross-lingual consistency studies make multilingual extension incremental unless semantic equivalence and calibrated transport are rigorously established. Qualified bilingual annotation is a boundary.

Disposition: DEFERRED. Threats: [@arxiv240213253], [@arxiv250503427], [@arxiv260201714], [@arxiv260907687].

## T3 — Semantic encoder replacement for understanding and image generation

PixelUMM and unified models threaten encoder-removal novelty; Qwen-Image conditioning is more than width matching. A stronger resource result needs real hardware and licensed image evidence.

Disposition: OPTIONAL_FOLLOW_UP. Threats: [@arxiv260938597], [@arxiv250514683], [@arxiv241013848].

## T1 — Single-checkpoint heterogeneous capability fusion

MedUAG, UniMedVL, SynerMedGen, BAGEL, PixelUMM already unify capabilities; no evidence that consolidation causes a clinical gain. Large heterogeneous rights/runtime burden.

Disposition: DEFERRED. Threats: [@arxiv260818937], [@arxiv251015710], [@arxiv260508724], [@arxiv250514683], [@arxiv260938597].
