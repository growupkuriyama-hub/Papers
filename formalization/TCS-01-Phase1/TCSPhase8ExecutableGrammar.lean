import TCSPhase8UnaryEnumeration
import TCSPhase8BinaryEnumeration
import TCSPhase8StartLexical

/-! Executable finite reconstruction grammar: all six literal production
fields agree with Phase 5A's mathematical specification. -/
namespace TCSPhase8
open TCSPhase5
variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Monoid M] [DecidableEq M]

def buildRecGrammar (t : LetterTable Alphabet M)
    (K : Finset (List Alphabet)) : RecGrammar Alphabet := {
  nonterminals := efficientObservedFactors K
  binaryRules := efficientBinaryRules K
  unaryRules := efficientUnaryRules t K
  lexicalRules := efficientLexicalRules K
  startRules := efficientStartRules K
  startEmpty := efficientStartEmpty K
}

/-- Equality of the complete grammar object, including all six finite
rule components, under agreement of the supplied table with h. -/
theorem buildRecGrammar_eq_makeRecGrammar
    (h : List Alphabet →* M) (t : LetterTable Alphabet M)
    (ht : ∀ a, t.letter a = h [a]) (K : Finset (List Alphabet)) :
    buildRecGrammar t K = makeRecGrammar h K := by
  have hnt : (buildRecGrammar t K).nonterminals =
      (makeRecGrammar h K).nonterminals :=
    efficient_observed_factors_eq K
  have hbinary : (buildRecGrammar t K).binaryRules =
      (makeRecGrammar h K).binaryRules :=
    efficient_binary_rules_eq h K
  have hunary : (buildRecGrammar t K).unaryRules =
      (makeRecGrammar h K).unaryRules :=
    efficient_unary_rules_eq h t ht K
  have hlexical : (buildRecGrammar t K).lexicalRules =
      (makeRecGrammar h K).lexicalRules :=
    efficient_lexical_rules_eq h K
  have hstart : (buildRecGrammar t K).startRules =
      (makeRecGrammar h K).startRules :=
    efficient_start_rules_eq h K
  have hempty : (buildRecGrammar t K).startEmpty =
      (makeRecGrammar h K).startEmpty :=
    efficient_start_empty_eq h K
  cases ha : buildRecGrammar t K with
  | mk nt b u l s e =>
    cases hb : makeRecGrammar h K with
    | mk nt' b' u' l' s' e' =>
      simp only [ha, hb] at hnt hbinary hunary hlexical hstart hempty
      cases hnt
      cases hbinary
      cases hunary
      cases hlexical
      cases hstart
      cases hempty
      rfl

#print axioms TCSPhase8.buildRecGrammar_eq_makeRecGrammar
end TCSPhase8
