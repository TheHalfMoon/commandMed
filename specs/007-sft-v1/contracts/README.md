# Spec 007 Contract Registry

These schemas freeze the planning boundary for future offline validators. They do not authorize execution and do not imply that a concrete model, dataset, backend, device, or training recipe exists.

| Contract | Purpose | Concrete external evidence required before real use? |
|---|---|---|
| `curriculum-record.schema.json` | provenance-complete SFT example admission | real data authority/provenance |
| `base-checkpoint-binding.schema.json` | bind Founder+ChatGPT winner + tokenizer/license/lineage | authorized tournament + winner decision |
| `candidate-evidence-record.schema.json` | neutral candidate evidence; Pi recommendation forced NONE | model/tournament evidence |
| `prompt-rendering.schema.json` | exact semantic→prompt rendering identity | winner tokenizer/template |
| `loss-mask-policy.schema.json` | explicit supervised-token classes | concrete rendering/tokenizer |
| `packing-truncation-policy.schema.json` | safe sequence composition/truncation | backend compatibility |
| `training-config.schema.json` | versioned future recipe | winner/backend/numerics evidence |
| `dataset-snapshot.schema.json` | exact admitted record set and coverage | real approved curriculum |
| `capability-preservation.schema.json` | paired base-vs-SFT qualification binding | frozen evaluation evidence |
| `checkpoint-selection-policy.schema.json` | quarantine-safe pre-registered selection | future run policy |
| `abort-sentinel-policy.schema.json` | abort/disqualify-only safety monitoring | separately admissible sentinel source |
| `environment-manifest.schema.json` | pinned runtime/software/device identity | selected backend/device |
| `training-checkpoint-manifest.schema.json` | resumable checkpoint identity | authorized training run |
| `frozen-evaluation-protocol-binding.schema.json` | D-001 pre-run evaluation freeze | exact accepted eval identities |
| `non-executing-recipe-evidence.schema.json` | static evidence allowed before training | no execution-derived evidence allowed |
| `backend-candidate-evidence.schema.json` | backend compatibility evidence without selection | selected winner compatibility |
| `run-manifest.schema.json` | fail-closed future activation root | all access/finance/training gates |
| `record-class-definition.schema.json` | pre-register defensible record/SOTA comparison class | future comparison design |
| `resource-accounting.schema.json` | raw delivered-resource measurements | device/runtime execution |
| `efficiency-scorecard.schema.json` | raw + normalized medical/resource scorecard | qualified medical/resource evidence |
| `failure-taxonomy.schema.json` | classify future development failures without auto-training | admissible development evidence |

## Cross-contract invariants

1. Concrete `BaseCheckpointBinding` cannot exist before Founder+ChatGPT winner selection from authorized tournament evidence.
2. `RunManifest` validity is not execution authority.
3. Protected quarantine sources may not enter prohibited SFT optimization/selection surfaces.
4. `AbortSentinelPolicy` can never rank checkpoints or tune recipe/hyperparameters.
5. `NonExecutingRecipeEvidence` can never contain model execution, gradients, benchmark execution, loss/convergence or checkpoint comparison evidence.
6. `CandidateEvidenceRecord.pi_recommendation` is always `NONE`.
7. `RecordClassDefinition` must be pre-registered; record/SOTA claims cannot be invented after seeing results.
8. `EfficiencyScorecard` cannot turn a hard safety failure into a qualified record.
9. Real resource values are evidence, not synthetic planning defaults.
10. Every real input asset must satisfy the inherited Spec 003 identity contract before admission.

## Implementation discipline

Implementation may consolidate these contracts into fewer Python modules where sensible. One schema does not imply one runtime class/service/module. No plugin system, service, database, trainer abstraction, or new dependency is required merely because the contract exists.
