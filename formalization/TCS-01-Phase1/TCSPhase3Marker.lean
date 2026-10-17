import TCSPhase3Suffix

/-! Appendix C last-closing-marker invariant. The assertion is restricted to
the two actual closing stack symbols; the arbitrary-nt version is false. -/

namespace TCSPhase3
open TCSPhase1 TCSPhase2

/-- Once only a closing marker remains, parsing can only stay there
with empty input or pop it and terminate. -/
theorem run_single_closer {bound : Nat} {m : Frame}
    (hm : m = Frame.ceilClose ∨ m = Frame.floorClose)
    {w : Word} {θ : Stack}
    (h : Run bound [m] w θ) :
    θ = [] ∨ θ = [m] := by
  rcases hm with rfl | rfl
  · cases h with
    | nil _ => exact Or.inr rfl
    | next hs hr =>
        cases hs with
        | ceilPop tail => exact Or.inl (run_from_nil hr).2
  · cases h with
    | nil _ => exact Or.inr rfl
    | next hs hr =>
        cases hs with
        | floorPop tail => exact Or.inl (run_from_nil hr).2

/-- Every nonempty result of a run starting with a bottom closing marker
still has EXACTLY the same bottom marker, regardless of how much prefix
was consumed. This is the actual paper's last-marker property. -/
theorem run_preserves_last_marker {bound : Nat} {m : Frame}
    (hm : m = Frame.ceilClose ∨ m = Frame.floorClose)
    {α θ : Stack} {w : Word}
    (h : Run bound (α ++ [m]) w θ) (hθ : θ ≠ []) :
    ∃ β : Stack, θ = β ++ [m] := by
  by_cases hα : α = []
  · subst α
    have hsingle : Run bound [m] w θ := by simpa using h
    rcases run_single_closer hm hsingle with he | he
    · exact False.elim (hθ he)
    · exact ⟨[], by simpa using he⟩
  · rcases first_visit_factorization hα h with hremain | hvisit
    · obtain ⟨β, _, _, he⟩ := hremain
      exact ⟨β, he⟩
    · obtain ⟨u, v, hw, hu, hv⟩ := hvisit
      rcases run_single_closer hm hv with he | he
      · exact False.elim (hθ he)
      · exact ⟨[], by simpa using he⟩

/-- Two nonempty stacks with distinct bottom closing markers cannot match. -/
theorem ceil_floor_suffix_ne (α β : Stack) :
    α ++ [Frame.ceilClose] ≠ β ++ [Frame.floorClose] := by
  intro h
  have hr := congrArg List.reverse h
  simp [List.reverse_append] at hr

#print axioms TCSPhase3.run_single_closer
#print axioms TCSPhase3.run_preserves_last_marker
#print axioms TCSPhase3.ceil_floor_suffix_ne

end TCSPhase3
