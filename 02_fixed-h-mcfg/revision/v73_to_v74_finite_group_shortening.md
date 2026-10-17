# MCFG #2 v73 -> v74: arbitrary finite-group shortening

Date: 2026-10-18 (JST)
Branch: `revision/02-v74-finite-group-shortening`
Status: pre-submission mathematical revision, pending PR CI, PDF visual inspection, and independent human mathematical review. No arXiv or journal submission is made here.

## Changes

- Preserve the v73 direct zero-sum theorem for a finite **abelian** group and its sharper constant in `appendix_window_abelian.tex`.
- Add `appendix_window_group.tex` and its Japanese mirror, proving polynomial short representatives for **any fixed finite group** without commutativity, using a homogeneous block-order lemma, multicolor finite Ramsey extraction, and a noncommutative prefix-ratio interval lemma.
- Infer the same original-grammar thickness-dependent characteristic positive-data upper bound, `O(||G||^3 max(1,theta_G))`, for fixed prefix/suffix window plus arbitrary fixed finite-group typing.
- Update English/Japanese abstracts, contribution summaries, comparison tables and future-work text. The existing no-group window bound and all prior separations remain unchanged.
- Keep the separate open problem about higher-fan-out lower bounds for **arbitrary finite-monoid** typings: its scope is different.

## Independently checked mathematics

1. Linearity and nondeletion yield disjoint contiguous root blocks for incomparable derivation subtrees.
2. Uniform unary and pairwise block-order patterns imply separated or interleaved type classes. For a class, the rank chunks have a common orientation; region contiguity follows by contradiction.
3. For any finite group and ordered region, if `P_p` and `Q_p` are original and replacement prefix products, the ratio `P_p Q_p^{-1}` detects replacement intervals preserving the entire group product. Multiplication order is preserved; commutativity is never used.
4. Finite Ramsey homogenization plus pigeonhole over at most f class-region group states bounds heavy antichain width by a constant depending only on group order and fan-out.
5. Path-label elimination bounds depth by `|V||A|^f`. Heavy nodes are bounded by antichain width times depth, giving `O(|V| theta_G)` shortest representatives.
6. The existing marked-boundary skeleton step replaces each omitted child by a **same componentwise group-vector** short derivation and therefore does not require commutativity.

A separate Python implementation (rather than copying the exploration program) exhaustively inspected homogeneous configurations for (types,indices)=(2,4), (3,3): 12 and 108 homogeneous orders respectively, and checked their S3 noncommutative interval identities on independently sampled group labels. No counterexample occurred in these **finite** checks. These checks corroborate but do not replace a general proof.

## Constants and scope

Let N=max(3,|A|^f), c=2^(f^2), U=f^(f+1) f!, and M=U*c^[c(N-1)+1]. The explicit representative bound is

`(r_max+1) max(1,theta_G) max(1, (M-1)|V||A|^f).`

These constants are enormous (for S3,f=2, M=2^2248) and should not be advertised as practically small.

The theorem does **not** assert an original-thickness bound for arbitrary finite monoids, and does not claim a novel general learning mechanism beyond Yoshinaka's framework.

## Verification and release gates

- [x] Independent line-by-line argument inspection of the block-order, interval product, and heavy-antichain proof chain.
- [x] Small-parameter independent computational checks.
- [x] Direct identification of the noncommutative multiplication order and separation of the abelian appendix.
- [x] English and Japanese manuscript/appendix sources updated.
- [ ] GitHub English LaTeX compilation and final reference check.
- [ ] GitHub Japanese LaTeX compilation and final reference check.
- [ ] Full PDF visual inspection and final page count.
- [ ] External independent human review of the new lemma chain.
- [ ] Author approval of revised manuscript, AI-use declaration and journal submission details.
- [ ] #1 arXiv v5 citation synchronisation where applicable.

Submission should remain paused if either compilation or substantive review finds a problem.
