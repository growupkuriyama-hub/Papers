#!/usr/bin/env python3
"""Synchronize 49 response-table locators against the ACTUAL marked manuscript PDF.

Only PDF page/margin-line numbers observed in pdftotext are emitted. These are
anchors at the beginning of named sections/statements, not fabricated ranges.
"""
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[1]
marked = root / "TCS-D-26-00494_Manuscript_Marked.pdf"
response = root / "response/response_round1.tex"
if not marked.is_file() or marked.stat().st_size < 10000:
    raise SystemExit("Missing marked manuscript; refusing unverified locators")
raw = subprocess.check_output(["pdftotext", "-layout", str(marked), "-"], text=True)
pages = [p.splitlines() for p in raw.split("\f") if p.strip()]
if len(pages) < 12:
    raise SystemExit("Unexpected marked-manuscript page count")

def margin_number(line):
    for pat in (r"\s{2,}(\d{1,4})\s*$", r"^\s*(\d{1,4})\s+(?:[^\d]|$)"):
        m = re.search(pat, line)
        if m:
            return int(m.group(1))
    return None

def locate(section_or_statement):
    statement = re.search(
        r"(Definition|Theorems?|Proposition|Lemma|Corollary)\s+(\d+\.\d+)",
        section_or_statement, flags=re.I)
    if statement:
        kind = statement.group(1).replace("Theorems", "Theorem")
        number = statement.group(2)
        heading = re.compile(r"^\s*(?:\d{1,4}\s+)?"
                             + re.escape(kind) + r"\s+" + re.escape(number)
                             + r"\b", re.I)
    else:
        section = re.search(r"Sections?\s+(\d+(?:\.\d+)?)", section_or_statement)
        if section:
            number = section.group(1)
        elif "Appendic" in section_or_statement:
            m = re.search(r"Appendic\w*\s+([ABC])", section_or_statement)
            number = m.group(1) if m else "A"
        elif "Introduction" in section_or_statement:
            number = "1"
        else:
            return None
        heading = re.compile(r"^\s*(?:\d{1,4}\s+)?"
                             + re.escape(number) + r"(?![.\d])\s+[A-Za-z]")
    for page_number, lines in enumerate(pages, 1):
        for j, line in enumerate(lines):
            if not heading.search(line):
                continue
            number_at_anchor = margin_number(line)
            if number_at_anchor is None:
                # pdftotext sometimes emits a displayed heading and its
                # margin number on different consecutive text lines.
                for distance in (1, -1, 2, -2, 3, -3):
                    k = j + distance
                    if 0 <= k < len(lines):
                        number_at_anchor = margin_number(lines[k])
                        if number_at_anchor is not None:
                            break
            if number_at_anchor is not None:
                return page_number, number_at_anchor
    return None

s = response.read_text()
heading_re = re.compile(
    r"\\noindent\\textbf\{Locator guide for the [^}]*\.\}")
header = heading_re.search(s)
if not header:
    raise SystemExit("Missing response locator-table header")
table_begin = s.index(r"\begingroup", header.end())
table_end = s.index(r"\end{longtable}", table_begin)
before = s[:header.start()]
after = s[table_begin:table_end]
row_re = re.compile(r"(?m)^(E\.1|R[12]\.\d+) & ([^\n]*?)\\\\$")
rows = row_re.findall(after)
if len(rows) != 49:
    raise SystemExit(f"Expected 49 response locator rows, found {len(rows)}")

mapped = 0
def update_row(match):
    global mapped
    item, entry = match.groups()
    segments = [c.strip() for c in entry.split(";") if c.strip()]
    revised = []
    for segment in segments:
        # Re-running after a previous build must be idempotent.
        segment = re.sub(r"\s*\(marked PDF p\.~\d+, margin l\.~\d+\)", "", segment)
        found = locate(segment)
        if found is None:
            raise SystemExit(f"Unable to verify marked-PDF anchor: {item}, {segment}")
        page, line = found
        revised.append(segment + f" (marked PDF p.~{page}, margin l.~{line})")
    mapped += 1
    return item + " & " + "; ".join(revised) + r"\\"

after = row_re.sub(update_row, after)
if mapped != 49:
    raise SystemExit(f"Locator coverage only {mapped}/49")
preface = (
    r"\noindent\textbf{Locator guide for the additions-marked revised manuscript.}" "\n"
    "Each location below is anchored to a named section or statement, with its\n"
    "actual PDF page and a margin-line number checked in the freshly compiled\n"
    "additions-marked manuscript. A section anchor may cover multiple revised\n"
    "paragraphs; the named statement identifies the relevant paragraph.\n"
)
s = before + preface + s[table_begin:table_end].replace(s[table_begin:table_end], after) + s[table_end:]
s = s.replace("The locator table below uses stable section and statement anchors\n"
              "rather than source-line or PDF margin-line numbers; its references should\n"
              "remain meaningful after the final pagination of the marked manuscript.",
              "The locator table below gives the revised statement or section and\n"
              "its verified marked-PDF page and margin-line anchor.")
s = s.replace("Each row uses section or theorem-like statement references in the revised\n"
              "manuscript. The references do not depend on a particular PDF pagination.\n", "")
response.write_text(s)
print(f"Verified actual marked PDF page and margin-line anchor for all {mapped} items "
      f"over {len(pages)} manuscript pages.")
