import KuriyamaMathlib.Distribution.Calculus
import LeanCfgProject.TCS1.LeastClosedCFGLanguage

/-! Shared arbitrary mixed-RHS semantics, using the existing 01 grammar kernel.
Finite CFGs instantiate this more general relational interface. -/
namespace KuriyamaMathlib
open LeanCfgProject.TCS1
universe u v
variable {α : Type u} {N : Type v}

def rhsSet (X : N → Set (Word α)) (rhs : List (MixedSymbol N α)) :
    Set (Word α) := {w | RhsRealizes X rhs w}

def symbolSet (X : N → Set (Word α)) : MixedSymbol N α → Set (Word α)
  | .inl A => X A
  | .inr a => {[a]}

theorem rhsSet_cons (X : N → Set (Word α)) (s : MixedSymbol N α)
    (rhs : List (MixedSymbol N α)) :
    rhsSet X (s :: rhs) = wordProduct (symbolSet X s) (rhsSet X rhs) := by
  cases s with
  | inl A =>
    ext w
    constructor
    · rintro ⟨x, y, h, hx, hy⟩
      exact ⟨x, hx, y, hy, h⟩
    · rintro ⟨x, hx, y, hy, h⟩
      exact ⟨x, y, h, hx, hy⟩
  | inr a =>
    ext w
    constructor
    · rintro ⟨t, rfl, ht⟩
      exact ⟨[a], rfl, t, ht, rfl⟩
    · rintro ⟨x, hx, t, ht, rfl⟩
      have he : x = [a] := hx
      subst x
      exact ⟨t, rfl, ht⟩

theorem rhsSet_mono {X Y : N → Set (Word α)}
    (h : ∀ A, X A ⊆ Y A) (rhs : List (MixedSymbol N α)) :
    rhsSet X rhs ⊆ rhsSet Y rhs := by
  intro w hw
  exact rhsRealizes_mono h hw

/-- Arbitrarily many nonterminal occurrences, including zero and epsilon. -/
theorem rhsSet_closure_subset (L : Set (Word α)) (X : N → Set (Word α))
    (rhs : List (MixedSymbol N α)) :
    rhsSet (fun A => closure L (X A)) rhs ⊆ closure L (rhsSet X rhs) := by
  induction rhs with
  | nil =>
    intro w hw
    exact subset_closure L (rhsSet X []) hw
  | cons s rhs ih =>
    rw [rhsSet_cons, rhsSet_cons]
    have hs : symbolSet (fun A => closure L (X A)) s ⊆ closure L (symbolSet X s) := by
      cases s with
      | inl A => exact fun _ h => h
      | inr a => exact subset_closure L _
    exact (wordProduct_mono hs ih).trans (closure_product_subset L _ _)

theorem rhs_frames_insensitive (L : Set (Word α)) (X Y : N → Set (Word α))
    (h₁ : ∀ A, X A ⊆ Y A) (h₂ : ∀ A, Y A ⊆ closure L (X A))
    (rhs : List (MixedSymbol N α)) :
    frames L (rhsSet Y rhs) = frames L (rhsSet X rhs) := by
  apply frames_eq_of_sandwich L (rhsSet_mono h₁ rhs)
  exact (rhsSet_mono h₂ rhs).trans (rhsSet_closure_subset L X rhs)

def initialLanguage (I : Set N) (X : N → Set (Word α)) : Set (Word α) :=
  {w | ∃ A ∈ I, w ∈ X A}

def grammarLanguage (R : MixedRules N α) (I : Set N) : Set (Word α) :=
  initialLanguage I (LeastClosedLanguage R)

def SoundPrefixedPoint (R : MixedRules N α) (I : Set N)
    (X : N → Set (Word α)) : Prop :=
  GrammarClosed R X ∧ initialLanguage I X = grammarLanguage R I

theorem leastClosed_subset (R : MixedRules N α) {X : N → Set (Word α)}
    (h : GrammarClosed R X) (A : N) : LeastClosedLanguage R A ⊆ X A := by
  intro w hw
  exact hw X h

theorem spp_iff (R : MixedRules N α) (I : Set N) (X : N → Set (Word α)) :
    SoundPrefixedPoint R I X ↔
      GrammarClosed R X ∧ ∀ A ∈ I, X A ⊆ grammarLanguage R I := by
  constructor
  · rintro ⟨hc, he⟩
    refine ⟨hc, ?_⟩
    intro A hA w hw
    rw [← he]
    exact ⟨A, hA, hw⟩
  · rintro ⟨hc, hs⟩
    refine ⟨hc, Set.Subset.antisymm ?_ ?_⟩
    · rintro w ⟨A, hA, hw⟩
      exact hs A hA hw
    · rintro w ⟨A, hA, hw⟩
      exact ⟨A, hA, leastClosed_subset R hc A hw⟩

/-- Exact closure family on the same grammar is an SPP whenever X is.
The context argument includes the empty context at initial symbols. -/
theorem closure_spp (R : MixedRules N α) (I : Set N)
    (X : N → Set (Word α)) (h : SoundPrefixedPoint R I X) :
    SoundPrefixedPoint R I (fun A => closure (grammarLanguage R I) (X A)) := by
  let L := grammarLanguage R I
  have hp := (spp_iff R I X).mp h
  apply (spp_iff R I _).mpr
  constructor
  · intro A w hw
    rcases hw with ⟨rhs, hr, hw⟩
    have hsub : rhsSet X rhs ⊆ X A := fun z hz => hp.1 A ⟨rhs, hr, hz⟩
    exact closure_mono L hsub (rhsSet_closure_subset L X rhs hw)
  · intro A hA w hw
    have hc : (([], []) : Context α) ∈ frames L (X A) := by
      intro z hz
      simpa using hp.2 A hA hz
    simpa using hw ([], []) hc

end KuriyamaMathlib
