import TCSPhase8DedupCount
import TCSPhase8ActualItemLength
import TCSPhase8TrieExtractionUnique

/-!
The actual encoded reconstruction production stream is passed through
the instrumented search-plus-conditional-insertion trie program.
This only accounts for trie lookup and insertion node visits, not
candidate generation, serialization, or output processing.
-/
namespace TCSPhase8

/-- The real encoded six-field candidate stream, with its actual
search-and-insert execution and measured visit count. -/
def dedupActualKeysCount {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) : List (List Bool) × Nat :=
  BitTrie.dedupTrieKeysCount
    ((emitAllRecItems t sample).map (encodeRecItem c))

theorem dedupActualKeysCount_correct {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) :
    (dedupActualKeysCount c t sample).1 =
      BitTrie.dedupTrieKeys
        ((emitAllRecItems t sample).map (encodeRecItem c)) := by
  exact BitTrie.dedupTrieKeysCount_correct _

/-- Decoding the counted keys reproduces the existing operational
unique-rule output, without a new reconstruction or uniqueness proof. -/
theorem dedupActualKeysCount_decode_correct {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) :
    (dedupActualKeysCount c t sample).1.filterMap (decodeRecItem c) =
      dedupRecItems c t sample := by
  rw [dedupActualKeysCount_correct]
  rfl

theorem dedupActualKeysCount_nodup {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) :
    (dedupActualKeysCount c t sample).1.Nodup := by
  rw [dedupActualKeysCount_correct]
  exact BitTrie.dedupTrieKeys_nodup _

theorem mem_dedupActualKeysCount_iff {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) (key : List Bool) :
    key ∈ (dedupActualKeysCount c t sample).1 ↔
      key ∈ (emitAllRecItems t sample).map (encodeRecItem c) := by
  rw [dedupActualKeysCount_correct]
  exact BitTrie.mem_dedupTrieKeys_iff _ key

/-- Fourth-degree bound for search plus performed insertions in the
real trie-based deduplicator, as counted by its own execution. -/
theorem actual_dedup_lookup_insert_steps_fourth {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) :
    (dedupActualKeysCount c t sample).2 ≤
      (36 * tokenBound c + 6) * (encodedListSample sample + 1)^4 := by
  let keys := (emitAllRecItems t sample).map (encodeRecItem c)
  have hcount :
      (dedupActualKeysCount c t sample).2 ≤
        2 * (keys.map (fun k => k.length + 1)).sum := by
    exact BitTrie.dedupTrieKeysCount_cost_le_twice keys
  have hsum :
      (keys.map (fun k => k.length + 1)).sum =
        (buildItemTrie c t sample).2 := by
    simpa [keys, List.map_map, Function.comp_def] using
      (buildItemTrie_steps c t sample).symm
  calc
    (dedupActualKeysCount c t sample).2 ≤
        2 * (keys.map (fun k => k.length + 1)).sum := hcount
    _ = 2 * (buildItemTrie c t sample).2 := by rw [hsum]
    _ ≤ 2 * ((18 * tokenBound c + 3) *
          (encodedListSample sample + 1)^4) := by
      exact Nat.mul_le_mul_left 2
        (buildItemTrie_insertion_steps_fourth c t sample)
    _ = (36 * tokenBound c + 6) *
          (encodedListSample sample + 1)^4 := by ring

#print axioms TCSPhase8.dedupActualKeysCount_correct
#print axioms TCSPhase8.dedupActualKeysCount_decode_correct
#print axioms TCSPhase8.dedupActualKeysCount_nodup
#print axioms TCSPhase8.mem_dedupActualKeysCount_iff
#print axioms TCSPhase8.actual_dedup_lookup_insert_steps_fourth
end TCSPhase8
