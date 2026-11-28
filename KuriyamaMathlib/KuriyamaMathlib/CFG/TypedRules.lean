import KuriyamaMathlib.CFG.KernelReduction
import KuriyamaMathlib.Algebra.FreshIdentity

/-! Syntactic rule typing implies semantic fibre consistency.
No type-consistency obligation is assumed as an axiom. -/
namespace KuriyamaMathlib
open LeanCfgProject.TCS1
universe u v z
variable {α : Type u} {N : Type v} {M : Type z}

def rhsType (obs : Word α → M) (τ : N → M) (e : M)
    (mul : M → M → M) : List (MixedSymbol N α) → M
  | [] => e
  | .inl A :: rhs => mul (τ A) (rhsType obs τ e mul rhs)
  | .inr a :: rhs => mul (obs [a]) (rhsType obs τ e mul rhs)

theorem rhs_realizes_type (obs : Word α → M) (τ : N → M) (e : M)
    (mul : M → M → M) (hnil : obs [] = e)
    (happend : ∀ x y, obs (x ++ y) = mul (obs x) (obs y))
    (X : N → Set (Word α)) (hX : ∀ A, X A ⊆ fiber obs (τ A))
    (rhs : List (MixedSymbol N α)) (w : Word α)
    (hw : RhsRealizes X rhs w) : obs w = rhsType obs τ e mul rhs := by
  induction rhs generalizing w with
  | nil =>
    have he : w = [] := hw
    subst w
    exact hnil
  | cons s rhs ih =>
    cases s with
    | inl A =>
      rcases hw with ⟨x, y, rfl, hx, hy⟩
      have ht : obs x = τ A := hX A hx
      change obs (x ++ y) = mul (τ A) (rhsType obs τ e mul rhs)
      rw [happend, ht, ih y hy]
    | inr a =>
      rcases hw with ⟨y, rfl, hy⟩
      change obs ([a] ++ y) = mul (obs [a]) (rhsType obs τ e mul rhs)
      rw [happend, ih y hy]

theorem ruleFiberConsistent_of_types (R : MixedRules N α)
    (obs : Word α → M) (τ : N → M) (e : M) (mul : M → M → M)
    (hnil : obs [] = e)
    (happend : ∀ x y, obs (x ++ y) = mul (obs x) (obs y))
    (hτ : ∀ A rhs, R A rhs → τ A = rhsType obs τ e mul rhs) :
    RuleFiberConsistent R obs τ := by
  intro X hX A rhs hr w hw
  change obs w = τ A
  exact (rhs_realizes_type obs τ e mul hnil happend X hX rhs w hw).trans
    (hτ A rhs hr).symm

theorem semigroup_ruleFiberConsistent {S : Type z} [Semigroup S] [Fintype S]
    (R : MixedRules N α) (T : FiniteSemigroupTyping α S) (τ : N → Option S)
    (hτ : ∀ A rhs, R A rhs → τ A = rhsType T.eval τ none freshMul rhs) :
    RuleFiberConsistent R T.eval τ :=
  ruleFiberConsistent_of_types R T.eval τ none freshMul rfl T.eval_append hτ

theorem typed_kernel_reduction_semigroup {S : Type z} [Semigroup S] [Fintype S]
    (R : MixedRules N α) (I : Set N) (T : FiniteSemigroupTyping α S)
    (τ : N → Option S) (K : N → Set (Word α))
    (hK : ∀ A, K A ⊆ fiber T.eval (τ A))
    (hτ : ∀ A rhs, R A rhs → τ A = rhsType T.eval τ none freshMul rhs) :
    SoundPrefixedPoint R I (fun A => typedClosure (grammarLanguage R I) (K A) T.eval (τ A)) ↔
    SoundPrefixedPoint R I (fun A => closure (grammarLanguage R I) (K A)) :=
  typed_kernel_spp_iff R I T.eval τ K hK (semigroup_ruleFiberConsistent R T τ hτ)

end KuriyamaMathlib
