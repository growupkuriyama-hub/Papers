import TCSPhase6CharacteristicData
import TCSPhase6ContextCompression

/-! Quantitative typed characteristic-data theorem for arbitrary finite
monoids and the existing successful-tree trimmed typed refinement.
No shortlex tie-breaking claim is made about Phase 5B representatives. -/
namespace TCSPhase6
open TCSPhase5B
open TCSPhase5
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

theorem canonical_context_length_bound
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (A : NT) (μ : M) (hr : RetainedTypedSymbol G h A μ) :
    (chosenContext G h A μ).1.length +
      (chosenContext G h A μ).2.length ≤
        ((finiteTypedRefinement G h).symbols.card - 1) *
          typedThickness G h :=
  context_compression_bound G h A μ hr

theorem canonical_witness_length_bound
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (w : List Alphabet) (hw : w ∈ PositiveWitnesses G h) :
    w.length ≤ ((finiteTypedRefinement G h).symbols.card + 1) *
        typedThickness G h :=
  witness_word_length_le_of_context_bound G h
    (context_compression_bound G h) w hw

theorem canonical_witness_encoded_size_bound
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M) :
    encodedSize (PositiveWitnesses G h) ≤
      (Fintype.card NT * Fintype.card M +
        G.terminalRules.card +
        G.binaryRules.card * Fintype.card M ^ 2 + 1) *
      ((Fintype.card NT * Fintype.card M + 1) *
        typedThickness G h + 1) :=
  encoded_size_le_of_context_bound G h (context_compression_bound G h)

theorem polynomial_characteristic_data
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (hSub : TypedSubstitutable h (GrammarLanguage G)) :
    ∃ W : Finset (List Alphabet),
      W = PositiveWitnesses G h ∧
      TCSPhase1.Characteristic (RecLanguage h) (GrammarLanguage G) W ∧
      encodedSize W ≤
        (Fintype.card NT * Fintype.card M +
          G.terminalRules.card +
          G.binaryRules.card * Fintype.card M ^ 2 + 1) *
        ((Fintype.card NT * Fintype.card M + 1) *
          typedThickness G h + 1) :=
  quantitative_characteristic_sample_of_context_bound G h hSub
    (context_compression_bound G h)

#print axioms TCSPhase6.canonical_context_length_bound
#print axioms TCSPhase6.canonical_witness_length_bound
#print axioms TCSPhase6.canonical_witness_encoded_size_bound
#print axioms TCSPhase6.polynomial_characteristic_data
end TCSPhase6
