import TCSPhase5BGeneralSSBNF

/-! Independent typed derivations over *any* monoid homomorphism. -/
namespace TCSPhase5B
open TCSPhase5
variable {Alphabet NT M : Type*}
variable [Fintype NT] [DecidableEq NT] [Monoid M]

inductive TypedDerives (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) : NT → M → List Alphabet → Prop
  | terminal {A : NT} {a : Alphabet}
      (hr : (A,a) ∈ G.terminalRules) :
      TypedDerives G h A (h [a]) [a]
  | binary {A B C : NT} {μ ν : M}
      {u v : List Alphabet}
      (hr : (A,B,C) ∈ G.binaryRules)
      (hu : TypedDerives G h B μ u)
      (hv : TypedDerives G h C ν v) :
      TypedDerives G h A (μ * ν) (u ++ v)

/-- Erase all actual type annotations and prove the annotated type is
the homomorphic image of the derived terminal yield. -/
theorem typed_sound {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    {w : List Alphabet} (hd : TypedDerives G h A μ w) :
    DerivesFrom G A w ∧ h w = μ := by
  induction hd with
  | terminal hr =>
      exact ⟨DerivesFrom.terminal hr, rfl⟩
  | binary hr hu hv ihU ihV =>
      constructor
      · exact DerivesFrom.binary hr ihU.1 ihV.1
      · change h (_ * _) = _ * _
        rw [map_mul, ihU.2, ihV.2]

/-- Annotate an arbitrary original derivation tree bottom up with
actual h-types; no type-equality premise is assumed. -/
theorem typed_complete {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT}
    {w : List Alphabet} (hd : DerivesFrom G A w) :
    TypedDerives G h A (h w) w := by
  induction hd with
  | terminal hr =>
      exact TypedDerives.terminal hr
  | binary hr hu hv ihU ihV =>
      change TypedDerives G h _ (h (_ * _)) (_ ++ _)
      rw [map_mul]
      exact TypedDerives.binary hr ihU ihV

theorem typed_lifting {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    {w : List Alphabet} :
    TypedDerives G h A μ w ↔
      DerivesFrom G A w ∧ h w = μ := by
  constructor
  · exact typed_sound
  · rintro ⟨hd,ht⟩
    rw [← ht]
    exact typed_complete hd

theorem typed_nonempty {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    {w : List Alphabet} (hd : TypedDerives G h A μ w) :
    w ≠ [] := derives_nonempty (typed_sound hd).1

#print axioms TCSPhase5B.typed_sound
#print axioms TCSPhase5B.typed_complete
#print axioms TCSPhase5B.typed_lifting
#print axioms TCSPhase5B.typed_nonempty
end TCSPhase5B
