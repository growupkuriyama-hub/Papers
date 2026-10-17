import TCSPhase3CAux

namespace TCSPhase3
open TCSPhase1 TCSPhase2

/-- The residual stacks after opposite initial branches cannot finish
at the same state without both first consuming their protected suffix. -/
theorem opposite_branches_both_visit {bound i : Nat} {ψ θ : Stack}
    {x y : Word}
    (hx : Run bound (Frame.nt i :: Frame.ceilClose :: ψ) x θ)
    (hy : Run bound
      (Frame.nt i :: Frame.nt i :: Frame.floorClose :: ψ) y θ) :
    ∃ u v xr yr : Word,
      x = u ++ xr ∧ y = v ++ yr ∧
      Run bound [Frame.nt i, Frame.ceilClose] u [] ∧
      Run bound [Frame.nt i, Frame.nt i, Frame.floorClose] v [] ∧
      Run bound ψ xr θ ∧ Run bound ψ yr θ := by
  have hx' : Run bound ([Frame.nt i, Frame.ceilClose] ++ ψ) x θ := by
    simpa using hx
  have hy' : Run bound ([Frame.nt i, Frame.nt i, Frame.floorClose] ++ ψ) y θ := by
    simpa using hy
  rcases classified_first_visit (α := [Frame.nt i, Frame.ceilClose])
      (ψ := ψ) (by simp) hx' with hxu | hxu
  · obtain ⟨βx, hβx, hrunx, hθx, hwtx⟩ := hxu
    rcases classified_first_visit (α := [Frame.nt i, Frame.nt i, Frame.floorClose])
        (ψ := ψ) (by simp) hy' with hyu | hyv
    · obtain ⟨βy, hβy, hruny, hθy, hwty⟩ := hyu
      obtain ⟨γx, hγx⟩ :=
        run_preserves_last_marker
          (m := Frame.ceilClose) (α := [Frame.nt i])
          (Or.inl rfl) (by simpa using hrunx) hβx
      obtain ⟨γy, hγy⟩ :=
        run_preserves_last_marker
          (m := Frame.floorClose) (α := [Frame.nt i, Frame.nt i])
          (Or.inr rfl) (by simpa using hruny) hβy
      have he : βx = βy :=
        suffix_cancel_right βx βy ψ (hθx.symm.trans hθy)
      rw [hγx, hγy] at he
      exact False.elim (ceil_floor_suffix_ne γx γy he)
    · obtain ⟨v, yr, hey, hruny, hyrest, hwty⟩ := hyv
      omega
  · obtain ⟨u, xr, hex, hrunx, hxrest, hwtx⟩ := hxu
    rcases classified_first_visit (α := [Frame.nt i, Frame.nt i, Frame.floorClose])
        (ψ := ψ) (by simp) hy' with hyu | hyv
    · obtain ⟨βy, hβy, hruny, hθy, hwty⟩ := hyu
      omega
    · obtain ⟨v, yr, hey, hruny, hyrest, hwty⟩ := hyv
      exact ⟨u, v, xr, yr, hex, hey, hrunx, hruny, hxrest, hyrest⟩

/-- Opposite opening moves synchronize at complete L_{i+1} subtrees. -/
theorem oriented_branch_synchronization (bound i : Nat)
    (hi : i + 1 ≤ bound) (ψ θ : Stack) (x y : Word)
    (hx : Run bound (Frame.nt i :: Frame.ceilClose :: ψ) x θ)
    (hy : Run bound (Frame.nt i :: Frame.nt i :: Frame.floorClose :: ψ) y θ) :
    ∃ w w' xr yr : Word,
      Terminal.squareLeft :: x = w ++ xr ∧
      Terminal.left :: y = w' ++ yr ∧
      w ∈ Language (i + 1) ∧ w' ∈ Language (i + 1) ∧
      Run bound ψ xr θ ∧ Run bound ψ yr θ := by
  obtain ⟨u, v, xr, yr, hxsplit, hysplit, hrunx, hruny, hrestx, hresty⟩ :=
    opposite_branches_both_visit hx hy
  have hrunx' : Run bound (Frame.nt i :: Frame.ceilClose :: ψ) u ψ := by
    simpa using run_suffix hrunx ψ
  have hruny' :
      Run bound (Frame.nt i :: Frame.nt i :: Frame.floorClose :: ψ) v ψ := by
    simpa using run_suffix hruny ψ
  have hxl : (Terminal.squareLeft :: u) ∈ Language (i + 1) :=
    recognition_converse bound (i + 1) ψ _ hi
      (Run.next (Step.unary i hi ψ) hrunx')
  have hyl : (Terminal.left :: v) ∈ Language (i + 1) :=
    recognition_converse bound (i + 1) ψ _ hi
      (Run.next (Step.binary i hi ψ) hruny')
  refine ⟨Terminal.squareLeft :: u, Terminal.left :: v, xr, yr,
    ?_, ?_, hxl, hyl, hrestx, hresty⟩
  · simp [hxsplit]
  · simp [hysplit]

/-- Appendix C branch synchronization, without any substitutability premise. -/
theorem branch_synchronization {bound : Nat} {σ θ : Stack}
    {c d : Terminal} {x y : Word}
    (hc : c ≠ d) (hx : Run bound σ (c :: x) θ)
    (hy : Run bound σ (d :: y) θ) :
    ∃ (i : Nat) (ψ : Stack) (w w' xr yr : Word),
      1 ≤ i ∧ i ≤ bound ∧ σ = Frame.nt i :: ψ ∧
      c :: x = w ++ xr ∧ d :: y = w' ++ yr ∧
      w ∈ Language i ∧ w' ∈ Language i ∧
      Run bound ψ xr θ ∧ Run bound ψ yr θ := by
  cases hx with
  | next hs hxr =>
      cases hy with
      | next ht hyr =>
          obtain ⟨i, ψ, hi, hσ, hcases⟩ :=
            distinct_initial_steps hc hs ht
          rcases hcases with hleft | hright
          · obtain ⟨rfl, htargetx, rfl, htargety⟩ := hleft
            rw [htargetx] at hxr
            rw [htargety] at hyr
            obtain ⟨w,w',xr,yr,hxs,hys,hw,hw',hrx,hry⟩ :=
              oriented_branch_synchronization bound i hi ψ θ x y hxr hyr
            exact ⟨i+1,ψ,w,w',xr,yr,by omega,hi,hσ,hxs,hys,hw,hw',hrx,hry⟩
          · obtain ⟨rfl, htargetx, rfl, htargety⟩ := hright
            rw [htargetx] at hxr
            rw [htargety] at hyr
            obtain ⟨w,w',xr,yr,hys,hxs,hw,hw',hry,hrx⟩ :=
              oriented_branch_synchronization bound i hi ψ θ y x hyr hxr
            exact ⟨i+1,ψ,w',w,yr,xr,by omega,hi,hσ,hxs,hys,hw',hw,hrx,hry⟩

#print axioms TCSPhase3.opposite_branches_both_visit
#print axioms TCSPhase3.oriented_branch_synchronization
#print axioms TCSPhase3.branch_synchronization

end TCSPhase3
