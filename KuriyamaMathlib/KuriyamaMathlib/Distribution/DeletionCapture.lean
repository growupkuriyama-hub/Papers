import KuriyamaMathlib.Distribution.Calculus

/-! One-word deletion and local kernel capture (09 lem:one-word,
lem:capture), independent of a particular grammar or observer. -/
namespace KuriyamaMathlib
universe u
variable {α : Type u}

def CaptureCondition (L : Set (Word α)) (R T T₀ : Word α) : Prop :=
  ∀ y : Word α, (y ++ T ∈ L ∧ y ++ T₀ ∉ L) ↔ y = R

theorem one_word_deletion_capture (L : Set (Word α)) (R T T₀ : Word α)
    (hw : R ++ T₀ ∈ L) (hz : R ++ T ∈ L) (hne : T ≠ T₀)
    (hreplace : ∀ y : Word α, y ++ T ∈ L → y ++ T₀ ∈ L) :
    R ++ T ∈ L \ {R ++ T₀} ∧
    CaptureCondition (L \ {R ++ T₀}) R T T₀ := by
  have hdiff : R ++ T ≠ R ++ T₀ := by
    intro h
    exact hne (List.append_cancel_left h)
  have hzm : R ++ T ∈ L \ {R ++ T₀} := ⟨hz, hdiff⟩
  refine ⟨hzm, ?_⟩
  intro y
  constructor
  · rintro ⟨hy, hn⟩
    have he : y ++ T₀ = R ++ T₀ := by
      by_contra hh
      exact hn ⟨hreplace y hy.1, hh⟩
    exact List.append_cancel_right he
  · rintro rfl
    exact ⟨hzm, fun h => h.2 rfl⟩

/-- The language-theoretic heart of lem:capture. A calling grammar must
supply the genuine reaching-context property and occurrence split. -/
theorem kernel_capture (L K : Set (Word α)) (R T T₀ p x q₀ : Word α)
    (hc : CaptureCondition L R T T₀)
    (hR : p ++ x ++ q₀ = R)
    (hx : x ∈ closure L K)
    (hreach : ∀ e ∈ K, p ++ e ++ q₀ ++ T ∈ L) :
    x ∈ K := by
  classical
  have hbad : R ++ T₀ ∉ L := ((hc R).mpr rfl).2
  have hbadx : p ++ x ++ (q₀ ++ T₀) ∉ L := by
    simpa only [← List.append_assoc, hR] using hbad
  have hn : (p, q₀ ++ T₀) ∉ frames L K := by
    intro h
    exact hbadx (hx (p, q₀ ++ T₀) h)
  have he : ∃ e ∈ K, p ++ e ++ (q₀ ++ T₀) ∉ L := by
    by_contra h
    apply hn
    intro e he
    by_contra hnot
    exact h ⟨e, he, hnot⟩
  rcases he with ⟨e, heK, hebad⟩
  have hey : p ++ e ++ q₀ = R :=
    (hc (p ++ e ++ q₀)).mp ⟨hreach e heK, by
      simpa only [List.append_assoc] using hebad⟩
  have heq : p ++ e ++ q₀ = p ++ x ++ q₀ := hey.trans hR.symm
  have ex : e = x := List.append_cancel_left (List.append_cancel_right heq)
  simpa only [ex] using heK

end KuriyamaMathlib
