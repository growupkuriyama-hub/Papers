import TCSPhase8Occurrences

/-! Explicit occurrence-count upper bounds; not a machine-time bound for Finset. -/
namespace TCSPhase8
open TCSPhase5
variable {Alphabet : Type*} [DecidableEq Alphabet]

theorem splits_card_le (w : List Alphabet) :
    (splits w).card ≤ w.length + 1 := by
  classical
  calc
    (splits w).card ≤ (Finset.range (w.length+1)).card :=
      Finset.card_image_le
    _ = w.length+1 := by simp

theorem occurrencesIn_card_le_square (w : List Alphabet) :
    (occurrencesIn w).card ≤ (w.length+1)^2 := by
  classical
  calc
    (occurrencesIn w).card ≤
        ∑ p ∈ splits w,
          (((splits p.2).filter (fun q => q.1 ≠ [])).image
            (fun q => (p.1,q.1,q.2))).card := by
      unfold occurrencesIn
      exact Finset.card_biUnion_le
    _ ≤ ∑ _p ∈ splits w, (w.length+1) := by
      apply Finset.sum_le_sum
      intro p hp
      have h1 :
          (((splits p.2).filter (fun q => q.1 ≠ [])).image
            (fun q => (p.1,q.1,q.2))).card ≤
          ((splits p.2).filter (fun q => q.1 ≠ [])).card :=
        Finset.card_image_le
      have h2 : ((splits p.2).filter (fun q => q.1 ≠ [])).card ≤
          (splits p.2).card := Finset.card_filter_le _ _
      have h3 := splits_card_le p.2
      have h4 : p.2.length ≤ w.length := by
        have hsp := (mem_splits_iff w p.1 p.2).mp hp
        simp only [hsp, List.length_append]
        omega
      omega
    _ = (splits w).card * (w.length+1) := by simp
    _ ≤ (w.length+1)^2 := by
      have h := Nat.mul_le_mul_right (w.length+1) (splits_card_le w)
      simpa [pow_two] using h

theorem enumerateOccurrences_card_le_square
    (K : Finset (List Alphabet)) :
    (enumerateOccurrences K).card ≤ (TCSPhase1.encodedSize K)^2 := by
  classical
  let n := TCSPhase1.encodedSize K
  calc
    (enumerateOccurrences K).card ≤
        ∑ w ∈ K, (occurrencesIn w).card := by
      unfold enumerateOccurrences
      exact Finset.card_biUnion_le
    _ ≤ ∑ w ∈ K, (w.length+1)^2 := by
      apply Finset.sum_le_sum
      intro w hw
      exact occurrencesIn_card_le_square w
    _ ≤ ∑ w ∈ K, (w.length+1) * n := by
      apply Finset.sum_le_sum
      intro w hw
      have hsmall : w.length+1 ≤ n := by
        dsimp [n, TCSPhase1.encodedSize]
        exact Finset.single_le_sum (s := K)
          (f := fun z : List Alphabet => z.length + 1)
          (fun _ _ => Nat.zero_le _) hw
      nlinarith [Nat.mul_le_mul_left (w.length+1) hsmall]
    _ = n*n := by
      simp [n, TCSPhase1.encodedSize, Finset.sum_mul]
    _ = n^2 := by ring

#print axioms TCSPhase8.splits_card_le
#print axioms TCSPhase8.occurrencesIn_card_le_square
#print axioms TCSPhase8.enumerateOccurrences_card_le_square
end TCSPhase8
