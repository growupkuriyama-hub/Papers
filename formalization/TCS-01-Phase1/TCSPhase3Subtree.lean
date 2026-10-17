import TCSPhase3RecognitionFull

/-!
Appendix C complete-subtree exchange (optional Phase 3B milestone).
Uses the *fully proved* parser/CFG recognition equivalence and its
arbitrary-start-stack assertion. Clark--Eyraud substitutability is not taken as a premise.
-/

namespace TCSPhase3
open TCSPhase1 TCSPhase2

/-- If a context of L_n contains a complete L_i subtree, every other
L_i word can be substituted into that same concrete context. -/
theorem grammar_context_replace (n i : Nat) (hi : i ≤ n)
    (x y p q : Word) (hx : x ∈ Language i) (hy : y ∈ Language i)
    (hp : p ++ x ++ q ∈ Language n) :
    p ++ y ++ q ∈ Language n := by
  have haccept : Run n [Frame.nt n] (p ++ (x ++ q)) [] := by
    simpa [List.append_assoc] using
      grammar_language_parses n (p ++ x ++ q) hp
  obtain ⟨s, hpRun, hxqRun⟩ :=
    run_append_split p (x ++ q) haccept
  obtain ⟨t, hxRun, hqRun⟩ :=
    run_append_split x q hxqRun
  obtain ⟨ψ, hstart, hend⟩ :=
    recognition_arbitrary_start n i s t x hi hxRun hx
  subst s
  subst t
  have hyRun : Run n (Frame.nt i :: ψ) y ψ :=
    generated_word_parses n i ψ y hi hy
  have hreplacement : Run n [Frame.nt n] (p ++ y ++ q) [] := by
    have hcombined := run_append hpRun (run_append hyRun hqRun)
    simpa [List.append_assoc] using hcombined
  exact recognition_converse n n [] (p ++ y ++ q) le_rfl hreplacement

/-- Appendix C complete-subtree exchange, for all n and i ≤ n,
where language membership refers to the original CFG derivations. -/
theorem complete_subtree_exchange (n i : Nat) (hi : i ≤ n)
    (x y : Word) (hx : x ∈ Language i) (hy : y ∈ Language i) :
    Distributions (Language n) x = Distributions (Language n) y := by
  ext p
  change (p.1 ++ x ++ p.2 ∈ Language n) ↔
    (p.1 ++ y ++ p.2 ∈ Language n)
  constructor
  · exact grammar_context_replace n i hi x y p.1 p.2 hx hy
  · exact grammar_context_replace n i hi y x p.1 p.2 hy hx

#print axioms TCSPhase3.grammar_context_replace
#print axioms TCSPhase3.complete_subtree_exchange

end TCSPhase3
