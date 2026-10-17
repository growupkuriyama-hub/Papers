import TCSPhase3Suffix

/-! Reverse recognition: actual parser runs returning to their old suffix
are grammar derivations in TCSPhase2.Language, not an invented language. -/

namespace TCSPhase3
open TCSPhase1 TCSPhase2

/-- If the overall run empties the entire stack, it must have visited a
nonempty protected suffix, and that first visit splits the input. -/
theorem split_run_to_nil {bound : Nat} {α ψ : Stack} {w : Word}
    (hα : α ≠ []) (hψ : ψ ≠ [])
    (h : Run bound (α ++ ψ) w []) :
    ∃ u v : Word, w = u ++ v ∧
      Run bound α u [] ∧ Run bound ψ v [] := by
  rcases first_visit_factorization hα h with hremain | hvisit
  · obtain ⟨β, hβ, hrun, heq⟩ := hremain
    have hn : (β ++ ψ).length = 0 :=
      congrArg List.length heq.symm
    rw [List.length_append] at hn
    have hψ0 : ψ.length = 0 := by omega
    have hh : ψ = [] := List.length_eq_zero_iff.mp hψ0
    exact False.elim (hψ hh)
  · exact hvisit

/-- A complete pop of one ceiling-closing marker consumes exactly its label. -/
theorem run_ceil_close_exact {bound : Nat} {w : Word}
    (h : Run bound [Frame.ceilClose] w []) :
    w = [Terminal.squareRight] := by
  cases h with
  | next hs hr =>
      cases hs with
      | ceilPop tail =>
          obtain ⟨he, _⟩ := run_from_nil hr
          subst he
          rfl

theorem run_floor_close_exact {bound : Nat} {w : Word}
    (h : Run bound [Frame.floorClose] w []) :
    w = [Terminal.right] := by
  cases h with
  | next hs hr =>
      cases hs with
      | floorPop tail =>
          obtain ⟨he, _⟩ := run_from_nil hr
          subst he
          rfl

/-- Reverse-recognition with empty protected suffix.
Natural-number induction is on the actual nonterminal height. -/
theorem run_nt_nil_derives (bound : Nat) :
    ∀ (i : Nat) (w : Word), i ≤ bound →
      Run bound [Frame.nt i] w [] → Derives i w := by
  intro i
  induction i with
  | zero =>
      intro w hi hr
      cases hr with
          | next hs hrest =>
          cases hs with
          | atom tail =>
              obtain ⟨hword, _⟩ := run_from_nil hrest
              subst hword
              exact Derives.atom
  | succ i ih =>
      intro w hi hr
      cases hr with
          | next hs hrest =>
          cases hs with
          | unary j hj tail =>
              obtain ⟨u, v, heq, hu, hv⟩ :=
                split_run_to_nil
                  (α := [Frame.nt i]) (ψ := [Frame.ceilClose])
                  (by simp) (by simp) (by simpa using hrest)
              have hv' := run_ceil_close_exact hv
              have hdu : Derives i u := ih u (by omega) hu
              rw [heq, hv']
              simpa [unaryWord] using (Derives.unary hdu)
          | binary j hj tail =>
              obtain ⟨u, rest, heq, hu, hr2⟩ :=
                split_run_to_nil
                  (α := [Frame.nt i]) (ψ := [Frame.nt i, Frame.floorClose])
                  (by simp) (by simp) (by simpa using hrest)
              have ht2 : Run bound
                  ([Frame.nt i] ++ [Frame.floorClose]) rest [] := by
                simpa using hr2
              obtain ⟨v, tailw, heq2, hv, hpop⟩ :=
                split_run_to_nil (by simp) (by simp) ht2
              have hc := run_floor_close_exact hpop
              have hdu : Derives i u := ih u (by omega) hu
              have hdv : Derives i v := ih v (by omega) hv
              rw [heq, heq2, hc]
              simpa [binaryWord, List.append_assoc] using
                (Derives.binary hdu hdv)

/-- Converse of the first equivalence in Appendix C Lemma C.1. -/
theorem recognition_converse (bound i : Nat) (ψ : Stack) (w : Word)
    (hi : i ≤ bound)
    (h : Run bound (Frame.nt i :: ψ) w ψ) :
    w ∈ Language i := by
  have h0 : Run bound [Frame.nt i] w [] := by
    exact (run_to_suffix_iff_run_to_nil (by simp : [Frame.nt i] ≠ [])).mp
      (by simpa using h)
  exact run_nt_nil_derives bound i w hi h0

theorem recognition_iff (bound i : Nat) (ψ : Stack) (w : Word)
    (hi : i ≤ bound) :
    Run bound (Frame.nt i :: ψ) w ψ ↔ w ∈ Language i := by
  constructor
  · exact recognition_converse bound i ψ w hi
  · exact generated_word_parses bound i ψ w hi

#print axioms TCSPhase3.split_run_to_nil
#print axioms TCSPhase3.run_ceil_close_exact
#print axioms TCSPhase3.run_floor_close_exact
#print axioms TCSPhase3.run_nt_nil_derives
#print axioms TCSPhase3.recognition_converse
#print axioms TCSPhase3.recognition_iff

end TCSPhase3
