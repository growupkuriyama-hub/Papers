import TCSPhase3Main

/-!
Appendix C first-visit suffix factorization. "First visit" is enforced by
induction: the active prefix remains nonempty at each recursive step until
a step first yields the empty active prefix. Thereafter the suffix run is
kept separate and may consume the suffix.
-/

namespace TCSPhase3
open TCSPhase1 TCSPhase2

/-- There is no outgoing one-letter transition from the empty stack. -/
theorem no_step_from_nil {bound : Nat} {c : Terminal} {t : Stack} :
    ¬ Step bound [] c t := by
  intro h
  cases h

/-- Every run from an empty stack consumes no characters and stays empty. -/
theorem run_from_nil {bound : Nat} {w : Word} {t : Stack}
    (h : Run bound [] w t) : w = [] ∧ t = [] := by
  cases h with
  | nil _ => exact ⟨rfl, rfl⟩
  | next hs hr => exact False.elim (no_step_from_nil hs)

/-- A single transition on a nonempty prefix cannot touch the appended suffix.
The new active prefix may become empty, precisely at the first visit. -/
theorem step_prefix_decompose {bound : Nat} {α ψ θ : Stack}
    {c : Terminal} (hα : α ≠ [])
    (h : Step bound (α ++ ψ) c θ) :
    ∃ β : Stack, Step bound α c β ∧ θ = β ++ ψ := by
  cases α with
  | nil => contradiction
  | cons top rest =>
      change Step bound (top :: (rest ++ ψ)) c θ at h
      cases h with
      | atom tail =>
          exact ⟨rest, Step.atom rest, rfl⟩
      | unary i hi tail =>
          exact ⟨Frame.nt i :: Frame.ceilClose :: rest,
            Step.unary i hi rest, rfl⟩
      | binary i hi tail =>
          exact ⟨Frame.nt i :: Frame.nt i :: Frame.floorClose :: rest,
            Step.binary i hi rest, rfl⟩
      | ceilPop tail =>
          exact ⟨rest, Step.ceilPop rest, rfl⟩
      | floorPop tail =>
          exact ⟨rest, Step.floorPop rest, rfl⟩

/-- Either a nonempty active prefix remains after the entire input, or a
prefix u of the input first empties the active prefix and all subsequent
input v runs on the exposed suffix. -/
theorem first_visit_factorization {bound : Nat}
    {α ψ θ : Stack} {w : Word} (hα : α ≠ [])
    (h : Run bound (α ++ ψ) w θ) :
    (∃ β : Stack, β ≠ [] ∧ Run bound α w β ∧ θ = β ++ ψ) ∨
    (∃ u v : Word, w = u ++ v ∧ Run bound α u [] ∧
      Run bound ψ v θ) := by
  induction w generalizing α θ with
  | nil =>
      cases h
      exact Or.inl ⟨α, hα, Run.nil α, rfl⟩
  | cons c rest ih =>
      cases h with
      | next hs hr =>
          obtain ⟨β, hstep, heq⟩ :=
            step_prefix_decompose hα hs
          cases heq
          by_cases hβ : β = []
          · right
            subst β
            exact ⟨[c], rest, rfl, Run.next hstep (Run.nil []), hr⟩
          · rcases ih hβ hr with hremain | hver
            · obtain ⟨γ, hγ, hrun, hfinal⟩ := hremain
              left
              exact ⟨γ, hγ, Run.next hstep hrun, hfinal⟩
            · obtain ⟨u, v, hw, hu, hv⟩ := hver
              right
              refine ⟨c :: u, v, ?_, Run.next hstep hu, hv⟩
              simp [hw]

/-- A run that arrives at the protected suffix must have consumed its
whole input while emptying the active prefix. -/
theorem run_to_suffix_iff_run_to_nil {bound : Nat}
    {α ψ : Stack} {w : Word} (hα : α ≠ []) :
    Run bound (α ++ ψ) w ψ ↔ Run bound α w [] := by
  constructor
  · intro hr
    rcases first_visit_factorization hα hr with hremain | hver
    · obtain ⟨β, hβ, hb, heq⟩ := hremain
      have hlen : β.length + ψ.length = ψ.length := by
        have := congrArg List.length heq
        simpa [List.length_append] using this.symm
      have hzero : β = [] := List.length_eq_zero_iff.mp (by omega)
      exact False.elim (hβ hzero)
    · obtain ⟨u, v, hw, hu, hv⟩ := hver
      have hvnil : v = [] := run_no_nonempty_cycle hv
      subst v
      simpa [hw] using hu
  · intro hr
    simpa using run_suffix hr ψ

#print axioms TCSPhase3.no_step_from_nil
#print axioms TCSPhase3.run_from_nil
#print axioms TCSPhase3.step_prefix_decompose
#print axioms TCSPhase3.first_visit_factorization
#print axioms TCSPhase3.run_to_suffix_iff_run_to_nil

end TCSPhase3
