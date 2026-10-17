import TCSPhase7Learner
import TCSPhase5BCharacteristic

/-! Structural stabilization and Gold identification for the actual
finite-production reconstruction grammar, independently of complexity. -/
namespace TCSPhase7
open TCSPhase5
open TCSPhase5B

variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

variable (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
variable (T : PositiveText Alphabet (GrammarLanguage G))
variable (hSub : TypedSubstitutable h (GrammarLanguage G))

/-- The finite characteristic set appears in some finite prefix of every text. -/
theorem characteristic_stage :
    ∃ n₀ : Nat, PositiveWitnesses G h ⊆ observed T.data n₀ := by
  exact eventually_observes_finite T (PositiveWitnesses G h)
    (positive_witnesses_subset_language G h)

/-- A first post-characteristic rebuild uses the full observed sample and
therefore reconstructs the target language exactly. -/
theorem rebuild_after_characteristic
    {n₀ n : Nat} (hle : n₀ ≤ n+1)
    (hW : PositiveWitnesses G h ⊆ observed T.data n₀)
    (hRebuild : RebuildAt h T.data n) :
    hypothesisLanguage h (learner h T.data (n+1)) = GrammarLanguage G := by
  have hWn : PositiveWitnesses G h ⊆ observed T.data (n+1) :=
    Finset.Subset.trans hW (observed_mono T.data hle)
  rw [learner_rebuild h T.data n hRebuild]
  exact rec_exact_reconstruction G h (observed T.data (n+1))
    hSub hWn (observed_positive T (n+1))

/-- If a hypothesis already generates the whole target, no later positive
input can trigger an update. The snapshot (and its CFG) is unchanged. -/
theorem stable_after_exact
    (n₀ : Nat)
    (hExact : hypothesisLanguage h (learner h T.data n₀) = GrammarLanguage G) :
    ∀ n : Nat, n₀ ≤ n → learner h T.data n = learner h T.data n₀ := by
  have aux : ∀ d : Nat, learner h T.data (n₀ + d) = learner h T.data n₀ := by
    intro d
    induction d with
    | zero => simp
    | succ d ih =>
        have hmem : T.data (n₀+d) ∈
            hypothesisLanguage h (learner h T.data (n₀+d)) := by
          rw [ih, hExact]
          exact T.positive (n₀+d)
        calc
          learner h T.data (n₀ + (d+1)) =
              learner h T.data ((n₀+d)+1) := by simp [Nat.add_assoc]
          _ = learner h T.data (n₀+d) :=
              learner_conservative h T.data (n₀+d) hmem
          _ = learner h T.data n₀ := ih
  intro n hn
  obtain ⟨d, hd⟩ := Nat.exists_eq_add_of_le hn
  rw [hd]
  exact aux d

/-- Once characteristic observations exist, two distinct subsequent
rebuild events are impossible. This counts events, not only changed CFGs. -/
theorem at_most_one_rebuild_after_characteristic
    {n₀ : Nat} (hW : PositiveWitnesses G h ⊆ observed T.data n₀) :
    ∀ n m : Nat, n₀ ≤ n+1 → n < m →
      RebuildAt h T.data n → ¬ RebuildAt h T.data m := by
  intro n m hn hlt hRebuild hLater
  have hexact := rebuild_after_characteristic G h T hSub hn hW hRebuild
  have hfixed : learner h T.data m = learner h T.data (n+1) :=
    stable_after_exact G h T (n+1) hexact m (Nat.succ_le_iff.mpr hlt)
  have hmem : T.data m ∈ hypothesisLanguage h (learner h T.data m) := by
    rw [hfixed, hexact]
    exact T.positive m
  exact hLater hmem

/-- The same post-characteristic at-most-one statement for actual changes
of finite grammar snapshots (which need not coincide with rebuild events). -/
theorem at_most_one_change_after_characteristic
    {n₀ : Nat} (hW : PositiveWitnesses G h ⊆ observed T.data n₀) :
    ∀ n m : Nat, n₀ ≤ n+1 → n < m →
      learner h T.data (n+1) ≠ learner h T.data n →
      ¬ (learner h T.data (m+1) ≠ learner h T.data m) := by
  intro n m hn hlt hchange hlater
  have hr := change_implies_rebuild h T.data n hchange
  have hrLater := change_implies_rebuild h T.data m hlater
  exact (at_most_one_rebuild_after_characteristic G h T hSub hW
    n m hn hlt hr) hrLater

/-- If no later rebuild occurs, all hypotheses are literally one CFG. -/
theorem stable_if_no_rebuild (n₀ : Nat)
    (hNo : ∀ n, n₀ ≤ n → ¬ RebuildAt h T.data n) :
    ∀ n, n₀ ≤ n → learner h T.data n = learner h T.data n₀ := by
  classical
  have aux : ∀ d : Nat, learner h T.data (n₀+d) = learner h T.data n₀ := by
    intro d
    induction d with
    | zero => simp
    | succ d ih =>
        have hnot := hNo (n₀+d) (Nat.le_add_right n₀ d)
        have hmem : T.data (n₀+d) ∈
            hypothesisLanguage h (learner h T.data (n₀+d)) :=
          not_not.mp hnot
        calc
          learner h T.data (n₀+(d+1)) =
              learner h T.data ((n₀+d)+1) := by simp [Nat.add_assoc]
          _ = learner h T.data (n₀+d) :=
              learner_conservative h T.data (n₀+d) hmem
          _ = learner h T.data n₀ := ih
  intro n hn
  obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le hn
  rw [hd]
  exact aux d

/-- Without a later rebuild the fixed hypothesis is correct because the text
covers the entire target, not simply because its syntax is constant. -/
theorem exact_if_no_rebuild (n₀ : Nat)
    (hNo : ∀ n, n₀ ≤ n → ¬ RebuildAt h T.data n) :
    hypothesisLanguage h (learner h T.data n₀) = GrammarLanguage G := by
  apply Set.Subset.antisymm
  · exact learner_soundness h T hSub n₀
  · intro w hw
    obtain ⟨i, hi⟩ := T.covering w hw
    let n := max n₀ (i+1)
    have hwi : w ∈ observed T.data (i+1) := by
      simpa [hi] using (observed_current T.data i)
    have hwn : w ∈ observed T.data n :=
      (observed_mono T.data (Nat.le_max_right n₀ (i+1))) hwi
    have hCons := learner_sample_consistency h T.data n hwn
    rw [stable_if_no_rebuild h T n₀ hNo n (Nat.le_max_left n₀ (i+1))] at hCons
    exact hCons

/-- Gold identification with equality of finite-grammar snapshots, not merely
an equality of abstract languages. -/
theorem gold_identification :
    ∃ N : Nat,
      (∀ n : Nat, N ≤ n → learner h T.data n = learner h T.data N) ∧
      hypothesisLanguage h (learner h T.data N) = GrammarLanguage G := by
  obtain ⟨n₀,hW⟩ := characteristic_stage G h T
  by_cases hSome : ∃ n : Nat, n₀ ≤ n ∧ RebuildAt h T.data n
  · obtain ⟨n,hn,hRebuild⟩ := hSome
    have hExact := rebuild_after_characteristic G h T hSub
      (Nat.le_trans hn (Nat.le_succ n)) hW hRebuild
    exact ⟨n+1, stable_after_exact G h T (n+1) hExact, hExact⟩
  · have hNo : ∀ n, n₀ ≤ n → ¬ RebuildAt h T.data n := by
      intro n hn hr
      exact hSome ⟨n, hn, hr⟩
    exact ⟨n₀, stable_if_no_rebuild h T n₀ hNo,
      exact_if_no_rebuild G h T hSub n₀ hNo⟩

#print axioms TCSPhase7.characteristic_stage
#print axioms TCSPhase7.rebuild_after_characteristic
#print axioms TCSPhase7.stable_after_exact
#print axioms TCSPhase7.at_most_one_rebuild_after_characteristic
#print axioms TCSPhase7.at_most_one_change_after_characteristic
#print axioms TCSPhase7.exact_if_no_rebuild
#print axioms TCSPhase7.gold_identification
end TCSPhase7
