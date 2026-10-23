# v91 — Higher-arity sliding obstruction and local-group main-text presentation

Date: 2026-10-23. Target: Information and Computation. Status: working revision; not submitted.

## Selected inputs

A Claude review of the pre-v90 manuscript raised points M1–M8. We adopted
M1's request to explain why discontinuous, noncommutative blocks cannot be
shortened by preserving each child independently; M2's request to present the
local-group theorem in the paper's quantitative main text; and M3's novel
two-dimensional nonmembership argument. M4 had already been resolved in
v90 through the explicit SUBST_D versus SUBST_P distinction. We intentionally
retain the positive-semigroup/fresh-identity distinction and the version-locked
companion manuscript reference.

## Mathematical changes

1. The local-group theorem now appears in Section 4 with the original exact
   assumptions and cubic bound. Its detailed proof stays in the LG appendix.
2. A new sliding-separator lemma uses at most |S|^2 possible componentwise
   types at distinct internal occurrences of one separator.
3. A new no-lift proposition shows: for every fixed finite semigroup typing
   s with target semigroup S, the companion doubling pair L_n, L_n^- fails
   (2,s)-tuple substitutability for n >= 2|S|+3. This exploits eventual
   periodicity of powers of the left-bracket type and a binary-to-unary
   substitution at a fixed point of the left spine. It is NOT a
   higher-fan-out data-length lower bound.
4. The higher-fan-out open problem now explicitly excludes naive transfer
   of the companion doubling family and points to the distributional
   representative-length obstruction.
5. The abelian-filtered target proof has an explicit RHS and parameter
   dependence remark; the main-text novelty explanation distinguishes
   group-block order from naive tuple pruning.

## Preserved

- v90's additional finite-Ramsey qualitative proof of noncommutative block
  replacement and the original explicit polynomial-order bound.
- v90's minimal-ideal and Rees-coordinate local-group proofs.
- The sharp asymptotic claims (quadratic window; cubic window-group and LG).
- Yoshinaka 2011/2015 attribution and SUBST_D/SUBST_P caveat.
- Positive image s(Sigma^+) versus fresh identity completion.
- The existing AI-use disclosure.

## Verification gates

Bilingual LaTeX compilation and reference/citation check, merged PR
validation, published PDF checks, and mathematical review of the
new no-lift proof are necessary. Automated tests do not establish
the universal theorem by themselves. No arXiv or I&C submission is included.
