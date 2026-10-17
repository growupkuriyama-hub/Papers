# Phase 7 — Gold convergence formal-verification report

**Status: A — the mathematical theorem suite is kernel-verified.** Proof-code Git HEAD `e5256bdf086f4b3ac7e10cf3d85ce0b6fc996d11` passed [GitHub Actions 39079689703](https://github.com/growupkuriyama-hub/Papers/actions/runs/39079689703), job **117533933589**. The report-only final HEAD is checked by its separate automatic workflow run.

## Baseline and scope

Target `01_fixed-h-cfg/main.tex`, `cor:ilt`, `PAPER.yaml` `v227`. Phase 6 inherited baseline `da6cdc7c0e601d967069d582b120979a3beea010` (successful [Phase6 run 39077871376](https://github.com/growupkuriyama-hub/Papers/actions/runs/39077871376), job `117528675709`). Phase 7 branch `formalization/tcs-phase7-gold-convergence-20261018`. Lean 4.24.0; Mathlib v4.24.0. Previous 49 inherited modules and nine Phase6 additions are unchanged.

`PositiveText Alphabet L` is a structure with `data : Nat → List Alphabet`, `positive : ∀ n, data n ∈ L`, and `covering : ∀ w, w ∈ L → ∃ n, data n = w`. Its finite prefix is `observed T n = (Finset.range n).image T`.

`Hypothesis Alphabet` has constructors `initial` and `reconstructed (sample : Finset (List Alphabet))`. `hypothesisGrammar h (.reconstructed K) = TCSPhase5.makeRecGrammar h K`, the real finite B/U/L/S production sets, with independent language semantics `finite_rec_language_iff`. The initial grammar has no start productions and empty language. `learner h T` is a noncomputable structural `Nat.rec` that retains the hypothesis if `T n` belongs to its generated language and otherwise rebuilds with `observed T (n+1)`.

## Exact theorem statements (Lean identifiers)

1. **`eventually_observes_finite`**: For a finite `W` with `(↑W : Set (List Alphabet)) ⊆ L`, `∃ n, W ⊆ observed T.data n`. This is proved from enumeration, not assumed.
2. **`learner_conservative`**: `T n ∈ hypothesisLanguage h (learner h T n) → learner h T (n+1) = learner h T n`.
3. **`learner_rebuild`**: `RebuildAt h T n → learner h T (n+1) = .reconstructed (observed T (n+1))`. `learner_step` proves both alternatives of the actual update.
4. **`change_implies_rebuild`**: `learner h T (n+1) ≠ learner h T n → RebuildAt h T n`. A rebuild event need not be treated as a distinct hypothesis object.
5. **`learner_sample_consistency`**:
   ```lean
   ∀ n : Nat, (↑(observed T n) : Set (List Alphabet)) ⊆
     hypothesisLanguage h (learner h T n)
   ```
   Uses the **existing** `TCSPhase5.rec_sample_consistency`.
6. **`learner_soundness`** for `T : PositiveText Alphabet L` and `hSub : TypedSubstitutable h L`:
   ```lean
   ∀ n : Nat, hypothesisLanguage h (learner h T.data n) ⊆ L
   ```
   Uses the **existing** `TCSPhase5.rec_soundness`.
7. **`characteristic_stage`** for `T : PositiveText Alphabet (GrammarLanguage G)`:
   ```lean
   ∃ n₀ : Nat, PositiveWitnesses G h ⊆ observed T.data n₀
   ```
   Uses `positive_witnesses_subset_language` from Phase5B and the finite-text lemma.
8. **`rebuild_after_characteristic`** under explicit `hSub`, `n₀ ≤ n+1`, witness-set inclusion in `observed T.data n₀`, and `RebuildAt h T.data n`:
   ```lean
   hypothesisLanguage h (learner h T.data (n+1)) = GrammarLanguage G
   ```
   Uses genuine Phase5B `rec_exact_reconstruction` and full sample inclusion.
9. **`stable_after_exact`**: If `hypothesisLanguage h (learner h T.data n₀) = GrammarLanguage G`, then `∀ n, n₀ ≤ n → learner h T.data n = learner h T.data n₀`; identity is **syntactic**.
10. **`at_most_one_rebuild_after_characteristic`**, under `hSub` and `hW : PositiveWitnesses G h ⊆ observed T.data n₀`:
    ```lean
    ∀ n m : Nat, n₀ ≤ n+1 → n < m →
      RebuildAt h T.data n → ¬ RebuildAt h T.data m
    ```
11. **`at_most_one_change_after_characteristic`**, under the same hypotheses:
    ```lean
    ∀ n m : Nat, n₀ ≤ n+1 → n < m →
      learner h T.data (n+1) ≠ learner h T.data n →
      ¬ (learner h T.data (m+1) ≠ learner h T.data m)
    ```
12. **`exact_if_no_rebuild`**, under `hSub` and `hNo : ∀ n, n₀ ≤ n → ¬ RebuildAt h T.data n`:
    ```lean
    hypothesisLanguage h (learner h T.data n₀) = GrammarLanguage G
    ```
    Text coverage provides `GrammarLanguage G ⊆ hypothesisLanguage` by a sufficiently late observed prefix and `learner_sample_consistency`; `learner_soundness` supplies the reverse inclusion. No unsupported inference from inactivity occurs.
13. **`gold_identification`** under explicit `hSub : TypedSubstitutable h (GrammarLanguage G)`:
    ```lean
    ∃ N : Nat,
      (∀ n : Nat, N ≤ n → learner h T.data n = learner h T.data N) ∧
      hypothesisLanguage h (learner h T.data N) = GrammarLanguage G
    ```
    The proof splits on the existence of a rebuild after a finite characteristic stage and combines the previously established alternatives.

## CI, intermediate failures, and axiom audit

- Exploratory [run 39078615273](https://github.com/growupkuriyama-hub/Papers/actions/runs/39078615273): stopped at the implicit `Decidable` obligation of a conditional in a theorem statement.
- Exploratory [run 39078932384](https://github.com/growupkuriyama-hub/Papers/actions/runs/39078932384): same statement-level problem; the learner transition was restated as a two-case proposition without an artificial decidability hypothesis.
- Exploratory [run 39079356127](https://github.com/growupkuriyama-hub/Papers/actions/runs/39079356127): texts, learner, and `stable_after_exact` checked, but convergence proofs omitted `hSub` from several declaration statements; explicit substitution assumptions were added without changing the mathematical claim.
- **Successful proof code run:** [39079689703](https://github.com/growupkuriyama-hub/Papers/actions/runs/39079689703), job `117533933589`, HEAD `e5256bdf086f4b3ac7e10cf3d85ce0b6fc996d11`, `lake build` **7448 jobs**. Four new Phase 7 modules and all nine Phase6 modules compiled directly in order, then all 49 inherited Phase1–5B modules compiled directly. Last job message: `All Phase 1-7 modules compiled and kernel axioms audited`.

All inspected `#print axioms` outputs for every new main theorem, notably `gold_identification`, `rebuild_after_characteristic`, `at_most_one_rebuild_after_characteristic`, `at_most_one_change_after_characteristic`, `exact_if_no_rebuild`, show **[propext, Classical.choice, Quot.sound]**, and no `sorryAx`. The source scan for forbidden proof commands passed. There are **no custom unproved mathematical axioms**.

## Indexing, edge cases, protected files

`observed T n` uses input indices below `n`. `RebuildAt h T n` is a reconstruction at output stage `n+1`; hence `n₀ ≤ n+1` represents the manuscript's `n ≥ n₀` correctly in one-based output indexing, including the initial observation-stage boundary. A positive-text structure entails a nonempty target, including singleton epsilon; empty targets require a separate presentation protocol. No probability, efficiency, time complexity, normalization, or shortlex-tie theorem is claimed.

Protected change audit against `da6cdc7c0e601d967069d582b120979a3beea010`: only new `TCSPhase7*.lean` files, Phase7-specific workflow, and these new reports. No changes to the English/Japanese paper, `PAPER.yaml`, response to reviewers, submitted PDF, existing Phase1–6 mathematical proofs, main branch, arXiv, or Editorial Manager.

**Formal outcome: Phase7 class A for the requested conservative Gold convergence theorem, validated on proof-code HEAD.** The closing docs-only commit is then checked on its own final HEAD by the same comprehensive workflow; that final CI URL is reported alongside the commit once the run finishes.
