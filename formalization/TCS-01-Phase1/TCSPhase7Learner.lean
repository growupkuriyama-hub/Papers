import TCSPhase7Texts
import TCSPhase5FiniteDerivation

/-! A conservative learner with syntactically distinguishable finite B/U/L/S
hypotheses. The initial object is a fixed no-production grammar, whereas any
reconstruction records the full observed sample used for its finite grammar. -/
namespace TCSPhase7
open TCSPhase5

variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet] [Monoid M]

inductive Hypothesis (Alphabet : Type*) where
  | initial : Hypothesis Alphabet
  | reconstructed (sample : Finset (List Alphabet)) : Hypothesis Alphabet

/-- Actual finite reconstruction grammar attached to each hypothesis. -/
noncomputable def hypothesisGrammar (h : List Alphabet →* M) :
    Hypothesis Alphabet → RecGrammar Alphabet
  | .initial => makeRecGrammar h ∅
  | .reconstructed K => makeRecGrammar h K

/-- The distinguished initial hypothesis represents the empty language. -/
def hypothesisLanguage (h : List Alphabet →* M) :
    Hypothesis Alphabet → Set (List Alphabet)
  | .initial => ∅
  | .reconstructed K => RecLanguage h K

theorem reconstructed_language_iff (h : List Alphabet →* M)
    (K : Finset (List Alphabet)) (w : List Alphabet) :
    w ∈ hypothesisLanguage h (.reconstructed K) ↔
      FiniteRecStartDerives h K w :=
  (finite_rec_language_iff h K w).symm

/-- There are no start productions in the designated initial finite CFG. -/
theorem initial_grammar_no_start (h : List Alphabet →* M) :
    (hypothesisGrammar h .initial).startRules = ∅ ∧
    (hypothesisGrammar h .initial).startEmpty = false := by
  classical
  simp [hypothesisGrammar, makeRecGrammar]

/-- The actual conservative recursion uses all data observed through step n. -/
noncomputable def learner (h : List Alphabet →* M)
    (T : Nat → List Alphabet) : Nat → Hypothesis Alphabet := by
  classical
  exact Nat.rec .initial (fun n H =>
    if T n ∈ hypothesisLanguage h H then H
    else .reconstructed (observed T (n+1)))

theorem learner_zero (h : List Alphabet →* M) (T : Nat → List Alphabet) :
    learner h T 0 = .initial := rfl

theorem learner_step (h : List Alphabet →* M)
    (T : Nat → List Alphabet) (n : Nat) :
    learner h T (n+1) =
      if T n ∈ hypothesisLanguage h (learner h T n) then learner h T n
      else .reconstructed (observed T (n+1)) := rfl

/-- A rebuild is an event, not an assumption that the two CFGs are distinct. -/
def RebuildAt (h : List Alphabet →* M)
    (T : Nat → List Alphabet) (n : Nat) : Prop :=
  T n ∉ hypothesisLanguage h (learner h T n)

theorem learner_conservative (h : List Alphabet →* M)
    (T : Nat → List Alphabet) (n : Nat)
    (hmem : T n ∈ hypothesisLanguage h (learner h T n)) :
    learner h T (n+1) = learner h T n := by
  rw [learner_step]
  exact if_pos hmem

theorem learner_rebuild (h : List Alphabet →* M)
    (T : Nat → List Alphabet) (n : Nat)
    (hmiss : RebuildAt h T n) :
    learner h T (n+1) = .reconstructed (observed T (n+1)) := by
  rw [learner_step]
  exact if_neg hmiss

/-- A syntactic change can happen only on a missed positive datum. -/
theorem change_implies_rebuild (h : List Alphabet →* M)
    (T : Nat → List Alphabet) (n : Nat)
    (hchange : learner h T (n+1) ≠ learner h T n) :
    RebuildAt h T n := by
  intro hmem
  exact hchange (learner_conservative h T n hmem)

/-- Even an epsilon-only text rebuilds at its very first input. -/
theorem first_rebuild (h : List Alphabet →* M)
    (T : Nat → List Alphabet) : RebuildAt h T 0 := by
  simp [RebuildAt, learner_zero, hypothesisLanguage]

/-- All observed data belong to the current actual hypothesis language. -/
theorem learner_sample_consistency (h : List Alphabet →* M)
    (T : Nat → List Alphabet) :
    ∀ n : Nat, (↑(observed T n) : Set (List Alphabet)) ⊆
      hypothesisLanguage h (learner h T n) := by
  intro n
  induction n with
  | zero =>
      simp [observed_zero]
  | succ n ih =>
      intro w hw
      by_cases hmem : T n ∈ hypothesisLanguage h (learner h T n)
      · have hkeep := learner_conservative h T n hmem
        rw [hkeep]
        rw [observed_succ] at hw
        rcases Finset.mem_insert.mp hw with heq | hprev
        · subst w
          exact hmem
        · exact ih hprev
      · have hstep := learner_rebuild h T n hmem
        rw [hstep]
        exact rec_sample_consistency h (observed T (n+1)) hw

/-- Every learner hypothesis is sound for a positive substitutable target. -/
theorem learner_soundness {L : Set (List Alphabet)}
    (h : List Alphabet →* M) (T : PositiveText Alphabet L)
    (hSub : TypedSubstitutable h L) :
    ∀ n : Nat, hypothesisLanguage h (learner h T.data n) ⊆ L := by
  intro n
  induction n with
  | zero =>
      simp [learner_zero, hypothesisLanguage]
  | succ n ih =>
      by_cases hmem : T.data n ∈ hypothesisLanguage h (learner h T.data n)
      · simpa [learner_conservative h T.data n hmem] using ih
      · simpa [learner_rebuild h T.data n hmem, hypothesisLanguage] using
          (rec_soundness h (observed T.data (n+1)) L
            (observed_positive T (n+1)) hSub)

#print axioms TCSPhase7.learner_conservative
#print axioms TCSPhase7.learner_rebuild
#print axioms TCSPhase7.change_implies_rebuild
#print axioms TCSPhase7.first_rebuild
#print axioms TCSPhase7.learner_sample_consistency
#print axioms TCSPhase7.learner_soundness
end TCSPhase7
