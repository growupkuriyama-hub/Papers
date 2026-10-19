# PR #62 — v230 referee-compatibility restoration and focused mathematics audit

Date: 2026-10-19. Version: PR #62 experimental BUNF/positive-semigroup branch.
Main and the previously submitted TCS files are not changed.

## Restored reviewer responses
- R1.7: Reinserted the presentation-order dependence argument. On a fixed convergent text for an infinite language, choose a member word longer than all finite examples at the last rebuild. The stabilized grammar for that text does not have its factor nonterminal, but the text obtained by prepending this word does; both learned grammars generate the same language.
- Definition 5.1: BUNF is numbered rather than explained in unnumbered prose, restoring the historical Section 5 numbering: Proposition 5.2, Theorem 5.3, Theorem 5.4, Corollary 5.5, Theorem 5.6.
- R1.11/R1.12/R1.13: Reviewer responses refer correctly to positive-semigroup typing, fresh-identity completion, and the congruence/quotient realization of fixed windows (rather than the removed four-case monoid product).
- R2.1/R2.8/R2.10: Updated the semigroup scope, rule-by-rule BUNF witnesses, and the fixed-semigroup Gold identification formulation. All original referee quotations remain unchanged.
- Corrected remaining mathematical occurrences of h where the revised reply actually describes the s-typed proof (R1.18, R1.26, R1.27, R2.2, R2.3); auxiliary transition-monoid morphisms remain h when appropriate.

## Focused mathematical check
1. The restored R1.7 argument relies on a finite last-rebuild sample and the hypothesis nonterminals indexed by positive factors in that sample. Prepending the long word forces an initial rebuild from a sample containing it and every later rebuild retains it. This proves syntactic order dependence without weakening Gold convergence.
2. Numbering BUNF does not change its admissible grammar productions A→BC, A→B, A→a, and A→lambda, or the typed refinement, completeness proof, sample-size bounds, or lower-bound hypotheses.
3. Every v230 monoid typing h:Sigma*→M restricts to a positive-semigroup typing s=h|Sigma+; the added fresh identity handles epsilon separately. Therefore the former fixed-h target class is retained under the change of formulation.
4. The window–finite-group bound has a larger polynomial coefficient in the PR but applies to reduced BUNF rather than SSBNF and retains the polynomial-in-grammar-size-and-thickness conclusion. The bracketed characteristic-sample lower bound and its operator quantifiers are unchanged in strength.
5. No independent fully formalized derivation of the BUNF window–group lemma or complete Appendix C parser theorem is claimed. These original/generalized mathematical proofs still deserve adversarial third-party audit before journal submission.

## Verified editorial / build gates
- Both language manuscripts: 58 labels, 39 proof environments; English canonical/Clean content identical; no missing label refs.
- Experimental branch-only GitHub Actions regenerates an additions-only marked manuscript against the original submitted arXiv source, synchronizes 49 reviewer locators against that actual PDF, and compiles the response.
- The first completed experimental synchronization yielded 49 response table rows and 77 verified marked-PDF page/line anchors; marked PDF 26 A4 pages and response PDF 14 A4 pages.
- Later response-only notation corrections require a fresh marked/response build; the experimental branch workflow performs this recheck automatically.
- Neither merge nor TCS/arXiv submission has been authorized.
