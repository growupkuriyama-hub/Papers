import KuriyamaMathlib.Algebra.SemigroupTyping

/-! A fresh identity, not the original identity of an existing monoid. -/
namespace KuriyamaMathlib
universe u v

def freshMul {S : Type v} [Semigroup S] : Option S → Option S → Option S
  | none, b => b
  | some a, none => some a
  | some a, some b => some (a * b)

theorem freshMul_assoc {S : Type v} [Semigroup S] (a b c : Option S) :
    freshMul (freshMul a b) c = freshMul a (freshMul b c) := by
  cases a <;> cases b <;> cases c <;> simp [freshMul, mul_assoc]

theorem freshMul_none_left {S : Type v} [Semigroup S] (a : Option S) :
    freshMul none a = a := rfl

theorem freshMul_none_right {S : Type v} [Semigroup S] (a : Option S) :
    freshMul a none = a := by cases a <;> rfl

theorem foldl_mul_left {α : Type u} {S : Type v} [Semigroup S]
    (letter : α → S) (w : Word α) (x y : S) :
    w.foldl (fun acc b => acc * letter b) (x * y) =
      x * w.foldl (fun acc b => acc * letter b) y := by
  induction w generalizing y with
  | nil => rfl
  | cons a w ih =>
    simp only [List.foldl_cons]
    rw [mul_assoc, ih]

theorem FiniteSemigroupTyping.eval_append {α : Type u} {S : Type v}
    [Semigroup S] [Fintype S] (T : FiniteSemigroupTyping α S)
    (u v : Word α) :
    T.eval (u ++ v) = freshMul (T.eval u) (T.eval v) := by
  cases u with
  | nil => rfl
  | cons a u =>
    cases v with
    | nil => simp [FiniteSemigroupTyping.eval, freshMul]
    | cons b v =>
      simp only [List.cons_append, FiniteSemigroupTyping.eval, freshMul,
        List.foldl_append, List.foldl_cons]
      rw [foldl_mul_left]

end KuriyamaMathlib
