# MCFG v52 -> v53 revision note

## Purpose

v53 closes the primary-source citation audit requested by the pre-submission
review.  The exact numbered references used in the main Yoshinaka/Seki
comparison chain were checked directly against the canonical PDFs stored in
Research-Library, rather than against secondary notes or bibliographic cards.

## Primary-source checks

For Yoshinaka (2011), the PDF confirms the manuscript's use of:

- Section 2.3 / Lemma 1 for good-form and nonmerging normalization;
- Section 3.1 and footnote 3 for the nonempty-component convention;
- Examples 3 and 5 for the fan-out/substitutability examples;
- Algorithm 1 and Lemmas 5--7 for the conservative learner, completeness,
  polynomial construction, and characteristic-data bounds;
- Proposition 4 for the fixed-dimension/fixed-rank membership bound;
- Definition 1 and Theorem 1 for the polynomial-time-and-data criterion;
- Corollary 2 for the unbounded-rank qualitative learner.

For Seki et al. (1991), the PDF confirms the manuscript's use of:

- Lemma 2.2 for the information-lossless/nondeleting normalization;
- Lemma 3.3 for the equal-block fan-out lower bound used in the H_m argument;
- Theorem 3.9 for substitution closure, hence homomorphism closure.

## Textual changes

Three citations were tightened:

1. the nonempty-component convention now points to Yoshinaka Section 3.1 and
   footnote 3 rather than to the paper generically;
2. the Seki et al. Lemma 3.3 citation now includes p. 202;
3. the Seki et al. Theorem 3.9 citation now includes p. 203.

No mathematical statement or proof changed.
