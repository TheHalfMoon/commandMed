#!/usr/bin/env python3
"""Resolve selected V5 RiskCalcs sources against PubMed without model execution.

Only minimal publication metadata and hashes are persisted. PubMed abstract text is
used transiently to establish presence/hash and is never written to repository artifacts.
"""
from __future__ import annotations

import hashlib
import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

PACKET = Path(__file__).resolve().parents[1]
MANIFEST = PACKET / "riskcalcs-rule-oracle-final-candidate-v5.json"
OUT = PACKET / "clinical-source-audit-v5.json"
REVIEW = PACKET / "clinical-source-review-v5.md"
SOURCE_URL = (
    "https://raw.githubusercontent.com/ncbi-nlp/Clinical-Tool-Learning/"
    "d474a95128e128623933c9be0d389ff7d82ef782/"
    "riskqa_evaluation/tools/riskcalcs.json"
)
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
UA = "CommandMed-research/1.0 (public metadata audit)"


def get_bytes(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def text(node: ET.Element | None, path: str) -> str:
    if node is None:
        return ""
    found = node.find(path)
    return "" if found is None else "".join(found.itertext()).strip()


def article_ids(article: ET.Element) -> dict[str, str]:
    result: dict[str, str] = {}
    for item in article.findall(".//PubmedData/ArticleIdList/ArticleId"):
        kind = str(item.attrib.get("IdType", "")).lower()
        value = (item.text or "").strip()
        if kind and value:
            result[kind] = value
    return result


def publication_types(article: ET.Element) -> list[str]:
    values = []
    for item in article.findall(".//PublicationTypeList/PublicationType"):
        value = (item.text or "").strip()
        if value:
            values.append(value)
    return sorted(set(values))


def abstract_text(article: ET.Element) -> str:
    parts = []
    for item in article.findall(".//Abstract/AbstractText"):
        body = "".join(item.itertext()).strip()
        if body:
            parts.append(body)
    return " ".join(parts)


def fetch_pubmed(pmids: list[str]) -> dict[str, dict[str, object]]:
    query = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"})
    root = ET.fromstring(get_bytes(f"{EFETCH}?{query}"))
    records: dict[str, dict[str, object]] = {}
    for article in root.findall(".//PubmedArticle"):
        pmid = text(article, ".//MedlineCitation/PMID")
        ids = article_ids(article)
        types = publication_types(article)
        abstract = abstract_text(article)
        records[pmid] = {
            "pubmed_title": text(article, ".//Article/ArticleTitle"),
            "journal": text(article, ".//Article/Journal/Title"),
            "pub_date": text(article, ".//Article/Journal/JournalIssue/PubDate"),
            "doi": ids.get("doi", ""),
            "publication_types": types,
            "abstract_present": bool(abstract),
            "abstract_sha256": hashlib.sha256(abstract.encode("utf-8")).hexdigest() if abstract else "",
            "retraction_or_withdrawal_flag": any(
                token in " ".join(types).lower()
                for token in ("retracted", "retraction", "withdrawn")
            ),
        }
    return records


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    source = json.loads(get_bytes(SOURCE_URL))
    selected = manifest.get("selected", [])
    pmids = [str(row["pmid"]) for row in selected]
    pubmed = fetch_pubmed(pmids)

    rows = []
    specialty_counts: Counter[str] = Counter()
    for row in selected:
        pmid = str(row["pmid"])
        upstream = source.get(pmid, {})
        specialty = str(upstream.get("specialty", "")).strip()
        for component in specialty.split(","):
            component = component.strip()
            if component:
                specialty_counts[component] += 1
        resolved = pubmed.get(pmid, {})
        rows.append({
            "pmid": pmid,
            "calculator_title": row["title"],
            "selection_specialty_stratum": row.get("selection_specialty_stratum", ""),
            "source_specialty": specialty,
            "prospective_case_space": row["prospective_case_space"],
            "code_sha256": row["code_sha256"],
            "pubmed_resolved": bool(resolved),
            **resolved,
        })

    unresolved = [row["pmid"] for row in rows if not row["pubmed_resolved"]]
    retracted = [row["pmid"] for row in rows if row.get("retraction_or_withdrawal_flag")]
    missing_abstracts = [row["pmid"] for row in rows if row["pubmed_resolved"] and not row.get("abstract_present")]
    payload = {
        "status": "SOURCE_LEVEL_METADATA_AUDIT_NOT_FINAL_CLINICAL_ADMISSION",
        "copyright_minimization": "NO_PUBMED_ABSTRACT_TEXT_OR_SOURCE_INTERPRETATION_TEXT_PERSISTED",
        "selected_count": len(rows),
        "pubmed_resolved_count": len(rows) - len(unresolved),
        "unresolved_pmids": unresolved,
        "abstract_present_count": len(rows) - len(unresolved) - len(missing_abstracts),
        "missing_abstract_pmids": missing_abstracts,
        "retraction_or_withdrawal_pmids": retracted,
        "component_specialty_counts": dict(sorted(specialty_counts.items())),
        "rows": rows,
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# V5 selected-calculator clinical source review", "",
        "Status: source metadata review queue; not final clinical admission.", "",
        "This queue intentionally persists publication metadata and hashes only. It does not reproduce PubMed abstracts or upstream interpretation prose.", "",
        f"- selected calculators: `{len(rows)}`",
        f"- PubMed identities resolved: `{len(rows) - len(unresolved)}`",
        f"- abstracts present (text not persisted): `{len(rows) - len(unresolved) - len(missing_abstracts)}`",
        f"- unresolved PMIDs: `{len(unresolved)}`",
        f"- retraction/withdrawal flags from PubMed publication types: `{len(retracted)}`", "",
        "## Review queue", "",
    ]
    for row in rows:
        lines.extend([
            f"### PMID {row['pmid']} - {row['calculator_title']}", "",
            f"- first-listed source specialty stratum: {row.get('selection_specialty_stratum') or 'UNKNOWN'}",
            f"- source-declared specialties: {row['source_specialty'] or 'UNKNOWN'}",
            f"- PubMed title: {row.get('pubmed_title') or 'UNRESOLVED'}",
            f"- journal/date: {row.get('journal') or 'UNKNOWN'} / {row.get('pub_date') or 'UNKNOWN'}",
            f"- DOI: {row.get('doi') or 'NONE_RECORDED'}",
            f"- publication types: {', '.join(row.get('publication_types', [])) or 'UNKNOWN'}",
            f"- abstract present: {row.get('abstract_present', False)}",
            f"- abstract SHA-256: {row.get('abstract_sha256') or 'NONE'}",
            f"- prospective case space: {row['prospective_case_space']}",
            "- clinical appropriateness decision: `PENDING_QUALIFIED_REVIEW`",
            "- replacement required: `PENDING`", "",
        ])
    REVIEW.write_text("\n".join(lines).rstrip("\n") + "\n", encoding="utf-8", newline="\n")
    print(f"PUBMED_RESOLVED={len(rows) - len(unresolved)}/{len(rows)}")
    print(f"ABSTRACTS_PRESENT={len(rows) - len(unresolved) - len(missing_abstracts)}/{len(rows)}")
    print(f"RETRACTION_WITHDRAWAL_FLAGS={len(retracted)}")
    print(f"OUT={OUT}")
    print(f"REVIEW={REVIEW}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())