import TCSPhase8Occurrences

/-!
Actual ordered, duplicate-tolerant lists of factor occurrences. Unlike a
Finset membership witness, the enumerators below explicitly iterate over
start and end offsets using List.range, map and flatMap. No CandidateWords
alphabet-wide enumeration is called.
-/
namespace TCSPhase8

variable {Alphabet : Type*} [DecidableEq Alphabet]

/-- All boundaries, scanned in the concrete order 0,...,|w|. -/
def splitsList (w : List Alphabet) :
    List (List Alphabet × List Alphabet) :=
  (List.range (w.length + 1)).map
    (fun i => (w.take i, w.drop i))

theorem mem_splitsList_iff (w u v : List Alphabet) :
    (u,v) ∈ splitsList w ↔ w = u ++ v := by
  constructor
  · intro hm
    obtain ⟨i, hi, heq⟩ := List.mem_map.mp hm
    have hu : w.take i = u := congrArg Prod.fst heq
    have hv : w.drop i = v := congrArg Prod.snd heq
    calc
      w = w.take i ++ w.drop i := (List.take_append_drop i w).symm
      _ = u ++ v := by rw [hu,hv]
  · intro hw
    apply List.mem_map.mpr
    refine ⟨u.length, ?_, ?_⟩
    · simp only [List.mem_range, hw, List.length_append]
      omega
    · simp [hw]

/-- Ordered scan of start/end offsets; duplicate triples are allowed. -/
def occurrencesInList (w : List Alphabet) :
    List (List Alphabet × List Alphabet × List Alphabet) :=
  (splitsList w).flatMap (fun st =>
    ((splitsList st.2).filter (fun xv => xv.1 ≠ [])).map
      (fun xv => (st.1, xv.1, xv.2)))

theorem mem_occurrencesInList_iff
    (w u x v : List Alphabet) :
    (u,x,v) ∈ occurrencesInList w ↔
      x ≠ [] ∧ w = u ++ x ++ v := by
  constructor
  · intro hm
    obtain ⟨⟨u',t⟩, hleft, hright⟩ := List.mem_flatMap.mp hm
    obtain ⟨⟨x',v'⟩, hsplit, heq⟩ := List.mem_map.mp hright
    have hfactor := List.mem_filter.mp hsplit
    have ha : u' = u := congrArg Prod.fst heq
    have hb : (x',v') = (x,v) := congrArg Prod.snd heq
    have hx : x' = x := congrArg Prod.fst hb
    have hv : v' = v := congrArg Prod.snd hb
    have hword : w = u' ++ t := (mem_splitsList_iff w u' t).mp hleft
    have htail : t = x' ++ v' := (mem_splitsList_iff t x' v').mp hfactor.1
    constructor
    · simpa [hx] using hfactor.2
    · simpa [ha,hx,hv,List.append_assoc,htail] using hword
  · rintro ⟨hne, hw⟩
    apply List.mem_flatMap.mpr
    refine ⟨(u,x++v), ?_, ?_⟩
    · exact (mem_splitsList_iff w u (x++v)).mpr
        (by simpa [List.append_assoc] using hw)
    · apply List.mem_map.mpr
      refine ⟨(x,v), ?_, rfl⟩
      exact List.mem_filter.mpr
        ⟨(mem_splitsList_iff (x++v) x v).mpr rfl, by simpa using hne⟩

/-- A concrete ordered List of sample words is the executable input.
It may contain repeated sample words, which are harmless here. -/
def enumerateOccurrencesList (sample : List (List Alphabet)) :
    List (List Alphabet × List Alphabet × List Alphabet) :=
  sample.flatMap occurrencesInList

theorem mem_enumerateOccurrencesList_iff
    (sample : List (List Alphabet)) (u x v : List Alphabet) :
    (u,x,v) ∈ enumerateOccurrencesList sample ↔
      x ≠ [] ∧ u ++ x ++ v ∈ sample := by
  constructor
  · intro hm
    obtain ⟨w, hw, he⟩ := List.mem_flatMap.mp hm
    have hs := (mem_occurrencesInList_iff w u x v).mp he
    exact ⟨hs.1, hs.2 ▸ hw⟩
  · rintro ⟨hne, hw⟩
    apply List.mem_flatMap.mpr
    exact ⟨u ++ x ++ v, hw,
      (mem_occurrencesInList_iff (u++x++v) u x v).mpr ⟨hne,rfl⟩⟩

/-- Converting only the *result* to a Finset proves equality with
the existing mathematical specification, without requiring Finset.toList
as an executable data conversion. -/
theorem enumerateOccurrencesList_toFinset_eq
    (sample : List (List Alphabet)) :
    (enumerateOccurrencesList sample).toFinset =
      enumerateOccurrences sample.toFinset := by
  classical
  ext p
  rcases p with ⟨u,x,v⟩
  rw [List.mem_toFinset, mem_enumerateOccurrencesList_iff,
      mem_enumerateOccurrences_iff]
  simp

#print axioms TCSPhase8.mem_splitsList_iff
#print axioms TCSPhase8.mem_occurrencesInList_iff
#print axioms TCSPhase8.mem_enumerateOccurrencesList_iff
#print axioms TCSPhase8.enumerateOccurrencesList_toFinset_eq

end TCSPhase8
