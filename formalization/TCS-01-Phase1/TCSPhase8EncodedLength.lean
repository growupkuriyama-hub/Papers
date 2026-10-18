import TCSPhase8CompleteEncoding

/-!
Proof obligations for the *actual* complete tagged serializer. The
explicit multiplier is fixed by a supplied finite-alphabet numbering.
No actual sample bound is asserted before the source-word lengths are
connected to concrete candidate membership.
-/
namespace TCSPhase8

def RecItem.letterCount {Alphabet : Type*} : RecItem Alphabet → Nat
  | .nonterminal w => w.length
  | .binary z x y => z.length + x.length + y.length
  | .unary x y => x.length + y.length
  | .lexical _ => 1
  | .start w => w.length
  | .startEmpty => 0

theorem encodeWordTokens_length {Alphabet : Type*}
    (c : LetterNumbering Alphabet) (w : List Alphabet) :
    (encodeWordTokens c w).length = w.length + 1 := by
  induction w with
  | nil => rfl
  | cons a rest ih =>
      simp [encodeWordTokens, ih]
 
theorem recItemTokens_length_le {Alphabet : Type*}
    (c : LetterNumbering Alphabet) (r : RecItem Alphabet) :
    (recItemTokens c r).length ≤ r.letterCount + 4 := by
  cases r <;>
    simp [recItemTokens, RecItem.letterCount,
      encodeWordTokens_length] <;> omega

def tokenBound {Alphabet : Type*} (c : LetterNumbering Alphabet) :
    Nat := max 6 (c.bound + 2)

theorem encodeWordTokens_bounded {Alphabet : Type*}
    (c : LetterNumbering Alphabet) (w : List Alphabet) :
    ∀ k ∈ encodeWordTokens c w, k + 1 ≤ tokenBound c := by
  induction w with
  | nil =>
      intro k hk
      simp [encodeWordTokens] at hk
      subst k
      exact le_trans (by decide : 1 ≤ 6) (Nat.le_max_left _ _)
  | cons a rest ih =>
      intro k hk
      simp only [encodeWordTokens, List.mem_cons] at hk
      rcases hk with h | h
      · subst k
        have hb := c.number_lt a
        have hle : c.number a + 1 + 1 ≤ c.bound + 2 := by omega
        exact le_trans hle (Nat.le_max_right _ _)
      · exact ih k h

def RecItem.itemTag {Alphabet : Type*} : RecItem Alphabet → Nat
  | .nonterminal _ => 0
  | .binary _ _ _ => 1
  | .unary _ _ => 2
  | .lexical _ => 3
  | .start _ => 4
  | .startEmpty => 5

def RecItem.itemWords {Alphabet : Type*} : RecItem Alphabet → List (List Alphabet)
  | .nonterminal w => [w]
  | .binary z x y => [z,x,y]
  | .unary x y => [x,y]
  | .lexical a => [[a]]
  | .start w => [w]
  | .startEmpty => []

theorem recItemTokens_as_flatMap {Alphabet : Type*}
    (c : LetterNumbering Alphabet) (r : RecItem Alphabet) :
    recItemTokens c r =
      r.itemTag :: r.itemWords.flatMap (encodeWordTokens c) := by
  cases r <;>
    simp [recItemTokens, RecItem.itemTag, RecItem.itemWords,
      List.append_assoc]

theorem recItemTokens_bounded {Alphabet : Type*}
    (c : LetterNumbering Alphabet) (r : RecItem Alphabet) :
    ∀ k ∈ recItemTokens c r, k + 1 ≤ tokenBound c := by
  intro k hk
  rw [recItemTokens_as_flatMap] at hk
  rcases List.mem_cons.mp hk with h | h
  · subst k
    have ht : r.itemTag ≤ 5 := by
      cases r <;> simp [RecItem.itemTag]
    have h6 : r.itemTag + 1 ≤ 6 := by omega
    exact le_trans h6 (Nat.le_max_left _ _)
  · obtain ⟨w, _, hw⟩ := List.mem_flatMap.mp h
    exact encodeWordTokens_bounded c w k hw

/-- Direct step bound for the bits *produced* by the serializer. -/
theorem encodeRecItem_length_le {Alphabet : Type*}
    (c : LetterNumbering Alphabet) (r : RecItem Alphabet) :
    (encodeRecItem c r).length ≤
      (r.letterCount + 4) * tokenBound c := by
  calc
    (encodeRecItem c r).length ≤
        (recItemTokens c r).length * tokenBound c := by
      exact encodeIndices_length_le _ _ (recItemTokens_bounded c r)
    _ ≤ (r.letterCount + 4) * tokenBound c :=
      Nat.mul_le_mul_right _ (recItemTokens_length_le c r)

#print axioms TCSPhase8.recItemTokens_length_le
#print axioms TCSPhase8.recItemTokens_bounded
#print axioms TCSPhase8.encodeRecItem_length_le
end TCSPhase8
