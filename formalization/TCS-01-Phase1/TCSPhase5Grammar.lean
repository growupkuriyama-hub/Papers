import TCSPhase5FactorsFinite
import TCSPhase5Derivations

namespace TCSPhase5

variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet] [Monoid M]

structure RecGrammar (Alphabet : Type*) where
  nonterminals : Finset (Word Alphabet)
  binaryRules : Finset (Word Alphabet × Word Alphabet × Word Alphabet)
  unaryRules : Finset (Word Alphabet × Word Alphabet)
  lexicalRules : Finset Alphabet
  startRules : Finset (Word Alphabet)
  startEmpty : Bool

/-- Exact finite B/U/L/S production collections. -/
noncomputable def makeRecGrammar
    (h : Word Alphabet →* M) (K : Finset (Word Alphabet)) :
    RecGrammar Alphabet := by
  classical
  let obs := ObservedFactors K
  exact {
    nonterminals := obs
    binaryRules := ((obs.product obs).image
      (fun p => (p.1 ++ p.2, p.1, p.2))).filter
        (fun r => r.1 ∈ obs)
    unaryRules := (obs.product obs).filter
      (fun p => DirectSimilar h K p.1 p.2)
    lexicalRules := (Finset.univ : Finset Alphabet).filter
      (fun a => [a] ∈ obs)
    startRules := K.filter (fun x => x ≠ [])
    startEmpty := decide (([] : Word Alphabet) ∈ K)
  }


variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet] [Monoid M]

theorem rec_node_iff (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) (x : Word Alphabet) :
    x ∈ (makeRecGrammar h K).nonterminals ↔ ObservedFactor K x := by
  simp [makeRecGrammar, mem_observedFactors]

theorem rec_lexical_rule_iff (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) (a : Alphabet) :
    a ∈ (makeRecGrammar h K).lexicalRules ↔
      ObservedFactor K [a] := by
  classical
  simp [makeRecGrammar, mem_observedFactors]

theorem rec_start_rule_iff (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) (w : Word Alphabet) :
    w ∈ (makeRecGrammar h K).startRules ↔ w ∈ K ∧ w ≠ [] := by
  classical
  simp [makeRecGrammar]

theorem rec_start_empty_iff (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) :
    (makeRecGrammar h K).startEmpty = true ↔
       ([] : Word Alphabet) ∈ K := by
  classical
  simp [makeRecGrammar]

theorem rec_unary_rule_iff (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) (x y : Word Alphabet) :
    (x, y) ∈ (makeRecGrammar h K).unaryRules ↔
      ObservedFactor K x ∧ ObservedFactor K y ∧
      DirectSimilar h K x y := by
  classical
  simp [makeRecGrammar, Finset.mem_product, mem_observedFactors,
    and_assoc]

#print axioms TCSPhase5.rec_node_iff
#print axioms TCSPhase5.rec_lexical_rule_iff
#print axioms TCSPhase5.rec_start_rule_iff
#print axioms TCSPhase5.rec_start_empty_iff
#print axioms TCSPhase5.rec_unary_rule_iff

end TCSPhase5
