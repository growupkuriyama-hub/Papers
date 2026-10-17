import TCSPhase4SSBNF

namespace TCSPhase4
open TCSPhase1 TCSPhase2

/-- The *independent* inductive grammar of typed terminal and binary
productions. This is not a definitional abbreviation of untyped derivation
and a word-type equation. -/
inductive TypedDerives {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT) : NT → U1 → Word → Prop
  | terminal {A : NT} {c : Terminal}
      (hr : (A, c) ∈ G.terminalRules) :
      TypedDerives G A (hU [c]) [c]
  | binary {A B C : NT} {μ ν : U1} {u v : Word}
      (hr : (A, B, C) ∈ G.binaryRules)
      (hB : TypedDerives G B μ u)
      (hC : TypedDerives G C ν v) :
      TypedDerives G A (μ * ν) (u ++ v)

/-- Erasing type annotations maps independent typed derivations to G. -/
theorem typed_sound {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {A : NT} {μ : U1} {w : Word}
    (h : TypedDerives G A μ w) :
    DerivesFrom G A w ∧ hU w = μ := by
  induction h with
  | terminal hr =>
      exact ⟨DerivesFrom.terminal hr, rfl⟩
  | binary hr hB hC ihB ihC =>
      exact ⟨DerivesFrom.binary hr ihB.1 ihC.1, by
        rw [hU_mul, ihB.2, ihC.2]⟩

/-- Every ordinary derivation tree has a unique yield-type annotation. -/
theorem typed_complete {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {A : NT} {w : Word}
    (h : DerivesFrom G A w) : TypedDerives G A (hU w) w := by
  induction h with
  | terminal hr =>
      exact TypedDerives.terminal hr
  | binary hr hB hC ihB ihC =>
      rw [hU_mul]
      exact TypedDerives.binary hr ihB ihC

/-- Fundamental typed-lifting equivalence for arbitrary SSBNF grammars. -/
theorem typed_lifting {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {A : NT} {μ : U1} {w : Word} :
    TypedDerives G A μ w ↔
      DerivesFrom G A w ∧ hU w = μ := by
  constructor
  · exact typed_sound
  · rintro ⟨hd, ht⟩
    rw [← ht]
    exact typed_complete hd

#print axioms TCSPhase4.typed_sound
#print axioms TCSPhase4.typed_complete
#print axioms TCSPhase4.typed_lifting
end TCSPhase4
