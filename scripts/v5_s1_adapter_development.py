#!/usr/bin/env python3
"""One complete atomic C1/C2 seed; frozen BF16 final-block LoRA only.

No cross-runtime checkpoint/resume. SQuAD payloads and decoded text never leave
the source VM. This implementation must be reviewed/pushed before model use.
"""
from __future__ import annotations

import argparse
import contextlib
import gc
import json
import math
import shutil
import time
from dataclasses import asdict
from pathlib import Path

import v5_s1_colab_qualification as colab
import v5_s1_b1_development as b1

base = colab.base
SEEDS = (11, 29, 47)
INTERVENTIONS = ('C1_CRDI_V1', 'C2_CRDI_RETAIN_V1')
ACCUMULATION = 8
TRAIN_COUNT = 256
OPTIMIZER_STEPS = TRAIN_COUNT // ACCUMULATION


def maintenance_indices(step: int) -> tuple[int, int]:
    """Two ranked anchors per optimizer step: all 64 once over 32 steps."""
    if not isinstance(step, int) or isinstance(step, bool) or not 0 <= step < OPTIMIZER_STEPS:
        raise ValueError('C2_OPTIMIZER_STEP_OUT_OF_RANGE')
    return (2 * step) % 64, (2 * step + 1) % 64


def require_atomic_duration(projected: float, remaining: float) -> None:
    if not math.isfinite(projected) or projected <= 0 or not math.isfinite(remaining) or projected + 600 > remaining:
        raise RuntimeError('COLAB_RUNTIME_DURATION_BLOCKER')


def full_answer_projection(elapsed: float, generated_tokens: int) -> float:
    if not math.isfinite(elapsed) or elapsed <= 0 or not isinstance(generated_tokens,int) or isinstance(generated_tokens,bool) or not 1 <= generated_tokens <= 32:
        raise RuntimeError('C2_INVALID_RESOURCE_DECODE_OBSERVATION')
    return elapsed * 32 / generated_tokens


def kl_from_logits(torch, teacher, candidate):
    """Mean gold-position teacher KL; same 1e-15 candidate floor as V5 math."""
    p = torch.softmax(teacher.float(), dim=-1)
    log_q = torch.log(torch.softmax(candidate.float(), dim=-1).clamp_min(1e-15))
    log_p = torch.log(torch.where(p > 0, p, torch.ones_like(p)))
    return (p * (log_p - log_q)).sum(dim=-1).mean()


def semantic_js(torch, p, q):
    midpoint = .5 * (p + q)
    log_m = torch.log(midpoint.clamp_min(1e-15))
    log_p = torch.log(torch.where(p > 0, p, torch.ones_like(p)))
    log_q = torch.log(torch.where(q > 0, q, torch.ones_like(q)))
    return .5 * torch.sum(p * (log_p-log_m)) + .5 * torch.sum(q * (log_q-log_m))


def run(args):
    import torch
    from peft import LoraConfig, TaskType, get_peft_model
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from commandmed.reliability_v5 import retention_dataset as retention

    if args.intervention not in INTERVENTIONS or args.seed not in SEEDS:
        raise ValueError('UNFROZEN_ADAPTER_RUN_IDENTITY')
    c2 = args.intervention == 'C2_CRDI_RETAIN_V1'
    if c2 and args.retention_source is None:
        raise ValueError('C2_REQUIRES_EXACT_RETENTION_SOURCE')
    started = time.perf_counter()
    admission = json.loads(args.admission.read_text())
    colab.validate_admission(admission)
    resource, output = colab.qualify(args)
    if resource['status'] != 'RESOURCE_QUALIFICATION_MEASURED':
        return resource, output
    gc.collect()
    torch.cuda.empty_cache()
    result = {'status': 'IN_PROGRESS', 'code_sha': args.expected_head, 'intervention': args.intervention,
              'seed': args.seed, 'complete_matrix': False, 'medical_optimizer_steps': 0,
              'durable_export_verified': False, 'resume': False, 'spend_usd': 0,
              'confirmatory': False, 'reserve': False}
    rows = []
    sampler = base.MemorySampler()
    sampler.start()
    try:
        def require_observed_headroom():
            colab.require_headroom(colab.memory(torch))
            if sampler.min_available < base.MIN_MEMORY_HEADROOM:
                raise RuntimeError('SYSTEM_HEADROOM_BELOW_1_5_GIB')

        tokenizer = AutoTokenizer.from_pretrained(args.model_dir, local_files_only=True)
        qa_metadata, maintenance, evaluation = None, [], []
        if c2:
            import pyarrow.parquet as parquet
            import v5_s1_retention_preparation as preparation
            qa_metadata = preparation.prepare(args.retention_source, args.model_dir)
            base.write_json(output / 'retention-preparation.json', qa_metadata)
            maintenance, evaluation = retention.select_roles(parquet.read_table(args.retention_source).to_pylist())
        projection = json.loads((output / 'workload-projection.json').read_text())
        training_projection = projection['c2_training_length_sensitivity_seconds' if c2 else 'c1_training_length_sensitivity_seconds']
        preliminary_projection = projection['c1_or_c2_decision_matrix_length_sensitivity_seconds'] + training_projection
        remaining = admission['observed_remaining_runtime_seconds'] - (time.perf_counter() - started)
        base.write_json(output / 'adapter-preliminary-duration-admission.json', {'projected_seconds': preliminary_projection,
            'remaining_seconds': remaining, 'retention_cost_unmeasured': c2, 'atomic_seed': args.seed})
        require_atomic_duration(preliminary_projection, remaining)
        prior = json.loads((output / 'environment-manifest.json').read_text())
        config = {'seed': args.seed, 'intervention': args.intervention, 'medical_epochs': 1,
                  'train_count': 256, 'micro_batch_size': 1, 'gradient_accumulation': 8,
                  'optimizer_steps': 32, 'lr': 5e-4, 'weight_decay': 0.0, 'betas': [.9, .999],
                  'eps': 1e-8, 'clip_norm': 1.0, 'contract_weight': .1, 'retention_weight': .1 if c2 else 0,
                  'medical_order': 'CPU_TORCH_GENERATOR_SEEDED_RANDPERM_OF_FROZEN_MATERIALIZATION',
                  'maintenance_schedule': 'TWO_RANKED_ANCHORS_PER_OPTIMIZER_STEP; ALL_64_ONCE' if c2 else None}
        environment = {'resource_environment_sha256': prior['environment_sha256'], 'config': config,
                       'runner_sha256': base.sha256_file(Path(__file__)), 'admission': admission,
                       'retention_metadata_sha256': base.sha256_bytes(base.canonical_json(qa_metadata)) if c2 else None}
        env_sha = base.sha256_bytes(base.canonical_json(environment))
        base.write_json(output / 'adapter-environment.json', {**environment, 'environment_sha256': env_sha})
        counter = 0

        def preflight(action, label, qa=False):
            nonlocal counter
            colab.verify_head(args.expected_head)
            authority = base.DevelopmentAuthority(approved=True, authority_id='COLAB_AUTHORITY_SHA256:'+base.sha256_bytes(base.canonical_json(prior['authority_sha256'])))
            manifest = base.DevelopmentRunManifest(action=action, model_repo=base.MODEL_REPO, model_revision=base.MODEL_REVISION,
                model_artifact_sha256=colab.EXPECTED_BUNDLE, intervention_id=args.intervention,
                data_roles=('SQUAD_RETENTION',) if qa else ('RULE_ORACLE_DEVELOPMENT','RULE_ORACLE_CALIBRATION'),
                code_sha=args.expected_head, environment_id='sha256:'+env_sha,
                output_destination=output.relative_to(base.REPO).as_posix()+'/')
            decision = base.evaluate_development_preflight(manifest, authority)
            counter += 1
            base.write_json(output / f'adapter-preflight-{counter:02d}-{label}.json', {'manifest':asdict(manifest),'authority':asdict(authority),'decision':asdict(decision)})
            if not decision.allowed or decision.state != 'PREFLIGHT_PASS':
                raise RuntimeError('ADAPTER_EXACT_RUN_PREFLIGHT_BLOCKED')
            print(label+'=PREFLIGHT_PASS',flush=True)

        preflight('MODEL_LOAD','load')
        torch.manual_seed(args.seed)
        torch.cuda.manual_seed_all(args.seed)
        load_started = time.perf_counter()
        model = AutoModelForCausalLM.from_pretrained(args.model_dir, local_files_only=True, dtype=torch.bfloat16, low_cpu_mem_usage=True).to('cuda').eval()
        torch.cuda.synchronize()
        base.write_json(output/'adapter-load-observation.json', {'wall_seconds':time.perf_counter()-load_started, **colab.memory(torch)})
        require_observed_headroom()
        if any(p.dtype != torch.bfloat16 for p in model.parameters()):
            raise RuntimeError('ADAPTER_BASE_DTYPE_MISMATCH')
        for p in model.parameters():
            p.requires_grad_(False)
        base_before = b1.parameter_identity(model, torch)
        targets = base.final_block_linear_names(model, torch)
        adapted = get_peft_model(model,LoraConfig(r=4,lora_alpha=8,lora_dropout=0.0,bias='none',target_modules=targets,task_type=TaskType.CAUSAL_LM),autocast_adapter_dtype=False)
        trainable = [(name,p) for name,p in adapted.named_parameters() if p.requires_grad]
        recorded = json.loads((output/'trainable-parameters.json').read_text())
        trainable_record = {'target_modules':targets,'parameters':[{'name':name,'count':p.numel(),'dtype':str(p.dtype)} for name,p in trainable], 'total':sum(p.numel() for _,p in trainable)}
        if trainable_record != recorded or trainable_record['total'] != 100352 or any('lora_' not in name or 'layers.23.' not in name or p.dtype != torch.bfloat16 for name,p in trainable):
            raise RuntimeError('ADAPTER_EXACT_PARAMETER_SCOPE_MISMATCH')
        base.write_json(output/'adapter-trainable-parameters.json',trainable_record)
        frozen_before = [(name,b1.tensor_sha(p,torch)) for name,p in adapted.named_parameters() if not p.requires_grad]
        prep = json.loads((output/'preparation/task-preparation-evidence.json').read_text())
        candidate_ids = [prep['tokenizer_candidate_ids'][x] for x in ('A','B')]
        rules = base.bind_selected_rules(source_bytes=args.source.read_bytes(),selection_manifest=json.loads(base.SELECTION_MANIFEST.read_text()))
        examples = base.materialize_development_examples(rules)
        training = [example for example in examples if example.split=='S1_TRAIN']
        if len(training)!=TRAIN_COUNT:
            raise RuntimeError('ADAPTER_TRAIN_COUNT_MISMATCH')

        def forward(prompt):
            encoded = tokenizer(prompt,return_tensors='pt',add_special_tokens=False).to('cuda')
            if encoded.input_ids.shape[1]>768:
                raise RuntimeError('ADAPTER_MEDICAL_OVER_768_NO_TRUNCATION')
            logits = adapted(**encoded,use_cache=False).logits[0,-1,candidate_ids].float()
            if not bool(torch.isfinite(logits).all()):
                raise RuntimeError('ADAPTER_NONFINITE_MEDICAL_LOGITS')
            return logits

        def anchor_logits(row,teacher):
            prompt=retention.render_prompt(row)
            prompt_ids=tokenizer.encode(prompt,add_special_tokens=False)
            combined=tokenizer.encode(prompt+retention.gold_answers(row)[0],add_special_tokens=False)
            if combined[:len(prompt_ids)] != prompt_ids:
                raise RuntimeError('C2_GOLD_PREFIX_CHANGED')
            gold=combined[len(prompt_ids):][:8]
            if not gold:
                raise RuntimeError('C2_EMPTY_GOLD_ANCHOR')
            ids=torch.tensor([prompt_ids+gold],device='cuda',dtype=torch.long)
            context = adapted.disable_adapter() if teacher else contextlib.nullcontext()
            grad = torch.no_grad() if teacher else contextlib.nullcontext()
            with context,grad:
                all_logits=adapted(input_ids=ids,attention_mask=torch.ones_like(ids),use_cache=False).logits
                logits=all_logits[0,len(prompt_ids)-1:len(prompt_ids)+len(gold)-1,:]
                if not bool(torch.isfinite(logits).all()):
                    raise RuntimeError('C2_NONFINITE_ANCHOR_LOGITS')
                return logits.detach() if teacher else logits

        def decode(row,teacher):
            prompt=retention.render_prompt(row)
            encoded=tokenizer(prompt,return_tensors='pt',add_special_tokens=False).to('cuda')
            context=adapted.disable_adapter() if teacher else contextlib.nullcontext()
            with context,torch.no_grad():
                generated=adapted.generate(**encoded,do_sample=False,num_beams=1,max_new_tokens=32,min_new_tokens=0,
                    repetition_penalty=1.0,use_cache=True,
                    eos_token_id=model.generation_config.eos_token_id,pad_token_id=model.generation_config.pad_token_id)
            completion=generated[0,encoded.input_ids.shape[1]:]
            if completion.numel()>32:
                raise RuntimeError('C2_GENERATION_BOUND_EXCEEDED')
            return tokenizer.decode(completion,skip_special_tokens=True),b1.tensor_sha(completion,torch),completion.numel()

        retention_timing=0.0
        if c2:
            # Identity/length-only selection, fixed before outputs; no score or
            # decoded text used to choose samples or decide admission.
            preflight('INFERENCE','retention-resource',qa=True)
            adapted.eval()
            samples=sorted(evaluation,key=lambda row:(-len(tokenizer.encode(retention.render_prompt(row),add_special_tokens=False)),row['id']))[:4]
            observed=[]
            for row in samples:
                for teacher in (True,False):
                    tick=time.perf_counter()
                    _,digest,generated_count=decode(row,teacher)
                    torch.cuda.synchronize()
                    elapsed=time.perf_counter()-tick
                    observed.append({'source_id':row['id'],'adapter_disabled':teacher,'wall_seconds':elapsed,
                        'generated_tokens':generated_count,'full_32_token_sensitivity_seconds':full_answer_projection(elapsed,generated_count),
                        'raw_token_sha256':digest})
                    require_observed_headroom()
            retention_timing=max(item['full_32_token_sensitivity_seconds'] for item in observed)*512*1.25
            # Measure the longest maintenance teacher/candidate KL backward
            # without an optimizer update. Verify that adapter bytes do not
            # change; resource-only gradients are cleared before real training.
            longest=max(maintenance,key=lambda row:len(tokenizer.encode(retention.render_prompt(row),add_special_tokens=False)))
            preflight('TRAINING','maintenance-resource-backward',qa=True)
            adapter_before=b1.parameter_identity(dict_module(trainable),torch)
            anchor_sampler=base.MemorySampler()
            anchor_sampler.start()
            tick=time.perf_counter()
            try:
                reference=anchor_logits(longest,True)
                candidate=anchor_logits(longest,False)
                anchor_loss=kl_from_logits(torch,reference,candidate)
                if not bool(torch.isfinite(anchor_loss)):
                    raise RuntimeError('C2_RESOURCE_NONFINITE_KL')
                anchor_loss.backward()
                if any(p.grad is None or p.grad.dtype!=torch.bfloat16 or not bool(torch.isfinite(p.grad).all()) for _,p in trainable):
                    raise RuntimeError('C2_RESOURCE_GRADIENT_CONTRACT_FAILURE')
                del reference,candidate,anchor_loss
                adapted.zero_grad(set_to_none=True)
                torch.cuda.synchronize()
            finally:
                anchor_memory=anchor_sampler.stop()
            if anchor_memory['min_system_available_bytes']<base.MIN_MEMORY_HEADROOM:
                raise RuntimeError('C2_RESOURCE_SYSTEM_HEADROOM_BLOCKER')
            require_observed_headroom()
            if b1.parameter_identity(dict_module(trainable),torch)!=adapter_before:
                raise RuntimeError('C2_RESOURCE_CHANGED_ADAPTER_PARAMETER')
            anchor_projection=(time.perf_counter()-tick)*64*1.25
            training_projection+=anchor_projection
            base.write_json(output/'retention-resource-timing.json',{'scope':'RESOURCE_QUALIFICATION_ONLY; NO_SCIENTIFIC_METRIC',
                'selection':'FOUR_LONGEST_EVALUATION_PROMPTS; ID_TIEBREAK','sample':observed,
                'full_paired_decode_projection_seconds':retention_timing,'maintenance_cost_projection_seconds':anchor_projection,
                'maintenance_resource_backward':True,'maintenance_resource_optimizer_steps':0,'maintenance_resource_memory':anchor_memory})
        if training_projection > base.MAX_PROJECTED_SEED_SECONDS:
            raise RuntimeError('PROJECTED_C1_C2_SEED_EXCEEDS_12_HOURS')
        projected=projection['c1_or_c2_decision_matrix_length_sensitivity_seconds']+training_projection+retention_timing
        remaining=admission['observed_remaining_runtime_seconds']-(time.perf_counter()-started)
        base.write_json(output/'adapter-stage-duration-admission.json',{'projected_seconds':projected,'remaining_seconds':remaining,
            'complete_medical_prompts':16384,'medical_optimizer_steps':32,'retention_eval_count':256 if c2 else 0})
        require_atomic_duration(projected,remaining)
        baseline_retention=[]
        baseline_output_hashes=[]
        if c2:
            preflight('INFERENCE','complete-base-retention',qa=True)
            for row in evaluation:
                decoded,digest,_=decode(row,True)
                baseline_retention.append(retention.score_answer(retention.prediction_span(decoded),retention.gold_answers(row)))
                baseline_output_hashes.append({'source_id':row['id'],'raw_token_sha256':digest})
                require_observed_headroom()
        optimizer=torch.optim.AdamW([p for _,p in trainable],lr=5e-4,betas=(.9,.999),eps=1e-8,weight_decay=0.0)
        permutation=torch.randperm(256,generator=torch.Generator().manual_seed(args.seed)).tolist()
        order=[training[index] for index in permutation]
        base.write_json(output/'adapter-training-identities.json',{'medical_task_ids':[item.task_id for item in order],
            'maintenance_ids_by_step':[[maintenance[i]['id'] for i in maintenance_indices(step)] for step in range(32)] if c2 else None})
        preflight('TRAINING','medical-training')
        if c2:
            preflight('TRAINING','maintenance-training',qa=True)
        training_started=time.perf_counter()
        losses=[]
        adapted.train()
        for step in range(32):
            optimizer.zero_grad(set_to_none=True)
            medical_losses=[]
            for example in order[step*8:(step+1)*8]:
                pair=[forward(prompt) for prompt in (example.canonical_prompt,example.transformed_prompt)]
                p,q=[torch.softmax(logits,dim=-1) for logits in pair]
                if example.option_a_semantic!='MATCH':
                    p,q=p.flip(0),q.flip(0)
                target=0 if example.target_label=='A' else 1
                loss=-torch.log(torch.softmax(pair[0],dim=-1)[target].clamp_min(1e-15))+.1*semantic_js(torch,p,q)
                if not bool(torch.isfinite(loss)):
                    raise RuntimeError('ADAPTER_NONFINITE_MEDICAL_LOSS')
                (loss/8).backward()
                medical_losses.append(float(loss.detach().cpu()))
                del pair,p,q,loss
            anchor_losses=[]
            if c2:
                for index in maintenance_indices(step):
                    reference=anchor_logits(maintenance[index],True)
                    candidate=anchor_logits(maintenance[index],False)
                    loss=kl_from_logits(torch,reference,candidate)
                    if not bool(torch.isfinite(loss)):
                        raise RuntimeError('C2_NONFINITE_RETENTION_KL')
                    (.1*loss/2).backward()
                    anchor_losses.append(float(loss.detach().cpu()))
                    del reference,candidate,loss
            if any(p.grad is None or p.grad.dtype!=torch.bfloat16 or not bool(torch.isfinite(p.grad).all()) for _,p in trainable):
                raise RuntimeError('ADAPTER_GRADIENT_CONTRACT_FAILURE')
            norm=torch.nn.utils.clip_grad_norm_([p for _,p in trainable],1.0)
            if not bool(torch.isfinite(norm)):
                raise RuntimeError('ADAPTER_NONFINITE_GRADIENT_NORM')
            optimizer.step()
            result['medical_optimizer_steps']+=1
            if any(p.dtype!=torch.bfloat16 or not bool(torch.isfinite(p).all()) for _,p in trainable):
                raise RuntimeError('ADAPTER_PARAMETER_CONTRACT_FAILURE')
            losses.append({'step':step+1,'mean_medical_loss':sum(medical_losses)/8,
                'mean_retention_kl':sum(anchor_losses)/2 if c2 else None,'unclipped_gradient_norm':float(norm.cpu())})
            require_observed_headroom()
            elapsed_training=time.perf_counter()-training_started
            if elapsed_training > base.MAX_PROJECTED_SEED_SECONDS:
                raise RuntimeError('ACTUAL_C1_C2_SEED_TRAINING_EXCEEDS_12_HOURS')
            remaining=admission['observed_remaining_runtime_seconds']-(time.perf_counter()-started)
            require_atomic_duration(projection['c1_or_c2_decision_matrix_length_sensitivity_seconds']+
                retention_timing/2+(32-step-1)*elapsed_training/(step+1)*1.25,remaining)
            print(f'ADAPTER_TRAIN_PROGRESS={step+1}/32',flush=True)
        base.write_json(output/'adapter-training-observation.json',{'config':config,'losses':losses,'wall_seconds':time.perf_counter()-training_started})
        adapted.eval()
        preflight('INFERENCE','complete-medical-matrix')
        matrix_started=time.perf_counter()
        with torch.no_grad():
            for example in examples:
                for variant,prompt in (('canonical',example.canonical_prompt),('transformed',example.transformed_prompt)):
                    values=forward(prompt).cpu().tolist()
                    rows.append({'task_id':example.task_id,'calculator_id':example.calculator_id,'split':example.split,
                        'variant':variant,'target_index':0 if example.target_label=='A' else 1,
                        'option_a_semantic':example.option_a_semantic,'prompt_sha256':base.sha256_bytes(prompt.encode()),'logits':values})
                    require_observed_headroom()
                    if len(rows)%128==0:
                        elapsed=time.perf_counter()-matrix_started
                        print(f'ADAPTER_MATRIX_PROGRESS={len(rows)}/16384; WALL_SECONDS={elapsed:.3f}',flush=True)
                        remaining=admission['observed_remaining_runtime_seconds']-(time.perf_counter()-started)
                        if len(rows)<16384:
                            require_atomic_duration((16384-len(rows))*elapsed/len(rows)*1.25+retention_timing/2,remaining)
        raw_sha=base.write_json(output/'adapter-decision-matrix.json',{'complete':True,'intervention':args.intervention,'seed':args.seed,'rows':rows})
        analysis_sha=base.write_json(output/'adapter-analysis.json',b1.analyze_rows(rows))
        if c2:
            preflight('INFERENCE','complete-candidate-retention',qa=True)
            candidate_retention=[]
            candidate_output_hashes=[]
            for row in evaluation:
                decoded,digest,_=decode(row,False)
                candidate_retention.append(retention.score_answer(retention.prediction_span(decoded),retention.gold_answers(row)))
                candidate_output_hashes.append({'source_id':row['id'],'raw_token_sha256':digest})
                require_observed_headroom()
            def averages(items):
                return {'exact_match':sum(x[0] for x in items)/256,'token_f1':sum(x[1] for x in items)/256,'count':256}
            # Persist only IDs/hashes and aggregate scores, never per-item QA
            # predictions, answers, question/passages or per-item score arrays.
            baseline_metrics,candidate_metrics=averages(baseline_retention),averages(candidate_retention)
            base.write_json(output/'paired-retention-aggregate.json',{'scope':'PAIRED_SQUAD_V1_1_ONLY; NOT_GENERAL_CAPABILITY_PRESERVATION',
                'baseline':baseline_metrics,'candidate':candidate_metrics,
                'paired_mean_delta':{key:candidate_metrics[key]-baseline_metrics[key] for key in ('exact_match','token_f1')},
                'source_ids':[row['id'] for row in evaluation],'metadata_sha256':environment['retention_metadata_sha256'],
                'baseline_raw_output_aggregate_sha256':base.sha256_bytes(base.canonical_json(baseline_output_hashes)),
                'candidate_raw_output_aggregate_sha256':base.sha256_bytes(base.canonical_json(candidate_output_hashes)),
                'scorer_git_blob':retention.OFFICIAL_V1_SCORER_PORT_GIT_BLOB,'prompt_template_sha256':qa_metadata['prompt_template_sha256'],
                'max_new_tokens':32,'greedy':True,'truncation':False})
        frozen_after=[(name,b1.tensor_sha(p,torch)) for name,p in adapted.named_parameters() if not p.requires_grad]
        if frozen_after!=frozen_before or result['medical_optimizer_steps']!=32 or len(rows)!=16384:
            raise RuntimeError('ADAPTER_BASE_CHANGED_OR_INCOMPLETE_SEED')
        result.update(status='ADAPTER_SEED_COMPLETE_DEVELOPMENT',complete_matrix=True,prompt_count=len(rows),
            base_identity_before_adapter_insertion=base_before,frozen_parameter_identity_before=base.sha256_bytes(base.canonical_json(frozen_before)),
            frozen_parameter_identity_after=base.sha256_bytes(base.canonical_json(frozen_after)),
            adapter_parameter_identity=b1.parameter_identity(dict_module(trainable),torch),
            raw_output_sha256=raw_sha,analysis_sha256=analysis_sha,
            wall_seconds=time.perf_counter()-started,memory=colab.memory(torch),retention_evaluated=c2)
    except KeyboardInterrupt:
        result.update(status='RUNTIME_INTERRUPTION',reason='INTERACTIVE_EXECUTION_INTERRUPTED')
    except (Exception,SystemExit) as exc:
        result.update(status='ADAPTER_SEED_BLOCKED',reason=str(exc),exception_type=type(exc).__name__)
    finally:
        result['memory_sampling']=sampler.stop()
        if result['memory_sampling']['min_system_available_bytes']<base.MIN_MEMORY_HEADROOM:
            result.update(status='ADAPTER_SEED_BLOCKED',reason='SYSTEM_HEADROOM_BELOW_1_5_GIB')
    if result['status']!='ADAPTER_SEED_COMPLETE_DEVELOPMENT' and rows:
        base.write_json(output/'incomplete-adapter-decision-matrix.json',{'complete':False,'rows':rows})
    base.write_json(output/'adapter-seed-result.json',result)
    return result,output


class dict_module:
    """Small identity-only view; does not own, mutate or execute parameters."""
    def __init__(self, parameters):
        self.parameters=parameters

    def named_parameters(self):
        return iter(self.parameters)


def main():
    parser=argparse.ArgumentParser()
    for name in ('model-dir','source','admission'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--retention-source',type=Path)
    parser.add_argument('--expected-head',required=True)
    parser.add_argument('--intervention',choices=INTERVENTIONS,required=True)
    parser.add_argument('--seed',type=int,choices=SEEDS,required=True)
    args=parser.parse_args()
    result,output=run(args)
    archive=shutil.make_archive(str(output),'zip',output)
    print(json.dumps({'result':result,'evidence_zip':archive,'evidence_zip_sha256':base.sha256_file(Path(archive))},sort_keys=True),flush=True)
    return 0 if result['status']=='ADAPTER_SEED_COMPLETE_DEVELOPMENT' else 2


if __name__=='__main__':
    raise SystemExit(main())
