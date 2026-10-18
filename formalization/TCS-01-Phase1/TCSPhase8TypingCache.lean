import TCSPhase8Typing

/-!
# Incremental monoid typing cache

A concrete List scan records each prefix type, along with exactly one
multiplication per extension. A second scan starts at each nonempty suffix.
These counts cover monoid multiplications only, not list allocation,
substring copying, dictionary operations, or wall-clock time.
-/
namespace TCSPhase8

variable {Alphabet M : Type*} [Monoid M]

/-- A single left-to-right scan. The Nat result counts each actual
occurrence of the multiplication `acc * t.letter a` in this algorithm. -/
def cachedScan (t : LetterTable Alphabet M) (acc : M) :
    List Alphabet → List M × Nat
  | [] => ([], 0)
  | a :: rest =>
      let next := acc * t.letter a
      let result := cachedScan t next rest
      (next :: result.1, result.2 + 1)

/-- Each extension executes exactly one recorded monoid multiplication. -/
theorem cachedScan_count (t : LetterTable Alphabet M) (acc : M)
    (w : List Alphabet) : (cachedScan t acc w).2 = w.length := by
  induction w generalizing acc with
  | nil => rfl
  | cons a ws ih =>
    change (cachedScan t (acc * t.letter a) ws).2 + 1 = (a::ws).length
    rw [ih]
    rfl

theorem cachedScan_length (t : LetterTable Alphabet M) (acc : M)
    (w : List Alphabet) : (cachedScan t acc w).1.length = w.length := by
  induction w generalizing acc with
  | nil => rfl
  | cons a ws ih =>
    change ((acc * t.letter a) ::
      (cachedScan t (acc * t.letter a) ws).1).length = (a::ws).length
    simpa using ih (acc * t.letter a)

/-- An independently defined standard-library running fold specifies
exactly the stored sequence (excluding its initial value). -/
theorem cachedScan_eq_scanl (t : LetterTable Alphabet M)
    (acc : M) (w : List Alphabet) :
    (cachedScan t acc w).1 =
      (w.scanl (fun m a => m * t.letter a) acc).drop 1 := by
  induction w generalizing acc with
  | nil => rfl
  | cons a ws ih =>
    change (acc * t.letter a) ::
      (cachedScan t (acc * t.letter a) ws).1 =
      List.scanl (fun m a => m * t.letter a) (acc * t.letter a) ws
    rw [ih]
    cases ws <;> rfl

/-- Scan every start position, storing each nonempty interval's type
by a single multiplication that extends its previous interval. -/
def cacheAllStarts (t : LetterTable Alphabet M) :
    List Alphabet → List (List M) × Nat
  | [] => ([], 0)
  | a :: rest =>
      let head := cachedScan t 1 (a :: rest)
      let tail := cacheAllStarts t rest
      (head.1 :: tail.1, head.2 + tail.2)

/-- The number of monoid multiplications is quadratically bounded for
the complete cache of interval types in one word. -/
theorem cacheAllStarts_count_le_square (t : LetterTable Alphabet M)
    (w : List Alphabet) :
    (cacheAllStarts t w).2 ≤ (w.length + 1)^2 := by
  induction w with
  | nil => simp [cacheAllStarts]
  | cons a rest ih =>
    change (cachedScan t 1 (a::rest)).2 + (cacheAllStarts t rest).2 ≤
      ((a::rest).length + 1)^2
    rw [cachedScan_count]
    simp only [List.length_cons]
    nlinarith

#print axioms TCSPhase8.cachedScan_count
#print axioms TCSPhase8.cachedScan_length
#print axioms TCSPhase8.cachedScan_eq_scanl
#print axioms TCSPhase8.cacheAllStarts_count_le_square
end TCSPhase8
