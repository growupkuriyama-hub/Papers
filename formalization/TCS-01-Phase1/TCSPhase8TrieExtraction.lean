import TCSPhase8OperationalTrie
import TCSPhase8TrieUnique

/-!
Recover typed grammar items from the executable trie-driven unique-key
stream by the verified decoder of the *complete* rule serializer.
This step uses no Finset and does not invoke the Phase 5 specification.
-/
namespace TCSPhase8

def dedupRecItems {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) : List (RecItem Alphabet) :=
  (BitTrie.dedupTrieKeys
    ((emitAllRecItems t sample).map (encodeRecItem c))).filterMap
      (decodeRecItem c)

/-- Decoding the actual trie-backed unique-key stream preserves exactly
the set of tagged productions emitted by the six-field generator. -/
theorem mem_dedupRecItems_iff {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) (r : RecItem Alphabet) :
    r ∈ dedupRecItems c t sample ↔
      r ∈ emitAllRecItems t sample := by
  constructor
  · intro hm
    obtain ⟨key, hkey, hdec⟩ := List.mem_filterMap.mp hm
    have hcodes :
        key ∈ (emitAllRecItems t sample).map (encodeRecItem c) :=
      (BitTrie.mem_dedupTrieKeys_iff
        ((emitAllRecItems t sample).map (encodeRecItem c)) key).mp hkey
    obtain ⟨s, hs, hcode⟩ := List.mem_map.mp hcodes
    have heq : s = r := by
      have hsome : some s = some r := by
        calc
          some s = decodeRecItem c (encodeRecItem c s) :=
            (decodeRecItem_encodeRecItem c s).symm
          _ = decodeRecItem c key := by rw [hcode]
          _ = some r := hdec
      exact Option.some.inj hsome
    simpa [heq] using hs
  · intro hr
    apply List.mem_filterMap.mpr
    refine ⟨encodeRecItem c r, ?_, decodeRecItem_encodeRecItem c r⟩
    apply (BitTrie.mem_dedupTrieKeys_iff
      ((emitAllRecItems t sample).map (encodeRecItem c))
      (encodeRecItem c r)).mpr
    exact List.mem_map.mpr ⟨r, hr, rfl⟩

#print axioms TCSPhase8.mem_dedupRecItems_iff
end TCSPhase8
