#!/usr/bin/env python3
"""Single-GPU Kaggle runtime binding for the unchanged atomic C1 algorithm.

The original adapter module and scientific functions are reused byte-for-byte.
Only its runtime-qualification namespace is substituted. Legacy COLAB-prefixed
authority/stop labels in that module remain labels, with Kaggle authority hashes
and explicit runtime metadata bound underneath them. GPU 1 is inaccessible.
"""
import argparse
import json
import os
import shutil
import sys
import time
from dataclasses import asdict
from pathlib import Path

# Set before importing torch or the original runner. cuda:0 maps to physical 0.
os.environ['CUDA_VISIBLE_DEVICES']='0'

import v5_s1_adapter_development as frozen
import v5_s1_kaggle_preflight as metadata
import v5_s1_colab_qualification as shared

base=shared.base
EXPECTED_BUNDLE=shared.EXPECTED_BUNDLE
memory=shared.memory
require_headroom=shared.require_headroom


def validate_admission(record):
    metadata.validate_admission(record)
    if record.get('intervention')!='C1_CRDI_V1' or record.get('seed')!=11:
        raise RuntimeError('KAGGLE_C1_SEED_11_ONLY')


def verify_head(expected):
    if base.git_text('rev-parse','HEAD')!=expected:
        raise RuntimeError('KAGGLE_EXACT_REVIEWED_HEAD_MISMATCH')
    for row in base.git_text('status','--porcelain','--untracked-files=all').splitlines():
        if not row[3:].startswith(metadata.OUTPUT_REL.as_posix()+'/'):
            raise RuntimeError('KAGGLE_NON_EVIDENCE_CHECKOUT_CHANGE')
    return expected


def qualify(args):
    import torch
    from peft import LoraConfig,TaskType,get_peft_model
    from transformers import AutoModelForCausalLM,AutoTokenizer

    if torch.cuda.device_count()!=1 or torch.cuda.current_device()!=0:
        raise RuntimeError('KAGGLE_ATOMIC_SCIENTIFIC_GPU_ISOLATION_FAILED')
    result,output=metadata.qualify(args)
    if result['status']!='KAGGLE_PREFLIGHT_PASS':
        return result,output
    admission=json.loads(args.admission.read_text())
    environment=json.loads((output/'environment-manifest.json').read_text())
    authority_bindings={name:base.sha256_file(shared.PACKET/name) for name in shared.AUTHORITY_FILES}
    authority_bindings[metadata.AMENDMENT]=base.sha256_file(shared.PACKET/metadata.AMENDMENT)
    environment.pop('environment_sha256')
    environment.update(authority_sha256=authority_bindings,runtime_backend_sha256=base.sha256_file(Path(__file__)),
                       original_adapter_runner_sha256=base.sha256_file(Path(frozen.__file__)),
                       cuda_visible_devices='0',physical_hardware=json.loads(args.physical_hardware.read_text()))
    env_sha=base.sha256_bytes(base.canonical_json(environment))
    base.write_json(output/'environment-manifest.json',{**environment,'environment_sha256':env_sha})
    state={'status':'RESOURCE_QUALIFICATION_IN_PROGRESS','code_sha':args.expected_head,
           'git_tree':base.git_text('show','-s','--format=%T','HEAD'),'model_loaded':False,
           'model_inference':False,'optimization_executed':False,'medical_optimizer_steps':0,
           'scientific_gpu_count':1,'scientific_device':'cuda:0','durable_export_verified':False}
    prep=json.loads((output/'preparation/task-preparation-evidence.json').read_text())
    persist=lambda name,value:base.write_json(output/name,value)

    def preflight(action,roles=('SYNTHETIC_MECHANICAL',),label=None):
        verify_head(args.expected_head)
        authority=base.DevelopmentAuthority(approved=True,authority_id='KAGGLE_AUTHORITY_SHA256:'+base.sha256_bytes(base.canonical_json(authority_bindings)))
        manifest=base.DevelopmentRunManifest(action=action,model_repo=base.MODEL_REPO,model_revision=base.MODEL_REVISION,
            model_artifact_sha256=EXPECTED_BUNDLE,intervention_id='C1_CRDI_V1',data_roles=roles,
            code_sha=args.expected_head,environment_id='sha256:'+env_sha,output_destination=output.relative_to(base.REPO).as_posix()+'/')
        decision=base.evaluate_development_preflight(manifest,authority)
        persist('resource-preflight-'+(label or action.lower())+'.json',{'authority':asdict(authority),'manifest':asdict(manifest),'decision':asdict(decision)})
        if not decision.allowed or decision.state!='PREFLIGHT_PASS':
            raise RuntimeError('KAGGLE_RESOURCE_ACTION_PREFLIGHT_BLOCKED')

    try:
        # This is the original resource sequence, objective and sample rule.
        preflight('MODEL_LOAD')
        tick=time.perf_counter()
        sampler=base.MemorySampler()
        sampler.start()
        try:
            model=AutoModelForCausalLM.from_pretrained(args.model_dir,local_files_only=True,dtype=torch.bfloat16,low_cpu_mem_usage=True)
            state['model_loaded']=True
            model.to('cuda:0').eval()
            torch.cuda.synchronize()
        finally:
            observed=sampler.stop()
            persist('load-observation.json',{'load_seconds':time.perf_counter()-tick,**observed,**memory(torch)})
        if observed['min_system_available_bytes']<base.MIN_MEMORY_HEADROOM:
            raise RuntimeError('KAGGLE_MODEL_LOAD_SYSTEM_HEADROOM_BLOCKER')
        require_headroom(memory(torch))
        if any(p.dtype!=torch.bfloat16 or p.device!=torch.device('cuda:0') for p in model.parameters()):
            raise RuntimeError('KAGGLE_RESOURCE_MODEL_DTYPE_OR_DEVICE_MISMATCH')
        tokenizer=AutoTokenizer.from_pretrained(args.model_dir,local_files_only=True)
        a,b=prep['tokenizer_candidate_ids']['A'],prep['tokenizer_candidate_ids']['B']
        preflight('INFERENCE')
        encoded=tokenizer('TASK: Mechanical label check.\nA = MATCH\nB = MISMATCH\nReturn only A or B.\nANSWER:\n',return_tensors='pt',add_special_tokens=False).to('cuda:0')
        tick=time.perf_counter()
        with torch.no_grad():
            state['model_inference']=True
            logits=model(**encoded,use_cache=False).logits[0,-1,[a,b]]
        torch.cuda.synchronize()
        if not bool(torch.isfinite(logits).all()):
            raise RuntimeError('KAGGLE_NONFINITE_SMOKE_LOGITS')
        persist('smoke-inference.json',{'candidate_logits':logits.float().cpu().tolist(),'wall_seconds':time.perf_counter()-tick,'logits_dtype':str(logits.dtype),'memory':memory(torch)})
        targets=base.final_block_linear_names(model,torch)
        adapted=get_peft_model(model,LoraConfig(r=4,lora_alpha=8,lora_dropout=0.0,bias='none',target_modules=targets,task_type=TaskType.CAUSAL_LM),autocast_adapter_dtype=False)
        trainable=[(name,p) for name,p in adapted.named_parameters() if p.requires_grad]
        if sum(p.numel() for _,p in trainable)!=100352 or any('lora_' not in name or 'layers.23.' not in name or p.dtype!=torch.bfloat16 for name,p in trainable):
            raise RuntimeError('KAGGLE_FINAL_BLOCK_LORA_SCOPE_OR_DTYPE_MISMATCH')
        persist('trainable-parameters.json',{'target_modules':targets,'parameters':[{'name':name,'count':p.numel(),'dtype':str(p.dtype)} for name,p in trainable],'total':sum(p.numel() for _,p in trainable)})
        preflight('TRAINING')
        unit=tokenizer.encode(' mechanical',add_special_tokens=False)
        ids=torch.tensor([(unit*(256//len(unit)+1))[:256]],dtype=torch.long,device='cuda:0')
        optimizer=torch.optim.AdamW([p for _,p in trainable],lr=5e-4,betas=(0.9,0.999),eps=1e-8,weight_decay=0.0)

        def step(label):
            optimizer.zero_grad(set_to_none=True)
            pair=[adapted(input_ids=ids,attention_mask=torch.ones_like(ids),use_cache=False).logits[:,-1,[a,b]].float() for _ in range(2)]
            probabilities=[torch.softmax(item,dim=-1)[0].clamp_min(1e-12) for item in pair]
            loss=torch.nn.functional.cross_entropy(pair[0],torch.tensor([0],device='cuda:0'))+0.1*base.js_divergence(torch,*probabilities)
            if not bool(torch.isfinite(loss)):
                raise RuntimeError('KAGGLE_NONFINITE_SYNTHETIC_LOSS')
            loss.backward()
            if any(p.grad is None or not bool(torch.isfinite(p.grad).all()) for _,p in trainable):
                raise RuntimeError('KAGGLE_NONFINITE_OR_MISSING_LORA_GRADIENT')
            torch.nn.utils.clip_grad_norm_([p for _,p in trainable],1.0)
            optimizer.step()
            state['optimization_executed']=True
            if any(not bool(torch.isfinite(p).all()) for _,p in trainable):
                raise RuntimeError('KAGGLE_NONFINITE_LORA_PARAMETER')
            torch.cuda.synchronize()
            persist(label+'-step.json',{'loss':float(loss.detach().cpu()),'memory':memory(torch),'synthetic_tokens':256})
            require_headroom(memory(torch))

        step('warmup')
        torch.cuda.reset_peak_memory_stats()
        sampler=base.MemorySampler()
        sampler.start()
        tick=time.perf_counter()
        try:
            step('timed')
        finally:
            timing={'wall_seconds':time.perf_counter()-tick,**sampler.stop(),**memory(torch)}
            persist('benchmark-timing.json',timing)
        shared.require_benchmark_bounds(timing)
        rules=base.bind_selected_rules(source_bytes=args.source.read_bytes(),selection_manifest=json.loads(base.SELECTION_MANIFEST.read_text()))
        examples=base.materialize_development_examples(rules)
        domain='|CommandMed-V5-S1-COLAB-RESOURCE-TIMING-v1'
        sample=sorted(examples,key=lambda example:base.sha256_bytes((example.task_id+domain).encode('ascii')))[:16]
        preflight('INFERENCE',roles=('RULE_ORACLE_DEVELOPMENT','RULE_ORACLE_CALIBRATION'),label='medical-resource-timing')
        observations=[]
        with adapted.disable_adapter(),torch.no_grad():
            for example in sample:
                for variant,prompt in (('canonical',example.canonical_prompt),('transformed',example.transformed_prompt)):
                    encoded=tokenizer(prompt,return_tensors='pt',add_special_tokens=False).to('cuda:0')
                    torch.cuda.synchronize()
                    tick=time.perf_counter()
                    logits=adapted(**encoded,use_cache=False).logits[0,-1,[a,b]]
                    torch.cuda.synchronize()
                    if not bool(torch.isfinite(logits).all()):
                        raise RuntimeError('KAGGLE_NONFINITE_RESOURCE_MEDICAL_LOGITS')
                    observations.append({'task_id':example.task_id,'variant':variant,'tokens':encoded.input_ids.shape[1],
                        'wall_seconds':time.perf_counter()-tick,'logits_sha256':base.sha256_bytes(base.canonical_json(logits.float().cpu().tolist()))})
                    require_headroom(memory(torch))
        mean=sum(row['wall_seconds'] for row in observations)/len(observations)
        persist('medical-resource-timing.json',{'scope':'RESOURCE_QUALIFICATION_ONLY; NO_SCIENTIFIC_METRIC','domain':domain,'adapter_disabled':True,'sample':observations,'mean_forward_seconds':mean})
        projection=shared.project_workload(timing['wall_seconds'],max(prep['max_prompt_tokens_by_split'].values()),mean)
        persist('workload-projection.json',projection)
        if max(projection['original_256_example_seed_seconds'],projection['c2_training_length_sensitivity_seconds'])>43200:
            raise RuntimeError('KAGGLE_PROJECTED_C1_C2_TRAINING_EXCEEDS_12_HOURS')
        full=projection['c1_training_length_sensitivity_seconds']+projection['c1_or_c2_decision_matrix_length_sensitivity_seconds']
        remaining=admission['observed_remaining_runtime_seconds']
        frozen.require_atomic_duration(full,remaining)
        state.update(status='RESOURCE_QUALIFICATION_MEASURED',projected_complete_c1_seconds=full,
                     resource_only=True,medical_optimizer_steps=0)
    except (Exception,SystemExit) as exc:
        state.update(status='KAGGLE_RESOURCE_BLOCKED',reason=str(exc),exception_type=type(exc).__name__)
    persist('resource-qualification.json',state)
    return state,output


def main():
    parser=argparse.ArgumentParser()
    for name in ('model-dir','source','admission','physical-hardware'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--expected-head',required=True)
    args=parser.parse_args()
    admission=json.loads(args.admission.read_text())
    validate_admission(admission)
    admission['observed_remaining_runtime_seconds']=metadata.validate_admission(admission)
    args.admission.write_text(json.dumps(admission),encoding='utf-8')
    args.intervention='C1_CRDI_V1'
    args.seed=11
    args.retention_source=None
    frozen.colab=sys.modules[__name__]
    result,output=frozen.run(args)
    archive=Path(shutil.make_archive(str(output),'zip',output))
    print(json.dumps({'result':result,'evidence_zip':str(archive),'evidence_zip_sha256':base.sha256_file(archive)},sort_keys=True),flush=True)
    return 0 if result['status']=='ADAPTER_SEED_COMPLETE_DEVELOPMENT' else 2


if __name__=='__main__':
    raise SystemExit(main())
