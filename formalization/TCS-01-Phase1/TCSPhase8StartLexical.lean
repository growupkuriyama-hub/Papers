import TCSPhase8Occurrences
import TCSPhase5FiniteDerivation

/-! Executable finite lexical and start production collections. -/
namespace TCSPhase8
open TCSPhase5
variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet] [Monoid M]

def efficientLexicalRules (K : Finset (List Alphabet)) : Finset Alphabet :=
  (Finset.univ : Finset Alphabet).filter
    (fun a => [a] ∈ efficientObservedFactors K)

def efficientStartRules (K : Finset (List Alphabet)) :
    Finset (List Alphabet) := K.filter (fun w => w ≠ [])

def efficientStartEmpty (K : Finset (List Alphabet)) : Bool :=
  decide (([] : List Alphabet) ∈ K)

theorem efficient_lexical_rules_eq
    (h : List Alphabet →* M) (K : Finset (List Alphabet)) :
    efficientLexicalRules K = (makeRecGrammar h K).lexicalRules := by
  classical
  ext a
  simpa only [efficientLexicalRules, Finset.mem_filter,
    Finset.mem_univ, true_and, efficient_observed_factors_iff] using
    (rec_lexical_rule_iff h K a).symm

theorem efficient_start_rules_eq
    (h : List Alphabet →* M) (K : Finset (List Alphabet)) :
    efficientStartRules K = (makeRecGrammar h K).startRules := by
  simp [efficientStartRules, makeRecGrammar]

theorem efficient_start_empty_eq
    (h : List Alphabet →* M) (K : Finset (List Alphabet)) :
    efficientStartEmpty K = (makeRecGrammar h K).startEmpty := by
  simp [efficientStartEmpty, makeRecGrammar]

#print axioms TCSPhase8.efficient_lexical_rules_eq
#print axioms TCSPhase8.efficient_start_rules_eq
#print axioms TCSPhase8.efficient_start_empty_eq
end TCSPhase8
