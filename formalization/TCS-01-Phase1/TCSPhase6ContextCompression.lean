import TCSPhase6DependencyPaths
import TCSPhase6WitnessLengths

/-! Phase 6: cost-descent compression of successful reaching contexts.
A canonical context of positive length has a productive parent of
strictly smaller canonical context cost. The predecessor never uses an
unproductive binary rule. -/
namespace TCSPhase6
open TCSPhase5B
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

noncomputable def contextCost (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (A : NT) (μ : M) : Nat :=
  (chosenContext G h A μ).1.length +
    (chosenContext G h A μ).2.length

noncomputable def contextRank (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (A : NT) (μ : M) : Nat :=
  ((finiteTypedRefinement G h).symbols.filter
    (fun p => contextCost G h p.1 p.2 < contextCost G h A μ)).card

/-- Productive predecessor of a positive-length minimum context.
This establishes a strict descent in the *actual* canonical context cost,
rather than postulating a path-length upper bound. -/
theorem context_predecessor
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (A : NT) (μ : M) (hr : RetainedTypedSymbol G h A μ)
    (hpos : 0 < contextCost G h A μ) :
    ∃ (B : NT) (ν : M), RetainedTypedSymbol G h B ν ∧
      contextCost G h B ν < contextCost G h A μ ∧
      contextCost G h A μ ≤
        contextCost G h B ν + typedThickness G h := by
  classical
  have hc := chosenContext_spec hr
  cases hc with
  | root hs hd =>
      have he := chosenContext_start_empty hs hd
      simp [contextCost, he] at hpos
  | @left P Q R α β u v wQ wR hparent rule hQ hR =>
      have hp : RetainedTypedSymbol G h P (α * β) :=
        ⟨u,v,hparent⟩
      obtain ⟨hq, hretR⟩ :=
        retained_binary_children hp rule hQ hR
      have hminP := chosenContext_is_shortest G h P (α*β) hp u v hparent
      have hposR : 0 < wR.length := by
        have hne := typed_nonempty hR
        cases wR with
        | nil => exact False.elim (hne rfl)
        | cons a as => simp
      have hcanon := chosenContext_spec hp
      have hcandidate : TypedContext G h Q α
          (chosenContext G h P (α*β)).1
          (chosenYield G h R β ++ (chosenContext G h P (α*β)).2) :=
        TypedContext.left hcanon rule
          (chosenYield_spec hq) (chosenYield_spec hretR)
      have hminQ := chosenContext_is_shortest G h Q α hq
        (chosenContext G h P (α*β)).1
        (chosenYield G h R β ++ (chosenContext G h P (α*β)).2)
        hcandidate
      have hlenR := chosenYield_length_le_typedThickness G h R β hretR
      refine ⟨P,α*β,hp,?_,?_⟩
      · dsimp [contextCost]
        simp only [List.length_append]
        omega
      · dsimp [contextCost] at *
        simp only [List.length_append] at *
        omega
  | @right P Q R α β u v wQ wR hparent rule hQ hR =>
      have hp : RetainedTypedSymbol G h P (α * β) :=
        ⟨u,v,hparent⟩
      obtain ⟨hretQ, hrR⟩ :=
        retained_binary_children hp rule hQ hR
      have hminP := chosenContext_is_shortest G h P (α*β) hp u v hparent
      have hposQ : 0 < wQ.length := by
        have hne := typed_nonempty hQ
        cases wQ with
        | nil => exact False.elim (hne rfl)
        | cons a as => simp
      have hcanon := chosenContext_spec hp
      have hcandidate : TypedContext G h R β
          ((chosenContext G h P (α*β)).1 ++ chosenYield G h Q α)
          (chosenContext G h P (α*β)).2 :=
        TypedContext.right hcanon rule
          (chosenYield_spec hretQ) (chosenYield_spec hrR)
      have hminR := chosenContext_is_shortest G h R β hrR
        ((chosenContext G h P (α*β)).1 ++ chosenYield G h Q α)
        (chosenContext G h P (α*β)).2 hcandidate
      have hlenQ := chosenYield_length_le_typedThickness G h Q α hretQ
      refine ⟨P,α*β,hp,?_,?_⟩
      · dsimp [contextCost]
        simp only [List.length_append]
        omega
      · dsimp [contextCost] at *
        simp only [List.length_append] at *
        omega

/-- Strictly smaller context cost implies strictly smaller finite rank
among *actually retained* typed symbols. -/
theorem contextRank_strict
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (A B : NT) (μ ν : M)
    (hrA : RetainedTypedSymbol G h A μ)
    (hlt : contextCost G h A μ < contextCost G h B ν) :
    contextRank G h A μ < contextRank G h B ν := by
  classical
  let s := (finiteTypedRefinement G h).symbols
  let lowerA := s.filter (fun p => contextCost G h p.1 p.2 < contextCost G h A μ)
  let lowerB := s.filter (fun p => contextCost G h p.1 p.2 < contextCost G h B ν)
  have hA : (A,μ) ∈ s := (finite_symbols_iff G h A μ).mpr hrA
  have hmem : (A,μ) ∈ lowerB := Finset.mem_filter.mpr ⟨hA,hlt⟩
  have hnot : (A,μ) ∉ lowerA := by
    simp [lowerA]
  have hsub : lowerA ⊆ lowerB := by
    intro p hp
    obtain ⟨hps,hltp⟩ := Finset.mem_filter.mp hp
    exact Finset.mem_filter.mpr ⟨hps,lt_trans hltp hlt⟩
  have hins : insert (A,μ) lowerA ⊆ lowerB := by
    intro p hp
    rcases Finset.mem_insert.mp hp with he | he
    · subst p; exact hmem
    · exact hsub he
  have hcard := Finset.card_le_card hins
  rw [Finset.card_insert_of_not_mem hnot] at hcard
  change lowerA.card < lowerB.card
  omega

theorem contextRank_lt_card
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (A : NT) (μ : M) (hr : RetainedTypedSymbol G h A μ) :
    contextRank G h A μ < (finiteTypedRefinement G h).symbols.card := by
  classical
  let s := (finiteTypedRefinement G h).symbols
  let lower := s.filter (fun p => contextCost G h p.1 p.2 < contextCost G h A μ)
  have hmem : (A,μ) ∈ s := (finite_symbols_iff G h A μ).mpr hr
  have hnot : (A,μ) ∉ lower := by simp [lower]
  have hins : insert (A,μ) lower ⊆ s := by
    intro p hp
    rcases Finset.mem_insert.mp hp with he | he
    · subst p; exact hmem
    · exact (Finset.mem_filter.mp he).1
  have hcard := Finset.card_le_card hins
  rw [Finset.card_insert_of_not_mem hnot] at hcard
  change lower.card < s.card
  omega

/-- Every decreasing predecessor chain has at most one representative
per retained typed symbol. The rank proof avoids any arbitrary graph
diameter assumption or unproved cycle-removal premise. -/
theorem context_cost_le_rank_times_thickness
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M) :
    ∀ (A : NT) (μ : M), RetainedTypedSymbol G h A μ →
      contextCost G h A μ ≤
        contextRank G h A μ * typedThickness G h := by
  classical
  have key : ∀ n : Nat, ∀ (A : NT) (μ : M),
      RetainedTypedSymbol G h A μ →
      contextCost G h A μ = n →
      contextCost G h A μ ≤
        contextRank G h A μ * typedThickness G h := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro A μ hr he
      by_cases hz : contextCost G h A μ = 0
      · omega
      · have hp : 0 < contextCost G h A μ := by omega
        obtain ⟨B,ν,hrB,hstrict,hstep⟩ :=
          context_predecessor G h A μ hr hp
        have hi := ih (contextCost G h B ν) (by omega)
          B ν hrB rfl
        have hrank := contextRank_strict G h B A ν μ hrB hstrict
        have hmul := Nat.mul_le_mul_right (typedThickness G h)
          (Nat.succ_le_iff.mpr hrank)
        calc
          contextCost G h A μ ≤
              contextCost G h B ν + typedThickness G h := hstep
          _ ≤ contextRank G h B ν * typedThickness G h +
                typedThickness G h := Nat.add_le_add_right hi _
          _ = (contextRank G h B ν + 1) * typedThickness G h := by
              rw [add_mul]; simp
          _ ≤ contextRank G h A μ * typedThickness G h := hmul
  intro A μ hr
  exact key (contextCost G h A μ) A μ hr rfl

/-- First numerical target of lem:typed-thickness-bound.
The Nat subtraction is safe even with empty/refinement-free grammars,
because the retained case has positive symbol cardinality. -/
theorem context_compression_bound (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) :
    ContextCompressionBound G h := by
  intro A μ hr
  have hcost := context_cost_le_rank_times_thickness G h A μ hr
  have hcard := contextRank_lt_card G h A μ hr
  have hrank : contextRank G h A μ ≤
      (finiteTypedRefinement G h).symbols.card - 1 := by omega
  have hmul := Nat.mul_le_mul_right (typedThickness G h) hrank
  exact hcost.trans hmul

#print axioms TCSPhase6.context_predecessor
#print axioms TCSPhase6.contextRank_strict
#print axioms TCSPhase6.context_cost_le_rank_times_thickness
#print axioms TCSPhase6.context_compression_bound
end TCSPhase6
