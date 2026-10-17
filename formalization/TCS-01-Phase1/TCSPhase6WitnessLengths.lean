import TCSPhase6RuleCounts
import TCSPhase6Contexts

/-! The four literal witness families, with bounds reduced to the
separate (not assumed by the final theorem) context-compression task. -/
namespace TCSPhase6
open TCSPhase5B
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

/-- This is a *bridge premise*, not an established Phase-6 result.
The full project must derive it from typed dependency paths. -/
def ContextCompressionBound (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) : Prop :=
  ∀ (A : NT) (μ : M), RetainedTypedSymbol G h A μ →
    (chosenContext G h A μ).1.length +
      (chosenContext G h A μ).2.length ≤
      ((finiteTypedRefinement G h).symbols.card - 1) * typedThickness G h

theorem retained_card_pos (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M)
    (A : NT) (μ : M) (hr : RetainedTypedSymbol G h A μ) :
    1 ≤ (finiteTypedRefinement G h).symbols.card := by
  classical
  have hm : (A, μ) ∈ (finiteTypedRefinement G h).symbols :=
    (finite_symbols_iff G h A μ).mpr hr
  have hp : 0 < (finiteTypedRefinement G h).symbols.card :=
    Finset.card_pos.mpr ⟨(A,μ),hm⟩
  omega

private theorem arithmetic_length_bound (n τ k : Nat)
    (hn : 1 ≤ n) (hk : k ≤ 2) :
    (n-1) * τ + k * τ ≤ (n+1) * τ := by
  have h : n-1+k ≤ n+1 := by omega
  calc
    (n-1)*τ + k*τ = (n-1+k)*τ := (add_mul ..).symm
    _ ≤ (n+1)*τ := Nat.mul_le_mul_right τ h

theorem witness_word_length_le_of_context_bound
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (hctx : ContextCompressionBound G h) :
    ∀ w ∈ PositiveWitnesses G h,
      w.length ≤ ((finiteTypedRefinement G h).symbols.card + 1) *
        typedThickness G h := by
  classical
  intro w hw
  let n := (finiteTypedRefinement G h).symbols.card
  let τ := typedThickness G h
  have hbase (A : NT) (μ : M)
      (hr : RetainedTypedSymbol G h A μ) :
      (chosenContext G h A μ).1.length +
        (chosenContext G h A μ).2.length ≤ (n-1)*τ :=
    hctx A μ hr
  have hn (A : NT) (μ : M) (hr : RetainedTypedSymbol G h A μ) :
      1 ≤ n := retained_card_pos G h A μ hr
  have hy (A : NT) (μ : M) (hr : RetainedTypedSymbol G h A μ) :
      (chosenYield G h A μ).length ≤ τ :=
    chosenYield_length_le_typedThickness G h A μ hr
  have ht : 1 ≤ τ := one_le_typedThickness G h
  unfold PositiveWitnesses at hw
  rcases Finset.mem_union.mp hw with h123 | he
  · rcases Finset.mem_union.mp h123 with h12 | hb
    · rcases Finset.mem_union.mp h12 with hs | hl
      · obtain ⟨p,hp,rfl⟩ := Finset.mem_image.mp hs
        rcases p with ⟨A,μ⟩
        have hr := (finite_symbols_iff G h A μ).mp hp
        have hupper := arithmetic_length_bound n τ 1 (hn A μ hr) (by omega)
        have hcx := hbase A μ hr
        have hyl := hy A μ hr
        simp only [wrapYield, List.length_append]
        omega
      · obtain ⟨p,hp,rfl⟩ := Finset.mem_image.mp hl
        rcases p with ⟨⟨A,μ⟩,a⟩
        obtain ⟨_,_,hr⟩ := (finite_terminal_iff G h A μ a).mp hp
        have hupper := arithmetic_length_bound n τ 1 (hn A μ hr) (by omega)
        have hcx := hbase A μ hr
        simp only [wrapYield, List.length_append, List.length_cons, List.length_nil]
        omega
    · obtain ⟨p,hp,rfl⟩ := Finset.mem_image.mp hb
      rcases p with ⟨⟨A,μ⟩,⟨B,ν⟩,⟨C,ρ⟩⟩
      obtain ⟨_,_,hrA,hrB,hrC⟩ :=
        (finite_binary_iff G h A B C μ ν ρ).mp hp
      have hupper := arithmetic_length_bound n τ 2 (hn A μ hrA) (by omega)
      have hcx := hbase A μ hrA
      have hyl := hy B ν hrB
      have hyr := hy C ρ hrC
      simp only [wrapYield, List.length_append]
      omega
  · unfold WitnessEmpty at he
    split at he
    · have hw0 : w = [] := by simpa using he
      subst w
      simp
    · simp at he

#print axioms TCSPhase6.witness_word_length_le_of_context_bound
end TCSPhase6
