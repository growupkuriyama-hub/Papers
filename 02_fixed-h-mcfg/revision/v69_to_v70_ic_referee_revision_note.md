# MCFG #2 v70: I&C independent-referee revision

Date: 2026-10-17
Branch: `revision/02-v70-ic-audit`
Paper: `02_fixed-h-mcfg/main.tex`
Review source: `MCFG02_v70_Independent_Referee_Audit_and_Actionable_Revision_Blueprint_20261017.md`
Status: **revision under verification**, see [PR #32](https://github.com/growupkuriyama-hub/Papers/pull/32).

## Goals and scope

Respond to the v69 independent report without changing the existing boundary theorem, its exponent or its underlying proof. Preserve the revised semilattice lower bound and the distinction between earlier learning results and the present quantitative MCFG result. New abelian-group mathematics is isolated and can be excluded independently if further verification finds a gap.

## Changed source files

- `main.tex`: clarify fan-out-one priority and the origin of the lower bound; compress bounded-rank complexity and the COPY example; move Yoshinaka 2015 signature correspondence to an appendix; add references to two new appendices; update the 2026 journal AI declaration **heading only**, leaving the author-controlled factual declaration body untouched.
- `appendix_bracketed_substitutability.tex`: independent in-paper proof of Clark–Eyraud substitutability of the bracketed-doubling family from the companion CFG paper. Proves stack recognition, branch synchronization, and distributional equivalence; referenced by `prop:fanout-one-lower-bound`. The attribution to #1 remains explicit.
- `appendix_window_abelian.tex`: separate new `lem:group-typed-shortest`, `lem:window-abelian-short`, and `thm:window-abelian-polydata`. Finite abelian group g plus fixed prefix/suffix typing h yields a total characteristic-data length bound `O(||G||^4 max{1, theta_G})` at fixed fan-out/rank. This does **not** replace or strengthen the statement of the pre-existing window-only `thm:boundary-polydata`; it is a distinct additional theorem.
- `PAPER.yaml`, `README.md`: version and file-list metadata updated to v70.

## Mathematical audits undertaken

1. The doubling-family lower-bound argument no longer relies solely on an unreleased companion manuscript for substitutability; the appendix reproduces the main stack proof. The reference to the companion paper remains to acknowledge priority.
2. Group-value shortening: lexicographically minimal derivations cannot repeat a pair (nonterminal, componentwise A-value) on one path; mutually incomparable heavy subtrees have additive replacement deltas in an abelian group, permitting a zero-sum shortening; at most `(|A|^f-1)|V||A|^f` heavy nodes remain. This bounds fixed-group-vector tuple lengths.
3. Boundary shortening: in the existing marked-skeleton proof, replace each omitted child by a tuple of the same g-vector with the length bound from step 2. This preserves all root component group values **and** protected window symbols; the refined root h-type is preserved. Characteristic words inherit an `O(||G||^4 theta_G)` total bound.
4. Nonabelian groups are not claimed, and the higher-fan-out original-thickness lower-bound question remains open.

## Prior-art and submission notes

- The fan-out-one window-only polynomial result precedes #2 (Yoshinaka 2008 and companion CFG). The new window-abelian theorem for MCFG has a different size degree (four), and the existing window-only theorem retains degree three.
- The full standard signature correspondence is retained in an appendix, not dropped.
- The current public arXiv `2605.11644` is substantially older/different; the I&C cover letter should transparently explain this.
- As of the October 2026 Elsevier journal AI policy, substantive AI drafting/analysis and proof exploration may require description beyond language editing. **The author must confirm the factual declaration and verify mathematical proofs before journal submission.** Only the section heading was automatically adjusted; no assertion of independent human proof verification is added on the author's behalf.
- The latest journal-specific Guide for Authors, Highlights requirements, CRediT need, and Elsevier/elsarticle requirements still require final verification; do not assume that a LaTeX build alone certifies submission compliance.

## Verification gates

- [x] Combined-source static check: defined references and citations; no duplicated labels.
- [x] Initial full v70 PR PDF CI after adding both appendices: successful (44 pages, 3 pdflatex passes, no final unresolved references or boxes).
- [ ] Final post-reorganization PR head PDF CI and log check.
- [ ] Manual full 44-page PDF visual inspection (CI alone is not visual inspection).
- [ ] Independent human review of the new abelian-group theorem and the doubled-family appendix.
- [ ] Author review of all claims and AI-use disclosure; confirm arXiv/submission plan.
- [ ] Merge to main only if final checks pass; otherwise keep PR open.

## Deferred

- Generalization to arbitrary finite nonabelian groups when f >= 2.
- Higher-fan-out operator-independent semilattice lower bounds.
- Major additional compression if it compromises presentation of proofs and separations.
