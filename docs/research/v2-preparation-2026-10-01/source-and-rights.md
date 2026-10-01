# Source revisions, licenses and provenance

Status: metadata identities captured; scientific/runtime/rights qualification incomplete. `source-manifest.json` separates code revisions, model revisions, file Git blob OIDs, published LFS hashes and local hashes of retrieved metadata. Published weight hashes and sizes were read from public metadata; weight contents were never retrieved or verified locally.

Qwen3.8-27B model pin: `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`. Qwen-Image-2.1 model pin: `d26bb61231c349cf6b7896fa83353113880e1ba3`. Kev-27B model pin: `af0e6d551bdc2cc724f3e9d7a8bee1cd4fb8f7bf`. The full manifest also pins Kev-0.8B, its Qwen3.5-0.8B base, decider-2B, CLM's head repository and Qwen3-8B encoder. A GitHub code SHA is never substituted for a Hugging Face model SHA.

| Source | Observed license evidence | Admission implication |
|---|---|---|
| Qwen3.8 model | Retrieved Apache-2.0 text at pinned model revision | Preserve notices; post-training data provenance remains partly unknown; not a clinical winner |
| Qwen-Image-2.1 | Retrieved Qwen Research License, 2026-09-20 | Non-commercial research/evaluation only without separate commercial license; redistribution conditions still apply |
| Kev code/model | Code license text and model-card Apache label | Code/weight license does not resolve all training-data/teacher obligations; current 27B card names share-alike data and a generated-data teacher lineage |
| decider code/model | Code Apache text and model-card label | Teacher-labelled training provenance and intended derivative use require source-level review |
| CLM code/model | Code and model Apache text | Head is bound to its Qwen3-8B pooling encoder; no automatic transfer to Qwen3.8 |
| MergeKit | Retrieved LGPL v3 text | Inspect actual integration/distribution obligations; do not relabel the tool Apache-2.0; using a tool does not automatically determine an output model license |
| OptMerge repository | Apache text observed in `fusion_bench/LICENSE` | File/subtree scope only; root method code and bundled third-party projects need a file-level license inventory |
| ExpertMerging | No root license observed in complete tree | Reading/reference permitted; source copying/execution admission remains unresolved pending terms |
| Gax-registered Laya/restricted-logit | License text retrieved at registry's immutable pins | Baseline reference only; checkpoint identity and transport/admission still required |

Qwen Research License sections 2–4 require non-commercial use, passing on the agreement, marking modified files, preserving the required Notice, attribution when outputs/results improve a distributed model, and avoiding Qwen as the primary derivative name. A CommandMed Apache software license cannot erase these obligations. Research and permissive release lineages must stay separate. No commercial use, rights waiver, output distillation or release license is approved by this note.

The historical Gax URL now redirects publicly to `TheHalfMoon/DAL`. Current registry source: `d676beccfec001fd75d1b157b43068eb49a5733d`. Its CLM/decider revisions differ from the newly observed upstream snapshots; preserve both namespaces rather than substituting one for the other. Registry statuses qualify only that repository's adapters/control plane, not CommandMed execution or model performance. The historical source-map SHA could not be read through the connector and remains an unresolved historical lookup.

Still required before execution: complete tokenizer/processor artifacts and semantic token-ID checks, environment/runtime lock, file-level software obligations, dataset and teacher lineage review, exact asset access scope, resource/personnel bindings, and an authorized bounded execution spec. No inferred permission from a license, public availability or a donor's calibration certificate satisfies these gates.
