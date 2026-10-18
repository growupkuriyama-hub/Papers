import TCSPhase8TrieSemantics

/-!
Executable one-pass duplicate elimination. The trie controls membership,
while an accumulator retains precisely the keys first encountered.
The accumulator grows by cons, never by a repeated end append.
A separate cost semantics for lookup and the output are still required.
-/
namespace TCSPhase8.BitTrie

/-- Keys already in the trie are skipped; new keys are inserted and
remembered in reverse encounter order. -/
def collectUniqueKeys : List (List Bool) → BitTrie →
    List (List Bool) → BitTrie × List (List Bool)
  | [], trie, acc => (trie, acc)
  | key :: rest, trie, acc =>
      if contains key trie then
        collectUniqueKeys rest trie acc
      else
        collectUniqueKeys rest (insertCount key trie).1 (key :: acc)

/-- This is an invariant of the *concrete* accumulator/trie pair. -/
theorem collectUniqueKeys_mem
    (keys : List (List Bool)) :
    ∀ trie acc,
      (∀ query, query ∈ acc ↔ contains query trie = true) →
      ∀ query,
        query ∈ (collectUniqueKeys keys trie acc).2 ↔
          query ∈ keys ∨ query ∈ acc := by
  induction keys with
  | nil =>
      intro trie acc hinv query
      simp [collectUniqueKeys]
  | cons key rest ih =>
      intro trie acc hinv query
      by_cases hkey : contains key trie = true
      · have hmem : key ∈ acc := (hinv key).mpr hkey
        simp only [collectUniqueKeys, hkey, ite_true]
        rw [ih trie acc hinv query]
        simp only [List.mem_cons]
        constructor
        · intro h
          rcases h with h | h
          · exact Or.inl (Or.inr h)
          · exact Or.inr h
        · intro h
          rcases h with h | h
          · rcases h with h | h
            · exact Or.inr (by simpa [h] using hmem)
            · exact Or.inl h
          · exact Or.inr h
      · have hinv' :
            ∀ query,
              query ∈ key :: acc ↔
                contains query (insertCount key trie).1 = true := by
          intro q
          rw [contains_insertCount_iff]
          constructor
          · intro hm
            rcases List.mem_cons.mp hm with h | h
            · exact Or.inl h
            · exact Or.inr ((hinv q).mp h)
          · intro hm
            rcases hm with h | h
            · exact List.mem_cons.mpr (Or.inl h)
            · exact List.mem_cons.mpr (Or.inr ((hinv q).mpr h))
        simp only [collectUniqueKeys, hkey, ite_false]
        rw [ih (insertCount key trie).1 (key :: acc) hinv' query]
        simp only [List.mem_cons]
        tauto

/-- Actual implementation for duplicate-free bit keys. -/
def dedupTrieKeys (keys : List (List Bool)) : List (List Bool) :=
  (collectUniqueKeys keys empty []).2.reverse

/-- No key is lost or manufactured by actual counted-trie insertion. -/
theorem mem_dedupTrieKeys_iff
    (keys : List (List Bool)) (query : List Bool) :
    query ∈ dedupTrieKeys keys ↔ query ∈ keys := by
  have hinv :
      ∀ q, q ∈ ([] : List (List Bool)) ↔ contains q empty = true := by
    intro q
    simp [contains_empty_eq_false]
  have h := collectUniqueKeys_mem keys empty [] hinv query
  simpa [dedupTrieKeys] using h

#print axioms TCSPhase8.BitTrie.collectUniqueKeys_mem
#print axioms TCSPhase8.BitTrie.mem_dedupTrieKeys_iff
end TCSPhase8.BitTrie
