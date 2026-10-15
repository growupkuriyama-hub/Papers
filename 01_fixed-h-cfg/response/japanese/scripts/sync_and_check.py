#!/usr/bin/env python3
"""Check fidelity to the English source, synchronize anchors, and flatten Japanese TeX.

English prose changes intentionally fail CI until the Japanese translation is reviewed.
Locator-only changes are synchronized automatically without resetting the translation lock.
"""
from __future__ import annotations
from pathlib import Path
import re
import sys

JP = Path(__file__).resolve().parents[1]
RESPONSE = JP.parent
EN = RESPONSE / "response_round1.tex"
LOCK = JP / "english_body_fingerprint.txt"
MAIN = JP / "main_JP.tex"
LOC = JP / "locator_table_JP.tex"
FLAT = JP / "TCS-D-26-00494_Response_to_Reviewers_JP.tex"

def without_locator(text: str) -> str:
    a = text.index(r"\noindent\textbf{Locator guide for")
    b = text.index(r"\endgroup", a)
    return text[:a] + "<<AUTO_LOCATOR_TABLE>>" + text[b + len(r"\endgroup"):]

def fingerprint(text: str) -> str:
    h = 0xcbf29ce484222325
    for c in without_locator(text):
        h = ((h ^ ord(c)) * 0x100000001b3) & ((1 << 64) - 1)
    return f"{h:016x}"

def jp_locator(segment: str) -> str:
    # Change only the labels. The actual PDF coordinates stay verbatim.
    names = {
        "Introduction and related work": "序論と関連研究",
        "Introduction": "序論",
        "Theorems": "定理",
        "Theorem": "定理",
        "Proposition": "命題",
        "Corollary": "系",
        "Definition": "定義",
        "Lemma": "補題",
        "Appendices": "付録",
        "Appendix": "付録",
    }
    for src, dest in names.items():
        segment = re.sub(r"\b" + re.escape(src) + r"\b", dest, segment)
    segment = re.sub(r"\band\b", "および", segment)
    segment = re.sub(r"\bSections?\s+([\d.]+(?:--[\d.]+)?)", r"第\1節", segment)
    segment = re.sub(
        r"\(marked PDF p\.~(\d+), margin l\.~(\d+)\)",
        r"（Marked PDF p.~\1，余白行~\2）",
        segment,
    )
    return segment

def write_locator(en: str) -> tuple[int, int]:
    a = en.index(r"\noindent\textbf{Locator guide for")
    b = en.index(r"\endgroup", a) + len(r"\endgroup")
    table_en = en[a:b]
    rows = re.findall(r"(?m)^(E\.1|R[12]\.\d+) & ([^\n]*?)\\\\$", table_en)
    if len(rows) != 49:
        raise ValueError(f"Expected 49 locator rows, got {len(rows)}")
    anchors = table_en.count("marked PDF p.~")
    if anchors != 77:
        raise ValueError(f"Expected 77 anchors, got {anchors}")
    lines = [
        r"\subsection*{修正表示PDFに対する参照表}",
        "以下の49項目・77参照は、英語版査読回答の検証済み参照表から自動的に転記される。",
        r"\begingroup\small",
        r"\setlength{\LTpre}{4pt}\setlength{\LTpost}{6pt}",
        r"\begin{longtable}{@{}p{0.09\linewidth}p{0.83\linewidth}@{}}",
        r"\toprule", r"項目 & 改訂原稿での位置\\",
        r"\midrule\endfirsthead",
        r"\toprule", r"項目 & 改訂原稿での位置\\",
        r"\midrule\endhead",
    ]
    for item, cell in rows:
        lines.append(item + " & " + jp_locator(cell) + r"\\")
    lines += [r"\bottomrule", r"\end{longtable}", r"\endgroup"]
    LOC.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(rows), anchors

def flatten(tex: str, visited: set[str] | None = None) -> str:
    if visited is None:
        visited = set()
    pattern = re.compile(r"\\input\{(japanese/[^}]+)\}")
    def replace(m):
        name = m.group(1)
        if name in visited:
            raise RuntimeError(f"Recursive input {name}")
        sub = RESPONSE / name
        if not sub.is_file():
            raise FileNotFoundError(sub)
        return "\n% --- BEGIN " + name + " ---\n" + flatten(
            sub.read_text(encoding="utf-8"), visited | {name}
        ) + "\n% --- END " + name + " ---\n"
    return pattern.sub(replace, tex)

def main() -> int:
    src = EN.read_text(encoding="utf-8")
    expected = LOCK.read_text(encoding="utf-8").strip()
    actual = fingerprint(src)
    if actual != expected:
        print(f"STALE JAPANESE TRANSLATION: source={actual}, translated={expected}", file=sys.stderr)
        print("Update all Japanese translations and the reviewed fingerprint first.", file=sys.stderr)
        return 2
    rows, refs = write_locator(src)
    result = flatten(MAIN.read_text(encoding="utf-8"))
    ids = re.findall(r"\\Comment\{((?:E\.1|R[12]\.\d+))\}", result)
    expected_ids = ["E.1"] + [f"R1.{i}" for i in range(1, 38)] + [f"R2.{i}" for i in range(1, 12)]
    if sorted(ids) != sorted(expected_ids) or len(ids) != 49:
        raise RuntimeError(f"Incomplete translation! {len(ids)} comment headings; expected 49.")
    FLAT.write_text(result, encoding="utf-8")
    print(f"Japanese full translation in sync: body={actual}, {len(ids)} responses, {rows} locator rows, {refs} anchors")
    print(FLAT)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
