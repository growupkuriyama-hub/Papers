import KuriyamaMathlib.CFG.SoundPrefixedPoint

/-! Shared semantic version of Paper 09's Kernel Reduction Lemma.
RuleFiberConsistent is the semantic obligation of typed productions;
the multiplicative-observation bridge is separate. -/
namespace KuriyamaMathlib
open LeanCfgProject.TCS1
universe u v z
variable {α : Type u} {N : Type v} {M : Type z}

def RuleFiberConsistent (R : MixedRules N α) (obs : Word α → M)
    (τ : N → M) : Prop :=
  ∀ (X : N → Set (Word α)), (∀ A, X A ⊆ fiber obs (τ A)) →
    ∀ A rhs, R A rhs → rhsSet X rhs ⊆ fiber obs (τ A)

theorem closed_iff_rules (R : MixedRules N α) (X : N → Set (Word α)) :
    GrammarClosed R X ↔ ∀ A rhs, R A rhs → rhsSet X rhs ⊆ X A := by
  constructor
  · intro h A rhs hr w hw
    exact h A ⟨rhs, hr, hw⟩
  · intro h A w hw
    rcases hw with ⟨rhs, hr, hw⟩
    exact h A rhs hr hw

theorem typed_kernel_closed_iff (R : MixedRules N α)
    (L : Set (Word α)) (obs : Word α → M) (τ : N → M)
    (K : N → Set (Word α)) (hK : ∀ A, K A ⊆ fiber obs (τ A))
    (hR : RuleFiberConsistent R obs τ) :
    GrammarClosed R (fun A => typedClosure L (K A) obs (τ A)) ↔
    GrammarClosed R (fun A => closure L (K A)) := by
  let X : N → Set (Word α) := fun A => typedClosure L (K A) obs (τ A)
  let Y : N → Set (Word α) := fun A => closure L (K A)
  have hX : ∀ A, X A ⊆ fiber obs (τ A) := fun A _ hw => hw.2
  have hKX : ∀ A, K A ⊆ X A := fun A => typedClosure_extensive L (K A) obs (τ A) (hK A)
  have hXY : ∀ A, X A ⊆ Y A := fun A _ hw => hw.1
  have hKY : ∀ A, K A ⊆ Y A := fun A => subset_closure L (K A)
  change GrammarClosed R X ↔ GrammarClosed R Y
  rw [closed_iff_rules, closed_iff_rules]
  constructor
  · intro h A rhs hr
    have hf := rhs_frames_insensitive L K X hKX hXY rhs
    have hg := rhs_frames_insensitive L K Y hKY (fun _ _ hw => hw) rhs
    have hp := (typed_subset_closure_iff L (K A) (rhsSet X rhs) obs (τ A)
      (hR X hX A rhs hr)).mp (h A rhs hr)
    apply (subset_closure_iff L (K A) (rhsSet Y rhs)).mpr
    rw [hg, ← hf]
    exact hp
  · intro h A rhs hr
    have hf := rhs_frames_insensitive L K X hKX hXY rhs
    have hg := rhs_frames_insensitive L K Y hKY (fun _ _ hw => hw) rhs
    have hp := (subset_closure_iff L (K A) (rhsSet Y rhs)).mp (h A rhs hr)
    apply (typed_subset_closure_iff L (K A) (rhsSet X rhs) obs (τ A)
      (hR X hX A rhs hr)).mpr
    rw [hf, ← hg]
    exact hp

theorem closure_subset_target_iff (L K : Set (Word α)) :
    closure L K ⊆ L ↔ K ⊆ L := by
  constructor
  · intro h
    exact (subset_closure L K).trans h
  · intro h w hw
    have hc : (([], []) : Context α) ∈ frames L K := by
      intro x hx
      simpa using h hx
    simpa using hw ([], []) hc

theorem typed_kernel_spp_iff (R : MixedRules N α) (I : Set N)
    (obs : Word α → M) (τ : N → M) (K : N → Set (Word α))
    (hK : ∀ A, K A ⊆ fiber obs (τ A)) (hR : RuleFiberConsistent R obs τ) :
    SoundPrefixedPoint R I (fun A => typedClosure (grammarLanguage R I) (K A) obs (τ A)) ↔
    SoundPrefixedPoint R I (fun A => closure (grammarLanguage R I) (K A)) := by
  let L := grammarLanguage R I
  rw [spp_iff, spp_iff]
  constructor
  · rintro ⟨hc, hs⟩
    refine ⟨(typed_kernel_closed_iff R L obs τ K hK hR).mp hc, ?_⟩
    intro A hA
    apply (closure_subset_target_iff L (K A)).mpr
    exact (typedClosure_extensive L (K A) obs (τ A) (hK A)).trans (hs A hA)
  · rintro ⟨hc, hs⟩
    refine ⟨(typed_kernel_closed_iff R L obs τ K hK hR).mpr hc, ?_⟩
    intro A hA w hw
    exact hs A hA hw.1

end KuriyamaMathlib
