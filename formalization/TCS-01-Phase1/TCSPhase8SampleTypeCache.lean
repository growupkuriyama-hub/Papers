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
    nlinarith

#print axioms TCSPhase8.cacheSampleTypes_count_le_square
end TCSPhase8
