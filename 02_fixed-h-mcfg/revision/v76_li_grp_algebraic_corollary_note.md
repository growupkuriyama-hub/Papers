# #2 fixed-h MCFG — algebraic sufficient conditions (v76 candidate)

Date: 2026-10-18. Working branch: \`mcfg2-v76-algebraic-corollary-chatgpt\`.
Base: Claude's draft branch \`mcfg2-v76-strengthening-drafts\` at commit
\`a265729464ad2e584e474f1750252ceedd26dd5f\`.
**This is a candidate revision, not a journal or arXiv submission.**

## New statements

- Lemma \`lem:mcfg-li-group-window\`: If the **positive image semigroup**
  \`h(Sigma^+)\` belongs to \`LI join Grp\`, then \`h\` is refined on **all**
  of \`Sigma^*\` by a prefix/suffix window paired with a morphism into a
  finite group. The proof lifts letter values into a subsemigroup of a
  product of a locally trivial finite semigroup and a finite group;
  local triviality gives a positive-word window. The window's empty-word
  isolation extends the kernel inclusion from positive words to all words.
- Corollary \`cor:mcfg-li-group-polydata\`: Original-thickness total positive
  length is \`O(||G||^2 theta_bar)\` for positive image in \`LI\`, and
  \`O(||G||^3 theta_bar)\` for positive image in \`LI join Grp\`, with
  fixed alphabet, typing, fan-out and rank, for reduced good presentations
  of targets in the relevant typed-substitutable class.
- English and Japanese abstract, introduction, conclusion, mathematical
  lemma, corollary and references updated symmetrically.

## What this does and does not claim

- It is a **deduced sufficient condition** from the finite-semigroup
  window characterization proved in the companion TCS #1 manuscript
  and the window--finite-group total-length theorem of #2.
- It **does not** prove a converse, any semigroup classification/dichotomy,
  a universal arbitrary-monoid bound, an optimal exponent, or the
  higher-fan-out lower-bound open problem.
- Additional bibliographic references: Costa (2002) two papers in the
  research Project Source 07; Pin (1986), and the version-locked companion
  CFG manuscript. The Costa joins provide algebraic context, not the
  MCFG learning theorem itself.

## Independent review gates

1. Verify the locally trivial semigroup identities used for the chosen
   finite \`S_0\`, and their application when the middle substring is empty.
2. Confirm the kernel inclusion and the fixed-parameter quantifiers, including
   the epsilon versus nonempty case and the trivial-group specialization.
3. Inspect the proof of the arbitrary finite-group theorem from #2
   Appendix D separately. The algebraic corollary inherits its status.
4. English/Japanese CI build, full-PDF page review, author signoff.
5. The separate v76 draft PR's new order-homogenization lemma and
   minimum-weight witness algorithm require their own independent
   mathematical review; this note does not certify them.

Do not count successful compilation or an AI review as an external mathematical proof audit.
