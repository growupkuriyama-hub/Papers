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


## Finite-semigroup / fixed-window systematic refactor (2026-10-19)
- Retained all original numbering and labels for Propositions 3.3/3.5 and Lemma 7.4. Replaced the four-case monoid multiplication table for the window congruence by a direct positive-word quotient-semigroup proof.
- The LI criterion operates on the positive image `S=s(Sigma+)`, not fresh-identity `S-sharp`. Lemma 7.4 uses factor projections of chosen letter lifts into a divisor of LI x finite group; no monoid adjunction is needed in this proof.
- The bracketed doubling family defines `U1` and `s_U:Gamma_br+->U1` on the spot; its empty-word type is `e`, not the existing identity `1` of `U1`. Deleted the false Section 3 forward reference.
- Replaced the `s_U x s_U` detour for `L_n^-` by the direct fiber-filter argument using `L_n cap shat_U^{-1}({zeta})`.
- Standardized the learning-facing notation `s_0`, `s_{k,l}`, `s_U`, and `s_{pm,e}`; monoid-valued maps are retained for the actual auxiliary calculations, notably `h_star` and the DFA transition morphisms `h_rho`, whose restrictions give `s_star` and `s_rho`.
- Replaced domain-mismatched products by explicit `g|_{Sigma+}` where necessary. Still experimental: R1 Response/Marked and TCS submission form abstracts remain tied to the v230 baseline.

## One self-audit pass: fixed-semigroup unification (2026-10-19)

**Scope.** Independent read-through of the changed proof steps in Propositions 3.3 and 3.5, Lemma 7.4, the semilattice `s_U` family, the Section 7 window-group bound and the newly restricted auxiliary maps. Auditing is not formal proof certification; untouched sections and former R1 files remain outside the edited branch's verification scope.

**Algebraic proof review.**
- Proposition 3.3 defines `s_{k,l}` only for positive words, with a short/long tag and the positive-word congruence; concatenation retains the shared window on long factors. The quotient inherits multiplication and the Yoshinaka four-word condition.
- Proposition 3.5 uses the *positive* image. Its short classes are not idempotent, and long classes obey `ete=e`; conversely the Pin finite-LI identities imply the `(n,n)` window refinement with `n=|S|+1`. Fresh-identity `S-sharp` is not asserted locally trivial.
- Lemma 7.4 uses arbitrary lifts of each letter through a divisor `V subset T x G`, the resulting *positive* projections and the LI criterion; the group projection extends uniquely to `Sigma*` and no monoid on the LI side is needed.
- The filter `L_n-minus = L_n cap shat_U^{-1}({zeta})` retains `s_U`-substitutability, since equal positive types yield identical filter membership inside any common context; intersection with a regular language preserves context-freeness.
- The auxiliary finite monoid morphisms `h_star` and `h_rho` remain only where whole-word summaries are used, with learning-facing restrictions `s_star` and `s_rho`; all remaining `g` products use its restriction to positive words.

**Finite reproducibility checks (sanity only).**
- Alphabet `{a,b}`; each `(k,l)` with `0 <= k,l <= 2`; positive words of length at most 8, and added left/right contexts up to length 3: no counterexample to the short/long congruence. Quotient representative multiplication was associative and locally trivial for all nine cases, including `(0,0)`.
- Enumerated finite bracketed-doubling `L_n` for `n=1,2,3` (respectively 2, 6, 42 words). Constructed all factor distributions and found no counterexample to `L_n` being trivially substitutable, nor to `L_n minus {w_n*}` being `s_U`-substitutable. These are finite checks, not a proof for all n.

**Three consistency defects found and repaired during the pass.**
1. The inherited phrase `s_{0,0}` 'separates lambda from nonempty words' was mathematically invalid since `s_{0,0}` is defined only on `Sigma+`. Replaced it by `s_{0,0}=s_0` on `Sigma+` in both languages.
2. The algorithm section still called the carrier of `s` a 'fixed monoid'. Changed this to a finite semigroup.
3. Japanese nonlinear proof still described positive factor equality as an `h_star`-type; aligned its prose with `s_star`, retaining `h_star` for monoid-valued whole-word calculations.

**Static consistency checks.** Both manuscripts retain 58 labels and 39 proof environments, no duplicate labels, no missing LaTeX references, no `SSBNF`, and no learning-facing `h_U`/`h_{k,l}`/`h_0` uses. The same English content is used for main and Clean.

**Open gates.** Compile EN/JP at the final commit; check PDF layouts and representative edited passages; audit the substantive BUNF window-group shortening and all other untouched results independently before adopting. Stored official v230 R1 Marked PDF, 49 responses/77 locators and the old form abstract are intentionally not synchronized.

## Restoration of Yoshinaka (2015) attribution detail (2026-10-19)
- Restored the substantive explanation from v230 Section 1.1 while retaining the concise PR #62 Introduction: the 2014 preprint precedes the publication of Yoshinaka's (2015) general many-sorted signature theorem; nonempty fixed-semigroup fibers are modeled as disjoint sorts with typed concatenation and whole-string promotion.
- Explicitly distinguish the author's specific choice of sorts from Yoshinaka's contribution, and acknowledge the prior qualitative positive-data existence theorem without treating it as original.
- Retain the focus on explicit reconstruction, encoded characteristic-data bounds, and algebraic/expressive consequences; identify the LI fixed-window criterion as classical.
- English canonical and Clean TeX are exact mirrors; Japanese has corresponding semantic wording. No changes to definitions, results, numbering or proofs. Existing official marked revision/response package is not synchronized with this experimental PR.
