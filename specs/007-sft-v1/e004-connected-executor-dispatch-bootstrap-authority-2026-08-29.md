# E004 Connected-Executor Dispatch Bootstrap Authority — 2026-08-29

**Spec:** 007 SFT V1  
**Authority class:** bounded execution-blocker remediation  
**Authority effect:** authorizes exactly one transient native GitHub Actions dispatch bootstrap plus one transient SHA-named Git branch used only to reduce and detect ref-resolution races; does not authorize model conversion, contamination assessment, A15 activation, training, or downstream execution  
**Current authorized spend:** USD 0

## Founder directive capture

The connected executor had already reached a genuine tooling blocker: the exact canonical runtime-evidence workflow was live and authorized for one fresh `workflow_dispatch`, but the connected GitHub tool catalog exposed no action that could create that event.

The Founder then issued the following direct instruction in the active commandMed continuation session:

```text
FOUNDER_DIRECTIVE=fix that then go ahead do not stop until finish the project , you have all approvals fro me
FOUNDER_DIRECTIVE_SHA256=c2d68af8a8b029dee2f1f8b6c7d93a4e1f5cdd2fd8dd2301d4625989e8e16684
FOUNDER_DIRECTIVE_SESSION_LOCAL_TIME=2026-08-29T16:08+03:00
```

This record interprets `fix that` narrowly as authorization to remove the already-described connected-executor fresh-dispatch blocker while preserving every scientific, execution, spend, and downstream boundary that is not necessary to remove that blocker.

## Bounded remediation decision

```text
E004_CONNECTED_EXECUTOR_BLOCKER_REMEDIATION_AUTHORITY=AUTHORIZED_BOUNDED
REMEDIATION_MECHANISM=ONE_SHOT_NATIVE_GITHUB_ACTIONS_DISPATCH_BOOTSTRAP
BOOTSTRAP_PATH=.github/workflows/e004-runtime-evidence-dispatch-bootstrap.yml
BOOTSTRAP_TRIGGER=push_to_main_path_scoped_to_bootstrap_file
BOOTSTRAP_RUNNER=ubuntu-24.04
MAX_AUTHORIZED_BOOTSTRAP_RUNS=1
MAX_AUTHORIZED_TARGET_DISPATCHES_CREATED_BY_BOOTSTRAP=1
TARGET_WORKFLOW=.github/workflows/e004-conversion-runtime-evidence.yml
TARGET_REQUIRED_GIT_BLOB_SHA1=591317f1f570480b9ac68e7956d070db8ed5ef45
TARGET_REQUIRED_RAW_SHA256=95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327
TARGET_TRIGGER_REMAINS=workflow_dispatch_only
TARGET_CANONICAL_SOURCE_SHA=then-current_canonical_main_sha
TARGET_EXECUTION_REF=transient_sha_named_branch_initially_pointing_to_TARGET_CANONICAL_SOURCE_SHA
TARGET_EXECUTION_REF_PATTERN=e004-runtime-evidence-bind-<40_lower_hex_sha>
TARGET_EXECUTION_REF_IMMUTABLE=NO
MAX_AUTHORIZED_TRANSIENT_BINDING_REFS=1
TARGET_RUNTIME_EVIDENCE_RUN_ALLOWANCE_REMAINS=1
BOOTSTRAP_GITHUB_API_VERSION=2026-03-10
DISPATCH_REQUEST_BODY_FIELDS=ref_only
DISPATCH_RESPONSE_HTTP_STATUS=200
DISPATCH_RESPONSE_RUN_ID_BINDING=REQUIRED
CURRENT_AUTHORIZED_SPEND_USD=0
```

GitHub's current workflow-dispatch endpoint accepts a branch or tag name as `ref`; it does not provide a raw commit-SHA execution-ref parameter. A normal Git ref can be moved or deleted unless separately protected. No such repository-wide exclusion control is available to this bounded bootstrap.

The bootstrap is therefore a transport-only, fail-closed control step whose sole permitted mutations are:

1. create one transient SHA-named Git branch that initially points exactly to the then-current canonical `main` SHA; and
2. create the already-authorized native `workflow_dispatch` event for the exact target workflow using that branch name as the dispatch ref.

No repository file content may be changed by the bootstrap.

## Required bootstrap behavior

Before creating the target dispatch, the bootstrap must fail closed unless all of the following are true:

1. The bootstrap is running from the canonical `main` push created by canonical admission of this exact remediation surface.
2. The then-current canonical `main` SHA is read from GitHub.
3. The target workflow exists at `.github/workflows/e004-conversion-runtime-evidence.yml` on that exact canonical SHA.
4. The target workflow Git blob is exactly `591317f1f570480b9ac68e7956d070db8ed5ef45`.
5. The target workflow remains active and its target trigger is unchanged from the already-reviewed canonical workflow.
6. Workflow-specific GitHub Actions history across all refs reports zero prior target `workflow_dispatch` runs.
7. The bootstrap creates exactly one branch named `e004-runtime-evidence-bind-<canonical-main-sha>` and requires the created Git ref object to resolve exactly to the verified canonical `main` SHA.
8. The target workflow is re-read through that SHA-named binding ref and must have the same required Git blob identity before dispatch.
9. The binding ref is read back again immediately before dispatch and must still resolve to the verified canonical `main` SHA.
10. The bootstrap uses only the ephemeral repository `GITHUB_TOKEN`, with `actions: write` solely for the target dispatch and `contents: write` solely because GitHub requires repository-content write permission to create/delete Git refs. No file create/update/delete operation is permitted.
11. Under GitHub REST API version `2026-03-10`, the dispatch request body contains only the binding branch `ref`. The bootstrap requires the default `200` response containing `workflow_run_id`, `run_url`, and `html_url`, binds those returned details, reads that exact run back from GitHub, and requires its `head_sha`, `head_branch`, event, and workflow path to match the verified canonical SHA, exact binding branch, `workflow_dispatch`, and exact target path.
12. The bootstrap then requires workflow-specific target history across all refs to contain exactly one `workflow_dispatch` and requires that sole run to be the returned run ID.

If any prerequisite fails before the dispatch POST, the bootstrap must not dispatch. If any post-dispatch identity/cardinality check fails, the bootstrap must fail visibly and no rerun is authorized; any already-created run must be classified from live evidence rather than silently repeated.

## Residual external-interference risks

Two race classes cannot be made impossible by this bootstrap because it does not possess or create repository-wide administrative exclusion controls:

1. another actor can independently dispatch the target workflow between the final zero-run check and this bootstrap's dispatch request; and
2. another actor with sufficient repository authority can move/delete the SHA-named binding ref between its final read-back and GitHub resolving that branch for dispatch.

The Founder remediation directive authorizes proceeding with this bounded transport fix under the following explicit detection-only, fail-closed disposition:

```text
CONCURRENT_EXTERNAL_TARGET_DISPATCH_EXCLUSION=NOT_ENFORCEABLE_BY_THIS_BOOTSTRAP
BINDING_REF_MOVE_OR_DELETE_EXCLUSION=NOT_ENFORCEABLE_BY_THIS_BOOTSTRAP
RESIDUAL_EXTERNAL_INTERFERENCE_RISK_ACCEPTED_FOR_ONE_SHOT_TRANSPORT_REMEDIATION=YES
AUTHORIZED_TARGET_RUN=EXACT_BOOTSTRAP_RETURNED_WORKFLOW_RUN_ID_ONLY_IF_ALL_POSTCHECKS_PASS
ANY_OTHER_CONCURRENT_TARGET_DISPATCH=UNAUTHORIZED_EXTERNAL_INTERFERENCE
BINDING_REF_MOVED_OR_DELETED_BEFORE_DISPATCH_RESOLUTION=UNAUTHORIZED_EXTERNAL_INTERFERENCE
RETURNED_RUN_HEAD_SHA_MUST_EQUAL_VERIFIED_CANONICAL_SHA=YES
RETURNED_RUN_HEAD_BRANCH_MUST_EQUAL_SHA_NAMED_BINDING_BRANCH=YES
POST_DISPATCH_TOTAL_TARGET_WORKFLOW_DISPATCH_COUNT_MUST_EQUAL=1
ANY_POSTCHECK_MISMATCH=INCIDENT_FAIL_CLOSED
INCIDENT_FAIL_CLOSED_EFFECT=NO_RERUN_NO_RUNTIME_EVIDENCE_PROMOTION_E004_REMAINS_BLOCKED
EXTRA_OR_MISMATCHED_RUN_EXISTENCE_MAY_NOT_BE_ERASED_OR_RELABELED_AS_AUTHORIZED=YES
```

This acceptance does **not** authorize a second target dispatch or a moved-ref execution. It recognizes that external interference cannot be made impossible by this bootstrap alone and requires exact returned-run verification to invalidate evidence promotion rather than conceal or compensate for an incident.

## Supersession boundary

The prior V5 reconciliation correctly prohibited alternate execution routes while no exact Founder remediation authority existed. This record supersedes that prohibition only for the exact one-shot bootstrap and exact transient SHA-named binding ref defined here:

```text
V5_ALTERNATE_EXECUTION_ROUTE_PROHIBITION_SUPERSEDED=YES_EXACT_BOOTSTRAP_AND_BINDING_REF_ONLY
RERUN_AS_SUBSTITUTE_FOR_FRESH_DISPATCH=PROHIBITED
TARGET_TRIGGER_MUTATION=PROHIBITED
PUSH_OR_SCHEDULE_TRIGGER_ADDITION_TO_TARGET=PROHIBITED
ALTERNATE_TARGET_WORKFLOW=PROHIBITED
CARRIER_MODEL_OR_CONVERSION_EXECUTION=PROHIBITED
ALL_OTHER_ALTERNATE_EXECUTION_ROUTES=PROHIBITED
```

The target workflow itself must remain byte-identical to the already-canonical subject. No target-workflow text reconstruction or trigger mutation is authorized.

## Explicit exclusions

```text
MODEL_SOURCE_WEIGHT_ACQUISITION=PROHIBITED_BY_BOOTSTRAP
MODEL_CONVERSION=PROHIBITED_BY_BOOTSTRAP
MODEL_INFERENCE=PROHIBITED_BY_BOOTSTRAP
BENCHMARK_OR_DEVICE_EXECUTION=PROHIBITED_BY_BOOTSTRAP
CONTAMINATION_ASSESSMENT=PROHIBITED_BY_BOOTSTRAP
A15_ACTIVATION=PROHIBITED_BY_BOOTSTRAP
TRAINING=PROHIBITED_BY_BOOTSTRAP
PRIVATE_GOLD_OR_PHI_ACCESS=PROHIBITED_BY_BOOTSTRAP
EXTERNAL_REVIEWER_OUTREACH=PROHIBITED_BY_BOOTSTRAP
PROVIDER_GENERATION=PROHIBITED_BY_BOOTSTRAP
PROCUREMENT_OR_PAYMENT=PROHIBITED_BY_BOOTSTRAP
ARTIFACT_UPLOAD=PROHIBITED_BY_BOOTSTRAP
CACHE_UPLOAD=PROHIBITED_BY_BOOTSTRAP
PERSISTENT_CREDENTIAL_STORAGE=PROHIBITED
REPOSITORY_FILE_CONTENT_MUTATION_BY_BOOTSTRAP=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

This authority does not satisfy T1/A2, G1-G4, personnel/access/finance evidence, contamination evidence, A1-A14, A15, E004 tournament evidence, E005 winner selection, model conversion authority, or training authority.

## Cleanup rule

After the bootstrap has either created the single authorized target dispatch or terminally failed, no second bootstrap execution is authorized.

If the transient SHA-named binding branch was created, it must not be intentionally mutated by project automation. After the target run is terminal and its result has been captured, the binding branch and bootstrap workflow must be removed through ordinary reviewed cleanup. Cleanup must not alter the target runtime-evidence workflow or rewrite history.

## Exit evidence

This remediation authority is repository-level complete only when exact-head review confirms:

```text
FOUNDER_FIX_DIRECTIVE_CAPTURED=YES
BOOTSTRAP_SCOPE_TRANSIENT_AND_ONE_SHOT=YES
TARGET_WORKFLOW_IDENTITY_UNCHANGED=YES
TARGET_TRIGGER_REMAINS_WORKFLOW_DISPATCH_ONLY=YES
CANONICAL_MAIN_SHA_CAPTURE_REQUIRED=YES
SHA_NAMED_BINDING_REF_REQUIRED=YES
BINDING_REF_INITIAL_SHA_MUST_EQUAL_VERIFIED_CANONICAL_MAIN_SHA=YES
BINDING_REF_FINAL_PRE_DISPATCH_READBACK_REQUIRED=YES
BINDING_REF_IMMUTABILITY_FALSE_CLAIMED=NO
PRE_DISPATCH_ZERO_RUN_CHECK_REQUIRED=YES
CURRENT_API_DISPATCH_BODY_REF_ONLY=YES
DISPATCH_DEFAULT_200_RUN_DETAILS_REQUIRED=YES
DISPATCH_RETURNED_RUN_ID_BOUND=YES
POST_DISPATCH_EXACT_RUN_IDENTITY_CHECK_REQUIRED=YES
POST_DISPATCH_CARDINALITY_EQUALS_ONE_REQUIRED=YES
RESIDUAL_EXTERNAL_INTERFERENCE_FAIL_CLOSED_DISPOSITION_EXPLICIT=YES
MAX_TARGET_DISPATCHES_CREATED_BY_BOOTSTRAP=1
GITHUB_TOKEN_SCOPE_MINIMIZED_TO_REQUIRED_API_PERMISSIONS=YES
NO_REPOSITORY_FILE_CONTENT_MUTATION_BY_BOOTSTRAP=YES
NO_MODEL_CONVERSION_OR_TRAINING_AUTHORITY_CREATED=YES
NO_SCIENTIFIC_OR_GOVERNANCE_GATE_FABRICATED=YES
CURRENT_AUTHORIZED_SPEND_USD=0
```
