import TCSPhase8TrieCost

/-!
Exact logical semantics of the *existing* instrumented bit-trie insertion
program. The trie is not merely a set surrogate: the statements below
are about `insertCount` and `insertManyCount` from Phase 8.
-/
namespace TCSPhase8.BitTrie

/-- An empty trie accepts no bit string. -/
theorem contains_empty_eq_false (q : List Bool) :
    contains q empty = false := by
  induction q with
  | nil => rfl
  | cons bit rest ih =>
    cases bit <;> rfl

@[simp]
theorem contains_blank_false (q : List Bool) :
    contains q (.node false none none) = false := by
  simpa [empty] using contains_empty_eq_false q

/-- One concrete insertion adds exactly its argument to the recognized
language; all previously accepted keys are preserved. -/
theorem contains_insertCount_iff
    (key query : List Bool) (trie : BitTrie) :
    contains query (insertCount key trie).1 = true ↔
      query = key ∨ contains query trie = true := by
  induction key generalizing trie query with
  | nil =>
      cases trie with
      | node accept left right =>
        cases query with
        | nil => simp [insertCount, contains]
        | cons bit rest =>
          cases bit <;> simp [insertCount, contains]
  | cons bit rest ih =>
      cases trie with
      | node accept left right =>
        cases query with
        | nil => cases bit <;> simp [insertCount, contains]
        | cons qbit qrest =>
          cases bit <;> cases qbit <;>
            cases left <;> cases right <;>
            simp [insertCount, contains, ih, contains_blank_false]

/-- The concrete batch insertion preserves the exact input key set,
allowing duplicates in its input list. -/
theorem contains_insertManyCount_iff
    (keys : List (List Bool)) (trie : BitTrie) (query : List Bool) :
    contains query (insertManyCount keys trie).1 = true ↔
      query ∈ keys ∨ contains query trie = true := by
  induction keys generalizing trie with
  | nil =>
      simp [insertManyCount]
  | cons key rest ih =>
      change
        contains query (insertManyCount rest (insertCount key trie).1).1 = true ↔
          query ∈ (key :: rest) ∨ contains query trie = true
      rw [ih, contains_insertCount_iff]
      simp only [List.mem_cons]
      tauto

/-- The batch trie produced from an initially empty trie recognizes
precisely the supplied list of keys, independent of their duplicates. -/
theorem contains_insertMany_empty_iff
    (keys : List (List Bool)) (query : List Bool) :
    contains query (insertManyCount keys empty).1 = true ↔ query ∈ keys := by
  rw [contains_insertManyCount_iff]
  simp [contains_empty_eq_false]

#print axioms TCSPhase8.BitTrie.contains_empty_eq_false
#print axioms TCSPhase8.BitTrie.contains_insertCount_iff
#print axioms TCSPhase8.BitTrie.contains_insertManyCount_iff
#print axioms TCSPhase8.BitTrie.contains_insertMany_empty_iff

end TCSPhase8.BitTrie
