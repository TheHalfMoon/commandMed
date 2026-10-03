# Rights and Source Admission V5

Status: `STATIC_REVIEW_ONLY`; `PAYLOAD_EXECUTION=NO`.

## Admitted lineage candidates

### Small-model backbones

`Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68` and `HuggingFaceTB/SmolLM2-1.7B@effd688a12921b4cc83e3312b6feb579f70f9c71` were rechecked through public Hugging Face metadata. Both exact revisions resolved, were not gated/private, and exposed `license:apache-2.0` metadata at inspection time.

This is a model-card/repository admission fact, not a warranty about every upstream training datum. Training-data contamination remains a scientific limitation.

### AgentMD / RiskCalcs / RiskQA

Repository: `ncbi-nlp/Clinical-Tool-Learning@d474a95128e128623933c9be0d389ff7d82ef782`.

The bound root license states that the software/database is a United States Government Work and that NLM/U.S. Government placed no restriction on its use or reproduction. The study repository exposes RiskCalcs and RiskQA under this repository-level notice.

Bound identities:
- license blob: `8b18c9d4c47d23c56c4680381ed2e38c2025874a`
- RiskQA dataset blob: `2a2372ddd705efab4194f2ff7a3bf21c74dc1c7e`
- RiskQA tools tree: `aefb538408534212809ed2651309554c2bed596e`
- RiskQA README blob: `ce5bd60a2f0a8ebee8c524bbb3d735c11e05c0e8`
The published AgentMD article reports that RiskQA contains 350 questions created from manually validated calculator parameter sets. CommandMed may use that fact for prospective power planning, but does not treat the AgentMD paper's performance as CommandMed evidence.

The repository also contains private/restricted evaluation paths involving Yale ED notes and MIMIC data. Those paths are explicitly excluded. Public repository access does not authorize private clinical records.

## Selection-bias control

The public `chujiezheng/LLM-MCQ-Bias` repository was inspected at current commit `2ae2f40c77006f7a00a4675bdfb30151c2406691`. No root license file was visible in the inspected repository contents.

Therefore CommandMed will not copy or vendor that repository's code. `A2_SELBIAS_V1` will be an independent project-owned implementation from the published method description, with provenance to the paper and no claim of code identity.

## Still unadmitted

The following remain `NOT_ADMITTED` for confirmatory payload use: MedQA/USMLE derivatives, MedMCQA, PubMedQA article text, ArabicMMLU, MedArabiQ, MedAraBench, MIMIC-derived records, Yale clinical records, and medical image datasets. A permissive card label is not sufficient when underlying source-content rights or privacy constraints remain unresolved.

Scite MCP was also tested during this freeze pass and required a paid plan/free-trial activation. Under the zero-cost program it was not used as qualification evidence; public primary sources were used instead.
## Selected-calculator source audit — 2026-10-03

The hardened static RiskCalcs gate currently yields `82` eligible numeric/Boolean-threshold calculators across `15` first-listed source specialty strata, each with at least `1024` prospective states. The prospective 64-calculator set is selected by deterministic availability-constrained stratum round-robin, not by model performance and not as a prevalence sample.

For the current 64-entry set:
- all `64/64` PMIDs resolve through the public PubMed record;
- all `64/64` expose an abstract in the current PubMed fetch;
- `0/64` carry a PubMed publication-type retraction/withdrawal flag in the current metadata audit;
- exact source metadata and PubMed identities are recorded in `clinical-source-audit-v5.json`;
- `clinical-source-review-v5.md` remains a review queue rather than a clinical approval list.

This audit establishes provenance and removes unresolved/retracted-source failure modes. It does **not** establish that every historical score remains clinically appropriate today. The primary mechanical endpoint is therefore deterministic **rule conformance**. Any clinical-validity interpretation requires a separate qualified review of the specific rule, intended population, version, and use.

## Capability-retention control admission — 2026-10-03

`rajpurkar/squad` is admitted at revision `7b6d24c440a36b6815f21b70d25016731768db1f` for one narrow purpose: paired SQuAD v1.1 extractive-QA retention measurement on the validation split after parameter-changing interventions.

The dataset metadata reports `CC-BY-SA-4.0`. CommandMed does not infer dataset rights from the MIT license of the separate `SQuAD-explorer` software repository. The source payload will not be vendored in CommandMed; evaluation retrieves the pinned dataset externally and public artifacts expose attribution, source identity/hashes, configuration and aggregate metrics. Any broader redistribution requires a separate compliance review.

Because SQuAD is a long-public benchmark with plausible pretraining exposure, it cannot establish uncontaminated generalization or broad capability preservation. The allowed claim is restricted to paired retention on the named pinned SQuAD v1.1 validation task.
