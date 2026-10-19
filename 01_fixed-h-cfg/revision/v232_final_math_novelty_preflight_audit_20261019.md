# TCS-D-26-00494 v232 — final mathematical / novelty / package preflight (2026-10-19)

**Status:** independent focused review, not a formal proof certificate, not a journal submission. Original baseline: `main` commit `f3fb8ea69dead1cd35d8e7470f77498482119595`; source file `01_fixed-h-cfg/main.tex`. This audit branch modifies the English master and Clean TeX only to repair the notation issue noted below. Existing checked-in PDFs and ZIP correspond to **baseline v232**, not this branch's amended source. Do not treat the branch as submission-ready until regenerated and verified.

## 1. Appendix A.1: window–group typed-yield lemma

Inspected the complete argument in Appendix A.1 and its stated Lemma 7.1, including nullable/unit productions and original-start-symbol copies.

- The protected first `k` and last `ell` letters, plus one nonemptiness anchor, retain the window and a positive result under replacements. In particular the anchor is needed for `k=ell=0`.
- Along any ancestry chain the sets of protected positions are nested and change at most `d` times. Equality of the protected-mark set, nonterminal, and finite-group value permits grafting the lower derivation into the upper one. A shortest-word / fewest-nodes tie-break excludes repetitions and bounds nonterminal depth by `(d+1)Nq`.
- At a fixed depth, at most `d` disjoint nodes cover protected positions. If `q` further nodes have yields longer than `tau_G+1`, replace an interval of those by shortest underlying nonterminal yields. With prefix products `r_j,t_j` and discrepancies `x_j=t_j r_j^{-1}`, the equality `x_i=x_j` implies `t_{i:j}=r_{i:j}`, by left and right cancellation **without assuming commutativity**. The new word is shorter and has the same protected letters and group product.
- Essential nodes are ancestor-closed; counting the at most `m+q` essential nodes at each bounded depth and the maximal nonessential subtrees recovers the displayed polynomial bound.
- **Actual defect found:** English source defines `Prot` as the protected-position set but defines `d:=|P|`, while `P` also denotes the grammar's production set. On this branch we changed the latter to `d:=|\\mathrm{Prot}|` in both English `main.tex` and `TCS-D-26-00494_Manuscript_Clean.tex`. The Japanese proof already defines its own local `P`; no Japanese change was necessary. This is a notation repair, not a change to the bound.

**Assessment:** no decisive logical counterexample identified in the inspected proof; a fully formal verification has not been performed. Particular follow-up targets remain zero-yield sibling subtrees, tie-break grafting, and exact constants.

## 2. Appendix C: bracketed doubling substitutability

Inspected the parser transition system, recognition lemma, complete-subtree exchange, branch synchronization, and path-congruence induction.

- For each input letter, the transition is a partial injection. The weight `4^i` for `E_i` and weight `1` for closing markers strictly decreases under every step, excluding positive-length return loops.
- The stack-suffix and final-closing-marker properties support the recognition of `L_i` by `E_i` and the branch-synchronization argument when the first input letters differ.
- The induction on the sum of input lengths reduces identical first letters by determinism and differing first letters by exchange of complete `L_i` subtrees, yielding the needed syntactic congruence.
- Independent finite enumeration of `L_1,L_2,L_3` yielded respectively **2, 6, 42** target words, **14, 125, 2027** distinct nonempty factors, and **0** counterexamples to substitutability or the tested same-state-pair path equivalence. These finite tests do not prove the universal claim.

**Assessment:** no decisive mathematical defect found in this focused review; this is not a formal certificate.

## 3. Yoshinaka (2015) novelty audit

Compared the actual text of R. Yoshinaka, *General Perspective on Distributionally Learnable Classes*, MoL 14 (2015), especially Section 6.1, Theorem 1 and Lemma 3, with the revised Introduction, reviewer response (R1.3, R2.1), and TCS submission-form abstract.

| Result category | Yoshinaka (2015) | Current paper's defensible position |
| --- | --- | --- |
| Positive-only identification, conservative updates | Covered by signature-based substitutable grammar learning | Fixed finite-semigroup instance; **not independently novel** |
| Polynomial hypothesis-update complexity | Under signature tractability assumptions | A concrete instantiation; **not independently novel** |
| Polynomial **number** of characteristic witness words | Lemma 3: at most `|N|+|P|` in the signature-grammar setting | Fixed-typing cardinality is **not independently novel** |
| Polynomial **total encoded length** of witness words | Does **not** follow from cardinality bound without a shortest-yield length estimate | Typed thickness, `LI vee Grp`/window–group, linear-grammar bounds are the quantitative claims to emphasize |
| Exponential data-length obstruction / presentation-independent typed-thickness lower bound | Not supplied by the cited Theorem 1/Lemma 3 | Central claimed contribution, especially Proposition 6.3/Corollary 6.4 |
| Fixed windows and finite-semigroup algebra | Classical antecedents (Yoshinaka 2008, Pin, etc.) | Explicitly credited; applications/quantitative contrasts are the relevant claims |

A concrete Yoshinaka-signature realization uses disjoint positive-type sorts corresponding to nonempty fibers of the fixed semigroup morphism, a separate empty type (fresh identity) for nullable yields, typed concatenation operations, and promotion to the whole-word sort. The original framework's assumptions and exact encoding are relevant when citing the specialization. The current Introduction and reviewer response properly separate the old qualitative results from the newer quantitative assertions; **no further claim-strengthening is recommended**.

Retain the following qualifications: fixed `s` throughout the learning class; no learner for the varying-`s` union; polynomial encoded characteristic data for the set-driven operator (not a uniform incremental Gold sample bound); algebraic upper bounds only under the stated group/window hypothesis; lower bounds for set-driven operators with characteristic samples for the distinguishing pair (not arbitrary Gold-learners' running time).

## 4. Baseline v232 package preflight

Current main metadata lists v232 and status **prepared, not submitted**. The baseline `main.tex` and Clean TeX have identical Git blob SHA `0d1c581ef26faecb8eae5a8f9ce44285fe67e8e1`; the submission-form abstract agrees substantively with the manuscript abstract.

- GitHub Actions run [39267763201](https://github.com/growupkuriyama-hub/Papers/actions/runs/39267763201), 2026-10-19, succeeded in building the marked manuscript and the PDF-anchored reviewer response. Logs confirm **26 marked pages**, 49 response items with actual marked-PDF location checks, a successful response build, a three-file archive, successful `unzip -t`, and an archive member count of exactly 3.
- Baseline package contains the Clean TeX, Marked PDF, and Reviewer Response PDF; the baseline Clean PDF was separately reported as 25 pages, Response PDF as 14 pages.
- **Direct artifact-byte validation (additional independent check):** downloaded GitHub Actions artifact `12193633404` from successful run `39267763201`; verified ZIP member list and CRC (`unzip -t`), exactly three files. Recomputed the Git blob SHA of the extracted English Clean TeX as `0d1c581ef26faecb8eae5a8f9ce44285fe67e8e1`, exactly matching the baseline `main.tex` blob. The extracted Marked PDF is 26 A4 pages and Reviewer Response PDF 14 A4 pages. Both pass the PDF preflight checks with zero warnings; all 40 PDF pages rendered at 110 dpi without renderer errors, and sampled pages of both documents were visually inspected with no evident clipping or missing glyphs. The blue underlining in the Marked PDF is intentional markup; this check is not a print-prepress or page-by-page semantic proof inspection.
- Baseline manuscript source static checks: 58 distinct labels, 39 proof environments, no missing local `ref` targets, and complete bibitem coverage for citations. The audit-branch's master/Clean TeX remain byte-identical after the one-symbol notation repair.
- The repo's README still advertises v231 whereas `PAPER.yaml` identifies v232. Correct README in this branch.
- The Japanese reviewer-response workflow has a separate failure and the Japanese response translation is marked historic in `PAPER.yaml`. It is **not** part of the English TCS submission triple.

**Important release boundary:** the tested ZIP and its 77 claimed anchors belong to the existing baseline v232. They have **not** been regenerated from this audit branch. After deciding to adopt the notation fix, rebuild English Clean PDF, Marked PDF, Response PDF and three-file ZIP, recheck the 49 items/77 anchors against the new PDF, and update the release version/status accordingly. Do not submit old artifacts with amended TeX. Check final PDF appearance. Update Editorial Manager title, abstract, keywords, and competing-interest statement separately; no portal action is performed by this audit.

## Conclusion

The first-pass adversarial audit has not found a decisive counterexample in Appendix A.1 or C. It did identify and repair one English notation mismatch. The novelty framing versus Yoshinaka (2015) is appropriate. The v232 baseline package passed its GitHub build and consistency checks, but the branch's corrected TeX requires a new, synchronized release before submission. This report is a focused independent mathematical audit, not a formal mathematical proof, complete literature novelty search, or Editorial Manager acceptance guarantee.
