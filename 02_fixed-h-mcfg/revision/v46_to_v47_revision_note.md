# MCFG v46 -> v47 revision note

## Purpose

v47 responds to the second independent pre-submission review of v46.  The main correction is conceptual rather than theorem-level: v46 incorrectly described the trivial-typing Type-I part of Yoshinaka's finite-sample grammar as strictly broader than the present composition-witness constructor.  Rechecking Yoshinaka (2011), Section 4.1 and the proof of Lemma 6 shows that the two Type-I constructions coincide (up to notation and the separate treatment of the empty word).  v47 corrects that attribution and repositions the paper around the genuinely new typed, quantitative, and separation results.

No headline theorem is withdrawn, and no new minimum-rank-two separation theorem is added.

## Main changes

1. **Corrected the Yoshinaka Type-I comparison (major positioning fix).**
   Proposition `prop:yoshinaka-type-guard` now states the exact relationship:
   - under trivial typing, the capped reconstruction agrees with Yoshinaka's `G(K)` for `A(f,r)`, apart from notation and the direct `eps` start convention;
   - for a general finite typing `h`, the reconstruction is obtained by deleting exactly those Type-II / Link rules whose source and target tuples have unequal componentwise `h`-types;
   - the same statement holds for the uncapped construction and Yoshinaka's `A(f,*)`.
   The proof now gives both directions of the Type-I <-> (Const)+(Comp) correspondence and cites Yoshinaka's single-sample-word factorization count.

2. **Removed the unsupported “sample-local reconstruction” novelty claim.**
   All claims that the present Type-I/Comp architecture is stricter than Yoshinaka's have been deleted.  The abstract, Contributions, and prior-work discussion now describe the qualitative result as a finite-typed guarded version of Yoshinaka's learner whose completeness is recovered by yield-typed refinement.

3. **Shifted the novelty emphasis.**
   The introduction now separates three layers:
   - Yoshinaka 2011: semantic baseline, Type I--III grammar, conservative update policy, rule-witness completeness, and unbounded-rank qualitative identification;
   - the companion CFG manuscript: fan-out-one antecedent for finite-monoid yield typing;
   - this paper: componentwise typing for tuples, rank-sensitive characteristic-data bounds, refinement obstructions, and fan-out / regular-filter separations.
   The rank-one size-only theorem, the higher-rank boundary transfer, the two exponential obstructions, and Section 5 separations are presented as the main technical contributions.

4. **Removed the version-dependent fan-out-one operator proposition.**
   The R1--R5 restatement and Proposition `prop:fanout-one-operator` have been removed from Section 3.  Fan-out-one definitions are now stated self-containedly in this manuscript.  References to the companion paper are bibliographic / comparative only and are not used in proofs.

5. **Made the companion-paper citation honest about public availability.**
   The bibliography now describes the cited object as the revised manuscript under review, with arXiv:1409.6247v4 explicitly labeled as the public predecessor.  Exact class/operator identities are no longer delegated to that public predecessor.

6. **Added missing Yoshinaka attributions.**
   - the conservative update policy cites Algorithm 1 / Section 4.1;
   - the completeness proposition is explicitly identified as the finite-typed counterpart of Lemma 5;
   - the thickness comparison cites Section 4.3;
   - fan-out nonmonotonicity cites Section 4.1 and Example 5;
   - the copy-language proposition now distinguishes Yoshinaka's untyped arity-one obstruction from the new “no finite typing repairs it” statement.

7. **Sharpened compatibility with Yoshinaka's efficiency scale.**
   The trivial-typing comparison now uses the no-splitting corollary rather than the more general boundary theorem.  Yoshinaka's Lemma 7 and Theorem 1 are cited explicitly.  The boundary theorem itself now displays the good-presentation bounds
   `|Wit| = O(||G||)` and `||Wit||_+ = O(||G||^3 * theta_bar_G)`
   for fixed parameters.

8. **Clarified the higher-rank theorem's scope.**
   The abstract and Section 4 now say explicitly that the prefix--suffix theorem is a uniform arbitrary-fixed-rank transfer result.  The manuscript does not claim a minimum-rank->1 strictness witness on which it is stronger than the rank-one theorem; that remains open.

9. **Fixed the renamed-copy pigeonhole gap.**
   For `{w phi(w)}`, the pigeonhole argument is now applied to the pair
   `(h(u), h(phi(u)))`, using `2^n > |M|^2`, and the distinguishing context is written out.

10. **Renamed the hierarchy witness and added the separator comparison.**
    The paper's separator-free hierarchy family is now `H_m`, avoiding collision with Yoshinaka's `L_m` from Example 3.  A new paragraph explains that Yoshinaka's separator symbols expose block boundaries explicitly, whereas the present `(1,1)` typing supplies finite boundary information.  The theorem also states that its hierarchy content is minimum fan-out `m`; for strictness at a fixed `f >= 2`, `H_2` already suffices.

11. **Mechanical / presentation fixes.**
    - repaired the broken nonpermuting-rule sentence;
    - removed the R1--R5 `lambda` / `eps` notation clash together with the moved comparison material;
    - renamed the Appendix A empty-component family from `G_n` to `E_n` to avoid collision with the Section 4 family;
    - shortened repeated “proof-strategy limitation, not lower bound” language;
    - added brief related-work references to Oates et al. (2006) and Kanazawa--Yoshinaka (2023).

## Deliberately not added

- No speculative minimum-rank-two witness was added.  The candidate suggested in review still requires a genuine proof of non-membership in `MCFL(2,1)`; a rank-two presentation by itself would not establish the desired language-level separation.
- Appendix A's standard normalization bookkeeping was not aggressively shortened in this pass, because the thickness-transfer invariant and empty-component obstruction still depend on the exact conversion stages.

## External submission actions still required

1. Publish the current revised #1 manuscript as a new arXiv version, then update the #2 bibliography to that actual public version number.  v47 deliberately does not invent “v5”.
2. Update arXiv:2605.11644 to the present #2 manuscript before or at I&C submission, since the public arXiv baseline substantially predates v47.
3. Run the author's full TeX pipeline before submission.

## Checks performed

- Current `main.tex` SHA-256: `7e5df2aa00627aa85ece9d7a31c65f635aaa487bbbc08f43b19b65d69bf4094b`.
- Static scan: no duplicate labels.
- Static scan: no unresolved `\\ref` / `\\eqref` targets.
- Static scan: no unresolved bibliography keys.
- Static scan: all `\\begin{...}` / `\\end{...}` counts match.
- Static scan: balanced unescaped braces.
- No full TeX-engine build was available in this connector pass.
