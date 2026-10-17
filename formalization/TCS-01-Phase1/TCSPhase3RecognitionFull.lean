import TCSPhase3RecognitionConverse
import TCSPhase3Prefix

/-! Second assertion of Appendix C Lemma C.1:
a COMPLETE CFG word forces the entire initial nonterminal height and
the unchanged remainder of the initial stack. -/

namespace TCSPhase3
open TCSPhase1 TCSPhase2

/-- Any run reading the special opening prefix of a level-i grammar word
must have started with nonterminal E_i, independently of where it ends. -/
theorem initial_nt_of_opening_prefix {bound : Nat} {i : Nat}
    {w : Word} {s t : Stack}
    (hp : OpeningPrefix i w) (h : Run bound s w t) :
    ∃ ψ : Stack, s = Frame.nt i :: ψ := by
  induction hp generalizing s t with
  | atom suffix =>
      cases h with
      | next hs hr =>
          cases hs with
          | atom tail => exact ⟨tail, rfl⟩
  | @ceil k u hp ih =>
      cases h with
      | next hs hr =>
          cases hs with
          | unary j hj tail =>
              obtain ⟨ψ, he⟩ := ih hr
              have hheads : Frame.nt j = Frame.nt k :=
                (List.cons.inj he).1
              have hji : j = k := Frame.nt.inj hheads
              subst j
              exact ⟨tail, rfl⟩
  | @floor k u hp ih =>
      cases h with
      | next hs hr =>
          cases hs with
          | binary j hj tail =>
              obtain ⟨ψ, he⟩ := ih hr
              have hheads : Frame.nt j = Frame.nt k :=
                (List.cons.inj he).1
              have hji : j = k := Frame.nt.inj hheads
              subst j
              exact ⟨tail, rfl⟩

/-- The second, arbitrary-initial-stack assertion of Appendix C Lemma C.1.
It uses the *actual* L_i, bounded parsing, the proved initial frame
lemma, and deterministic execution plus the forward recognition lemma. -/
theorem recognition_arbitrary_start (bound i : Nat)
    (s t : Stack) (w : Word) (hi : i ≤ bound)
    (h : Run bound s w t) (hw : w ∈ Language i) :
    ∃ ψ : Stack, s = Frame.nt i :: ψ ∧ t = ψ := by
  obtain ⟨ψ, he⟩ :=
    initial_nt_of_opening_prefix (language_opening_prefix i w hw) h
  subst s
  have hgenerated : Run bound (Frame.nt i :: ψ) w ψ :=
    generated_word_parses bound i ψ w hi hw
  have ht : t = ψ := run_deterministic h hgenerated
  exact ⟨ψ, rfl, ht⟩

#print axioms TCSPhase3.initial_nt_of_opening_prefix
#print axioms TCSPhase3.recognition_arbitrary_start

end TCSPhase3
