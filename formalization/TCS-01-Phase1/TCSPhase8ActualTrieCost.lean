import TCSPhase8OperationalTrie
import TCSPhase8TrieCost

/-!
# Trie insertion on the actual tagged reconstruction stream

The first theorem charges the concrete emitted item list and the actual
complete serializer. The letter-count hypothesis remains explicit;
proving it from source occurrences is a separate mathematical obligation.
This is an insertion-step bound, NOT a total runtime bound.
-/
namespace TCSPhase8

theorem buildItemTrie_steps_le_of_letter_bound
    {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) (B : Nat)
    (hletters : ∀ r ∈ emitAllRecItems t sample, r.letterCount ≤ B) :
    (buildItemTrie c t sample).2 ≤
      3 * (encodedListSample sample + 1)^3 *
        ((B + 4) * tokenBound c + 1) := by
  let items := emitAllRecItems t sample
  let keyBound := (B + 4) * tokenBound c + 1
  have hsize :
      ∀ key ∈ items.map (encodeRecItem c), key.length + 1 ≤ keyBound := by
    intro key hk
    obtain ⟨r, hr, heq⟩ := List.mem_map.mp hk
    have hb : r.letterCount ≤ B := hletters r hr
    have hbit := encodeRecItem_length_le c r
    have hmul :
        (r.letterCount + 4) * tokenBound c ≤
          (B + 4) * tokenBound c :=
      Nat.mul_le_mul_right (tokenBound c) (Nat.add_le_add_right hb 4)
    rw [← heq]
    dsimp [keyBound]
    omega
  have hsteps :
      (buildItemTrie c t sample).2 ≤ items.length * keyBound := by
    change (BitTrie.insertManyCount
      (items.map (encodeRecItem c)) BitTrie.empty).2 ≤
        items.length * keyBound
    have hi := BitTrie.insertManyCount_cost_le
      (items.map (encodeRecItem c)) BitTrie.empty keyBound hsize
    simpa only [List.length_map] using hi
  calc
    (buildItemTrie c t sample).2 ≤ items.length * keyBound := hsteps
    _ ≤ (3 * (encodedListSample sample + 1)^3) * keyBound := by
      exact Nat.mul_le_mul_right keyBound
        (emitAllRecItems_length_le t sample)
    _ = 3 * (encodedListSample sample + 1)^3 *
        ((B + 4) * tokenBound c + 1) := rfl

/-- Quartic bound for the actual trie insertion if each actually emitted
production has at most twice the encoded sample size in source letters.
The remaining membership-to-length premise is displayed in the type. -/
theorem buildItemTrie_steps_le_fourth_if_linear_letters
    {Alphabet M : Type*}
    [Fintype Alphabet] [DecidableEq Alphabet]
    [Monoid M] [DecidableEq M]
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet))
    (hletters : ∀ r ∈ emitAllRecItems t sample,
      r.letterCount ≤ 2 * (encodedListSample sample + 1)) :
    (buildItemTrie c t sample).2 ≤
      (18 * tokenBound c + 3) * (encodedListSample sample + 1)^4 := by
  let n := encodedListSample sample
  let b := tokenBound c
  have hi := buildItemTrie_steps_le_of_letter_bound c t sample
    (2 * (n+1)) hletters
  have hfactor : 2 * (n+1) + 4 ≤ 6 * (n+1) := by omega
  have hm := Nat.mul_le_mul_right b hfactor
  have hsize :
      ((2 * (n+1) + 4) * b + 1) ≤
        (6*b + 1) * (n+1) := by
    nlinarith
  calc
    (buildItemTrie c t sample).2 ≤
      3 * (n+1)^3 * ((2 * (n+1)+4)*b+1) := hi
    _ ≤ 3 * (n+1)^3 * ((6*b+1)*(n+1)) :=
      Nat.mul_le_mul_left _ hsize
    _ = (18*b+3)*(n+1)^4 := by ring

#print axioms TCSPhase8.buildItemTrie_steps_le_of_letter_bound
#print axioms TCSPhase8.buildItemTrie_steps_le_fourth_if_linear_letters
end TCSPhase8
