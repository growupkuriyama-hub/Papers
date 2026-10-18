import TCSPhase8OperationalGrammar

/-!
A tagged representation of all six fields of the operational List grammar.
Its source lists remain in their existing executable order and retain
duplicate productions. No Finset conversion is performed by this emitter.
-/
namespace TCSPhase8

inductive RecItem (Alphabet : Type*) where
  | nonterminal (w : List Alphabet)
  | binary (z x y : List Alphabet)
  | unary (x y : List Alphabet)
  | lexical (a : Alphabet)
  | start (w : List Alphabet)
  | startEmpty
  deriving Inhabited

/-- Tags are disjoint by the inductive constructors. -/
def ListedRecGrammar.items {Alphabet : Type*}
    (g : ListedRecGrammar Alphabet) : List (RecItem Alphabet) :=
  g.nonterminals.map RecItem.nonterminal ++
  g.binaryRules.map (fun p => RecItem.binary p.1 p.2.1 p.2.2) ++
  g.unaryRules.map (fun p => RecItem.unary p.1 p.2) ++
  g.lexicalRules.map RecItem.lexical ++
  g.startRules.map RecItem.start ++
  (if g.startEmpty then [RecItem.startEmpty] else [])

/-- The exact duplicate-tolerant stream emitted by the six-field builder. -/
def emitAllRecItems {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) : List (RecItem Alphabet) :=
  (buildListedRecGrammar t sample).items

theorem items_startEmpty_iff {Alphabet : Type*}
    (g : ListedRecGrammar Alphabet) :
    RecItem.startEmpty ∈ g.items ↔ g.startEmpty = true := by
  cases h : g.startEmpty <;>
    simp [ListedRecGrammar.items, h]

theorem items_length {Alphabet : Type*}
    (g : ListedRecGrammar Alphabet) :
    g.items.length =
      g.nonterminals.length + g.binaryRules.length +
      g.unaryRules.length + g.lexicalRules.length +
      g.startRules.length + (if g.startEmpty then 1 else 0) := by
  cases h : g.startEmpty <;>
    simp [ListedRecGrammar.items, h]

#print axioms TCSPhase8.items_startEmpty_iff
#print axioms TCSPhase8.items_length
end TCSPhase8
