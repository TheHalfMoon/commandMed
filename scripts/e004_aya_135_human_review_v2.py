#!/usr/bin/env python3
"""Local-human-only privacy and embedded-source-risk review for the exact Aya 135 set (V2 replay repair).

This program is deliberately interactive and local. It never sends content over the
network, never reads user_id, never writes prompt/target text to output, and requires
an actual human operator to review each exact candidate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import unicodedata
from pathlib import Path
from typing import Any, Iterable

SOURCE_SHA256 = "51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06"
SOURCE_SIZE = 137195800
EXPECTED_COUNT = 135
EXPECTED_MANIFEST_CANONICAL_SHA256 = "dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99"
EXPECTED_RECORD_ID_SET_SHA256 = "d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83"
EXPECTED_CONTENT_SET_SHA256 = "ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64"
REVIEW_METHOD_ID = "AYA_135_LOCAL_HUMAN_PRIVACY_EMBEDDED_SOURCE_REVIEW_V2"


def canonical_bytes(v: Any) -> bytes:
    return json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_file(p: Path) -> str:
    h=hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
    return h.hexdigest()


def set_root(values: Iterable[str]) -> str:
    return hashlib.sha256(("\n".join(sorted(values))+"\n").encode("ascii")).hexdigest()


def norm(v: str|None) -> str:
    s=unicodedata.normalize("NFC",v or "")
    return s.replace("\r\n","\n").replace("\r","\n").strip()


def load_manifest(p: Path) -> dict[str,Any]:
    m=json.loads(p.read_text(encoding="utf-8"))
    if hashlib.sha256(canonical_bytes(m)).hexdigest()!=EXPECTED_MANIFEST_CANONICAL_SHA256:
        raise SystemExit("CANDIDATE_MANIFEST_IDENTITY_MISMATCH")
    rs=m.get("records")
    if not isinstance(rs,list) or len(rs)!=EXPECTED_COUNT: raise SystemExit("CANDIDATE_COUNT_MISMATCH")
    if set_root(str(r["candidate_record_id"]) for r in rs)!=EXPECTED_RECORD_ID_SET_SHA256:
        raise SystemExit("RECORD_ID_SET_MISMATCH")
    if set_root(str(r["content_sha256"]) for r in rs)!=EXPECTED_CONTENT_SET_SHA256:
        raise SystemExit("CONTENT_SET_MISMATCH")
    return m


def candidate_rows(parquet: Path, manifest: dict[str,Any]):
    import pyarrow.parquet as pq
    if parquet.stat().st_size!=SOURCE_SIZE or sha256_file(parquet)!=SOURCE_SHA256:
        raise SystemExit("AYA_SOURCE_IDENTITY_MISMATCH")
    by_id={str(r["candidate_record_id"]):str(r["content_sha256"]) for r in manifest["records"]}
    if len(by_id)!=EXPECTED_COUNT: raise SystemExit("RECORD_ID_NOT_UNIQUE")
    found=set(); idx=0
    f=pq.ParquetFile(parquet)
    for rg in range(f.num_row_groups):
        t=f.read_row_group(rg,columns=["inputs","targets","language_code","annotation_type"])
        for prompt,target,lang,ann in zip(t["inputs"].to_pylist(),t["targets"].to_pylist(),t["language_code"].to_pylist(),t["annotation_type"].to_pylist(),strict=True):
            p,tgt=norm(prompt),norm(target)
            rep={"annotation_type":ann,"inputs":p,"language_code":lang,"targets":tgt}
            ch=hashlib.sha256(canonical_bytes(rep)).hexdigest()
            recomputed=hashlib.sha256(f"{SOURCE_SHA256}:{idx}:{ch}".encode("ascii")).hexdigest()
            expected_ch=by_id.get(recomputed)
            if expected_ch is not None:
                if expected_ch!=ch: raise SystemExit("CONTENT_REPLAY_MISMATCH")
                rid=recomputed
                if rid in found: raise SystemExit("DUPLICATE_CANDIDATE_MATCH")
                found.add(rid)
                yield rid,ch,str(lang),p,tgt
            idx+=1
    if len(found)!=EXPECTED_COUNT: raise SystemExit("CANDIDATE_REPLAY_INCOMPLETE")


def choice(prompt:str, allowed:dict[str,str])->str:
    while True:
        print(prompt)
        for k,v in allowed.items(): print(f"  {k}: {v}")
        ans=input("> ").strip().upper()
        if ans in allowed: return allowed[ans]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--aya-parquet",required=True,type=Path)
    ap.add_argument("--candidate-manifest",required=True,type=Path)
    ap.add_argument("--out",required=True,type=Path)
    ap.add_argument("--reviewer-id",required=True,help="Non-secret local reviewer identifier; do not use email or personal ID.")
    a=ap.parse_args()
    if not sys.stdin.isatty(): raise SystemExit("INTERACTIVE_HUMAN_TTY_REQUIRED")
    manifest=load_manifest(a.candidate_manifest)
    records=[]
    for n,(rid,ch,lang,prompt,target) in enumerate(candidate_rows(a.aya_parquet,manifest),1):
        os.system("clear" if os.name!="nt" else "cls")
        print(f"Human review {n}/{EXPECTED_COUNT} | language={lang} | record={rid[:16]}…")
        print("\n=== INPUT ===\n"+prompt+"\n\n=== TARGET ===\n"+target+"\n")
        privacy=choice("Privacy/PHI disposition after human inspection:",{
            "N":"NO_PHI_KNOWN","R":"RESTRICTED_OR_PHI","U":"UNRESOLVED"})
        embedded=choice("Embedded/quoted third-party source-risk disposition:",{
            "C":"NO_EMBEDDED_SOURCE_RISK_OBSERVED","P":"EMBEDDED_SOURCE_RISK_PRESENT","U":"UNRESOLVED"})
        scope=choice("SP007-RO-001 learner/researcher scope verification:",{
            "P":"PASS","F":"FAIL","U":"UNRESOLVED"})
        records.append({"candidate_record_id":rid,"content_sha256":ch,"privacy_state":privacy,
                        "embedded_source_risk_state":embedded,"scope_verification":scope})
    out={"schema_version":"1","artifact_id":"e004-aya-135-local-human-review-v1",
         "method_id":REVIEW_METHOD_ID,"candidate_count":len(records),"reviewer_id":a.reviewer_id,
         "interactive_human_tty_required":True,"external_provider_used":False,"model_ai_review_used":False,
         "user_id_read":False,"raw_text_persisted":False,"records":records}
    a.out.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
    print("HUMAN_REVIEW_COMPLETE=YES")
    print("OUTPUT_SHA256="+sha256_file(a.out))

if __name__=="__main__": main()
