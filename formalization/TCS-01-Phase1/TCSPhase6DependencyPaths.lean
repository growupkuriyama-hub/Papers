import TCSPhase6Contexts

/-! Every actual successful reaching context supplies a typed dependency
walk. Steps retain the original binary production *and* productive typed
derivations of both children; no purely syntactic/unproductive edges. -/
namespace TCSPhase6
open TCSPhase5B
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

inductive TypedDependencyPath (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) :
    (NT × M) → List (NT × M) → Prop
  | root {A : NT} {μ : M} {w : List Alphabet}
      (hs : A ∈ G.startRules) (hd : TypedDerives G h A μ w) :
      TypedDependencyPath G h (A,μ) [(A,μ)]
  | left {A B C : NT} {μ ν : M} {wB wC : List Alphabet}
      {p : List (NT × M)}
      (hp : TypedDependencyPath G h (A, μ * ν) p)
      (rule : (A,B,C) ∈ G.binaryRules)
      (hB : TypedDerives G h B μ wB)
      (hC : TypedDerives G h C ν wC) :
      TypedDependencyPath G h (B,μ) (p ++ [(B,μ)])
  | right {A B C : NT} {μ ν : M} {wB wC : List Alphabet}
      {p : List (NT × M)}
      (hp : TypedDependencyPath G h (A, μ * ν) p)
      (rule : (A,B,C) ∈ G.binaryRules)
      (hB : TypedDerives G h B μ wB)
      (hC : TypedDerives G h C ν wC) :
      TypedDependencyPath G h (C,ν) (p ++ [(C,ν)])

/-- A real successful typed context contains a derivation-backed
root-to-target dependency walk. -/
theorem typedContext_dependency_path
    {G : SSBNFGrammar Alphabet NT} {h : List Alphabet →* M}
    {A : NT} {μ : M} {u v : List Alphabet}
    (hc : TypedContext G h A μ u v) :
    ∃ p : List (NT × M), TypedDependencyPath G h (A,μ) p := by
  induction hc with
  | root hs hd =>
      exact ⟨_,TypedDependencyPath.root hs hd⟩
  | left hc rule hB hC ih =>
      obtain ⟨p,hp⟩ := ih
      exact ⟨_, TypedDependencyPath.left hp rule hB hC⟩
  | right hc rule hB hC ih =>
      obtain ⟨p,hp⟩ := ih
      exact ⟨_, TypedDependencyPath.right hp rule hB hC⟩

/-- The end of such a walk is necessarily productive and reachable. -/
theorem typedDependencyPath_retained
    {G : SSBNFGrammar Alphabet NT} {h : List Alphabet →* M}
    {A : NT} {μ : M} {p : List (NT × M)}
    (hp : TypedDependencyPath G h (A,μ) p) :
    RetainedTypedSymbol G h A μ := by
  induction hp with
  | root hs hd => exact retained_at_start hs hd
  | left hp rule hB hC ih =>
      exact (retained_binary_children ih rule hB hC).1
  | right hp rule hB hC ih =>
      exact (retained_binary_children ih rule hB hC).2

/-- All actually retained symbols admit such a successful walk. -/
theorem retained_dependency_path
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (A : NT) (μ : M) (hr : RetainedTypedSymbol G h A μ) :
    ∃ p : List (NT × M), TypedDependencyPath G h (A,μ) p := by
  obtain ⟨u,v,hc⟩ := hr
  exact typedContext_dependency_path hc

#print axioms TCSPhase6.typedContext_dependency_path
#print axioms TCSPhase6.typedDependencyPath_retained
#print axioms TCSPhase6.retained_dependency_path
end TCSPhase6
