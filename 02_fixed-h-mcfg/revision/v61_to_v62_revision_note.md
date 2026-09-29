# v61 → v62 comparison-section compression

## Purpose

v62 is a page-reduction pass confined to Section 5, “Comparison with Multidimensional Substitutability.” It shortens repeated exposition and proof narration without changing the mathematical architecture.

## Safety constraints

- No theorem, proposition, lemma, definition, corollary, or label was removed.
- Named result statements are unchanged.
- The intrinsic-rank-two subsection and its Gallot/Bishop lower-bound proof are unchanged.
- Reconstruction, TxtEx, complexity, and characteristic-data sections are unchanged.
- No font, margin, spacing, or document-class compression was used.

## Main edits

- Compressed the proof of the prefix–suffix semantic specialization.
- Compressed the same-typing filter proof.
- Shortened the four-part proof for L_cd while preserving each witness and separation.
- Shortened the COPY pigeonhole/context argument.
- Compressed the strictly-2-local boundary lemma proof.
- Compressed the H_m substitution rectangle by removing parity narration and combining definitions.
- Shortened the arbitrary-filter comparison.
- Compressed the typed-membership and DFA-pumping parts of the L_star proof.

## Quantitative effect before typesetting

The comparison section decreases from approximately 6209 to 5066 TeX-tokenized words, a reduction of 1143 words (about 18.4%).

## Validation

Static checks confirm unchanged theorem-like environment counts, an identical label set, and balanced unescaped braces. Full pdfLaTeX CI and the resulting page count will be recorded after the build.
