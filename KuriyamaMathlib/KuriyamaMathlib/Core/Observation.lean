import LeanCfgProject.TCS1.FixedHSubstitutability

/-! Shared word and observation interface. The old finite-monoid typing is
not identified with the newer surjective semigroup typing. -/
namespace KuriyamaMathlib

universe u v

abbrev Word (α : Type u) := List α
abbrev Context (α : Type u) := Word α × Word α

abbrev FiniteMonoidObservation (α : Type u) (M : Type v)
    [Monoid M] [Fintype M] :=
  LeanCfgProject.TCS1.FixedFiniteMonoidHom α M

/-- The fibre of a word observation (no algebraic assumptions needed). -/
def fiber {α : Type u} {M : Type v} (obs : Word α → M) (m : M) :
    Set (Word α) := {w | obs w = m}

/-- Interface for the new papers: an observation on nonempty words.
The multiplicative, surjectivity and fresh-identity requirements belong
to a subsequent semigroup-extension module, not this bare interface. -/
abbrev NonemptyWord (α : Type u) := {w : Word α // w ≠ []}

theorem fiber_refines {α : Type u} {M N : Type v}
    (fine : Word α → N) (coarse : Word α → M)
    (π : N → M) (h : ∀ w, coarse w = π (fine w)) (n : N) :
    fiber fine n ⊆ fiber coarse (π n) := by
  intro w hw
  change fine w = n at hw
  change coarse w = π n
  rw [h w, hw]

end KuriyamaMathlib
