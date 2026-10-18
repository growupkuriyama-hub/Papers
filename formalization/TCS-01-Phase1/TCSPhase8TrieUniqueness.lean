import TCSPhase8TrieUnique

/-!
# No duplicated encoded keys in the concrete trie-based stream

The original collector is retained verbatim. This proof establishes
a genuine List.Nodup postcondition, not merely equality of finite sets.
-/
namespace TCSPhase8.BitTrie

theorem collectUniqueKeys_nodup (keys : List (List Bool)) :
    ∀ trie acc,
      (∀ q, q ∈ acc ↔ contains q trie = true) →
      acc.Nodup →
      (collectUniqueKeys keys trie acc).2.Nodup := by
  induction keys with
  | nil =>
      intro trie acc hinv hn
      simpa [collectUniqueKeys] using hn
  | cons key rest ih =>
      intro trie acc hinv hn
      by_cases hkey : contains key trie = true
      · simpa [collectUniqueKeys, hkey] using
          (ih trie acc hinv hn)
      · have hfalse : contains key trie = false := by
          cases hc : contains key trie <;> simp_all
        have hnot : key ∉ acc := by
          intro hm
          exact hkey ((hinv key).mp hm)
        have hinv' :
            ∀ q, q ∈ key :: acc ↔
              contains q (insertCount key trie).1 = true := by
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
        have hn' : (key :: acc).Nodup :=
          List.nodup_cons.mpr ⟨hnot,hn⟩
        simpa [collectUniqueKeys, hfalse] using
          (ih (insertCount key trie).1 (key :: acc) hinv' hn')

/-- The concrete trie-controlled duplicate elimination yields a List
with no repeated bitstrings, preserving its original encounter order. -/
theorem dedupTrieKeys_nodup (keys : List (List Bool)) :
    (dedupTrieKeys keys).Nodup := by
  have hinv :
      ∀ q, q ∈ ([] : List (List Bool)) ↔ contains q empty = true := by
    intro q
    simp [contains_empty_eq_false]
  have hn := collectUniqueKeys_nodup keys empty [] hinv (by simp)
  change (collectUniqueKeys keys empty []).2.reverse.Nodup
  exact List.nodup_reverse.mpr hn

#print axioms TCSPhase8.BitTrie.collectUniqueKeys_nodup
#print axioms TCSPhase8.BitTrie.dedupTrieKeys_nodup
end TCSPhase8.BitTrie
