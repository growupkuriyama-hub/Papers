import TCSPhase6Thickness

/-! Explicit Nat.find minimality interfaces for the existing Phase 5B
canonical (minimum-length, not shortlex-tie-broken) choices. -/
namespace TCSPhase6
open TCSPhase5B
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

theorem chosenYield_is_shortest
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (A : NT) (μ : M) (hr : RetainedTypedSymbol G h A μ)
    (w : List Alphabet) (hw : TypedDerives G h A μ w) :
    (chosenYield G h A μ).length ≤ w.length := by
  classical
  have he := (shortestYieldOfRet_spec hr).2
  change (shortestYieldOfRet hr).length = shortestYieldLength hr at he
  have hmin : shortestYieldLength hr ≤ w.length := by
    unfold shortestYieldLength
    apply Nat.find_min'
    exact ⟨w,hw,rfl⟩
  unfold chosenYield
  simp only [dif_pos hr]
  omega

theorem chosenContext_is_shortest
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (A : NT) (μ : M) (hr : RetainedTypedSymbol G h A μ)
    (u v : List Alphabet) (hc : TypedContext G h A μ u v) :
    (chosenContext G h A μ).1.length +
      (chosenContext G h A μ).2.length ≤ u.length + v.length := by
  classical
  have he := (shortestContextOfRet_spec hr).2
  have hmin : shortestContextLength hr ≤ u.length + v.length := by
    unfold shortestContextLength
    apply Nat.find_min'
    exact ⟨(u,v),hc,rfl⟩
  unfold chosenContext
  simp only [dif_pos hr]
  omega

theorem chosenYield_length_pos
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (A : NT) (μ : M) (hr : RetainedTypedSymbol G h A μ) :
    0 < (chosenYield G h A μ).length := by
  cases he : chosenYield G h A μ with
  | nil => exact False.elim ((chosenYield_nonempty hr) he)
  | cons a as => simp [he]

#print axioms TCSPhase6.chosenYield_is_shortest
#print axioms TCSPhase6.chosenContext_is_shortest
#print axioms TCSPhase6.chosenYield_length_pos
end TCSPhase6
