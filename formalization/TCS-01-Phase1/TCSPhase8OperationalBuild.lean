import TCSPhase8TrieExtraction
import TCSPhase8OperationalGrammar

/-!
# Operational six-field output from trie-backed unique bit keys

The actual executable path constructs List candidates, encodes each tagged
production, removes duplicate bit keys using the trie, decodes the result,
and projects it into the six concrete List fields. Finset conversion is
confined to the correctness statement.
-/
namespace TCSPhase8

/-- Separate the six production sorts without a mathematical Finset or
a call to the abstract reconstruction specification. -/
def projectRecItems {Alphabet : Type*}
    (items : List (RecItem Alphabet)) : ListedRecGrammar Alphabet := {
  nonterminals := items.filterMap (fun
    | .nonterminal w => some w
    | _ => none)
  binaryRules := items.filterMap (fun
    | .binary z x y => some (z,x,y)
    | _ => none)
  unaryRules := items.filterMap (fun
    | .unary x y => some (x,y)
    | _ => none)
  lexicalRules := items.filterMap (fun
    | .lexical a => some a
    | _ => none)
  startRules := items.filterMap (fun
    | .start w => some w
    | _ => none)
  startEmpty := items.any (fun
    | .startEmpty => true
    | _ => false)
}

/-- For any specific tagged-field projection, identical input membership
gives identical output sets, even if the input Lists have duplicates. -/
theorem filterMap_toFinset_eq_of_mem {α β : Type*}
    [DecidableEq β] (xs ys : List α) (f : α → Option β)
    (h : ∀ a, a ∈ xs ↔ a ∈ ys) :
    (xs.filterMap f).toFinset = (ys.filterMap f).toFinset := by
  ext b
  simp only [List.mem_toFinset]
  constructor
  · intro hb
    obtain ⟨a, ha, hf⟩ := List.mem_filterMap.mp hb
    exact List.mem_filterMap.mpr ⟨a, (h a).mp ha, hf⟩
  · intro hb
    obtain ⟨a, ha, hf⟩ := List.mem_filterMap.mp hb
    exact List.mem_filterMap.mpr ⟨a, (h a).mpr ha, hf⟩

/-- The sixth field can likewise be determined solely by tagged-item
membership. -/
theorem projectRecItems_startEmpty_iff {Alphabet : Type*}
    (xs : List (RecItem Alphabet)) :
    (projectRecItems xs).startEmpty = true ↔
      RecItem.startEmpty ∈ xs := by
  simp only [projectRecItems, List.any_eq_true]
  constructor
  · rintro ⟨r, hr, hp⟩
    cases r <;> simp at hp
    exact hr
  · intro hr
    exact ⟨RecItem.startEmpty, hr, rfl⟩

/-- All six mathematical output fields depend only on input membership. -/
theorem projectRecItems_spec_of_mem {Alphabet : Type*}
    [DecidableEq Alphabet]
    (xs ys : List (RecItem Alphabet))
    (h : ∀ r, r ∈ xs ↔ r ∈ ys) :
    (projectRecItems xs).asRecGrammar =
      (projectRecItems ys).asRecGrammar := by
  classical
  unfold projectRecItems ListedRecGrammar.asRecGrammar
  congr 1
  · exact filterMap_toFinset_eq_of_mem xs ys _ h
  · exact filterMap_toFinset_eq_of_mem xs ys _ h
  · exact filterMap_toFinset_eq_of_mem xs ys _ h
  · exact filterMap_toFinset_eq_of_mem xs ys _ h
  · exact filterMap_toFinset_eq_of_mem xs ys _ h
  · have heq :
        (projectRecItems xs).startEmpty = true ↔
          (projectRecItems ys).startEmpty = true :=
        (projectRecItems_startEmpty_iff xs).trans
          ((h RecItem.startEmpty).trans
            (projectRecItems_startEmpty_iff ys).symm)
    change (projectRecItems xs).startEmpty =
      (projectRecItems ys).startEmpty
    cases hx : (projectRecItems xs).startEmpty <;>
      cases hy : (projectRecItems ys).startEmpty <;>
      simp_all

/-- Eliminating an always-failing partial projection really returns
an empty list, independently of the element type. -/
theorem filterMap_none_elements {α β : Type*} (xs : List α) :
    xs.filterMap (fun _ => (none : Option β)) = [] := by
  induction xs with
  | nil => rfl
  | cons x tail ih => simp [ih]

/-- Splitting a grammar's own tagged item stream reconstructs all six
original fields (as sets), including the empty-start Boolean. -/
theorem projectRecItems_items_spec {Alphabet : Type*}
    [DecidableEq Alphabet] (g : ListedRecGrammar Alphabet) :
    (projectRecItems g.items).asRecGrammar = g.asRecGrammar := by
  classical
  cases g with
  | mk ns bs us ls ss eps =>
      cases eps <;>
        simp [projectRecItems, ListedRecGrammar.asRecGrammar,
          ListedRecGrammar.items, List.filterMap_append,
          List.filterMap_map, List.map_map, Function.comp_def,
          filterMap_none_elements]

/-- This is the executable path: no mathematical grammar specification
is used in any intermediate operation. -/
def reconstructOperational {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) : ListedRecGrammar Alphabet :=
  projectRecItems (dedupRecItems c t sample)

/-- Extensional equality of all six operational grammar fields with the
Phase 5 mathematical reconstruction, including empty-start. -/
theorem reconstructOperational_correct {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (h : List Alphabet →* M)
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (ht : ∀ a, t.letter a = h [a])
    (sample : List (List Alphabet)) :
    (reconstructOperational c t sample).asRecGrammar =
      TCSPhase5.makeRecGrammar h sample.toFinset := by
  calc
    _ = (projectRecItems (emitAllRecItems t sample)).asRecGrammar := by
      apply projectRecItems_spec_of_mem
      intro r
      exact mem_dedupRecItems_iff c t sample r
    _ = (buildListedRecGrammar t sample).asRecGrammar := by
      exact projectRecItems_items_spec (buildListedRecGrammar t sample)
    _ = TCSPhase5.makeRecGrammar h sample.toFinset :=
      buildListedRecGrammar_correct h t ht sample

#print axioms TCSPhase8.filterMap_toFinset_eq_of_mem
#print axioms TCSPhase8.projectRecItems_items_spec
#print axioms TCSPhase8.reconstructOperational_correct
end TCSPhase8
