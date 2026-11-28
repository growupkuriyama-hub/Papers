import KuriyamaMathlib.Distribution.Closure

/-! Common syntactic closure calculus. Paper 09 lem:clark, lem:typed-galois,
lem:star (binary and then arbitrary RHS in CFG/SoundPrefixedPoint). -/
namespace KuriyamaMathlib
universe u v
variable {α : Type u}

theorem frames_closure (L K : Set (Word α)) :
    frames L (closure L K) = frames L K := by
  apply Set.Subset.antisymm
  · exact frames_antitone L (subset_closure L K)
  · intro c hc w hw
    exact hw c hc

theorem subset_closure_iff (L K Y : Set (Word α)) :
    Y ⊆ closure L K ↔ frames L K ⊆ frames L Y :=
  polar_galois L Y (frames L K)

theorem closure_mono (L : Set (Word α)) {X Y : Set (Word α)}
    (h : X ⊆ Y) : closure L X ⊆ closure L Y := by
  intro w hw c hc
  exact hw c (frames_antitone L h hc)

theorem closure_idempotent (L X : Set (Word α)) :
    closure L (closure L X) = closure L X := by
  unfold closure at *
  change exemplars L (frames L (closure L X)) = exemplars L (frames L X)
  rw [frames_closure]

theorem typed_subset_closure_iff {M : Type v} (L K Y : Set (Word α))
    (obs : Word α → M) (m : M) (hY : Y ⊆ fiber obs m) :
    Y ⊆ typedClosure L K obs m ↔ frames L K ⊆ frames L Y :=
  typed_polar_galois L Y (frames L K) obs m hY

theorem typedClosure_extensive {M : Type v} (L K : Set (Word α))
    (obs : Word α → M) (m : M) (hK : K ⊆ fiber obs m) :
    K ⊆ typedClosure L K obs m := by
  intro w hw
  exact ⟨subset_closure L K hw, hK hw⟩

theorem typedClosure_mono {M : Type v} (L : Set (Word α))
    {K J : Set (Word α)} (obs : Word α → M) (m : M)
    (h : K ⊆ J) : typedClosure L K obs m ⊆ typedClosure L J obs m := by
  intro w hw
  exact ⟨closure_mono L h hw.1, hw.2⟩

theorem typedClosure_idempotent {M : Type v} (L K : Set (Word α))
    (obs : Word α → M) (m : M) (hK : K ⊆ fiber obs m) :
    typedClosure L (typedClosure L K obs m) obs m =
      typedClosure L K obs m := by
  change exemplars L (frames L (typedClosure L K obs m)) ∩ fiber obs m =
    exemplars L (frames L K) ∩ fiber obs m
  rw [frames_typedClosure L K obs m hK]

theorem typed_closed_iff_frames {M : Type v} (L X : Set (Word α))
    (obs : Word α → M) (m : M) :
    typedClosure L X obs m = X ↔
      ∃ C : Set (Context α), X = exemplars L C ∩ fiber obs m := by
  constructor
  · intro h
    exact ⟨frames L X, h.symm⟩
  · rintro ⟨C, rfl⟩
    apply Set.Subset.antisymm
    · intro w hw
      refine ⟨?_, hw.2⟩
      intro c hc
      apply hw.1 c
      intro x hx
      exact hx.1 c hc
    · apply typedClosure_extensive
      exact fun _ h => h.2

def wordProduct (X Y : Set (Word α)) : Set (Word α) :=
  {w | ∃ x ∈ X, ∃ y ∈ Y, w = x ++ y}

theorem wordProduct_mono {X Y X' Y' : Set (Word α)}
    (hx : X ⊆ X') (hy : Y ⊆ Y') :
    wordProduct X Y ⊆ wordProduct X' Y' := by
  rintro w ⟨x, h1, y, h2, rfl⟩
  exact ⟨x, hx h1, y, hy h2, rfl⟩

theorem closure_product_subset (L X Y : Set (Word α)) :
    wordProduct (closure L X) (closure L Y) ⊆ closure L (wordProduct X Y) := by
  rintro w ⟨x, hx, y, hy, rfl⟩
  intro c hc
  have hxctx : (c.1, y ++ c.2) ∈ frames L X := by
    intro a ha
    have hyctx : (c.1 ++ a, c.2) ∈ frames L Y := by
      intro b hb
      have hp := hc (a ++ b) ⟨a, ha, b, hb, rfl⟩
      simpa only [List.append_assoc] using hp
    have hp := hy (c.1 ++ a, c.2) hyctx
    simpa only [List.append_assoc] using hp
  have hp := hx (c.1, y ++ c.2) hxctx
  simpa only [List.append_assoc] using hp

theorem frames_eq_of_sandwich (L : Set (Word α)) {X Y : Set (Word α)}
    (h₁ : X ⊆ Y) (h₂ : Y ⊆ closure L X) :
    frames L Y = frames L X := by
  apply Set.Subset.antisymm
  · exact frames_antitone L h₁
  · intro c hc
    intro w hw
    exact h₂ hw c hc

theorem closure_singleton_subset_language (L : Set (Word α)) (w : Word α)
    (hw : w ∈ L) : closure L {w} ⊆ L := by
  intro x hx
  have hc : (([], []) : Context α) ∈ frames L ({w} : Set (Word α)) := by
    intro y hy
    have he : y = w := hy
    simpa [he] using hw
  simpa using hx ([], []) hc

end KuriyamaMathlib
