import KuriyamaMathlib.Core.Observation

/-! The finite-semigroup convention used by the current papers.
The empty word has a fresh observation value (none), distinct from all
semigroup elements (some s), even when S already has an identity.
The multiplication on the fresh-identity extension and the morphism
theorem are subsequent work. -/
namespace KuriyamaMathlib

universe u v

structure FiniteSemigroupTyping (α : Type u) (S : Type v)
    [Semigroup S] [Fintype S] where
  letter : α → S
  onto : ∀ s : S, ∃ a : α, ∃ w : Word α,
    w.foldl (fun acc b => acc * letter b) (letter a) = s

def FiniteSemigroupTyping.eval {α : Type u} {S : Type v}
    [Semigroup S] [Fintype S] (T : FiniteSemigroupTyping α S) :
    Word α → Option S
  | [] => none
  | a :: w => some (w.foldl (fun acc b => acc * T.letter b) (T.letter a))

theorem FiniteSemigroupTyping.eval_eq_none_iff {α : Type u} {S : Type v}
    [Semigroup S] [Fintype S] (T : FiniteSemigroupTyping α S)
    (w : Word α) : T.eval w = none ↔ w = [] := by
  cases w <;> simp [FiniteSemigroupTyping.eval]

end KuriyamaMathlib
