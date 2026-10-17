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

end TCSPhase5
