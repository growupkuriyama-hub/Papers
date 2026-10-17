import TCSPhase5BRuleSimulation

/-! The paper's completeness conclusion, with no K⊆L or substitutability
premise. The entire proof operates on genuine grammar derivation trees. -/
namespace TCSPhase5B
open TCSPhase5
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

theorem rec_complete_from_positive_witnesses
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (K : Finset (List Alphabet))
    (hW : PositiveWitnesses G h ⊆ K) :
    GrammarLanguage G ⊆ RecLanguage h K := by
  intro w hw
  change StartDerives G w at hw
  change RecStartDerives h K w
  cases hw with
  | empty he =>
      exact RecStartDerives.empty (hW (empty_witness_mem G h he))
  | @root A w hs hd =>
      have htyped : TypedDerives G h A (h w) w :=
        typed_complete hd
      have ret : RetainedTypedSymbol G h A (h w) :=
        retained_at_start hs htyped
      have hcontext := chosenContext_start_empty hs htyped
      have hstart :
          chosenYield G h A (h w) ∈ K := by
        have hwit := hW (symbol_witness_mem G h A (h w) ret)
        simpa [wrapYield, hcontext] using hwit
      exact RecStartDerives.root hstart (chosenYield_nonempty ret)
        (canonical_symbol_reconstructs G h K hW
          (trimmed_complete htyped ret))

#print axioms TCSPhase5B.rec_complete_from_positive_witnesses
end TCSPhase5B
