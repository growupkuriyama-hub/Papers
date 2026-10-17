import TCSPhase4TypedLifting

namespace TCSPhase4
open TCSPhase1 TCSPhase2

/-- A node in an actual successful *typed derivation tree*. The inductive
left/right constructors require successful productions in every sibling:
this is stronger than dependency-graph reachability or productivity alone. -/
inductive TypedOccurrence {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT) : NT → U1 → NT → U1 → Prop
  | here {A : NT} {μ : U1} {w : Word}
      (h : TypedDerives G A μ w) : TypedOccurrence G A μ A μ
  | left {A B C X : NT} {μ ν ρ : U1} {v : Word}
      (hr : (A, B, C) ∈ G.binaryRules)
      (hC : TypedDerives G C ν v)
      (h : TypedOccurrence G B μ X ρ) :
      TypedOccurrence G A (μ * ν) X ρ
  | right {A B C X : NT} {μ ν ρ : U1} {u : Word}
      (hr : (A, B, C) ∈ G.binaryRules)
      (hB : TypedDerives G B μ u)
      (h : TypedOccurrence G C ν X ρ) :
      TypedOccurrence G A (μ * ν) X ρ

/-- Semantic trimming: occurs in a *successful* tree from a start production. -/
def RetainedTypedSymbol {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT) (X : NT) (ρ : U1) : Prop :=
  ∃ A : NT, ∃ μ : U1, A ∈ G.startRules ∧
    TypedOccurrence G A μ X ρ

theorem occurrence_productive {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {A X : NT} {μ ρ : U1}
    (h : TypedOccurrence G A μ X ρ) :
    ∃ w, TypedDerives G X ρ w := by
  induction h with
  | here h => exact ⟨_, h⟩
  | left hr hC h ih => exact ih
  | right hr hB h ih => exact ih

theorem retained_productive {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {A : NT} {μ : U1}
    (h : RetainedTypedSymbol G A μ) :
    ∃ w, TypedDerives G A μ w := by
  obtain ⟨S, τ, hs, occ⟩ := h
  exact occurrence_productive occ

/-- Exchanging a successful subtree at an occurrence yields another
successful tree at the same typed root; this is the reachability invariant
needed to prove that all productive refinements of retained nodes survive. -/
theorem occurrence_compose {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {S A X : NT} {τ μ ρ : U1}
    (h : TypedOccurrence G S τ A μ)
    (h' : TypedOccurrence G A μ X ρ) :
    TypedOccurrence G S τ X ρ := by
  induction h with
  | here h => exact h'
  | left hr hC occ ih =>
      exact TypedOccurrence.left hr hC (ih h')
  | right hr hB occ ih =>
      exact TypedOccurrence.right hr hB (ih h')

theorem retained_at_start {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {A : NT} {μ : U1} {w : Word}
    (hs : A ∈ G.startRules)
    (hd : TypedDerives G A μ w) :
    RetainedTypedSymbol G A μ :=
  ⟨A, μ, hs, TypedOccurrence.here hd⟩

theorem retained_binary_children {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT}
    {A B C : NT} {μ ν : U1} {u v : Word}
    (hr : (A, B, C) ∈ G.binaryRules)
    (hRet : RetainedTypedSymbol G A (μ * ν))
    (hB : TypedDerives G B μ u) (hC : TypedDerives G C ν v) :
    RetainedTypedSymbol G B μ ∧ RetainedTypedSymbol G C ν := by
  obtain ⟨S, τ, hs, hOcc⟩ := hRet
  constructor
  · refine ⟨S, τ, hs, ?_⟩
    exact occurrence_compose hOcc
      (TypedOccurrence.left hr hC (TypedOccurrence.here hB))
  · refine ⟨S, τ, hs, ?_⟩
    exact occurrence_compose hOcc
      (TypedOccurrence.right hr hB (TypedOccurrence.here hC))

/-- Only productions whose typed nodes occur in some successful start
tree survive semantic trimming. This is an independent derivation relation. -/
inductive TrimmedTypedDerives {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT) : NT → U1 → Word → Prop
  | terminal {A : NT} {c : Terminal}
      (hr : (A, c) ∈ G.terminalRules)
      (hret : RetainedTypedSymbol G A (hU [c])) :
      TrimmedTypedDerives G A (hU [c]) [c]
  | binary {A B C : NT} {μ ν : U1} {u v : Word}
      (hr : (A, B, C) ∈ G.binaryRules)
      (hret : RetainedTypedSymbol G A (μ * ν))
      (hB : TrimmedTypedDerives G B μ u)
      (hC : TrimmedTypedDerives G C ν v) :
      TrimmedTypedDerives G A (μ * ν) (u ++ v)

theorem trimmed_sound {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {A : NT} {μ : U1} {w : Word}
    (h : TrimmedTypedDerives G A μ w) :
    TypedDerives G A μ w := by
  induction h with
  | terminal hr hret => exact TypedDerives.terminal hr
  | binary hr hret hB hC ihB ihC =>
      exact TypedDerives.binary hr ihB ihC

/-- Grafting gives every child of an alternative derivation an actual
successful start-tree occurrence, so the trimmed rules suffice. -/
theorem trimmed_complete {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {A : NT} {μ : U1} {w : Word}
    (h : TypedDerives G A μ w)
    (hret : RetainedTypedSymbol G A μ) :
    TrimmedTypedDerives G A μ w := by
  induction h with
  | terminal hr =>
      exact TrimmedTypedDerives.terminal hr hret
  | binary hr hB hC ihB ihC =>
      obtain ⟨hretB, hretC⟩ :=
        retained_binary_children hr hret hB hC
      exact TrimmedTypedDerives.binary hr hret
        (ihB hretB) (ihC hretC)

theorem trimmed_lifting {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {A : NT} {μ : U1} {w : Word}
    (hret : RetainedTypedSymbol G A μ) :
    TrimmedTypedDerives G A μ w ↔
      DerivesFrom G A w ∧ hU w = μ := by
  rw [← typed_lifting]
  exact ⟨trimmed_sound, fun h => trimmed_complete h hret⟩

#print axioms TCSPhase4.retained_productive
#print axioms TCSPhase4.occurrence_compose
#print axioms TCSPhase4.retained_at_start
#print axioms TCSPhase4.retained_binary_children
#print axioms TCSPhase4.trimmed_lifting
end TCSPhase4
