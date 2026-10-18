import TCSPhase8TypingCache

/-!
# Incremental typing cache across a list of sample words

The Nat component counts every monoid multiplication performed by
the structurally recursive cache construction. The bound is on those
multiplications; it is NOT a total execution-time assertion.
-/
namespace TCSPhase8

variable {Alphabet M : Type*} [Monoid M]

/-- Encoded list-sample size, including one delimiter per word. -/
def encodedListSample (sample : List (List Alphabet)) : Nat :=
  (sample.map (fun w => w.length + 1)).sum

/-- One complete all-starts cache for every word, preserving sample order. -/
def cacheSampleTypes (t : LetterTable Alphabet M) :
    List (List Alphabet) → List (List (List M)) × Nat
  | [] => ([], 0)
  | w :: rest =>
      let current := cacheAllStarts t w
      let later := cacheSampleTypes t rest
      (current.1 :: later.1, current.2 + later.2)

/-- The entire concrete list traversal uses at most n² multiplications. -/
theorem cacheSampleTypes_count_le_square
    (t : LetterTable Alphabet M) (sample : List (List Alphabet)) :
    (cacheSampleTypes t sample).2 ≤ (encodedListSample sample)^2 := by
  induction sample with
  | nil => simp [cacheSampleTypes, encodedListSample]
  | cons w rest ih =>
    change (cacheAllStarts t w).2 + (cacheSampleTypes t rest).2 ≤
      (w.length + 1 + encodedListSample rest)^2
    have hw := cacheAllStarts_count_le_square t w
    have hcross : 0 ≤ (w.length + 1) * encodedListSample rest := Nat.zero_le _
    nlinarith

/-- The concrete List representation of a Finset has precisely the
original encoded sample size. -/
theorem encodedListSample_toList [DecidableEq Alphabet]
    (K : Finset (List Alphabet)) :
    encodedListSample K.toList = TCSPhase1.encodedSize K := by
  classical
  simp [encodedListSample, TCSPhase1.encodedSize]

/-- Quadratic bound in the paper's actual finite-sample size n_K,
for all monoid multiplication updates executed by this List algorithm. -/
theorem cacheSampleTypes_finset_count_le_square [DecidableEq Alphabet]
    (t : LetterTable Alphabet M) (K : Finset (List Alphabet)) :
    (cacheSampleTypes t K.toList).2 ≤ (TCSPhase1.encodedSize K)^2 := by
  simpa only [encodedListSample_toList] using
    (cacheSampleTypes_count_le_square t K.toList)

#print axioms TCSPhase8.encodedListSample_toList
#print axioms TCSPhase8.cacheSampleTypes_finset_count_le_square

#print axioms TCSPhase8.cacheSampleTypes_count_le_square
end TCSPhase8
