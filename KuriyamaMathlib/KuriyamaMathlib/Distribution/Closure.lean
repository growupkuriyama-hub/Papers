import KuriyamaMathlib.Core.Observation

/-! Relational closure shared by papers 01, 02 and 09.
These definitions do not assume decidability or finiteness. -/
namespace KuriyamaMathlib

universe u v

variable {α : Type u}

/-- Common accepting contexts (right polar). -/
def frames (L K : Set (Word α)) : Set (Context α) :=
  {c | ∀ w ∈ K, c.1 ++ w ++ c.2 ∈ L}

/-- Words accepted in every supplied context (left polar). -/
def exemplars (L : Set (Word α)) (C : Set (Context α)) :
    Set (Word α) :=
  {w | ∀ c ∈ C, c.1 ++ w ++ c.2 ∈ L}

def closure (L K : Set (Word α)) : Set (Word α) :=
  exemplars L (frames L K)

def typedClosure {M : Type v} (L K : Set (Word α))
    (obs : Word α → M) (m : M) : Set (Word α) :=
  closure L K ∩ fiber obs m

theorem polar_galois (L K : Set (Word α)) (C : Set (Context α)) :
    K ⊆ exemplars L C ↔ C ⊆ frames L K := by
  constructor
  · intro h c hc w hw
    exact h hw c hc
  · intro h w hw c hc
    exact h hc w hw

theorem subset_closure (L K : Set (Word α)) : K ⊆ closure L K := by
  intro w hw c hc
  exact hc w hw

theorem frames_antitone (L : Set (Word α)) {K J : Set (Word α)}
    (h : K ⊆ J) : frames L J ⊆ frames L K := by
  intro c hc w hw
  exact hc w (h hw)

theorem typed_polar_galois {M : Type v} (L K : Set (Word α))
    (C : Set (Context α)) (obs : Word α → M) (m : M)
    (hK : K ⊆ fiber obs m) :
    K ⊆ exemplars L C ∩ fiber obs m ↔ C ⊆ frames L K := by
  constructor
  · intro h
    apply (polar_galois L K C).mp
    intro w hw
    exact (h hw).1
  · intro h w hw
    exact ⟨(polar_galois L K C).mpr h hw, hK hw⟩

theorem frames_typedClosure {M : Type v} (L K : Set (Word α))
    (obs : Word α → M) (m : M) (hK : K ⊆ fiber obs m) :
    frames L (typedClosure L K obs m) = frames L K := by
  apply Set.Subset.antisymm
  · apply frames_antitone L
    intro w hw
    exact ⟨subset_closure L K hw, hK hw⟩
  · intro c hc w hw
    exact hw.1 c hc

end KuriyamaMathlib
