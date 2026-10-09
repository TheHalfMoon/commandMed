#!/usr/bin/env python3
"""Official private Kaggle script bootstrap for metadata-only S1 qualification.

No model load, inference or training. Credentials are never sent to this VM.
Only the allowlisted evidence archive is placed in Kaggle's exported directory.
"""
import importlib.metadata
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(expected_head: str, admission: dict) -> int:
    if not re.fullmatch('[0-9a-f]{40}',expected_head):
        raise ValueError('EXACT_GIT_HEAD_REQUIRED')
    if admission.get('private') is not True or admission.get('scientific_device')!='cuda:0':
        raise ValueError('PRIVATE_SINGLE_GPU_ADMISSION_REQUIRED')
    output=Path('/kaggle/working')
    workspace=Path(tempfile.mkdtemp(prefix='commandmed-qualification-'))
    repo=workspace/'repo'
    result={'status':'KAGGLE_BOOTSTRAP_IN_PROGRESS','expected_head':expected_head,
            'model_loaded':False,'model_inference':False,'training':False,'spend_usd':0}
    os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN']='1'
    try:
        import torch
        runtime={'python':sys.version,'torch':torch.__version__,'cuda':torch.version.cuda,
                 'cuda_available':torch.cuda.is_available(),'cuda_device_count':torch.cuda.device_count(),
                 'visible_gpus':[{'index':index,'name':torch.cuda.get_device_name(index),
                    'total_memory_bytes':torch.cuda.get_device_properties(index).total_memory}
                    for index in range(torch.cuda.device_count())],
                 'scientific_gpu_count':1,'scientific_device':'cuda:0',
                 'bfloat16_support':torch.cuda.is_bf16_supported() if torch.cuda.is_available() else False}
        (output/'commandmed-initial-runtime.json').write_text(json.dumps(runtime,indent=2,sort_keys=True)+'\n',encoding='utf-8')
        subprocess.run(['git','clone','--single-branch','--branch','research/commandmed-paper-first-principles',
                        'https://github.com/TheHalfMoon/commandMed.git',str(repo)],check=True)
        actual=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
        if actual!=expected_head:
            raise RuntimeError('KAGGLE_BOOTSTRAP_LIVE_HEAD_MISMATCH')
        torch_before=importlib.metadata.version('torch')
        # These are previously used public implementation versions, selected
        # before outputs. Preserve Kaggle's supplied torch/CUDA installation.
        subprocess.run([sys.executable,'-m','pip','install','--disable-pip-version-check',
                        'transformers==5.18.0','tokenizers==0.23.2','peft==0.21.2','psutil==7.1.0',
                        'safetensors==0.8.0','huggingface-hub==1.33.0'],check=True)
        if importlib.metadata.version('torch')!=torch_before:
            raise RuntimeError('KAGGLE_SUPPLIED_TORCH_CHANGED_DURING_DEPENDENCY_SETUP')
        admission_path=workspace/'admission.json'
        admission_path.write_text(json.dumps(admission),encoding='utf-8')
        command=[sys.executable,str(repo/'scripts/v5_s1_kaggle_preflight.py'),
                 '--expected-head',expected_head,'--admission',str(admission_path),
                 '--model-dir',str(workspace/'model'),'--source',str(workspace/'riskcalcs.json')]
        process=subprocess.run(command)
        archive=repo/'artifacts/v5/development/s1-kaggle-preflight/seed-11.zip'
        if archive.is_file():
            shutil.copyfile(archive,output/'commandmed-kaggle-preflight.zip')
        result.update(status='KAGGLE_QUALIFICATION_FINISHED',exit_code=process.returncode,
                      torch_before=torch_before,torch_after=importlib.metadata.version('torch'),
                      exported_archive=archive.is_file())
    except Exception as exc:
        result.update(status='KAGGLE_BOOTSTRAP_BLOCKED',reason=str(exc),exception_type=type(exc).__name__)
    finally:
        (output/'commandmed-bootstrap-result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
        print(json.dumps(result,sort_keys=True),flush=True)
    return 0 if result.get('exit_code')==0 else 2


if __name__=='__main__':
    raise SystemExit(run(os.environ['COMMANDMED_EXPECTED_HEAD'],json.loads(os.environ['COMMANDMED_ADMISSION_JSON'])))
