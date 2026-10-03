# Literature refresh — 2026-10-02

Purpose: adversarially test Paper V3 before any experiment.

## Medical probability and evaluation evidence

Gu et al., *Probabilistic medical predictions of large language models*, npj Digital Medicine 7:367 (2024), DOI `10.1038/s41746-024-01366-4`, compared explicit verbalized probabilities with implicit label-token probabilities across six open-source LLMs and five medical datasets. Their result directly motivates treating probability extraction mechanism as an empirical factor rather than assuming verbalized confidence is reliable.

Savage et al., *Large language model uncertainty proxies: discrimination and calibration for medical diagnosis and treatment*, JAMIA 32(1):139–149 (2025), DOI `10.1093/jamia/ocae254`, compared confidence elicitation, token-level probability and sample-consistency proxies. It reinforces the distinction between discrimination and calibration.

Griot et al., *Large Language Models lack essential metacognition for reliable medical reasoning*, Nature Communications 16:642 (2025), DOI `10.1038/s41467-024-55628-6`, evaluates confidence and missing-answer recognition. This threatens any claim that missing-answer awareness itself is novel.

Bedi et al., *Testing and Evaluation of Health Care Applications of Large Language Models: A Systematic Review*, JAMA 333(4):319–328 (2025), DOI `10.1001/jama.2024.21700`, reviewed 519 studies and found calibration/uncertainty rarely evaluated relative to accuracy. This supports the evaluation motivation, not CRDI novelty.
## Selection bias and permutation controls

Pezeshkpour and Hruschka, *Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions*, Findings of NAACL 2024, DOI `10.18653/v1/2024.findings-naacl.130`, establishes substantial order sensitivity and permutation-based calibration effects.

Zheng et al., *Large Language Models Are Not Robust Multiple Choice Selectors*, ICLR 2024, identifies option-ID/token selection bias and proposes PriDe. CommandMed cannot claim discovery of selection bias.

Egressy and Stühmer, *Set-LLM: A Permutation-Invariant LLM*, arXiv:2505.15433 (2025), introduces an architecture with permutation-invariance guarantees for mixed set-text input.

Jiao, Huang and Zhang, *Embracing Positional Bias in Multiple-Choice Question Answering via Permutation Equivariant Neural Networks*, AAAI 2026, DOI `10.1609/aaai.v40i37.40401`, provides an explicit permutation-equivariant architecture control.

J. Zheng et al., *Mitigating Selection Bias in Large Language Models via Permutation-Aware GRPO*, ACL 2026, DOI `10.18653/v1/2026.acl-long.1621`, trains for cross-permutation consistency. This is a mandatory training baseline/threat.

## Metamorphic and semantic-invariance threats

de Curtò and de Zarzà, *Metamorphic Testing for Semantic Invariance in Large Language Models*, IEEE Access 13 (2025), DOI `10.1109/ACCESS.2025.3646270`, already frames semantic-preserving transformations as a reliability test.

Zhou et al., *LGMT: Logic-Grounded Metamorphic Testing for evaluating the reasoning reliability of LLMs*, Knowledge-Based Systems 348:116324 (2026), DOI `10.1016/j.knosys.2026.116324`, grounds metamorphic relations in formal logic.

Therefore “semantic invariance testing for LLMs” is not a sufficient novelty claim.
## Evidence intervention neighbors

RULE is peer-reviewed at EMNLP 2024: Peng Xia et al., *RULE: Reliable Multimodal RAG for Factuality in Medical Vision Language Models*, DOI `10.18653/v1/2024.emnlp-main.62`. It calibrates retrieval-context selection and studies over-reliance on retrieved evidence. The earlier V2 record that left this identity pending must be corrected before publication.

Javadi et al., *Contradictions in Context: Challenges for Retrieval-Augmented Generation in Healthcare*, arXiv:2511.06668v2 (2026), studies outdated/contradictory medical retrieval. It narrows the novelty of C4 evidence contradiction.

The existing V2 corpus also includes CLEAR, CliniCARE, MemSafe, SURE-RAG, Sufficient Context and Visual Jev. V3 cannot claim that evidence sufficiency, contradictory evidence, selective abstention, or typed decisions are individually new.

## Current bounded novelty

The remaining candidate novelty is the **joint probability contract**: inverse-mapped distribution equivariance under meaning-preserving interface transformations, calibrated responsiveness under meaning-changing evidence interventions, and retained language capability under one matched evaluation design. This remains a search hypothesis, not a firstness claim.

## Research-tool audit

Consensus was available and used only for discovery/cross-checking; important claims were traced to original publisher/proceedings records. Scite MCP was tested but blocked by a paid-plan requirement, so it is `SCITE_DEFERRED_ZERO_COST_POLICY` and contributes no qualification evidence. No paid API was used. Web/arXiv/ACL/AAAI/publisher primary sources remain the zero-cost verification path.

A final targeted literature refresh is required immediately before scientific freeze and again before submission.