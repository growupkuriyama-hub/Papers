import TCSPhase8BinaryRuleLists
import TCSPhase8UnaryRuleLists
import TCSPhase8StartLexicalLists
import TCSPhase8ExecutableGrammar

/-!
# List-form reconstruction with a mathematical RecGrammar projection
The list-valued algorithm is executable and retains duplicate candidates.
The projection `asRecGrammar` proves semantic equality with Phase 5; it
is NOT the claimed quartic-time duplicate elimination algorithm.
-/
namespace TCSPhase8
open TCSPhase5

variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Monoid M] [DecidableEq M]

structure ListedRecGrammar (Alphabet : Type*) where
  nonterminals : List (List Alphabet)
  binaryRules : List (List Alphabet × List Alphabet × List Alphabet)
  unaryRules : List (List Alphabet × List Alphabet)
  lexicalRules : List Alphabet
  startRules : List (List Alphabet)
  startEmpty : Bool

/-- Exactly the concrete order of candidate generation; duplicates allowed. -/
def buildListedRecGrammar (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) : ListedRecGrammar Alphabet := {
  nonterminals := (enumerateOccurrencesList sample).map (fun p => p.2.1)
  binaryRules := emitBinaryCandidates sample
  unaryRules := emitUnaryCandidates t sample
  lexicalRules := emitLexicalCandidates sample
  startRules := emitStartCandidates sample
  startEmpty := emitStartEmpty sample
}

/-- Specification projection; NOT used in the operational List scan. -/
def ListedRecGrammar.asRecGrammar (g : ListedRecGrammar Alphabet) :
    RecGrammar Alphabet := {
  nonterminals := g.nonterminals.toFinset
  binaryRules := g.binaryRules.toFinset
  unaryRules := g.unaryRules.toFinset
  lexicalRules := g.lexicalRules.toFinset
  startRules := g.startRules.toFinset
  startEmpty := g.startEmpty
}

/-- Every nonempty observed factor occurs in the actual List scan. -/
theorem listedNonterminals_eq
    (sample : List (List Alphabet)) :
    ((enumerateOccurrencesList sample).map (fun p => p.2.1)).toFinset =
      efficientObservedFactors sample.toFinset := by
  classical
  unfold efficientObservedFactors
  rw [← enumerateOccurrencesList_toFinset_eq]
  ext x
  simp only [List.mem_toFinset, List.mem_map, Finset.mem_image]

/-- Equality of six fields in the set-valued specification projection. -/
theorem buildListedRecGrammar_spec
    (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) :
    (buildListedRecGrammar t sample).asRecGrammar =
      buildRecGrammar t sample.toFinset := by
  unfold ListedRecGrammar.asRecGrammar buildListedRecGrammar buildRecGrammar
  simp [listedNonterminals_eq,
    emitBinaryCandidates_toFinset_eq,
    emitUnaryCandidates_toFinset_eq,
    emitLexicalCandidates_toFinset_eq,
    emitStartCandidates_toFinset_eq,
    emitStartEmpty_eq]

/-- Semantics agree with the Phase 5 mathematical reconstruction grammar. -/
theorem buildListedRecGrammar_correct
    (h : List Alphabet →* M) (t : LetterTable Alphabet M)
    (ht : ∀ a, t.letter a = h [a])
    (sample : List (List Alphabet)) :
    (buildListedRecGrammar t sample).asRecGrammar =
      makeRecGrammar h sample.toFinset := by
  rw [buildListedRecGrammar_spec]
  exact buildRecGrammar_eq_makeRecGrammar h t ht sample.toFinset

#print axioms TCSPhase8.listedNonterminals_eq
#print axioms TCSPhase8.buildListedRecGrammar_spec
#print axioms TCSPhase8.buildListedRecGrammar_correct
end TCSPhase8
