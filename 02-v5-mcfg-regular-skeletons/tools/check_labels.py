#!/usr/bin/env python3
"""Check that the English and Japanese manuscripts stay in sync.

Compares, between main.tex and japanese/main_JP.tex:
  * the sequence of \\label{...},
  * the set of \\ref/\\eqref targets,
  * the set of \\cite keys and \\bibitem keys,
  * the sequence of theorem-like environments and sectioning commands.
Exit code 0 if everything matches, 1 otherwise.
Usage: python3 tools/check_labels.py   (run from the paper folder)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN = ROOT / "main.tex"
JA = ROOT / "japanese" / "main_JP.tex"

ENVS = ("mainthm", "theorem", "lemma", "proposition", "corollary", "fact",
        "definition", "example", "remark", "openproblem")


def strip_comments(text):
    return re.sub(r"(?<!\\)%.*", "", text)


def extract(path):
    text = strip_comments(path.read_text(encoding="utf-8"))
    labels = re.findall(r"\\label\{([^}]*)\}", text)
    refs = set(re.findall(r"\\(?:ref|eqref)\{([^}]*)\}", text))
    cites = set()
    for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]*)\}", text):
        cites.update(k.strip() for k in group.split(","))
    bibitems = re.findall(r"\\bibitem\{([^}]*)\}", text)
    envs = re.findall(r"\\begin\{(" + "|".join(ENVS) + r")\}", text)
    sections = re.findall(r"\\(section|subsection)\*?\{", text)
    return dict(labels=labels, refs=refs, cites=cites, bibitems=bibitems,
                envs=envs, sections=sections)


def main():
    en, ja = extract(EN), extract(JA)
    ok = True
    for key in ("labels", "bibitems", "envs", "sections"):
        if en[key] != ja[key]:
            ok = False
            print(f"MISMATCH in {key}:")
            print("  EN:", en[key])
            print("  JA:", ja[key])
    for key in ("refs", "cites"):
        if en[key] != ja[key]:
            ok = False
            print(f"MISMATCH in {key}: EN-only={sorted(en[key]-ja[key])} "
                  f"JA-only={sorted(ja[key]-en[key])}")
    for name, data in (("EN", en), ("JA", ja)):
        missing = sorted(data["refs"] - set(data["labels"]))
        if missing:
            ok = False
            print(f"{name}: references without label: {missing}")
        nocite = sorted(data["cites"] - set(data["bibitems"]))
        if nocite:
            ok = False
            print(f"{name}: citations without bibitem: {nocite}")
    print(f"labels={len(en['labels'])} envs={len(en['envs'])} "
          f"sections={len(en['sections'])} cites={len(en['cites'])}")
    print("OK" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
