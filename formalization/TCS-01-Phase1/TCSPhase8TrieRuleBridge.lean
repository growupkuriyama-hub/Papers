import TCSPhase8TrieSemantics

/-!
# Key-level bridge from a candidate List to the counted trie
The injectivity hypothesis is a separate obligation for the complete
grammar production encoder; it is not manufactured here.
-/
namespace TCSPhase8.BitTrie

theorem contains_encoded_list_iff {Rule : Type*}
    (encode : Rule → List Bool) (he : Function.Injective encode)
    (rules : List Rule) (r : Rule) :
    contains (encode r) (insertManyCount (rules.map encode) empty).1 = true ↔
      r ∈ rules := by
  rw [contains_insertMany_empty_iff]
  constructor
  · intro h
    obtain ⟨s, hs, heq⟩ := List.mem_map.mp h
    have hsr : s = r := he heq
    simpa [hsr] using hs
  · intro hr
    exact List.mem_map.mpr ⟨r, hr, rfl⟩

theorem encoded_list_steps {Rule : Type*}
    (encode : Rule → List Bool) (rules : List Rule) :
    (insertManyCount (rules.map encode) empty).2 =
      (rules.map (fun r => (encode r).length + 1)).sum := by
  rw [insertManyCount_steps]
  simp only [List.map_map, Function.comp_def]

#print axioms TCSPhase8.BitTrie.contains_encoded_list_iff
#print axioms TCSPhase8.BitTrie.encoded_list_steps
end TCSPhase8.BitTrie
