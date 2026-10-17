# Phase 5A Formal Verification Report — Rec_h B/U/L/S reconstruction

## A. Provenance

Paper: Takayuki Kuriyama, *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*, TCS-D-26-00494. Main HEAD: `8de71485799120c963b58b701921e25eb62aede4`. `01_fixed-h-cfg/PAPER.yaml` internal **v222**, source `main.tex` Git blob `3963c9f93c08d00cb47e0421ad5e16932d651051`.

Verified source claims by labels, not line-number guessing: `lem:sample-consistency`, `thm:soundness`, `eq:soundness-invariant`, `prop:typed-thickness-gap` item (iii), and literal (B)(U)(L)(S) rules of `sec:algo`.

Branch: `formalization/tcs-phase5a-rec-soundness-20261017`, branched from completed Phase 4 `5d83a618386c935968f17d8980841d04627cc293`. All Phase 1–4 Lean theorems and the protected manuscript files must remain unmodified. **Lean 4.24.0, Lake 5.0.0, Mathlib v4.24.0.**

## B. Definition audit

- `ObservedFactor K x := x ≠ [] ∧ ∃ u v, u ++ x ++ v ∈ K`: an actual contiguous nonempty factor.
- `ObservedFactors K : Finset (List Alphabet)`: finite enumeration based on finite alphabets and an upper bound from `encodedSize K`; `mem_observedFactors` establishes equivalence, `observedFactors_mono` inclusion monotonicity.
- `SampleDistributions K x` and `Distributions L x`: sets of **two-sided** context pairs. Left/right congruence is independently established for any alphabet.
- `DirectSimilar h K x y := h x = h y ∧ ∃p, p∈D_K(x) ∧ p∈D_K(y)`. No transitive closure is used. Nonemptiness is required at both endpoints of each U production.
- `RecFactorDerives`: inductive lexical (L), binary (B), direct unary (U). Explicit observed-factor requirements hold for all their displayed nonterminal names. The unary case does not assume acyclicity.
- `RecStartDerives`: nonempty sample-start production (S), optional empty-word start exactly when epsilon occurs in K.
- `RecGrammar`: actual **finite** nonterminal, binary, unary, lexical and start `Finset`s. Membership is checked by `rec_{node,lexical,binary,unary,start}_iff` and `rec_start_empty_iff`.
- `FiniteRecFactorDerives`/`FiniteRecStartDerives`: independently defined inductive derivations **from the real finite rule sets**; `finite_rec_factor_iff`, `finite_rec_start_iff` and `finite_rec_language_iff` prove exact equivalence.

The generic main soundness and sample theorems require `[DecidableEq Alphabet]`, `[Monoid M]`, and `h : List Alphabet →* M`. The real finite presentation uses additionally `[Fintype Alphabet]`. Thus even though the paper assumes a finite target monoid, the proved logical soundness has no `[Fintype M]` hypothesis. No special `U1` assumption is made in the general proof.

## C. Core exact kernel-checked theorem interfaces

```lean
theorem rec_factor_nonempty
    (hd : RecFactorDerives h K x w) : w ≠ []

theorem rec_factor_soundness_invariant
    (h : Word Alphabet →* M) (K : Finset (Word Alphabet))
    (L : Set (Word Alphabet))
    (hKL : (↑K : Set (Word Alphabet)) ⊆ L)
    (hSub : TypedSubstitutable h L)
    {x w : Word Alphabet} (hd : RecFactorDerives h K x w) :
    Distributions L x = Distributions L w ∧ h w = h x

theorem rec_soundness
    (h : Word Alphabet →* M) (K : Finset (Word Alphabet))
    (L : Set (Word Alphabet))
    (hKL : (↑K : Set (Word Alphabet)) ⊆ L)
    (hSub : TypedSubstitutable h L) :
    RecLanguage h K ⊆ L

theorem rec_sample_consistency
    (h : Word Alphabet →* M) (K : Finset (Word Alphabet)) :
    (↑K : Set (Word Alphabet)) ⊆ RecLanguage h K

theorem rec_monotone
    (h : Word Alphabet →* M)
    {K K' : Finset (Word Alphabet)} (hKK : K ⊆ K') :
    RecLanguage h K ⊆ RecLanguage h K'
```

**Real CI evidence:** [run #39025683868](https://github.com/growupkuriyama-hub/Papers/actions/runs/39025683868), job `117376087814`, exact successful code commit `b3435521c50e6d18e6873412d108f762a2cfd9b1`. `Build completed successfully (7416 jobs).` Then all direct compiles and source/log scans passed. The main three theorems and invariant report only `[propext, Quot.sound]`, no custom assumptions and no `sorryAx`.

**Finite grammar milestone:** [run #39025908567](https://github.com/growupkuriyama-hub/Papers/actions/runs/39025908567) built `TCSPhase5FactorsFinite`, `TCSPhase5Grammar`, `TCSPhase5FiniteDerivation` and all prior core modules successfully. The **overall run failed** exclusively at the optional concrete `TCSPhase5ConcreteGap.lean` module because `Word` resolved to the generic type constructor rather than `TCSPhase2.Word`. It is **not** counted as a CI success. The exact fix uses `TCSPhase2.Word` in its statements; follow-up CI is tracked separately.

## D. Mathematical proof audit

Factor soundness: tree induction. Lexical is reflexivity. Unary takes an actual shared *sample* context; sample inclusion produces a shared target context; nonempty observed factors and h-type equality allow the original fixed-typing substitutability premise. Transitivity with the subtree invariant finishes both distribution and type equations. Binary uses independently proved left/right distribution-congruence and genuine `MonoidHom.map_mul`; factor labels remain nonempty. Start-word soundness uses the empty left/right context of the actual positive sampled start word, and epsilon is present only if directly sampled.

Sample consistency: structural induction of any positive observed word, using (L) for a singleton and (B) to split its first letter from nonempty remainder. Every factor is justified by the original positive sample occurrence; epsilon uses its separate (S) rule. Empty sample is handled automatically.

Monotonicity: the proof recursively transports each finite derivation tree under `K⊆K'`; observed factors and direct sample overlap are monotone, so B/U/L/S productions are preserved. No grammar-object equality is claimed.

## E. Genuine optional Proposition 6.3(iii)

The implementation connects `TCSPhase3.languageMinus_typed` and the newly proven generic soundness to `RecLanguage TCSPhase2.hU K`. The intended exact theorems are:
```lean
rec_languageMinus_sound (n : Nat) (K : Finset TCSPhase2.Word)
  (hK : (↑K : Set TCSPhase2.Word) ⊆ LanguageMinus n) :
  RecLanguage hU K ⊆ LanguageMinus n

rec_witness_exclusion (n : Nat) (K : Finset TCSPhase2.Word)
  (hK : (↑K : Set TCSPhase2.Word) ⊆ Language n)
  (hnot : witness n ∉ K) :
  witness n ∉ RecLanguage hU K
```
**Milestone H is independently VERIFIED:** [GitHub Actions #39026224393](https://github.com/growupkuriyama-hub/Papers/actions/runs/39026224393), job **`117377624280`**, successful corrected code commit **`72dcba522dc459158012cd82c36c234ad6bd5f05`**. The log contains `Built TCSPhase5ConcreteGap`, `Built TCSPhase5Main`, `Build completed successfully (7426 jobs).`, followed by `Phase 1-5A modules compiled and audited`. Both `rec_languageMinus_sound` and `rec_witness_exclusion` report **`[propext, Classical.choice, Quot.sound]`** only. This does not claim characteristic-sample existence.

## F. Limits

This phase does not prove canonical-witness completeness, existence of characteristic samples, conservative Gold-learning convergence, incremental learner soundness, or polynomial runtime of the grammar-construction algorithm. The bounded-enumeration proof of finite observed factors is mathematical, not an efficient extraction algorithm.

## G. Final integrated audit

**Full mathematics and finite-rule correspondence completed at commit `72dcba522dc459158012cd82c36c234ad6bd5f05`**, CI #39026224393. Core soundness/consistency/monotonicity use **`[propext, Quot.sound]`**, while finite rule enumeration and the special U1 bridge also use standard **`Classical.choice`**. All original 28 modules and the 10 new modules directly compile; no `sorryAx` occurs.

The branch workflow is `.github/workflows/tcs-phase5a-lean.yml`. It rebuilds all **28 earlier sources** and all **10 Phase 5A sources**, and directly checks every Lean file; it runs `#print axioms`, a forbidden-source-proof-token scanner and a `sorryAx` detector. Record the final successful branch HEAD, full job ID, build job count and source-diff audit in the final user-facing report once the **entire** workflow passes. No paper, main branch, arXiv or Editorial Manager mutation is permitted.
