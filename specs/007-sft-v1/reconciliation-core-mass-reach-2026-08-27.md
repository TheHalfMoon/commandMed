# Core / Mass-Reach / Nano Reconciliation — 2026-08-27

**Spec:** 007 SFT V1 — E001 mass-reach reconciliation
**Date:** 2026-08-27
**Status:** ADDITIVE RECONCILIATION ARTIFACT — does not amend frozen Spec 005 gates; proposes editorial amendment to density strategy §4.1
**Authority:** `AUTHORIZED_TO_START` (I001-I045 complete). This artifact is evidence/documentation only — `TRAINING_AUTHORITY=NONE`, `BACKBONE_WINNER=NEEDS_EVIDENCE`
**Purpose:** Reconcile the canonical conflict between Spec 005 universal low-resource distribution priority and the newer Medical Intelligence Density strategy's approximate parameter bands before E001 manifest freeze.

---

## 1. Conflicting texts identified

**Text A — Canonical, frozen, taking precedence:**

`specs/005-base-model-tournament/spec.md` bounded clarification sessions (2026-08-23), incorporated by reference in Spec 007 plan §3 inherited contracts:

```text
UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY
QUALITY_FLOOR_THEN_SIZE_FIRST
SUB_700MB_MASS_REACH
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_HARD_CEILING=700_MiB
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_ENGINEERING_TARGET<=600_MiB
PEAK_WORKING_RAM_HARD_CAP=2_GiB (common 8K, all five targets)
LOW_RESOURCE_PHONE_CLASS=4_GB
COMMON_CONTEXT=8192 (7K prompt + 1K generation)
SUB4BIT_PRIMARY_CANONICAL_RELEASE=PROHIBITED
GGUF_LLAMA_CPP_CANONICAL
Q4_FLOOR_SMALLEST_PASSING
BASE_ONLY_PRIMARY
COMMON_CORE_PRIMARY_RANKING
FULLY_ADMITTED_PRIMARY_ONLY
```

Supported by:
- `specs/005-base-model-tournament/tasks.md` (frozen mass-reach five-target set: iPhone 17 Pro 12GB, iPhone 13 4GB, Galaxy A56 8GB, Galaxy A16 4GB, N100 8GB x86-64)
- `specs/005-base-model-tournament/ultra-compact-candidate-sweep.md` (Qwen3-0.6B Q8_0 639 MB / Q4 ~480 MB; Qwen3.5-0.8B Q4_0 563 MB — both satisfy SUB_700MB)
- `specs/005-base-model-tournament/admission-evidence.md` (Qwen3.5-0.8B as current ultra-compact primary lead, Apertus conditional due gated AUP, MedGemma multi-GB excluded from V1 mass-reach)
- `specs/007-sft-v1/plan.md` §3 inherited contracts (§4 authority boundary `MODEL_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY`)

**Text B — Additive hypothesis, not frozen gate:**

`docs/COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md` §4.1–4.2:

> Core: strongest compact general Health & Medical core that can plausibly live in the roughly 2–4B-class frontier or an equivalently small delivered-resource class.
> Nano: approximately 0.6–1.5B-class later hypothesis.

This document's own header states:

```text
Status: ADDITIVE PLANNING STRATEGY — does not amend execution authority
```

It is dated 2026-08-27, after Spec 005's frozen gates, and explicitly does not claim to override them.

---

## 2. Authority and chronology

- Spec 005 gates were frozen via bounded clarification sessions (sessions 2–5) ending at merge `5e35cd4` (implementation) and reconciliation `799c36a`, then Spec 006 closure, then Spec 007 specification `645da20`. Their resource envelope is canonical and was the basis for I001-I045 offline deterministic qualification.
- Density strategy was authored 2026-08-27 as an additive planning hypothesis to operationalize per-byte/joule/second measurement (record board, resource-normalized metrics). It was never merged as a Spec 005 amendment.
- Spec 007 `spec.md` explicitly states: `Spec 007 inherits without weakening` Spec 005 tournament/preconstruction/device control plane. Its lifecycle note carries Spec 005 precedence.

**Precedence rule (existing governance):** A bounded spec's frozen gates cannot be silently overridden by a planning strategy document. Strategy phrases are hypotheses; gates are hard requirements. Therefore Text A controls the current tournament's resource class.

---

## 3. Intended harmonized interpretation (Founder+ChatGPT strategic intent, 2026-08-27)

Founder + ChatGPT direct:

```text
CORE_DEFINITION = CAPABILITY_AND_SAFETY_CONTRACT_NOT_PARAMETER_BAND
```

Harmonization:

- **CORE** = the frozen capability/safety/product contract: the selected model must satisfy the full frozen Core quality, safety, Arabic, provenance, tool-use, abstention, and device/resource contract before it can be called commandMed Core. Parameter count does not itself determine Core vs Nano.
- **MASS_REACH_CORE** = the subset of Core candidates satisfying the current `SUB_700MB_MASS_REACH` / `2 GiB` contract under `GGUF_LLAMA_CPP_CANONICAL`. This is the *current tournament* contract. Solving Mass-Reach Core is the present product/engineering goal (universal low-resource distribution).
- **NANO** = a later explicitly scoped derived/distilled/compressed tier created **after** proven Mass-Reach Core capability exists (Spec 007 plan §11, density strategy §19). It is defined by a new explicit resource contract and capability-retention target, not merely by `0.6–1.5B` parameter count.

Approximate parameter bands in density strategy §4.1–4.2 (`2–4B Core`, `0.6–1.5B Nano`) are **research hypotheses for dense classes** under those names, not authority to override measured shipped bytes / peak RAM. A 350M model that satisfies the full Mass-Reach Core contract **is Core**; a 4B model that cannot satisfy `SUB_700MB` **is not Core for the current tournament** (it is a scale/quality control).

Scientific thesis of the mass-reach tournament is:

```text
QUALITY_FLOOR_THEN_SIZE_FIRST_WITH_EXPLICIT_SCALE_CONTROL
```

Question: *Can an ultra-compact, permissively releasable model (350M–0.8B) satisfy the frozen medical-quality, safety, Arabic, tool-use, abstention, and SUB_700MB/2 GiB device constraints?*

- If YES: choose among qualifying PRIMARY per frozen comparison policy.
- If NO: return `PRIMARY_RESULT=NO_SELECTION` — do not weaken gates. Only then `FOUNDER+CHATGPT_RESOURCE_CLASS_RECONSIDERATION_REQUIRED` (may open a 2–4B Core manifest v2).

---

## 4. Required document amendments

### 4.1 Spec 005

No amendment required. Its frozen gates (`SUB_700MB`, `2 GiB`, `GGUF_LLAMA_CPP_CANONICAL`, etc.) remain correct and are the basis for E001 Primary eligibility.

### 4.2 Density strategy `COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md` §4.1

**Required editorial amendment** (additive strategy, not gate):

Proposed replacement paragraph for §4.1 (retaining 2026-08-27 date, adding reconciliation footnote):

> Primary research target: the strongest compact general Health & Medical core that satisfies the **frozen Mass-Reach Core contract** (`SUB_700MB_MASS_REACH` with engineering targets, `2 GiB` common 8K peak, `8192` context under `Q8_0` symmetric KV, `B512_U128`, pinned llama.cpp). Approximate dense-class labels such as `2–4B` or `0.6–1.5B` are research hypotheses for the resource class, not overrides of measured shipped bytes or peak RAM. A mass-reach candidate such as 350M–0.8B that satisfies the full frozen contract is Core; a larger model that cannot satisfy that contract is a scale/quality control or fallback for a future resource-class manifest.

No Founder decision is needed to amend this additive strategy (it is not a locked gate). A separate editorial PR should apply the change and cross-reference this reconciliation artifact.

### 4.3 Spec 007 wording that inherited the 2–4B band

`specs/007-sft-v1/plan.md` §11 (Core vs Nano boundary) and `docs/COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md` §4.2 describe Nano as `0.6–1.5B`. These are consistent with the new interpretation (Nano after proven Core), but a future editorial should clarify Nano is defined by its **explicit future resource contract + retention target**, not by parameter count alone.

---

## 5. Consequences for E001 manifest

- **PRIMARY for mass-reach** is restricted to candidates whose **complete minimum text/core GGUF bundle** can plausibly satisfy `SUB_700MB_MASS_REACH` (and, under the frozen device condition, `2 GiB` peak). Per current admission evidence and this repair's fresh sweep:
  - `Qwen/Qwen3-0.6B-Base` — PRIMARY ultra-compact anchor
  - `Qwen/Qwen3.5-0.8B-Base` — PRIMARY ultra-compact challenger
  - `ibm-granite/granite-4.0-350m-base` — PRIMARY ultra-compact (IBM, 350M dense RoPE 32K, Q4_K_M 237 MB)
  These three jointly test ultra-compact + vendor diversity hypotheses. All exceed the `QUALITY_FLOOR_THEN_SIZE_FIRST` floor only if they later pass medical/safety/Arabic/device gates; size does not rescue a gate failure.

- **CONTROL (non-winner):**
  - `Qwen/Qwen3-4B-Base` — scale/quality control (≈2.4 GB Q4_K_M, will fail SUB_700MB by design). Purpose: measure opportunity cost of mass-reach.
  - Larger Apache candidates (Qwen3.5-2B-Base, Qwen3.5-4B-Base, Gemma-4 E2B/E4B, Ministral-3 3B) are **fallback controls** for a future `RESOURCE_CLASS_RECONSIDERATION` manifest v2 if all ultra-compact PRIMARY return `NO_SELECTION`.

- `Phi-4-mini-instruct` is **not BASE_ONLY_PRIMARY** (no base checkpoint exists) — retained as `REFERENCE_ONLY`.
- `BASE_ONLY_PRIMARY` and `COMMON_CORE_PRIMARY_RANKING` (modality secondary) remain fully enforced.

---

## 6. No new authority granted by this artifact

```text
TRAINING_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
BACKBONE_WINNER=NEEDS_EVIDENCE
PRIMARY_MANIFEST_FROZEN=NO
```

E001 remains `FOUNDER+CHATGPT_DECISION_REQUIRED`. This reconciliation merely records the conflict, the harmonized interpretation, and the minimal editorial change needed. It does not freeze the manifest and does not select a winner.

---

## 7. History preservation

No canonical file has been silently edited away. Spec 005's frozen text remains authoritative at its merges; density strategy's 2026-08-27 text remains readable at its commit. This reconciliation artifact is the traceable bridge between them. Any future editorial PR amending density strategy §4.1 must reference this artifact in its commit message.

---

**Prepared by:** Pi (documentation synthesis) — no model execution, no training, no gated access.
**Next:** Repair PR #55 research packet (already done at `research-E001-model-landscape-2026-08-27.md` v2) → obtain exact-head review → merge → await Founder+ChatGPT manifest freeze (E001) per roles above.

