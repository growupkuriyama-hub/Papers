import KuriyamaMathlib.Distribution.Closure

/-! Paper 09: typed frame/exemplar generation for individual categories.
These are not yet the grammar-wide strong/weak/very weak FCP/FKP properties;
the SPP and derivation semantics must be connected before those are defined. -/
namespace KuriyamaMathlib

universe u v

def TypedFrameGenerated {α : Type u} {M : Type v}
    (L X : Set (Word α)) (obs : Word α → M) (m : M) (k : Nat) : Prop :=
  ∃ C : Finset (Context α), C.card ≤ k ∧
    X = exemplars L (↑C : Set (Context α)) ∩ fiber obs m

def TypedKernelGenerated {α : Type u} {M : Type v}
    (L X : Set (Word α)) (obs : Word α → M) (m : M) (k : Nat) : Prop :=
  ∃ K : Finset (Word α), K.card ≤ k ∧ (↑K : Set (Word α)) ⊆ fiber obs m ∧
    X = typedClosure L (↑K : Set (Word α)) obs m

theorem typedFrameGenerated_subset_fiber {α : Type u} {M : Type v}
    {L X : Set (Word α)} {obs : Word α → M} {m : M} {k : Nat}
    (h : TypedFrameGenerated L X obs m k) : X ⊆ fiber obs m := by
  rcases h with ⟨C, _, rfl⟩
  intro w hw
  exact hw.2

theorem typedKernelGenerated_subset_fiber {α : Type u} {M : Type v}
    {L X : Set (Word α)} {obs : Word α → M} {m : M} {k : Nat}
    (h : TypedKernelGenerated L X obs m k) : X ⊆ fiber obs m := by
  rcases h with ⟨K, _, _, rfl⟩
  intro w hw
  exact hw.2

end KuriyamaMathlib
