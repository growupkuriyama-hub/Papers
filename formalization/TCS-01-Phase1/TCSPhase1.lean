import Mathlib

/-
Phase 1 of TCS Proposition 6.3, from canonical HEAD
55c2f818c64ff51aaea3940ebad1c08b655dc4f6,
main.tex lines 281--294 and 1108--1227 (v209).
CFG membership and Theorem 4.2 soundness are NOT proved here.
-/

namespace TCSPhase1

variable {α : Type*}

/-- Set-driven characteristic sample: positive finite sample S, and
exact reconstruction from any finite K between S and L. -/
def Characteristic (Op : Finset α → Set α) (L : Set α)
    (S : Finset α) : Prop :=
  (↑S : Set α) ⊆ L ∧
    ∀ K : Finset α, S ⊆ K → (↑K : Set α) ⊆ L → Op K = L

/-- Prop. 6.3(iv), abstract distinguishing-pair principle.
No monotonicity or finiteness assumption on Op or L. -/
theorem distinguishing_word
    (Op : Finset α → Set α) (L : Set α) (w : α)
    (hw : w ∈ L)
    (hMinus : ∃ T : Finset α, Characteristic Op (L \ {w}) T)
    (S : Finset α) (hS : Characteristic Op L S) : w ∈ S := by
  classical
  by_contra hnot
  obtain ⟨T, hT⟩ := hMinus
  let K : Finset α := S ∪ T
  have hKminus : (↑K : Set α) ⊆ L \ {w} := by
    intro x hx
    have hxK : x ∈ S ∪ T := hx
    rcases Finset.mem_union.mp hxK with hxS | hxT
    · have hxne : x ≠ w := by
        intro heq
        apply hnot
        exact heq ▸ hxS
      exact ⟨hS.1 hxS, by simpa using hxne⟩
    · exact hT.1 hxT
  have hKplus : (↑K : Set α) ⊆ L := by
    intro x hx
    exact (hKminus hx).1
  have hOpL : Op K = L := hS.2 K Finset.subset_union_left hKplus
  have hOpMinus : Op K = L \ {w} :=
    hT.2 K Finset.subset_union_right hKminus
  have hEq : L = L \ {w} := hOpL.symm.trans hOpMinus
  rw [hEq] at hw
  simp at hw

/-- Five literal terminal symbols in the bracketed family. -/
inductive Terminal where
  | a | left | right | squareLeft | squareRight
  deriving DecidableEq, Repr

/-- w0 = a; w(n+1) = ◁ wn wn ▷ as an actual finite word. -/
def witness : Nat → List Terminal
  | 0 => [Terminal.a]
  | n + 1 => [Terminal.left] ++ witness n ++ witness n ++ [Terminal.right]

private theorem witness_length_succ (n : Nat) :
    (witness (n + 1)).length = 2 * (witness n).length + 2 := by
  simp [witness, List.length_append]
  omega

/-- Exact length formula without truncated subtraction. -/
theorem witness_length_plus_two (n : Nat) :
    (witness n).length + 2 = 3 * 2 ^ n := by
  induction n with
  | zero => simp [witness]
  | succ n ih =>
      rw [witness_length_succ, pow_succ]
      omega

theorem witness_length (n : Nat) :
    (witness n).length = 3 * 2 ^ n - 2 := by
  have h := witness_length_plus_two n
  omega

/-- Encoded size from main.tex line 293: sum (word length + 1). -/
def encodedSize {β : Type*} (K : Finset (List β)) : Nat :=
  ∑ x ∈ K, x.length + 1

theorem encodedSize_ge (n : Nat) (K : Finset (List Terminal))
    (hmem : witness n ∈ K) :
    3 * 2 ^ n - 1 ≤ encodedSize K := by
  have hle : (witness n).length + 1 ≤ encodedSize K := by
    unfold encodedSize
    simpa using (Finset.single_le_sum (s := K)
      (f := fun x : List Terminal => x.length + 1)
      (fun _ _ => Nat.zero_le _) hmem)
  have hlen := witness_length_plus_two n
  omega

/-- Combined conditional exponential bound of Prop. 6.3(iv).
Explicit assumptions: witness membership and a characteristic sample
for the punctured language; neither is inferred by fiat. -/
theorem characteristic_exponential_lower_bound
    (Op : Finset (List Terminal) → Set (List Terminal))
    (L : Set (List Terminal)) (n : Nat)
    (hw : witness n ∈ L)
    (hMinus : ∃ T : Finset (List Terminal),
      Characteristic Op (L \ {witness n}) T)
    (S : Finset (List Terminal)) (hS : Characteristic Op L S) :
    3 * 2 ^ n - 1 ≤ encodedSize S := by
  have hmem := distinguishing_word Op L (witness n) hw hMinus S hS
  exact encodedSize_ge n S hmem

/-- Prop. 6.3(iii) as an implication FROM soundness.
Does NOT establish the actual Rec_h soundness of Theorem 4.2. -/
theorem soundness_excludes
    (Rec : Finset α → Set α) (L : Set α) (w : α)
    (K : Finset α)
    (hSound : ∀ J : Finset α, (↑J : Set α) ⊆ L \ {w} →
      Rec J ⊆ L \ {w})
    (hK : (↑K : Set α) ⊆ L) (hnot : w ∉ K) :
    w ∉ Rec K := by
  have hKminus : (↑K : Set α) ⊆ L \ {w} := by
    intro x hx
    have hxne : x ≠ w := by
      intro heq
      apply hnot
      exact heq ▸ hx
    exact ⟨hK hx, by simpa using hxne⟩
  intro hwRec
  have hwminus := hSound K hKminus hwRec
  simp at hwminus

#print axioms TCSPhase1.distinguishing_word
#print axioms TCSPhase1.witness_length_plus_two
#print axioms TCSPhase1.witness_length
#print axioms TCSPhase1.encodedSize_ge
#print axioms TCSPhase1.characteristic_exponential_lower_bound
#print axioms TCSPhase1.soundness_excludes

end TCSPhase1
