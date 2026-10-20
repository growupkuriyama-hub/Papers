# TCS-D-26-00494 Japanese translation audit — English v245

Date: 2026-10-20. Target: English `01_fixed-h-cfg/main.tex` (v245), Japanese `01_fixed-h-cfg/japanese/main_JP.tex`. **The English submission source is unchanged by this audit.** Japanese text is a *reference translation*, not an Editorial Manager submission item.

## Result

**Substantially faithful technical translation:** no material disagreement detected in the 41 numbered mathematical statements, theorem hypotheses and conclusions, upper/lower bounds, the fixed-typing versus union-of-typings scope, or the central Gold/set-driven distinction. The Japanese version is **not a literal sentence-by-sentence identical translation** and has several expository additions and contractions. A completely independent human translation/proof audit was not performed.

## Inventory cross-check

| Item | English | Japanese | Finding |
|---|---:|---:|---|
| Ordered headings (sections, subsections, paragraphs) | 44 | 44 | Exact hierarchy/order correspondence |
| Numbered definition/lemma/proposition/theorem/corollary/remark statements | 41 | 41 | Each statement compared against its Japanese counterpart |
| Proof environments | 39 | 39 | All present in matching sequence; core proof logic and high-risk arguments inspected |
| Labels | 58 | 58 | Same keys in the same order |
| English display mathematics vs Japanese display mathematics | 43 | 45 | All **43 English displays** reproduced after whitespace, punctuation and `\\text` normalization; two additional Japanese displays merely format English inline formulas |
| Bibliography entries | 25 | 25 | Same sequence and English source entries |
| Cited bibliography keys (counting multiple keys separately) | 62 | 62 | Same cited key set |
| Footnotes | 3 | 4 | Japanese has an explanatory footnote for the `+1` sample-size convention; the same mathematical content is in English inline text |

For the two Japanese-only displayed equations: (a) canonical RHS yield `t_\\rho` in Section 5; (b) BUNF normalization polynomial bounds in Section 7. Both expressions occur in the English manuscript as inline mathematics. Layout differences alone are not substantive omissions.

## Section-by-section content audit

1. **Introduction:** prior-art attribution to Yoshinaka (2015), the author's 2014 preprint, qualitative claims versus encoded witness-length novelty, finite-semigroup typing, and lower-bound caveat align.
2. **Preliminaries:** grammatical conventions, Gold learning and characteristic samples, separate fresh identity `1_sharp`, empty versus nonempty factors, and finite typing align.
3. **Fixed Recognizable Substitutability:** regular-language and fixed-window realization, refinement/closure under regular filtering and inverse homomorphisms, algebraic locally trivial criterion, and main theorem align. The Eilenberg (1974) citation in Proposition 3.1's proof was restored during this audit.
4. **Reconstruction Operator and Sequential Learner:** reconstruction rules, sample consistency, soundness and hypothesis-change criterion align.
5. **Finite Witnesses:** arbitrary CFG typed production refinement, witness construction, completeness for nullable/unit/long RHS productions, exact reconstruction and Gold convergence align.
6. **Typed Thickness:** BUNF-specific quantitative parameter, typed yield and witness bounds, presentation dependence, doubling family exponential characteristic-data lower bounds and operator-independent two-target caveat align.
7. **Polynomial Thick Data Beyond Fixed Windows:** fixed-window and finite-group case, ordinary thickness via polynomial BUNF normalization, `LI ∨ Grp` join and two-element semilattice exclusion align.
8. **Linear Subclass:** linear-spine BUNF normalization, bounded typed shortest yields, polynomial characteristic data, nonregular examples and regular control-set construction align.
9. **Expressiveness and Boundaries:** nonlinear `Delta^*` example, capped versus unbounded counters, fixed-window separation, Dyck obstruction and congruential comparison align.
10. **Conclusion and backmatter:** data availability, no competing interests, no external funding, Makoto Kanazawa/Ryo Yoshinaka/two anonymous reviewers/**Alexander Clark**, full ChatGPT/Claude generative-AI declaration all present; closing claims aligned with English.
11. **Appendix A:** protected nonemptiness anchor, noncommutative finite-group argument, `D_dep` and `W_ess` bounds and normalizations align.
12. **Appendix B:** linear-spine normalization formulae and terminal wrapper construction align.
13. **Appendix C:** bracketed doubling family parser, stack lemmas, synchronization and substitutability conclusion align.

## Edits made during audit

- Added the Eilenberg (1974) citation at the corresponding Japanese Proposition 3.1 proof location.
- Replaced one unexplained English `iff` inside Japanese prose with `は同値`.
- Standardized one `正規言語` to `正則言語`.
- Refreshed the Japanese-source SHA-256 in `PAPER.yaml`.
- The Japanese PDF publication workflow is triggered automatically by the source change; its generated-PDF commit should be checked separately.

## Remaining distinctions and limits

- Japanese wording is sometimes more expansive than the current concise English v245; it is a technical translation, not a one-to-one diplomatic transcription. The additional footnote is not a missing mathematical claim.
- English and Japanese TeX use different document classes/fonts, so their pagination need not match.
- Mathematical proof *correctness* is separate from whether the Japanese proof faithfully conveys the English proof. This audit is not a new mathematical correctness certification.
- Japanese reviewer-response material in `response/japanese/` remains historic v229 and is **outside this manuscript audit**.
- The English `main.tex` remains the sole submission source of truth; the present check does not certify any future change after this snapshot.

Snapshot fingerprint: English source SHA-256 `87c68654f02de2675deaeab6081ae8db3315cad251f65ab99f5714799342021a`; Japanese source SHA-256 `ba1b0516338ae6e99ad15a2c7c5cddb59814b7e93271ef7e4150f97f9eb46a39`.
