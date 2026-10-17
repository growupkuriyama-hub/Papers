import TCSPhase3Parser

/-! One direction of Appendix C Lemma C.1, proved from Phase 2's independent CFG derivation. -/
namespace TCSPhase3
open TCSPhase1 TCSPhase2

/-- Every CFG derivation parses successfully from E_i with ANY lower stack suffix,
provided i is within the fixed parser's bound. -/
theorem derives_run {i : Nat} {w : Word} (hd : Derives i w) :
    ∀ (bound : Nat) (ψ : Stack), i ≤ bound →
      Run bound (Frame.nt i :: ψ) w ψ := by
  induction i generalizing w with
  | zero =>
      cases hd with
      | atom =>
          intro bound ψ hi
          exact Run.next (Step.atom ψ) (Run.nil ψ)
  | succ i ih =>
      cases hd with
      | unary hu =>
          intro bound ψ hi
          have hchild := ih hu bound (Frame.ceilClose :: ψ) (by omega)
          have hpop : Run bound (Frame.ceilClose :: ψ)
              [Terminal.squareRight] ψ :=
            Run.next (Step.ceilPop ψ) (Run.nil ψ)
          have hr := Run.next (Step.unary i hi ψ) (run_append hchild hpop)
          simpa [unaryWord] using hr
      | binary hu hv =>
          intro bound ψ hi
          have hfirst := ih hu bound
            (Frame.nt i :: Frame.floorClose :: ψ) (by omega)
          have hsecond := ih hv bound (Frame.floorClose :: ψ) (by omega)
          have hpop : Run bound (Frame.floorClose :: ψ)
              [Terminal.right] ψ :=
            Run.next (Step.floorPop ψ) (Run.nil ψ)
          have hr := Run.next (Step.binary i hi ψ)
            (run_append hfirst (run_append hsecond hpop))
          simpa [binaryWord, List.append_assoc] using hr

/-- Forward direction of Lemma C.1; the converse is NOT asserted here. -/
theorem generated_word_parses (bound i : Nat) (ψ : Stack) (w : Word)
    (hi : i ≤ bound) (hw : w ∈ Language i) :
    Run bound (Frame.nt i :: ψ) w ψ :=
  derives_run hw bound ψ hi

/-- In particular every member of the original G_n is recognized from S_0. -/
theorem grammar_language_parses (n : Nat) (w : Word)
    (hw : w ∈ Language n) :
    Run n [Frame.nt n] w [] := by
  simpa using generated_word_parses n n [] w le_rfl hw

#print axioms TCSPhase3.derives_run
#print axioms TCSPhase3.generated_word_parses
#print axioms TCSPhase3.grammar_language_parses
end TCSPhase3
