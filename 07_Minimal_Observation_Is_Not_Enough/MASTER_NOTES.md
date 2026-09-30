# MOINE — Research Master (Minimum Observer Size Is Not Enough)

Date: 2026-09-30  
Status: focused journal-candidate v1

## 1. Design objective

This manuscript replaces the broader bridge paper *Observation Is Not Enough*.

Optimization target:

- minimum manuscript length;
- independently submit-able after #1 and #2;
- maximum impact as the third paper in the dissertation *Identification in the Limit beyond Fixed Observation*.

The paper is not a compressed table of contents of #3 + OFET + old #7. It is a theorem paper with one narrative.

## 2. Narrative

fixed observation  
→ bounded unknown observation as background  
→ refinement monotonicity / safe-congruence frontier  
→ minimum observer image versus minimum reconstruction  
→ universal-observer penalty and affine reconstruction geometry

The key conceptual distinction is:

- **class-level sufficiency:** bounded finite observation is enough for TxtEx learning (background compilation principle);
- **order-level monotonicity:** finer observers remove reconstruction links;
- **resource-level separation:** minimum image cardinality need not select the reconstruction-optimal maximally coarse safe observer.

## 3. Headline results

### A. Refinement and kernel theorem

The current manuscript proves that #1 Rule (R3) and #2 Rule (Link) depend only on observer equality, hence only on (ker h).  Along the refinement order, a finer observer yields a subgrammar and cannot reduce characteristic-data cost.

### B. (R_{m,q}): exact frontier separation

The streamlined proof now contains a complete classification of all overlapping unequal factor distributions.  This closes the safety proof for (H^-) and (H^+).

Main exact statements:

- (mathrm{obs}_1(R_{m,q})=qm);
- (H^-) and (H^+) are both maximally coarse safe and incomparable;
- (mathrm{CD}_{min	ext{-image}}=4(m^2+2qm-m));
- (mathrm{CD}_{mathrm{global}}=4(m^2+qm+q-1));
- (Delta mathrm{CD}=4(m-1)(q-1)).

The sample-graph iff has been rewritten against the actual #1 R1--R5 rules.

### C. Universal-observer penalty

The bounded-unknown-observer product theorem is retained as background, not counted as a new contribution.  Combined with refinement monotonicity and the exact (R_{m,q}) cost formula, a sufficiently rich universal observer forces (kappa=m^2) and therefore requires the entire finite target as characteristic data.

### D. (X_{k,r}): exact affine geometry

The headline is no longer the bare scalar “obs=1 but cost unbounded” statement.  The substantive result is the exact affine formula

[
|C|_{min}=1+r(k-1).
]

The affine invariant has been rewritten directly in terms of #2 Start/Const/Comp/Link, including the half-contained-slot case.  For (X_{2,r}), this gives (r+1) examples and encoded cost ((2r+1)(r+1)).

## 4. What was intentionally cut

Do not restore unless a referee specifically requires it:

- full SCL theory;
- pseudovariety trichotomy;
- Clark--Wurm arity sequence 1,2,2,... as a headline result;
- relational morphisms;
- general Pareto/Dickson theorem;
- weighted objective phase transition;
- OFET higher-rank arithmetic/scheduling/hierarchy;
- rank-four computational census.

These are interesting but dilute the third-paper thesis narrative.

## 5. Proof audit priorities

Before journal submission:

1. independently re-audit the new complete conflict classification and maximally-coarse-safe proposition;
2. independently re-audit the expanded R1--R3 incidence-graph proof;
3. independently re-audit the revised Start/Const/Comp/Link affine invariant;
4. compile twice; current static audit has balanced environments/braces and no undefined refs/cites;
5. refresh literature priority around minimum quotient size versus characteristic-data optimization;
6. test whether an infinite-language analogue of the maximally-coarse-safe separation is worth adding, without diluting the focused paper.

## 6. Submission posture

The paper should be presented as a new focused theorem contribution, not as a survey or merger.

The main novelty claim should be scoped to the joint optimization problem over the same finite-observer space:

- minimum safe observation versus
- minimum positive reconstruction evidence.

Do not claim learner-independent sample-complexity lower bounds.

## 7. Dissertation role

The target dissertation can now be extremely compact:

1. #1 — CFG under fixed finite observation
2. #2 — MCFG under fixed finite observation
3. MOINE — beyond one fixed observer and limits of minimal observation

No separate #3 / OFET chapter is required for the minimal high-impact track.

## 8. Public-preprint overlap gate

`06_ofet` is public as arXiv:2609.34560v1 and already contains predecessor versions of the `R_{m,q}` exact resource formulas and the `X_{k,r}` affine characteristic-data argument (under the slot observer). The focused paper-07 path is viable only if treated transparently as a sharpening/superseding version of those overlapping portions.

New sharpenings isolated in paper 07 include:

- reconstruction/kernel invariance and congruence-index formulation;
- two incomparable maximally coarse safe observers on `R_{m,q}`;
- the universal-product "whole target" penalty;
- trivial-observer safety and exact affine cost for `X_{k,r}`;
- proof alignment to the current #1 R1--R5 and #2 Start/Const/Comp/Link constructors.

Submission gate: do not pursue independent journal publication of both overlapping theorem packages without removing the duplication or following the target venues' explicit extended-version policy.
