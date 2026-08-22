# Spec 003 — Independent Review Reconciliation

**Spec:** `003-data-license-provenance`
**Canonical base:** `a57f87e77bbd396332b197342d8129f6805ba452`
**Review sources:** independent CodeRabbit review on PR #25 plus post-review canonical-policy self-audit
**Status:** REPAIRED_PENDING_FINAL_EXACT_HEAD_REQUALIFICATION

## 1. Predecessor evidence invalidation

Two previously green implementation candidates are predecessor evidence only:

```text
ab594ad2756b33813d7b69166079849474a290aa
73048eed01583f13a24dff74748a50e3f33c91fa
```

`ab594ad...` was invalidated after independent review found two material authorization defects. `73048eed...` repaired those defects and passed exact-head GitHub validation, but a subsequent canonical-policy audit found that the repository's explicit MedGemma/HAI-DEF training-lineage default was documented but not machine-enforced. Therefore run `32596747649` and every earlier carrier result remain predecessor qualification only.

No predecessor PASS is used to qualify the final repaired head.

## 2. Finding R003-01 — Purpose-to-use authorization bypass

**Review thread:** `PRRT_kwDOT_FyzM6bbCBU`
**Original review comment:** `PRRC_kwDOT_FyzM7kso7_`
**Severity:** MATERIAL / SECURITY
**Resolution:** REPAIRED

### Finding

The evaluator special-cased `PRIVATE_GOLD` but did not enforce canonical Spec 001 `Purpose` policy before `ELIGIBLE`. A fully resolved record could present `PUBLIC_EXTERNAL_EVAL`, `CHECKPOINT_SELECTION`, `DEV`, or `CALIBRATION` while requesting training/adaptation.

### Repair

The V1 contract now contains and fail-closed validates this exact Purpose/use allowlist:

```text
TRAIN -> TRAINING_OR_ADAPTATION | TEACHER_OR_SYNTHETIC_GENERATION | MODIFICATION_OR_DERIVATION
DEV -> DEVELOPMENT_EVALUATION
CALIBRATION -> DEVELOPMENT_EVALUATION
CHECKPOINT_SELECTION -> DEVELOPMENT_EVALUATION
PUBLIC_EXTERNAL_EVAL -> DEVELOPMENT_EVALUATION | PRIVATE_RELEASE_EVALUATION
PRIVATE_GOLD -> PRIVATE_RELEASE_EVALUATION
```

Every non-`REFERENCE` use carrying canonical `Purpose` must be present in the allowlist or admission is `PROHIBITED / PURPOSE_USE_INCOMPATIBLE`. `validate_lineage_contract()` requires invariant `PURPOSE_USE_COMPATIBILITY_ENFORCED` and rejects a weakened/extended V1 matrix.

Regression tests cover public external evaluation/checkpoint-selection/dev -> training denial, TRAIN -> development-evaluation denial, public-evaluation -> redistribution denial, valid public development evaluation, and bounded private-Gold release evaluation.

## 3. Finding R003-02 — Parent restrictions not propagated

**Review thread:** `PRRT_kwDOT_FyzM6bbCBW`
**Original review comment:** `PRRC_kwDOT_FyzM7kso8C`
**Severity:** MATERIAL / SECURITY
**Resolution:** REPAIRED

### Finding

`parent_asset_ids` were local strings only. Parent records were not required to resolve and their restrictions were not propagated to derived/synthetic admission.

### Repair

The implementation now:

1. requires every referenced parent to resolve in the supplied lineage registry;
2. rejects duplicate IDs, self-parent references, unresolved parents, and cycles;
3. requires parent evidence to be scoped to the same exact `declared_use` as the child;
4. recursively evaluates parent records;
5. propagates parent state fail-closed:
   - `PROHIBITED` -> child `PROHIBITED / PARENT_PROHIBITED`;
   - `REFERENCE_ONLY` -> child `BLOCKED / PARENT_REFERENCE_ONLY`;
   - `BLOCKED` -> child `BLOCKED / PARENT_BLOCKED`;
   - no resolver -> `PARENT_REGISTRY_REQUIRED`;
   - invalid registry -> `PARENT_REGISTRY_INVALID`;
   - exact-use mismatch -> `PARENT_USE_EVIDENCE_MISMATCH`.

The contract requires invariant `PARENT_RESTRICTIONS_PROPAGATE`.

Regression tests cover missing registry, unresolved/self parent, cycles, exact-use mismatch, prohibited public-evaluation parent, unresolved-rights parent, reference-only parent, and a clean eligible training parent.

## 4. Finding S003-01 — Canonical reference-teacher policy was documented but not executable

**Source:** post-review audit against canonical `AGENTS.md`, grand master plan, Spec 003 specification, and implementation
**Severity:** MATERIAL / POLICY-ENFORCEMENT
**Resolution:** REPAIRED

### Canonical requirement

Canonical project policy states:

```text
MedGemma/HAI-DEF models are reference/evaluation assets only; their outputs must not train commandMed.
Frontier API outputs are evaluation/reference-only unless their terms explicitly permit the intended training use.
```

Spec 003 also required this default not to be silently weakened.

### Gap

The earlier implementation required generic `output_use_evidence_uri`, parent lineage, rights, privacy, and contamination evidence but had no machine rule preventing a clean-looking MedGemma/HAI-DEF-generated record from becoming `ELIGIBLE` for `TRAINING_OR_ADAPTATION`.

### Repair

The final V1 contract now requires invariant:

```text
REFERENCE_TEACHER_OUTPUTS_NOT_TRAINING_LINEAGE
```

and an exact fail-closed marker set:

```text
hai-def
hai_def
health-ai-developer-foundations
medgemma
```

`validate_lineage_contract()` treats that set as canonical V1 policy and rejects removal/extension. For `MODEL_GENERATED_OR_SYNTHETIC_ASSET` with declared use `TRAINING_OR_ADAPTATION`, a generator identity matching one of these canonical reference-family markers yields:

```text
PROHIBITED / GENERATOR_TRAINING_PROHIBITED
```

A non-prohibited external/provider output still does **not** become training lineage merely from its name: it must separately satisfy exact-use rights evidence, output-use evidence, parent resolution/propagation, privacy, contamination, artifact binding, and all other admission gates.

Regression tests cover contract-invariant removal, marker-set weakening, MedGemma-generated output training denial, HAI-DEF-generated output training denial, and clean non-prohibited-provider parent propagation.

## 5. Adjacent hardening

The reconciliation also makes these fail-closed rules explicit:

- `PRIVATE_GOLD` purpose and quarantine state agree in both directions;
- generic `QUARANTINED` state prohibits non-reference admission;
- Purpose/use policy is an exact allowlist for all non-reference uses;
- scientific identity and admission remain evaluator-owned rather than caller-asserted;
- source/family verification remains distinct from exact artifact binding;
- unresolved or component-specific rights cannot be widened by a child or generated artifact.

## 6. Authority boundary

Nothing in these repairs authorizes execution or data access.

```text
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
TEACHER_API_GENERATION_AUTHORITY=NONE
PHI_RESTRICTED_DATA_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_PAYLOAD_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
SPEC_004=BLOCKED
```

All tests and records are metadata/fixture-only. No model/provider call, benchmark payload, model weight, PHI, restricted data, or private-Gold payload is required.

## 7. Final qualification status

```text
AB594_QUALIFICATION=INVALIDATED_BY_R003_01_AND_R003_02
73048_QUALIFICATION=INVALIDATED_BY_S003_01
ALL_REPAIRS_IMPLEMENTED=YES
FOCUSED_REGRESSION_TESTS_ADDED=YES
CURRENT_FINAL_HEAD_QUALIFICATION=PENDING
FRESH_INDEPENDENT_FINAL_HEAD_REVIEW=PENDING
MERGE_AUTHORIZED=NO
```

The final repaired head must pass a fresh exact-head GitHub validation carrier, inherited semantic-identity checks, focused tests, full offline regression, diff hygiene, bounded-path preflight, and a fresh independent exact-head review before PR #25 may be considered merge-qualified.
