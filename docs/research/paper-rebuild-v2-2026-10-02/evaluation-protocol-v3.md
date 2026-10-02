# Prospective evaluation protocol v3 — CommandMed Contract

Status: DRAFT FOR SCIENTIFIC FREEZE. No model execution is authorized.

## Primary question

Can a decision interface preserve its probability semantics under meaning-preserving transformations while changing appropriately under meaning-changing evidence interventions, after supervision, backbone, capacity and tuning budget are controlled?

## Primary factorial structure

- interface: restricted LM candidate logits vs fitted typed head vs CRDI;
- adaptation: frozen representation vs decision adaptation vs decision + language-maintenance adaptation;
- transformation: canonical vs E-family semantics-preserving variants;
- intervention: clean vs C-family evidence/answer-set changes;
- backbone: one small Qwen-family model plus one independently structured family if lawfully runnable.

The primary inference is not “which checkpoint wins.” It is the interaction among interface, semantics-preserving transformation, and evidence-changing intervention.
## Scorecards

A. **Decision quality:** NLL and Brier primary; accuracy and discrimination secondary.

B. **Contract equivariance:** CED primary; CAFR and per-transform distributions secondary.

C. **Semantic responsiveness:** SRF, RR and proper-score change under C-family interventions.

D. **Calibration transport:** CTG, reliability diagnostics, frozen-map performance by intervention stratum.

E. **Selective behavior:** risk-coverage/AURC and coverage at prespecified risk target.

F. **Capability retention:** medical knowledge, nonmedical retained competence, bounded free-form generation.

G. **Subgroups/language:** only where lawful sample sizes and validated labels support inference; Arabic is not automatically pooled with English.

H. **Systems:** latency, active/resident memory and installed bytes only on named hardware; no extrapolated energy claim.

No aggregate score may hide a noncompensable failure.
## Transformation validity

Every E-family transformation must have a machine-checkable mapping where possible and a documented semantic-validity procedure. Option permutation and opaque identifier substitution are mechanically valid. Natural-language rubric paraphrases are development-only until independently validated and frozen.

Every C-family intervention must specify what semantic fact changed and why the expected response should change. “Remove a sentence” is not automatically an evidence-removal label; the item may remain answerable from other evidence or prior knowledge.

## Mandatory baselines

Structured generation, restricted LM logits, same-representation linear/MLP heads, post-hoc temperature scaling, PriDe/permutation inference where applicable, permutation-aware training, a set/permutation-equivariant architecture control, and a decision-specialist control when lawful.

## Confirmatory discipline

Freeze transformation generator, inverse mappings, primary contrasts, metric code, calibration rule, tuning budget and selection rule before confirmatory access. Repeated access converts a set into development evidence.

Generated or transformed items that fail semantic validation are excluded before model outputs are inspected; exclusions after model inspection require a deviation record.