import TCSPhase2

/-!
Phase 2, Milestone D: exact distribution/context definitions and a CONDITIONAL
bridge from Clark–Eyraud substitutability to fixed-h substitutability
after a regular type filter. The Appendix C CE premise is not proved.
-/

namespace TCSPhase2

/-- Distribution of a factor x: pairs (u,v) with uxv in the target. -/
def Distributions (L : Set Word) (x : Word) : Set (Word × Word) :=
  {p | p.1 ++ x ++ p.2 ∈ L}

/-- The two factor distributions have a common context. -/
def SharedContext (L : Set Word) (x y : Word) : Prop :=
  ∃ p : Word × Word, p ∈ Distributions L x ∧ p ∈ Distributions L y

/-- Clark–Eyraud substitutability on NONEMPTY factors only. -/
def ClarkEyraud (L : Set Word) : Prop :=
  ∀ x y : Word, x ≠ [] → y ≠ [] →
    SharedContext L x y → Distributions L x = Distributions L y

/-- Same property with equality of factor h-types required. -/
def TypedSubstitutable (h : Word →* U1) (L : Set Word) : Prop :=
  ∀ x y : Word, x ≠ [] → y ≠ [] → h x = h y →
    SharedContext L x y → Distributions L x = Distributions L y

/-- Common h-typing of x,y preserves membership in an arbitrary filter F
inside *every* surrounding context. -/
theorem filter_distributions_eq
    (h : Word →* U1) (F : Set U1) (L : Set Word)
    (x y : Word) (hxy : h x = h y)
    (hd : Distributions L x = Distributions L y) :
    Distributions (L ∩ {w | h w ∈ F}) x =
      Distributions (L ∩ {w | h w ∈ F}) y := by
  ext p
  have hcontext : h (p.1 ++ x ++ p.2) = h (p.1 ++ y ++ p.2) := by
    change h (p.1 * x * p.2) = h (p.1 * y * p.2)
    simp only [map_mul, hxy]
  change (p.1 ++ x ++ p.2 ∈ L ∧ h (p.1 ++ x ++ p.2) ∈ F) ↔
    (p.1 ++ y ++ p.2 ∈ L ∧ h (p.1 ++ y ++ p.2) ∈ F)
  constructor
  · rintro ⟨hxL, hxF⟩
    have hp : p ∈ Distributions L x := hxL
    rw [hd] at hp
    exact ⟨hp, hcontext ▸ hxF⟩
  · rintro ⟨hyL, hyF⟩
    have hp : p ∈ Distributions L y := hyL
    rw [← hd] at hp
    exact ⟨hp, hcontext.symm ▸ hyF⟩

/-- Proposition 6.3(iv) proof's filter step, conditional on CE of L.
Stronger: ANY accepting type set F, rather than just {zero}. -/
theorem ce_filter_is_typed
    (h : Word →* U1) (F : Set U1) (L : Set Word)
    (hCE : ClarkEyraud L) :
    TypedSubstitutable h (L ∩ {w | h w ∈ F}) := by
  intro x y hx hy ht hshared
  obtain ⟨p, hpx, hpy⟩ := hshared
  have hLshared : SharedContext L x y :=
    ⟨p, hpx.1, hpy.1⟩
  exact filter_distributions_eq h F L x y ht
    (hCE x y hx hy hLshared)

/-- Only CE(L_n) remains unproved (Appendix C); the step to
typed substitutability of the *concretely derived* punctured target is verified. -/
theorem languageMinus_typed_of_CE (n : Nat)
    (hCE : ClarkEyraud (Language n)) :
    TypedSubstitutable hU (LanguageMinus n) := by
  have hfilter : LanguageMinus n =
      Language n ∩ {w | hU w ∈ ({U1.zero} : Set U1)} := by
    rw [languageMinus_type_zero]
    ext w
    simp
  rw [hfilter]
  exact ce_filter_is_typed hU ({U1.zero} : Set U1) (Language n) hCE

#print axioms TCSPhase2.filter_distributions_eq
#print axioms TCSPhase2.ce_filter_is_typed
#print axioms TCSPhase2.languageMinus_typed_of_CE

end TCSPhase2
