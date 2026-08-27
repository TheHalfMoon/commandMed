# Tasks — Spec 007 SFT V1

**Current lifecycle:** `AUTHORIZED_TO_START`
**Implementation authority:** `AUTHORIZED_TO_START` — offline deterministic I001-I045 only
**Training authority:** NONE

Tasks are dependency ordered. `[x]` means the planning artifact exists in this branch; `[ ]` means future work. Implementation tasks MUST NOT begin until a separate canonical implementation authorization exists.

## Phase P — Planning package

- [x] **P001** Bind planning package to PR #50 / canonical main `981987390...`.
- [x] **P002** Preserve Founder+ChatGPT-only model-selection authority.
- [x] **P003** Add medical-intelligence-density additive strategy without rewriting the frozen Grand Master Plan.
- [x] **P004** Recover and strengthen SFT V1 training-grade plan from parked PR #48 on fresh canonical main.
- [x] **P005** Define Core-vs-Nano boundary and downstream research handoffs.
- [x] **P006** Define strict data model for curriculum, rendering, masking, dataset, config, selection, environment, resume and run activation.
- [x] **P007** Define record-class, resource-accounting, efficiency-scorecard and failure-taxonomy records.
- [x] **P008** Author strict JSON schema contracts for planned records.
- [x] **P009** Author non-executing quickstart and authority stop boundaries.
- [x] **P010** Author requirements checklist.
- [x] **P011** Author dependency-ordered implementation/evidence tasks.
- [x] **P012** Author static planning analysis.
- [x] **P013** Run repository baseline checks on exact planning head and record actual results. — Subject `701c933acdf84572f627446e5199231236f97988` / tree `faa5c15c84dbd84d162b6ba6850bbc312584203b`; run `33040059680`, job `98411371329` explicitly checked out and verified that subject (carrier `65973326632d07bb63cab03d9ab696b5f1f0c375` is trigger-only); compileall PASS; 627 tests + 128 subtests PASS; diff-check PASS.
- [x] **P014** Obtain fresh exact-head independent review of complete planning package. — Qodo and CodeRabbit both `MATERIAL_BLOCKER=NO` on `701c933acdf84572f627446e5199231236f97988`.
- [x] **P015** Repair every valid material finding and re-run checks/review. — All material review threads resolved before final qualification.
- [x] **P016** Merge qualified planning package canonically without expanding authority. — PR #51 merge `947f3aba4d4316e21470ac26352d96e3bfb74ae6`.
- [x] **P017** Close parked carrier PR #48 as superseded after canonical recovery is proven. — Closed without merge on 2026-08-27.

## Phase I0 — Future offline implementation foundation

Authorized by the canonical Spec 007 implementation authorization record. Scope is I001-I045 offline deterministic implementation only; E001-E015 remain separately blocked.

- [x] **I001** Create minimal `src/commandmed/spec007` package only if existing modules cannot own the contracts. Depends on P016 + implementation authority. — `src/commandmed/spec007/__init__.py`, `src/commandmed/spec007/foundation.py`; exact-head GREEN `a3ff3ce90d47c8615dd0047f80c0eb3ce61cb373`.
- [x] **I002** Implement deterministic canonical serialization/identity utilities using repository precedent; no duplicate framework. Depends on I001. — Reuses `eval_contract.canonical` by identity; no second serializer; covered by `tests/spec007/test_foundation_canonical.py`.
- [x] **I003** Implement closed vocabularies and strict record parsing. Depends on I001-I002. — Frozen three-role vocabulary, duplicate-key-safe JSON object parsing, closed-object and SHA-256 validation in `foundation.py`.
- [x] **I004** Add synthetic fixtures proving undeclared/missing/invalid field rejection. Depends on I003. — RED run `33043673901` / job `98422681423` failed only because the package was absent; GREEN run `33043755992` / job `98422942429` compiled the new surface and passed 13 focused tests.

## Phase I1 — Curriculum / provenance / quarantine

- [ ] **I005** Implement CurriculumRecord validator against full Spec 003 identity requirements, including mandatory cross-field rendering invariants declared by the contract registry. Depends on I003.
- [ ] **I006** Implement knowledge-placement validation. Depends on I005.
- [ ] **I007** Implement raw duplicate/near-duplicate report contract. Depends on I005.
- [ ] **I008** Implement purpose-aware canonical quarantine-matrix binding; never rely only on copied names. Depends on I005.
- [ ] **I009** Add negative fixtures for every prohibited training/monitoring/recipe/checkpoint/model-selection purpose. Depends on I008.
- [ ] **I010** Implement DatasetSnapshot and CurriculumCoverageReport generation over synthetic fixtures, enforcing `record_count == len(record_ids)` and snapshot token-accounting cross-field invariants fail closed. Depends on I005-I009.

## Phase I2 — Rendering / loss / sequence semantics

- [ ] **I011** Implement PromptRenderingPolicy validator without model runtime. Depends on I003.
- [ ] **I012** Implement LossMaskPolicy validator with all required token classes explicit. Depends on I011.
- [ ] **I013** Implement PackingTruncationPolicy validator and fail-closed reason codes. Depends on I011.
- [ ] **I014** Add synthetic conformance fixtures proving required context cannot be silently truncated. Depends on I013.
- [ ] **I015** Add multi-turn/tool semantic fixture records without executing tools/models. Depends on I011-I014.

## Phase I3 — Arabic / behavior / safety preservation

- [ ] **I016** Implement LanguageProfile validator for MSA, Saudi/Gulf, code-switch, transliteration, terminology-normalization identity and verification state. Depends on I005.
- [ ] **I017** Implement future candidate tokenizer-evidence packet shape; measurements remain `NEEDS_EVIDENCE`. Depends on I016.
- [ ] **I018** Implement CapabilityPreservationBinding validator. Depends on I003.
- [ ] **I019** Implement AbortSentinelPolicy validator with only CONTINUE/ABORT/DISQUALIFY effects. Depends on I008,I018.
- [ ] **I020** Prove sentinel cannot rank checkpoints, tune recipe, change hyperparameters or create preferred early stopping. Depends on I019.

## Phase I4 — Selection / reproducibility / resume

- [ ] **I021** Implement CheckpointSelectionPolicy default fixed-pre-registered rule and structured source-purpose authorization validation for any separately authorized mode. Depends on I003,I008.
- [ ] **I022** Reject protected evaluation, LLM-judge, human-inspection and sentinel evidence as ranking inputs absent separately canonical source/purpose authority; require exact source-set equality with the structured authorization object. Depends on I008,I021.
- [ ] **I023** Implement EnvironmentManifest validator. Depends on I003.
- [ ] **I024** Implement TrainingCheckpointManifest validator and distinguish resumable checkpoint from export. Depends on I023.
- [ ] **I025** Implement FrozenEvaluationProtocolBinding with `frozen_before_training_authorization=true` and provenance-complete manifests for every metric input, replay fixture, threshold, stratification, sample-size or other consumed evaluation asset. Depends on I003,I008.
- [ ] **I026** Implement NonExecutingRecipeEvidence validator rejecting any execution-derived evidence. Depends on I003.

## Phase I5 — Intelligence-density / failure-development contracts

- [ ] **I027** Implement RecordClassDefinition validator requiring pre-registration and hard-safety PASS. Depends on I003.
- [ ] **I028** Implement ResourceAccountingRecord shape with synthetic-only planning fixtures; no real device measurements. Depends on I027.
- [ ] **I029** Implement EfficiencyScorecard validator preserving raw values and disqualifying safety failure. Depends on I027-I028.
- [ ] **I030** Implement FailureTaxonomyRecord validator. Depends on I003.
- [ ] **I031** Enforce protected-final-evidence rule: protected failures cannot authorize training-data admission. Depends on I030,I008.

## Phase I6 — Config / run activation composition

- [ ] **I032** Implement TrainingConfigurationRecord validator; unresolved values remain typed `NEEDS_EVIDENCE`. Depends on I010,I011-I026.
- [ ] **I033** Implement BackendCandidateEvidence validator; evidence-only and no backend selection. Depends on I032.
- [ ] **I034** Implement CandidateEvidenceRecord with `pi_recommendation=NONE`. Depends on I003.
- [ ] **I035** Implement BaseCheckpointBinding validator but leave concrete binding unavailable until Founder+ChatGPT winner decision. Depends on I034.
- [ ] **I036** Implement RunManifest validator. Depends on I010,I012,I013,I018,I021,I023,I025,I026,I032,I035.
- [ ] **I037** Implement composed non-executing activation preflight checking identity freshness, quarantine, evaluation, finance/access/training authority presence. Depends on I036.
- [ ] **I038** Prove activation never loads weights, executes models, benchmarks, devices or network. Depends on I037.

## Phase I7 — Offline verification and implementation qualification

- [ ] **I039** Add focused tests for all Spec 007 validators using synthetic fixtures, including every `x-commandmed-cross-field-invariants` rule. Depends on I038.
- [ ] **I040** Add negative tests for malformed identity, undeclared fields, protected sources, partial rendering bundles, rendered/supervised token-accounting violations, snapshot record-count mismatch, evaluation assets lacking complete provenance, checkpoint source-purpose mismatch, execution-derived evidence, stale/mismatched bindings and authority gaps. Depends on I039.
- [ ] **I041** Run focused Spec 007 tests. Depends on I040.
- [ ] **I042** Run full offline repository regression, compileall and diff-check. Depends on I041.
- [ ] **I043** Open bounded implementation PR with exact task/evidence mapping. Depends on I042.
- [ ] **I044** Obtain exact-head independent implementation review; repair until no material blockers. Depends on I043.
- [ ] **I045** Merge offline control plane only after all implementation gates and separate merge authority/precedent are satisfied. Depends on I044.

## Phase E — Controlled external evidence / authority gates

These are not implementation tasks and must not be fabricated.

- [ ] **E001** Founder+ChatGPT freeze candidate manifest after fresh model landscape research. `FOUNDER+CHATGPT_DECISION_REQUIRED`.
- [ ] **E002** Authorize model/weight access required by tournament. `SEPARATE_AUTHORIZATION_REQUIRED`.
- [ ] **E003** Authorize live tournament execution. `SEPARATE_AUTHORIZATION_REQUIRED`.
- [ ] **E004** Produce tournament evidence pack under frozen protocol. `EXECUTION_REQUIRED`.
- [ ] **E005** Founder+ChatGPT choose backbone winner and bind decision. `FOUNDER+CHATGPT_DECISION_REQUIRED`.
- [ ] **E006** Bind concrete tokenizer/template/checkpoint identities. Depends on E005.
- [ ] **E007** Resolve backend/update strategy from permitted evidence. No unauthorized pilot. Depends on E005-E006.
- [ ] **E008** Construct/admit real curriculum only under data/provenance authority. `DATA_AUTHORITY_REQUIRED`.
- [ ] **E009** Freeze concrete DatasetSnapshot and training numerics. Depends on E007-E008.
- [ ] **E010** Bind frozen evaluation protocol, access, device, finance and activation evidence. Depends on E005-E009.
- [ ] **E011** Founder grants explicit training authority for an exact RunManifest. `FOUNDER_AUTHORIZATION_REQUIRED`.
- [ ] **E012** Execute first SFT run only after E011. `TRAINING_EXECUTION`.
- [ ] **E013** Resolve checkpoint using the pre-registered quarantine-safe policy. Depends on E012.
- [ ] **E014** Run full frozen qualification and capability-preservation evaluation. Depends on E013.
- [ ] **E015** Accept/reject/narrow SFT V1 candidate without recycling protected results into the same optimization cycle. Depends on E014.

## Downstream handoff gates

- [ ] **D008** Spec 008: CPT-vs-no-CPT + data-efficiency ablation after Spec 007 evidence.
- [ ] **D009** Spec 009: failure-conditioned/on-policy distillation after Spec 008 decision.
- [ ] **D010** Spec 010: verifiable RL + reasoning efficiency after Spec 009.
- [ ] **D011** Spec 011: calibration/selective risk.
- [ ] **D012** Spec 012: real-device compression/QAD experiments.
- [ ] **D013** Spec 013: Arabic deepening.
- [ ] **D015** Spec 015: human evaluation.
- [ ] **D017** Spec 017: independent record/claim/HF/paper audit.

No downstream checkbox grants its own authority.
