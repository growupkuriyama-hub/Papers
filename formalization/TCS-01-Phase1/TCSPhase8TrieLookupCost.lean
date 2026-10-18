import TCSPhase8TrieSemantics

/-!
Lookup instrumentation for the existing concrete bit trie. The counter
charges a visit at each examined trie node, including the terminal
position, and stops when the requested child does not exist.
-/
namespace TCSPhase8.BitTrie

/-- Run the existing search with a node-visit counter. -/
def containsCount : List Bool → BitTrie → Bool × Nat
  | [], .node accept _ _ => (accept, 1)
  | false :: rest, .node _ left _ =>
      match left with
      | none => (false, 1)
      | some child =>
          let result := containsCount rest child
          (result.1, result.2 + 1)
  | true :: rest, .node _ _ right =>
      match right with
      | none => (false, 1)
      | some child =>
          let result := containsCount rest child
          (result.1, result.2 + 1)

/-- Instrumentation preserves the Boolean result of the real lookup. -/
theorem containsCount_correct (key : List Bool) (trie : BitTrie) :
    (containsCount key trie).1 = contains key trie := by
  induction key generalizing trie with
  | nil =>
      cases trie
      rfl
  | cons bit rest ih =>
      cases trie with
      | node mark left right =>
          cases bit <;> cases left <;> cases right <;>
            simp [containsCount, contains, ih]

/-- Missing children allow early termination; every lookup visits at
most one node per key bit, plus the initial node. -/
theorem containsCount_steps_le (key : List Bool) (trie : BitTrie) :
    (containsCount key trie).2 ≤ key.length + 1 := by
  induction key generalizing trie with
  | nil =>
      cases trie
      simp [containsCount]
  | cons bit rest ih =>
      cases trie with
      | node mark left right =>
          cases bit <;> cases left <;> cases right <;>
            simp [containsCount, ih] <;> omega

#print axioms TCSPhase8.BitTrie.containsCount_correct
#print axioms TCSPhase8.BitTrie.containsCount_steps_le
end TCSPhase8.BitTrie
