# Spec 003 — Independent Review Reconciliation

**Spec:** `003-data-license-provenance`
**Canonical base:** `a57f87e77bbd396332b197342d8129f6805ba452`
**Review sources:** independent CodeRabbit review on PR #25 plus post-review canonical-policy self-audit
**Status:** REPAIRED_PENDING_FINAL_EXACT_HEAD_REQUALIFICATION

## 1. Predecessor evidence invalidation

Four previously green implementation candidates are predecessor evidence only:

```text
ab594ad2756b33813d7b69166079849474a290aa
73048eed01583f13a24dff74748a50e3f33c91fa
2bd7e453575b01484428a76b34cbe451cdc5f0a1
378d30b184a1a60aa68a40a38a96ff686429c9f2
```

`ab594ad...` was invalidated after independent review found two material authorization defects. `73048eed...` repaired those defects and passed exact-head GitHub validation, but a subsequent canonical-policy audit found that the explicit MedGemma/HAI-DEF training-lineage default was documented but not machine-enforced. `2bd7e453...` added that policy and passed exact-head validation, but the next exact-head independent review found a classification-laundering bypass through `DERIVED_RESEARCH_ARTIFACT`. `378d30b...` repaired that derived-class bypass and passed exact-head validation, but fresh independent review found that the same prohibited teacher output could still be relabeled as a generic `DATASET_OR_CORPUS` because `asset_class` remained caller-controlled evidence.

No predecessor PASS is used to qualify the final repaired head.

## 2. Finding R003-01 — Purpose-to-use authorization bypass

**Review thread:** `PRRT_kwDOT_FyzM6bbCBU`
**Original review comment:** `PRRC_kwDOT_FyzM7kso7_`
**Severity:** MATERIAL / SECURITY
**Resolution:** REPAIRED

### Finding

The evaluator special-cased `PRIVATE_GOLD` but did not enforce canonical Spec 001 `Purpose` policy before `ELIGIBLE`. A fully resolved record could present `PUBLIC_EXTERNAL_EVAL`, `CHECKPOINT_SELECTION`, `DEV`, or `CALIBRATION` while requesting training/adaptation.

### Repair

The V1 contract contains and fail-closed validates this exact Purpose/use allowlist:

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

The V1 contract requires invariant:

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

The marker set is itself contract-validated and cannot be removed or extended silently. Training admission for generated/derived output must separately satisfy exact-use rights evidence, output-use evidence, parent resolution/propagation, privacy, contamination, artifact binding, and all other gates.

## 5. Finding R003-03 — Reference-teacher classification laundering through derived artifacts

**Source:** fresh exact-head CodeRabbit review of `2bd7e453575b01484428a76b34cbe451cdc5f0a1`
**Severity:** MATERIAL / SECURITY
**Resolution:** REPAIRED

### Finding

The first reference-teacher repair applied the prohibited-generator marker check only to `MODEL_GENERATED_OR_SYNTHETIC_ASSET`. A caller could instead represent the same model output as:

```text
asset_class=DERIVED_RESEARCH_ARTIFACT
origin_type=DERIVED
declared_use=TRAINING_OR_ADAPTATION
```

omit `generator_identity`, provide a clean parent registry, and potentially reach `ELIGIBLE`.

### Repair

The training-lineage producer/generator boundary was extended across both derived classes:

```text
MODEL_GENERATED_OR_SYNTHETIC_ASSET
DERIVED_RESEARCH_ARTIFACT
```

For `TRAINING_OR_ADAPTATION`, derived records require explicit producer/generator identity and output-use evidence; prohibited MedGemma/HAI-DEF markers produce `PROHIBITED / GENERATOR_TRAINING_PROHIBITED`.

Dedicated regression coverage proves missing producer provenance blocks, MedGemma/HAI-DEF relabeling to `DERIVED_RESEARCH_ARTIFACT` is prohibited, and a deterministic non-prohibited derivation can remain eligible only when every exact-use gate passes.

## 6. Finding R003-04 — Reference-teacher laundering through a generic non-derived asset class

**Source:** fresh exact-head CodeRabbit review of `378d30b184a1a60aa68a40a38a96ff686429c9f2`
**Severity:** MATERIAL / SECURITY
**Resolution:** REPAIRED_PENDING_REQUALIFICATION

### Finding

The R003-03 repair still treated `asset_class` as a practical provenance boundary. Because `asset_class` is caller-controlled evidence, the same MedGemma/HAI-DEF output could be represented as:

```text
asset_class=DATASET_OR_CORPUS
declared_use=TRAINING_OR_ADAPTATION
```

and omit `origin_type`, `parent_asset_ids`, `generator_identity`, and `output_use_evidence_uri`. With otherwise clean-looking training metadata, that generic-class record could reach `ELIGIBLE`.

### Repair

Training-origin enforcement is now independent of `asset_class`.

For every `TRAINING_OR_ADAPTATION` record:

1. `origin_type` is mandatory; omission is an invalid record rather than an implicit `ORIGINAL` default.
2. Any non-`ORIGINAL` origin requires:
   - `parent_asset_ids`;
   - `generator_identity` / producer identity;
   - resolved `output_use_evidence_uri`;
   - `generation_config_id` when `origin_type=MODEL_GENERATED`.
3. `origin_type=ORIGINAL` together with `generator_identity` is contradictory and fails validation.
4. The prohibited MedGemma/HAI-DEF marker scan runs for **all training records**, not only records whose `asset_class` is derived/model-generated.
5. The marker scan uses identity-bearing producer/source metadata including `generator_identity`, `source_identifier`, `canonical_name`, `source_uri`, `source_evidence_uri`, and `artifact_locator`.
6. Non-original generic-class records with parents enter the same registry-resolution and recursive parent-propagation path as explicit derived classes.

The contract now requires:

```text
TRAINING_ORIGIN_PROVENANCE_REQUIRED
```

and `validate_lineage_contract()` treats removal of that invariant as a weakened invalid V1 contract.

Dedicated regression coverage proves:

- a training record with omitted `origin_type` is invalid;
- a non-original `DATASET_OR_CORPUS` cannot omit parent/generator/config/output-use provenance;
- MedGemma output relabeled as `DATASET_OR_CORPUS` and `ORIGINAL` is still prohibited from training when its source/canonical provenance identifies the reference family;
- the same is true for HAI-DEF;
- contradictory `ORIGINAL` plus generator identity is invalid;
- a non-prohibited model-generated generic dataset can remain eligible only with complete provenance, an eligible exact-use parent, and every other gate satisfied.

## 7. Adjacent hardening

The reconciliation also makes these fail-closed rules explicit:

- `PRIVATE_GOLD` purpose and quarantine state agree in both directions;
- generic `QUARANTINED` state prohibits non-reference admission;
- Purpose/use policy is an exact allowlist for all non-reference uses;
- scientific identity and admission remain evaluator-owned rather than caller-asserted;
- source/family verification remains distinct from exact artifact binding;
- unresolved or component-specific rights cannot be widened by a child or generated artifact;
- training provenance cannot be broadened by changing `asset_class`;
- non-original training lineage cannot omit producer/generator provenance;
- original training origin is explicit rather than inferred.

## 8. Authority boundary

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

## 9. Final qualification status

```text
AB594_QUALIFICATION=INVALIDATED_BY_R003_01_AND_R003_02
73048_QUALIFICATION=INVALIDATED_BY_S003_01
2BD7_QUALIFICATION=INVALIDATED_BY_R003_03
378D_QUALIFICATION=INVALIDATED_BY_R003_04
ALL_KNOWN_REPAIRS_IMPLEMENTED=YES
FOCUSED_REGRESSION_TESTS_ADDED=YES
CURRENT_FINAL_HEAD_QUALIFICATION=PENDING
FRESH_INDEPENDENT_FINAL_HEAD_REVIEW=PENDING
MERGE_AUTHORIZED=NO
```

The final repaired head must pass a fresh exact-head GitHub validation carrier, inherited semantic-identity checks, all focused regression tests, full offline regression, diff hygiene, bounded-path preflight, and a fresh independent exact-head review before PR #25 may be considered merge-qualified.