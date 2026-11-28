import KuriyamaMathlib.MCFG.Basic
import KuriyamaMathlib.Algebra.SemigroupTyping

/-! Paper 02 MCFG: reuse the existing arity-indexed MCFG syntax.
The legacy module is imported unchanged; no new fan-out theorem is claimed. -/
namespace KuriyamaMathlib

universe u v

abbrev WordTuple (α : Type u) (d : Nat) := MCFG.Tuple α d

def tupleObservation {α : Type u} {M : Type v} {d : Nat}
    (obs : Word α → M) (x : WordTuple α d) : Fin d → M :=
  fun i => obs (x i)

theorem tupleObservation_refines {α : Type u} {M N : Type v} {d : Nat}
    (fine : Word α → N) (coarse : Word α → M)
    (π : N → M) (h : ∀ w, coarse w = π (fine w)) (x : WordTuple α d) :
    tupleObservation coarse x = fun i => π (tupleObservation fine x i) := by
  funext i
  exact h (x i)

end KuriyamaMathlib
