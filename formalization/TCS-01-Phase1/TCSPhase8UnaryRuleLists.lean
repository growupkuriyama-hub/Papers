import TCSPhase8OccurrenceLists
import TCSPhase8UnaryEnumeration

/-!
Actual ordered unary-rule candidate list: loop through every observed
occurrence and every input sample word, extract exactly one possible
middle word, test nonemptiness, matching contexts and monoid types.
There is no transitive-closure operation or CandidateWords call.
-/
namespace TCSPhase8
open TCSPhase5

variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Monoid M] [DecidableEq M]

def emitUnaryCandidates (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) :
    List (List Alphabet × List Alphabet) :=
  (enumerateOccurrencesList sample).flatMap (fun occ =>
    (sample.filter (fun w =>
      let u := occ.1
      let x := occ.2.1
      let v := occ.2.2
      let y := middle u v w
      y ≠ [] ∧ u ++ y ++ v = w ∧ codeWord t x = codeWord t y)).map
        (fun w => (occ.2.1, middle occ.1 occ.2.2 w)))

/-- Equality of *sets* after emitting a possibly duplicate-containing
ordered list from the concrete pair loops. -/
theorem mem_emitUnaryCandidates_iff
    (t : LetterTable Alphabet M) (sample : List (List Alphabet))
    (x y : List Alphabet) :
    (x,y) ∈ emitUnaryCandidates t sample ↔
      (x,y) ∈ efficientUnaryRules t sample.toFinset := by
  constructor
  · intro hm
    obtain ⟨⟨u,x',v⟩, ho, hr⟩ := List.mem_flatMap.mp hm
    obtain ⟨w, hw, heq⟩ := List.mem_map.mp hr
    have hfiltered := List.mem_filter.mp hw
    have hoccData :=
      (mem_enumerateOccurrencesList_iff sample u x' v).mp ho
    have hoccFin :
        (u,x',v) ∈ enumerateOccurrences sample.toFinset := by
      apply (mem_enumerateOccurrences_iff sample.toFinset u x' v).mpr
      exact ⟨hoccData.1, by simpa using hoccData.2⟩
    have hwFin : w ∈ sample.toFinset := by
      simpa using hfiltered.1
    have hpair :
        ((u,x',v),w) ∈
          (enumerateOccurrences sample.toFinset).product
            sample.toFinset :=
      Finset.mem_product.mpr ⟨hoccFin,hwFin⟩
    have hcondition :
        middle u v w ≠ [] ∧
          u ++ middle u v w ++ v = w ∧
          codeWord t x' = codeWord t (middle u v w) := by
      simpa only [] using hfiltered.2
    apply Finset.mem_image.mpr
    refine ⟨((u,x',v),w), ?_, heq⟩
    exact Finset.mem_filter.mpr ⟨hpair, hcondition⟩
  · intro hm
    obtain ⟨⟨⟨u,x',v⟩,w⟩, hpair, heq⟩ := Finset.mem_image.mp hm
    have hf := Finset.mem_filter.mp hpair
    have hp := Finset.mem_product.mp hf.1
    apply List.mem_flatMap.mpr
    refine ⟨(u,x',v), ?_, ?_⟩
    · exact (mem_enumerateOccurrencesList_iff sample u x' v).mpr
        ⟨((mem_enumerateOccurrences_iff sample.toFinset u x' v).mp hp.1).1,
          by simpa using ((mem_enumerateOccurrences_iff sample.toFinset u x' v).mp hp.1).2⟩
    · apply List.mem_map.mpr
      refine ⟨w, ?_, heq⟩
      exact List.mem_filter.mpr ⟨by simpa using hp.2, by simpa using hf.2⟩

theorem emitUnaryCandidates_toFinset_eq
    (t : LetterTable Alphabet M) (sample : List (List Alphabet)) :
    (emitUnaryCandidates t sample).toFinset = efficientUnaryRules t sample.toFinset := by
  classical
  ext p
  rcases p with ⟨x,y⟩
  change (x,y) ∈ (emitUnaryCandidates t sample).toFinset ↔
    (x,y) ∈ efficientUnaryRules t sample.toFinset
  rw [List.mem_toFinset, mem_emitUnaryCandidates_iff]

#print axioms TCSPhase8.mem_emitUnaryCandidates_iff
#print axioms TCSPhase8.emitUnaryCandidates_toFinset_eq

end TCSPhase8
