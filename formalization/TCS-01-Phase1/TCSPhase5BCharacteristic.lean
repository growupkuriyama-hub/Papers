import TCSPhase5BCompleteness

/-! Exact finite reconstruction, and Phase 1's original Characteristic
predicate witnessed by an explicitly constructed Finset. -/
namespace TCSPhase5B
open TCSPhase5
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

theorem rec_exact_reconstruction
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (K : Finset (List Alphabet))
    (hSub : TypedSubstitutable h (GrammarLanguage G))
    (hW : PositiveWitnesses G h ⊆ K)
    (hKL : (↑K : Set (List Alphabet)) ⊆ GrammarLanguage G) :
    RecLanguage h K = GrammarLanguage G := by
  apply Set.Subset.antisymm
  · exact rec_soundness h K (GrammarLanguage G) hKL hSub
  · exact rec_complete_from_positive_witnesses G h K hW

/-- Full original set-driven characteristic-sample predicate, with
the positive witness set constructed as a literal finite Finset. -/
theorem canonical_witnesses_characteristic
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (hSub : TypedSubstitutable h (GrammarLanguage G)) :
    TCSPhase1.Characteristic (RecLanguage h)
      (GrammarLanguage G) (PositiveWitnesses G h) := by
  constructor
  · exact positive_witnesses_subset_language G h
  · intro K hW hKL
    exact rec_exact_reconstruction G h K hSub hW hKL

/-- Witness existence for this specific real reconstruction operator,
rather than a conditional assumption about an abstract learner. -/
theorem rec_characteristic_sample_exists
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (hSub : TypedSubstitutable h (GrammarLanguage G)) :
    ∃ W : Finset (List Alphabet),
      TCSPhase1.Characteristic (RecLanguage h) (GrammarLanguage G) W :=
  ⟨PositiveWitnesses G h,canonical_witnesses_characteristic G h hSub⟩

#print axioms TCSPhase5B.rec_exact_reconstruction
#print axioms TCSPhase5B.canonical_witnesses_characteristic
#print axioms TCSPhase5B.rec_characteristic_sample_exists
end TCSPhase5B
