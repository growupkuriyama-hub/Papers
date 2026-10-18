import TCSPhase8OccurrenceLists
import TCSPhase8SampleTypeCache

/-!
Resource count for *raw* candidate List traversal, before any deduplication.
This is distinct from the cardinality of a Finset of occurrences.
-/
namespace TCSPhase8
variable {Alphabet : Type*} [DecidableEq Alphabet]

/-- A general bound for an actual nested List.flatMap loop. -/
theorem length_flatMap_le_mul {α β : Type*}
    (xs : List α) (f : α → List β) (n : Nat)
    (hf : ∀ x ∈ xs, (f x).length ≤ n) :
    (xs.flatMap f).length ≤ xs.length * n := by
  induction xs with
  | nil => simp
  | cons x rest ih =>
    have hx := hf x (by simp)
    have hrest : ∀ y ∈ rest, (f y).length ≤ n := by
      intro y hy
      exact hf y (by simp [hy])
    have htail := ih hrest
    simp only [List.flatMap_cons, List.length_append,
      List.length_cons, Nat.succ_mul]
    omega

theorem splitsList_length (w : List Alphabet) :
    (splitsList w).length = w.length + 1 := by
  simp [splitsList]

/-- The actual double-boundary scan produces at most (m+1)^2 entries. -/
theorem occurrencesInList_length_le_square (w : List Alphabet) :
    (occurrencesInList w).length ≤ (w.length + 1)^2 := by
  unfold occurrencesInList
  have hrow :
      ∀ st ∈ splitsList w,
        (((splitsList st.2).filter
          (fun p => p.1 ≠ [] )).map
          (fun p => (st.1,p.1,p.2))).length ≤ w.length+1 := by
    intro st hst
    have h1 := List.length_filter_le
      (fun p : List Alphabet × List Alphabet => p.1 ≠ [])
      (splitsList st.2)
    have hw := (mem_splitsList_iff w st.1 st.2).mp hst
    have hlen : st.2.length ≤ w.length := by
      rw [hw]
      simp
    simp only [List.length_map]
    rw [splitsList_length] at h1
    omega
  have htotal := length_flatMap_le_mul (splitsList w)
    (fun st =>
      ((splitsList st.2).filter
        (fun p => p.1 ≠ [])).map
        (fun p => (st.1,p.1,p.2))) (w.length+1) hrow
  rw [splitsList_length] at htotal
  nlinarith

/-- Sum of actual occurrence-output lengths over a concrete word list
is bounded quadratically by that list's encoded length. -/
theorem occurrenceLists_count_le_square
    (sample : List (List Alphabet)) :
    (sample.flatMap occurrencesInList).length ≤
      (encodedListSample sample)^2 := by
  induction sample with
  | nil => simp [encodedListSample]
  | cons w rest ih =>
    have hw := occurrencesInList_length_le_square w
    have hcross : 0 ≤ (w.length + 1) *
      encodedListSample rest := Nat.zero_le _
    simp only [List.flatMap_cons, List.length_append,
      encodedListSample, List.map_cons, List.sum_cons] at *
    nlinarith

/-- Unlike the earlier Finset bound, this bounds the actual emitted
List's length, counting repeated triples. -/
theorem enumerateOccurrencesList_length_le_square
    (K : Finset (List Alphabet)) :
    (enumerateOccurrencesList K).length ≤
      (TCSPhase1.encodedSize K)^2 := by
  simpa [enumerateOccurrencesList, encodedListSample_toList] using
    (occurrenceLists_count_le_square K.toList)

#print axioms TCSPhase8.length_flatMap_le_mul
#print axioms TCSPhase8.occurrencesInList_length_le_square
#print axioms TCSPhase8.enumerateOccurrencesList_length_le_square
end TCSPhase8
