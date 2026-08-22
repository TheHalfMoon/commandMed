# Spec 003 — Data, License & Provenance Candidate Closeout Evidence

**Closeout type:** metadata-only lineage-governance implementation
**Status:** `CLOSEOUT_CANDIDATE_PENDING_EXTERNAL_EXACT_HEAD_QUALIFICATION`
**Canonical starting base:** `a57f87e77bbd396332b197342d8129f6805ba452`
**Implementation branch:** `spec/003-data-license-provenance`
**Implementation PR:** `#25`
**State transition rule:** implementation merge does not make Spec 003 `CLOSED_CANONICAL`; a dedicated post-merge closure-only PR remains required.

## 1. Purpose

Record the bounded Spec 003 implementation evidence without creating a self-referential final-head claim and without granting any model, benchmark, training, provider, PHI, private-Gold, restricted-data, gated-asset, or Spec 004 authority.

Spec 003 adds one reusable, fail-closed lineage layer for:

- canonical lineage-contract validation;
- exact artifact binding;
- source verification and exact-use rights separation;
- privacy/access and contamination evidence;
- canonical Spec 001 Purpose/use authorization;
- private-Gold/quarantine preservation;
- generated/derived parent lineage and recursive restriction propagation;
- class-independent training-origin provenance;
- class-independent MedGemma/HAI-DEF reference-teacher training prohibition;
- deterministic scientific-record and admission identities.

It does not create a data lake, payload ingester, model registry service, downloader, inference runner, benchmark runner, training loop, provider client, legal-compliance engine, or Spec 004 tournament implementation.

## 2. Implementation predecessor qualification

Immediately before this closeout file was added, exact implementation head:

```text
IMPLEMENTATION_PREDECESSOR_HEAD=a251ef1ac8e519dff94048e779678c50d2be8d83
CANONICAL_BASE=a57f87e77bbd396332b197342d8129f6805ba452
VALIDATION_RUN=32598082466
VALIDATION_JOB=97092060616
WORKFLOW=Spec 003 Exact-Head Validation
CONCLUSION=SUCCESS
```

GitHub Actions explicitly checked out detached HEAD `a251ef1ac8e519dff94048e779678c50d2be8d83` rather than the carrier branch head.

Observed exact-head evidence:

```text
EXACT_HEAD=a251ef1ac8e519dff94048e779678c50d2be8d83
PYTHON_VERSION=3.11.16
PYTHON_SYNTAX=PASS
LINEAGE_CONTRACT_VALIDATION=PASS
LINEAGE_CONTRACT_SHA256=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
FOCUSED_SPEC003_TESTS=71/71_PASS
INHERITED_HARD_GATES=9/9_PASS
FULL_OFFLINE_SUITE=228/228_PASS
INHERITED_SEMANTIC_IDENTITIES=PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
```

Because this closeout document creates a newer branch head, the implementation predecessor above is intentionally **not** the final PR-head qualification. The resulting closeout head must be requalified externally after this document's final repository-content mutation.

## 3. Independent exact-head review evidence

A fresh CodeRabbit static review was explicitly requested against exact implementation predecessor `a251ef1ac8e519dff94048e779678c50d2be8d83` and canonical base `a57f87e77bbd396332b197342d8129f6805ba452`.

The review reported:

```text
INDEPENDENT_EXACT_HEAD_STATIC_REVIEW=PASS_NO_REMAINING_MATERIAL_AUTHORIZATION_OR_SECURITY_BYPASS
```

The review statically verified, among other controls:

- exact V1 Purpose/use authorization and prohibited-generator marker contract enforcement;
- mandatory `origin_type` for every training/adaptation record;
- parent, generator/producer, and output-use evidence for non-original training lineage;
- generation-config identity for model-generated training lineage;
- parent resolution and recursive restriction propagation;
- immutable locator binding and rejection of mutable/named revisions;
- fail-closed rights, privacy, contamination, quarantine, and private-Gold controls;
- caller-supplied admission/scientific-identity rejection;
- metadata-only authority boundary with no payload/model/provider/training access.

CodeRabbit did not independently rerun repository tests in its sandbox; GitHub Actions Run `32598082466` is the executable qualification evidence. The static review independently checked the requested exact commit/base and `git diff --check` and found no remaining material blocker.

## 4. Material review reconciliation

All known material findings before this closeout candidate are recorded in `review-reconciliation.md` and repaired on the implementation predecessor:

1. **R003-01 — Purpose/use authorization bypass**
   - repaired with exact canonical `Purpose -> declared_use` allowlist and contract invariant.
2. **R003-02 — Parent restrictions not propagated**
   - repaired with registry resolution, cycle rejection, exact-use matching, and recursive parent-state propagation.
3. **S003-01 — Canonical MedGemma/HAI-DEF policy documented but not executable**
   - repaired with contract-bound prohibited reference-teacher markers.
4. **R003-03 — Reference-teacher laundering through `DERIVED_RESEARCH_ARTIFACT`**
   - repaired by requiring producer/generator provenance for derived training lineage and applying the prohibited-family gate beyond the model-generated class.
5. **R003-04 — Reference-teacher laundering through generic `DATASET_OR_CORPUS`**
   - repaired by making training-origin provenance and prohibited-family detection independent of `asset_class`.

Previously green heads invalidated by later material findings remain predecessor evidence only:

```text
ab594ad2756b33813d7b69166079849474a290aa
73048eed01583f13a24dff74748a50e3f33c91fa
2bd7e453575b01484428a76b34cbe451cdc5f0a1
378d30b184a1a60aa68a40a38a96ff686429c9f2
```

No prior PASS substitutes for final closeout-head qualification.

## 5. Final-head binding without self-reference

This closeout file MUST NOT be mutated merely to embed the SHA produced by its own mutation. Doing so would create an endless self-reference cycle.

Final PR-head qualification is therefore bound by immutable GitHub evidence external to this file:

1. the temporary GitHub validation carrier explicitly checks out the resulting final PR head SHA;
2. the workflow requires the canonical lineage-contract SHA and inherited semantic identities;
3. the run/job records prove focused tests, inherited hard gates, full regression, diff hygiene, and bounded path scope on that exact SHA;
4. a fresh independent review is anchored to that same final SHA;
5. any later repository-content mutation invalidates final qualification and requires a new exact-head run/review.

PR Draft/Ready state is external GitHub metadata and is not frozen as a current-state assertion inside this document. Ready state alone never grants merge authority.

After this file's final mutation, no further repository-content change is permitted before final qualification unless a material defect is discovered.

## 6. Canonical semantic identities

The implementation-predecessor qualification re-confirmed:

```text
data/lineage/lineage_contract.json=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
data/eval/benchmarks.json=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
data/eval/gold_protocols.json=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
data/eval/metrics.json=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
data/eval/quarantine.json=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
data/eval/safety_policy.json=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
SEMANTIC_IDENTITIES=PASS
```

The final external exact-head run must re-confirm these identities after this evidence-only mutation.

## 7. Acceptance matrix

| # | Spec 003 acceptance criterion | Candidate evidence | Status |
|---|---|---|---|
| 1 | Contract validates fail-closed before record admission | contract validator + weakening regressions | CANDIDATE_PASS |
| 2 | Source verification is distinct from exact artifact binding | explicit states + immutable/direct binding tests | CANDIDATE_PASS |
| 3 | Exact-byte uses cannot silently use mutable/unbound identity | mutable/named revision and UNBOUND regressions | CANDIDATE_PASS |
| 4 | Rights/privacy uncertainty cannot become eligible by assumption | fail-closed admission regressions | CANDIDATE_PASS |
| 5 | Private Gold and quarantine semantics remain bounded | bidirectional purpose/quarantine + use-denial tests | CANDIDATE_PASS |
| 6 | Canonical Purpose cannot authorize a broader declared use | exact Purpose/use contract matrix + negative tests | CANDIDATE_PASS |
| 7 | Derived/generated parents resolve and restrictions propagate | registry/cycle/exact-use/recursive propagation tests | CANDIDATE_PASS |
| 8 | Training provenance cannot be broadened by asset-class relabeling | mandatory origin + generic/derived laundering tests | CANDIDATE_PASS |
| 9 | MedGemma/HAI-DEF outputs remain non-training by canonical default | class-independent producer/source marker gate | CANDIDATE_PASS |
| 10 | Scientific identity/admission are evaluator-owned and deterministic | canonical hashing + computed-field rejection tests | CANDIDATE_PASS |
| 11 | Spec 001 semantic identities and hard gates remain intact | Run #32598082466 predecessor evidence | PENDING_FINAL_PR_HEAD |
| 12 | Focused/full offline tests and final scope hygiene pass on unchanged closeout head | external exact-head carrier + fresh review | PENDING_FINAL_PR_HEAD |

Spec 003 MUST NOT be described as fully merge-qualified until rows 11 and 12 are re-proven on the final exact PR head produced by this closeout document.

## 8. Repository-scope authority attestation

```text
MODEL_RUNTIME_OR_DOWNLOADER_ADDED=NO
BENCHMARK_RUNNER_ADDED=NO
TRAINING_LOOP_ADDED=NO
PROVIDER_CLIENT_ADDED=NO
DATA_INGESTION_SERVICE_ADDED=NO
NEW_THIRD_PARTY_RUNTIME_DEPENDENCY=NO
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
TEACHER_API_GENERATION_AUTHORITY=NONE
PHI_RESTRICTED_DATA_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_PAYLOAD_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
SPEC_004=BLOCKED
```

Spec 003 qualification uses synthetic metadata and canonical repository metadata only. It does not require or authorize model weights, inference, training, external teacher generation, benchmark payload execution, PHI, restricted clinical data, private-Gold payloads, or gated assets.

## 9. Final qualification gate

Before guarded merge of PR #25, all of the following must be true on the one unchanged final exact head created by this document:

1. lineage contract validation passes;
2. lineage-contract SHA-256 remains `2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962`;
3. all focused Spec 003 lineage regressions pass;
4. inherited Spec 001 hard-gate tests pass;
5. complete offline repository regression passes;
6. inherited semantic identities remain unchanged;
7. `git diff --check` and bounded-path preflight pass;
8. all material review findings remain reconciled;
9. fresh independent exact-head review finds no material authorization/security blocker;
10. PR metadata records the final exact candidate and qualification evidence;
11. GitHub PR metadata shows Ready on that unchanged exact head immediately before merge;
12. guarded merge is performed without any intervening repository-content mutation.

Until every final gate is externally proven:

```text
SPEC_003=CLOSEOUT_CANDIDATE_PENDING_EXTERNAL_EXACT_HEAD_QUALIFICATION
MERGE_AUTHORITY=NO
SPEC_004=BLOCKED
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```

After a qualified implementation merge, Spec 003 still remains not `CLOSED_CANONICAL` until a dedicated closure-only PR binds the resulting canonical implementation merge SHA/tree and updates `specs/README.md`.