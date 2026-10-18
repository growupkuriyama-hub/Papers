import TCSPhase8TrieLookupCost
import TCSPhase8TrieUnique

/-!
Count both actual searches and conditional insertions while preserving
the original trie and reverse accumulator. The counter is returned by
the same recursion that computes the result, not by a separate estimate.
-/
namespace TCSPhase8.BitTrie

/-- The first projection is the real collector result; the second
projection adds actual lookup visits and performed insertion visits. -/
def collectUniqueKeysCount :
    List (List Bool) → BitTrie → List (List Bool) →
      (BitTrie × List (List Bool)) × Nat
  | [], trie, acc => ((trie, acc), 0)
  | key :: rest, trie, acc =>
      let lookup := containsCount key trie
      if lookup.1 then
        let later := collectUniqueKeysCount rest trie acc
        (later.1, lookup.2 + later.2)
      else
        let inserted := insertCount key trie
        let later := collectUniqueKeysCount rest inserted.1 (key :: acc)
        (later.1, lookup.2 + inserted.2 + later.2)

/-- The counted traversal computes exactly the uninstrumented collector. -/
theorem collectUniqueKeysCount_correct (keys : List (List Bool)) :
    ∀ trie acc,
      (collectUniqueKeysCount keys trie acc).1 =
        collectUniqueKeys keys trie acc := by
  induction keys with
  | nil =>
      intro trie acc
      rfl
  | cons key rest ih =>
      intro trie acc
      cases h : contains key trie with
      | false =>
          have hh : (containsCount key trie).1 = false := by
            rw [containsCount_correct]
            exact h
          simp [collectUniqueKeysCount, collectUniqueKeys, h, hh,
            ih (insertCount key trie).1 (key :: acc)]
      | true =>
          have hh : (containsCount key trie).1 = true := by
            rw [containsCount_correct]
            exact h
          simp [collectUniqueKeysCount, collectUniqueKeys, h, hh, ih trie acc]

/-- Search plus insertion work is charged to each input key at most
twice, regardless of the trie shape and the input's duplicates. -/
theorem collectUniqueKeysCount_cost_le_twice
    (keys : List (List Bool)) :
    ∀ trie acc,
      (collectUniqueKeysCount keys trie acc).2 ≤
        2 * (keys.map (fun k => k.length + 1)).sum := by
  induction keys with
  | nil =>
      intro trie acc
      simp [collectUniqueKeysCount]
  | cons key rest ih =>
      intro trie acc
      have hlook := containsCount_steps_le key trie
      cases hc : (containsCount key trie).1 with
      | true =>
          have ht := ih trie acc
          calc
            (collectUniqueKeysCount (key :: rest) trie acc).2 =
                (containsCount key trie).2 +
                  (collectUniqueKeysCount rest trie acc).2 := by
                    simp [collectUniqueKeysCount, hc]
            _ ≤ (key.length + 1) +
                2 * (rest.map (fun k => k.length + 1)).sum := by omega
            _ ≤ 2 * ((key :: rest).map
                (fun k => k.length + 1)).sum := by
                  simp [List.map_cons, List.sum_cons] <;> omega
      | false =>
          have ht := ih (insertCount key trie).1 (key :: acc)
          have hi := insertCount_steps key trie
          calc
            (collectUniqueKeysCount (key :: rest) trie acc).2 =
                (containsCount key trie).2 +
                  (insertCount key trie).2 +
                  (collectUniqueKeysCount rest
                    (insertCount key trie).1 (key :: acc)).2 := by
                      simp [collectUniqueKeysCount, hc]
            _ ≤ (key.length + 1) + (key.length + 1) +
                2 * (rest.map (fun k => k.length + 1)).sum := by omega
            _ = 2 * ((key :: rest).map
                (fun k => k.length + 1)).sum := by
                  simp [List.map_cons, List.sum_cons] <;> omega

/-- Reverse the accumulator once, exactly as in the original deduplicator. -/
def dedupTrieKeysCount (keys : List (List Bool)) :
    List (List Bool) × Nat :=
  let result := collectUniqueKeysCount keys empty []
  (result.1.2.reverse, result.2)

theorem dedupTrieKeysCount_correct (keys : List (List Bool)) :
    (dedupTrieKeysCount keys).1 = dedupTrieKeys keys := by
  change (collectUniqueKeysCount keys empty []).1.2.reverse =
    (collectUniqueKeys keys empty []).2.reverse
  rw [collectUniqueKeysCount_correct]

theorem dedupTrieKeysCount_cost_le_twice (keys : List (List Bool)) :
    (dedupTrieKeysCount keys).2 ≤
      2 * (keys.map (fun k => k.length + 1)).sum := by
  change (collectUniqueKeysCount keys empty []).2 ≤ _
  exact collectUniqueKeysCount_cost_le_twice keys empty []

/-- Reuse the earlier output uniqueness theorem by exact result equality. -/
theorem dedupTrieKeysCount_nodup (keys : List (List Bool)) :
    (dedupTrieKeysCount keys).1.Nodup := by
  rw [dedupTrieKeysCount_correct]
  exact dedupTrieKeys_nodup keys

/-- No key disappears and no new key is manufactured. -/
theorem mem_dedupTrieKeysCount_iff
    (keys : List (List Bool)) (query : List Bool) :
    query ∈ (dedupTrieKeysCount keys).1 ↔ query ∈ keys := by
  rw [dedupTrieKeysCount_correct]
  exact mem_dedupTrieKeys_iff keys query

#print axioms TCSPhase8.BitTrie.collectUniqueKeysCount_correct
#print axioms TCSPhase8.BitTrie.collectUniqueKeysCount_cost_le_twice
#print axioms TCSPhase8.BitTrie.dedupTrieKeysCount_correct
#print axioms TCSPhase8.BitTrie.dedupTrieKeysCount_cost_le_twice
#print axioms TCSPhase8.BitTrie.dedupTrieKeysCount_nodup
end TCSPhase8.BitTrie
