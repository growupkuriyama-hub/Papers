import TCSPhase4TrimmingLanguage
import TCSPhase4Thickness

namespace TCSPhase4
open TCSPhase1 TCSPhase2

/-- An explicit finite presentation of the semantically trimmed typed
refinement: distinct nonterminals are pairs (A,μ), terminal and binary
rules are finite filters of actual original rules and type equations,
and all retained symbols must occur in a successful typed start tree. -/
noncomputable def FiniteTrimmedRefinement {NT : Type}
    [Fintype NT] [DecidableEq NT] (G : SSBNFGrammar NT) :
    SSBNFGrammar (NT × U1) := by
  classical
  exact {
    startRules := Finset.univ.filter
      (fun p => p.1 ∈ G.startRules ∧ RetainedTypedSymbol G p.1 p.2)
    startEmpty := G.startEmpty
    terminalRules := Finset.univ.filter
      (fun p => (p.1.1, p.2) ∈ G.terminalRules ∧
        p.1.2 = hU [p.2] ∧ RetainedTypedSymbol G p.1.1 p.1.2)
    binaryRules := Finset.univ.filter
      (fun p => (p.1.1, p.2.1.1, p.2.2.1) ∈ G.binaryRules ∧
        p.1.2 = p.2.1.2 * p.2.2.2 ∧
        RetainedTypedSymbol G p.1.1 p.1.2 ∧
        RetainedTypedSymbol G p.2.1.1 p.2.1.2 ∧
        RetainedTypedSymbol G p.2.2.1 p.2.2.2)
  }

/-- Each terminal rule of the finite trimmed refinement corresponds
to a real original terminal rule, its exact hU annotation, and a
successfully retained parent. -/
theorem finite_trimmed_terminal_iff {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT)
    (A : NT) (μ : U1) (c : Terminal) :
    ((A, μ), c) ∈ (FiniteTrimmedRefinement G).terminalRules ↔
      (A, c) ∈ G.terminalRules ∧ μ = hU [c] ∧
      RetainedTypedSymbol G A μ := by
  classical
  simp [FiniteTrimmedRefinement]

theorem finite_trimmed_binary_iff {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT)
    (A B C : NT) (μ ν ρ : U1) :
    ((A, μ), (B, ν), (C, ρ)) ∈
      (FiniteTrimmedRefinement G).binaryRules ↔
      (A, B, C) ∈ G.binaryRules ∧ μ = ν * ρ ∧
      RetainedTypedSymbol G A μ ∧
      RetainedTypedSymbol G B ν ∧
      RetainedTypedSymbol G C ρ := by
  classical
  simp [FiniteTrimmedRefinement]

theorem trimmed_root_retained {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT}
    {A : NT} {μ : U1} {w : Word}
    (h : TrimmedTypedDerives G A μ w) :
    RetainedTypedSymbol G A μ := by
  cases h with
  | terminal hr hret => exact hret
  | binary hr hret hB hC => exact hret

/-- From the independent inductive retained typed derivation to an actual
derivation of the finite rule-set refinement. -/
theorem finite_trimmed_complete {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT}
    {A : NT} {μ : U1} {w : Word}
    (h : TrimmedTypedDerives G A μ w) :
    DerivesFrom (FiniteTrimmedRefinement G) (A, μ) w := by
  induction h with
  | terminal hr hret =>
      apply DerivesFrom.terminal
      exact (finite_trimmed_terminal_iff G _ _ _).mpr
        ⟨hr, rfl, hret⟩
  | binary hr hret hB hC ihB ihC =>
      have hretB := trimmed_root_retained hB
      have hretC := trimmed_root_retained hC
      apply DerivesFrom.binary
        ((finite_trimmed_binary_iff G _ _ _ _ _ _).mpr
          ⟨hr, rfl, hret, hretB, hretC⟩) ihB ihC

/-- Every derivation from the actual finite typed rule set is sound for
the independent semantic trimmed derivation relation. -/
theorem finite_trimmed_sound {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT}
    {X : NT × U1} {w : Word}
    (h : DerivesFrom (FiniteTrimmedRefinement G) X w) :
    TrimmedTypedDerives G X.1 X.2 w := by
  induction h with
  | terminal hr =>
      obtain ⟨A, μ⟩ := X
      obtain ⟨hr', ht, hret⟩ :=
        (finite_trimmed_terminal_iff G A μ _).mp hr
      subst μ
      exact TrimmedTypedDerives.terminal hr' hret
  | binary hr hB hC ihB ihC =>
      obtain ⟨A, μ⟩ := X
      obtain ⟨B, ν⟩ := B
      obtain ⟨C, ρ⟩ := C
      obtain ⟨hr', ht, hret, _, _⟩ :=
        (finite_trimmed_binary_iff G A B C μ ν ρ).mp hr
      subst μ
      exact TrimmedTypedDerives.binary hr' hret ihB ihC

#print axioms TCSPhase4.finite_trimmed_terminal_iff
#print axioms TCSPhase4.finite_trimmed_binary_iff
#print axioms TCSPhase4.finite_trimmed_complete
#print axioms TCSPhase4.finite_trimmed_sound
end TCSPhase4
