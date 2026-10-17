import TCSPhase5Factors

namespace TCSPhase5
variable {Alphabet : Type*} [Fintype Alphabet] [DecidableEq Alphabet]

/-- A finite complete enumeration of words of EXACT length n. -/
def WordsOfLength (Alphabet : Type*) [Fintype Alphabet]
    [DecidableEq Alphabet] : Nat → Finset (Word Alphabet)
  | 0 => {[]}
  | n + 1 =>
      ((Finset.univ : Finset Alphabet).product
        (WordsOfLength Alphabet n)).image (fun p => p.1 :: p.2)

theorem mem_wordsOfLength (w : Word Alphabet) :
    w ∈ WordsOfLength Alphabet w.length := by
  induction w with
  | nil => simp [WordsOfLength]
  | cons a as ih =>
      change a :: as ∈ WordsOfLength Alphabet (as.length + 1)
      simp only [WordsOfLength, Finset.mem_image]
      exact ⟨(a, as), Finset.mem_product.mpr
        ⟨Finset.mem_univ _, ih⟩, rfl⟩

/-- Finiteness is witnessed by a literal finite superset of every word
of length at most the sample's encoded size. Enumeration is finite but
not claimed to be an efficient implementation of the original learner. -/
def CandidateWords (K : Finset (Word Alphabet)) :
    Finset (Word Alphabet) :=
  (Finset.range (TCSPhase1.encodedSize K + 1)).biUnion
    (WordsOfLength Alphabet)

theorem observed_length_le (K : Finset (Word Alphabet))
    {x : Word Alphabet} (hx : ObservedFactor K x) :
    x.length ≤ TCSPhase1.encodedSize K := by
  obtain ⟨hne, u, v, hmem⟩ := hx
  have hle : (u ++ x ++ v).length + 1 ≤
      TCSPhase1.encodedSize K := by
    unfold TCSPhase1.encodedSize
    exact Finset.single_le_sum (s := K)
      (f := fun z : Word Alphabet => z.length + 1)
      (fun _ _ => Nat.zero_le _) hmem
  simp only [List.length_append] at hle
  omega

theorem observed_mem_candidates (K : Finset (Word Alphabet))
    {x : Word Alphabet} (hx : ObservedFactor K x) :
    x ∈ CandidateWords K := by
  apply Finset.mem_biUnion.mpr
  exact ⟨x.length,
    Finset.mem_range.mpr (by have := observed_length_le K hx; omega),
    mem_wordsOfLength x⟩

/-- The actual FINITE set of nonempty observed contiguous factors. -/
noncomputable def ObservedFactors (K : Finset (Word Alphabet)) :
    Finset (Word Alphabet) := by
  classical
  exact (CandidateWords K).filter (ObservedFactor K)

theorem mem_observedFactors (K : Finset (Word Alphabet))
    (x : Word Alphabet) :
    x ∈ ObservedFactors K ↔ ObservedFactor K x := by
  classical
  simp only [ObservedFactors, Finset.mem_filter]
  exact ⟨And.right, fun hx => ⟨observed_mem_candidates K hx, hx⟩⟩

theorem observed_finite (K : Finset (Word Alphabet)) :
    {x : Word Alphabet | ObservedFactor K x}.Finite := by
  have heq : {x : Word Alphabet | ObservedFactor K x} =
      (↑(ObservedFactors K) : Set (Word Alphabet)) := by
    ext x
    simpa using (mem_observedFactors K x).symm
  rw [heq]
  exact Finset.finite_toSet _

theorem observedFactors_mono {K K' : Finset (Word Alphabet)}
    (hKK : K ⊆ K') :
    ObservedFactors K ⊆ ObservedFactors K' := by
  intro x hx
  apply (mem_observedFactors K' x).mpr
  exact observed_mono hKK ((mem_observedFactors K x).mp hx)

#print axioms TCSPhase5.mem_wordsOfLength
#print axioms TCSPhase5.observed_length_le
#print axioms TCSPhase5.mem_observedFactors
#print axioms TCSPhase5.observed_finite
#print axioms TCSPhase5.observedFactors_mono

end TCSPhase5
