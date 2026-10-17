import TCSPhase5BCharacteristic
import TCSPhase5BFiniteDerivation
import TCSPhase5FiniteDerivation

/-! Kernel dependency audit: generic typed grammar, productive typed nodes,
witness set, genuine U/B/L/S simulation, completeness and the
set-driven characteristic predicate of Phase 1. -/
#print axioms TCSPhase5B.typed_lifting
#print axioms TCSPhase5B.retained_productive
#print axioms TCSPhase5B.context_plug
#print axioms TCSPhase5B.trimmed_lifting
#print axioms TCSPhase5B.chosenYield_spec
#print axioms TCSPhase5B.chosenYield_type
#print axioms TCSPhase5B.chosenContext_spec
#print axioms TCSPhase5B.chosenContext_start_empty
#print axioms TCSPhase5B.finite_terminal_iff
#print axioms TCSPhase5B.finite_binary_iff
#print axioms TCSPhase5B.positive_witnesses_subset_language
#print axioms TCSPhase5B.witness_unary
#print axioms TCSPhase5B.simulate_terminal
#print axioms TCSPhase5B.simulate_binary
#print axioms TCSPhase5B.canonical_symbol_reconstructs
#print axioms TCSPhase5B.rec_complete_from_positive_witnesses
#print axioms TCSPhase5B.rec_exact_reconstruction
#print axioms TCSPhase5B.canonical_witnesses_characteristic
#print axioms TCSPhase5B.rec_characteristic_sample_exists
#print axioms TCSPhase5.finite_rec_language_iff

/-- Relate Phase 5B completeness directly to the *independent* derivations
from Phase 5A's real finite B/U/L/S production collections. -/
namespace TCSPhase5B
open TCSPhase5
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

theorem finite_rec_complete_from_positive_witnesses
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (K : Finset (List Alphabet))
    (hW : PositiveWitnesses G h ⊆ K) :
    GrammarLanguage G ⊆ {w | FiniteRecStartDerives h K w} := by
  intro w hw
  exact (finite_rec_language_iff h K w).mpr
    (rec_complete_from_positive_witnesses G h K hW hw)
end TCSPhase5B

#print axioms TCSPhase5B.finite_typed_sound
#print axioms TCSPhase5B.finite_typed_complete
#print axioms TCSPhase5B.finite_typed_iff
#print axioms TCSPhase5B.finite_typed_start_iff
#print axioms TCSPhase5B.finite_typed_grammar_language_eq
#print axioms TCSPhase5B.finite_rec_complete_from_positive_witnesses
