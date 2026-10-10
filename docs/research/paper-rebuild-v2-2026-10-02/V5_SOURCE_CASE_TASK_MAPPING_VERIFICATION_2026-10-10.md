# V5 S1 development source-case to task-ID mapping verification — 2026-10-10

Status: `SOURCE_BOUND_MODEL_FREE_DEVELOPMENT_VERIFIED; POWER_GATE_NOT_QUALIFIED`.

## Motivation and observed contract

The frozen V5 statistics protocol requires the **source medical case** to be the inferential cluster, never the canonical/transformed prompt count. The development paired SD inventory currently indexes by `task_id`; without checking the original generator, a `task_id` could potentially be a prompt-derived identifier and introduce pseudoreplication.

A **full** model-free replay of the prospectively frozen rule-oracle source generator confirms that for this *specific synthetic, static-risk-calculator* S1 development/calibration allocation, each intrinsic `case_id` corresponds to **exactly one** `task_id`, and each task generates **exactly two** ordered prompt variants. There are 64 bound public RiskCalcs calculators, 8,192 distinct original source cases and 16,384 rows; no case ID, task ID or calculator-state tuple is reused. The split counts are 256 TRAIN, 3,840 DEV_EVAL, 256 CAL_TUNE, 3,840 CAL_EVAL; each calculator contributes 4/60/4/60 source cases in that order. The 7,680 source cases across DEV_EVAL and CAL_EVAL therefore qualify as distinct *source-case* development units, not 15,360 independent prompts.

The read-only `scripts/v5_s1_source_case_pairing_audit.py` rebuilds the original tasks from the **public, commit-pinned** RiskCalcs JSON source, the frozen 64-rule selected manifest, the byte-pinned original case generator and task renderer, and the frozen original task-preparation sequence. It replays **every original task, target, calculator ID, split, option semantics and both prompt hashes** against the 16,384-row R1 matrix and separately against all 16,384 rows of R2, with strict metadata types and distinct repeat labels. The verifier checks exact original R1 and R2 matrix bytes and rejects false one-to-one mappings, changed source state assignments, reused cases and altered prompt identities.

## Auditable identity and command

Source: `ncbi-nlp/Clinical-Tool-Learning@d474a95128e128623933c9be0d389ff7d82ef782`, `riskqa_evaluation/tools/riskcalcs.json`, SHA-256 `00a7a0089afffb66f2f32903bad94a5a2ea842841defb2d78e0686b0a5eb9ab9`.

```sh
python3 scripts/v5_s1_source_case_pairing_audit.py \
  --riskcalcs-source /path/to/exact-public-riskcalcs.json
PYTHONPATH=src python3 -m pytest -q tests/reliability_v5/test_source_case_pairing_audit.py
```

The output contains the exact frozen ordered task sequence SHA `36c86610e2a762cb57ab61a8dff6a829e7196a638178dc612b5d1d3d5bdd5e0c` and a freshly derived case-to-task mapping SHA-256 `43ce4be40bb5c1749dbbe21f6d8788dfd5c33bf72cea78936ec47011e72cf700`. It does not persist cases, prompt text or source medical inputs. Both source/output matrices, generator and selected manifest are SHA-bound in the script.

The existing minimal-permission GitHub Actions V5 provenance workflow now also retrieves **only this pinned public blob** using HTTPS and SHA-256-verifies the download before replaying both full response matrices, without using credentials, GPU or any model. The frozen public-rule evaluator requires `numpy` for its verified `np.exp` calculator; the CI runner explicitly installs `numpy==2.4.6` and `pytest==8.4.2` before running this check. This is deterministic integrity verification, not a new scientific model execution.

## Interpretation boundary

This audit establishes a **one-to-one structural identity mapping only for the prospectively fixed S1 synthetic rule-oracle development population**. It does not prove that the 64 calculators are clinically current/valid, that cases constitute independent real patient samples, that two model variants are independent, or that cross-calculator case distributions generalize to medical practice.

More importantly, it does **not** close the final power gate. The 72 descriptive paired SD values are within-training-seed development observations; a qualified multi-seed conservative variance procedure, the exact prospective hard-gate non-target hypothesis family, a validated missingness policy, and required additional effect margins still remain. The planned 4,096 confirmatory case count has **not** been shown to meet 90% power. No confirmatory or reserve identity is generated, no clinical validity is asserted, and all publication/merging/review/signature gates stay open.
