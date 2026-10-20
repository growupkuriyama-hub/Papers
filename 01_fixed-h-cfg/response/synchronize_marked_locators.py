#!/usr/bin/env python3
"""Synchronize 49 response-table locators against the ACTUAL marked manuscript PDF.

Only PDF page/margin-line numbers observed in pdftotext are emitted. These are
anchors at the beginning of named sections/statements, not fabricated ranges.
"""
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
marked = root / "TCS-D-26-00494_Manuscript_Marked.pdf"
response = root / "response/response_round1.tex"
if not marked.is_file() or marked.stat().st_size < 10000:
    raise SystemExit("Missing marked manuscript; refusing unverified locators")
raw = subprocess.check_output(["pdftotext", "-layout", str(marked), "-"], text=True)
pages = [p.splitlines() for p in raw.split("\f") if p.strip()]
if len(pages) < 12:
    raise SystemExit("Unexpected marked-manuscript page count")

# Use word coordinates to associate theorem headings with their own
# margin number rather than the previous/next line in pdftotext -layout.
bbox_xml = subprocess.check_output(
    ["pdftotext", "-bbox-layout", str(marked), "-"], text=True
)
bbox_root = ET.fromstring(bbox_xml)
bbox_pages = []
for page in bbox_root.findall(".//{*}page"):
    words = []
    for node in page.findall(".//{*}word"):
        value = "".join(node.itertext()).strip()
        if value:
            words.append((
                value,
                float(node.attrib["xMin"]), float(node.attrib["xMax"]),
                float(node.attrib["yMin"]), float(node.attrib["yMax"])
            ))
    bbox_pages.append((float(page.attrib["width"]), words))
if len(bbox_pages) != len(pages):
    raise SystemExit("BBox and layout page counts disagree")

def locate_statement_bbox(kind, number):
    for page_number, (width, words) in enumerate(bbox_pages, 1):
        # On latexdiff PDFs the word stream can interleave change-markup
        # strokes and following text; heading words need not be adjacent.
        # Match statement number on the *same visual line* instead.
        for value, x0, x1, y0, y1 in words:
            if value.lower() != kind.lower() or not (55 <= x0 <= 100):
                continue
            center = (y0 + y1) / 2
            is_heading = any(
                v.rstrip(".") == number
                and x1 - 1 <= vx0 <= x1 + 65
                and abs((vy0 + vy1) / 2 - center) < 7
                for v, vx0, vx1, vy0, vy1 in words
            )
            if not is_heading:
                continue
            if kind.lower() == "corollary" and number == "5.4":
                if not any("gold" in v.lower() and abs((vy0 + vy1) / 2 - center) < 28
                           for v, vx0, vx1, vy0, vy1 in words):
                    continue
            # Corollary 5.4 also occurs in an earlier body-text citation.
            # The actual theorem heading has x0 at the left text margin;
            # same-line matching distinguishes the heading reliably.
            margin = [
                (abs((my0 + my1) / 2 - center), int(v))
                for v, mx0, mx1, my0, my1 in words
                if v.isdigit() and 100 <= int(v) <= 3000
                and (mx1 < 67 or mx0 > width - 85)
                and abs((my0 + my1) / 2 - center) < 8
            ]
            if margin:
                margin.sort()
                return page_number, margin[0][1]
        for i in range(len(words) - 1):
            word, x0, x1, y0, y1 = words[i]
            nxt, nx0, nx1, ny0, ny1 = words[i + 1]
            if (word.lower() != kind.lower()
                    or nxt.rstrip(".") != number
                    or not 55 <= x0 <= 100
                    or abs((y0 + y1) - (ny0 + ny1)) > 16
                    or nx0 - x1 > 48):
                continue
            # Corollary 5.4 is also mentioned earlier as a forward
            # reference. Its actual heading includes "Gold identification".
            # Require that heading text rather than selecting the first
            # in-prose mention on an earlier page.
            if kind.lower() == "corollary" and number == "5.4":
                if not any(
                    "gold" in value.lower()
                    and abs((my0 + my1) - (y0 + y1)) < 28
                    for value, _, _, my0, my1 in words[i + 2:i + 10]
                ):
                    continue
            center = (y0 + y1) / 2
            nearby = []
            for value, mx0, mx1, my0, my1 in words:
                if (value.isdigit()
                        and 100 <= int(value) <= 3000
                        and (mx1 < 67 or mx0 > width - 85)
                        and abs((my0 + my1) / 2 - center) <= 8):
                    nearby.append((abs((my0 + my1)/2 - center), int(value)))
            if len(nearby) == 1:
                return page_number, nearby[0][1]
            if nearby:
                nearby.sort()
                if len(nearby) == 1 or nearby[0][0] + 2 < nearby[1][0]:
                    return page_number, nearby[0][1]
    return None

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
        exact = locate_statement_bbox(kind, number)
        if exact is not None:
            return exact
        heading = re.compile(r"^\s*(?:\d{1,4}\s+)?"
                             + re.escape(kind) + r"\s+" + re.escape(number)
                             + r"\b", re.I)
    else:
        section = re.search(r"Sections?\s+(\d+(?:\.\d+)?)", section_or_statement)
        if section:
            number = section.group(1)
        elif re.search(r"Append(?:ix|ices)\b", section_or_statement):
            m = re.search(r"Append(?:ix|ices)\s+([ABC])", section_or_statement)
            number = m.group(1) if m else "A"
        elif "Introduction" in section_or_statement:
            number = "1"
        else:
            return None
        # Match known titles, not incidental prose such as "A separate".
        titles = {
            "A": "Fixed-window", "B": "Proof",
            "C": "Substitutability",
        }
        prefix = titles.get(number)
        if prefix:
            heading = re.compile(r"^\s*(?:\d{1,4}\s+)?"
                                 + re.escape(number) + r"\s+"
                                 + re.escape(prefix), re.I)
        else:
            heading = re.compile(r"^\s*(?:\d{1,4}\s+)?"
                                 + re.escape(number) + r"(?![.\d])\s+[A-Za-z]")
    for page_number, lines in enumerate(pages, 1):
        for j, line in enumerate(lines):
            if not heading.search(line):
                continue
            number_at_anchor = margin_number(line)
            # Distinguish a heading's section number (e.g. "9 Expressiveness")
            # from an actual PDF margin line number.
            if (not statement and number.isdigit()
                    and number_at_anchor == int(number)
                    and not re.search(r"\s{2,}\d{1,4}\s*$", line)):
                number_at_anchor = None
            if number_at_anchor is None and statement and kind == "Theorem" and number == "5.2":
                # Theorem 5.2's marked heading may wrap across several lines.
                # Its own margin anchor is l.439; the preceding l.438 belongs
                # to Section 5.2 and must not be used.
                for distance in range(1, 15):
                    k = j + distance
                    if k >= len(lines):
                        break
                    number_at_anchor = margin_number(lines[k])
                    if number_at_anchor is not None:
                        break
            if number_at_anchor is None:
                # pdftotext sometimes emits a displayed heading and its
                # margin number on different consecutive text lines.
                for distance in (1, -1, 2, -2, 3, -3):
                    k = j + distance
                    if 0 <= k < len(lines):
                        number_at_anchor = margin_number(lines[k])
                        if number_at_anchor is not None:
                            break
            if number_at_anchor is None and statement:
                # With additions marking, a long statement heading may wrap
                # across many pdftotext lines before its margin-line number.
                # Search only the consecutive nonblank heading lines.
                for distance in range(4, 15):
                    k = j + distance
                    if k >= len(lines) or not lines[k].strip():
                        break
                    number_at_anchor = margin_number(lines[k])
                    if number_at_anchor is not None:
                        break
            if number_at_anchor is not None:
                return page_number, number_at_anchor
    return None

# Require heading anchors in their current mathematical order (v236+ numbering).
ordered_statements = [
    ("Proposition", "6.4"),
    ("Lemma", "7.6"),
    ("Lemma", "8.2"),
    ("Theorem", "8.3"),
]
ordered_positions = [locate_statement_bbox(k, n) for k, n in ordered_statements]
if any(p is None for p in ordered_positions) or ordered_positions != sorted(ordered_positions):
    raise SystemExit(f"Statement locator order or coordinate matching failed: {list(zip(ordered_statements, ordered_positions))}")
print(f"Verified ordered theorem coordinates: {list(zip(ordered_statements, ordered_positions))}")

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
