import TCSPhase8ExecutableGrammar
import TCSPhase8RuleCandidateBounds

/-!
# Phase 8: executable reconstruction and finite-candidate bounds

This module collects the already proved literal grammar equality and
the polynomial *candidate cardinality* inequalities. It intentionally
does not assert an execution-time bound for `Finset` operations.
-/

namespace TCSPhase8

variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Monoid M] [DecidableEq M]

/-- Phase 8 verified qualitative construction and combinatorial resource bounds.
This theorem does NOT claim O(n⁴) execution time. -/
theorem reconstruction_correct_and_candidate_bounds
    (h : List Alphabet →* M) (t : LetterTable Alphabet M)
    (ht : ∀ a, t.letter a = h [a])
    (K : Finset (List Alphabet)) :
    buildRecGrammar t K = TCSPhase5.makeRecGrammar h K ∧
    (enumerateOccurrences K).card ≤ (TCSPhase1.encodedSize K)^2 ∧
    ((enumerateOccurrences K).product K).card ≤ (TCSPhase1.encodedSize K)^3 ∧
    (efficientBinaryRules K).card ≤
       (TCSPhase1.encodedSize K)^2 * (TCSPhase1.encodedSize K+1) := by
  exact ⟨buildRecGrammar_eq_makeRecGrammar h t ht K,
    enumerateOccurrences_card_le_square K,
    unary_candidate_pairs_card_le_cube K,
    binary_rules_card_le_cubic K⟩

#print axioms TCSPhase8.mem_enumerateOccurrences_iff
#print axioms TCSPhase8.efficient_observed_factors_eq
#print axioms TCSPhase8.codeWord_eq_h
#print axioms TCSPhase8.efficient_binary_rules_eq
#print axioms TCSPhase8.efficient_unary_rules_eq
#print axioms TCSPhase8.enumerateOccurrences_card_le_square
#print axioms TCSPhase8.buildRecGrammar_eq_makeRecGrammar
#print axioms TCSPhase8.unary_candidate_pairs_card_le_cube
#print axioms TCSPhase8.binary_rules_card_le_cubic
#print axioms TCSPhase8.reconstruction_correct_and_candidate_bounds

end TCSPhase8
