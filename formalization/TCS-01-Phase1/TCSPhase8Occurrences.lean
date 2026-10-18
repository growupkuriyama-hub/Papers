import TCSPhase7Main

/-! Polynomial-scale substring occurrence enumeration, distinct from the
exponential-alphabet CandidateWords finite superset in Phase 5A. -/
namespace TCSPhase8
open TCSPhase5

variable {Alphabet : Type*} [DecidableEq Alphabet]

/-- Executable list splitting at the boundaries 0,...,length. -/
def splits (w : List Alphabet) : Finset (List Alphabet × List Alphabet) :=
  (Finset.range (w.length + 1)).image
    (fun i => (w.take i, w.drop i))

theorem mem_splits_iff (w u v : List Alphabet) :
    (u,v) ∈ splits w ↔ w = u ++ v := by
  classical
  constructor
  · intro hm
    obtain ⟨i, _, heq⟩ := Finset.mem_image.mp hm
    have hu : w.take i = u := congrArg Prod.fst heq
    have hv : w.drop i = v := congrArg Prod.snd heq
    calc
      w = w.take i ++ w.drop i := (List.take_append_drop i w).symm
      _ = u ++ v := by rw [hu,hv]
  · intro heq
    apply Finset.mem_image.mpr
    refine ⟨u.length, ?_, ?_⟩
    · simp only [heq, List.length_append, Finset.mem_range]
      omega
    · simp [heq]

/-- All nonempty factor occurrences of one word, retaining both contexts.
The two scans enumerate split positions, not candidate strings. -/
def occurrencesIn (w : List Alphabet) :
    Finset (List Alphabet × List Alphabet × List Alphabet) :=
  (splits w).biUnion (fun st =>
    ((splits st.2).filter (fun xv => xv.1 ≠ [])).image
      (fun xv => (st.1, xv.1, xv.2)))

theorem mem_occurrencesIn_iff
    (w u x v : List Alphabet) :
    (u,x,v) ∈ occurrencesIn w ↔ x ≠ [] ∧ w = u ++ x ++ v := by
  classical
  constructor
  · intro hm
    obtain ⟨⟨u',t⟩, hleft, hright⟩ :=
      Finset.mem_biUnion.mp (show (u,x,v) ∈ _ from hm)
    obtain ⟨⟨x',v'⟩, hsplit, heq⟩ := Finset.mem_image.mp hright
    have hfactor := Finset.mem_filter.mp hsplit
    have ha : u' = u := congrArg Prod.fst heq
    have hb : (x',v') = (x,v) := congrArg Prod.snd heq
    have hx : x' = x := congrArg Prod.fst hb
    have hv : v' = v := congrArg Prod.snd hb
    have hword : w = u' ++ t := (mem_splits_iff w u' t).mp hleft
    have htail : t = x' ++ v' := (mem_splits_iff t x' v').mp hfactor.1
    constructor
    · simpa [hx] using hfactor.2
    · simpa [ha,hx,hv,List.append_assoc,htail] using hword
  · rintro ⟨hne,hw⟩
    apply Finset.mem_biUnion.mpr
    refine ⟨(u,x++v), ?_, ?_⟩
    · apply (mem_splits_iff w u (x++v)).mpr
      simpa [List.append_assoc] using hw
    · apply Finset.mem_image.mpr
      refine ⟨(x,v), ?_, rfl⟩
      exact Finset.mem_filter.mpr
        ⟨(mem_splits_iff (x++v) x v).mpr rfl, hne⟩

/-- A finite sample is scanned by enumerating occurrences in every word. -/
def enumerateOccurrences (K : Finset (List Alphabet)) :
    Finset (List Alphabet × List Alphabet × List Alphabet) :=
  K.biUnion occurrencesIn

theorem mem_enumerateOccurrences_iff
    (K : Finset (List Alphabet)) (u x v : List Alphabet) :
    (u,x,v) ∈ enumerateOccurrences K ↔
      x ≠ [] ∧ u ++ x ++ v ∈ K := by
  classical
  constructor
  · intro hm
    obtain ⟨w, hw, hocc⟩ := Finset.mem_biUnion.mp hm
    have hs := (mem_occurrencesIn_iff w u x v).mp hocc
    exact ⟨hs.1, hs.2 ▸ hw⟩
  · rintro ⟨hne,hK⟩
    apply Finset.mem_biUnion.mpr
    exact ⟨u ++ x ++ v, hK,
      (mem_occurrencesIn_iff (u++x++v) u x v).mpr ⟨hne,rfl⟩⟩

/-- Factors obtained only from actual contiguous substring occurrences. -/
def efficientObservedFactors (K : Finset (List Alphabet)) :
    Finset (List Alphabet) :=
  (enumerateOccurrences K).image (fun p => p.2.1)

theorem efficient_observed_factors_iff
    (K : Finset (List Alphabet)) (x : List Alphabet) :
    x ∈ efficientObservedFactors K ↔ ObservedFactor K x := by
  classical
  constructor
  · intro hx
    obtain ⟨⟨u,y,v⟩, hocc, heq⟩ := Finset.mem_image.mp hx
    have hmem := (mem_enumerateOccurrences_iff K u y v).mp hocc
    have hxy : y = x := heq
    subst y
    exact ⟨hmem.1, u, v, hmem.2⟩
  · rintro ⟨hne,u,v,hK⟩
    apply Finset.mem_image.mpr
    exact ⟨(u,x,v), (mem_enumerateOccurrences_iff K u x v).mpr
      ⟨hne,hK⟩, rfl⟩

/-- Same observed nonempty factors as the original mathematical grammar;
this statement itself makes no claim about execution time. -/
theorem efficient_observed_factors_eq [Fintype Alphabet]
    (K : Finset (List Alphabet)) :
    efficientObservedFactors K = ObservedFactors K := by
  classical
  ext x
  rw [efficient_observed_factors_iff, mem_observedFactors]

#print axioms TCSPhase8.mem_splits_iff
#print axioms TCSPhase8.mem_occurrencesIn_iff
#print axioms TCSPhase8.mem_enumerateOccurrences_iff
#print axioms TCSPhase8.efficient_observed_factors_eq
end TCSPhase8
