import KuriyamaMathlib.Algebra.SemigroupTyping
import KuriyamaMathlib.Distribution.Closure

/-! Paper 02 CFG: observation-relative substitutability interface.
LG, U₁, thickness and characteristic-data theorems are not yet ported. -/
namespace KuriyamaMathlib

universe u v

def ObservationSubstitutable {α : Type u} {M : Type v}
    (obs : Word α → M) (L : Set (Word α)) : Prop :=
  ∀ x y : Word α, x ≠ [] → y ≠ [] → obs x = obs y →
    LeanCfgProject.TCS1.HaveSharedContext L x y →
    LeanCfgProject.TCS1.Distribution L x =
      LeanCfgProject.TCS1.Distribution L y

theorem observationSubstitutable_of_refines {α : Type u} {M N : Type v}
    (coarse : Word α → M) (fine : Word α → N)
    (π : N → M) (h : ∀ w, coarse w = π (fine w))
    (L : Set (Word α)) (hL : ObservationSubstitutable coarse L) :
    ObservationSubstitutable fine L := by
  intro x y hx hy ht hc
  apply hL x y hx hy _ hc
  rw [h x, h y, ht]

end KuriyamaMathlib
