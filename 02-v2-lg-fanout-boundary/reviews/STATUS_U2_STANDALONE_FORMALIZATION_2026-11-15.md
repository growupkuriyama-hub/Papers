# U₂ standalone theorem — mathematical status and archival index (2026-11-15)

**Scope: research-only, not manuscript mathematics.** Paper #2 `main.tex`, `japanese/main_JP.tex`, built PDFs, `PAPER.yaml`, Theorems A/B/C, and Open Problem `op:fanout-two` were **not edited**.

## 1. Statement and verdict

For `Σ={a,b,c}`, overlapping projections `A={a,c}`, `B={b,c}`, length-two endpoint/count data `dat_ov`, content typing `c_Σ`, fan-out ≤2, rank ≤2, and a reduced good MCFG `G` of a substitutable target `L` whose nonempty membership is determined by `dat_ov`, the separately written research theorem gives

\[
\tau(G,c_\Sigma)=O(v^{18}\bar\theta_G^{17}),\qquad
\|K\|_+=O(\|G\|^{19}\bar\theta_G^{17}).
\]

Here `v=|V(G)|` and `\bar\theta_G` is the rule thickness **of the original grammar**. The detailed inequality and constant `4096` are in the theorem note. The argument bounds **distribution-equivalent representatives**, not shortest yields of typed nonterminals.

**Status:** A full hand-proof argument has been submitted by Claude Round Eleven and independently hand-audited by ChatGPT as **VALID WITH CLARIFICATIONS**. The standalone note reorders and sharpens its statement, explains the corrected no-jump DFS argument, expands one delicate `0e2(ii)` subcase, and explicitly lists publication-oriented refinements. This is **not** expert peer review or machine-checked formal verification. No general result about arbitrary typings or pseudovarieties is inferred. **The actual `op:fanout-two` remains OPEN.**

## 2. Artifact index

- [Theorem U₂ — standalone mathematical note and complete argument](theorem_U2_overlapping_projections_standalone_2026-11-15.md)
- [Round Eleven reproducibility bundle: original report, checkpoint, checker, logs, dependencies, and independent audit](ROUND11_SOURCE_BUNDLE_2026-11-15.md). The raw original files are included with byte lengths and SHA256 in the bundle.
- [Round Nine P1/B6 report](claude_fanout2_round9_P1_B6_report_2026-11-14.md), [Round Nine independent audit](audit_round9_P1_B6_independent_2026-11-14.md)
- [Round Ten U₂ integration report](claude_fanout2_round10_U2_integration_report_2026-11-14.md), [Round Ten independent audit](audit_claude_fanout2_round10_independent_2026-11-15.md)
- Existing [Round Eight HC_III report](claude_fanout2_round8_HCIII_report_2026-11-14.md) and [Round Eight independent audit](audit_claude_fanout2_round8_independent_2026-11-14.md)
- [Main paper source](../main.tex) (**untouched**)

## 3. Proof dependencies — none silently imported

1. Round Nine P1: full-Σ span impurity coloring, true nonnegative window deletion, componentwise `c` conservation, whole-word boundary-window identity. Count-only B6: disjoint deletion sets of origin windows, preserved endpoint signature/content, realizable intermediate states. The stronger position-form invariant is false and not needed.
2. Round Ten P0 uses **total projected bigram counts** over components and componentwise endpoint signature/content. H** expands any nonnegative conservative difference into hole words. J joins F-side/Y-side hole hosting into a strict distribution-preserving shortening step, subject to no more than two nonempty, nonadjacent holes and projection-length requirements.
3. Round Eleven M/V/E/N: endpoint marks exclude purported half-transition types in nonrich components; E closes same-root ac/b or bc/a; N covers the full nonrich family. The rich case is covered by T5. Earlier HC_I/II/III and T1–T4 are no longer needed as direct proof dependencies.
4. Typed-root minimum derivation height `H≤49v`, ≤`32c*` marked positions (with `c*=3`), polynomial number of span colors, origin-window partition, and the **correct** bound that only the colors of *non-jump DFS positions* are pairwise distinct (≤C), yield exponent `18` in `v`, `17` in original `θ̄_G`.
5. Apply canonical `cor:distribution-representatives` to obtain sample total length, using the original grammar's `θ̄_G`, not refined-grammar thickness.

## 4. Reproduction / proof quality limits

- Submitted Round Eleven model checker: **193,945 settings**, `PROOF_FAIL=0`, `VERIFY_FAIL=0`; 838 configurations in previously OPEN types passed, and 475 nonzero actual-good-derivation stages passed. The previous full independent rerun reproduced `ALL CHECKS PASSED`; time/explicit exit notation differences only.
- Additional independent checker (not importing Claude code): **88,572 nonempty words of length ≤10**, all checked marked-window M/V implications passed.
- The constructed cases used partial hosting oracles in some finite validations. Actual **typed-node-minimal** derivations of the former same-root residual were not independently generated.
- The `0e2(ii)` same/different `c`-interval ordering in the nonrich case deserves an explicit independent, interval-indexed proof in an eventual publication and expert adversarial review. Section 6.2 of the theorem note records this and other proof presentation obligations.
- No assertion of complete formal verification or independently peer-reviewed theorem is made here.

## 5. Manuscript / open problem boundary

This research note is not a revision to paper #2. It is a special-class upper bound and is **not** either direction of the full LG pseudovariety boundary question at fan-out ≥2. In particular it is not a universal upper bound for `U₁` typings; `c_Σ` and unbounded `dat_ov` must not be identified with `U₁`.

**Future work:** obtain expert-level adversarial line-by-line proof review, optionally formalize local Γ/hosting lemmas, consider a separate paper for this theorem, and independently resume superpolynomial lower-bound search for the true `op:fanout-two`.
