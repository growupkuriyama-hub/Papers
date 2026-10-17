import TCSPhase3CMain

/-!
Generic finite separated-start binary normal form (SSBNF) grammars.
No property of the specific bracketed G_n appears in this grammar data.
-/
namespace TCSPhase4
open TCSPhase1 TCSPhase2

/-- A finite SSBNF presentation, with non-start symbols of a finite type.
The distinguished start symbol is deliberately external to NT, so it cannot
occur on the right-hand side of any non-start rule. -/
structure SSBNFGrammar (NT : Type) [Fintype NT] [DecidableEq NT] where
  startRules : Finset NT
  startEmpty : Bool
  terminalRules : Finset (NT × Terminal)
  binaryRules : Finset (NT × NT × NT)

/-- Actual finite-branching derivations of arbitrary SSBNF productions. -/
inductive DerivesFrom {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT) : NT → Word → Prop
  | terminal {A : NT} {c : Terminal}
      (hr : (A, c) ∈ G.terminalRules) :
      DerivesFrom G A [c]
  | binary {A B C : NT} {u v : Word}
      (hr : (A, B, C) ∈ G.binaryRules)
      (hB : DerivesFrom G B u) (hC : DerivesFrom G C v) :
      DerivesFrom G A (u ++ v)

/-- Start productions are *only* S0 -> epsilon and S0 -> A. -/
inductive StartDerives {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT) : Word → Prop
  | empty (he : G.startEmpty = true) : StartDerives G []
  | from {A : NT} {w : Word} (hs : A ∈ G.startRules)
      (h : DerivesFrom G A w) : StartDerives G w

def GrammarLanguage {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT) : Set Word :=
  {w | StartDerives G w}

theorem derivesFrom_nonempty {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {A : NT} {w : Word}
    (h : DerivesFrom G A w) : w ≠ [] := by
  induction h with
  | terminal hr => simp
  | binary hr hl hr ihl ihr =>
      intro he
      have hn := congrArg List.length he
      simp only [List.length_append, List.length_nil] at hn
      have hlen : (List.nil : Word).length = 0 := rfl
      have : _ := ihl
      have hzero : _ := he
      simp_all [List.append_eq_nil_iff]

/-- Any nonempty start derivation must begin with a start-unit production. -/
theorem nonempty_start_has_root {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {w : Word}
    (hw : w ∈ GrammarLanguage G) (hne : w ≠ []) :
    ∃ A : NT, A ∈ G.startRules ∧ DerivesFrom G A w := by
  change StartDerives G w at hw
  cases hw with
  | empty he => contradiction
  | from hs hd => exact ⟨_, hs, hd⟩

theorem start_rule_generates {NT : Type} [Fintype NT] [DecidableEq NT]
    {G : SSBNFGrammar NT} {A : NT} {w : Word}
    (hs : A ∈ G.startRules) (hd : DerivesFrom G A w) :
    w ∈ GrammarLanguage G :=
  StartDerives.from hs hd

#print axioms TCSPhase4.nonempty_start_has_root
#print axioms TCSPhase4.start_rule_generates
end TCSPhase4
