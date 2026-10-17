import TCSPhase6Thickness
import TCSPhase5BWitnesses

/-! Phase 6: rule counts are proved by explicit images of the original
finite rule sets, never by assuming distinct witness words. -/
namespace TCSPhase6
open TCSPhase5B
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

theorem typed_symbols_card_le (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) :
    (finiteTypedRefinement G h).symbols.card ≤
      Fintype.card NT * Fintype.card M := by
  classical
  calc
    (finiteTypedRefinement G h).symbols.card ≤
        (Finset.univ : Finset (NT × M)).card :=
      Finset.card_le_card (Finset.subset_univ _)
    _ = Fintype.card NT * Fintype.card M := by simp [Fintype.card_prod]

theorem typed_terminal_card_le (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) :
    (finiteTypedRefinement G h).terminalRules.card ≤
      G.terminalRules.card := by
  classical
  let lift : NT × Alphabet → (NT × M) × Alphabet :=
    fun p => ((p.1, h [p.2]), p.2)
  have hs : (finiteTypedRefinement G h).terminalRules ⊆
      G.terminalRules.image lift := by
    intro p hp
    rcases p with ⟨⟨A, μ⟩, a⟩
    obtain ⟨hr, he, _⟩ := (finite_terminal_iff G h A μ a).mp hp
    subst μ
    exact Finset.mem_image.mpr ⟨(A,a),hr,rfl⟩
  exact (Finset.card_le_card hs).trans (Finset.card_image_le)

theorem typed_binary_card_le (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) :
    (finiteTypedRefinement G h).binaryRules.card ≤
      G.binaryRules.card * Fintype.card M ^ 2 := by
  classical
  let source := G.binaryRules.product
    ((Finset.univ : Finset M).product (Finset.univ : Finset M))
  let lift : (NT × NT × NT) × (M × M) →
      (NT × M) × (NT × M) × (NT × M) :=
    fun p => ((p.1.1, p.2.1 * p.2.2),
      (p.1.2.1, p.2.1), (p.1.2.2, p.2.2))
  have hs : (finiteTypedRefinement G h).binaryRules ⊆
      source.image lift := by
    intro p hp
    rcases p with ⟨⟨A, μ⟩, ⟨B, ν⟩, ⟨C, ρ⟩⟩
    obtain ⟨hr, he, _, _, _⟩ :=
      (finite_binary_iff G h A B C μ ν ρ).mp hp
    subst μ
    apply Finset.mem_image.mpr
    refine ⟨((A,B,C),(ν,ρ)), ?_, rfl⟩
    simp [source,hr]
  calc
    (finiteTypedRefinement G h).binaryRules.card ≤
        (source.image lift).card := Finset.card_le_card hs
    _ ≤ source.card := Finset.card_image_le
    _ = G.binaryRules.card * Fintype.card M ^ 2 := by
       simp [source, Finset.card_product, pow_two, mul_assoc]

theorem typed_empty_card_le (G : SSBNFGrammar Alphabet NT) :
    (WitnessEmpty (M := M) G).card ≤ 1 := by
  unfold WitnessEmpty
  split <;> simp

theorem positive_witnesses_card_le (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) :
    (PositiveWitnesses G h).card ≤
      Fintype.card NT * Fintype.card M + G.terminalRules.card +
      G.binaryRules.card * Fintype.card M ^ 2 + 1 := by
  classical
  have hsym : (WitnessSymbols G h).card ≤
      (finiteTypedRefinement G h).symbols.card :=
    Finset.card_image_le
  have hter : (WitnessLexical G h).card ≤
      (finiteTypedRefinement G h).terminalRules.card :=
    Finset.card_image_le
  have hbin : (WitnessBinary G h).card ≤
      (finiteTypedRefinement G h).binaryRules.card :=
    Finset.card_image_le
  have hu1 : (WitnessSymbols G h ∪ WitnessLexical G h).card ≤
      (WitnessSymbols G h).card + (WitnessLexical G h).card :=
    Finset.card_union_le _ _
  have hu2 :
      (WitnessSymbols G h ∪ WitnessLexical G h ∪ WitnessBinary G h).card ≤
      (WitnessSymbols G h ∪ WitnessLexical G h).card +
        (WitnessBinary G h).card :=
    Finset.card_union_le _ _
  have hu3 :
      (PositiveWitnesses G h).card ≤
      (WitnessSymbols G h ∪ WitnessLexical G h ∪ WitnessBinary G h).card +
        (WitnessEmpty G).card := by
    unfold PositiveWitnesses
    exact Finset.card_union_le _ _
  have he := typed_empty_card_le (M := M) G
  have hn := typed_symbols_card_le G h
  have ht := typed_terminal_card_le G h
  have hb := typed_binary_card_le G h
  omega

#print axioms TCSPhase6.typed_symbols_card_le
#print axioms TCSPhase6.typed_terminal_card_le
#print axioms TCSPhase6.typed_binary_card_le
#print axioms TCSPhase6.positive_witnesses_card_le
end TCSPhase6
