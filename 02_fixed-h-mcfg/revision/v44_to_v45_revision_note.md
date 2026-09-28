# MCFG v44 -> v45 revision note

## Purpose
v45 incorporates the parts of the latest Claude review that survive independent checking, while deliberately not adding the proposed minimum-rank-two witness `L_cat`, whose supplied pumping proof still needs a complete case analysis for general good unary fan-out-two templates.

## Main mathematical / structural changes

1. **Corrected the novelty statement about unbounded rank.**
   Yoshinaka (2011), Corollary 2 already gives qualitative positive-data identification without a fixed rule-rank bound for the trivial-typing baseline. v45 therefore does **not** claim that rank-unbounded learning is new at trivial typing. The introduction now says that the present qualitative theorem extends that rank-unbounded setting to a fixed finite typing.

2. **Made the relation with Yoshinaka's finite-sample grammar precise.**
   Added Lemma `lem:type-guarded-subgrammar`: relative to the paper's own trivial-typing constructor, a finite typing changes only Rule (Link), deleting links between componentwise type-incompatible tuples.

   v45 also clarifies an important non-identity: the present trivial-typing constructor is a **sample-local subgrammar** of Yoshinaka's `G(K)`, not literally the same grammar. Yoshinaka's Type I rules allow any good algebraic decomposition among observed tuple values; the present Rule (Comp) requires that the decomposition be materialized inside one observed parent occurrence.

3. **Proved finite-sample equivalence of the two fan-out-one reconstruction architectures.**
   Replaced the old explanatory remark by Proposition `prop:fanout-one-operator`. For every finite sample and every rank cap at least two, the generated language of the current fan-out-one value-based constructor, its uncapped version, and the companion CFG constructor coincide. The proof gives explicit simulations of CFG Rules R1--R5 by (Comp)/(Link)/(Const)/(Start) and conversely.

4. **Corrected the fan-out-sensitivity positioning.**
   The manuscript now explicitly cites Yoshinaka's Example 5 (`L_reverse`) for the fact that increasing tested arity can destroy substitutability already under trivial typing. The stronger new point of `L_cd` is stated as: **no finite componentwise typing can repair the fan-out-two failure**.

5. **Separated the assertion inside “composition witness” from its definition.**
   The definition now only specifies the segmentation/template data. A new lemma, `lem:composition-witness-materialization`, proves that induced child tuples are observed occurrences and that the induced template is good.

6. **Strengthened thickness transfer to deleting but lambda-free inputs.**
   Proposition `prop:structural-good-thickness` now starts from an arbitrary reduced lambda-free presentation of bounded fan-out/rank; deleting rules are allowed. The proof uses the full projection invariant of the nondeleting conversion and then the length-preserving permutation/nonmerging stages. The boundary-data theorem's input-presentation clause has been widened accordingly.

7. **Added an empty-component normalization obstruction.**
   New Proposition `prop:empty-component-blowup` gives a size-O(n), fan-out-two, rank-two family with small source nonterminal/rule thickness but an empty-component decorated state of thickness at least `2^n`. This explains why the lambda-free hypothesis in the transfer result is substantive and aligns the empty-component phenomenon with the existing exponential yield-type-refinement obstruction.

8. **Clarified scope in abstract/conclusion.**
   The abstract now calls fixed typing a *relaxation* of Yoshinaka's multidimensional substitutability, states the lambda-free transfer range, and mentions the empty-component obstruction. The conclusion now distinguishes baseline fan-out sensitivity from the stronger “no finite typing repairs it” result and records both thickness obstructions.

9. **Minor cleanup.**
   - Removed the undefined/loaded term “superfinite” and stated Gold's obstruction directly.
   - Moved the rank-zero/Link parenthetical outside the polynomial-construction theorem statement.
   - Broadened the formal definition of rule/nonterminal thickness to arbitrary reduced finite presentations, while retaining polynomial equivalence only for reduced good presentations.

## Deliberately not added

- **No claim that rank-unbounded identification is new for trivial typing.** That would contradict Yoshinaka (2011), Corollary 2.
- **No new `L_ef` fan-out-sensitivity language.** Yoshinaka's existing Example 5 already supplies the untyped baseline phenomenon.
- **No `L_cat` minimum-rank-two separation theorem yet.** The proposed rank-one impossibility proof does not yet exhaust all good unary fan-out-two template forms (in particular, separated occurrences of two child components inside one output component), so adding it now would create a new correctness risk.
- **No global renaming of theta/tau.** The manuscript keeps `theta_G` = rule thickness and `tau_G` = nonterminal thickness, with the explicit Yoshinaka notation correspondence already stated.

## Build / checks

- `pdflatex` run three times successfully.
- Final PDF: **40 pages** in the current 11pt / 1in layout.
- No undefined references or citations.
- No duplicate labels.
- No missing or unused bibliography entries.
- No overfull boxes reported on the final pass.
- PDF rendered to PNG at 150 dpi; pages containing the new Introduction material, fan-out-one equivalence proposition, and Appendix thickness propositions were visually inspected.