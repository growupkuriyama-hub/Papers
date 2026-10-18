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
- [x] Both languages compile via three successful CI workflows (runs `39120401690`, `39120401767`, `39120401662`); the final reference/citation check passes.
- [x] Verified CI logs contain no overfull hboxes; all long structural formulas retained as displays.
- [x] Source label audit: every theorem/lemma/definition label retained, no duplicates or missing refs. Representative page thumbnails visually checked for main theorem, semilattice lemmas and LG appendix; full human page-by-page mathematical review remains pending.
- [ ] Human review of final I&C submission and scholarly claims.

Caution: number of display pairs in a TeX source is not necessarily the number of equations; `align` and `cases` can contain multiple equations, while `\\[2pt]` is a linebreak spacing command, not a display delimiter.

## Final v84 results

- EN: 43 pages (v83 46); standalone display expressions 65 -> 48 across main and three algebraic appendices; source lines 4438 -> 4274.
- JP: 47 pages (v83 49); standalone display expressions 77 -> 54 across main and three appendices; source lines 4900 -> 4716.
- The original v83 source remains on its own branch; original v82 proofs are archived verbatim.
- Latex CI: overfull hbox 0, undefined final references/citations 0. An underfull hbox warning in one English paragraph does not indicate overflow.
- EN and JP PDFs extracted and inspected from GitHub Actions Verify MCFG artifact run `39120401767`, artifact `12134112260`.
- A JP definition environment initially failed, was corrected, and then passed all CI runs. This correction is included in the SHA256 metadata.
