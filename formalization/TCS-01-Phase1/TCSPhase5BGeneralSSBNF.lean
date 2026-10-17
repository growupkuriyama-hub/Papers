import TCSPhase5Main

/-! A general finite SSBNF for an arbitrary alphabet, distinct
from Phase 4's fixed five-symbol implementation. -/
namespace TCSPhase5B
open TCSPhase5

variable {Alphabet NT : Type*}
variable [Fintype NT] [DecidableEq NT]

structure SSBNFGrammar (Alphabet NT : Type*)
    [Fintype NT] [DecidableEq NT] where
  startRules : Finset NT
  startEmpty : Bool
  terminalRules : Finset (NT × Alphabet)
  binaryRules : Finset (NT × NT × NT)

/-- The start is not an NT and cannot occur on a production RHS. -/
inductive DerivesFrom (G : SSBNFGrammar Alphabet NT) :
    NT → List Alphabet → Prop
  | terminal {A : NT} {a : Alphabet}
      (hr : (A,a) ∈ G.terminalRules) : DerivesFrom G A [a]
  | binary {A B C : NT} {u v : List Alphabet}
      (hr : (A,B,C) ∈ G.binaryRules)
      (hu : DerivesFrom G B u) (hv : DerivesFrom G C v) :
      DerivesFrom G A (u ++ v)

/-- Separate productions for the distinguished start. -/
inductive StartDerives (G : SSBNFGrammar Alphabet NT) :
    List Alphabet → Prop
  | empty (he : G.startEmpty = true) : StartDerives G []
  | root {A : NT} {w : List Alphabet}
      (hs : A ∈ G.startRules) (hd : DerivesFrom G A w) :
      StartDerives G w

def GrammarLanguage (G : SSBNFGrammar Alphabet NT) :
    Set (List Alphabet) := {w | StartDerives G w}

theorem derives_nonempty {G : SSBNFGrammar Alphabet NT}
    {A : NT} {w : List Alphabet}
    (hd : DerivesFrom G A w) : w ≠ [] := by
  induction hd with
  | terminal hr => simp
  | binary hr hu hv ihU ihV =>
      intro he
      exact ihU ((List.append_eq_nil_iff.mp he).1)

theorem nonempty_root {G : SSBNFGrammar Alphabet NT}
    {w : List Alphabet} (hw : w ∈ GrammarLanguage G)
    (hne : w ≠ []) :
    ∃ A : NT, A ∈ G.startRules ∧ DerivesFrom G A w := by
  cases hw with
  | empty he => exact False.elim (hne rfl)
  | @root A w hs hd => exact ⟨A,hs,hd⟩

theorem start_from_root {G : SSBNFGrammar Alphabet NT}
    {A : NT} {w : List Alphabet}
    (hs : A ∈ G.startRules) (hd : DerivesFrom G A w) :
    w ∈ GrammarLanguage G :=
  StartDerives.root hs hd

#print axioms TCSPhase5B.derives_nonempty
#print axioms TCSPhase5B.nonempty_root
#print axioms TCSPhase5B.start_from_root
end TCSPhase5B
