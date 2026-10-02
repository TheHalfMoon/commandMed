# 8. Limitations

First, the assurance vector is not claimed to be exhaustive. Fairness, privacy, provenance, explanation fidelity and distributional transport may require separate axes or separate studies.

Second, intervention effects are task- and model-dependent. Even successful replication across two backbone families would not justify a universal claim about all foundation models or clinical domains.

Third, exact clinical-rule oracles cover only settings where deterministic rules are appropriate. They provide clean action references but cannot represent the full ambiguity of diagnosis, prognosis or treatment decisions.

Fourth, semantic transformations can be mislabeled. The protocol therefore requires independent validation and excludes transformations before model outputs are observed when their semantic status is uncertain.

Fifth, post-hoc and trained interventions operate at different system loci. Cross-level comparisons are useful operationally but should not be interpreted as isolated causal mechanism comparisons.

Sixth, zero-cost compute constraints may limit backbone scale. The paper prioritizes causal identification, matched controls and replication over a flagship parameter count; scaling claims are excluded unless separately demonstrated.

Finally, a negative result can be underpowered. Equivalence or modularity language is allowed only when prespecified margins and power justify it.
