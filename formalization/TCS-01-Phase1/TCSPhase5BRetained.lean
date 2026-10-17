import TCSPhase5BTypedRefinement

/-! Typed successful-tree contexts and retained symbols for arbitrary
finite h-typing, independent of the earlier fixed h_U construction. -/
namespace TCSPhase5B
open TCSPhase5
variable {Alphabet NT M : Type*}
variable [Fintype NT] [DecidableEq NT] [Monoid M]

/-- Actual terminal reaching contexts. Each descent uses an original
binary production and a successful typed derivation of its sibling.
Unlike mere graph reachability, the path is witnessed by real trees. -/
inductive TypedContext (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) :
    NT → M → List Alphabet → List Alphabet → Prop
  | root {A : NT} {μ : M} {w : List Alphabet}
      (hs : A ∈ G.startRules)
      (hd : TypedDerives G h A μ w) :
      TypedContext G h A μ [] []
  | left {A B C : NT} {μ ν : M}
      {u v wB wC : List Alphabet}
      (hc : TypedContext G h A (μ * ν) u v)
      (hr : (A,B,C) ∈ G.binaryRules)
      (hB : TypedDerives G h B μ wB)
      (hC : TypedDerives G h C ν wC) :
      TypedContext G h B μ u (wC ++ v)
  | right {A B C : NT} {μ ν : M}
      {u v wB wC : List Alphabet}
      (hc : TypedContext G h A (μ * ν) u v)
      (hr : (A,B,C) ∈ G.binaryRules)
      (hB : TypedDerives G h B μ wB)
      (hC : TypedDerives G h C ν wC) :
      TypedContext G h C ν (u ++ wB) v

def RetainedTypedSymbol (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (A : NT) (μ : M) : Prop :=
  ∃ u v, TypedContext G h A μ u v

/-- Every retained typed symbol actually produces a nonempty yield.
This is proved by induction on the successful typed context path. -/
theorem context_productive {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    {u v : List Alphabet}
    (hc : TypedContext G h A μ u v) :
    ∃ w, TypedDerives G h A μ w := by
  induction hc with
  | root hs hd => exact ⟨_,hd⟩
  | left hc hr hB hC ih => exact ⟨_,hB⟩
  | right hc hr hB hC ih => exact ⟨_,hC⟩

theorem retained_productive {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) :
    ∃ w, TypedDerives G h A μ w := by
  obtain ⟨_,_,hc⟩ := hr
  exact context_productive hc

/-- Changing a successful subtree at the context's hole does not
affect the validity of the whole start derivation. -/
theorem context_plug {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    {u v : List Alphabet}
    (hc : TypedContext G h A μ u v) :
    ∀ {w : List Alphabet}, TypedDerives G h A μ w →
       u ++ w ++ v ∈ GrammarLanguage G := by
  induction hc with
  | root hs hd =>
      intro w hw
      simpa using start_from_root hs (typed_sound hw).1
  | left hc hr hB hC ih =>
      intro w hw
      have hparent := ih (TypedDerives.binary hr hw hC)
      simpa only [List.append_assoc] using hparent
  | right hc hr hB hC ih =>
      intro w hw
      have hparent := ih (TypedDerives.binary hr hB hw)
      simpa only [List.append_assoc] using hparent

theorem retained_context_plug {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) :
    ∃ u v, ∀ w, TypedDerives G h A μ w →
      u ++ w ++ v ∈ GrammarLanguage G := by
  obtain ⟨u,v,hc⟩ := hr
  exact ⟨u,v,fun _ hd => context_plug hc hd⟩

theorem retained_at_start {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    {w : List Alphabet} (hs : A ∈ G.startRules)
    (hd : TypedDerives G h A μ w) :
    RetainedTypedSymbol G h A μ :=
  ⟨[], [], TypedContext.root hs hd⟩

theorem retained_binary_children {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A B C : NT} {μ ν : M}
    {wB wC : List Alphabet}
    (ha : RetainedTypedSymbol G h A (μ * ν))
    (rule : (A,B,C) ∈ G.binaryRules)
    (hB : TypedDerives G h B μ wB)
    (hC : TypedDerives G h C ν wC) :
    RetainedTypedSymbol G h B μ ∧
      RetainedTypedSymbol G h C ν := by
  obtain ⟨u,v,hctx⟩ := ha
  exact ⟨⟨u,wC ++ v,TypedContext.left hctx rule hB hC⟩,
    ⟨u ++ wB,v,TypedContext.right hctx rule hB hC⟩⟩

/-- An independent grammar derivation relation whose rules retain
every symbol, not merely a semantic language predicate. -/
inductive TrimmedTypedDerives (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) : NT → M → List Alphabet → Prop
  | terminal {A : NT} {a : Alphabet}
      (hr : (A,a) ∈ G.terminalRules)
      (ret : RetainedTypedSymbol G h A (h [a])) :
      TrimmedTypedDerives G h A (h [a]) [a]
  | binary {A B C : NT} {μ ν : M} {u v : List Alphabet}
      (hr : (A,B,C) ∈ G.binaryRules)
      (ret : RetainedTypedSymbol G h A (μ * ν))
      (hB : TrimmedTypedDerives G h B μ u)
      (hC : TrimmedTypedDerives G h C ν v) :
      TrimmedTypedDerives G h A (μ * ν) (u ++ v)

theorem trimmed_sound {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    {w : List Alphabet}
    (hd : TrimmedTypedDerives G h A μ w) :
    TypedDerives G h A μ w := by
  induction hd with
  | terminal rule ret => exact TypedDerives.terminal rule
  | binary rule ret hB hC ihB ihC =>
      exact TypedDerives.binary rule ihB ihC

theorem trimmed_complete {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    {w : List Alphabet}
    (hd : TypedDerives G h A μ w)
    (ret : RetainedTypedSymbol G h A μ) :
    TrimmedTypedDerives G h A μ w := by
  induction hd with
  | terminal rule =>
      exact TrimmedTypedDerives.terminal rule ret
  | binary rule hB hC ihB ihC =>
      obtain ⟨retB, retC⟩ :=
        retained_binary_children ret rule hB hC
      exact TrimmedTypedDerives.binary rule ret
        (ihB retB) (ihC retC)

theorem trimmed_lifting {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    {w : List Alphabet}
    (ret : RetainedTypedSymbol G h A μ) :
    TrimmedTypedDerives G h A μ w ↔
      DerivesFrom G A w ∧ h w = μ := by
  constructor
  · intro hd
    exact typed_sound (trimmed_sound hd)
  · intro hd
    exact trimmed_complete ((typed_lifting).mpr hd) ret

#print axioms TCSPhase5B.context_productive
#print axioms TCSPhase5B.retained_productive
#print axioms TCSPhase5B.context_plug
#print axioms TCSPhase5B.retained_at_start
#print axioms TCSPhase5B.retained_binary_children
#print axioms TCSPhase5B.trimmed_lifting
end TCSPhase5B
