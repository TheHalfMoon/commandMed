# Tasks — Spec 007 SFT V1

**Current lifecycle:** `AUTHORIZED_TO_START`
**Implementation authority:** `AUTHORIZED_TO_START` — offline deterministic I001-I045 only
**Training authority:** NONE

Tasks are dependency ordered. `[x]` means the task has concrete evidence recorded here; `[ ]` means incomplete or still gated. Implementation work below is authorized only by the separate canonical Spec 007 implementation-authorization record; no checkbox expands model, data, execution, training, device, credential, or spend authority.

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

Authorized by the canonical Spec 007 implementation authorization record. Scope is I001-I045 offline deterministic implementation only. That implementation authorization does not extend into Phase E; E001-E003 are closed only by their separate Founder decisions, while E004-E015 remain separately gated or evidence-dependent.

- [x] **I001** Create minimal `src/commandmed/spec007` package only if existing modules cannot own the contracts. Depends on P016 + implementation authority. — `src/commandmed/spec007/__init__.py`, `src/commandmed/spec007/foundation.py`; exact-head GREEN `a3ff3ce90d47c8615dd0047f80c0eb3ce61cb373`.
- [x] **I002** Implement deterministic canonical serialization/identity utilities using repository precedent; no duplicate framework. Depends on I001. — Reuses `eval_contract.canonical` by identity; no second serializer; covered by `tests/spec007/test_foundation_canonical.py`.
- [x] **I003** Implement closed vocabularies and strict record parsing. Depends on I001-I002. — Frozen three-role vocabulary, duplicate-key-safe JSON object parsing, closed-object and SHA-256 validation in `foundation.py`.
- [x] **I004** Add synthetic fixtures proving undeclared/missing/invalid field rejection. Depends on I003. — RED run `33043673901` / job `98422681423` failed only because the package was absent; GREEN run `33043755992` / job `98422942429` compiled the new surface and passed 13 focused tests.

## Phase I1 — Curriculum / provenance / quarantine

- [x] **I005** Implement CurriculumRecord validator against full Spec 003 identity requirements, including mandatory cross-field rendering invariants declared by the contract registry. Depends on I003. — `src/commandmed/spec007/curriculum.py`; exact-head GREEN `fac65cefd4030730a5150df3a1e7d074448a8523`.
- [x] **I006** Implement knowledge-placement validation. Depends on I005. — Closed knowledge-placement vocabulary and fail-closed validation in `curriculum.py`.
- [x] **I007** Implement raw duplicate/near-duplicate report contract. Depends on I005. — Duplicate/contamination report validation in the I1 surface.
- [x] **I008** Implement purpose-aware canonical quarantine-matrix binding; never rely only on copied names. Depends on I005. — `src/commandmed/spec007/quarantine.py` reads and validates canonical `data/eval/quarantine.json` rather than copying policy names.
- [x] **I009** Add negative fixtures for every prohibited training/monitoring/recipe/checkpoint/model-selection purpose. Depends on I008. — Explicit prohibited-purpose fixtures in `tests/spec007/test_quarantine_snapshot.py`.
- [x] **I010** Implement DatasetSnapshot and CurriculumCoverageReport generation over synthetic fixtures, enforcing `record_count == len(record_ids)` and snapshot token-accounting cross-field invariants fail closed. Depends on I005-I009. — `src/commandmed/spec007/snapshot.py`; I1 GREEN run `33044322855` / job `98424696714`: 37 passed + 8 subtests.

## Phase I2 — Rendering / loss / sequence semantics

- [x] **I011** Implement PromptRenderingPolicy validator without model runtime. Depends on I003. — `src/commandmed/spec007/sequence.py`.
- [x] **I012** Implement LossMaskPolicy validator with all required token classes explicit. Depends on I011. — All eight contract token classes validated explicitly.
- [x] **I013** Implement PackingTruncationPolicy validator and fail-closed reason codes. Depends on I011. — Static packing/truncation validator only.
- [x] **I014** Add synthetic conformance fixtures proving required context cannot be silently truncated. Depends on I013. — Required-context negative fixtures in `tests/spec007/test_sequence_contracts.py`.
- [x] **I015** Add multi-turn/tool semantic fixture records without executing tools/models. Depends on I011-I014. — Static semantic fixtures only; I2 GREEN run `33044504501` / job `98425278204`: 48 passed + 8 subtests.

## Phase I3 — Arabic / behavior / safety preservation

- [x] **I016** Implement LanguageProfile validator for MSA, Saudi/Gulf, code-switch, transliteration, terminology-normalization identity and verification state. Depends on I005. — `src/commandmed/spec007/preservation.py`.
- [x] **I017** Implement future candidate tokenizer-evidence packet shape; measurements remain `NEEDS_EVIDENCE`. Depends on I016. — Evidence packet requires `execution_performed=false`, measurements `NEEDS_EVIDENCE`, recommendation `NONE`.
- [x] **I018** Implement CapabilityPreservationBinding validator. Depends on I003. — Exact required preservation slices enforced.
- [x] **I019** Implement AbortSentinelPolicy validator with only CONTINUE/ABORT/DISQUALIFY effects. Depends on I008,I018. — Closed allowed effects and frozen-before-run checks.
- [x] **I020** Prove sentinel cannot rank checkpoints, tune recipe, change hyperparameters or create preferred early stopping. Depends on I019. — Negative fixtures in `tests/spec007/test_preservation_contracts.py`; I3 GREEN run `33044740770` / job `98426007386`: 59 passed + 8 subtests.

## Phase I4 — Selection / reproducibility / resume

- [x] **I021** Implement CheckpointSelectionPolicy default fixed-pre-registered rule and structured source-purpose authorization validation for any separately authorized mode. Depends on I003,I008. — `src/commandmed/spec007/selection.py`.
- [x] **I022** Reject protected evaluation, LLM-judge, human-inspection and sentinel evidence as ranking inputs absent separately canonical source/purpose authority; require exact source-set equality with the structured authorization object. Depends on I008,I021. — Explicit four-source negative/authorized fixtures in `tests/spec007/test_selection_reproducibility.py`; final review follow-up also proves `ABORT_SENTINEL` and `PROTECTED_EVALUATION` remain structurally prohibited even when the underlying dev source is separately authorized.
- [x] **I023** Implement EnvironmentManifest validator. Depends on I003. — Closed environment identity and known-nondeterminism validation.
- [x] **I024** Implement TrainingCheckpointManifest validator and distinguish resumable checkpoint from export. Depends on I023. — Full optimizer/scheduler/RNG/data-position state required for resumable classification.
- [x] **I025** Implement FrozenEvaluationProtocolBinding with `frozen_before_training_authorization=true` and provenance-complete manifests for every metric input, replay fixture, threshold, stratification, sample-size or other consumed evaluation asset. Depends on I003,I008. — Asset identity/provenance/hash checks fail closed.
- [x] **I026** Implement NonExecutingRecipeEvidence validator rejecting any execution-derived evidence. Depends on I003. — I4 GREEN requalification `9499f623dd4f74c514458735ab0dd9d05ba060e2`; run `33047626288` / job `98435248283`: 83 passed + 8 subtests.

## Phase I5 — Intelligence-density / failure-development contracts

- [x] **I027** Implement RecordClassDefinition validator requiring pre-registration and hard-safety PASS. Depends on I003. — `src/commandmed/spec007/intelligence.py`.
- [x] **I028** Implement ResourceAccountingRecord shape with synthetic-only planning fixtures; no real device measurements. Depends on I027. — Validator accepts supplied raw records only; no measurement code exists.
- [x] **I029** Implement EfficiencyScorecard validator preserving raw values and disqualifying safety failure. Depends on I027-I028. — Safety FAIL => DISQUALIFIED; insufficient evidence cannot qualify.
- [x] **I030** Implement FailureTaxonomyRecord validator. Depends on I003. — Closed failure/remediation vocabularies and reason-code validation.
- [x] **I031** Enforce protected-final-evidence rule: protected failures cannot authorize training-data admission. Depends on I030,I008. — I5 GREEN run `33047827616` / job `98435898849`: 103 passed + 8 subtests.

## Phase I6 — Config / run activation composition

- [x] **I032** Implement TrainingConfigurationRecord validator; unresolved values remain typed `NEEDS_EVIDENCE`. Depends on I010,I011-I026. — `src/commandmed/spec007/activation.py`; planning mode rejects invented numeric/strategy resolution.
- [x] **I033** Implement BackendCandidateEvidence validator; evidence-only and no backend selection. Depends on I032. — Requires `non_executing_evidence_only=true`.
- [x] **I034** Implement CandidateEvidenceRecord with `pi_recommendation=NONE`. Depends on I003. — Candidate evidence cannot recommend a winner.
- [x] **I035** Implement BaseCheckpointBinding validator but leave concrete binding unavailable until Founder+ChatGPT winner decision. Depends on I034. — Structural validator only; fixtures are explicitly synthetic/not-a-winner.
- [x] **I036** Implement RunManifest validator. Depends on I010,I012,I013,I018,I021,I023,I025,I026,I032,I035. — Closed manifest, exact software identities, component-reference resolution, explicit authority IDs.
- [x] **I037** Implement composed non-executing activation preflight checking identity freshness, quarantine, evaluation, finance/access/training authority presence. Depends on I036. — Data-only decision with explicit fail-closed reason codes; review repairs additionally validate every directly resolved RunManifest component with its canonical validator before preflight can allow execution.
- [x] **I038** Prove activation never loads weights, executes models, benchmarks, devices or network. Depends on I037. — `activation.py` contains no loader/device/network/optimizer/training entry point; preflight always reports `model_loaded=false`, `device_opened=false`, `training_started=false`; I6 GREEN run `33048129036` / job `98436866639`: 124 passed + 8 subtests.

## Phase I7 — Offline verification and implementation qualification

- [x] **I039** Add focused tests for all Spec 007 validators using synthetic fixtures, including every `x-commandmed-cross-field-invariants` rule. Depends on I038. — `tests/spec007/` spans foundation, curriculum/quarantine/snapshot, sequence, preservation, selection/reproducibility, intelligence/failure, activation; final follow-up adds explicit review regression coverage in `tests/spec007/test_review_followup_regressions.py`.
- [x] **I040** Add negative tests for malformed identity, undeclared fields, protected sources, partial rendering bundles, rendered/supervised token-accounting violations, snapshot record-count mismatch, evaluation assets lacking complete provenance, checkpoint source-purpose mismatch, execution-derived evidence, stale/mismatched bindings and authority gaps. Depends on I039. — Explicit negative fixtures cover each listed class across `tests/spec007/`, including malformed/unhashable nested values requested in final review.
- [x] **I041** Run focused Spec 007 tests. Depends on I040. — Original exact implementation head `2888b0d9cf9de11e77574cfba1f40a55f380c988`: compileall PASS; 124 passed + 8 subtests, run `33048129036` / job `98436866639`. Final pre-ledger review head `b4b6c87fa55c1e66a5e4377a160172f3980d6d5c`: 158 passed + 8 subtests in run `33051293464` / job `98447180522`.
- [x] **I042** Run full offline repository regression, compileall and diff-check. Depends on I041. — Original head `2888b0d9cf9de11e77574cfba1f40a55f380c988`: run `33048270761` / job `98437313527`, 751 passed + 136 subtests. Final pre-ledger review head `b4b6c87fa55c1e66a5e4377a160172f3980d6d5c`: run `33051293464` / job `98447180522`, 785 passed + 136 subtests; 36 combined review regressions; compileall PASS; `git diff --check` PASS; bounded diff scope PASS.
- [x] **I043** Open bounded implementation PR with exact task/evidence mapping. Depends on I042. — PR #53 merged canonically from exact implementation head `5bbd2659bc0b86151b731fc240286203687c2a2b`; merge `469a56126ed63407a4a624218b06da106470741e` preserves the bounded Spec 007 path set.
- [x] **I044** Obtain exact-head independent implementation review; repair until no material blockers. Depends on I043. — Qodo raised 11 valid findings on the original implementation; RED `2e0f5cf485d9c5ca5f8b91c582d1087d50c20b60` / run-job `33049053415`/`98439810190`, repairs and GREEN `43936c1b3e13fad0d232015d1fe5a3547ed22b3a` / `33049539882`/`98441390167`, then Qodo 0 bugs / 0 rule violations. CodeRabbit independently found four remaining material/reliability issues; RED `4c5aa33235622a0eae8825942652d11bad5e36ad` / `33050087065`/`98443183736`, repairs and GREEN `c0bc78a6c094aee4ba66d619eafffc855d8ad625` / `33050446275`/`98444362630`; CodeRabbit confirmed the implementation fixes and requested only explicit regression coverage. Final coverage head `b4b6c87fa55c1e66a5e4377a160172f3980d6d5c` adds those tests and qualifies in `33051293464`/`98447180522` (36 review regressions, 158+8 focused, 785+136 full, compile/diff/scope PASS); Qodo re-reviewed that head with 0 bugs / 0 rule violations. CodeRabbit cannot produce another included review on this head at present (`0` included reviews remain; exact-head status reports manual review required for this OSS repository), so the canonical service-unavailable fallback is used transparently: substantive CodeRabbit review/fix confirmation on the unchanged implementation code at `c0bc78a6...`, exact-head Qodo review on the test-only `b4b6c87...` delta, all CodeRabbit material threads resolved, and exact-head deterministic qualification. No PASS is inferred from silence.
- [x] **I045** Merge offline control plane only after all implementation gates and separate merge authority/precedent are satisfied. Depends on I044. — Founder merge authorization was recorded on PR #53 before guarded merge; exact head `5bbd2659bc0b86151b731fc240286203687c2a2b` merged as `469a56126ed63407a4a624218b06da106470741e`, tree `f70278fd1acf96d4bfb938d14eedc78ac86c0cba`, with parents `19bdffc28f20e52575922852dd3a8de2b9d0d312` and `5bbd2659bc0b86151b731fc240286203687c2a2b`. Post-merge exact-main run/job `33051946611` / `98449362969`: 36 review regressions, 158 passed + 8 focused subtests, 785 passed + 136 full subtests, compileall/diff/scope PASS. See `implementation-reconciliation.md`. At that implementation-closure point E001-E015 remained unchecked; E001-E003 are subsequently closed by their separate canonical decision records, while E004-E015 remain gated/evidence-dependent.

## Phase E — Controlled external evidence / authority gates

These are not implementation tasks and must not be fabricated.

- [x] **E001** Founder+ChatGPT freeze candidate manifest after fresh model landscape research. — Exact manifest `e001-mass-reach-v1` / canonical SHA-256 `98d586500d12e7904bce199061c48d5ac50e9f66a372de034d9ecba4e2d3cc28` frozen by `e001-candidate-manifest-freeze-2026-08-27.md` after qualified evidence PR #55 merged as `1af0e05bf5e04eb3b75b39e170e4ec2b31d08cd5`. At E001 freeze time E002/E003 and all model/benchmark/device/training/spend authorities remained `NONE`; E002 is subsequently authorized only by `e002-model-access-authorization-2026-08-27.md`.
- [x] **E002** Authorize model/weight access required by tournament. — Founder authorization recorded by `e002-model-access-authorization-2026-08-27.md`: exact frozen PRIMARY+CONTROL public/ungated artifact access and non-executing downloads only. `MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY`; E003 was `NONE` at E002 closure and is subsequently authorized only by `e003-live-tournament-execution-authorization-2026-08-27.md`.
- [x] **E003** Authorize live tournament execution. — Founder authorization recorded by `e003-live-tournament-execution-authorization-2026-08-27.md`: exact frozen candidate/model execution plus only A15-bound public/ungated/provenance- and contamination-qualified tournament inputs under the frozen Spec 004/005/007 protocol. E004 execution remains fail-closed on the existing activation/preflight; E005 winner selection, conversion, training, Private Gold/PHI, credentials/gated assets, provider generation, and spend remain unauthorized.
- [ ] **E004** Produce tournament evidence pack under frozen protocol. `EXECUTION_REQUIRED`. — Still `BLOCKED_PREFLIGHT` and intentionally unchecked. Current global state is governed by `e004-registry-current-state-reconciliation-v18-2026-09-03.md`; the exact research-engineering component policy frontier remains V12. Founder successor execution Decision B remains canonical via PR #184 / merge `54c192248f09bf93730604e83947a135583ef162`. Founder public-data access Decision B remains canonical via PR #189 / merge `34c89dc710eeaeb1952d76f65c55e30b2eb9462a`. Founder Aya route Decision B is canonical via PR #192 / merge `169db96c8b7a013f3dda20ed5f8da400dce0019d`: `FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B`, with public `main` authorized only as a transport resolver after exact pin prechecks. The first post-decision verified-alias attempt passed all route prechecks and resolved to the canonical Xet hash `3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082`, but the current execution environment could not receive local payload bytes: `MATERIALIZATION_BLOCKER=AUTHORIZED_ROUTE_RESOLVED_BUT_LOCAL_BYTE_MATERIALIZATION_UNAVAILABLE`, `LOCAL_PAYLOAD_BYTES_RECEIVED=0`, `AYA_PAYLOAD_HASH_VERIFICATION_PERFORMED=NO`, `AYA_PAYLOAD_PARSED=NO`, `AYA_RECORD_LEVEL_SCREENING_PERFORMED=NO`, and `AYA_CANDIDATE_CONSTRUCTION_PERFORMED=NO`. The empty transient workspace was removed and no raw Aya payload remains. `DATA_ADMISSION_AUTHORITY=NONE`, `CONTAMINATION_ASSESSMENT_AUTHORITY=NONE`, `MODEL_CONVERSION_AUTHORITY=NONE`, `A15_ACTIVATION=ABSENT_NOT_AUTHORIZED`, `TRAINING_AUTHORITY=NONE`, and current authorized spend remains USD 0. No dependency-safe later execution unit is currently reachable. See `e004-registry-current-state-reconciliation-v18-2026-09-03.md` and `e004-aya-verified-alias-materialization-attempt-2026-09-03.md`.
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