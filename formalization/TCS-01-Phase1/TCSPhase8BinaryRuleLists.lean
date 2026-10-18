import TCSPhase8OccurrenceLists
import TCSPhase8BinaryEnumeration

/-!
Ordered binary-rule emission by nested start/end/split position loops.
The output is a List of candidates, not a Finset, so duplicate
occurrences are retained. Its exact set agrees with the existing
Phase 8 binary grammar field.
-/
namespace TCSPhase8
open TCSPhase5

variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet] [Monoid M]

/-- For every actual occurrence, scan all proper nonempty splits. -/
def emitBinaryCandidates (sample : List (List Alphabet)) :
    List (List Alphabet × List Alphabet × List Alphabet) :=
  (enumerateOccurrencesList sample).flatMap (fun st =>
    ((splitsList st.2.1).filter
      (fun p => p.1 ≠ [] ∧ p.2 ≠ [])).map
      (fun p => (st.2.1, p.1, p.2)))

theorem mem_emitBinaryCandidates_iff
    (sample : List (List Alphabet))
    (z x y : List Alphabet) :
    (z,x,y) ∈ emitBinaryCandidates sample ↔
      (z,x,y) ∈ efficientBinaryRules sample.toFinset := by
  constructor
  · intro hm
    obtain ⟨⟨u,z',v⟩, hocc, hrule⟩ := List.mem_flatMap.mp hm
    obtain ⟨⟨x',y'⟩, hsplit, heq⟩ := List.mem_map.mp hrule
    have hp := List.mem_filter.mp hsplit
    have hzz : z' = z := congrArg Prod.fst heq
    have hxy : (x',y') = (x,y) := congrArg Prod.snd heq
    have hxx : x' = x := congrArg Prod.fst hxy
    have hyy : y' = y := congrArg Prod.snd hxy
    have hzw : z = x ++ y := by
      have hs := (mem_splitsList_iff z' x' y').mp hp.1
      simpa [hzz,hxx,hyy] using hs
    have ho := (mem_enumerateOccurrencesList_iff sample u z' v).mp hocc
    have hz : ObservedFactor sample.toFinset z := by
      rw [← hzz]
      exact ⟨ho.1,u,v,by simpa using ho.2⟩
    have hxne : x ≠ [] := by simpa [hxx] using hp.2.1
    have hyne : y ≠ [] := by simpa [hyy] using hp.2.2
    have hx : ObservedFactor sample.toFinset x :=
      observed_of_infix hz hxne ⟨[],y,by simpa using hzw⟩
    have hy : ObservedFactor sample.toFinset y :=
      observed_of_infix hz hyne ⟨x,[],by simpa using hzw⟩
    exact (efficient_binary_spec sample.toFinset z x y).mpr ⟨hzw,hx,hy,hz⟩
  · intro hm
    obtain ⟨hzw,hx,hy,hz⟩ := (efficient_binary_spec sample.toFinset z x y).mp hm
    obtain ⟨hne,u,v,hK⟩ := hz
    apply List.mem_flatMap.mpr
    refine ⟨(u,z,v), ?_, ?_⟩
    · exact (mem_enumerateOccurrencesList_iff sample u z v).mpr
        ⟨hne,by simpa using hK⟩
    · apply List.mem_map.mpr
      refine ⟨(x,y), ?_, rfl⟩
      exact List.mem_filter.mpr
        ⟨(mem_splitsList_iff z x y).mpr hzw,
          by simpa using (show x ≠ [] ∧ y ≠ [] from ⟨hx.1, hy.1⟩)⟩

/-- The duplicate-tolerant List emitter yields exactly the (B) rules
of the mathematical reconstruction grammar, as a set. -/
theorem emitBinaryCandidates_toFinset_eq
    (sample : List (List Alphabet)) :
    (emitBinaryCandidates sample).toFinset = efficientBinaryRules sample.toFinset := by
  classical
  ext p
  rcases p with ⟨z,x,y⟩
  change (z,x,y) ∈ (emitBinaryCandidates sample).toFinset ↔
    (z,x,y) ∈ efficientBinaryRules sample.toFinset
  rw [List.mem_toFinset, mem_emitBinaryCandidates_iff]

#print axioms TCSPhase8.mem_emitBinaryCandidates_iff
#print axioms TCSPhase8.emitBinaryCandidates_toFinset_eq

end TCSPhase8
