import TCSPhase2Bridge

namespace TCSPhase3
open TCSPhase1 TCSPhase2

/-- Top-of-stack is the first element. -/
inductive Frame where
  | nt (i : Nat)
  | ceilClose
  | floorClose
  deriving DecidableEq, Repr

abbrev Stack := List Frame

/-- Appendix C's five transitions, with 1 ≤ i ≤ bound in both expansions. -/
inductive Step (bound : Nat) : Stack → Terminal → Stack → Prop
  | atom (tail : Stack) :
      Step bound (Frame.nt 0 :: tail) Terminal.a tail
  | unary (i : Nat) (hi : i + 1 ≤ bound) (tail : Stack) :
      Step bound (Frame.nt (i + 1) :: tail) Terminal.squareLeft
        (Frame.nt i :: Frame.ceilClose :: tail)
  | binary (i : Nat) (hi : i + 1 ≤ bound) (tail : Stack) :
      Step bound (Frame.nt (i + 1) :: tail) Terminal.left
        (Frame.nt i :: Frame.nt i :: Frame.floorClose :: tail)
  | ceilPop (tail : Stack) :
      Step bound (Frame.ceilClose :: tail) Terminal.squareRight tail
  | floorPop (tail : Stack) :
      Step bound (Frame.floorClose :: tail) Terminal.right tail

/-- A run reads a word independently of CFG derivation. -/
inductive Run (bound : Nat) : Stack → Word → Stack → Prop
  | nil (s : Stack) : Run bound s [] s
  | next {s t u : Stack} {c : Terminal} {w : Word}
      (head : Step bound s c t) (tail : Run bound t w u) :
      Run bound s (c :: w) u

theorem run_empty (bound : Nat) (s : Stack) : Run bound s [] s :=
  Run.nil s

theorem step_deterministic {bound : Nat} {s t u : Stack} {c : Terminal}
    (h : Step bound s c t) (h' : Step bound s c u) : t = u := by
  cases h <;> cases h' <;> rfl

theorem step_reverse_injective {bound : Nat} {s t u : Stack} {c : Terminal}
    (h : Step bound s c u) (h' : Step bound t c u) : s = t := by
  cases h <;> cases h' <;> rfl

theorem run_append {bound : Nat} {s t u : Stack} {x y : Word}
    (hx : Run bound s x t) (hy : Run bound t y u) :
    Run bound s (x ++ y) u := by
  induction hx with
  | nil _ => simpa using hy
  | next hs hr ih => exact Run.next hs ih

theorem run_append_split {bound : Nat} {s t : Stack} (x y : Word)
    (h : Run bound s (x ++ y) t) :
    ∃ mid : Stack, Run bound s x mid ∧ Run bound mid y t := by
  induction x generalizing s with
  | nil => exact ⟨s, Run.nil s, by simpa using h⟩
  | cons c rest ih =>
      change Run bound s (c :: (rest ++ y)) t at h
      cases h with
      | next hs hr =>
          obtain ⟨mid, hleft, hright⟩ := ih hr
          exact ⟨mid, Run.next hs hleft, hright⟩

theorem run_deterministic {bound : Nat} {s t u : Stack} {w : Word}
    (h : Run bound s w t) (h' : Run bound s w u) : t = u := by
  induction h generalizing u with
  | nil _ => cases h'; rfl
  | next hs hr ih =>
      cases h' with
      | next hs' hr' =>
          have hm := step_deterministic hs hs'
          cases hm
          exact ih hr'

theorem run_reverse_injective {bound : Nat} {s t u : Stack} {w : Word}
    (h : Run bound s w u) (h' : Run bound t w u) : s = t := by
  induction w generalizing s t with
  | nil =>
      cases h
      cases h'
      rfl
  | cons c rest ih =>
      cases h with
      | next hs hr =>
          cases h' with
          | next hs' hr' =>
              have hm := ih hr hr'
              cases hm
              exact step_reverse_injective hs hs'

theorem step_suffix {bound : Nat} {s t : Stack} {c : Terminal}
    (h : Step bound s c t) (suffix : Stack) :
    Step bound (s ++ suffix) c (t ++ suffix) := by
  cases h with
  | atom tail => simpa using (Step.atom (bound := bound) (tail ++ suffix))
  | unary i hi tail =>
      simpa using (Step.unary (bound := bound) i hi (tail ++ suffix))
  | binary i hi tail =>
      simpa using (Step.binary (bound := bound) i hi (tail ++ suffix))
  | ceilPop tail =>
      simpa using (Step.ceilPop (bound := bound) (tail ++ suffix))
  | floorPop tail =>
      simpa using (Step.floorPop (bound := bound) (tail ++ suffix))

theorem run_suffix {bound : Nat} {s t : Stack} {w : Word}
    (h : Run bound s w t) (suffix : Stack) :
    Run bound (s ++ suffix) w (t ++ suffix) := by
  induction h with
  | nil s => exact Run.nil (s ++ suffix)
  | next hs hr ih => exact Run.next (step_suffix hs suffix) ih

def frameWeight : Frame → Nat
  | .nt i => 4 ^ i
  | .ceilClose | .floorClose => 1

def weight : Stack → Nat
  | [] => 0
  | s :: ss => frameWeight s + weight ss

theorem step_weight_lt {bound : Nat} {s t : Stack} {c : Terminal}
    (h : Step bound s c t) : weight t < weight s := by
  cases h with
  | atom tail => simp [weight, frameWeight]
  | ceilPop tail => simp [weight, frameWeight]
  | floorPop tail => simp [weight, frameWeight]
  | unary i hi tail =>
      change 4 ^ i + (1 + weight tail) <
        4 ^ (i + 1) + weight tail
      rw [pow_succ]
      have hp : 0 < 4 ^ i := pow_pos (by omega : (0 : Nat) < 4) i
      omega
  | binary i hi tail =>
      change 4 ^ i + (4 ^ i + (1 + weight tail)) <
        4 ^ (i + 1) + weight tail
      rw [pow_succ]
      have hp : 0 < 4 ^ i := pow_pos (by omega : (0 : Nat) < 4) i
      omega

theorem run_weight_le {bound : Nat} {s t : Stack} {w : Word}
    (h : Run bound s w t) : weight t ≤ weight s := by
  induction h with
  | nil _ => exact le_rfl
  | next hs hr ih => exact ih.trans (Nat.le_of_lt (step_weight_lt hs))

theorem run_weight_lt {bound : Nat} {s t : Stack} {w : Word}
    (h : Run bound s w t) (hw : w ≠ []) : weight t < weight s := by
  cases h with
  | nil _ => contradiction
  | next hs hr =>
      exact lt_of_le_of_lt (run_weight_le hr) (step_weight_lt hs)

theorem run_no_nonempty_cycle {bound : Nat} {s : Stack} {w : Word}
    (h : Run bound s w s) : w = [] := by
  by_contra hn
  have hp := run_weight_lt h hn
  omega

#print axioms TCSPhase3.step_deterministic
#print axioms TCSPhase3.step_reverse_injective
#print axioms TCSPhase3.run_append
#print axioms TCSPhase3.run_append_split
#print axioms TCSPhase3.run_deterministic
#print axioms TCSPhase3.run_reverse_injective
#print axioms TCSPhase3.step_suffix
#print axioms TCSPhase3.run_suffix
#print axioms TCSPhase3.step_weight_lt
#print axioms TCSPhase3.run_no_nonempty_cycle

end TCSPhase3
