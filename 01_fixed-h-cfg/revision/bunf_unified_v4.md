# BUNF-only proof refactor v4 (2026-10-19)

Status: EXPERIMENTAL, independent mathematical audit pending. No merge, TCS resubmission, arXiv update or reviewer-response refresh. Source base: PR #61 `1c4c49fcefd7684bc310715ea974408451fcd7ab`.

## Uniform structural decision
Use reduced BUNF (`A->BC`, `A->B`, `A->a`, `A->lambda`) for every target/normalization/quantitative argument. Neither start-symbol isolation nor unit/nullable deletion is imposed. The hypothesis grammar is the PR #61 positive-factor `Rec_s(K)` with no empty-factor nonterminal. The typed refinement includes typed copies of the original start symbol.

## New argument A: presentation-independent typed-thickness gap
Every reduced BUNF grammar for `L_n` has the productive typed start copy `(S_0)_1`. Its typed language is `L_n ∩ shat_U^{-1}(1) = {w_n^*}`, hence its canonical yield has exponential length. No root `S_0->A` shape is needed. This strengthens the previous SSBNF-only conclusion.

## New argument B: window x group bound in arbitrary BUNF
For each positive typed copy (including start copies) choose shortest NONEMPTY word in the finer window x group fiber. For `m=k+l`, protect all prefix/suffix window letters and one anchor letter, giving at most `m+1` protected positions. The anchor is essential for `m=0`, where erasing nullable subtrees could otherwise collapse a positive word to lambda. Choose a derivation with the fewest nonterminal nodes among minimum-length witnesses. On a path, a repeated (protected-position set, nonterminal, group value) produces a shorter witness or an equally short witness with fewer nodes, even across unit or nullable edges. Bounding essential nodes per depth uses ordered (possibly noncommutative) group products, and allows shortest sibling words to be empty. Quantitative displayed bound: `m+1 + [1+2(m+q)(m+2)|V|q](tau_G+1)`.

## New argument C: CFG-to-BUNF thickness-preserving conversion
Terminal isolation + RHS binarization already preserve original nonterminal languages and give polynomial length bounds for fresh block symbols; no nullable or unit elimination needed.

## New argument D: linear-spine BUNF
Keep original unit and epsilon rules. Convert only longer linear productions into left/right unary-terminal-wrapper chains. Every binary rule has one wrapper (one terminal) plus one continuing spine child. For a shortest typed yield, choose a minimum-node derivation. No typed spine label can repeat; otherwise replacement shortens the yield (binary step) or reduces derivation nodes (unit-only). This gives `|omega(X)|<=N_t`.

## Review gates / possible pitfalls
1. Review the window prefix/suffix protected-position argument for overlapping windows and words of length below `k+l`.
2. Review zero-output children, pure unit cycles, nullable cycles and start symbols on RHS.
3. Inspect group cancellation for nonabelian `G`, maximal nonessential frontier counting, and the `m=0` anchor.
4. Check polynomial encoded size of BUNF normalization and linear spine; no accidental multi-wrapper binary productions.
5. Verify the enriched BUNF witness count, proof labels, EN/JP source parity, and full source ref/citation compilation.
6. Existing binary PDFs, marked R1 response documents (49 items/77 locators), and ZIP are not valid v4 submission packages. Regenerate only if author adopts v4.

These are proposed mathematical proofs; build success is not a proof certificate.

## First independent-audit repair pass (2026-10-19)

- **F01 (fixed):** Removed the false general-BUNF implication `tau_{h0}^{typ}(G) <= max(1,tau_G)` from Proposition `prop:typed-thickness-gap` (ii). The existing explicit characteristic sample `F_n`, its encoded-size calculation, reconstruction monotonicity, and soundness give the result independently.
- **F05 (simplified):** Added the unnumbered fiber-minimum bound implied by retaining typed copies of the original start symbol. Deduce the intrinsic type-1 exponential gap directly from its singleton fiber; no new theorem numbering.
- **F02 (strengthened):** Clarified disjoint window positions when `|w|>=k+l`, the nonempty anchor (which may overlap protected window positions), equal-mark tree grafting, and noncommutative ordered-product group cancellation. Retained the same quantitative bound.
- **F03 (strengthened):** Defined the continuing spine excluding terminal wrapper children, and explicitly justified grafting identical typed spine states while preserving a typed derivation.
- **F04 (strengthened):** Clarified fresh per-original-production binarization symbols, their contiguous RHS blocks, and preserved original shortest yields.
- **F06 (selective):** Removed the redundant argument in gap (ii), compressed the intrinsic-gap corollary, retained the normalization proposition and control-set discussion to avoid shifting reviewer landmarks before R1 response synchronization.

**Publication gate:** Independent adversarial mathematical verification is still pending. Existing R1 marked PDFs, 49 replies, 77 marked-page locators and submission ZIP are NOT synchronized with this experiment. Do not merge with main or submit without author approval.

## R1-directed front-matter compression (2026-10-19)

- Revised English Abstract from approximately 172 to 132 whitespace-delimited words (the count includes TeX fragments), retaining the fixed-semigroup learning problem, set-driven versus Gold-learner distinction, general typed-yield upper bound, window-group/linear quantitative regimes, semilattice exponential lower bound with operator-level scope, and expressive boundaries.
- Reduced Introduction Section 1.2, `Contributions and main results`, from about 291 to 218 English whitespace-delimited words; preserved two, and only two, high-level contributions as requested by Reviewer 1 (R1.3 and R1.5), instead of enumerating proof-local lemmas.
- Responds to Reviewer 1's R1.2 verbosity and undefined-technical-term concerns. The qualitative existence from Yoshinaka's many-sorted theory and classical finite-semigroup window criterion are expressly not presented as new.
- Replaced unexplained early acronym "BUNF" in that section with a descriptive binary–unit–nullable form (formal definition later); no claim of uniform ordinary-thickness or incremental polynomial-data learning.
- Changed **only** Abstract and Section 1.2 in the manuscript sources; synchronized `main.tex`, `TCS-D-26-00494_Manuscript_Clean.tex`, and `japanese/main_JP.tex`.
- The **existing TCS submission form abstract** and stored marked/response PDF packages remain tied to the earlier official baseline. This is PR #62 experimental drafting only, NOT an R1 submission.

