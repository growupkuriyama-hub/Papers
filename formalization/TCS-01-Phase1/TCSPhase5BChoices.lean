import TCSPhase5BRetained

/-! Minimum-length (not yet shortlex-tie-broken) productive yields and
terminal reaching contexts of *retained* typed symbols. -/
namespace TCSPhase5B
open TCSPhase5
variable {Alphabet NT M : Type*}
variable [Fintype NT] [DecidableEq NT] [Monoid M]

private theorem length_yield_exists {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) :
    ∃ n : Nat, ∃ w : List Alphabet,
      TypedDerives G h A μ w ∧ w.length = n := by
  obtain ⟨w,hd⟩ := retained_productive hr
  exact ⟨w.length,w,hd,rfl⟩

/-- Least length of a retained symbol's actual typed terminal yields. -/
noncomputable def shortestYieldLength {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) : Nat :=
  Nat.find (length_yield_exists hr)

noncomputable def shortestYieldOfRet {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) : List Alphabet :=
  Classical.choose (Nat.find_spec (length_yield_exists hr))

theorem shortestYieldOfRet_spec {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) :
    TypedDerives G h A μ (shortestYieldOfRet hr) ∧
      (shortestYieldOfRet hr).length = shortestYieldLength hr := by
  exact Classical.choose_spec (Nat.find_spec (length_yield_exists hr))

/-- Selected shortest-length yield at each retained symbol; [] is an
unobservable fallback outside the retained domain. -/
noncomputable def chosenYield (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (A : NT) (μ : M) : List Alphabet :=
  if hr : RetainedTypedSymbol G h A μ then shortestYieldOfRet hr else []

theorem chosenYield_spec {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) :
    TypedDerives G h A μ (chosenYield G h A μ) := by
  unfold chosenYield
  simp only [dif_pos hr]
  exact (shortestYieldOfRet_spec hr).1

theorem chosenYield_nonempty {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) :
    chosenYield G h A μ ≠ [] :=
  typed_nonempty (chosenYield_spec hr)

theorem chosenYield_type {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) :
    h (chosenYield G h A μ) = μ :=
  (typed_sound (chosenYield_spec hr)).2

private theorem context_length_exists {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) :
    ∃ n : Nat, ∃ p : List Alphabet × List Alphabet,
      TypedContext G h A μ p.1 p.2 ∧
      p.1.length + p.2.length = n := by
  obtain ⟨u,v,hctx⟩ := hr
  exact ⟨u.length+v.length,(u,v),hctx,rfl⟩

/-- A minimum-total-length terminal reaching context (with unspecified
tie-breaking among equal-length contexts). -/
noncomputable def shortestContextOfRet {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) :
    List Alphabet × List Alphabet :=
  Classical.choose (Nat.find_spec (context_length_exists hr))

theorem shortestContextOfRet_spec {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) :
    TypedContext G h A μ (shortestContextOfRet hr).1
      (shortestContextOfRet hr).2 ∧
    (shortestContextOfRet hr).1.length +
      (shortestContextOfRet hr).2.length =
      Nat.find (context_length_exists hr) := by
  exact Classical.choose_spec (Nat.find_spec (context_length_exists hr))

noncomputable def chosenContext (G : SSBNFGrammar Alphabet NT)
    (h : List Alphabet →* M) (A : NT) (μ : M) :
    List Alphabet × List Alphabet :=
  if hr : RetainedTypedSymbol G h A μ then
    shortestContextOfRet hr else ([],[])

theorem chosenContext_spec {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    (hr : RetainedTypedSymbol G h A μ) :
    TypedContext G h A μ (chosenContext G h A μ).1
      (chosenContext G h A μ).2 := by
  unfold chosenContext
  simp only [dif_pos hr]
  exact (shortestContextOfRet_spec hr).1

/-- Minimum distance zero at every productive typed start child is
forced, not assumed as a context-selection hypothesis. -/
theorem chosenContext_start_empty {G : SSBNFGrammar Alphabet NT}
    {h : List Alphabet →* M} {A : NT} {μ : M}
    {w : List Alphabet} (hs : A ∈ G.startRules)
    (hd : TypedDerives G h A μ w) :
    chosenContext G h A μ = ([], []) := by
  have hr : RetainedTypedSymbol G h A μ :=
    retained_at_start hs hd
  have h0 : ∃ p : List Alphabet × List Alphabet,
      TypedContext G h A μ p.1 p.2 ∧
      p.1.length + p.2.length = 0 :=
    ⟨([],[]),TypedContext.root hs hd,rfl⟩
  have hle : Nat.find (context_length_exists hr) ≤ 0 :=
    Nat.find_min' (context_length_exists hr) 0 h0
  have hc := (shortestContextOfRet_spec hr).2
  have hlen : (shortestContextOfRet hr).1.length +
      (shortestContextOfRet hr).2.length = 0 := by omega
  have hp : shortestContextOfRet hr = ([],[]) := by
    cases hp : shortestContextOfRet hr with
    | mk u v =>
        simp only at hlen
        have hu : u = [] := List.length_eq_zero_iff.mp (by omega)
        have hv : v = [] := List.length_eq_zero_iff.mp (by omega)
        subst u
        subst v
        rfl
  simp only [chosenContext, dif_pos hr, hp]

#print axioms TCSPhase5B.chosenYield_spec
#print axioms TCSPhase5B.chosenYield_type
#print axioms TCSPhase5B.chosenContext_spec
#print axioms TCSPhase5B.chosenContext_start_empty
end TCSPhase5B
