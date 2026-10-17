import TCSPhase5BFiniteTyped

/-! Independent derivations from the actual finite typed/retained
production sets, with exact correspondence to the independently
defined trimmed typed derivations. -/
namespace TCSPhase5B
open TCSPhase5
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

inductive FiniteTypedDerives (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) :
    TypedSymbol NT M → List Alphabet → Prop
  | terminal {A : NT} {μ : M} {a : Alphabet}
      (hr : ((A,μ),a) ∈ (finiteTypedRefinement G h).terminalRules) :
      FiniteTypedDerives G h (A,μ) [a]
  | binary {A B C : NT} {τ μ ν : M} {u v : List Alphabet}
      (hr : ((A,τ),(B,μ),(C,ν)) ∈
        (finiteTypedRefinement G h).binaryRules)
      (hu : FiniteTypedDerives G h (B,μ) u)
      (hv : FiniteTypedDerives G h (C,ν) v) :
      FiniteTypedDerives G h (A,τ) (u ++ v)

theorem finite_typed_sound {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {p : TypedSymbol NT M}
    {w : List Alphabet}
    (hd : FiniteTypedDerives G h p w) :
    TrimmedTypedDerives G h p.1 p.2 w := by
  induction hd with
  | terminal hr =>
      obtain ⟨orig,ht,ret⟩ := (finite_terminal_iff G h _ _ _).mp hr
      subst μ
      exact TrimmedTypedDerives.terminal orig ret
  | binary hr hu hv ihU ihV =>
      obtain ⟨orig,ht,ret,_,_⟩ :=
        (finite_binary_iff G h _ _ _ _ _ _).mp hr
      subst τ
      exact TrimmedTypedDerives.binary orig ret ihU ihV

theorem finite_typed_complete {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    {w : List Alphabet} (hd : TrimmedTypedDerives G h A μ w) :
    FiniteTypedDerives G h (A,μ) w := by
  induction hd with
  | terminal rule ret =>
      exact FiniteTypedDerives.terminal
        ((finite_terminal_iff G h _ _ _).mpr ⟨rule,rfl,ret⟩)
  | binary rule ret hB hC ihB ihC =>
      obtain ⟨rB,rC⟩ :=
        retained_binary_children ret rule (trimmed_sound hB) (trimmed_sound hC)
      exact FiniteTypedDerives.binary
        ((finite_binary_iff G h _ _ _ _ _ _).mpr
          ⟨rule,rfl,ret,rB,rC⟩) ihB ihC

theorem finite_typed_iff (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (A : NT) (μ : M)
    (w : List Alphabet) :
    FiniteTypedDerives G h (A,μ) w ↔
      TrimmedTypedDerives G h A μ w := by
  exact ⟨finite_typed_sound, finite_typed_complete⟩

inductive FiniteTypedStart (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) : List Alphabet → Prop
  | empty (he : (finiteTypedRefinement G h).startEmpty = true) :
      FiniteTypedStart G h []
  | root {A : NT} {μ : M} {w : List Alphabet}
      (hs : (A,μ) ∈ (finiteTypedRefinement G h).startRules)
      (hd : FiniteTypedDerives G h (A,μ) w) :
      FiniteTypedStart G h w

/-- Language preservation by a *real finite-rule-set* typed refinement,
not just an equality of semantic-language predicates. -/
theorem finite_typed_start_iff (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (w : List Alphabet) :
    FiniteTypedStart G h w ↔ StartDerives G w := by
  constructor
  · intro hd
    cases hd with
    | empty he =>
        exact StartDerives.empty (by simpa [finiteTypedRefinement] using he)
    | root hs ht =>
        have hs' := (finite_start_iff G h _ _).mp hs
        exact StartDerives.root hs'.1
          (typed_sound (trimmed_sound (finite_typed_sound ht))).1
  · intro hd
    cases hd with
    | empty he =>
        exact FiniteTypedStart.empty
          (by simpa [finiteTypedRefinement] using he)
    | root hs hd =>
        have ht := typed_complete (h:=h) hd
        have ret := retained_at_start hs ht
        exact FiniteTypedStart.root
          ((finite_start_iff G h _ _).mpr ⟨hs,ret⟩)
          (finite_typed_complete (trimmed_complete ht ret))

#print axioms TCSPhase5B.finite_typed_iff
#print axioms TCSPhase5B.finite_typed_start_iff
end TCSPhase5B
