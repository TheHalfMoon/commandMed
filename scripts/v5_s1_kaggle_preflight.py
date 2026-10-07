#!/usr/bin/env python3
"""Private Kaggle S1 pre-model qualification; no model load or inference."""
from __future__ import annotations

import argparse
import importlib.metadata
import json
import math
import platform
import shutil
import sys
import time
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import v5_s1_colab_qualification as existing

base = existing.base
PACKET = existing.PACKET
OUTPUT_REL = Path('artifacts/v5/development/s1-kaggle-preflight')
AMENDMENT = 'V5_S1_KAGGLE_RUNTIME_AMENDMENT_2026-10-08.md'
KERNEL = 'abdulazizshehri/commandmed-v5-c1-seed-11-qualification'


def validate_admission(record: dict, now: float | None = None) -> float:
    required = {'cost_basis':'KAGGLE_ZERO_COST_RUNTIME', 'username':'abdulazizshehri',
                'private':True, 'expected_incremental_spend_usd':0, 'new_purchase':False,
                'scientific_gpu_count':1, 'scientific_device':'cuda:0',
                'confirmatory_materialized':False, 'reserve_materialized':False, 'phi':False}
    if any(record.get(key)!=value for key,value in required.items()):
        raise RuntimeError('KAGGLE_COST_PRIVACY_OR_GPU_ADMISSION_BLOCKED')
    if record.get('kernel_ref') != KERNEL:
        raise RuntimeError('KAGGLE_KERNEL_IDENTITY_MISMATCH')
    now = time.time() if now is None else now
    observed = record.get('quota_observed_unix')
    quota = record.get('free_gpu_seconds_available')
    timeout = record.get('requested_session_timeout_seconds')
    numbers = (observed, quota, timeout, now)
    if any(isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) for x in numbers):
        raise RuntimeError('KAGGLE_QUOTA_OR_WINDOW_OBSERVATION_MISSING')
    age = now-observed
    if age < 0 or age > 600 or quota <= 0 or not 0 < timeout <= 43200:
        raise RuntimeError('KAGGLE_QUOTA_OR_WINDOW_OBSERVATION_STALE_OR_INVALID')
    remaining = min(quota,timeout)-age
    if remaining <= 600:
        raise RuntimeError('KAGGLE_ATOMIC_WINDOW_UNAVAILABLE')
    return remaining


def verify_frozen_bindings() -> dict:
    binding = json.loads((PACKET/'V5_S1_KAGGLE_RUNTIME_AMENDMENT_BINDINGS_2026-10-08.json').read_text())
    rows = binding['unchanged_entry_files']
    failures = [row['path'] for row in rows if base.sha256_file(base.REPO/row['path']) != row['sha256']]
    if failures or base.sha256_file(PACKET/AMENDMENT)!=binding['amendment_sha256']:
        raise RuntimeError('KAGGLE_FROZEN_ENTRY_BINDING_MISMATCH:'+','.join(failures))
    return {'verified_entry_file_count':len(rows),'binding_sha256':base.sha256_file(PACKET/'V5_S1_KAGGLE_RUNTIME_AMENDMENT_BINDINGS_2026-10-08.json'),
            'scientific_freeze_sha256':base.sha256_file(PACKET/'scientific-freeze-bindings-v5.json'),
            'amendment_sha256':binding['amendment_sha256']}


def verify_gpu_binding(torch) -> list[dict]:
    if not torch.cuda.is_available() or torch.cuda.device_count()<1:
        raise RuntimeError('KAGGLE_ASSIGNED_CUDA_ACCELERATOR_UNAVAILABLE')
    torch.cuda.set_device(0)
    if torch.cuda.current_device()!=0:
        raise RuntimeError('KAGGLE_SCIENTIFIC_DEVICE_NOT_CUDA_0')
    visible = []
    for index in range(torch.cuda.device_count()):
        props = torch.cuda.get_device_properties(index)
        visible.append({'index':index,'name':props.name,'total_memory_bytes':props.total_memory,
                        'compute_capability':list(torch.cuda.get_device_capability(index)),
                        'scientific_use':index==0})
    if 'T4' not in visible[0]['name']:
        raise RuntimeError('KAGGLE_SINGLE_T4_QUALIFICATION_HARDWARE_MISMATCH')
    if not torch.cuda.is_bf16_supported():
        raise RuntimeError('KAGGLE_BFLOAT16_UNSUPPORTED')
    return visible


def qualify(args) -> tuple[dict,Path]:
    output = base.REPO/OUTPUT_REL/'seed-11'
    output.mkdir(parents=True,exist_ok=False)
    result = {'status':'IN_PROGRESS','model_loaded':False,'model_inference':False,'training':False,
              'confirmatory_materialized':False,'reserve_materialized':False,'phi':False,'spend_usd':0,
              'scientific_gpu_count':1,'scientific_device':'cuda:0','durable_export_verified':False}
    def persist(name,value):
        base.write_json(output/name,value)
    try:
        head = base.git_text('rev-parse','HEAD')
        if head!=args.expected_head or base.git_text('status','--porcelain','--untracked-files=no'):
            raise RuntimeError('KAGGLE_EXACT_CLEAN_HEAD_MISMATCH')
        remote = base.git_text('ls-remote','origin','refs/heads/research/commandmed-paper-first-principles')
        if remote.split()[0]!=head:
            raise RuntimeError('KAGGLE_LIVE_REMOTE_HEAD_MISMATCH')
        result.update(code_sha=head,git_tree=base.git_text('show','-s','--format=%T','HEAD'))
        admission = json.loads(args.admission.read_text())
        validate_admission(admission)
        frozen = verify_frozen_bindings()
        persist('frozen-bindings.json',frozen)
        import torch
        import psutil
        hardware = verify_gpu_binding(torch)
        persist('hardware-manifest.json',{'visible_gpus':hardware,'cuda_device_count':len(hardware),
                                        'scientific_gpu_count':1,'scientific_device':'cuda:0'})
        torch.set_num_threads(base.CPU_THREADS)
        torch.set_num_interop_threads(base.CPU_INTEROP_THREADS)
        # Seed the CPU and the scientific GPU only. Do not seed GPU 1.
        torch.random.default_generator.manual_seed(11)
        torch.cuda.manual_seed(11)
        packages = {name:importlib.metadata.version(name) for name in
                    ('torch','transformers','tokenizers','peft','numpy','huggingface-hub','safetensors','psutil')}
        environment = {'python':sys.version,'platform':platform.platform(),'packages':packages,
                       'cuda':torch.version.cuda,'runtime_dtype':'bfloat16','visible_gpus':hardware,
                       'scientific_gpu_count':1,'scientific_device':'cuda:0',
                       'native_bfloat16_support':torch.cuda.is_bf16_supported(including_emulation=False),
                       'bfloat16_support':torch.cuda.is_bf16_supported(),'cpu_count':psutil.cpu_count(),
                       'ram_total_bytes':psutil.virtual_memory().total,'admission':admission,
                       'frozen_bindings':frozen,'runner_sha256':base.sha256_file(Path(__file__))}
        persist('environment-before-imports.json',environment)
        # Imports qualify implementation support; these do not load weights.
        from transformers import AutoModelForCausalLM, AutoTokenizer
        from peft import LoraConfig, TaskType, get_peft_model
        environment['required_imports']='PASS'
        environment['memory_before_load']=existing.memory(torch)
        existing.require_headroom(environment['memory_before_load'])
        environment['bfloat16_primitive_probe']=existing.primitive_probe(torch)
        acquired = base.acquire_model(args.model_dir)
        if acquired['resolved_sha']!=base.MODEL_REVISION or acquired['private'] or acquired['gated']:
            raise RuntimeError('KAGGLE_EXACT_PUBLIC_MODEL_REVISION_MISMATCH')
        artifact,bundle = base.bind_artifact(args.model_dir)
        artifact['files']=existing.reproduce_frozen_file_order(artifact['files'])
        artifact['bundle_sha256']=base.sha256_bytes(base.canonical_json(artifact['files']))
        if artifact['bundle_sha256']!=existing.EXPECTED_BUNDLE:
            raise RuntimeError('KAGGLE_MODEL_ARTIFACT_MISMATCH')
        persist('model-artifact-manifest.json',artifact)
        base.acquire_source(args.source)
        if shutil.disk_usage(args.model_dir).free<base.MIN_DISK_HEADROOM:
            raise RuntimeError('KAGGLE_DISK_HEADROOM_BELOW_2_GIB')
        prep = existing.verify_preparation(args.model_dir,args.source,output)
        if prep['example_count']!=8192 or prep['full_prompt_candidate_check_count']!=32768 or prep['tokenizer_candidate_ids']!={'A':32,'B':33} or prep['answer_prefix']!='ANSWER:\n' or max(prep['max_prompt_tokens_by_split'].values())>768 or prep['overlength_count']:
            raise RuntimeError('KAGGLE_FULL_INTERFACE_QUALIFICATION_MISMATCH')
        remaining = validate_admission(admission)
        environment.update(model_revision=base.MODEL_REVISION,artifact_bundle_sha256=artifact['bundle_sha256'],
                           tokenizer_files=prep['tokenizer_files'],preparation_sha256=base.sha256_file(output/'preparation/task-preparation-evidence.json'),
                           remaining_window_and_quota_seconds=remaining)
        env_sha=base.sha256_bytes(base.canonical_json(environment))
        persist('environment-manifest.json',{**environment,'environment_sha256':env_sha})
        authority = base.DevelopmentAuthority(approved=True,authority_id='KAGGLE_AUTHORITY_SHA256:'+frozen['amendment_sha256'])
        manifest = base.DevelopmentRunManifest(action='MODEL_LOAD',model_repo=base.MODEL_REPO,
                   model_revision=base.MODEL_REVISION,model_artifact_sha256=existing.EXPECTED_BUNDLE,
                   intervention_id='C1_CRDI_V1',data_roles=('RULE_ORACLE_DEVELOPMENT','RULE_ORACLE_CALIBRATION'),
                   code_sha=head,environment_id='sha256:'+env_sha,output_destination=output.relative_to(base.REPO).as_posix()+'/')
        decision = base.evaluate_development_preflight(manifest,authority)
        persist('preflight-model-load.json',{'authority':asdict(authority),'manifest':asdict(manifest),'decision':asdict(decision)})
        if not decision.allowed or decision.state!='PREFLIGHT_PASS':
            raise RuntimeError('KAGGLE_EXACT_RUN_PREFLIGHT_BLOCKED')
        result.update(status='KAGGLE_PREFLIGHT_PASS',model_load_executed=False,
                      duration_admission='NOT_REACHED_NO_MODEL_RESOURCE_MEASUREMENT',remaining_seconds=remaining,
                      finished_at=datetime.now(timezone.utc).isoformat())
    except (Exception,SystemExit) as exc:
        result.update(status='KAGGLE_PREFLIGHT_BLOCKED',exception_type=type(exc).__name__,reason=str(exc))
    persist('kaggle-preflight-result.json',result)
    return result,output


def main():
    parser=argparse.ArgumentParser()
    for name in ('model-dir','source','admission'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--expected-head',required=True)
    args=parser.parse_args()
    result,output=qualify(args)
    archive=Path(shutil.make_archive(str(output),'zip',output))
    print(json.dumps({'result':result,'evidence_zip':str(archive),'evidence_zip_sha256':base.sha256_file(archive)},sort_keys=True),flush=True)
    return 0 if result['status']=='KAGGLE_PREFLIGHT_PASS' else 2


if __name__=='__main__':
    raise SystemExit(main())
