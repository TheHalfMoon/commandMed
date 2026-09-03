#!/usr/bin/env python3
"""Re-evaluate Aya-135 FD-008 evidence with canonical Spec 003 using DIRECT_DIGEST.

Consumes only repository-safe candidate identities, content digests, and categorical
FD-008 evidence. It never reads Aya raw text and delegates admission state entirely
to the canonical Spec 003 evaluator.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
from pathlib import Path
from typing import Any

from src.commandmed.eval_contract.lineage import evaluate_lineage_admission, validate_lineage_contract, validate_lineage_record

SOURCE_REPOSITORY = "CohereLabs/aya_dataset"
SOURCE_REVISION = "f9ea04583f02a8f86404ff6c58bf75fe637df8a2"
SOURCE_FILE = "data/train-00000-of-00001.parquet"
SOURCE_FILE_SHA256 = "51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06"
EXPECTED_COUNT = 135
EXPECTED_MANIFEST_CANONICAL_SHA256 = "dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99"
EXPECTED_RECORD_ID_SET_SHA256 = "d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83"
EXPECTED_CONTENT_SET_SHA256 = "ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64"
EXPECTED_PROJECTION_SHA256 = "1c696862705e50f10b8621f425389f8f9db0122ef8cc3027e46d50d6835430e7"
EXPECTED_DETERMINISTIC_OUTPUT_SHA256 = "129688b220a75773a7709c656a2aa313f2aed770541dc62a39b3351848beb07d"
EXPECTED_MAP_PART_SHA256 = [
    "b6028a65c05d41a251ef8b4a5073d30e8b4048322853a97ad020783cdea79687",
    "59d1445a98f6ac5bfc8d50fb125700fbbd590d61f17b7fd35e1f9d0f428923a3",
    "48310fdf92872e39d0c4f9527dab52e6682b9a117040f2cedef70fcf4eb63ef2",
    "5d58375d6a36eaa1abb5fedda95004d12381e685b09b20c129171ddadf2d4b95",
    "13014dcfab8fc511554c2f4fcd7afa105a84c7ccd43cf449b583627ed0fb1597",
]
CONTAMINATION_METHOD_ID = "AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1"
CONTAMINATION_RESULTS_SHA256 = "f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857"
EVALUATOR_SOURCE_COMMIT = "7fa0b8d4baee9e6ef5f2a0ca30aaf0bd8199c6fc"
EVALUATOR_LINEAGE_BLOB_SHA = "5d7a5b6a8b48b2b5a7afea35ed18ceb1c9fe6425"
LINEAGE_CONTRACT_BLOB_SHA = "692de9b32271031b0f1dd9cc6edc98bc44b580b5"
ARTIFACT_ID = "e004-aya-135-spec003-direct-digest-correction-v1"
RIGHTS_EVIDENCE_URI = f"https://huggingface.co/datasets/{SOURCE_REPOSITORY}/blob/{SOURCE_REVISION}/README.md"
SOURCE_EVIDENCE_URI = f"https://huggingface.co/datasets/{SOURCE_REPOSITORY}/blob/{SOURCE_REVISION}/{SOURCE_FILE}"
SOURCE_URI = f"https://huggingface.co/datasets/{SOURCE_REPOSITORY}/tree/{SOURCE_REVISION}"


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def file_sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def set_root(values: list[str]) -> str:
    return hashlib.sha256(("\n".join(sorted(values))+"\n").encode("ascii")).hexdigest()


def load_projection(path: Path, allow_local_generated: bool=False) -> dict[str, Any]:
    if not allow_local_generated and file_sha256(path) != EXPECTED_PROJECTION_SHA256:
        raise SystemExit("PROJECTION_SHA256_MISMATCH")
    p=json.load(open(path, encoding='utf-8'))
    expected={
      'artifact_id':'e004-aya-135-deterministic-admission-projection-v1',
      'candidate_count':EXPECTED_COUNT,
      'candidate_manifest_canonical_sha256':EXPECTED_MANIFEST_CANONICAL_SHA256,
      'candidate_record_id_set_sha256':EXPECTED_RECORD_ID_SET_SHA256,
      'candidate_content_sha256_set_sha256':EXPECTED_CONTENT_SET_SHA256,
      'deterministic_evidence_output_sha256':EXPECTED_DETERMINISTIC_OUTPUT_SHA256,
      'method_id':'AYA_135_LOCAL_DETERMINISTIC_RECORD_EVIDENCE_V1',
      'privacy_no_phi_known_count':118,
      'source_risk_clear_count':43,
      'source_risk_unresolved_count':92,
      'scope_pass_count':135,
      'external_ai_or_model_used':False,
      'external_provider_used':False,
      'network_access_performed':False,
      'raw_text_persisted':False,
      'user_id_read':False,
    }
    for k,v in expected.items():
        if p.get(k)!=v: raise SystemExit(f"PROJECTION_{k.upper()}_MISMATCH")
    groups = {
      'supported': set(p['rights_supported_candidate_ids']),
      'unresolved': set(p['rights_unresolved_candidate_ids']),
      'privacy_unresolved': set(p['privacy_unresolved_candidate_ids']),
      'privacy_restricted': set(p['privacy_restricted_or_phi_candidate_ids']),
      'scope_fail': set(p['scope_fail_candidate_ids']),
      'scope_unresolved': set(p['scope_unresolved_candidate_ids']),
    }
    all_ids=groups['supported']|groups['unresolved']
    if groups['supported'] & groups['unresolved']: raise SystemExit('RIGHTS_GROUP_OVERLAP')
    if len(groups['supported'])!=43 or len(groups['unresolved'])!=92: raise SystemExit('RIGHTS_COUNTS_MISMATCH')
    if len(groups['privacy_unresolved'])!=17 or groups['privacy_restricted']: raise SystemExit('PRIVACY_COUNTS_MISMATCH')
    if groups['scope_fail'] or groups['scope_unresolved']: raise SystemExit('SCOPE_NOT_FULL_PASS')
    if not groups['privacy_unresolved'] <= all_ids: raise SystemExit('PRIVACY_ID_OUTSIDE_SET')
    if set_root(list(all_ids)) != EXPECTED_RECORD_ID_SET_SHA256: raise SystemExit('PROJECTION_RECORD_ROOT_MISMATCH')
    return p


def load_digest_map(paths: list[Path]) -> dict[str,str]:
    if len(paths)!=5: raise SystemExit('DIGEST_MAP_PART_COUNT_MISMATCH')
    result={}
    for idx,(path,expected_sha) in enumerate(zip(paths,EXPECTED_MAP_PART_SHA256), start=1):
        if file_sha256(path)!=expected_sha: raise SystemExit(f'DIGEST_MAP_PART_{idx}_SHA256_MISMATCH')
        part=json.load(open(path, encoding='utf-8'))
        if part.get('artifact_id')!='e004-aya-135-candidate-content-digest-map-v1' or part.get('schema_version')!='1': raise SystemExit(f'DIGEST_MAP_PART_{idx}_SCHEMA_MISMATCH')
        if part.get('part')!=idx or part.get('part_count')!=5 or part.get('candidate_count_total')!=135: raise SystemExit(f'DIGEST_MAP_PART_{idx}_ENVELOPE_MISMATCH')
        if len(part.get('records',[]))!=27: raise SystemExit(f'DIGEST_MAP_PART_{idx}_COUNT_MISMATCH')
        for rec in part['records']:
            rid=rec.get('candidate_record_id'); digest=rec.get('content_sha256')
            if not isinstance(rid,str) or len(rid)!=64 or not isinstance(digest,str) or len(digest)!=64: raise SystemExit('DIGEST_MAP_INVALID_RECORD')
            if rid in result: raise SystemExit('DIGEST_MAP_DUPLICATE_RECORD_ID')
            result[rid]=digest
    if len(result)!=135: raise SystemExit('DIGEST_MAP_TOTAL_COUNT_MISMATCH')
    if set_root(list(result))!=EXPECTED_RECORD_ID_SET_SHA256: raise SystemExit('DIGEST_MAP_RECORD_ROOT_MISMATCH')
    if set_root(list(result.values()))!=EXPECTED_CONTENT_SET_SHA256: raise SystemExit('DIGEST_MAP_CONTENT_ROOT_MISMATCH')
    return result


def verify_contamination(path: Path) -> None:
    e=json.load(open(path, encoding='utf-8'))
    checks={
      'candidate_count':135,
      'candidate_manifest_canonical_sha256':EXPECTED_MANIFEST_CANONICAL_SHA256,
      'candidate_record_id_set_sha256':EXPECTED_RECORD_ID_SET_SHA256,
      'candidate_content_sha256_set_sha256':EXPECTED_CONTENT_SET_SHA256,
      'source_file_sha256':SOURCE_FILE_SHA256,
      'contamination_method_id':CONTAMINATION_METHOD_ID,
      'contamination_results_sha256':CONTAMINATION_RESULTS_SHA256,
      'purpose':'TRAIN',
      'quarantine_state':'NOT_QUARANTINED',
    }
    for k,v in checks.items():
        if e.get(k)!=v: raise SystemExit(f'CONTAMINATION_{k.upper()}_MISMATCH')
    if e.get('contamination_state_counts')!={'ASSESSED_CLEAN':135}: raise SystemExit('CONTAMINATION_STATE_MISMATCH')
    if e.get('quarantine_conflict_observed') is not False or e.get('private_gold_used') is not False or e.get('public_external_eval_used_as_training_source') is not False: raise SystemExit('QUARANTINE_EVIDENCE_CONFLICT')


def lineage_record(rid:str, content_sha:str, projection:dict[str,Any]) -> dict[str,Any]:
    supported=set(projection['rights_supported_candidate_ids'])
    privacy_unresolved=set(projection['privacy_unresolved_candidate_ids'])
    return {
      'asset_id':f'aya-135:{rid}',
      'asset_class':'DATASET_OR_CORPUS',
      'canonical_name':f'Aya exact candidate {rid}',
      'record_version':'1',
      'source_identifier':f'{SOURCE_REPOSITORY}:{SOURCE_FILE}:{rid}',
      'source_uri':SOURCE_URI,
      'source_revision':SOURCE_REVISION,
      'source_verification_status':'VERIFIED',
      'source_evidence_uri':SOURCE_EVIDENCE_URI,
      'declared_use':'TRAINING_OR_ADAPTATION',
      'access_class':'PUBLIC',
      'rights_state':'SUPPORTED' if rid in supported else 'UNRESOLVED',
      'rights_evidence_uri':RIGHTS_EVIDENCE_URI,
      'artifact_binding_state':'DIRECT_DIGEST',
      'content_sha256':content_sha,
      'phi_privacy_state':'UNRESOLVED' if rid in privacy_unresolved else 'NO_PHI_KNOWN',
      'purpose':'TRAIN',
      'quarantine_state':'NOT_QUARANTINED',
      'contamination_state':'ASSESSED_CLEAN',
      'origin_type':'ORIGINAL',
      'spdx_license_expression':'Apache-2.0',
    }


def evaluate(projection_path:Path, map_parts:list[Path], contamination_path:Path, contract_path:Path, allow_local_generated_projection:bool=False) -> dict[str,Any]:
    projection=load_projection(projection_path, allow_local_generated_projection)
    digest_map=load_digest_map(map_parts)
    candidate_ids=set(projection['rights_supported_candidate_ids'])|set(projection['rights_unresolved_candidate_ids'])
    if candidate_ids != set(digest_map): raise SystemExit('PROJECTION_DIGEST_MAP_ID_SET_MISMATCH')
    verify_contamination(contamination_path)
    contract=json.load(open(contract_path, encoding='utf-8'))
    if validate_lineage_contract(contract): raise SystemExit('SPEC003_CONTRACT_INVALID')
    results=[]; states=collections.Counter(); reasons=collections.Counter(); validation_errors=0
    for rid in sorted(candidate_ids):
        rec=lineage_record(rid,digest_map[rid],projection)
        errors=validate_lineage_record(rec,contract)
        if errors:
            validation_errors+=1
            raise SystemExit(f'SPEC003_RECORD_INVALID:{rid}')
        adm=evaluate_lineage_admission(rec,contract)
        state=str(adm['state']); rcs=[str(x) for x in adm['reason_codes']]
        states[state]+=1; reasons.update(rcs)
        results.append({'candidate_record_id':rid,'content_sha256':digest_map[rid],'privacy_state':rec['phi_privacy_state'],'rights_state':rec['rights_state'],'scope_verification':'PASS','contamination_state':'ASSESSED_CLEAN','state':state,'reason_codes':rcs,'contract_sha256':adm['contract_sha256'],'record_sha256':adm['record_sha256']})
    if validation_errors!=0 or states != collections.Counter({'BLOCKED':92,'ELIGIBLE':43}) or reasons != collections.Counter({'RIGHTS_UNRESOLVED':92,'PRIVACY_UNRESOLVED':17}):
        raise SystemExit('SPEC003_EXPECTED_RESULT_MISMATCH')
    return {
      'artifact_id':ARTIFACT_ID,
      'schema_version':'1',
      'correction_of_historical_result_sha256':'3e7e4f15a913ca5e72c091aee4dda563f48037ed6fd67a3781fef1ade71d21ef',
      'correction_reason':'Historical committed deterministic evidence blob failed byte-identity verification against the declared FD-008 output SHA-256; this result is recomputed from the verified projection plus exact candidate content digests.',
      'candidate_count':135,
      'candidate_manifest_canonical_sha256':EXPECTED_MANIFEST_CANONICAL_SHA256,
      'candidate_record_id_set_sha256':EXPECTED_RECORD_ID_SET_SHA256,
      'candidate_content_sha256_set_sha256':EXPECTED_CONTENT_SET_SHA256,
      'deterministic_evidence_method_id':'AYA_135_LOCAL_DETERMINISTIC_RECORD_EVIDENCE_V1',
      'deterministic_evidence_output_sha256':EXPECTED_DETERMINISTIC_OUTPUT_SHA256,
      'projection_sha256':EXPECTED_PROJECTION_SHA256,
      'digest_map_part_sha256':EXPECTED_MAP_PART_SHA256,
      'contamination_method_id':CONTAMINATION_METHOD_ID,
      'contamination_results_sha256':CONTAMINATION_RESULTS_SHA256,
      'evaluator_source_commit':EVALUATOR_SOURCE_COMMIT,
      'evaluator_lineage_blob_sha':EVALUATOR_LINEAGE_BLOB_SHA,
      'lineage_contract_blob_sha':LINEAGE_CONTRACT_BLOB_SHA,
      'artifact_binding_state':'DIRECT_DIGEST',
      'caller_controlled_eligible_state':False,
      'state_counts':dict(sorted(states.items())),
      'reason_counts':dict(sorted(reasons.items())),
      'validation_error_count':validation_errors,
      'results':results,
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--projection', type=Path, required=True)
    ap.add_argument('--digest-map-part', type=Path, action='append', required=True)
    ap.add_argument('--contamination-evidence', type=Path, required=True)
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--allow-local-generated-projection', action='store_true')
    a=ap.parse_args()
    result=evaluate(a.projection,a.digest_map_part,a.contamination_evidence,a.contract,a.allow_local_generated_projection)
    a.out.write_bytes(canonical_bytes(result)+b'\n')
    print(json.dumps({'artifact_id':ARTIFACT_ID,'candidate_count':135,'output_sha256':file_sha256(a.out),'state_counts':result['state_counts'],'reason_counts':result['reason_counts'],'validation_error_count':0},sort_keys=True,separators=(',',':')))

if __name__=='__main__': main()
