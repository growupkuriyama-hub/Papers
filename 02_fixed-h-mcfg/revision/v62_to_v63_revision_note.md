# v62 → v63 characteristic-data and appendix compression

## Purpose

v63 performs the second and final planned page-reduction pass. It compresses the characteristic-data section and the normalization appendix while preserving every named result and all mathematical dependencies.

## Safety constraints

- No theorem, proposition, lemma, corollary, definition, open problem, or label was removed.
- Result statements are unchanged.
- Exact reconstruction, TxtEx convergence, the comparison witnesses, and the intrinsic-rank-two Gallot/Bishop argument are untouched.
- The prefix--suffix higher-rank theorem statement and its core skeleton argument are untouched.
- No font, margin, spacing, bibliography, or document-class trick is used.

## Main edits

- Replaced repeated thickness-notation exposition by a compact notation correspondence.
- Compressed proofs of thickness equivalence, reusable canonical contexts, refined-thickness baseline, and the no-splitting criterion.
- Shortened the full-refinement exponential example without changing the family or bound.
- Compressed the rank-one unary-chain argument and theorem proof while preserving its explicit data bound.
- Condensed the appendix bookkeeping for nondeleting, permutation, empty-component, and nonmerging conversions.
- Compressed the two appendix thickness propositions while preserving both quantitative statements and witness constructions.

## Quantitative effect before typesetting

Characteristic-data section: approximately 4314 → 3266 TeX-tokenized words.
Normalization appendix: approximately 1408 → 795 TeX-tokenized words.
Combined reduction: 1661 words.

## Validation

Static checks confirm unchanged theorem-like environment counts, an identical label set, and balanced unescaped braces.  A follow-up safety check restored the explicit rank-one setup for $G$ and $\widetilde G_0$ and retained the audited restriction to Seki et al.'s step (f3). GitHub Actions job `pdfLaTeX — 02 fixed-h MCFG` completed successfully for source commit `110d61f23ac7dc4a63431600b81aad510fe7a2c3`; the final pdfLaTeX pass reports 38 pages (down from 41 pages in v62 and 42 pages in v61).
