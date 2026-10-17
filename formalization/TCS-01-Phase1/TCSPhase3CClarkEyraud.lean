import TCSPhase3CPathCongruence

namespace TCSPhase3
open TCSPhase1 TCSPhase2

/-- Proposition 6.3(i): the original grammar language is CE-substitutable.
No CE hypothesis or special parser starting-state assumption is used. -/
theorem language_clark_eyraud (n : Nat) :
    ClarkEyraud (TCSPhase2.Language n) := by
  intro x y hx hy hshared
  obtain ⟨⟨p, q⟩, hpx, hpy⟩ := hshared
  have hpxL : p ++ x ++ q ∈ TCSPhase2.Language n := hpx
  have hpyL : p ++ y ++ q ∈ TCSPhase2.Language n := hpy
  have hacceptx : Run n [Frame.nt n] (p ++ (x ++ q)) [] := by
    simpa [List.append_assoc] using
      grammar_language_parses n (p ++ x ++ q) hpxL
  have haccepty : Run n [Frame.nt n] (p ++ (y ++ q)) [] := by
    simpa [List.append_assoc] using
      grammar_language_parses n (p ++ y ++ q) hpyL
  obtain ⟨σx, hpRunx, hxqRun⟩ :=
    run_append_split p (x ++ q) hacceptx
  obtain ⟨σy, hpRuny, hyqRun⟩ :=
    run_append_split p (y ++ q) haccepty
  have hσ : σx = σy := run_deterministic hpRunx hpRuny
  cases hσ
  obtain ⟨θx, hxRun, hqxRun⟩ :=
    run_append_split x q hxqRun
  obtain ⟨θy, hyRun, hqyRun⟩ :=
    run_append_split y q hyqRun
  have hθ : θx = θy := run_reverse_injective hqxRun hqyRun
  cases hθ
  exact path_congruence n σx θx x y hxRun hyRun

/-- The punctured language is finite since the original grammar language is. -/
theorem punctured_language_finite (n : Nat) :
    (LanguageMinus n).Finite := by
  apply (language_finite n).subset
  intro w hw
  exact hw.1

/-- Unconditional h_U-typed substitutability; no residual CE premise. -/
theorem languageMinus_typed (n : Nat) :
    TypedSubstitutable hU (LanguageMinus n) := by
  exact languageMinus_typed_of_CE n (language_clark_eyraud n)

#print axioms TCSPhase3.language_clark_eyraud
#print axioms TCSPhase3.punctured_language_finite
#print axioms TCSPhase3.languageMinus_typed

end TCSPhase3
