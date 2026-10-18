import TCSPhase8TrieExtraction
import TCSPhase8TrieUniqueness

/-!
The concrete trie key stream has unique bit keys. Every key in that
stream was made by encodeRecItem, so checked decoding can be proved
to return an equally duplicate-free list of actual grammar items.
-/
namespace TCSPhase8

theorem encode_filterMap_decode_encoded
    {Alphabet : Type*}
    (c : LetterNumbering Alphabet) :
    ∀ keys : List (List Bool),
      (∀ key ∈ keys, ∃ r : RecItem Alphabet, encodeRecItem c r = key) →
      ((keys.filterMap (decodeRecItem c)).map (encodeRecItem c)) = keys := by
  intro keys
  induction keys with
  | nil =>
      intro _
      rfl
  | cons key rest ih =>
      intro hv
      obtain ⟨r, heq⟩ := hv key (by simp)
      have ht : ∀ k ∈ rest,
          ∃ r : RecItem Alphabet, encodeRecItem c r = k := by
        intro k hk
        exact hv k (by simp [hk])
      subst key
      simp [decodeRecItem_encodeRecItem, ih ht]

/-- Re-encoding the actual decoded unique-item output returns exactly
the stored distinct-key stream. -/
theorem dedupRecItems_encoded_keys {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) :
    (dedupRecItems c t sample).map (encodeRecItem c) =
      BitTrie.dedupTrieKeys
        ((emitAllRecItems t sample).map (encodeRecItem c)) := by
  unfold dedupRecItems
  apply encode_filterMap_decode_encoded
  intro key hk
  have hmem :
      key ∈ (emitAllRecItems t sample).map (encodeRecItem c) :=
    (BitTrie.mem_dedupTrieKeys_iff _ key).mp hk
  obtain ⟨r,_,heq⟩ := List.mem_map.mp hmem
  exact ⟨r,heq⟩

/-- A map cannot acquire duplicates unless its underlying list already
contains duplicates; the converse requires no injectivity hypothesis. -/
theorem list_nodup_of_nodup_map {α β : Type*}
    (f : α → β) :
    ∀ xs : List α, (xs.map f).Nodup → xs.Nodup := by
  intro xs
  induction xs with
  | nil => intro _; simp
  | cons a rest ih =>
      intro hn
      have hp := List.nodup_cons.mp hn
      have hnot : a ∉ rest := by
        intro ha
        exact hp.1 (List.mem_map.mpr ⟨a,ha,rfl⟩)
      exact List.nodup_cons.mpr ⟨hnot, ih hp.2⟩

/-- No actual decoded grammar item is emitted twice by the operational
trie extraction function. -/
theorem dedupRecItems_nodup {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) :
    (dedupRecItems c t sample).Nodup := by
  have hk := BitTrie.dedupTrieKeys_nodup
    ((emitAllRecItems t sample).map (encodeRecItem c))
  rw [← dedupRecItems_encoded_keys c t sample] at hk
  exact list_nodup_of_nodup_map (encodeRecItem c) _ hk

#print axioms TCSPhase8.dedupRecItems_encoded_keys
#print axioms TCSPhase8.dedupRecItems_nodup
end TCSPhase8
