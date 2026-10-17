import TCSPhase5BMain

/-! Phase 6: the intrinsic typed thickness of the *actual* finite typed
refinement. This parameter only measures minimum typed yields. -/
namespace TCSPhase6
open TCSPhase5B
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

/-- Maximum of 1 and all shortest typed-yield lengths of retained symbols. -/
noncomputable def typedThickness (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) : Nat :=
  (((finiteTypedRefinement G h).symbols.image
    (fun p => (chosenYield G h p.1 p.2).length)) ∪ {1}).sup id

theorem one_le_typedThickness (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) : 1 ≤ typedThickness G h := by
  classical
  unfold typedThickness
  exact Finset.le_sup (f := id) (Finset.mem_union.mpr (Or.inr (by simp)))

theorem chosenYield_length_le_typedThickness
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (A : NT) (μ : M) (hr : RetainedTypedSymbol G h A μ) :
    (chosenYield G h A μ).length ≤ typedThickness G h := by
  classical
  have hm : (chosenYield G h A μ).length ∈
      ((finiteTypedRefinement G h).symbols.image
        (fun p => (chosenYield G h p.1 p.2).length)) ∪ {1} := by
    apply Finset.mem_union.mpr
    left
    exact Finset.mem_image.mpr
      ⟨(A, μ), (finite_symbols_iff G h A μ).mpr hr, rfl⟩
  exact Finset.le_sup (f := id) hm

#print axioms TCSPhase6.one_le_typedThickness
#print axioms TCSPhase6.chosenYield_length_le_typedThickness
end TCSPhase6
