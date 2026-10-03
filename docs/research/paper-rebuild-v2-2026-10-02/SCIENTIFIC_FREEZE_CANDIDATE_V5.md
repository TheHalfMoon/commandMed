# Scientific Freeze Candidate V5

Status: `PRE_FREEZE_CANDIDATE`; `CONFIRMATORY_FROZEN=NO`; `V5_DEVELOPMENT_EXECUTION_AUTHORIZED=YES`; confirmatory/reserve execution remains unauthorized.

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
- exactly 64 selected deterministic rule calculators;
- each selected calculator exposes at least `1024` deterministic candidate states; no fixed confirmatory pool is materialized before the implementation freeze;
- per calculator, `64` development and `64` calibration states are fixed before model work;
- after a clean implementation freeze and future public-randomness event, `64` confirmatory and `64` reserve states are selected from state indices not used by development/calibration;
- planned primary confirmatory cluster count remains `4096` (`64 calculators x 64 confirmatory cases`);
- every eligible calculator must expose at least `1024` prospective Boolean/numeric-threshold states;
- calculator eligibility and domain selection are decided without model outputs;
- selection is deterministic availability-constrained stratum round-robin across alphabetically ordered first-listed source specialty strata; within each specialty candidates are ordered by the frozen SHA-256 selection key and PMID;
- the design targets domain breadth and must not be interpreted as an estimate of clinical prevalence.

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
- `B1_TYPED_V1`: matched typed readout under matched supervision/capacity; pure linear typed-readout mechanics are implemented, but no learned model integration is authorized.
- `C1_CRDI_V1`: semantic-contract regularization on validated meaning-preserving transformations only; the pure objective is implemented, but no optimization is authorized.
- `C2_CRDI_RETAIN_V1`: `C1` plus a prespecified capability-maintenance anchor; the pure objective is implemented, but no optimization is authorized.
- `D1_DEFER_V1`: fixed act/defer policy operating on frozen scores.
- `D2_RULETOOL_V1`: deterministic rule-tool routing using identity-bound public-domain calculator logic; the endpoint is rule conformance, not clinical validity unless separately qualified.

Required ordered interactions are `A1 -> A2`, `A2 -> A1`, `A1 -> C1`, and `C1 -> A1` when both orders are technically meaningful. The order gap is reported rather than hiding noncommutativity.

## Remaining blockers to a real scientific freeze

`CONFIRMATORY_FROZEN` remains `NO` until all of the following are exact: model-integration/training qualification for B1/C1/C2; final generator and implementation hashes; property-specific meaningful margins; power calculation; and final confirmatory identity materialization after the clean implementation-freeze event plus the future public-randomness pulse. The source/provenance audit is sufficient for the declared rule-conformance construct; qualified clinical review is required only for any current-care clinical-validity interpretation and is not used to clear the methodological endpoint. The retention-task identity/rights and quarantine procedure are now bound, but no confirmatory membership has been materialized.

No blocker may be cleared by inspecting confirmatory model outputs.
## Static selector result

The committed non-executing selector parsed the bound RiskCalcs source as data, used Python AST only, and did not call any calculator function. The hardened V5 audit now admits `82` numeric/Boolean threshold-rule candidates with at least `1024` prospective input states across `15` first-listed source specialty strata. It selects `64` by deterministic specialty round-robin. For each selected calculator, only `64` development and `64` calibration cases are preselected; confirmatory/reserve states are not selected until the post-freeze future-randomness event.

All 64 selected PMIDs resolve in PubMed and none carries a retraction/withdrawal publication-type flag in the current source audit. This remains a **source/provenance audit, not final clinical qualification**. Rule conformance can be measured mechanically; any claim that a rule is clinically appropriate for current care requires separate qualified review. Replacement remains deterministic and cannot use model outputs.

## Founder-authorized S1 development transition — 2026-10-03

The bounded V5 development authority is now paired with `V5_S1_DEVELOPMENT_EXECUTION_PROTOCOL_2026-10-03.md`, frozen before any model output. The protocol fixes the S1 medical task construction, development/calibration subpartitions, B1 linear-readout budget, C1/C2 final-block rank-4 LoRA budget, seeds `11/29/47`, C2 SQuAD maintenance/evaluation separation, sequence policy, and resource stop rules.

The identity-bound RuleCalcs builder is implemented and unit-tested. It binds the exact RiskCalcs source SHA-256 and selected calculator code hashes, admits only the frozen safe AST shape, and cannot select confirmatory/reserve identities. Real 64-calculator source binding passed `64/64` before runtime qualification; executable materialization remains pending the separately pinned NumPy/PyTorch/Transformers runtime.

`CONFIRMATORY_FROZEN` remains `NO`. No development result may clear the later clean-freeze/future-randomness requirement for confirmatory/reserve identities.
