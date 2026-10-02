# Scientific Freeze Candidate V5

Status: `PRE_FREEZE_CANDIDATE`; `CONFIRMATORY_FROZEN=NO`; `EXECUTION_AUTHORIZED=NO`.

This document narrows the V5 study before any model execution. It binds candidate identities and deterministic selection rules without pretending that unresolved power, rights, or implementation gates are complete.

## Backbone identities

Primary development family:
- `Qwen/Qwen3.5-0.8B-Base`
- revision `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`
- observed card license: Apache-2.0
- observed pipeline: `image-text-to-text`; V5 uses the text decision path only unless separately authorized.

Independent replication family:
- `HuggingFaceTB/SmolLM2-1.7B`
- revision `effd688a12921b4cc83e3312b6feb579f70f9c71`
- observed card license: Apache-2.0
- observed architecture: `LlamaForCausalLM`

These two families are selected because they are small enough for a zero-cost feasibility path and are not the same model architecture. No flagship 27B model is required for the methodological paper.
## Primary medical source family

`RULE_ORACLE` is the primary confirmatory substrate.

Source lineage:
- `ncbi-nlp/Clinical-Tool-Learning`
- repository revision `d474a95128e128623933c9be0d389ff7d82ef782`
- root license blob `8b18c9d4c47d23c56c4680381ed2e38c2025874a`
- RiskCalcs tools tree `aefb538408534212809ed2651309554c2bed596e`

The repository license identifies the software/database as a United States Government Work with no restriction placed on use or reproduction. This does not convert third-party papers or private clinical records into project-owned material.

Prospective source-item design:
- exactly 64 eligible deterministic calculators;
- exactly 16 generated source cases per calculator;
- total primary cluster count: `4096` source cases;
- 16 deterministic generated input states per calculator; numeric-threshold calculators must include boundary-adjacent and interior values, while Boolean-only calculators use balanced state combinations;
- calculator eligibility is decided without model outputs;
- after static eligibility screening, selection is deterministic by SHA-256 ordering of the stable calculator identifier plus the literal salt `CommandMed-V5`.

If 64 calculators cannot pass the frozen eligibility criteria, this design gate fails; the count is not silently reduced after seeing model behavior.
## External validation family

`RISKQA_EXTERNAL` is secondary validation, not the source of the primary oracle.

Bound artifacts:
- RiskQA dataset blob `2a2372ddd705efab4194f2ff7a3bf21c74dc1c7e`
- RiskQA README blob `ce5bd60a2f0a8ebee8c524bbb3d735c11e05c0e8`
- upstream paper reports `350` manually curated benchmark questions.

Private Yale ED notes and MIMIC patient-note experiments are explicitly excluded from CommandMed V5. No restricted patient record is required.

`OPEN_CLINICAL_REASONING` remains optional and unadmitted until a source with independently acceptable rights and contamination posture is bound. MedQA, MedMCQA, PubMedQA, ArabicMMLU, MedArabiQ, MedAraBench, MIMIC-derived cases, and image datasets remain outside the confirmatory freeze unless a later rights review changes their status before test access.

## Training and decoding seeds

For any learned intervention, the development protocol uses three fixed training seeds: `11`, `29`, and `47`. Confirmatory inference is deterministic wherever the model interface permits: raw probability/logit readout for decision endpoints and greedy decoding for structured-generation controls. Any unavoidable stochastic component must declare its seed and repeated-run rule before confirmatory access.

No model weight, dataset payload, inference call, training run, or benchmark execution is authorized by this document.
## Intervention identities

The confirmatory candidate set is frozen by specification ID before implementation SHA binding:
- `A1_TS_V1`: project-owned temperature scaling; calibration target only.
- `A2_SELBIAS_V1`: project-owned paper-spec reimplementation of selection-bias correction; no upstream code copy.
- `B1_TYPED_V1`: matched typed readout under matched supervision/capacity.
- `C1_CRDI_V1`: semantic-contract regularization on validated meaning-preserving transformations only.
- `C2_CRDI_RETAIN_V1`: `C1` plus prespecified capability-maintenance objective.
- `D1_DEFER_V1`: fixed act/defer policy operating on frozen scores.
- `D2_RULETOOL_V1`: deterministic clinical-rule routing using admitted public-domain calculator logic.

Required ordered interactions are `A1 -> A2`, `A2 -> A1`, `A1 -> C1`, and `C1 -> A1` when both orders are technically meaningful. The order gap is reported rather than hiding noncommutativity.

## Remaining blockers to a real scientific freeze

`CONFIRMATORY_FROZEN` remains `NO` until all of the following are exact: final 64-calculator admission audit; generator specification and hashes; implementation SHAs for every admitted intervention; property-specific meaningful margins; power calculation; final retention task rights; and final confirmatory source identities/quarantine procedure.

No blocker may be cleared by inspecting confirmatory model outputs.
## Static selector result

The committed non-executing selector `freeze_tools/select_riskcalcs_manifest.py` parsed the bound RiskCalcs source as data, used Python AST only, and did not call any calculator function. It found `1993` coarse static candidates. A stricter second-stage AST audit reduced these to `734` numeric/Boolean threshold-rule candidates with at least 16 prospective input states, then deterministically selected `64` into `riskcalcs-rule-oracle-final-candidate-v5.json`.

This is a **candidate manifest**, not final clinical admission. Each selected calculator still requires a static domain/interpretation audit before its generator can enter confirmation. A failed audit may only be handled by the same prespecified deterministic next-candidate rule; model outputs cannot influence replacement.