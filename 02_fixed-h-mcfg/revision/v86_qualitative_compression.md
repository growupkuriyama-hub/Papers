# #2 MCFG v86 — concise qualitative Yoshinaka (2015) exposition

Date: 2026-10-23. Base: v85 on main. Working PR: https://github.com/growupkuriyama-hub/Papers/pull/68

## Outcome

- English PDF: 51 → 49 pages.
- Japanese PDF: 54 → 52 pages.
- English TeX: 3911 → 3757 lines before final documentation changes.
- Japanese TeX: 4459 → 4239 lines after restoring the Duncan-et-al. scope distinction.
- Bilingual TeX compilation, reference/citation checks: successful in GitHub Actions verify workflow run 39904987700 (final TeX commit 9b35a809...); English and Japanese PDFs were uploaded as PR artifacts.
- Rendered-page visual inspection and independent mathematical proof signoff: NOT yet complete.

## Genuine compression, not reflow

1. Shortened the Introduction's duplicated prior-work discussion without weakening the attribution to Yoshinaka (2008/2011/2015), the companion CFG's public v5 and pinned TCS R1, and the prior nonbranching obstruction.
2. Deleted the unreferenced equal-type illustrative example and removed duplicated prose following the finite-sample SUBST_P equivalence lemma. Kept the formal componentwise type guard and proof of finite-sample language equality.
3. Condensed proofs of the admissible-context lemma, signature-framework embedding, the SUBST_P correspondence, induced-child-context and composition congruence, explicit witness completeness, Gold stabilization, and polynomial-time capped learning.
4. Replaced the redundant Yoshinaka-framework recap after bounded-rank polynomial learning with the already-established cross-references.
5. Condensed the witness-pattern explanation while explicitly distinguishing semantic equality of generated languages from syntactic grammar identity.

## Preserved mathematical scope

- All 60 named theorem/lemma/proposition/corollary/definition statements are byte-identical in English and Japanese to their v85 counterparts.
- All substantive labels remain; only `ex:type-guard-purpose` (unreferenced deleted example) was removed.
- Section 3: typed finite-sort signature, Assumptions 1–3, the `SUBST_D` / `SUBST_P` distinction, direct finite-sample correspondence, and bounded-rank qualitative corollary remain.
- Unbounded rank retains a direct witness, soundness and completeness argument; the v85 Yoshinaka specialization by itself does NOT prove this part.
- Positive-data characteristic-word TOTAL LENGTH bounds, three independent group/LG appendices, rank-two witness and normalization/size-thickness results unchanged.
- The arXiv v5 (#1 CFG) citation remains, with frozen TCS R1 provenance.

## Next editorial gate

Do not force the originally proposed ~45 pages by deleting dependencies in the quantitative or unbounded-rank proofs. Additional reduction requires a separate mathematical audit before altering those arguments. Check all PDF pages visually and obtain independent mathematical validation before journal submission.

This note documents the current condensed draft, not a journal-submission signoff.
