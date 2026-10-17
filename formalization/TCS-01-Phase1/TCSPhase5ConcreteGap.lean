import TCSPhase5Monotonicity
import TCSPhase3CClarkEyraud

namespace TCSPhase5
open TCSPhase1 TCSPhase2

/-- Connect our general fixed-monoid definition with the existing
separately proved specific Phase 2 / 3C definition. -/
theorem languageMinus_generic_typed (n : Nat) :
    TypedSubstitutable hU (LanguageMinus n) := by
  intro x y hx hy ht hc
  exact TCSPhase3.languageMinus_typed n x y hx hy ht hc

/-- Soundness of the genuine newly formalized Rec_h_U, not Phase 1's
abstract operator. -/
theorem rec_languageMinus_sound (n : Nat) (K : Finset Word)
    (hK : (↑K : Set Word) ⊆ LanguageMinus n) :
    RecLanguage hU K ⊆ LanguageMinus n :=
  rec_soundness hU K (LanguageMinus n) hK
    (languageMinus_generic_typed n)

/-- Proposition 6.3(iii): the exponential witness cannot appear in the
actual reconstruction unless it was included in the positive sample. -/
theorem rec_witness_exclusion (n : Nat) (K : Finset Word)
    (hK : (↑K : Set Word) ⊆ Language n)
    (hnot : witness n ∉ K) :
    witness n ∉ RecLanguage hU K := by
  have hKminus : (↑K : Set Word) ⊆ LanguageMinus n := by
    intro x hx
    refine ⟨hK hx, ?_⟩
    intro he
    have hxeq : x = witness n := Set.mem_singleton_iff.mp he
    exact hnot (hxeq ▸ hx)
  intro hrec
  have hminus := rec_languageMinus_sound n K hKminus hrec
  exact hminus.2 (Set.mem_singleton_iff.mpr rfl)

#print axioms TCSPhase5.languageMinus_generic_typed
#print axioms TCSPhase5.rec_languageMinus_sound
#print axioms TCSPhase5.rec_witness_exclusion

end TCSPhase5
