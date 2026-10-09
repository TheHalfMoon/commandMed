#!/usr/bin/env python3
"""Verify immutable development exports without importing a model runtime.

This verifies recorded evidence and deterministic analysis, not model execution,
tensor identities from weights, scientific replication, or clinical validity.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import stat
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parent))
import v5_s1_b1_development as b1
import v5_s1_adapter_development as frozen_adapter
import v5_s1_colab_qualification as shared
from commandmed.reliability_v5 import retention_dataset as retention

base = shared.base
PACKET = shared.PACKET.relative_to(base.REPO).as_posix()
CORE = {
    'adapter-analysis.json', 'adapter-decision-matrix.json', 'adapter-environment.json',
    'adapter-load-observation.json',
    'adapter-preflight-01-load.json', 'adapter-preflight-02-retention-resource.json',
    'adapter-preflight-03-maintenance-resource-backward.json',
    'adapter-preflight-04-complete-base-retention.json',
    'adapter-preflight-05-medical-training.json',
    'adapter-preflight-06-maintenance-training.json',
    'adapter-preflight-07-complete-medical-matrix.json',
    'adapter-preflight-08-complete-candidate-retention.json',
    'adapter-preliminary-duration-admission.json', 'adapter-seed-result.json',
    'adapter-stage-duration-admission.json', 'adapter-trainable-parameters.json',
    'adapter-training-identities.json', 'adapter-training-observation.json',
    'benchmark-timing.json', 'environment-before-imports.json', 'environment-manifest.json',
    'frozen-bindings.json', 'hardware-manifest.json', 'kaggle-preflight-result.json',
    'load-observation.json', 'medical-resource-timing.json', 'model-artifact-manifest.json',
    'paired-retention-aggregate.json', 'preflight-model-load.json',
    'resource-preflight-inference.json', 'resource-preflight-medical-resource-timing.json',
    'resource-preflight-model_load.json', 'resource-preflight-training.json',
    'resource-qualification.json', 'retention-preparation-preload.json',
    'retention-preparation.json', 'retention-resource-timing.json', 'smoke-inference.json',
    'timed-step.json', 'trainable-parameters.json', 'warmup-step.json',
    'workload-projection.json', 'preparation/task-preparation-evidence.json',
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def strict_json(data):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, 'DUPLICATE_JSON_KEY')
            result[key] = value
        return result
    return json.loads(data, object_pairs_hook=pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError('NONFINITE_JSON')))


def archive_members(path):
    """Check member safety before reading; never extract untrusted paths."""
    payloads, seen = {}, set()
    with zipfile.ZipFile(path) as archive:
        require(len(archive.infolist()) <= 100, 'EXCESSIVE_ARCHIVE_MEMBERS')
        require(sum(item.file_size for item in archive.infolist()) <= 32 * 1024**2,
                'EXCESSIVE_ARCHIVE_SIZE')
        for item in archive.infolist():
            name = item.filename
            parts = PurePosixPath(name).parts
            require(name and '\\' not in name and ':' not in name and not name.startswith('/')
                    and '..' not in parts and '.' not in parts and '\x00' not in name,
                    'UNSAFE_ARCHIVE_MEMBER')
            require(name.casefold() not in seen, 'DUPLICATE_ARCHIVE_MEMBER')
            seen.add(name.casefold())
            require(not stat.S_ISLNK(item.external_attr >> 16), 'ARCHIVE_SYMLINK')
            if item.is_dir():
                require(name == 'preparation/', 'UNEXPECTED_ARCHIVE_DIRECTORY')
                continue
            require(name in CORE, 'NON_ALLOWLISTED_ARCHIVE_MEMBER:' + name)
            payloads[name] = archive.read(item)  # zipfile validates each CRC.
        require(archive.testzip() is None, 'ARCHIVE_CRC_FAILURE')
    require(set(payloads) == CORE, 'INCOMPLETE_C2_EXPORT')
    return payloads


def git_bytes(head, path):
    return subprocess.check_output(['git', '-C', str(base.REPO), 'show', head + ':' + path])


def close(actual, expected, path='analysis'):
    if isinstance(expected, dict):
        require(isinstance(actual, dict) and set(actual) == set(expected), path + ':KEYS')
        for key in expected:
            close(actual[key], expected[key], path + '/' + key)
    elif isinstance(expected, float):
        require(type(actual) in (float, int) and math.isfinite(actual)
                and abs(actual - expected) <= 1e-12, path + ':METRIC')
    else:
        require(type(actual) is type(expected) and actual == expected, path + ':VALUE')


def verify(archive, runtime, hardware, source, retention_source, expected_head, seed, kernel, version):
    require(re.fullmatch('[0-9a-f]{40}', expected_head) and type(seed) is int
            and seed in (11, 29, 47) and type(version) is int and version > 0,
            'INVALID_VERIFICATION_IDENTITY')
    payloads = archive_members(archive)
    records = {name: strict_json(data) for name, data in payloads.items()}
    forbidden_retention_keys = {'context', 'question', 'answers', 'answer', 'decoded',
                                'prediction', 'predictions', 'gold', 'gold_answer',
                                'gold_answers', 'passage'}
    def reject_retention_payload(value, path='root'):
        if isinstance(value, dict):
            for key, item in value.items():
                require(key.casefold() not in forbidden_retention_keys,
                        'FORBIDDEN_RETENTION_PAYLOAD_KEY:' + path + '/' + key)
                reject_retention_payload(item, path + '/' + key)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                reject_retention_payload(item, path + '/' + str(index))
    for name in ('retention-preparation-preload.json', 'retention-preparation.json',
                 'retention-resource-timing.json', 'paired-retention-aggregate.json'):
        reject_retention_payload(records[name], name)
    result = records['adapter-seed-result.json']
    env = records['environment-manifest.json']
    adapter_env = records['adapter-environment.json']
    raw = records['adapter-decision-matrix.json']
    require(result['status'] == 'ADAPTER_SEED_COMPLETE_DEVELOPMENT'
            and result['code_sha'] == expected_head and result['seed'] == seed
            and result['intervention'] == 'C2_CRDI_RETAIN_V1' and result['complete_matrix'] is True
            and result['prompt_count'] == 16384 and result['medical_optimizer_steps'] == 32
            and result['durable_export_verified'] is False and result['retention_evaluated'] is True
            and result['baseline_retention_completed'] == 256
            and result['candidate_retention_completed'] == 256,
            'INCOMPLETE_OR_WRONG_SEED')
    for key in ('confirmatory', 'reserve', 'resume'):
        require(result[key] is False, 'FORBIDDEN_EXECUTION_FLAG')
    require(result['spend_usd'] == 0, 'NONZERO_SPEND')
    exported = strict_json(runtime.read_bytes())
    physical = strict_json(hardware.read_bytes())
    require(exported['status'] == 'ATOMIC_KERNEL_FINISHED' and exported['exit_code'] == 0
            and exported['expected_head'] == expected_head and exported['seed'] == seed
            and exported['intervention'] == 'C2_CRDI_RETAIN_V1' and exported['exported_archive'] is True
            and exported['scientific_gpu_count'] == 1 and exported['scientific_device'] == 'cuda:0'
            and exported['spend_usd'] == 0 and exported['resume'] is False
            and exported['retention_repo'] == retention.SOURCE_REPO
            and exported['retention_revision'] == retention.SOURCE_REVISION
            and exported['retention_file'] == retention.SOURCE_FILE
            and exported['retention_source_sha256'] == retention.SOURCE_FILE_SHA256
            and exported['retention_source_payload_exported'] is False, 'RUNTIME_RESULT_MISMATCH')
    require(physical == env['physical_hardware'] and physical['cuda_device_count'] == 2
            and physical['visible_gpus'][0]['scientific_use'] is True
            and physical['visible_gpus'][1]['scientific_use'] is False, 'PHYSICAL_GPU_BINDING')
    require(env['scientific_gpu_count'] == 1 and env['scientific_device'] == 'cuda:0'
            and env['cuda_visible_devices'] == '0' and len(env['visible_gpus']) == 1
            and env['runtime_dtype'] == 'bfloat16', 'SCIENTIFIC_DEVICE_OR_DTYPE')
    for record in (env, adapter_env):
        body = {key: value for key, value in record.items() if key != 'environment_sha256'}
        require(digest(base.canonical_json(body)) == record['environment_sha256'], 'ENVIRONMENT_HASH')
    require(adapter_env['resource_environment_sha256'] == env['environment_sha256'], 'ENVIRONMENT_CHAIN')
    for key, path in [('runner_sha256', 'scripts/v5_s1_kaggle_c2_preflight.py'),
                      ('runtime_backend_sha256', 'scripts/v5_s1_kaggle_c2_adapter_development.py'),
                      ('original_adapter_runner_sha256', 'scripts/v5_s1_adapter_development.py')]:
        require(env[key] == digest(git_bytes(expected_head, path)), 'RUN_SOURCE_BINDING:' + path)
    require(adapter_env['runner_sha256'] == env['original_adapter_runner_sha256'], 'ADAPTER_SOURCE_BINDING')
    require(set(env['authority_sha256']) == set(shared.AUTHORITY_FILES) |
            {'V5_S1_KAGGLE_RUNTIME_AMENDMENT_2026-10-08.md'}, 'AUTHORITY_INVENTORY')
    for name, identity in env['authority_sha256'].items():
        require(identity == digest(git_bytes(expected_head, PACKET + '/' + name)), 'AUTHORITY_BINDING:' + name)
    binding_path = PACKET + '/V5_S1_KAGGLE_RUNTIME_AMENDMENT_BINDINGS_2026-10-08.json'
    binding_bytes = git_bytes(expected_head, binding_path)
    bindings = strict_json(binding_bytes)
    for row in bindings['unchanged_entry_files']:
        require(digest(git_bytes(expected_head, row['path'])) == row['sha256'], 'FROZEN_ENTRY_BINDING')
    require(env['frozen_bindings'] == records['frozen-bindings.json']
            and env['frozen_bindings']['binding_sha256'] == digest(binding_bytes)
            and env['frozen_bindings']['verified_entry_file_count'] == len(bindings['unchanged_entry_files']),
            'FROZEN_BINDING_CHAIN')
    tree = subprocess.check_output(['git', '-C', str(base.REPO), 'show', '-s', '--format=%T', expected_head], text=True).strip()
    admission = env['admission']
    require(admission == adapter_env['admission'] and admission['code_sha'] == expected_head
            and admission['git_tree'] == tree and admission['kernel_ref'] == kernel
            and admission['seed'] == seed and admission['private'] is True
            and admission['intervention'] == 'C2_CRDI_RETAIN_V1' and admission['resume'] is False
            and admission['retention_repo'] == retention.SOURCE_REPO
            and admission['retention_revision'] == retention.SOURCE_REVISION
            and admission['retention_file'] == retention.SOURCE_FILE
            and admission['retention_source_sha256'] == retention.SOURCE_FILE_SHA256
            and admission['expected_incremental_spend_usd'] == 0
            and admission['new_purchase'] is False and admission['pay_to_scale_enabled'] is False,
            'ADMISSION_BINDING')
    artifact = records['model-artifact-manifest.json']
    reference = strict_json(git_bytes(expected_head, 'artifacts/v5/development/s1-resource-qualification/model-artifact-manifest.json'))
    require(artifact == reference and artifact['bundle_sha256'] == shared.EXPECTED_BUNDLE
            and digest(base.canonical_json(artifact['files'])) == shared.EXPECTED_BUNDLE
            and artifact['repo'] == base.MODEL_REPO and artifact['revision'] == base.MODEL_REVISION,
            'EXACT_MODEL_MANIFEST_BINDING')
    prep = records['preparation/task-preparation-evidence.json']
    frozen_prep = strict_json(git_bytes(expected_head, 'artifacts/v5/development/s1_task_preparation/task-preparation-evidence.json'))
    require({k: v for k, v in prep.items() if k != 'code_sha'} ==
            {k: v for k, v in frozen_prep.items() if k != 'code_sha'} and prep['code_sha'] == expected_head,
            'FROZEN_PREPARATION_BINDING')
    require(env['preparation_sha256'] == digest(payloads['preparation/task-preparation-evidence.json'])
            and env['tokenizer_files'] == prep['tokenizer_files']
            and all(env['packages'][k] == v for k, v in prep['tokenizer_packages'].items()), 'TOKENIZER_BINDING')
    require(digest(retention_source.read_bytes()) == retention.SOURCE_FILE_SHA256,
            'RETENTION_SOURCE_FILE_HASH')
    retention_preload = records['retention-preparation-preload.json']
    retention_run = records['retention-preparation.json']
    require(retention_preload == retention_run, 'RETENTION_PRELOAD_RUN_METADATA_DRIFT')
    require(retention_run['status'] == 'PASS_RETENTION_METADATA_ONLY'
            and retention_run['code_sha'] == expected_head
            and retention_run['source_repo'] == retention.SOURCE_REPO
            and retention_run['source_revision'] == retention.SOURCE_REVISION
            and retention_run['source_file'] == retention.SOURCE_FILE
            and retention_run['source_file_sha256'] == retention.SOURCE_FILE_SHA256
            and retention_run['source_count'] == 10570
            and len(retention_run['roles']['S1_C2_MAINTENANCE']) == 64
            and len(retention_run['roles']['S1_RETENTION_EVAL']) == 256
            and retention_run['max_prompt_tokens'] > 0
            and retention_run['maximum_answer_tokens'] == 32
            and retention_run['maintenance_first_gold_annotation_max_tokens'] == 8
            and retention_run['truncation'] is False
            and retention_run['source_payload_exported'] is False
            and retention_run['model_loaded'] is False
            and retention_run['model_inference'] is False
            and retention_run['training'] is False,
            'RETENTION_METADATA_IDENTITY')
    import pyarrow.parquet as parquet
    maintenance, evaluation = retention.select_roles(parquet.read_table(retention_source).to_pylist())
    maintenance_ids = [row['id'] for row in maintenance]
    evaluation_ids = [row['id'] for row in evaluation]
    require([row['source_id'] for row in retention_run['roles']['S1_C2_MAINTENANCE']] == maintenance_ids
            and [row['source_id'] for row in retention_run['roles']['S1_RETENTION_EVAL']] == evaluation_ids,
            'RETENTION_ROLE_IDENTITY')
    require(adapter_env['retention_metadata_sha256'] == digest(base.canonical_json(retention_run))
            and env['retention_metadata_sha256'] == digest(base.canonical_json(retention_preload))
            and env['retention_source']['repo'] == retention.SOURCE_REPO
            and env['retention_source']['revision'] == retention.SOURCE_REVISION
            and env['retention_source']['file'] == retention.SOURCE_FILE
            and env['retention_source']['sha256'] == retention.SOURCE_FILE_SHA256
            and env['retention_source']['source_payload_exported'] is False,
            'RETENTION_ENVIRONMENT_BINDING')
    rules = base.bind_selected_rules(source_bytes=source.read_bytes(), selection_manifest=
                                    strict_json(git_bytes(expected_head, PACKET + '/riskcalcs-rule-oracle-final-candidate-v5.json')))
    examples = base.materialize_development_examples(rules)
    require(raw['complete'] is True and raw['seed'] == seed and raw['intervention'] == 'C2_CRDI_RETAIN_V1'
            and len(raw['rows']) == 16384, 'RAW_MATRIX_IDENTITY')
    identities = []
    for example in examples:
        for variant, prompt in [('canonical', example.canonical_prompt), ('transformed', example.transformed_prompt)]:
            identities.append({'task_id': example.task_id, 'calculator_id': example.calculator_id,
                'split': example.split, 'variant': variant, 'target_index': 0 if example.target_label == 'A' else 1,
                'option_a_semantic': example.option_a_semantic, 'prompt_sha256': digest(prompt.encode())})
    for expected, row in zip(identities, raw['rows'], strict=True):
        require({k: v for k, v in row.items() if k != 'logits'} == expected, 'ORDERED_TASK_CASE_PROMPT_IDENTITY')
        require(isinstance(row['logits'], list) and len(row['logits']) == 2
                and all(type(x) in (float, int) and math.isfinite(x) for x in row['logits']), 'NONFINITE_OR_INVALID_LOGITS')
    require(result['raw_output_sha256'] == digest(payloads['adapter-decision-matrix.json'])
            and result['analysis_sha256'] == digest(payloads['adapter-analysis.json']), 'RAW_ANALYSIS_HASH')
    regenerated = b1.analyze_rows(raw['rows'])
    close(records['adapter-analysis.json'], regenerated)
    config = {'seed': seed, 'intervention': 'C2_CRDI_RETAIN_V1', 'medical_epochs': 1,
              'train_count': 256, 'micro_batch_size': 1, 'gradient_accumulation': 8,
              'optimizer_steps': 32, 'lr': 5e-4, 'weight_decay': 0.0, 'betas': [.9, .999],
              'eps': 1e-8, 'clip_norm': 1.0, 'contract_weight': .1, 'retention_weight': .1,
              'medical_order': 'CPU_TORCH_GENERATOR_SEEDED_RANDPERM_OF_FROZEN_MATERIALIZATION',
              'maintenance_schedule': 'TWO_RANKED_ANCHORS_PER_OPTIMIZER_STEP; ALL_64_ONCE'}
    training = records['adapter-training-observation.json']
    require(adapter_env['config'] == config and training['config'] == config and training['complete'] is True
            and len(training['losses']) == 32, 'FROZEN_OPTIMIZER_CONFIG')
    for index, row in enumerate(training['losses'], 1):
        require(row['step'] == index and type(row['mean_retention_kl']) in (int, float)
                and math.isfinite(row['mean_retention_kl'])
                and all(type(row[k]) in (int, float) and math.isfinite(row[k])
                        for k in ('mean_medical_loss', 'unclipped_gradient_norm')), 'TRAINING_HISTORY')
    trained = records['adapter-training-identities.json']
    train_ids = {item.task_id for item in examples if item.split == 'S1_TRAIN'}
    require(len(trained['medical_task_ids']) == 256 and set(trained['medical_task_ids']) == train_ids
            and isinstance(trained['maintenance_ids_by_step'], list)
            and len(trained['maintenance_ids_by_step']) == 32, 'TRAINING_IDENTITY_SET')
    expected_maintenance = [[maintenance_ids[i] for i in frozen_adapter.maintenance_indices(step)]
                            for step in range(32)]
    require(trained['maintenance_ids_by_step'] == expected_maintenance,
            'C2_MAINTENANCE_SCHEDULE_IDENTITY')
    retention_timing = records['retention-resource-timing.json']
    require(retention_timing['scope'] == 'RESOURCE_QUALIFICATION_ONLY; NO_SCIENTIFIC_METRIC'
            and retention_timing['selection'] == 'FOUR_LONGEST_EVALUATION_PROMPTS; ID_TIEBREAK'
            and len(retention_timing['sample']) == 8
            and retention_timing['maintenance_resource_backward'] is True
            and retention_timing['maintenance_resource_optimizer_steps'] == 0
            and all(row['source_id'] in set(evaluation_ids)
                    and type(row['adapter_disabled']) is bool
                    and type(row['wall_seconds']) in (int, float) and math.isfinite(row['wall_seconds'])
                    and row['wall_seconds'] > 0
                    and type(row['generated_tokens']) is int and 0 <= row['generated_tokens'] <= 32
                    and re.fullmatch('[0-9a-f]{64}', row['raw_token_sha256'])
                    for row in retention_timing['sample']),
            'RETENTION_RESOURCE_TIMING_BINDING')
    paired = records['paired-retention-aggregate.json']
    require(paired['scope'] == 'PAIRED_SQUAD_V1_1_ONLY; NOT_GENERAL_CAPABILITY_PRESERVATION'
            and paired['source_ids'] == evaluation_ids
            and paired['metadata_sha256'] == adapter_env['retention_metadata_sha256']
            and paired['scorer_git_blob'] == retention.OFFICIAL_V1_SCORER_PORT_GIT_BLOB
            and paired['prompt_template_sha256'] == retention_run['prompt_template_sha256']
            and paired['max_new_tokens'] == 32 and paired['greedy'] is True
            and paired['truncation'] is False,
            'PAIRED_RETENTION_BINDING')
    for role in ('baseline', 'candidate'):
        metrics = paired[role]
        require(metrics['count'] == 256
                and all(type(metrics[k]) in (int, float) and math.isfinite(metrics[k])
                        and 0 <= metrics[k] <= 1 for k in ('exact_match', 'token_f1')),
                'PAIRED_RETENTION_METRICS')
    for key in ('exact_match', 'token_f1'):
        require(type(paired['paired_mean_delta'][key]) in (int, float)
                and math.isfinite(paired['paired_mean_delta'][key])
                and abs(paired['paired_mean_delta'][key]
                        - (paired['candidate'][key] - paired['baseline'][key])) <= 1e-12,
                'PAIRED_RETENTION_DELTA')
    require(result['baseline_retention_raw_output_aggregate_sha256']
            == paired['baseline_raw_output_aggregate_sha256']
            and result['candidate_retention_raw_output_aggregate_sha256']
            == paired['candidate_raw_output_aggregate_sha256'],
            'RETENTION_RAW_OUTPUT_AGGREGATE_BINDING')
    require(records['adapter-trainable-parameters.json'] == records['trainable-parameters.json']
            and records['trainable-parameters.json']['total'] == 100352
            and all('lora_' in row['name'] and 'layers.23.' in row['name'] and row['dtype'] == 'torch.bfloat16'
                    for row in records['trainable-parameters.json']['parameters']), 'ADAPTER_SCOPE')
    require(result['frozen_parameter_identity_before'] == result['frozen_parameter_identity_after'], 'BASE_CHANGED')
    for key in ('frozen_parameter_identity_before', 'adapter_parameter_identity', 'base_identity_before_adapter_insertion'):
        require(re.fullmatch('[0-9a-f]{64}', result[key]), 'TENSOR_IDENTITY_RECORD')
    for name in CORE:
        if name.startswith('adapter-preflight-'):
            record = records[name]
            require(record['decision']['allowed'] is True and record['decision']['state'] == 'PREFLIGHT_PASS'
                    and record['manifest']['code_sha'] == expected_head
                    and record['manifest']['environment_id'] == 'sha256:' + adapter_env['environment_sha256']
                    and record['manifest']['model_repo'] == base.MODEL_REPO
                    and record['manifest']['model_revision'] == base.MODEL_REVISION
                    and record['manifest']['model_artifact_sha256'] == shared.EXPECTED_BUNDLE
                    and record['manifest']['intervention_id'] == 'C2_CRDI_RETAIN_V1', 'ACTION_PREFLIGHT')
    for name in ('adapter-preliminary-duration-admission.json', 'adapter-stage-duration-admission.json'):
        duration = records[name]
        require(all(type(duration[k]) in (int, float) and math.isfinite(duration[k]) and duration[k] > 0
                    for k in ('projected_seconds', 'remaining_seconds'))
                and duration['projected_seconds'] + 600 <= duration['remaining_seconds'], 'ATOMIC_DURATION_ADMISSION')
    require(records['kaggle-preflight-result.json']['status'] == 'KAGGLE_C2_PREFLIGHT_PASS'
            and records['resource-qualification.json']['status'] == 'RESOURCE_QUALIFICATION_MEASURED',
            'FRESH_RUNTIME_GATES')
    return {'schema': 'commandmed.v5.adapter-export-verification.v1',
        'verified_at': datetime.now(timezone.utc).isoformat(), 'status': 'PASS_MODEL_FREE_C2_EXPORT_VERIFICATION',
        'verification_type': 'EVIDENCE_VERIFICATION_NOT_SCIENTIFIC_REPLICATION',
        'kernel_ref': kernel, 'kernel_version': version, 'run_head': expected_head, 'run_tree': tree,
        'seed': seed, 'intervention': 'C2_CRDI_RETAIN_V1', 'archive_sha256': digest(archive.read_bytes()),
        'archive_bytes': archive.stat().st_size, 'safe_unique_members_crc': True,
        'files': [{'path': name, 'bytes': len(data), 'sha256': digest(data)} for name, data in sorted(payloads.items())],
        'allowlisted_runtime_sha256': digest(runtime.read_bytes()), 'physical_hardware_sha256': digest(hardware.read_bytes()),
        'ordered_medical_rows_verified': 16384, 'ordered_case_task_legend_target_split_prompt_verified': True,
        'analysis_reproduced_absolute_tolerance': 1e-12, 'durable_export_verified': True,
        'original_payload_flags_unchanged': True, 'model_weights_loaded': False,
        'training_order_rng_reexecuted': False, 'training_identity_set_verified': True,
        'tensor_hashes_verified_as_recorded_bindings_only': True, 'clinical_validity': False,
        'confirmatory': False, 'reserve': False, 'spend_usd': 0,
        'retention_evaluated': True, 'retention_rows_verified': 256,
        'retention_source_sha256': retention.SOURCE_FILE_SHA256}


def main():
    parser = argparse.ArgumentParser()
    for name in ('archive', 'runtime', 'hardware', 'source', 'retention-source', 'receipt'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--expected-head', required=True)
    parser.add_argument('--seed', type=int, required=True)
    parser.add_argument('--kernel', required=True)
    parser.add_argument('--version', type=int, required=True)
    args = parser.parse_args()
    receipt = verify(args.archive, args.runtime, args.hardware, args.source, args.retention_source,
                     args.expected_head, args.seed, args.kernel, args.version)
    base.write_json(args.receipt, receipt)
    print(json.dumps({'status': receipt['status'], 'archive_sha256': receipt['archive_sha256'],
                      'rows': receipt['ordered_medical_rows_verified']}, sort_keys=True))


if __name__ == '__main__':
    main()
