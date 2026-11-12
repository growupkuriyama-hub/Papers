# Paper #2 — response to Claude's independent referee report (2026-11-12)

**Scope:** English `main.tex` and Japanese `japanese/main_JP.tex`, Plan2 core. Referee report: [claude_independent_referee_2026-11-12.md](claude_independent_referee_2026-11-12.md). The report is archived verbatim, with no retroactive editing of Claude's conclusions. The initial draft sources were EN git blob `04316baee47182c8b9669186d9f0c7a14c7a4376` and JP `612428586c1108f7f7c9150534618e92ec7d1cde`.

The purpose of the present changes is to repair exposition, provenance, and identified scope mismatches; **no counterexample to A/B/C was established by the referee. The referee's "Minor Revision" is a model assessment, not an independent journal decision or a formal proof certificate.**

## Referee issue disposition

| Item | Response | Mathematics affected |
|---|---|---|
| **m1** | Clarified that the same block position `t=u` is included in the homogeneous-order hypothesis of `lem:group-interval`, EN and JP. | **Hypothesis wording** clarified; proof and use unchanged |
| **m2** | Added a carefully limited **ordered product-one subsequence** viewpoint to the one-row `f=1` case and cited Olson–White (1977), *Sums from a Sequence of Group Elements*, *Number Theory and Algebra*, pp. 215–222. Distinguished this from the **unordered small Davenport constant**; did not claim Olson–White already proves the multirow lemma. | Expository identity only; no new dependence in theorem proofs |
| **m3** | Stated an explicit admissible bound on the hidden coefficient of the `O(||G||² θ̄_G)` estimate, as a remark and not as a universal lower bound for optimal coefficients. | Bound extracted algebraically from existing `C_s(G)`, `beta_lambda`, `N_typ` |
| **m4** | Added rank `<=r_max` and fixed-parameter dependence to the paragraph after `prop:typed-separation`, EN and JP. | Scope made explicit |
| **m5** | Changed the IPTtD argument to a conditional statement **assuming the algorithm satisfies the IPTtD data condition**; this prevents erroneously inferring characteristic samples from normalization alone. | Existing contradiction clarified |
| **m6** | Replaced the item-number-dependent appeal to Almeida et al. Prop. 2.3 in `thm:lg-characterization` with a short direct proof of `(i) <=> (ii) <=> (iii)`, retaining the historical citation as background. | Added proof explanation (no new statement) |
| **m7** | Made JP Theorem C(ii) and the underlying `thm:fanout-one-data`(iii) state the EN constants `||G_n||=13n+7`, `θ̄_G=4n` and `3*2^n-1 >= 2^((||G_n||+θ̄_G)/17)`. Added the English conclusion that no intermediate growth occurs **at the pseudovariety boundary of fan-out one**. | JP statement strengthened to match EN; old construction cited |
| **m8** | Cleaned the punctuation in `lem:order-homogenize`, renamed its local recurrence from `m_q` to `h_q`, and denoted the number of order regions by `d_reg`, EN and JP. | Dummy-variable renamings only |
| **m9** | Qualified the abstract's linear lower bound as **worst case for explicit finite targets**, EN and JP. | Scope clarity |
| **m10** | Not adopted: adding the `τ_G <= ||G|| t_G` comparison was discretionary and would need additional symbol-convention explanation. | None |
| **m11 (additional)** | Clarified the question at the end of the article: `M_{G,f}` was *already polynomial in |G| for fixed f*. The genuine open direction is a **uniform bounded polynomial degree**, i.e. `c_{G,f} <= A (|G|^f)^B` with constants independent of `f` and `G`. | Open-question formulation corrected; no theorem affected |

## Important distinctions

- **m1 counterexample**: it only refutes the **weakened** reading that excludes comparisons with `t=u`. The original application via `lem:order-homogenize` supplies those comparisons; it does **not** refute Theorem A.
- **m2 reference**: Olson–White's bibliographic identity was cross-checked against secondary bibliographies. Direct examination of the complete 1977 primary text has **not** been performed; the paper is cited for classical background, not a theorem invoked in a proof.
- **m3 constant**: the explicit coefficient is an *upper bound furnished by the current proof*, not evidence of any optimal lower bound. Its potentially enormous dependence on fixed parameters remains an open optimization question.
- **mathematical proof audit**: the report was written by Claude and includes scripts that verify bounded cases. Code tests are not proofs. The proof-preserving check against the Plan2 manuscript should be rerun on final EN/JP sources.
- **bibliographic checks**: not every older reference was directly verified in the report; see its Executive Verdict for gaps.

## Sources preserved and validation

- All the original mathematical results parked by Plan1 (formerly Appendices H–J, `prop:zeta-capacity`, related sources) are **unchanged**.
- Main A/B/C substantive proof arguments are intended to be preserved; the only inserted proof is the short self-contained algebraic equivalence for `thm:lg-characterization`.
- EN and JP LaTeX CI runs and their page counts **must be confirmed on the final commit**. Do not assume the 42/49 pages of Plan2 will be preserved automatically after these edits.
- The referee's uploaded Python bundle was separate from the report. If not committed in this PR, the report remains archived here but its companion scripts are not claimed to be hosted by GitHub.

## Remaining editorial judgments

1. Independent human mathematical review of the full manuscript remains advisable.
2. The exact degree-independent simultaneous-owner constant bound is still open.
3. Check original Olson–White source if deeper historical attribution or claims of optimality are contemplated.
4. Final bibliography, PDF visual inspection, and author sign-off before TCS submission.
