import TCSPhase8RecItem
import TCSPhase8RuleEncoding

/-!
A lossless bit representation of each of the six reconstructed grammar
item sorts. A concrete finite-letter numbering is passed as *data*;
its decoding law is verified, not guessed from Fintype existence.
The runtime representation contains only functions on alphabet letters
and numeric tokens.
-/
namespace TCSPhase8

/-- An explicit executable alphabet table with a verified partial inverse. -/
structure LetterNumbering (Alphabet : Type*) where
  number : Alphabet → Nat
  letter? : Nat → Option Alphabet
  decode_number : ∀ a, letter? (number a) = some a
  bound : Nat
  number_lt : ∀ a, number a < bound

/-- Zero delimits a word; every letter number is stored as successor. -/
def encodeWordTokens {Alphabet : Type*}
    (c : LetterNumbering Alphabet) : List Alphabet → List Nat
  | [] => [0]
  | a :: as => (c.number a + 1) :: encodeWordTokens c as

/-- Parsing one delimited word also returns the unconsumed suffix. -/
def readWordTokens {Alphabet : Type*}
    (c : LetterNumbering Alphabet) : List Nat →
      Option (List Alphabet × List Nat)
  | [] => none
  | 0 :: rest => some ([], rest)
  | (n + 1) :: rest => do
      let a ← c.letter? n
      let (w, tail) ← readWordTokens c rest
      return (a :: w, tail)

theorem readWordTokens_encode_append {Alphabet : Type*}
    (c : LetterNumbering Alphabet) (w : List Alphabet)
    (suffix : List Nat) :
    readWordTokens c (encodeWordTokens c w ++ suffix) =
      some (w, suffix) := by
  induction w with
  | nil => rfl
  | cons a rest ih =>
      simp [encodeWordTokens, readWordTokens, c.decode_number, ih]

/-- Numeric frame: fixed sort tag followed by delimited word arguments. -/
def recItemTokens {Alphabet : Type*}
    (c : LetterNumbering Alphabet) : RecItem Alphabet → List Nat
  | .nonterminal w => 0 :: encodeWordTokens c w
  | .binary z x y =>
      1 :: (encodeWordTokens c z ++ encodeWordTokens c x ++
        encodeWordTokens c y)
  | .unary x y =>
      2 :: (encodeWordTokens c x ++ encodeWordTokens c y)
  | .lexical a => 3 :: encodeWordTokens c [a]
  | .start w => 4 :: encodeWordTokens c w
  | .startEmpty => [5]

/-- The tag selects exactly the correct number of word frames. -/
def decodeRecItemTokens {Alphabet : Type*}
    (c : LetterNumbering Alphabet) : List Nat → Option (RecItem Alphabet)
  | 0 :: ns => do
      let (w, rest) ← readWordTokens c ns
      if rest = [] then return .nonterminal w else none
  | 1 :: ns => do
      let (z, rest) ← readWordTokens c ns
      let (x, rest) ← readWordTokens c rest
      let (y, rest) ← readWordTokens c rest
      if rest = [] then return .binary z x y else none
  | 2 :: ns => do
      let (x, rest) ← readWordTokens c ns
      let (y, rest) ← readWordTokens c rest
      if rest = [] then return .unary x y else none
  | 3 :: ns => do
      let (w, rest) ← readWordTokens c ns
      if rest = [] then
        match w with
        | [a] => return .lexical a
        | _ => none
      else none
  | 4 :: ns => do
      let (w, rest) ← readWordTokens c ns
      if rest = [] then return .start w else none
  | [5] => some .startEmpty
  | _ => none

theorem decodeRecItemTokens_roundtrip {Alphabet : Type*}
    (c : LetterNumbering Alphabet) (r : RecItem Alphabet) :
    decodeRecItemTokens c (recItemTokens c r) = some r := by
  cases r <;>
    simp [recItemTokens, decodeRecItemTokens,
      readWordTokens_encode_append, List.append_assoc]

/-- Complete bit encoding, not merely an encoding of numeric indices. -/
def encodeRecItem {Alphabet : Type*}
    (c : LetterNumbering Alphabet) (r : RecItem Alphabet) : List Bool :=
  encodeIndices (recItemTokens c r)

/-- Full decoder: first parse the unary numeric code, then typed frames. -/
def decodeRecItem {Alphabet : Type*}
    (c : LetterNumbering Alphabet) (bits : List Bool) :
      Option (RecItem Alphabet) :=
  (decodeIndicesAux 0 bits).bind (decodeRecItemTokens c)

theorem decodeRecItem_encodeRecItem {Alphabet : Type*}
    (c : LetterNumbering Alphabet) (r : RecItem Alphabet) :
    decodeRecItem c (encodeRecItem c r) = some r := by
  simp [decodeRecItem, encodeRecItem, decodeIndices_encodeIndices,
    decodeRecItemTokens_roundtrip]

theorem encodeRecItem_injective {Alphabet : Type*}
    (c : LetterNumbering Alphabet) :
    Function.Injective (encodeRecItem c) := by
  intro r s heq
  have h := congrArg (decodeRecItem c) heq
  simpa [decodeRecItem_encodeRecItem] using h

#print axioms TCSPhase8.readWordTokens_encode_append
#print axioms TCSPhase8.decodeRecItemTokens_roundtrip
#print axioms TCSPhase8.decodeRecItem_encodeRecItem
#print axioms TCSPhase8.encodeRecItem_injective
end TCSPhase8
