# v84 — I&C inline-math and concise-prose editing pass

Date: 2026-10-18  
Status: Draft; not merged, not submitted

## Exact reversible baseline

Original pre-edit v83 paper: branch `mcfg-v83-ic-focused-trim`, GitHub Draft PR #52. All complete archived v82 proof fragments remain in `archive/trim-v83/`. Version v84 edits only reading flow and typesetting of the active English/Japanese paper and its original algebraic appendices.

## Edits

- Condensed EN/JP Introduction, Yoshinaka comparison and Conclusion. Retained the distinction between Yoshinaka's earlier qualitative learning/signature results and new quantitative bounds. Kept the mathematical claims on rank one, windows, finite groups, LG and semilattice-indexed abelian cosets, the open higher-fan-out lower-bound problem and the disclosures.
- Replaced short, otherwise isolated display math with inline math in the main TeX and three appendices of each language.
- Kept long derivations, semilinear integer-programming equations, paired quantitative bounds, case definitions, grammar rules and principal theorem formulas displayed when necessary for legibility.
- Restored the Yoshinaka multidimensional substitutability definition's original LaTeX label `def:yoshinaka-pd-substitutability` after condensation.
- No new mathematics was introduced, and no proof hypothesis or theorem bound was intentionally weakened or extended.

## Quality-gate checklist

- [x] Bilingual source edits complete; v83 and v82 remain independently restorable.
- [x] All eight TeX source SHA-256 records synchronized in PAPER.yaml.
- [x] Cross-file labels and reference count: no undefined or duplicate labels.
- [ ] CI compiles both PDFs and checks references/citations.
- [ ] Scan for overfull math caused by inline conversion; if present, restore selective displays.
- [ ] Compare major theorem proofs and counts in PDFs with v83 baseline.
- [ ] Human review of final I&C submission and scholarly claims.

Caution: number of display pairs in a TeX source is not necessarily the number of equations; `align` and `cases` can contain multiple equations, while `\\[2pt]` is a linebreak spacing command, not a display delimiter.
