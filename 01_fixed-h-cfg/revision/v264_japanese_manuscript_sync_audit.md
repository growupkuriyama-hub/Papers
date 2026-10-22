# TCS-D-26-00494 — v264 Japanese manuscript synchronization audit

**Date:** 2026-10-22  
**English source of truth:** `01_fixed-h-cfg/main.tex` (EN v263, Git blob `a02a8036141c3ebb6b7de6f73c4d9421174e0172`)  
**Japanese synchronized source:** `01_fixed-h-cfg/japanese/main_JP.tex` (JP v264, Git blob `a64ec35acb4b2aaa2ea760e491c9c93e0624ff57`)

## Source integrity

- English SHA-256: `4059d10a664ca8c6742a2a901c4589095825f99db7c8d46f383662a31bce4e95`
- Japanese SHA-256: `b0fe88a9ba6dac7321fb35bdeffd3292aea10ed9b2f6eb3dc29693fc17bf58b3`
- English `main.tex` and the `TCS-D-26-00494_Manuscript_Clean.tex` mirror were identical in the approved EN v263 release.
- Only the Japanese manuscript source was altered for v264. English theorem statements, proofs, response, marked PDF, and submission package are unchanged.

## Bilingual structure audit

| Structural feature | English | Japanese | Outcome |
|---|---:|---:|---|
| Sections | 13 | 13 | Same |
| Subsections | 17 | 17 | Same |
| Proof environments | 39 | 39 | Same |
| Numbered theorem-like environment sequence | 42 | 42 | Identical order |
| Cross-reference labels | 59 | 59 | Identical order and keys |
| Bibliography keys | 25 | 25 | Identical order |
| Citation commands | 61 | 61 | Identical order and citation keys |
| Footnotes | 2 | 2 | Same |
| Tagged equations | 3 | 3 | Matching tags (`spadesuit`, `star`, `star-star`) |
| Enumerate environments and items | 8 / 24 | 8 / 24 | Same |
| Unresolved LaTeX label references | 0 | 0 | Same |

Displayed-math differences consisting only of Japanese `\\text` phrases, punctuation, and display-vs-inline layout were examined separately. The v264 work leaves no known unmatched main result or proof environment.

## Substantive v264 corrections

1. **Section 5.1:** Added the omitted justification for Rule (U) from shared reaching contexts and witness words for nonempty-type symbols; explicitly restored the empty-type exception and the limited logical role of typing.
2. **Section 3:** Replaced outdated Japanese-only commentary on Gold/Yoshinaka with the present English statement of fixed-slice versus union-class nonlearnability.
3. **Section 5 complexity:** Replaced a JP-only assertion about de la Higuera's Theorem 3 and obsolete BUNF description by the current English doubling-grammar observation.
4. **Section 7:** Added the exact Eyraud–Heinz–Yoshinaka Definition 2.5 citation and aligned the proof-variable names `T,H,V` of the U1 obstruction lemma.
5. **Section 7 post-corollary:** Removed Japanese-only extended algebraic claims and reproduced the English description of the pseudovariety join, including `s(Sigma+) in LI join Grp`.
6. **Section 8:** Restored the exact comparison to Clark–Eyraud and fixed-window classes in the nonregular-linear example introduction.
7. **Section 2:** Removed an extra Japanese-only footnote about sample size, already covered by the shared prose.
8. Performed structural, label, citation, theorem-order, technical-variable, quantitative-bound, and cross-reference checks on all main sections and appendices.

## Build and submission boundary

- GitHub Actions [Publish TCS #1 EN+JP PDFs](https://github.com/growupkuriyama-hub/Papers/actions/runs/39714304361): **PASSED** on 2026-10-22; Japanese PDF rebuilt at **30 pages**, English Clean PDF **26 pages**.
- The prior English v263 marked manuscript and reviewer response were verified in [revision package workflow](https://github.com/growupkuriyama-hub/Papers/actions/runs/39712559378): 26/14 pages, 49 reviewer-response items, 77 exact marked-PDF anchors, 3-file ZIP.
- **Out of scope:** `response/japanese/` is a separate historical v229 Japanese reviewer-response translation; it is **not** synchronized to EN v263 and should not be treated as current.
- **No Editorial Manager upload or resubmission** was performed. This is a document synchronization audit, not a mechanized proof of mathematical theorem correctness or an independent professional translation certification.
