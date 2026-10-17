import TCSPhase4FiniteRefinement

namespace TCSPhase4
open TCSPhase1 TCSPhase2

/-- Independent operational trimming reachability after productive-rule
filtering: starts must yield, and one may traverse a binary rule only if
both child typed symbols admit completed terminal derivations. This is a
least inductively generated relation, separate from successful-tree
occurrence used to define RetainedTypedSymbol. -/
inductive OperationalReachable {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) : NT → U1 → Prop
  | root {A : NT} {μ : U1} {w : Word}
      (hs : A ∈ G.startRules) (hd : TypedDerives G A μ w) :
      OperationalReachable G A μ
  | left {A B C : NT} {μ ν : U1} {u v : Word}
      (ha : OperationalReachable G A (μ * ν))
      (hr : (A, B, C) ∈ G.binaryRules)
      (hB : TypedDerives G B μ u) (hC : TypedDerives G C ν v) :
      OperationalReachable G B μ
  | right {A B C : NT} {μ ν : U1} {u v : Word}
      (ha : OperationalReachable G A (μ * ν))
      (hr : (A, B, C) ∈ G.binaryRules)
      (hB : TypedDerives G B μ u) (hC : TypedDerives G C ν v) :
      OperationalReachable G C ν

/-- A typed occurrence path can be followed by operational reachability
after the productivity test of all sibling branches. -/
theorem occurrence_to_operational {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT}
    {A X : NT} {μ ρ : U1}
    (occ : TypedOccurrence G A μ X ρ) :
    OperationalReachable G A μ → OperationalReachable G X ρ := by
  induction occ with
  | here hd =>
      intro hr
      exact hr
  | left hr hC hOcc ih =>
      intro hrA
      obtain ⟨u, hB⟩ := occurrence_root_productive hOcc
      exact ih (OperationalReachable.left hrA hr hB hC)
  | right hr hB hOcc ih =>
      intro hrA
      obtain ⟨v, hC⟩ := occurrence_root_productive hOcc
      exact ih (OperationalReachable.right hrA hr hB hC)

/-- Independently defined productive-rule graph reachability equals the
predicate "occurs in some successful typed start derivation tree". -/
theorem operational_retained_iff {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) (A : NT) (μ : U1) :
    OperationalReachable G A μ ↔ RetainedTypedSymbol G A μ := by
  constructor
  · intro h
    induction h with
    | root hs hd =>
        exact retained_at_start hs hd
    | left ha hr hB hC ih =>
        exact (retained_binary_children hr ih hB hC).1
    | right ha hr hB hC ih =>
        exact (retained_binary_children hr ih hB hC).2
  · rintro ⟨S, τ, hs, occ⟩
    obtain ⟨w, hd⟩ := occurrence_root_productive occ
    exact occurrence_to_operational occ (OperationalReachable.root hs hd)

/-- Consequently the actual finite typed terminal-rule pruning agrees
with this independently defined operational least reachability relation. -/
theorem finite_operational_terminal_iff {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT)
    (A : NT) (μ : U1) (c : Terminal) :
    ((A, μ), c) ∈ (FiniteTrimmedRefinement G).terminalRules ↔
      (A, c) ∈ G.terminalRules ∧ μ = hU [c] ∧
      OperationalReachable G A μ := by
  rw [finite_trimmed_terminal_iff]
  simp only [← operational_retained_iff]

theorem finite_operational_binary_iff {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT)
    (A B C : NT) (μ ν ρ : U1) :
    ((A, μ), (B, ν), (C, ρ)) ∈
      (FiniteTrimmedRefinement G).binaryRules ↔
      (A, B, C) ∈ G.binaryRules ∧ μ = ν * ρ ∧
      OperationalReachable G A μ ∧
      OperationalReachable G B ν ∧
      OperationalReachable G C ρ := by
  rw [finite_trimmed_binary_iff]
  simp only [← operational_retained_iff]

#print axioms TCSPhase4.occurrence_to_operational
#print axioms TCSPhase4.operational_retained_iff
#print axioms TCSPhase4.finite_operational_terminal_iff
#print axioms TCSPhase4.finite_operational_binary_iff

end TCSPhase4
