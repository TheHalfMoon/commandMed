"""Scientific-role separation, objective agreement and atomic duration gates."""
from __future__ import annotations

import importlib.util
import math
from pathlib import Path
import sys

import numpy as np
import pytest

SCRIPTS = Path(__file__).resolve().parents[2] / 'scripts'
sys.path.insert(0,str(SCRIPTS.parent/'src'))
from commandmed.reliability_v5.objectives import jensen_shannon_divergence, kl_divergence

sys.path.insert(0,str(SCRIPTS))
spec=importlib.util.spec_from_file_location('adapter_development',SCRIPTS/'v5_s1_adapter_development.py')
adapter=importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)


class ArrayMath:
    """NumPy evaluator for the tensor objective's public mathematical operations.

    This checks agreement against the independently implemented frozen scalar
    objectives without importing/loading the Windows model runtime.
    """
    log=staticmethod(np.log)
    where=staticmethod(np.where)
    ones_like=staticmethod(np.ones_like)
    sum=staticmethod(np.sum)

    @staticmethod
    def softmax(values,dim):
        values=np.asarray(values,dtype=float)
        exponent=np.exp(values-np.max(values,axis=dim,keepdims=True))
        return Array(exponent/exponent.sum(axis=dim,keepdims=True))


class Array(np.ndarray):
    def __new__(cls,values):
        return np.asarray(values,dtype=float).view(cls)

    def float(self):
        return self

    def clamp_min(self,value):
        return Array(np.maximum(self,value))

    def sum(self,axis=None,dtype=None,out=None,keepdims=False,**kwargs):
        if 'dim' in kwargs:
            axis=kwargs.pop('dim')
        return Array(np.asarray(self).sum(axis=axis,dtype=dtype,out=out,keepdims=keepdims,**kwargs))


def test_all_maintenance_ids_are_disjoint_and_used_once():
    assigned=[index for step in range(32) for index in adapter.maintenance_indices(step)]
    assert assigned==list(range(64))
    assert set(assigned).isdisjoint(range(64,320))
    for value in (-1,32,True,1.5):
        with pytest.raises(ValueError):
            adapter.maintenance_indices(value)


@pytest.mark.parametrize('left,right',[([.2,.8],[.6,.4]),([1.,0.],[0.,1.]),([1e-20,1.],[1.,1e-20])])
def test_semantic_js_agrees_with_frozen_scalar_oracle_and_mapping(left,right):
    observed=adapter.semantic_js(ArrayMath,Array(left),Array(right))
    expected=jensen_shannon_divergence(left,right)
    assert float(observed)==pytest.approx(expected,abs=1e-12)
    assert float(adapter.semantic_js(ArrayMath,Array(left[::-1]),Array(right[::-1])))==pytest.approx(expected,abs=1e-12)


@pytest.mark.parametrize('teacher,candidate',[([2.,-1.],[-2.,3.]),([1000.,-1000.],[-1000.,1000.]),([-50.,0.],[0.,-50.])])
def test_teacher_kl_matches_frozen_floor_and_handles_zero_probabilities(teacher,candidate):
    p=ArrayMath.softmax(Array([teacher]),-1)[0].tolist()
    q=ArrayMath.softmax(Array([candidate]),-1)[0].tolist()
    expected=kl_divergence(p,q)
    actual=float(adapter.kl_from_logits(ArrayMath,Array([teacher]),Array([candidate])))
    assert math.isfinite(actual)
    assert actual==pytest.approx(expected,abs=1e-12)


def test_atomic_duration_requires_whole_seed_and_export_buffer():
    adapter.require_atomic_duration(1000,1600)
    for projected,remaining in [(1000,1599),(math.nan,10000),(1000,math.inf),(0,10000)]:
        with pytest.raises(RuntimeError,match='COLAB_RUNTIME_DURATION_BLOCKER'):
            adapter.require_atomic_duration(projected,remaining)


def test_early_eos_cannot_underestimate_full_answer_cost():
    assert adapter.full_answer_projection(2,1)==64
    assert adapter.full_answer_projection(2,32)==2


@pytest.mark.parametrize('elapsed,tokens',[(2,0),(2,33),(2,True),(math.nan,8),(0,8)])
def test_invalid_decode_timing_is_not_admitted(elapsed,tokens):
    with pytest.raises(RuntimeError,match='INVALID_RESOURCE_DECODE_OBSERVATION'):
        adapter.full_answer_projection(elapsed,tokens)
