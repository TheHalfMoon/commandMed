# Third-Party Notices

This file tracks third-party software that is actually incorporated into commandMed and therefore requires retained attribution, license text, NOTICE content, or other redistribution obligations.

## Current canonical incorporation state

At the time this file was introduced:

```text
CANONICAL_TENCENT_DONOR_CODE_IMPORTED=NO
CANONICAL_TENCENT_DONOR_DEPENDENCY_IMPORTED=NO
CANONICAL_TENCENT_DONOR_DATASET_IMPORTED=NO
```

The following repositories are qualified research/reference sources but are **not** listed as incorporated components merely because commandMed studies them:

- `Tencent/AI-Infra-Guard@e4e622af3ad2b8228ce82dd62b01415dd8ce2b9c` — Apache-2.0;
- `Tencent/AICGSecEval@94428ebf45141bf4ecd365a51d596dcd51caa690` — Apache-2.0;
- `Tencent/hpc-ops@2a2e26562433a8ba4b504858f1c938eb7612c901` — MIT, with third-party BSD-3-Clause components including CUTLASS in the upstream distribution.

## Admission rule

Before copied, adapted, or vendored third-party source becomes canonical, its source-admission record must bind at least:

```text
adoption_record_id
donor_repository
donor_revision
donor_path
donor_blob_sha
upstream_license_id
upstream_license_file_identity
upstream_notice_state
third_party_component_state
permission_basis
adoption_mode
commandmed_destination_path
security_review_state
test_evidence_state
attribution_state
modification_notice_state
```

See `docs/governance/external-code-adoption.md`.

When an admitted component carries attribution or NOTICE obligations, this file and/or the root `NOTICE` file must be updated in the same bounded adoption change. License obligations are never inferred away by commandMed's Apache-2.0 root license.
