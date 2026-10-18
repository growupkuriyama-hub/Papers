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
    (K : Finset (List Alphabet)) :
    List (List Alphabet × List Alphabet) :=
  (enumerateOccurrencesList K).flatMap (fun occ =>
    (K.toList.filter (fun w =>
      let u := occ.1
      let x := occ.2.1
      let v := occ.2.2
      let y := middle u v w
      y ≠ [] ∧ u ++ y ++ v = w ∧ codeWord t x = codeWord t y)).map
        (fun w => (occ.2.1, middle occ.1 occ.2.2 w)))

/-- Equality of *sets* after emitting a possibly duplicate-containing
ordered list from the concrete pair loops. -/
theorem mem_emitUnaryCandidates_iff
    (t : LetterTable Alphabet M) (K : Finset (List Alphabet))
    (x y : List Alphabet) :
    (x,y) ∈ emitUnaryCandidates t K ↔
      (x,y) ∈ efficientUnaryRules t K := by
  constructor
  · intro hm
    obtain ⟨⟨u,x',v⟩, ho, hr⟩ := List.mem_flatMap.mp hm
    obtain ⟨w, hw, heq⟩ := List.mem_map.mp hr
    have hfiltered := List.mem_filter.mp hw
    apply Finset.mem_image.mpr
    refine ⟨((u,x',v),w), ?_, heq⟩
    apply Finset.mem_filter.mpr
    exact ⟨Finset.mem_product.mpr
      ⟨(mem_enumerateOccurrences_iff K u x' v).mpr
          ((mem_enumerateOccurrencesList_iff K u x' v).mp ho),
       by simpa using hfiltered.1⟩,
      hfiltered.2⟩
  · intro hm
    obtain ⟨⟨⟨u,x',v⟩,w⟩, hpair, heq⟩ := Finset.mem_image.mp hm
    have hf := Finset.mem_filter.mp hpair
    have hp := Finset.mem_product.mp hf.1
    apply List.mem_flatMap.mpr
    refine ⟨(u,x',v), ?_, ?_⟩
    · exact (mem_enumerateOccurrencesList_iff K u x' v).mpr
        ((mem_enumerateOccurrences_iff K u x' v).mp hp.1)
    · apply List.mem_map.mpr
      refine ⟨w, ?_, heq⟩
      exact List.mem_filter.mpr ⟨by simpa using hp.2, hf.2⟩

theorem emitUnaryCandidates_toFinset_eq
    (t : LetterTable Alphabet M) (K : Finset (List Alphabet)) :
    (emitUnaryCandidates t K).toFinset = efficientUnaryRules t K := by
  classical
  ext p
  rcases p with ⟨x,y⟩
  change (x,y) ∈ (emitUnaryCandidates t K).toFinset ↔
    (x,y) ∈ efficientUnaryRules t K
  rw [List.mem_toFinset, mem_emitUnaryCandidates_iff]

#print axioms TCSPhase8.mem_emitUnaryCandidates_iff
#print axioms TCSPhase8.emitUnaryCandidates_toFinset_eq

end TCSPhase8
