#!/usr/bin/env python3
"""Reject stale, unqualified theorem-number references in the TCS R1 response.

Compare the *types* and numbers of actual marked-PDF statement headings, rather
than accepting a same-number Remark when a Corollary is cited. Deliberately
historical references in the reply are exempt only when identified as such.
"""
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[1]
english = (root / "main.tex").read_text(encoding="utf-8")
clean = (root / "TCS-D-26-00494_Manuscript_Clean.tex").read_text(encoding="utf-8")
response = (root / "response/response_round1.tex").read_text(encoding="utf-8")
form = (root / "revision/TCS_FORM_ABSTRACT_CURRENT.txt").read_text(encoding="utf-8")
if english != clean:
    raise SystemExit("Clean manuscript does not match English main.tex")
if re.search(r"\bIf\s+Let\b", english):
    raise SystemExit("Found broken 'If Let' wording")
section5 = english.split(r"\section{Finite Witnesses, Exact Reconstruction, and Complexity}", 1)[1].split(
    r"\section{Typed Thickness for General Fixed Typings}", 1)[0]
counter = english.split(r"\subsection{A capped regular counter family}", 1)[1].split(
    r"\subsection{Natural deterministic context-free languages", 1)[0]
if r"\pi" in section5 or r"t_\rho" not in section5:
    raise SystemExit("Production label in Section 5 must be rho, not pi")
if r"\rho" in counter or r"\mathrm{CTR}_B" not in counter:
    raise SystemExit("Capped counter Section 9.2 must use B, not rho")
if r"\mathrm{CTR}_\rho" in response or r"t_\pi" in response:
    raise SystemExit("Reviewer response retains outdated counter / production notation")
if "finite targets" not in english or "finite targets" not in form:
    raise SystemExit("The form and manuscript abstracts do not share 'finite targets'")
if "finite target families" in form:
    raise SystemExit("Stale Editorial Manager abstract wording")

pdf = root / "TCS-D-26-00494_Manuscript_Marked.pdf"
marked = subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"], text=True)
kind = r"(?:Theorem|Proposition|Lemma|Corollary|Remark)"
headings = set(re.findall(
    rf"(?m)^\s*(?:\d{{1,4}}\s+)?({kind})\s+(\d+\.\d+)\b", marked
))
if ("Corollary", "6.6") not in headings or ("Remark", "6.5") not in headings:
    raise SystemExit("Expected v263+ Corollary 6.6 and Remark 6.5 PDF headings")

# This list is intentionally explicit. A new unqualified obsolete citation
# must not silently pass merely because some other statement has its number.
old_references = {
    ("Lemma", "4.5"), ("Lemma", "4.8"), ("Lemma", "9.8"),
    ("Proposition", "9.2"), ("Proposition", "9.6"),
    ("Proposition", "10.3"), ("Proposition", "10.5"),
    ("Corollary", "8.7"), ("Theorem", "8.6"),
}
checked = 0
for m in re.finditer(rf"\b({kind})~(\d+\.\d+)\b", response):
    key = m.group(1), m.group(2)
    if key in headings:
        checked += 1
        continue
    prior = response[max(0, m.start()-115):m.start()].lower()
    if key in old_references and (
        re.search(r"\b(former|submitted|old|original|deleted)\b", prior)
        or (key == ("Lemma", "9.8") and "Props.~9.2" in prior)
    ):
        continue
    raise SystemExit(f"Response references nonexistent revised {key[0]} {key[1]} "
                     f"near source offset {m.start()}")

print(f"Validated {checked} current-manuscript theorem-number references; "
      f"{len(headings)} candidate marked-PDF headings.")
