#!/usr/bin/env python3
"""Flag candidate defensive-writing patterns; never edit the source document."""

from __future__ import annotations

import argparse
import re
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

PATTERNS = [
    ("unnecessary disclaimer", re.compile(r"\b(?:we|this (?:paper|study|article))\s+(?:do(?:es)? not|did not)\s+(?:claim|attempt|seek|intend)\b", re.I)),
    ("unnecessary disclaimer", re.compile(r"(?:本文|本研究|我们)(?:并非|不|没有)(?:旨在|意在|试图|声称|宣称|试图说明)")),
    ("hypothetical-misreading clarification", re.compile(r"\b(?:this should not be (?:taken|interpreted) to mean|to be clear|it should be noted that)\b", re.I)),
    ("hypothetical-misreading clarification", re.compile(r"(?:需要说明|需要澄清|不应被理解为|这并不意味着)")),
    ("defensive contrast", re.compile(r"\b(?:not\s+.+?\s+but|rather than)\b", re.I)),
    ("defensive contrast", re.compile(r"(?:不是.+而是|而非)")),
    ("method defense", re.compile(r"\b(?:although|while)\b.+\b(?:used|employed|adopted)\b.+\b(?:because|due to|practical constraints)\b", re.I)),
    ("method defense", re.compile(r"(?:尽管|虽然).*(?:采用|使用).+(?:因为|由于|受限于)")),
    ("limitation-led framing", re.compile(r"^\s*(?:although|while)\b.+\b(?:limitation|limited|cannot)\b", re.I)),
    ("limitation-led framing", re.compile(r"^\s*(?:尽管|虽然).*(?:局限|不足|无法)")),
]
HEDGE = re.compile(r"\b(?:may|might|could|potentially|possibly|suggest(?:s|ed|ing)?)\b|(?:可能|或许|也许|一定程度上|或可)", re.I)
LIMITATION_TERMS = re.compile(r"\b(?:cross-sectional|observational|generaliz|external validity|in-domain|non-significant|meta-analysis|causal)\b|(?:横断面|观察性|外部效度|域内|不显著|元分析|因果)", re.I)
EVIDENCE_BOUNDARY = re.compile(r"\b(?:cross-sectional|observational|did not (?:undertake|conduct) a meta-analysis|without meta-analysis|in-domain|external validity|external validation|non-significant|causal)\b|(?:横断面|观察性|未进行元分析|未开展元分析|域内|外部效度|外部验证|不显著|因果)", re.I)


def read_text(path: Path) -> str:
    if path.suffix.lower() != ".docx":
        return path.read_text(encoding="utf-8", errors="replace")
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    paragraphs = []
    for para in root.findall(".//w:p", NS):
        text = "".join(para.itertext()).strip()
        if text:
            paragraphs.append(text)
    return "\n".join(paragraphs)


def sentences(text: str) -> list[str]:
    chunks = re.split(r"(?<=[。！？])\s*|(?<=[.!?])\s+|\n+", text)
    return [chunk.strip() for chunk in chunks if chunk.strip()]


def scan(text: str) -> list[tuple[int, str, str, str]]:
    hits = []
    prior_limits: Counter[str] = Counter()
    for number, sentence in enumerate(sentences(text), 1):
        if re.match(r"^\s*(?:case\s+\d+|#{1,6}\s)", sentence, re.I):
            continue
        for label, pattern in PATTERNS:
            if pattern.search(sentence):
                action = "classify before revising"
                if label == "method defense":
                    action = "retain design fact; move its interpretive limit to Limitations if needed"
                hits.append((number, label, action, sentence))
        hedge_count = len(HEDGE.findall(sentence))
        if hedge_count >= 2:
            hits.append((number, "stacked hedging", "replace only with evidence-calibrated wording", sentence))
        if EVIDENCE_BOUNDARY.search(sentence):
            hits.append((number, "evidence boundary", "preserve; verify its placement and exact consequence", sentence))
        if LIMITATION_TERMS.search(sentence):
            key = re.sub(r"\W+", " ", sentence.lower()).strip()
            prior_limits[key] += 1
    for key, count in prior_limits.items():
        if count > 1:
            hits.append((0, "repeated limitation", f"appears {count} times; consolidate if it is the same boundary", key))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Find candidate defensive-writing patterns without modifying a draft.")
    parser.add_argument("input", type=Path, help="UTF-8 text/Markdown/LaTex file or DOCX file")
    parser.add_argument("--format", choices=("markdown", "tsv"), default="markdown")
    args = parser.parse_args()
    hits = scan(read_text(args.input))
    if args.format == "markdown":
        print("| Sentence | Signal | Suggested handling | Text |")
        print("| --- | --- | --- | --- |")
        for number, label, action, sentence in hits:
            safe = sentence.replace("|", "\\|").replace("\n", " ")
            print(f"| {number or 'document'} | {label} | {action} | {safe} |")
    else:
        for number, label, action, sentence in hits:
            print("\t".join((str(number or "document"), label, action, sentence.replace("\t", " "))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
