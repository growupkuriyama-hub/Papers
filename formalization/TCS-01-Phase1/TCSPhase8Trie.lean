import TCSPhase8Main

/-!
# A concrete binary trie for removing duplicate bit-string encodings

The recursively instrumented operations below count visits to trie nodes.
Each insertion visits exactly (key.length + 1) nodes. This is one
necessary data-structure ingredient of the paper's O(n^4) argument,
NOT the whole bound: an injective production encoder and an operational
bridge between emitted grammar rules and trie keys remain to be proved.
-/
namespace TCSPhase8

inductive BitTrie where
  | node (accept : Bool) (left right : Option BitTrie)
  deriving Inhabited

namespace BitTrie

def empty : BitTrie := .node false none none

def contains : List Bool → BitTrie → Bool
  | [], .node accept _ _ => accept
  | false :: bs, .node _ left _ =>
      match left with
      | none => false
      | some child => contains bs child
  | true :: bs, .node _ _ right =>
      match right with
      | none => false
      | some child => contains bs child

/-- Recursive insertion with a visit counter. One visit is charged
for every recursive invocation, including the terminal bit position. -/
def insertCount : List Bool → BitTrie → BitTrie × Nat
  | [], .node _ left right => (.node true left right, 1)
  | false :: bs, .node accept left right =>
      let child := insertCount bs (left.getD empty)
      (.node accept (some child.1) right, child.2 + 1)
  | true :: bs, .node accept left right =>
      let child := insertCount bs (right.getD empty)
      (.node accept left (some child.1), child.2 + 1)

theorem insertCount_steps (key : List Bool) (trie : BitTrie) :
    (insertCount key trie).2 = key.length + 1 := by
  induction key generalizing trie with
  | nil =>
      cases trie
      rfl
  | cons bit rest ih =>
      cases trie with
      | node mark left right =>
        cases bit <;> simp [insertCount, ih]

theorem insertCount_contains (key : List Bool) (trie : BitTrie) :
    contains key (insertCount key trie).1 = true := by
  induction key generalizing trie with
  | nil =>
      cases trie
      rfl
  | cons bit rest ih =>
      cases trie with
      | node mark left right =>
        cases bit <;> simp [insertCount, contains, ih]

/-- Batch insertion uses the actual instrumented insertion operation. -/
def insertManyCount : List (List Bool) → BitTrie → BitTrie × Nat
  | [], trie => (trie, 0)
  | key :: keys, trie =>
      let first := insertCount key trie
      let remaining := insertManyCount keys first.1
      (remaining.1, first.2 + remaining.2)

theorem insertManyCount_steps (keys : List (List Bool)) (trie : BitTrie) :
    (insertManyCount keys trie).2 =
      (keys.map (fun key => key.length + 1)).sum := by
  induction keys generalizing trie with
  | nil => rfl
  | cons key rest ih =>
      change (insertCount key trie).2 +
        (insertManyCount rest (insertCount key trie).1).2 =
        (key.length + 1) + (rest.map (fun k => k.length + 1)).sum
      rw [insertCount_steps, ih]

#print axioms TCSPhase8.BitTrie.insertCount_steps
#print axioms TCSPhase8.BitTrie.insertCount_contains
#print axioms TCSPhase8.BitTrie.insertManyCount_steps

end BitTrie
end TCSPhase8
