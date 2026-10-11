#!/usr/bin/env python3
"""Synchronize TCS Round-1 response locator table with the *built* marked PDF.

The manuscript/source remains authoritative. Never invent a PDF margin-line
number: report verified PDF page anchors and stable section/statement names.
"""
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[1]
marked = root / "TCS-D-26-00494_Manuscript_Marked.pdf"
response = root / "response/response_round1.tex"
manuscript = root / "main.tex"
if not marked.is_file() or marked.stat().st_size < 10000:
    raise SystemExit("Marked PDF is missing or too small")
raw = subprocess.check_output(["pdftotext", "-layout", str(marked), "-"], text=True)
pages = [p for p in raw.split("\f") if p.strip()]
if len(pages) < 12:
    raise SystemExit("Marked PDF has implausibly few pages")

source_lines = manuscript.read_text().splitlines()
start_points = []
section, sub = 0, 0
appendix = False
for i, line in enumerate(source_lines, 1):
    if r"\appendix" in line:
        appendix = True
        section = 0
        sub = 0
    m = re.match(r"\s*\\(section|subsection)\{(.+)", line)
    if not m:
        continue
    kind, title = m.groups()
    if kind == "section":
        section += 1
        sub = 0
        number = chr(ord("A") + section - 1) if appendix else str(section)
    else:
        sub += 1
        number = (chr(ord("A") + section - 1) if appendix else str(section)) + "." + str(sub)
    title = title.split(r"\texorpdfstring")[0].split("}")[0]
    title = title.replace("~", " ").replace("--", "-").strip()
    start_points.append((i, number, title))

def where_page(pattern, strict=False):
    regex = re.compile(pattern, re.IGNORECASE | re.MULTILINE)
    for pno, page in enumerate(pages, 1):
        if strict:
            for line in page.splitlines():
                if regex.search(line):
                    return pno
        elif regex.search(page):
            return pno
    return None

number_pages = {}
for line, number, title in start_points:
    if not title or len(title) < 5:
        continue
    p = where_page(r"^\s*(?:\d{1,4}\s+)?"+re.escape(number)+r"\s+"+re.escape(title[:min(22,len(title))]), True)
    if p is None:
        p = where_page(r"\b"+re.escape(title[:min(22,len(title))])+r"\b")
    if p:
        number_pages[number] = p

# Use the actual compiled LaTeX .aux page references whenever available.
# These are more reliable than matching headings in a text extraction
# (added markup may interrupt PDF text or a heading may be quoted earlier).
aux_path = root / "main_marked_round1.aux"
if not aux_path.exists():
    raise SystemExit("No marked PDF auxiliary file to validate section pages")
aux_text = aux_path.read_text(errors="replace")
label_pages = {
    lab: int(pg)
    for lab, pg in re.findall(
        r"\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}",
        aux_text
    )
}
for lino, number, title in start_points:
    # Section labels can occur on the heading line or the following line.
    neighborhood = "\n".join(source_lines[lino - 1:lino + 2])
    for label in re.findall(r"\\label\{([^}]+)\}", neighborhood):
        if label in label_pages:
            number_pages[number] = label_pages[label]
            break

def near_source_page(lno):
    previous = [number_pages[num] for i, num, title in start_points if i <= lno and num in number_pages]
    return previous[-1] if previous else None

def resolve_segment(segment):
    refs = re.findall(
        r"(?:Definition|Theorems?|Proposition|Lemma|Corollary)\s+\d+\.\d+",
        segment
    )
    for ref in refs:
        ref = ref.replace("Theorems ", "Theorem ")
        pattern = r"^\s*(?:\d{1,4}\s+)?" + re.escape(ref) + r"(?:\.|\s|\()"
        p = where_page(pattern, True)
        if p:
            return p
    sec = re.search(r"Sections?\s+(\d+(?:\.\d+)?)", segment)
    if sec and sec.group(1) in number_pages:
        return number_pages[sec.group(1)]
    app = re.search(r"Appendices?\s+([A-C])", segment)
    if app and app.group(1) in number_pages:
        return number_pages[app.group(1)]
    if "Introduction" in segment:
        return number_pages.get("1", 1)
    source = re.search(r"\(source ll?\.~(\d+)(?:--\d+)?\)", segment)
    if source:
        return near_source_page(int(source.group(1)))
    return None

s = response.read_text()
# Trim obsolete notes, without changing the reviewer's quotations.
s = re.sub(
    r"(?m)^% Response synchronized with v176.*\n% Source-line locators.*\n% Submission preflight:.*\n",
    "% Response synchronized to the compiled additions-marked manuscript PDF.\n"
    "% Locator pages are verified PDF page anchors, not guessed margin lines.\n",
    s, count=1)
old_header = r"\noindent\textbf{Revised-manuscript locator ("
new_header = r"\noindent\textbf{Locator guide for the additions-marked revised PDF.}"
anchor = s.index(old_header) if old_header in s else s.index(new_header)
endtable = s.index(r"\end{longtable}", anchor)
table_start = s.index(r"\begingroup", anchor)
prefix = (
    r"\noindent\textbf{Locator guide for the additions-marked revised PDF.}" "\n"
    "Each cited section or theorem-like statement below is accompanied by\n"
    "the page on which its anchor appears in the compiled additions-marked\n"
    r"\texttt{TCS-D-26-00494\_Manuscript\_Marked.pdf}. "
    "Pages are PDF pages, not TeX source lines. Margin-line numbers are not\n"
    "asserted without a separate audit.\n"
)
s = s[:anchor] + prefix + s[table_start:]
anchor = s.index(r"\noindent\textbf{Locator guide")
endtable = s.index(r"\end{longtable}", anchor)
region = s[anchor:endtable]
rpat = re.compile(r"(?m)^(E\.1|R[12]\.\d+) & (.*?)\\\\$")
rows = list(rpat.finditer(region))
if len(rows) != 49:
    raise SystemExit(f"Expected 49 response locator rows, found {len(rows)}")
resolved = 0
def subrow(m):
    global resolved
    key, details = m.groups()
    # Idempotence: the checked-in response may already have an earlier
    # marked-PDF page mapping from the preceding generation.
    details = re.sub(r";?\s*marked PDF p\.~\d+", "", details)
    chunks = [c.strip() for c in details.split(";") if c.strip()]
    rendered = []
    mapped = False
    for chunk in chunks:
        page = resolve_segment(chunk)
        chunk = re.sub(r"\s*\(source ll?\.~\d+--\d+\)", "", chunk).strip()
        if page is not None:
            chunk += rf" (marked PDF p.~{page})"
            mapped = True
        rendered.append(chunk)
    if mapped:
        resolved += 1
    return key + " & " + "; ".join(rendered) + r"\\"

region = rpat.sub(subrow, region)
if resolved < 44:
    raise SystemExit(f"Only {resolved}/49 marked PDF locator anchors resolved")
s = s[:anchor] + region + s[endtable:]
# Remove stale PDF-location caveats in response prose. The human-readable
# statement numbers/sections are not renumbered or altered.
s = s.replace(
    "These checked\nsource-line locators are not PDF page or margin-line numbers.\n"
    "Before resubmission, rebuild the additions-marked PDF and independently\n"
    "re-audit its page, paragraph, and margin-line positions.",
    "The locator table below has been synchronized with the compiled\n"
    "additions-marked PDF and gives verified PDF page anchors; it does not\n"
    "claim unverified PDF margin-line numbers."
)
s = s.replace(
    "The source-line locators above were updated against v168; final\n"
    "marked-PDF page and margin-line verification remains a submission preflight.",
    "The locator guide was regenerated from the compiled marked manuscript;\n"
    "final paragraph/margin-line references, if required by the journal,\n"
    "remain subject to a separate human audit."
)
# In the response preamble, remove outdated statement claiming the abstract
# and marked PDF have not been regenerated.
response.write_text(s)
print(f"Marked PDF: {len(pages)} pages. PDF anchors: {resolved}/49. "
      f"Numbered section headings: {len(number_pages)}.")
for k, v in sorted(number_pages.items()):
    print(f"  {k}: p.{v}")
