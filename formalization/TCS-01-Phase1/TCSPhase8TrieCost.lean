import TCSPhase8Trie

/-!
# Conditional O(n^4) bound for *trie insertion*, not for Rec_h

This is an executable-operation theorem, unlike merely bounding a
Finset cardinality. Each key is inserted using insertCount; its
instrumentation was proved equal to key.length+1. The hypotheses here
are not yet linked to actual encoded reconstruction productions.
-/
namespace TCSPhase8
namespace BitTrie

theorem sum_key_sizes_le (n : Nat) :
    ∀ keys : List (List Bool),
      (∀ k ∈ keys, k.length + 1 ≤ n) →
      (keys.map (fun k => k.length + 1)).sum ≤ keys.length * n := by
  intro keys
  induction keys with
  | nil =>
      intro _
      simp
  | cons key rest ih =>
      intro h
      have hk : key.length + 1 ≤ n := h key (by simp)
      have hrest : ∀ k ∈ rest, k.length + 1 ≤ n := by
        intro k hm
        exact h k (by simp [hm])
      have ht := ih hrest
      simp only [List.map_cons, List.sum_cons, List.length_cons, Nat.succ_mul]
      omega

theorem insertManyCount_cost_le (keys : List (List Bool))
    (trie : BitTrie) (n : Nat)
    (hsize : ∀ key ∈ keys, key.length + 1 ≤ n) :
    (insertManyCount keys trie).2 ≤ keys.length * n := by
  rw [insertManyCount_steps]
  exact sum_key_sizes_le n keys hsize

/-- Precisely costed bit-trie insertion is quartic *provided* that
the concrete keys are cubic in number and at most linear in size. -/
theorem insertManyCount_cost_le_fourth
    (keys : List (List Bool)) (trie : BitTrie) (n : Nat)
    (hcount : keys.length ≤ n^3)
    (hsize : ∀ key ∈ keys, key.length + 1 ≤ n) :
    (insertManyCount keys trie).2 ≤ n^4 := by
  calc
    (insertManyCount keys trie).2 ≤ keys.length * n :=
      insertManyCount_cost_le keys trie n hsize
    _ ≤ n^3 * n := Nat.mul_le_mul_right n hcount
    _ = n^4 := by ring

#print axioms TCSPhase8.BitTrie.sum_key_sizes_le
#print axioms TCSPhase8.BitTrie.insertManyCount_cost_le
#print axioms TCSPhase8.BitTrie.insertManyCount_cost_le_fourth
end BitTrie
end TCSPhase8
