import TCSPhase5BChoices

/-! Actual finite typed/retained SSBNF production sets for general h. -/
namespace TCSPhase5B
open TCSPhase5
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

abbrev TypedSymbol (NT M : Type*) := NT × M

structure TypedFiniteGrammar (Alphabet NT M : Type*) where
  symbols : Finset (TypedSymbol NT M)
  startRules : Finset (TypedSymbol NT M)
  startEmpty : Bool
  terminalRules : Finset (TypedSymbol NT M × Alphabet)
  binaryRules : Finset (TypedSymbol NT M × TypedSymbol NT M × TypedSymbol NT M)

/-- Literal finite rule sets, not a language-semantics abbreviation. -/
noncomputable def finiteTypedRefinement (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) : TypedFiniteGrammar Alphabet NT M := by
  classical
  exact {
    symbols := Finset.univ.filter
      (fun p : NT × M => RetainedTypedSymbol G h p.1 p.2)
    startRules := Finset.univ.filter
      (fun p : NT × M => p.1 ∈ G.startRules ∧
        RetainedTypedSymbol G h p.1 p.2)
    startEmpty := G.startEmpty
    terminalRules := Finset.univ.filter
      (fun p : (NT × M) × Alphabet =>
        (p.1.1,p.2) ∈ G.terminalRules ∧
        p.1.2 = h [p.2] ∧ RetainedTypedSymbol G h p.1.1 p.1.2)
    binaryRules := Finset.univ.filter
      (fun p : (NT × M) × (NT × M) × (NT × M) =>
        (p.1.1,p.2.1.1,p.2.2.1) ∈ G.binaryRules ∧
        p.1.2 = p.2.1.2 * p.2.2.2 ∧
        RetainedTypedSymbol G h p.1.1 p.1.2 ∧
        RetainedTypedSymbol G h p.2.1.1 p.2.1.2 ∧
        RetainedTypedSymbol G h p.2.2.1 p.2.2.2)
  }

theorem finite_symbols_iff (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (A : NT) (μ : M) :
    (A,μ) ∈ (finiteTypedRefinement G h).symbols ↔
      RetainedTypedSymbol G h A μ := by
  classical
  simp [finiteTypedRefinement]

theorem finite_start_iff (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (A : NT) (μ : M) :
    (A,μ) ∈ (finiteTypedRefinement G h).startRules ↔
      A ∈ G.startRules ∧ RetainedTypedSymbol G h A μ := by
  classical
  simp [finiteTypedRefinement]

theorem finite_terminal_iff (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (A : NT) (μ : M)
    (a : Alphabet) :
    ((A,μ),a) ∈ (finiteTypedRefinement G h).terminalRules ↔
      (A,a) ∈ G.terminalRules ∧ μ = h [a] ∧
      RetainedTypedSymbol G h A μ := by
  classical
  simp [finiteTypedRefinement]

theorem finite_binary_iff (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (A B C : NT) (μ ν ρ : M) :
    ((A,μ),(B,ν),(C,ρ)) ∈
      (finiteTypedRefinement G h).binaryRules ↔
      (A,B,C) ∈ G.binaryRules ∧ μ = ν * ρ ∧
      RetainedTypedSymbol G h A μ ∧
      RetainedTypedSymbol G h B ν ∧
      RetainedTypedSymbol G h C ρ := by
  classical
  simp [finiteTypedRefinement]

#print axioms TCSPhase5B.finite_symbols_iff
#print axioms TCSPhase5B.finite_start_iff
#print axioms TCSPhase5B.finite_terminal_iff
#print axioms TCSPhase5B.finite_binary_iff
end TCSPhase5B
