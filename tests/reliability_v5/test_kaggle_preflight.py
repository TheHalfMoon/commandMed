"""Model-free tests of Kaggle cost, freshness, frozen bytes and GPU exclusion."""
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts'))
import v5_s1_kaggle_preflight as kaggle


def admission():
    return dict(cost_basis='KAGGLE_ZERO_COST_RUNTIME',username='abdulazizshehri',private=True,
                expected_incremental_spend_usd=0,new_purchase=False,scientific_gpu_count=1,
                scientific_device='cuda:0',confirmatory_materialized=False,reserve_materialized=False,
                phi=False,kernel_ref=kaggle.KERNEL,quota_observed_unix=1000,
                free_gpu_seconds_available=100000,requested_session_timeout_seconds=42000)


@pytest.mark.parametrize('key,value', [('private',False),('new_purchase',True),
    ('expected_incremental_spend_usd',1),('scientific_gpu_count',2),('scientific_device','cuda:1'),
    ('confirmatory_materialized',True),('reserve_materialized',True),('phi',True),
    ('username','other'),('free_gpu_seconds_available',float('nan')),
    ('requested_session_timeout_seconds',43201),('quota_observed_unix',True)])
def test_unauthorized_or_missing_admission_blocks(key,value):
    record=admission()
    record[key]=value
    with pytest.raises(RuntimeError):
        kaggle.validate_admission(record,now=1100)


def test_window_and_quota_both_bound_duration_and_stale_observation_blocks():
    record=admission()
    assert kaggle.validate_admission(record,now=1100)==41900
    record['free_gpu_seconds_available']=1800
    assert kaggle.validate_admission(record,now=1100)==1700
    for now in (999,1601):
        with pytest.raises(RuntimeError):
            kaggle.validate_admission(record,now=now)


def test_all_entry_research_and_evidence_bytes_still_match():
    assert kaggle.verify_frozen_bindings()['verified_entry_file_count']==307


def test_second_gpu_is_manifest_metadata_only():
    calls=[]
    cuda=SimpleNamespace(is_available=lambda:True,device_count=lambda:2,
        set_device=lambda device:calls.append(device),current_device=lambda:0,
        get_device_properties=lambda index:SimpleNamespace(name='Tesla T4',total_memory=15360*1024**2),
        get_device_capability=lambda index:(7,5),is_bf16_supported=lambda:True)
    hardware=kaggle.verify_gpu_binding(SimpleNamespace(cuda=cuda))
    assert calls==[0]
    assert hardware[0]['scientific_use'] is True
    assert hardware[1]['scientific_use'] is False


def test_wrong_gpu_or_no_bfloat16_blocks():
    cuda=SimpleNamespace(is_available=lambda:True,device_count=lambda:1,
        set_device=lambda device:None,current_device=lambda:0,
        get_device_properties=lambda index:SimpleNamespace(name='Tesla P100',total_memory=1),
        get_device_capability=lambda index:(6,0),is_bf16_supported=lambda:False)
    with pytest.raises(RuntimeError,match='HARDWARE_MISMATCH'):
        kaggle.verify_gpu_binding(SimpleNamespace(cuda=cuda))
