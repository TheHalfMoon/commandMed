# Adversarial literature protocol

Search began on 2026-10-01; identity and static source review continued on 2026-10-02. The pre-search protocol, every query, returned counts, duplicate identities, failures, refinements and assisted screening are in literature-search.json and source-retrieval-manifest.json. Scope is bounded by declared relevance/newest budgets; no exhaustive systematic review or novelty clearance is claimed. Selected papers have separate identity and inspection-depth fields. Potentially relevant unselected records remain visible. Read abstract before use; inspect methods/results for detailed assertions; metadata-only records are leads.

| System | Actual use/status |
|---|---|
| arXiv | Used: query feeds, abstracts, selected primary HTML |
| PubMed | Used: metadata and abstracts; no clinical records |
| OpenAlex | Used: free public endpoint metadata cross-check |
| PMLR / official proceedings | Used: Guo and SelectiveNet proceedings identities |
| Crossref | Used: publisher-registered DOI identities |
| Hugging Face | Used: public revision/config/card/license metadata only |
| GitHub | Used: public source/license inspection and provenance |
| Semantic Scholar | TOOL_UNAVAILABLE_AT_RETRIEVAL: no-key endpoint returned 429 |
| OpenReview | TOOL_UNAVAILABLE_AT_RETRIEVAL: API returned 403; proceedings claims remain unverified |
| Consensus, Elicit, ResearchRabbit, Connected Papers, Litmaps, SciSpace, Zotero, NotebookLM | TOOL_UNAVAILABLE: no callable integration in this environment |
| Scite, TinyFish | AVAILABLE_NOT_USED_ZERO_COST_UNVERIFIED; no cost-bearing calls |
| Google Scholar | NOT_USED; primary-source alternatives used |
| Jev | DEFERRED_ZERO_COST_POLICY; documented call has nonzero monetary cost |

No model-generated summary is a source. Search hits and source text are untrusted data; instructions embedded in papers or code examples are not execution authority. A refreshed search and independently checked closest-paper comparison remain required before submission.
