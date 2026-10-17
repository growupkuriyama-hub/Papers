# Phase 5A: genuine finite-sample reconstruction Rec_h

Paper: *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*, TCS-D-26-00494. Source of truth: `01_fixed-h-cfg/main.tex`, main HEAD `8de71485799120c963b58b701921e25eb62aede4`, `PAPER.yaml` v222, file blob SHA `3963c9f93c08d00cb47e0421ad5e16932d651051`.

Branch: `formalization/tcs-phase5a-rec-soundness-20261017`, based on Phase 4 final HEAD `5d83a618386c935968f17d8980841d04627cc293`. All Phase 1–4 original proof sources are unchanged.

## Exact generic model

For an alphabet `Alphabet`, monoid `M`, free list monoid `List Alphabet`, and genuine Lean `MonoidHom` `h : List Alphabet →* M`, finite samples are `Finset (List Alphabet)`. In the finite presentation the alphabet has `[Fintype Alphabet]`; the soundness theorem works even without a finite alphabet or finite monoid.

`ObservedFactor K x` means `x≠[]` and `∃u,v, u++x++v∈K`. These are **contiguous nonempty factors**, not subsequences. `ObservedFactors K` is an actual finite set with a proved membership equivalence. `DirectSimilar h K x y` is exactly equal h-type plus one **direct** shared sample context; it is not replaced by its transitive closure.

`RecFactorDerives` has exactly (L) observed one-letter lexical, (B) observed nonempty concatenation, and (U) observed direct overlap with equal type; unary cycles remain allowed. `RecStartDerives` adds exactly (S) observed nonempty sample starts and the optional empty-word start when epsilon belongs to K. `RecLanguage` is defined from these inductive **grammar derivations**, not from desired soundness.

`RecGrammar` stores concrete finite B/U/L/S production `Finset`s, with the nonterminal set exactly `ObservedFactors K`. `FiniteRecFactorDerives` and `FiniteRecStartDerives` are independently generated from these **finite rules**. Theorems `finite_rec_factor_iff`, `finite_rec_start_iff` and `finite_rec_language_iff` prove precise equivalence to the proof-friendly original derivations.

## Phase 5A targets

`rec_factor_soundness_invariant` proves `Distributions L x = Distributions L w ∧ h w = h x` by induction on the actual B/U/L tree, assuming only `K⊆L` and `TypedSubstitutable h L`.

`rec_soundness`: `K⊆L → TypedSubstitutable h L → RecLanguage h K ⊆ L`.

`rec_sample_consistency`: `K⊆RecLanguage h K`, including the empty and epsilon samples.

`rec_monotone`: `K⊆K' → RecLanguage h K ⊆ RecLanguage h K'`.

The optional `rec_languageMinus_sound` and `rec_witness_exclusion` apply the same **real operator** to the original Phase 2 punctured language and Proposition 6.3(iii). See [PHASE5A_VERIFICATION_REPORT.md](PHASE5A_VERIFICATION_REPORT.md) for exact statements and final CI status.

## Reproduction and scope

Run `lake update`, `lake exe cache get`, `lake build` from this folder. [The Phase 5A workflow](../../.github/workflows/tcs-phase5a-lean.yml) uses Lean 4.24.0 / Mathlib v4.24.0, directly compiles every old and new Lean module and audits forbidden proof tokens and `sorryAx`.

The canonical-witness completeness theorem, characteristic-sample existence, conservative Gold-learner convergence, and polynomial-time reconstruction algorithm are **not** formalized here. The finite-rule construction is mathematically finite; no polynomial executable complexity bound is claimed. Neither the TCS source and responses nor main, arXiv or Editorial Manager were changed.
