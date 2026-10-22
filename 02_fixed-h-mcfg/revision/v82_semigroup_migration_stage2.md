# MCFG #2 v82 — semigroup migration, Stage 2

Date: 2026-10-22. Target: Information and Computation.
Working branch: \`mcfg2-v82-semigroup-migration-stage1\`.
Base: #2 internal v81 and the frozen #1 TCS-D-26-00494R1 v267.
**Status: working revision, not submitted.** Never treat current main-branch
PDFs (v81) as compiled v82 PDFs; do not merge to main without signoff.

## Semantics inherited from #1 R1

A typing means a finite positive-semigroup morphism
\`s : Sigma+ -> S = s(Sigma+)\`.
For nullable template evaluation only, adjoin a **fresh** unit
\`1_sharp\`, even if \`S\` already has its own identity, and use
\`h=hat(s) : Sigma* -> S-sharp\`. All nonempty observed MCFG components
are compared by the positive kernel. For any legacy finite monoid
\`h0 : Sigma* -> M0\`, restricting to its positive image and freshly
completing leaves the tuple substitutability class and the exact set-driven
reconstruction grammar unchanged. In a **good** MCFG, productive trimmed
nonterminal yields all have nonempty components, allowing the same
witness words after renaming the type indices. This is the semantic
transfer lemma now proved in both texts. It does **not** assert
equivalence with an all-fragment historical condition that compares
epsilon against positive words.

## Stage 2 changes made

1. English/Japanese main quantified the exact reconstruction theorem,
   Gold/TxtEx corollary, polynomial update theorem, rank-one theorem,
   prefix-suffix quadratic bound, LI/Grp quantitative corollary and
   abelian-filtered theorem over positive semigroup \`s\`. Existing
   computational notation \`h=hat(s)\` is bound explicitly in the statements.
2. Positive image \`S\`, not \`S-sharp\`, is the \`LI\`, \`LI∨Grp\` or
   \`LG\` object. Abstracts now say “positive-image semigroup outside LG,”
   not “control monoid outside LG.”
3. The local-group/window–group factor lemma and its proof now quantify
   the semantic semigroup typing and distinguish its projected
   locally trivial factor \`sigma\`; the Japanese copy was corrected to
   avoid confusing the two maps.
4. The rare-type deletion lemma is for \`m in S\` and removes the
   **positive fiber only**. Its proof uses \`h=hat(s)\` to ensure epsilon
   is preserved. The corresponding positive rare-type lower bound is
   quantified over \`m in s(L ∩ Sigma+)\`.
5. The local Ramsey-shift lemma explicitly uses \`h=hat(s)\`:
   certain auxiliary subfactors in its coloring can be empty, and
   thus cannot be evaluated by \`s\` alone.
6. The universal bracketed-doubling nonmembership theorem now states
   \`n >= 2|S|+3\` for an arbitrary finite semigroup typing;
   the proof uses powers of the positive type and no longer shadows
   the morphism symbol with an integer index.
7. The higher-fan-out open problem is likewise semigroup-quantified.
   The previously misplaced rare-type/mobility material, including
   the fixed-window nonmembership proof, now precedes the final Conclusion.
8. Both source sets use the same theorem environment ordering.
   The three EN appendices and three JP appendix counterparts document
   how their group and local-group implementation maps relate to \`s\`.
9. Bibliography and README point to the frozen #1 R1 manuscript, not
   to the older finite-monoid companion version; \`PAPER.yaml\` retains
   v81 as the frozen baseline and advertises draft v82 separately.
10. A separate GitHub Actions workflow builds both language variants
   **on this branch only**, without publishing PDFs to main:
   \`/.github/workflows/check-mcfg-semigroup-v82.yml\`.

## Checks and caveats

* Static source scan (including all six external appendices):
  **no duplicate LaTeX labels**, **no missing internal refs** and
  matching EN/JP theorem-environment sequences.
* First branch-only EN/JP compile passed. A later intermediate
  build exposed an accidentally unclosed math delimiter in the
  translated higher-fan-out open problem; this was fixed, and a
  subsequent EN/JP compilation passed (see Actions branch history).
  Every further TeX change must pass its **own** final workflow run.
* Compilability and this transfer proof are **not** certification of
  the local-group/Rees reduction, arbitrary-group order homogenization,
  nonmerging witness composition, or the abelian-filter quantitative proof.
  These remain independent author/expert audit targets.
* The general fan-out >= 2 superpolynomial characteristic-length lower
  bound remains **open**. The nonmembership theorem for the doubling
  family does not supply such a bound.
* The final PDF needs full-page visual review, in particular long
  displays, English/Japanese theorem numbering, bibliography and
  underfull/overfull warnings.
* Full rewording of every legacy computational monoid occurrence is
  **not** necessary for soundness, but every occurrence must be
  classified as a representation, an auxiliary group, or the actual
  positive learning bias before submission.
* The working branch does not modify v81 PDFs, the public arXiv
  preprint, or the TCS #1 R1 archive.

## Verification references

* Branch: https://github.com/growupkuriyama-hub/Papers/tree/mcfg2-v82-semigroup-migration-stage1/02_fixed-h-mcfg
* Actions branch history: https://github.com/growupkuriyama-hub/Papers/actions/workflows/check-mcfg-semigroup-v82.yml
* Frozen #1 source: https://github.com/growupkuriyama-hub/Papers/blob/bbbcabfd948dea815b94bd21a3d78999a6a3e54f/01_fixed-h-cfg/archive/tcs-r1-2026-10-22/TCS-D-26-00494_Manuscript_Clean.tex
