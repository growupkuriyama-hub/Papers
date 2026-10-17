import TCSPhase3Subtree
import TCSPhase3Marker

/-! Auxiliary lemmas for Appendix C branch synchronization. -/
namespace TCSPhase3
open TCSPhase1 TCSPhase2

theorem frame_weight_pos (f : Frame) : 0 < frameWeight f := by
  cases f with
  | nt i =>
      exact pow_pos (by omega : (0 : Nat) < 4) i
  | ceilClose => simp [frameWeight]
  | floorClose => simp [frameWeight]

theorem weight_append (α ψ : Stack) :
    weight (α ++ ψ) = weight α + weight ψ := by
  induction α with
  | nil => simp [weight]
  | cons a as ih =>
      simp only [List.cons_append, weight, ih]
      omega

theorem weight_pos_of_ne {α : Stack} (h : α ≠ []) :
    0 < weight α := by
  cases α with
  | nil => contradiction
  | cons a as =>
      simp only [weight]
      have := frame_weight_pos a
      omega

theorem weight_nonempty_prefix_gt (α ψ : Stack) (h : α ≠ []) :
    weight ψ < weight (α ++ ψ) := by
  rw [weight_append]
  have := weight_pos_of_ne h
  omega

theorem weight_of_run_suffix_le {bound : Nat} {ψ θ : Stack}
    {w : Word} (h : Run bound ψ w θ) :
    weight θ ≤ weight ψ := run_weight_le h

theorem suffix_cancel_right (α β ψ : Stack)
    (h : α ++ ψ = β ++ ψ) : α = β := by
  simpa only [List.append_cancel_right_eq] using h

/-- Active nonvisited runs cannot lose or change their bottom closing marker. -/
theorem nonvisited_ceil_marker {bound : Nat} {β : Stack}
    {w : Word} (hβ : β ≠ [])
    (h : Run bound [Frame.nt 0, Frame.ceilClose] w β) :
    ∃ γ, β = γ ++ [Frame.ceilClose] := by
  exact run_preserves_last_marker (Or.inl rfl) (by simpa using h) hβ

/-- A useful reusable suffix-visit decision, including exact weight bounds. -/
theorem classified_first_visit {bound : Nat} {α ψ θ : Stack}
    {w : Word} (hα : α ≠ [])
    (h : Run bound (α ++ ψ) w θ) :
    (∃ β : Stack, β ≠ [] ∧ Run bound α w β ∧
        θ = β ++ ψ ∧ weight ψ < weight θ) ∨
    (∃ u v : Word, w = u ++ v ∧
        Run bound α u [] ∧ Run bound ψ v θ ∧
        weight θ ≤ weight ψ) := by
  rcases first_visit_factorization hα h with hremain | hvisit
  · obtain ⟨β, hβ, hb, heq⟩ := hremain
    left
    exact ⟨β, hβ, hb, heq, heq ▸ weight_nonempty_prefix_gt β ψ hβ⟩
  · obtain ⟨u, v, hw, hu, hv⟩ := hvisit
    right
    exact ⟨u, v, hw, hu, hv, run_weight_le hv⟩

/-- Exactly the two distinct initial-branch shapes of this parser. -/
theorem distinct_initial_steps {bound : Nat} {σ σ₁ σ₂ : Stack}
    {c d : Terminal} (hc : c ≠ d)
    (h₁ : Step bound σ c σ₁)
    (h₂ : Step bound σ d σ₂) :
    ∃ i ψ, i + 1 ≤ bound ∧ σ = Frame.nt (i + 1) :: ψ ∧
    ((c = Terminal.squareLeft ∧ σ₁ =
        Frame.nt i :: Frame.ceilClose :: ψ ∧
      d = Terminal.left ∧ σ₂ =
        Frame.nt i :: Frame.nt i :: Frame.floorClose :: ψ) ∨
     (c = Terminal.left ∧ σ₁ =
        Frame.nt i :: Frame.nt i :: Frame.floorClose :: ψ ∧
      d = Terminal.squareLeft ∧ σ₂ =
        Frame.nt i :: Frame.ceilClose :: ψ)) := by
  cases h₁ <;> cases h₂ <;> simp_all <;> aesop

#print axioms TCSPhase3.frame_weight_pos
#print axioms TCSPhase3.weight_append
#print axioms TCSPhase3.weight_nonempty_prefix_gt
#print axioms TCSPhase3.suffix_cancel_right
#print axioms TCSPhase3.classified_first_visit
#print axioms TCSPhase3.distinct_initial_steps
end TCSPhase3
