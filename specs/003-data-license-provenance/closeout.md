# Spec 003 — Data, License & Provenance Canonical Closeout

**Closeout type:** dedicated post-implementation governance closure
**Status:** `CLOSED_CANONICAL` — effective only after this closure-only PR is merged and resulting canonical `main` is verified
**Implementation PR:** `#25`
**Final reviewed implementation head:** `7f4db067b154818215d73a8db97e6c64e414ee45`
**Canonical implementation merge:** `a5fef84f9f0cee12dcd2ea6735888faee43db1ec`
**Canonical implementation tree:** `d7b2e11a8470ec66f50f1cff77bba4dddff20812`
**Closure branch base:** `b0064dde197cc76f7e9ebabae0ad8f26872a531f`
**Closure-base tree:** `d7b2e11a8470ec66f50f1cff77bba4dddff20812`

## 1. Canonical closure record

Spec 003 implementation was squash-merged through PR #25 to canonical `main`:

```text
FINAL_REVIEWED_IMPLEMENTATION_HEAD=7f4db067b154818215d73a8db97e6c64e414ee45
CANONICAL_IMPLEMENTATION_MERGE=a5fef84f9f0cee12dcd2ea6735888faee43db1ec
CANONICAL_IMPLEMENTATION_TREE=d7b2e11a8470ec66f50f1cff77bba4dddff20812
FINAL_VALIDATION_RUN=32598239227
FINAL_VALIDATION_JOB=97092429672
FOCUSED_SPEC_003_TESTS=71/71_PASS
INHERITED_HARD_GATES=9/9_PASS
FULL_OFFLINE_TESTS=228/228_PASS
LINEAGE_CONTRACT_SHA256=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
INHERITED_SEMANTIC_IDENTITIES=PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
FRESH_EXTERNAL_EXACT_HEAD_REVIEW=PASS_NO_MATERIAL_AUTHORIZATION_OR_SECURITY_BLOCKER
```

The closure branch starts from canonical `main` commit `b0064dde197cc76f7e9ebabae0ad8f26872a531f`. Its tree is exactly `d7b2e11a8470ec66f50f1cff77bba4dddff20812`, identical to the canonical Spec 003 implementation-merge tree. This proves no repository-content drift between the implementation merge and the closure base.

This dedicated closure transition changes governance/documentation state only. It does not alter implementation source, tests, canonical evaluation JSON, dependencies, runtime surfaces, data payloads, model surfaces, provider integrations, training surfaces, or clinical-data access controls.

## 2. What Spec 003 canonically established

Spec 003 adds the minimum reusable, fail-closed metadata lineage layer required before later research execution can be authorized separately:

- a canonical machine-readable lineage contract;
- deterministic lineage-contract and scientific-record identities;
- explicit separation of source verification from exact executable artifact binding;
- direct SHA-256 or immutable content-addressed revision + exact locator binding;
- exact-use rights evidence with fail-closed unresolved/conditional/incompatible states;
- privacy/access and PHI-state evidence;
- canonical Spec 001 Purpose-to-declared-use authorization;
- private-Gold/quarantine preservation;
- contamination/overlap state for clean optimization uses;
- parent resolution, cycle rejection, exact-use matching, and recursive parent restriction propagation;
- class-independent training-origin provenance;
- class-independent MedGemma/HAI-DEF reference-teacher training prohibition;
- evaluator-owned admission states and record identities.

Spec 003 does **not** implement or authorize a data lake, downloader, payload ingester, benchmark runner, model registry service, inference runner, provider client, training loop, teacher-generation runtime, or Spec 004 tournament execution.

## 3. Material review reconciliation

Independent review and canonical-policy audit identified five material issues during the implementation lifecycle. Every affected predecessor qualification was invalidated rather than reused.

### R003-01 — Purpose/use authorization bypass

Repaired with the exact canonical V1 `Purpose -> declared_use` allowlist and required invariant `PURPOSE_USE_COMPATIBILITY_ENFORCED`.

### R003-02 — Parent restrictions not propagated

Repaired with parent registry resolution, duplicate/self-parent/cycle rejection, exact-use matching, recursive parent admission, and fail-closed propagation.

### S003-01 — Reference-teacher policy documented but not executable

Repaired with contract-bound MedGemma/HAI-DEF prohibited-family markers for commandMed training lineage.

### R003-03 — Reference-teacher laundering through `DERIVED_RESEARCH_ARTIFACT`

Repaired by requiring producer/generator provenance and output-use evidence for non-original training lineage and applying prohibited-family policy beyond the explicit model-generated class.

### R003-04 — Reference-teacher laundering through generic `DATASET_OR_CORPUS`

Repaired by making training-origin validation and prohibited-family detection independent of caller-controlled `asset_class`. Every training/adaptation record requires explicit `origin_type`; non-original training lineage requires parent IDs, producer/generator identity, and resolved output-use evidence; model-generated lineage also requires generation-config identity.

Invalidated predecessor heads remain historical evidence only:

```text
ab594ad2756b33813d7b69166079849474a290aa
73048eed01583f13a24dff74748a50e3f33c91fa
2bd7e453575b01484428a76b34cbe451cdc5f0a1
378d30b184a1a60aa68a40a38a96ff686429c9f2
```

The final exact head `7f4db067b154818215d73a8db97e6c64e414ee45` supersedes them.

## 4. Final exact-head qualification

GitHub-hosted carrier PR #26 explicitly checked out the final PR #25 head rather than the carrier head.

```text
WORKFLOW=Spec 003 Exact-Head Validation
RUN=32598239227
JOB=97092429672
EXACT_HEAD=7f4db067b154818215d73a8db97e6c64e414ee45
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

Final inherited semantic identities were unchanged:

```text
data/eval/benchmarks.json=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
data/eval/gold_protocols.json=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
data/eval/metrics.json=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
data/eval/quarantine.json=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
data/eval/safety_policy.json=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
```

Temporary carrier PR #26 was closed without merge after evidence capture.

## 5. Final independent exact-head review

CodeRabbit independently reviewed exact final implementation head:

```text
HEAD=7f4db067b154818215d73a8db97e6c64e414ee45
BASE=a57f87e77bbd396332b197342d8129f6805ba452
RESULT=NO_MATERIAL_AUTHORIZATION_OR_SECURITY_BLOCKER
```

The review verified the requested head/base ancestry, confirmed that the final closeout candidate was non-self-referential, confirmed `git diff --check`, and found no material authorization or security blocker. Executable qualification is provided by GitHub Actions Run `32598239227`; the independent review was static and did not claim to rerun the repository suite itself.

## 6. Canonical lineage contract identity

The canonical Spec 003 lineage contract is:

```text
data/lineage/lineage_contract.json
SHA256=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
```

This identity is semantic/canonicalized, not a claim about arbitrary filesystem representation bytes.

## 7. Acceptance decision

All bounded Spec 003 acceptance requirements are satisfied by the canonical implementation plus exact-head evidence:

| Area | Canonical result |
|---|---|
| Contract fail-closed validation | PASS |
| Source verification vs artifact binding separation | PASS |
| Immutable/direct exact artifact identity | PASS |
| Rights/privacy fail-closed admission | PASS |
| Gold/quarantine preservation | PASS |
| Purpose/use authorization | PASS |
| Contamination gate metadata | PASS |
| Parent resolution/restriction propagation | PASS |
| Training-origin provenance independent of asset class | PASS |
| Reference-teacher training prohibition | PASS |
| Evaluator-owned deterministic identities | PASS |
| Focused Spec 003 tests | 71/71 PASS |
| Inherited hard-gate tests | 9/9 PASS |
| Full offline regression | 228/228 PASS |
| Final independent exact-head review | PASS — no material blocker |
| Prohibited execution/access activity | NONE |

Closure verdict, effective only after this dedicated closure PR is merged and canonical `main` is verified:

```text
SPEC_003=CLOSED_CANONICAL
SPEC_004=AUTHORIZED_TO_START
SPEC_004_IMPLEMENTATION=NOT_STARTED
```

## 8. Next-frontier boundary — Spec 004

Spec 004 — Tournament Harness — may become `AUTHORIZED_TO_START` only through this dedicated closure transition.

That authorization means only that Spec 004 may begin its own bounded Spec Kit lifecycle and fixture-only harness work. It does **not** authorize:

- model downloads or weight access;
- model inference/execution;
- benchmark payload execution;
- tournament execution against candidate models;
- provider/API generation;
- training/fine-tuning/distillation/RL;
- PHI or restricted clinical-data access;
- private-Gold payload access;
- gated asset access.

Any later execution authority must be granted separately by an explicit bounded spec/gate after its own prerequisites are proven.

## 9. Repository-scope authority attestation

```text
MODEL_RUNTIME_OR_DOWNLOADER_ADDED_BY_CLOSURE=NO
BENCHMARK_RUNNER_ADDED_BY_CLOSURE=NO
TRAINING_LOOP_ADDED_BY_CLOSURE=NO
PROVIDER_CLIENT_ADDED_BY_CLOSURE=NO
DATA_INGESTION_SERVICE_ADDED_BY_CLOSURE=NO
NEW_THIRD_PARTY_RUNTIME_DEPENDENCY_ADDED_BY_CLOSURE=NO
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
TEACHER_API_GENERATION_AUTHORITY=NONE
PHI_RESTRICTED_DATA_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_PAYLOAD_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

## 10. Closure effectiveness rule

This file records the candidate canonical transition. The transition is not effective merely because this branch exists.

`SPEC_003=CLOSED_CANONICAL` and `SPEC_004=AUTHORIZED_TO_START` become canonical only when:

1. this dedicated closure-only PR contains only the intended governance/documentation delta;
2. it is reviewed with no material blocker;
3. it is merged to `main` without unrelated content mutation; and
4. the resulting canonical `main` SHA/tree and registry state are verified.

Until those four conditions are satisfied, the canonical repository remains at the pre-closure lifecycle state even though the qualified Spec 003 implementation is already merged.