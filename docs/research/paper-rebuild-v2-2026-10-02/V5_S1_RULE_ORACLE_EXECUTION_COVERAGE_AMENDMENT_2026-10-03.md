# V5 S1 rule-oracle execution-coverage amendment — 2026-10-03

**Status:** `PROSPECTIVE_REPAIR_AFTER_PRE_MODEL_ORACLE_FAILURE`
**Applies to:** V5 S1 development/calibration rule-oracle preparation only
**Model load observed before this amendment:** `NO`
**Model inference observed before this amendment:** `NO`
**Training observed before this amendment:** `NO`
**Confirmatory/reserve materialization:** `NO`

## Trigger

The first deterministic S1 task-preparation attempt failed before any model load or model output. PMID `24103667` (`The SAH Score`) raised `UnboundLocalError` while executing a committed development/calibration state. The static numeric/Boolean eligibility gate had admitted the calculator because its source function and threshold syntax passed the frozen AST rules, but the threshold-expanded candidate-state generator could produce an out-of-domain value for which the calculator source leaves an internal score variable undefined.

This is a rule-oracle execution-domain failure. It is not model evidence and it is not a reason to weaken or bypass the oracle.

## Repair principle

The final 64-calculator set must be selected only from candidates that are mechanically executable on every already-defined pre-freeze development and calibration state under the unchanged case generator and quarantine mechanics.

For every candidate that passes the existing static numeric/Boolean eligibility gate:

1. bind the exact public RiskCalcs source bytes and exact function SHA-256;
2. derive the unchanged 64 development and 64 calibration state indices using `prefreeze_state_partition`;
3. materialize those 128 states with the unchanged `case_generator`;
4. execute the exact bound calculator function on every state using the fail-closed safe runtime;
5. require every output to be finite/serializable under the S1 rule-output contract and mechanically perturbable for the frozen MATCH/MISMATCH task;
6. reject the candidate on the first exception or unsupported output and record the rejection without repair, coercion, source editing, or case deletion.

Only execution-qualified candidates enter the unchanged deterministic availability-constrained specialty round-robin selection. Within each specialty stratum, the existing SHA-256 selection key and PMID order remain unchanged. The selected count remains exactly 64; if fewer than 64 execution-qualified candidates exist, the S1 rule-oracle gate fails rather than reducing the study.

## Scientific boundary

This amendment is stricter than the original static gate. It does not use model outputs, clinical outcome labels, confirmatory identities, reserve identities, or performance to select calculators. It does not modify calculator code or clamp generated inputs after failure. It only requires that the declared deterministic oracle be total over the already-defined development/calibration support used to qualify the implementation.

Execution qualification is not clinical validation. Passing this gate establishes only that the exact source implementation produces a supported deterministic output over the bounded pre-freeze development/calibration states.

## Required evidence

The regenerated rule-oracle manifest must record:

- the count of static numeric/Boolean candidates;
- the count of execution-qualified candidates;
- the count and identity of execution-rejected candidates;
- a deterministic rejection-reason digest;
- the selected 64 identities and specialty-stratum counts;
- source, selector, case-generator, quarantine, and execution-gate identities.

The first failed preparation attempt must remain preserved as negative development evidence. Any downstream case-index, quarantine commitment, clinical-source audit, scientific-freeze binding, and verification record whose identity depends on the selected 64 calculators must be regenerated and re-qualified.

No model load is permitted until the repaired selection and all dependent pre-model bindings are canonical and S1 task preparation passes under the frozen 768-token/no-truncation interface.
