# MCFG #2 v71 → v72: I&C final-referee corrections and sharper length bounds

Date: 2026-10-17 (JST)
Source: `MCFG02_v71_IC_Final_Independent_Referee_Report_20261017.md`
Baseline: v71, merge `5a60f5da0615082fc5c5e447988efc5deae27d58`
Branch: `revision/02-v72-final-referee`
Status: **review candidate, not submitted**.

## Decisions

1. **Leave companion CFG arXiv publication entirely with the author.**
   Do not push arXiv v5 or change the #1 manuscript.
   The current `kuriyamaCFG` bibliography entry still names public v4
   *and* a pinned revised GitHub source. Upon confirmed v5 publication,
   update the #2 citation and verify the cited Proposition 6.3,
   Appendix C and Theorem 7.2 genuinely occur in that released version.
   Until then #2 is not publication-ready on this point.
2. Fix P1/P2 editorial gaps:
   - Remove residual reference to the deleted all-fan-out strictness theorem
     from `ex:type-guard-purpose`.
   - Clarify that Yoshinaka (2015), Example 3, allowed more general
     components and operations; the signature here is a finite sort
     refinement of its **good nonempty-component variant**, not literally
     of the full Example 3 signature.
   - Restore the sample-level SUBST_P premise, trimming/effectiveness
     clarification, and provenance of Section 7.
   - Tighten the rank-one minimal-chain argument using lexicographic
     minimality (total length, number of rule applications).
   - Explain the unary singleton's substitutability and emphasize the
     fixed-window learning bias.
   - Indicate which quantitative theorem covers the retained
     separation examples and remove unused macros.
   - Clarify the abelian-product typing and name the capped
     reconstruction operator explicitly.
3. **Adopt the source-level proof of the stronger bound** suggested in
   the referee report, but keep it separately auditable as
   `lem:untyped-contexts`.
   For reduced good G, pick a successful source derivation with any
   rule whose lhs is A, remove that A-subtree and obtain a common
   sentence context E_A of length at most original rule thickness.
   Any tuple from L_A(G) can fill that hole. For typed X=A_t,
   L_X is a subset of L_A(G); h-refinement uniquely lifts the
   result to the typed presentation with that root type.
   For direct-start symbols E_S is the one-hole identity.
   This replaces the typed-path context-length factor, giving
   `|chi(X)|_fix <= max(1, theta_G)` and word length
   `<= 2 theta_bar_G + r_max b_can`.
4. **Stronger main results** for all fixed fan-out and rule rank:
   - `thm:boundary-polydata`:
     characteristic *total positive length* `O(||G||^2 max(1,theta_G))`
     (previously cubic).
   - `thm:window-abelian-polydata`:
     total positive length `O(||G||^3 max(1,theta_G))`
     (previously quartic).
   - The original `lem:boundary-short-canonical` and
     `lem:window-abelian-short` statements are unchanged.
     The older `lem:reusable-context-bound` is retained for
     arbitrary-typing and rank-one arguments.
5. **AI disclosure proposal requires author approval**:
   the manuscript now discloses ChatGPT and Claude use for
   exploratory proof development, critique, citation/consistency
   checking, and manuscript/LaTeX revision, rather than presenting
   their role as merely language editing.
   An introduction note addresses research-process uses as recommended
   by Elsevier's 2026 journal policy.
   This is a draft factual account, **not an assertion of independent
   human proof verification**. The author must confirm and adapt it
   before submission.

## Verification gates

- [ ] Combined source static labels, citations, and environment audit
- [ ] Full pdfLaTeX PR CI success, final page count and no unresolved citations
- [ ] Full PDF visual inspection
- [ ] Independent human mathematical check of new `lem:untyped-contexts`
- [ ] Author confirmation of AI-use disclosure and any journal requirements
- [ ] Confirm public arXiv v5 contents and update #1 bib cross-reference
- [ ] arXiv #2 version/citation/cover letter policy still to decide

No changes to any paper except #2. No arXiv push, no journal portal submission.
