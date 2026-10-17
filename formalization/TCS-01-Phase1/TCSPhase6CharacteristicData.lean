import TCSPhase6EncodedSize
import TCSPhase5BCharacteristic

/-! Quantitative characteristic sample: all hypotheses except the explicitly
identified context-compression lemma have been discharged. -/
namespace TCSPhase6
open TCSPhase5B
open TCSPhase5
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

theorem quantitative_characteristic_sample_of_context_bound
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (hSub : TypedSubstitutable h (GrammarLanguage G))
    (hctx : ContextCompressionBound G h) :
    ∃ W : Finset (List Alphabet),
      W = PositiveWitnesses G h ∧
      TCSPhase1.Characteristic (RecLanguage h) (GrammarLanguage G) W ∧
      encodedSize W ≤
        (Fintype.card NT * Fintype.card M +
          G.terminalRules.card +
          G.binaryRules.card * Fintype.card M ^ 2 + 1) *
        ((Fintype.card NT * Fintype.card M + 1) *
          typedThickness G h + 1) := by
  refine ⟨PositiveWitnesses G h, rfl, ?_, ?_⟩
  · exact canonical_witnesses_characteristic G h hSub
  · exact encoded_size_le_of_context_bound G h hctx

#print axioms TCSPhase6.quantitative_characteristic_sample_of_context_bound
end TCSPhase6
