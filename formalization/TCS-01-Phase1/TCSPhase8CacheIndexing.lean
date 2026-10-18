import TCSPhase8SampleTypeCache
import TCSPhase8TypingCacheCorrectness

/-!
Indexed completeness of the *existing* incremental monoid-type cache.
Rows correspond to start positions; columns to nonempty extensions.
All indexing is checked with Option-valued List indexing.
-/
namespace TCSPhase8

variable {Alphabet M : Type*} [Monoid M]

/-- A cached extension at zero-based position j is the type of
the first (j+1) letters. -/
theorem cachedScan_getElem?_spec
    (t : LetterTable Alphabet M) (acc : M) (w : List Alphabet) :
    ∀ j : Nat,
      (cachedScan t acc w).1[j]? =
        if j < w.length then
          some (acc * codeWord t (w.take (j+1)))
        else none := by
  induction w generalizing acc with
  | nil =>
      intro j
      simp [cachedScan]
  | cons a rest ih =>
      intro j
      cases j with
      | zero =>
          simp [cachedScan, codeWord]
      | succ k =>
          simpa [cachedScan, codeWord, mul_assoc] using
            (ih (acc * t.letter a) k)

/-- Exactly one row is stored for each possible nonempty suffix. -/
theorem cacheAllStarts_rows_length
    (t : LetterTable Alphabet M) (w : List Alphabet) :
    (cacheAllStarts t w).1.length = w.length := by
  induction w with
  | nil => rfl
  | cons a rest ih => simp [cacheAllStarts, ih]

/-- Row i is exactly the scan of the suffix beginning at position i. -/
theorem cacheAllStarts_getElem?_spec
    (t : LetterTable Alphabet M) (w : List Alphabet) :
    ∀ i : Nat,
      (cacheAllStarts t w).1[i]? =
        if i < w.length then
          some (cachedScan t 1 (w.drop i)).1
        else none := by
  induction w with
  | nil =>
      intro i
      simp [cacheAllStarts]
  | cons a rest ih =>
      intro i
      cases i with
      | zero => simp [cacheAllStarts]
      | succ k =>
          simpa [cacheAllStarts] using ih k

/-- Checked lookup of a strictly nonempty interval [i,j). -/
def cachedInterval?
    (t : LetterTable Alphabet M) (w : List Alphabet)
    (i j : Nat) : Option M :=
  ((cacheAllStarts t w).1[i]?).bind
    (fun row => row[j-i-1]?)

/-- Every legal nonempty interval is present at its exact cache indices,
and the stored value equals the original mathematical homomorphism. -/
theorem cachedInterval?_eq_h
    (h : List Alphabet →* M)
    (t : LetterTable Alphabet M)
    (ht : ∀ a, t.letter a = h [a])
    (w : List Alphabet) (i j : Nat)
    (hij : i < j) (hj : j ≤ w.length) :
    cachedInterval? t w i j =
      some (h ((w.drop i).take (j-i))) := by
  have hi : i < w.length := lt_of_lt_of_le hij hj
  have hidx : j-i-1 < (w.drop i).length := by
    simp only [List.length_drop]
    omega
  have hsub : j-i-1+1 = j-i := by omega
  unfold cachedInterval?
  rw [cacheAllStarts_getElem?_spec t w i]
  simp only [if_pos hi, Option.bind_some]
  rw [cachedScan_getElem?_spec]
  simp only [if_pos hidx, hsub]
  rw [codeWord_eq_h h t ht]
  simp

#print axioms TCSPhase8.cachedScan_getElem?_spec
#print axioms TCSPhase8.cacheAllStarts_rows_length
#print axioms TCSPhase8.cacheAllStarts_getElem?_spec
#print axioms TCSPhase8.cachedInterval?_eq_h

end TCSPhase8
