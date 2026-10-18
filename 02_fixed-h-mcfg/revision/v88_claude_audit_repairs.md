# MCFG #2 v88: independent-review repairs and verification gates

Date: 2026-10-19. Source review: `MCFG_v87_Independent_Adversarial_Mathematical_Audit.md` (Claude/Opus, based on v87 commit `e24a6cbc71467035a25d259631d43b47b46d385e`). This report is a **response to an external AI audit**, not an independent formal proof certificate.
Baseline preserved on `mcfg-v87-tcs-style-review-preflight`, PR #57. This v88 change is review-only, not merged to main or submitted.

## Mathematical corrections

- **F-01 / F-09 (LG transfer)**: added `lem:ordered-product-interval` to the finite-group appendix, proving a common preserved interval for abstract ordered products of fixed and variable group slots, without commutativity. Strengthened `lem:local-group-blocks` to quantify uniformly over all subsets of window-preserving block replacements. Added `lem:lg-heavy-antichain` with a full derivation-tree proof, and replaced the `verbatim` appeal inside `lem:local-group-shortest` with a direct application and depth count. All changes mirrored in English/Japanese.
- **F-02 (incorrect computability scope)**: narrowed `prop:effective-char-data` and its proof to bounds based on **generated canonical tuples and derivational contexts**. Explicitly exempted the existential semilattice-coset `K^\dagger` bound, which can be much shorter than any generated witness set (the v87 review supplies the exponential grammar family counterexample).
- **F-03 (unproved exact identification)**: removed the `exactly the finite-sort class` / `same language on each sample as SUBST_P` claim; correctly treats Yoshinaka's qualitative framework as background, not as an exact unproved algorithm equivalence.
- **F-04 (LG attribution)**: acknowledges Straubing/Tilson `G*D` window construction as classical and states the explicit `k=|S|` version for the present proof.
- **F-05 (LI∨G inclusion)**: derived directly from `LI,G\subseteq LG` plus pseudovariety closure; retains the companion CFG factorization to establish *strict* inclusion.
- **F-06 (group-heavy-antichain wording)**: specifies that **each** antichain subtree is above the thickness threshold and that the derivation is shortest from a fixed nonterminal with fixed root group values.
- **F-08 (conditional lower bound)**: qualified the companion-CFG lower-bound claim to the class of set-driven operators having characteristic samples for both distinguishing targets.
- **F-07 (notation, legacy label)**: Not mechanically renamed. Localized notation collisions do not invalidate proof; changing the externally used legacy label `thm:mcfg-abelian-filter-data` or all Rees-action symbols now risks needless cross-reference churn. Treat as optional copyediting.
- **F-10 (normalization sources)**: source attribution and dependent assumptions retained; original sources require separate human verification. No additional unverified theorem added.

## Claims deliberately unchanged

`thm:local-group-polydata` continues to give total length `O(||G||^3 thetaBar)`. The semilattice `3|Sigma|+1` / `3|Sigma|+2` exponents and their proofs are unchanged. Rank-one and fan-out-two-separation statements are unchanged. The unresolved higher-fan-out lower-bound problem remains open. Manuscript and archived mathematical results are not deleted.

## Testing and review gate

- [x] EN/JP static compiled-source label audit: 0 unresolved references, 0 duplicate labels.
- [x] EN/JP begin/end environment counts balanced after inserting new lemmas.
- [ ] EN/JP GitHub Actions PDF compilation and unresolved-reference check.
- [ ] PDF page-count and overfull math/line inspection.
- [ ] Independent adversarial re-audit **of the v88 patch**, especially common block-slot factors in noncommutative group products and the new LG antichain proof.
- [ ] Citation original-source checks (Papadimitriou, Straubing/Tilson, normalization) and author signoff.

Avoid silently upgrading the review's `VALID WITH REPAIR` status to `VERIFIED` until an independent checker assesses the new proof, including all possible block interleavings.
