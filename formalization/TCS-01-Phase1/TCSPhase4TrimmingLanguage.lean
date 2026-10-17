import TCSPhase4Trimming

namespace TCSPhase4
open TCSPhase1 TCSPhase2

/-- A typed occurrence necessarily belongs to a complete successful
typed derivation tree, including every sibling on its path. -/
theorem occurrence_root_productive {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT}
    {A X : NT} {μ ρ : U1}
    (h : TypedOccurrence G A μ X ρ) :
    ∃ w, TypedDerives G A μ w := by
  induction h with
  | here hd => exact ⟨_, hd⟩
  | left hr hC occ ih =>
      obtain ⟨u, hu⟩ := ih
      exact ⟨u ++ _, TypedDerives.binary hr hu hC⟩
  | right hr hB occ ih =>
      obtain ⟨v, hv⟩ := ih
      exact ⟨_ ++ v, TypedDerives.binary hr hB hv⟩

/-- Start productions of the trimmed typed grammar are exclusively
the optional empty-word production and typed copies of original starts. -/
inductive TrimmedStartDerives {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) : Word → Prop
  | empty (he : G.startEmpty = true) : TrimmedStartDerives G []
  | root {A : NT} {μ : U1} {w : Word}
      (hs : A ∈ G.startRules)
      (h : TrimmedTypedDerives G A μ w) :
      TrimmedStartDerives G w

def TrimmedGrammarLanguage {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT) : Set Word :=
  {w | TrimmedStartDerives G w}

/-- Semantic trimming of the successful typed-tree grammar preserves
the *whole original start language*, not just individual retained yields. -/
theorem trimmed_grammar_language_eq {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) :
    TrimmedGrammarLanguage G = GrammarLanguage G := by
  ext w
  constructor
  · intro hw
    change TrimmedStartDerives G w at hw
    cases hw with
    | empty he => exact StartDerives.empty he
    | root hs hd =>
        exact StartDerives.root hs (typed_sound (trimmed_sound hd)).1
  · intro hw
    change StartDerives G w at hw
    cases hw with
    | empty he => exact TrimmedStartDerives.empty he
    | root hs hd =>
        have ht := typed_complete hd
        have hret := retained_at_start hs ht
        exact TrimmedStartDerives.root hs (trimmed_complete ht hret)

#print axioms TCSPhase4.occurrence_root_productive
#print axioms TCSPhase4.trimmed_grammar_language_eq
end TCSPhase4
