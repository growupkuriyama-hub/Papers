# MCFG #2 v82 — finite-semigroup migration, Stage 1

Date: 2026-10-22. Branch: \`mcfg2-v82-semigroup-migration-stage1\`.
Status: **working branch; not submission-ready; no PDF rebuilt on this branch**.
Base: #2 v81 main, cross-checked with #1 TCS-D-26-00494R1 v267 frozen submission (2026-10-22).

## Scope and reason

The companion #1 R1 now takes a surjective finite-semigroup learning bias
\`s: Sigma+ -> S\`, not a monoid bias on all words. Its canonical *fresh*
identity completion \`hat(s): Sigma* -> S-sharp\` evaluates empty yields while
separating them from all nonempty words, even when S already has an identity.
The #2 preexisting semantic definition *already* compares only tuples
in \`(Sigma+)^d\`, so this is a conservative semantic migration: for a
finite-monoid typing \`h0\`, the induced positive semigroup typing
\`s0 = h0|Sigma+\` has exactly the same equality relation on the
observed nonempty components.

## Stage 1 edits committed

1. English title, abstract, keywords and Introduction now state finite
   **semigroup** bias with fresh completion; Japanese corresponding sections
   updated in parallel.
2. English and Japanese §2 have an explicit \`s\`, \`hat(s)\` convention and
   a proved nonempty-tuple transfer lemma \`lem:semigroup-transfer\`.
   The \`(f,s)\` definition and target-class definition are semigroup-first.
3. Refinement \`ker t subset ker s\` and product typing, both understood
   on \`Sigma+\` then freshly completed, are spelled out in the English
   foundation. Japanese semigroup note gives the corresponding kernel
   relations; pre-existing monoid refinement remains as a computational
   representation.
4. The boundary-window monoid \`h_Sigma^{k,l}\` is identified as an
   implementation of its positive semigroup restriction. It already
   distinguishes epsilon by its short-word tag.
5. Three substantive English appendices and all three Japanese mirrors
   document that group-valued morphisms and monoid presentations are
   auxiliary; the algebraic \`LG\` hypothesis is on \`h(Sigma+)\`, NEVER on
   \`S-sharp\`.
6. The English \`kuriyamaCFG\` bibliography now points to the frozen TCS R1
   Clean manuscript and TeX, with the updated semigroup title. The
   semilattice lower bound is R1 Proposition 6.4, not the historical
   version-locked Proposition 6.3.

## What is established by the migration lemma

* Nonempty tuple equality for \`h0\`, \`s0\`, and \`hat(s0)\` is identical.
  The \`(f,typing)\` substitutability classes coincide.
* The set-driven reconstruction grammar compares nonempty observed tuples,
  so for a fixed sample it has exactly the same rules (up to type notation).
  The epsilon start rule is independent of the comparison.
* In a **good** MCFG, all generated nonterminal tuple components are
  nonempty. Thus the *trimmed* typed refinements using either presentation
  correspond after renaming; witness words can be chosen identically.
* Therefore all existing qualitative learning and characteristic-data results
  transfer to positive semigroup biases by using the canonical monoid
  implementation \`M=S-sharp\`. Its size is \`|S|+1\`; the polynomial
  **exponents** in \`||G||\` and original thickness do not change.
* This is NOT the assertion that an old all-fragment CFG condition allowing
  epsilon to be compared with positive fragments is equivalent: #1 R1
  expressly distinguishes this stronger historical condition.

## Scientific / editorial gates still OPEN

1. **Systematic proof-text migration.** Numerous theorem statements and
   proofs still use old monoid parameter \`h\` as a deliberately retained
   implementation notation. Rewrite these one by one as \`s\` statements
   with explicit \`hat(s)\` in the template evaluator, and audit all
   quantifiers. Stage 1 is *not* the completed semigroup conversion.
2. **Core refinement checks.** Re-audit rank-zero and empty-template-factor
   evaluations, start epsilon, good normalization, trimming, witness
   composition, nonmerging and the precise \`h\`-to-\`s\` type renaming.
3. **Quantitative theorem audit.** Recheck the rank-one bound, window
   quadratic bound, finite-group and local-group cubic bounds, and
   rule-only/distributional witnesses with \`M=S-sharp\`. Group morphisms
   such as \`g:Sigma*->A\` remain legitimate auxiliary maps.
4. **Algebraic boundary.** Check LG/Rees reduction and LI∨Grp comparisons
   against primary references and #1 R1 *positive image* claims. Do not
   infer LG membership for \`S-sharp\` from LG membership of \`S\`.
5. **Bilingual source alignment.** This branch synchronizes the semantic
   bridge and appendix scope notes, but not every old occurrence of
   \`monoid/h\` in existing theorem and proof prose.
6. **Presentation issue.** The current English/Japanese Conclusion is
   followed by the important subsection on rare types/two-component
   mobility, rather than coming last; relocate before submission.
7. **Build/CI + visual QA.** LaTeX compilation, cross-reference and
   page-by-page PDF inspection have **not** been executed on Stage 1.
   Existing v81 passing builds are not evidence of v82 builds.
8. **Submission controls.** Keep \`PAPER.yaml\` current_baseline=v81 until
   a complete audited v82 release is built; do not replace the v81 PDFs
   or promote this branch to default main prematurely. Reconfirm novelty,
   AI disclosure and I&C author-guide fields with the author.

## Sources of truth

* #1 frozen TCS R1:
  https://github.com/growupkuriyama-hub/Papers/tree/main/01_fixed-h-cfg/archive/tcs-r1-2026-10-22
* #2 present Stage 1 branch:
  https://github.com/growupkuriyama-hub/Papers/tree/mcfg2-v82-semigroup-migration-stage1/02_fixed-h-mcfg
* #2 v81 audit:
  https://github.com/growupkuriyama-hub/Papers/blob/main/02_fixed-h-mcfg/revision/v81_submission_preflight_review.md

This note is a change log, not a formal proof certification or independent peer review.
