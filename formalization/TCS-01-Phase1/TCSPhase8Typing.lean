import TCSPhase8Occurrences

/-! A constructive letter table and recursive finite-monoid word type. -/
namespace TCSPhase8
variable {Alphabet M : Type*} [Monoid M]

structure LetterTable (Alphabet M : Type*) where
  letter : Alphabet → M

def codeWord (t : LetterTable Alphabet M) : List Alphabet → M
  | [] => 1
  | a :: w => t.letter a * codeWord t w

theorem codeWord_append (t : LetterTable Alphabet M) (u v : List Alphabet) :
    codeWord t (u ++ v) = codeWord t u * codeWord t v := by
  induction u with
  | nil => simp [codeWord]
  | cons a xs ih => simp [codeWord, ih, mul_assoc]

theorem codeWord_single_append (t : LetterTable Alphabet M)
    (w : List Alphabet) (a : Alphabet) :
    codeWord t (w ++ [a]) = codeWord t w * t.letter a := by
  rw [codeWord_append]
  simp [codeWord]

theorem codeWord_eq_h (h : List Alphabet →* M)
    (t : LetterTable Alphabet M)
    (ht : ∀ a, t.letter a = h [a]) (w : List Alphabet) :
    codeWord t w = h w := by
  induction w with
  | nil => simp [codeWord]
  | cons a xs ih =>
    calc
      codeWord t (a :: xs) = t.letter a * codeWord t xs := rfl
      _ = h [a] * h xs := by rw [ht a, ih]
      _ = h (a :: xs) := by
        change h [a] * h xs = h ([a] * xs)
        rw [map_mul]

#print axioms TCSPhase8.codeWord_append
#print axioms TCSPhase8.codeWord_single_append
#print axioms TCSPhase8.codeWord_eq_h
end TCSPhase8
