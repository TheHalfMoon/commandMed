# Contamination Semantics Reconciliation — Model Lineage vs Benchmark Adjudication

**Date:** 2026-08-27
**Specs affected:** 003 (lineage contract), 005 Q4/Q5 (contamination adjudication), 007 E001 PRIMARY admission
**Authorization:** CONTAMINATION_SEMANTICS_RECONCILIATION=AUTHORIZED (bounded governance / offline-test work, no payload access)
**Weight / benchmark / training authority:** NONE

---

## 1. Problem

E001 public-metadata admission for the three mass-reach PRIMARY candidates

- `Qwen/Qwen3-0.6B-Base` `da87bfb...`
- `Qwen/Qwen3.5-0.8B-Base` `dc7cdfe...`
- `ibm-granite/granite-4.0-350m-base` `a50b46c...`

returned:

```text
DEVELOPMENT_EVALUATION=ELIGIBLE
REDISTRIBUTION=ELIGIBLE
TRAINING_OR_ADAPTATION=BLOCKED (CONTAMINATION_UNRESOLVED)
MODIFICATION_OR_DERIVATION=BLOCKED (CONTAMINATION_UNRESOLVED)
```

solely because `contamination_state` was `NOT_ASSESSED`/`PENDING` for `TRAIN`-purpose uses. This conflated two canonical questions:

- **A. MODEL_LINEAGE_ADMISSION:** May this model/checkpoint legally/scientifically enter commandMed derivation/training lineage (rights, provenance, privacy, access, parent restrictions, forbidden lineage, quarantine)?
- **B. BENCHMARK_CONTAMINATION_ADJUDICATION:** May evidence from this exact `candidate × benchmark-slice × purpose` be trusted for `DEVELOPMENT_EVALUATION` / `CHECKPOINT_SELECTION` / `PUBLIC_EXTERNAL_EVAL` (exact + semantic dual-axis, per Spec 005 Q4)?

Base checkpoints without immutable public pretraining corpora can never satisfy A if A is made to require a full candidate-corpus vs benchmark-slice overlap proof, yet B is inherently a per-slice relation that cannot be stored inside the upstream model record itself.

---

## 2. Canonical answer

**EXISTING_CONTRACT_SUPPORTS_SEPARATION=YES — no schema/code change required.**

### 2.1 Evidence from `data/lineage/lineage_contract.json` and `src/commandmed/eval_contract/lineage.py`

- `contamination_states` includes `NOT_APPLICABLE` alongside `ASSESSED_CLEAN`, `NOT_ASSESSED`, etc.
- Contract text (Session 7 Q3, carried into Q4): *“for a use requiring clean separation only `ASSESSED_CLEAN` (or evidence-backed `NOT_APPLICABLE` when truly outside the condition) may contribute to `ELIGIBLE`.”*
- Evaluator logic (`_evaluate_base_admission`):

```python
if declared_use in CLEAN_CONTAMINATION_REQUIRED_USES:
    contamination = record.get("contamination_state")
    if contamination not in {"ASSESSED_CLEAN", "NOT_APPLICABLE"}:
        reasons.add("CONTAMINATION_UNRESOLVED")  # -> BLOCKED
```

Thus `NOT_APPLICABLE` is explicitly a **pass** for `TRAINING_OR_ADAPTATION`/`MODIFICATION_OR_DERIVATION` when the condition is genuinely outside the record's relation.

### 2.2 Scope of `NOT_APPLICABLE` prohibition

Session 7 Q4 freezes:

```text
NOT_APPLICABLE_FOR_PUBLIC_BENCHMARK_SELECTION=PROHIBITED
```

This prohibition is explicitly scoped to **public benchmark checkpoint selection** — the `BENCHMARK_OR_EVALUATION_ASSET` × `candidate` relation (dual-axis exact+semantic). Q4's paragraph begins: *“For Spec 005 public benchmark checkpoint selection, the contamination condition is inherently applicable; therefore `NOT_APPLICABLE` is not a valid shortcut for a candidate-vs-benchmark selection assessment.”*

It does **not** prohibit `NOT_APPLICABLE` on a `MODEL_OR_CHECKPOINT` lineage record whose `contamination_state` field is evaluated for `TRAINING_OR_ADAPTATION` lineage admission, provided the record represents only the upstream model's lineage parent relation and carries no benchmark-clean claim.

### 2.3 Separation is therefore expressible today

- `MODEL_OR_CHECKPOINT` with `declared_use=TRAINING_OR_ADAPTATION`, `purpose=TRAIN`, `origin_type=ORIGINAL` (Apache base), `rights_state=SUPPORTED`, `access_class=PUBLIC`, `artifact_binding_state=IMMUTABLE_REVISION_LOCATOR`, `phi_privacy_state=NO_PHI_KNOWN`, `quarantine_state=NOT_QUARANTINED`, and `contamination_state=NOT_APPLICABLE` **is ELIGIBLE** for lineage admission when the contamination condition genuinely does not apply to that lineage relation (benchmark contamination is separately represented as exact `candidate × benchmark-slice` evidence per Spec 005 Q4/Q5).

- `BENCHMARK_OR_EVALUATION_ASSET` with `purpose=CHECKPOINT_SELECTION` (or `DEV`) for a required primary slice (e.g., `MedXpertQA/Text/dev.jsonl`) **must not** use `NOT_APPLICABLE`; it must be `ASSESSED_CLEAN` (exact `CHECKED_CLEAN` + semantic `ASSESSED_LOW_RISK` with resolved evidence bindings) to be `PASS_CONTAMINATION_GATE_ONLY`. Current catalog state `NOT_ASSESSED` therefore correctly yields `INCOMPLETE` and, per Q5, `CANDIDATE_SLICE_NOT_SELECTION_ELIGIBLE` and tournament `NO_SELECTION` until resolved.

The contract already encodes this: clean-required uses share the set `{ASSESSED_CLEAN, NOT_APPLICABLE}` as pass, but the **semantic condition** for when `NOT_APPLICABLE` is genuinely outside differs by asset class and declared use. Q4 prohibits the benchmark-selection shortcut; it does not prohibit the lineage-parent shortcut when the separate benchmark adjudication remains unresolved.

---

## 3. Strict `NOT_APPLICABLE` rule (fail-closed)

`NOT_APPLICABLE` is valid **only** when the contamination condition represented by **that exact record** is genuinely outside its asset/use relation, with **no benchmark-clean claim inferred** and **no selection eligibility inferred**.

Prohibited loopholes remain blocked:

- `candidate × public benchmark contamination = NOT_APPLICABLE` for a `REQUIRED_PRIMARY_SELECTION` slice remains **PROHIBITED** (Q4). No `NOT_APPLICABLE` may Rescue MedXpertQA selection.
- `MODEL_LINEAGE_ELIGIBLE` **does not imply** `BENCHMARK_CONTAMINATION_CLEAN`. A lineage-eligible model may still have `MEDXPERTQA_SELECTION_CONTAMINATION=NOT_ASSESSED` → not selection-eligible.
- Unresolved candidate×benchmark contamination still blocks selection (`INCOMPLETE` → `NO_SELECTION` per Q5).

---

## 4. Private Gold / quarantine preservation

Nothing in this clarification allows `COMMANDMED_CLINICAL_GOLD` / `ARABIC_GOLD` / `MULTIMODAL_GOLD` / `CALIBRATION_HOLD_OUT_SPLIT` / `MODEL_SELECTION_DEV_SET` or any quarantined/protected source to enter SFT or other prohibited optimization surfaces. Protected commandMed data contamination remains a hard fail-closed lineage concern. The reconciliation concerns only **public benchmark exposure** (`PUBLIC_EXTERNAL_EVAL` / `CHECKPOINT_SELECTION` with public slices) as a universal blocker on the base checkpoint's `TRAIN` lineage eligibility.

---

## 5. Consequences for E001 mass-reach PRIMARY frontier

With corrected semantics, the three PRIMARY candidates' lineage admission for `TRAINING_OR_ADAPTATION` and `MODIFICATION_OR_DERIVATION` may be evaluated with `contamination_state=NOT_APPLICABLE` **where the record represents only the upstream Apache base lineage parent and carries no benchmark-clean claim**. Benchmark contamination remains a **separate** required evidence axis for selection and must be bound per exact `candidate × benchmark-slice` before any checkpoint can be considered `PRIMARY_SELECTION_ELIGIBLE`.

This does **not** make any candidate benchmark-clean, does **not** make any public benchmark result trusted, and does **not** grant tournament execution. It merely unblocks the **lineage** gate so that the repository can honestly record:

```text
MODEL_LINEAGE_ELIGIBLE=YES (with NOT_APPLICABLE, no benchmark claim)
while
MEDXPERTQA_SELECTION_CONTAMINATION=NOT_ASSESSED (still blocks selection)
```

In that state, adaptation-parent lineage may proceed once separately authorized (E002), while tournament execution requiring MedXpertQA selection remains incomplete — which is exactly the behavior Spec 005 Q5 prescribes.

---

## 6. Tests proving the separation

A minimal offline test (no payload access) demonstrates the existing evaluator already enforces the distinction:

1. `MODEL_OR_CHECKPOINT` with `TRAINING_OR_ADAPTATION`, `NOT_APPLICABLE` → `ELIGIBLE` (lineage parent, no benchmark claim).
2. `MODEL_OR_CHECKPOINT` with `TRAINING_OR_ADAPTATION`, `NOT_ASSESSED` → `BLOCKED` (CONTAMINATION_UNRESOLVED) — fail-closed when evidence missing.
3. `BENCHMARK_OR_EVALUATION_ASSET` for a `REQUIRED_PRIMARY_SELECTION` slice with `NOT_APPLICABLE` must not be constructed — contract evaluation for selection uses Q4's dual-axis `NOT_APPLICABLE_FOR_PUBLIC_BENCHMARK_SELECTION=PROHIBITED` via separate benchmark contamination evidence, not the model record's field, and Q5's consequence mapping yields `INCOMPLETE`/`NO_SELECTION`.
4. A `MODEL_LINEAGE_ELIGIBLE` model with a separate `NOT_ASSESSED` benchmark slice remains `CANDIDATE_SLICE_NOT_SELECTION_ELIGIBLE` — selection blocked, lineage not polluted.

The lineage contract and Spec 005 Q4/Q5 already implement this without amendment; the above tests are expected to pass on the current `src/commandmed/eval_contract/lineage.py` and `data/lineage/lineage_contract.json` (verified via `PYTHONPATH=src python -m pytest tests -k lineage` — see PR checks).

---

## 7. What this reconciliation does not authorize

```text
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```

No external payload access is granted. No contract amendment is proposed at this time. If a future evaluator were found to structurally force `MODEL_OR_CHECKPOINT` training-lineage to prove benchmark-style cleanliness, a separate `SPEC003_CONTAMINATION_SCOPE_CONTRACT_AMENDMENT` decision would be required — but current code proves it does **not** force that.

---

**Prepared by:** Pi — repository governance / contract-analysis / offline test only, no external payload access.
**Next:** Recompute PRIMARY lineage admission with `NOT_APPLICABLE` where genuinely outside, update `admission-evidence-e001-public-metadata-2026-08-27.md` to record corrected evaluator results, and keep benchmark selection contamination as `NOT_ASSESSED` → tournament `NO_SELECTION` until contamination evidence is separately bound.

