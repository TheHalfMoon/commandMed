# Novelty boundary and related-work snapshot

Status: scope-limited dated search; no uniqueness, priority or exhaustive-search conclusion. Search responses, exact queries, retrieval times, versions, reported totals, returned counts and inclusion state are in `literature-search.json`. Only the returned pages were inspected. Large result totals and unsearched databases remain explicit coverage limits. OpenReview API returned 403; the forum returned an access challenge. Neither response verifies proceedings metadata.

Search tracks include medical unified understanding/generation, multimodal/heterogeneous merging, typed decision readouts, and autoregressive/diffusion unification. Exact-title and domain-filtered follow-ups reduce query noise. Exclude unrelated quantum, materials, electronic-structure and similarly named Janus/Bagel papers from method comparison; do not count those keyword hits as competing multimodal methods. Unsummarized entries remain pending screening.

| Prior work | Verified identity | Implication for CommandMed |
|---|---|---|
| MedUAG | 2608.18937v1 | Medical understanding/generation and benchmark construction are prior art |
| UniMedVL | 2510.15710v3 | Single-model medical understanding/generation and mutual reinforcement are prior art |
| SynerMedGen | 2605.08724v3 | Generation-aligned understanding and staged transfer are prior art |
| HealthGPT | 2502.09838v3 | Heterogeneous medical comprehension/generation adaptation is prior art |
| MedUnifier | 2503.01019v3 | Medical VLP combined with image generation is prior art |
| Show-o | 2408.12528v7 | A transformer combining autoregressive and discrete diffusion computation is prior art; distinguish discrete diffusion from this proposal's continuous visual flow path |
| Janus / Janus-Pro | 2410.13848v1 / 2501.17811v1 | Decoupled visual encoding with unified processing and scaling are prior art |
| Dyad | 2609.36116v1 | Native typed decisions attached to an LLM are prior art outside medicine; cannot claim the head concept is new |
| Chinese-Jev | 2609.36965v1 | Medical typed decisions and multilingual specialization are prior art; English-only evidence is insufficient for Arabic |
| OptMerge | 2505.19892v3 | Multimodal capability/modality merging and task-vector optimization are prior art; current repository also contains later spectral methods |
| Expert Merging / ++ | 2509.25712v1 | Behavior alignment and importance-guided layer chunking are prior art; compatible expert baseline, not a solution proven for unrelated DiT/VAE tensors |
| PivotMerge | 2604.22823v2 | Cross-modal projector alignment and interference-aware merging are prior art |
| Heterogeneous knowledge-transfer study | 2609.39369v1 | Specialist-to-general parameter projection is prior art; this does not justify blind averaging across unrelated modules |
| MergeHEIR | 2609.32422v1 | Hallucination/retention trade-offs after merging require explicit regression evaluation |
| Typed-decision evidence audit | 2609.32160v1 | Typed output itself is not demonstrated to confer an accuracy advantage |
| Option-name binding / rejection studies | 2609.26758v2 / 2609.39496v1 | Include semantic label permutation, missing-valid-option and deterministic arithmetic controls |
| Laya independent reproduction | 2609.33843v1 | Calibration fitting can fail its preregistered criterion; synthetic teacher agreement is not medical truth |

Evidence depth: the original three medical papers and Expert Merging have retrieved HTML full text and targeted architecture inspection; the other records above have abstract/metadata or upstream README evidence. All performance descriptions are author-reported. No paper has been reproduced by CommandMed. ICLR 2026 for OptMerge is repository-reported; independent proceedings verification remains pending. Expert Merging's inherited ICLR label is not independently verified here; use its verified arXiv identity in references.

The defensible research question is whether medical autoregressive/multimodal reasoning, native calibrated typed decisions and visual flow generation can share a semantic backbone with measurable encoder removal and retained quality under matched full-pipeline budgets. The conjunction remains a research target, not an established gap. HCF must differ demonstrably from ordinary heads, bridges, adapter composition and joint training. If it does not, report the simpler method and drop an unsupported method contribution.

Submission refresh must finish a declared bounded screening protocol, expand general unified-model and calibration/abstention coverage, snowball included studies, inspect full text for every central comparison, verify venue/version metadata, and update the claim ledger. The current snapshot is usable for preparation and narrowing claims; it cannot support a first claim.
