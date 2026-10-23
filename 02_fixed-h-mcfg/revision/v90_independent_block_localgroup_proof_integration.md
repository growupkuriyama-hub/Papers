# MCFG #2 v90: independent noncommutative / local-group proof integration

Date: 2026-10-23. Status: working proof-readability revision (not a new mathematical claim or a submission).

## Mathematical purpose

The independent 2026-10-23 audit reconstructed noncommutative block replacement
and local-group shortening by an alternative proof route. This revision integrates
the arguments into the active English and Japanese manuscripts **without changing
the theorems, hypotheses, the explicit threshold** \(M_{A,f}\), **or the**
\(O(\|G\|^3\bar\theta_G)\) **bound**.

## Noncommutative block-replacement appendix

1. An additional qualitative proof uses finite multicolor Ramsey: select owners
   with equal within-owner block patterns; color owner pairs by all cross-type
   comparisons; choose a homogeneous subsequence; split each line into
   rank-ordered regions.
2. In each region, original and substituted prefix products \(P_j,Q_j\)
   yield \(\kappa_j=P_jQ_j^{-1}\). Equal boundary states supply a nonempty
   interval of owners preserving every line product, without commuting factors.
3. The original explicit monotone-comparison extraction is retained, recovering
   the stronger polynomial-in-\(|A|\) threshold. Finite Ramsey alone does
   **not** establish that sharper asymptotic dependence.

## Local-group appendix

1. Direct algebraic argument: for every idempotent \(e\in S\), and \(a\) in
   the minimal ideal \(K\), \(eae\in K\cap eSe\) has an inverse \(y\in eSe\)
   when \(S\in\mathbf{LG}\); therefore \(e=(eae)y\in K\).
   The elementary semilattice implications and the completely-simple converse
   are also displayed.
2. Spell out both Rees-coordinate invariants: right multiplication of
   \(z\in K\) preserves its \(I\)-coordinate; left multiplication preserves
   its \(\Lambda\)-coordinate.
3. Shortening separates window-preserving replacement candidates from the
   selection of a nonempty set whose *combined root* noncommutative group
   values are preserved; individual replaced subtrees need not retain
   their group values.
4. Hence \(\beta_{\mathrm w}=O(\|G\|\bar\theta_G)\),
   \(\beta_\lambda=O(\|G\|^2\bar\theta_G)\), and
   \(O(\|G\|)\) rule witnesses again imply the cubic total-length bound.

## Active sources modified

- English manuscript: main.tex, appendix_group_blocks.tex, appendix_local_group.tex
- Japanese manuscript: japanese/main_JP.tex,
  japanese/appendix_group_blocks_JP.tex,
  japanese/appendix_local_group_JP.tex
- Revision tracking: PAPER.yaml

Excluded legacy appendices are unchanged.

## Remaining release gates

1. Complete English/Japanese LaTeX build, labels and bibliography validation.
2. Confirm statement/assumption/bound invariance and review PDF renders.
3. Independent full-paper proof review outside this focused audit, including
   normalization, Yoshinaka-signature coverage and the abelian-filtered theorem.
4. Author approval prior to I&C submission.

Finite tests described in the 2026-10-23 independent audit are evidence of
additional checking, **not** formal proof certificates. The existing disclosure
of AI assistance is unchanged. No journal submission or arXiv upload is part
of this revision.
