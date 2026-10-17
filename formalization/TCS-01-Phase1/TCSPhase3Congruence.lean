import TCSPhase3Recognition

/-! General two-sided contextual congruence; does not assume substitutability. -/
namespace TCSPhase3
open TCSPhase2

theorem distributions_left_congruent (L : Set Word) (x y z : Word)
    (hxy : Distributions L x = Distributions L y) :
    Distributions L (z ++ x) = Distributions L (z ++ y) := by
  ext p
  have hp :
      ((p.1 ++ z, p.2) : Word × Word) ∈ Distributions L x ↔
      ((p.1 ++ z, p.2) : Word × Word) ∈ Distributions L y := by
    rw [hxy]
  simpa [Distributions, List.append_assoc] using hp

theorem distributions_right_congruent (L : Set Word) (x y z : Word)
    (hxy : Distributions L x = Distributions L y) :
    Distributions L (x ++ z) = Distributions L (y ++ z) := by
  ext p
  have hp :
      ((p.1, z ++ p.2) : Word × Word) ∈ Distributions L x ↔
      ((p.1, z ++ p.2) : Word × Word) ∈ Distributions L y := by
    rw [hxy]
  simpa [Distributions, List.append_assoc] using hp

theorem distributions_two_sided_congruent (L : Set Word) (x y u v : Word)
    (hxy : Distributions L x = Distributions L y) :
    Distributions L (u ++ x ++ v) = Distributions L (u ++ y ++ v) := by
  exact distributions_right_congruent L (u ++ x) (u ++ y) v
    (distributions_left_congruent L x y u hxy)

#print axioms TCSPhase3.distributions_left_congruent
#print axioms TCSPhase3.distributions_right_congruent
#print axioms TCSPhase3.distributions_two_sided_congruent
end TCSPhase3
