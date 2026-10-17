import TCSPhase3CSynchronization
import TCSPhase3Congruence

namespace TCSPhase3
open TCSPhase1 TCSPhase2

/-- Every actual CFG word has an initial terminal. -/
theorem language_word_nonempty (i : Nat) (w : Word)
    (hw : w ∈ TCSPhase2.Language i) : w ≠ [] := by
  intro he
  subst w
  cases language_opening_prefix i [] hw

/-- The precise Appendix C path-congruence property, independent of
common-context assumptions: equal endpoints of parser runs imply equal
distributions. Induction is on the sum of both input lengths. -/
theorem path_congruence (n : Nat) :
    ∀ (σ θ : Stack) (x y : Word),
      Run n σ x θ → Run n σ y θ →
      Distributions (TCSPhase2.Language n) x =
        Distributions (TCSPhase2.Language n) y := by
  have core : ∀ m : Nat, ∀ (σ θ : Stack) (x y : Word),
        x.length + y.length = m →
        Run n σ x θ → Run n σ y θ →
        Distributions (TCSPhase2.Language n) x =
          Distributions (TCSPhase2.Language n) y := by
    intro m
    induction m using Nat.strong_induction_on with
    | h m ih =>
        intro σ θ x y hm hx hy
        cases x with
        | nil =>
            cases hx
            have hyempty := run_no_nonempty_cycle hy
            subst y
            rfl
        | cons c xs =>
            cases y with
            | nil =>
                cases hy
                have hxempty := run_no_nonempty_cycle hx
                contradiction
            | cons d ys =>
                cases hx with
                | next hsc hrx =>
                    cases hy with
                    | next hsd hry =>
                        by_cases heq : c = d
                        · subst d
                          have heqState := step_deterministic hsc hsd
                          cases heqState
                          have hsmall : xs.length + ys.length < m := by
                            simp only [List.length_cons] at hm
                            omega
                          have htail := ih (xs.length + ys.length) hsmall
                            _ _ xs ys rfl hrx hry
                          simpa using distributions_left_congruent
                            (TCSPhase2.Language n) xs ys [c] htail
                        · obtain ⟨i, ψ, w, w', xr, yr, hmin, hi,
                            hσ, hxsplit, hysplit, hw, hw', hrunx, hruny⟩ :=
                            branch_synchronization heq
                              (Run.next hsc hrx) (Run.next hsd hry)
                          have hwne : w ≠ [] := language_word_nonempty i w hw
                          have hw'ne : w' ≠ [] := language_word_nonempty i w' hw'
                          have hsmall : xr.length + yr.length < m := by
                            have hxlen := congrArg List.length hxsplit
                            have hylen := congrArg List.length hysplit
                            simp only [List.length_cons, List.length_append] at hxlen hylen
                            simp only [List.length_cons] at hm
                            have hwp : 0 < w.length := by
                              cases w with
                              | nil => contradiction
                              | cons _ _ => simp
                            have hw'p : 0 < w'.length := by
                              cases w' with
                              | nil => contradiction
                              | cons _ _ => simp
                            omega
                          have htail := ih (xr.length + yr.length) hsmall
                            ψ θ xr yr rfl hrunx hruny
                          have hsubtrees :=
                            complete_subtree_exchange n i hi w w' hw hw'
                          calc
                            Distributions (TCSPhase2.Language n) (c :: xs)
                                = Distributions (TCSPhase2.Language n) (w ++ xr) := by
                                    rw [hxsplit]
                            _ = Distributions (TCSPhase2.Language n) (w' ++ xr) :=
                                  distributions_right_congruent
                                    (TCSPhase2.Language n) w w' xr hsubtrees
                            _ = Distributions (TCSPhase2.Language n) (w' ++ yr) :=
                                  distributions_left_congruent
                                    (TCSPhase2.Language n) xr yr w' htail
                            _ = Distributions (TCSPhase2.Language n) (d :: ys) := by
                                    rw [hysplit]
  intro σ θ x y hx hy
  exact core (x.length + y.length) σ θ x y rfl hx hy

#print axioms TCSPhase3.language_word_nonempty
#print axioms TCSPhase3.path_congruence
end TCSPhase3
