import TCSPhase6Main

/-! Positive texts and finite observation prefixes for Gold identification. -/
namespace TCSPhase7

variable {Alphabet : Type*} [DecidableEq Alphabet]

/-- A positive text is sound and enumerates every member of its nonempty target. -/
structure PositiveText (Alphabet : Type*) (L : Set (List Alphabet)) where
  data : Nat → List Alphabet
  positive : ∀ n, data n ∈ L
  covering : ∀ w, w ∈ L → ∃ n, data n = w

/-- Observations at stage n: input positions 0, ..., n-1. -/
def observed (T : Nat → List Alphabet) (n : Nat) : Finset (List Alphabet) :=
  (Finset.range n).image T

theorem observed_zero (T : Nat → List Alphabet) :
    observed T 0 = ∅ := by
  simp [observed]

theorem observed_succ (T : Nat → List Alphabet) (n : Nat) :
    observed T (n + 1) = insert (T n) (observed T n) := by
  simp [observed, Finset.range_succ]

theorem observed_current (T : Nat → List Alphabet) (n : Nat) :
    T n ∈ observed T (n + 1) := by
  rw [observed_succ]
  exact Finset.mem_insert_self _ _

theorem observed_mono (T : Nat → List Alphabet) {m n : Nat} (hm : m ≤ n) :
    observed T m ⊆ observed T n := by
  intro w hw
  obtain ⟨i, hi, rfl⟩ := Finset.mem_image.mp hw
  exact Finset.mem_image.mpr
    ⟨i, Finset.mem_range.mpr (lt_of_lt_of_le (Finset.mem_range.mp hi) hm), rfl⟩

theorem observed_positive {L : Set (List Alphabet)}
    (T : PositiveText Alphabet L) (n : Nat) :
    (↑(observed T.data n) : Set (List Alphabet)) ⊆ L := by
  intro w hw
  obtain ⟨i, _, rfl⟩ := Finset.mem_image.mp hw
  exact T.positive i

/-- Any finite subset of a text's target is eventually observed, from the
covering condition of the text rather than an extra stabilization assumption. -/
theorem eventually_observes_finite {L : Set (List Alphabet)}
    (T : PositiveText Alphabet L) (W : Finset (List Alphabet))
    (hW : (↑W : Set (List Alphabet)) ⊆ L) :
    ∃ n : Nat, W ⊆ observed T.data n := by
  classical
  suffices aux : ∀ (F : Finset (List Alphabet)),
      (↑F : Set (List Alphabet)) ⊆ L →
      ∃ n : Nat, F ⊆ observed T.data n from aux W hW
  intro F
  induction F using Finset.induction_on with
  | empty =>
      intro _
      exact ⟨0, Finset.empty_subset _⟩
  | @insert w F hnot ih =>
      intro hsub
      have hwL : w ∈ L := hsub (Finset.mem_insert_self _ _)
      have hFL : (↑F : Set (List Alphabet)) ⊆ L := by
        intro x hx
        exact hsub (Finset.mem_insert_of_mem hx)
      obtain ⟨n, hn⟩ := ih hFL
      obtain ⟨k, hk⟩ := T.covering w hwL
      refine ⟨max n (k+1), ?_⟩
      intro x hx
      rcases Finset.mem_insert.mp hx with rfl | hmem
      · apply (observed_mono T.data (Nat.le_max_right n (k + 1)))
        simpa [hk] using (observed_current T.data k)
      · apply (observed_mono T.data (Nat.le_max_left n (k + 1)))
        exact hn hmem

#print axioms TCSPhase7.observed_positive
#print axioms TCSPhase7.eventually_observes_finite
end TCSPhase7
