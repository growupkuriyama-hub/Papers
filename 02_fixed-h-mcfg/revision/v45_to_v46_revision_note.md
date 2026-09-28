# MCFG v45 -> v46 revision note

## Purpose

v46 is a submission-preparation revision driven by an independent re-check of the v45 manuscript together with a separate Claude review.  No new headline theorem is introduced.  The revision concentrates on theorem scope, companion-paper version dependence, proof wording, prior-work positioning, and the role of the separation examples.

## Main changes

1. **Separated uncapped and capped learners in the abstract and contribution statement.**
   The full fixed-`(f,h)` class is identified by the uncapped conservative learner.  Polynomial-time updates are now explicitly attributed to the separately capped learner on the rank-`<= r_max` subclass.

2. **Corrected the bounded-unknown-typing wording.**
   The introduction now says that the bounded union is **contained in** a single product-typing class, matching Proposition `prop:bounded-unknown-typing`; it no longer suggests an equality or literal reduction of classes.

3. **Sharpened the novelty / prior-work positioning.**
   The introduction now distinguishes material inherited from Yoshinaka's multidimensional substitutability from the new finite-typing and sample-local completeness work.  It also contrasts the present positive-data primal construction with the active / dual PMCFG setting of Clark--Yoshinaka.

4. **Corrected the materialization proof.**
   Lemma `lem:composition-witness-materialization` no longer says that same-parent child components must be separated by terminal material.  The proof now allows separation by nonempty sibling intervals, which is what nonmerging actually guarantees together with the witness definition.

5. **Made the fan-out-one comparison self-contained.**
   The revised companion CFG Rules R1--R5 are restated immediately before Proposition `prop:fanout-one-operator`, including the observed-state side condition and the direct empty-word start rule.

6. **Aligned the lambda-free deleting-input scope.**
   The preliminary normalization discussion now matches the v45 appendix result: reduced lambda-free inputs may contain deleting rules, with polynomial thickness transfer supplied by Proposition `prop:structural-good-thickness`.

7. **Made the thickness notation correspondence explicit.**
   A small table records
   `this paper: (rule, nonterminal) = (theta_G, tau_G)`
   versus
   `Yoshinaka: (rule, nonterminal) = (tau_G, t_G)`.
   This correspondence was checked against Yoshinaka (2011), Section 4.3 / Definition 1.

8. **Added the direct fan-out-one rank-one consequence.**
   The rank-one theorem now notes that, at fan-out one, the MCFG template argument also yields the linear fixed-`h` CFG characteristic-data result directly, without a separate spine-normalization argument.

9. **Clarified the roles of the separation witnesses.**
   The manuscript now states explicitly that `J_s` lies inside the same-typing regular-filter fragment and is used only to separate non-boundary finite typings from every fixed prefix--suffix typing.  It also explains why `L_star` is still needed: unlike `L_cd`, it remains finitely typed at fan-out two while separating arbitrary target-dependent regular filtering.

10. **Strengthened the every-fan-out proof presentation.**
    The inequality for `d = ceil(m/2)` is proved by parity, the factorization is given by explicit indices `q_i`, and the Seki et al. closure citation is phrased through substitution closure / homomorphism.

11. **Narrowed the higher-rank boundary-theorem claim.**
    The manuscript now says explicitly that the displayed strictness witnesses are rank one, for which the rank-one theorem gives the stronger size-only data bound.  The boundary theorem is presented as the general arbitrary-fixed-rank transfer result, while a strictness witness of minimum rule rank greater than one is left open.

## Companion-paper version issue

The public arXiv version of paper #1 is still the older v4 baseline, whereas the fan-out-one comparison in paper #2 refers to the current revised companion manuscript.  v46 reduces this dependency by restating Rules R1--R5 in full, but it deliberately does **not** invent an arXiv v5 citation.  Before I&C submission, paper #1's revised manuscript should be made publicly accessible (preferably as a new arXiv version), and the bibliography entry in paper #2 should then be updated to the actual public version.

## Checks performed

- GitHub `main.tex` after the v46 edits has SHA-256 `b109cd943fdfe76edaa343cc7e194ee3270651e9f4384afd90e36cbd073d61f3`.
- No duplicate LaTeX labels were found by a static scan.
- Counts of all `\\begin{...}` and `\\end{...}` environments match.
- Yoshinaka (2011) Corollary 2, the rule/nonterminal thickness notation, the nonmerging lemma, and the alternative empty-component convention were checked against the original source available in the project corpus.
- Seki et al. (1991) Lemma 3.3 and Theorem 3.9 were also checked against the original source available in the project corpus.

A full TeX engine build was not run in this connector-only revision pass.
