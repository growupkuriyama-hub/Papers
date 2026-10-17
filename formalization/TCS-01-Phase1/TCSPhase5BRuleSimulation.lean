import TCSPhase5BWitnesses

/-! From two actual positive witness words in the *same terminal
context*, construct a real single-step direct unary rule of Rec_h.
Neither U rule nor sample-substitutability is assumed. -/
namespace TCSPhase5B
open TCSPhase5
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

private theorem observed_in_context (K : Finset (List Alphabet))
    (u x v : List Alphabet)
    (hne : x ≠ []) (hmem : u ++ x ++ v ∈ K) :
    ObservedFactor K x := ⟨hne,u,v,hmem⟩

/-- A type-correct, witnessed (U) switch, using exactly a common
sample context and not the substitutability relation of the target. -/
theorem witness_unary (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (K : Finset (List Alphabet))
    (A : NT) (μ : M) (y : List Alphabet)
    (ret : RetainedTypedSymbol G h A μ)
    (hy : y ≠ []) (htype : h y = μ)
    (hW : PositiveWitnesses G h ⊆ K)
    (hyw : wrapYield G h A μ y ∈ PositiveWitnesses G h) :
    DirectSimilar h K (chosenYield G h A μ) y ∧
    ObservedFactor K (chosenYield G h A μ) ∧
    ObservedFactor K y := by
  have hxmem := hW (symbol_witness_mem G h A μ ret)
  have hymem := hW hyw
  have hx := observed_in_context K _ _ _
    (chosenYield_nonempty ret) hxmem
  have hyobs := observed_in_context K _ _ _ hy hymem
  have hsim : DirectSimilar h K (chosenYield G h A μ) y :=
    ⟨(chosenYield_type ret).trans htype.symm,
      ((chosenContext G h A μ).1,(chosenContext G h A μ).2),
       hxmem,hymem⟩
  exact ⟨hsim,hx,hyobs⟩

/-- Terminal-rule case of the paper's typed tree simulation. -/
theorem simulate_terminal (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (K : Finset (List Alphabet))
    (A : NT) (a : Alphabet)
    (rule : (A,a) ∈ G.terminalRules)
    (ret : RetainedTypedSymbol G h A (h [a]))
    (hW : PositiveWitnesses G h ⊆ K) :
    RecFactorDerives h K (chosenYield G h A (h [a])) [a] := by
  have hu := witness_unary G h K A (h [a]) [a] ret
    (by simp) rfl hW (lexical_witness_mem G h A a rule ret)
  exact RecFactorDerives.unary hu.2.1 hu.2.2 hu.1
    (RecFactorDerives.lexical hu.2.2)

/-- Binary-rule case, with both child's *actual* Rec_h derivations.
The witness makes the concatenation a nonempty observed factor. -/
theorem simulate_binary (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (K : Finset (List Alphabet))
    (A B C : NT) (μ ν : M)
    (rule : (A,B,C) ∈ G.binaryRules)
    (retA : RetainedTypedSymbol G h A (μ * ν))
    (retB : RetainedTypedSymbol G h B μ)
    (retC : RetainedTypedSymbol G h C ν)
    (hW : PositiveWitnesses G h ⊆ K)
    {wB wC : List Alphabet}
    (hb : RecFactorDerives h K (chosenYield G h B μ) wB)
    (hc : RecFactorDerives h K (chosenYield G h C ν) wC) :
    RecFactorDerives h K (chosenYield G h A (μ * ν))
      (wB ++ wC) := by
  let x := chosenYield G h B μ
  let y := chosenYield G h C ν
  have hxyne : x ++ y ≠ [] := by
    intro he
    exact (chosenYield_nonempty retB) (List.append_eq_nil_iff.mp he).1
  have htype : h (x ++ y) = μ * ν := by
    change h (x * y) = μ * ν
    rw [map_mul, chosenYield_type retB, chosenYield_type retC]
  have hbmem : wrapYield G h A (μ * ν) (x ++ y) ∈
       PositiveWitnesses G h :=
    binary_witness_mem G h A B C μ ν rule retA retB retC
  have hh := witness_unary G h K A (μ * ν) (x ++ y)
    retA hxyne htype hW hbmem
  have hxyobs : ObservedFactor K (x ++ y) := hh.2.2
  have hxobs : ObservedFactor K x :=
    observed_of_infix hxyobs (chosenYield_nonempty retB)
      ⟨[], y, by simp [x]⟩
  have hyobs : ObservedFactor K y :=
    observed_of_infix hxyobs (chosenYield_nonempty retC)
      ⟨x, [], by simp [y]⟩
  exact RecFactorDerives.unary hh.2.1 hxyobs hh.1
    (RecFactorDerives.binary hxobs hyobs hxyobs hb hc)

/-- The main non-start induction over real finite trimmed typed trees.
Its conclusion is the original Phase 5A grammar's B/U/L derivation. -/
theorem canonical_symbol_reconstructs
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (K : Finset (List Alphabet))
    (hW : PositiveWitnesses G h ⊆ K)
    {A : NT} {μ : M} {w : List Alphabet}
    (hd : TrimmedTypedDerives G h A μ w) :
    RecFactorDerives h K (chosenYield G h A μ) w := by
  induction hd with
  | terminal rule ret =>
      exact simulate_terminal G h K _ _ rule ret hW
  | binary rule ret hB hC ihB ihC =>
      have htB := trimmed_sound hB
      have htC := trimmed_sound hC
      obtain ⟨retB,retC⟩ :=
        retained_binary_children ret rule htB htC
      exact simulate_binary G h K _ _ _ _ _ rule
        ret retB retC hW ihB ihC

#print axioms TCSPhase5B.witness_unary
#print axioms TCSPhase5B.simulate_terminal
#print axioms TCSPhase5B.simulate_binary
#print axioms TCSPhase5B.canonical_symbol_reconstructs
end TCSPhase5B
