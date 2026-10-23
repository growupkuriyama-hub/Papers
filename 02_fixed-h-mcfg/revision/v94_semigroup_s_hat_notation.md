# MCFG #2 v94 — semigroup typing notation harmonization

Date: 2026-10-23.

## Objective
Match companion TCS #1 (\`01_fixed-h-cfg/main.tex\`): the **positive-word**
surjective semigroup morphism
\(s:\Sigma^+\twoheadrightarrow\mathsf S\) defines the substitution bias,
while its **fresh-identity monoid completion**
\(\widehat{s}:\Sigma^*\twoheadrightarrow\mathsf S^\sharp\)
handles empty terminal pieces and the yield-type refinement.

## Changes
- Re-index tuple-substitutability, the target class \(\Cmcf{f}{s}\),
  distributional equivalences, reconstruction \(\mathcal B_{f,s}\),
  conservative learner \(\mathcal A_{f,s}\), and the signature by \(s\).
- Write \(\widehat{s}\) explicitly for the total map in output evaluation;
  use \(\mathsf S^\sharp\), \(|\mathsf S^\sharp|\) rather than an otherwise
  unnecessary global monoid symbol \(M\).
- Write \(\widehat{s}_\Sigma^{k,\ell}\) for the full prefix--suffix map
  and \(s_\Sigma^{k,\ell}\) for its positive restriction.
- Preserve auxiliary finite groups, their maps, the semigroup-transfer
  lemma, and the **positive-image** nature of \(\mathbf{LG}\).
- Harmonize all source-included English and Japanese appendices.

## Invariants and validation requirements
- **Do not** equate an existing identity of \(\mathsf S\) with the *fresh*
  identity of \(\mathsf S^\sharp\).
- Do not compare the empty word with a nonempty tuple component in a
  substitutability test.
- Do not impose local-group membership on the completed monoid.
- All lemma/theorem/corollary labels and proof arguments should remain
  checkable through the manuscript; numerical bounds are unchanged.
- Run EN/JP LaTeX build, cross-reference/citation checks, and manual notation
  review on the source and on the generated PDFs.
