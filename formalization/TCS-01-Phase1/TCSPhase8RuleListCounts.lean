import TCSPhase8UnaryRuleLists
import TCSPhase8BinaryRuleLists
import TCSPhase8OccurrenceListCounts

/-!
Cardinality of *emitted candidate lists*, including repeated productions.
These counts are separate from the earlier Finset rule-cardinality bounds.
-/
namespace TCSPhase8
variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Monoid M] [DecidableEq M]

theorem sample_length_le_encodedListSample
    (sample : List (List Alphabet)) :
    sample.length ≤ encodedListSample sample := by
  induction sample with
  | nil => simp [encodedListSample]
  | cons w rest ih =>
    simp only [List.length_cons, encodedListSample,
      List.map_cons, List.sum_cons] at *
    omega

theorem word_length_le_encodedListSample
    (sample : List (List Alphabet)) (w : List Alphabet)
    (hw : w ∈ sample) :
    w.length ≤ encodedListSample sample := by
  induction sample with
  | nil => simp at hw
  | cons head rest ih =>
    rcases List.mem_cons.mp hw with h | h
    · subst w
      simp [encodedListSample]
    · have ht := ih h
      simp only [encodedListSample, List.map_cons, List.sum_cons]
      omega

/-- Every actual (occurrence, sample-word) unary candidate is charged
once by the nested List iteration, including unsuccessful comparisons. -/
theorem emitUnaryCandidates_length_le_cube
    (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) :
    (emitUnaryCandidates t sample).length ≤
      (encodedListSample sample)^3 := by
  let n := encodedListSample sample
  have hocc := enumerateOccurrencesList_length_le_square sample
  have hwords := sample_length_le_encodedListSample sample
  calc
    (emitUnaryCandidates t sample).length ≤
        (enumerateOccurrencesList sample).length * sample.length := by
      unfold emitUnaryCandidates
      apply length_flatMap_le_mul
      intro occ hocc
      simpa only [List.length_map] using
        (List.length_filter_le
          (fun w : List Alphabet =>
            let u := occ.1
            let x := occ.2.1
            let v := occ.2.2
            let y := middle u v w
            y ≠ [] ∧ u ++ y ++ v = w ∧
              codeWord t x = codeWord t y) sample)
    _ ≤ n^2*n := Nat.mul_le_mul hocc hwords
    _ = n^3 := by ring

/-- All actual binary candidate emission operations, including
duplicates, have a cubic (n²(n+1)) numerical bound. -/
theorem emitBinaryCandidates_length_le_cubic
    (sample : List (List Alphabet)) :
    (emitBinaryCandidates sample).length ≤
      (encodedListSample sample)^2 *
        (encodedListSample sample + 1) := by
  let n := encodedListSample sample
  have hocc := enumerateOccurrencesList_length_le_square sample
  have hrow :
      ∀ st ∈ enumerateOccurrencesList sample,
        (((splitsList st.2.1).filter
          (fun p => p.1 ≠ [] ∧ p.2 ≠ [])).map
          (fun p => (st.2.1, p.1, p.2))).length ≤ n+1 := by
    intro st hst
    rcases st with ⟨u,z,v⟩
    have hdata := (mem_enumerateOccurrencesList_iff sample u z v).mp hst
    have hlen := word_length_le_encodedListSample sample
      (u++z++v) hdata.2
    have hz : z.length ≤ n := by
      simp only [List.length_append] at hlen
      omega
    have hf := List.length_filter_le
      (fun p : List Alphabet × List Alphabet =>
        p.1 ≠ [] ∧ p.2 ≠ []) (splitsList z)
    simp only [List.length_map]
    rw [splitsList_length] at hf
    omega
  calc
    (emitBinaryCandidates sample).length ≤
        (enumerateOccurrencesList sample).length * (n+1) := by
      unfold emitBinaryCandidates
      exact length_flatMap_le_mul _ _ _ hrow
    _ ≤ n^2*(n+1) := Nat.mul_le_mul_right (n+1) hocc

#print axioms TCSPhase8.sample_length_le_encodedListSample
#print axioms TCSPhase8.emitUnaryCandidates_length_le_cube
#print axioms TCSPhase8.emitBinaryCandidates_length_le_cubic
end TCSPhase8
