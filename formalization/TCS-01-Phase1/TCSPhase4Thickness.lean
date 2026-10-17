import TCSPhase4Trimming

namespace TCSPhase4
open TCSPhase1 TCSPhase2

/-- Both elements of the genuine two-element finite monoid are enumerated.
Only a new finite enumeration is introduced; U1 and hU remain unchanged. -/
instance : Fintype U1 where
  elems := {U1.one, U1.zero}
  complete := by
    intro x
    cases x <;> simp

/-- Finite set of exactly those typed non-start symbols appearing
in a successful typed derivation from the distinguished start. -/
noncomputable def retainedTypedPairs {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) : Finset (NT × U1) := by
  classical
  exact Finset.univ.filter (fun p => RetainedTypedSymbol G p.1 p.2)

theorem mem_retainedTypedPairs {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) (A : NT) (μ : U1) :
    (A, μ) ∈ retainedTypedPairs G ↔ RetainedTypedSymbol G A μ := by
  classical
  simp [retainedTypedPairs]

/-- Minimal length of a word generated from a typed non-start symbol
*after trimming*. Only unreachable/unproductive symbols default to zero;
these are excluded from the retained-symbol maximum. -/
noncomputable def shortestTypedLength {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) (A : NT) (μ : U1) : Nat := by
  classical
  exact if h : ∃ k : Nat, ∃ w : Word,
      TrimmedTypedDerives G A μ w ∧ w.length = k
    then Nat.find h else 0

/-- A retained symbol has a genuine shortest terminal yield. -/
theorem shortestTypedLength_spec {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT} {A : NT} {μ : U1}
    (hret : RetainedTypedSymbol G A μ) :
    ∃ w : Word, TrimmedTypedDerives G A μ w ∧
      w.length = shortestTypedLength G A μ := by
  classical
  obtain ⟨w, hd⟩ := retained_productive hret
  have htrim := trimmed_complete hd hret
  have hex : ∃ k : Nat, ∃ v : Word,
      TrimmedTypedDerives G A μ v ∧ v.length = k :=
    ⟨w.length, w, htrim, rfl⟩
  unfold shortestTypedLength
  rw [dif_pos hex]
  exact Nat.find_spec hex

/-- The shortest length really is at most the length of *any* yield. -/
theorem shortestTypedLength_le {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT} {A : NT} {μ : U1}
    {w : Word} (h : TrimmedTypedDerives G A μ w) :
    shortestTypedLength G A μ ≤ w.length := by
  classical
  have hex : ∃ k : Nat, ∃ v : Word,
      TrimmedTypedDerives G A μ v ∧ v.length = k :=
    ⟨w.length, w, h, rfl⟩
  unfold shortestTypedLength
  rw [dif_pos hex]
  exact Nat.find_min' hex ⟨w, h, rfl⟩


/-- Any yield chosen by a length-first order (including shortlex)
has exactly the same length as shortestTypedLength. Conversely this
number is attained and is the least possible length. -/
theorem shortest_length_characterization {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT} {A : NT} {μ : U1}
    {w : Word} (hret : RetainedTypedSymbol G A μ)
    (hw : TrimmedTypedDerives G A μ w) :
    shortestTypedLength G A μ = w.length ↔
      ∀ v : Word, TrimmedTypedDerives G A μ v →
        w.length ≤ v.length := by
  constructor
  · intro hm v hv
    rw [← hm]
    exact shortestTypedLength_le hv
  · intro hmin
    obtain ⟨v, hv, hlen⟩ := shortestTypedLength_spec hret
    have hle := shortestTypedLength_le hw
    have hle' := hmin v hv
    omega

/-- Precise typed thickness: max(1, shortest terminal-yield lengths over
the finite set of retained non-start typed symbols). -/
noncomputable def typedThickness {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) : Nat := by
  classical
  exact ((retainedTypedPairs G).image
    (fun p => shortestTypedLength G p.1 p.2) ∪ {1}).max' (by simp)

/-- Every retained symbol contributes its shortest-yield length to the
maximum; unreachable symbols do not contribute. -/
theorem shortest_le_typedThickness {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) (A : NT) (μ : U1)
    (hret : RetainedTypedSymbol G A μ) :
    shortestTypedLength G A μ ≤ typedThickness G := by
  classical
  unfold typedThickness
  apply Finset.le_max'
  apply Finset.mem_union.mpr
  left
  apply Finset.mem_image.mpr
  exact ⟨(A, μ), (mem_retainedTypedPairs G A μ).mpr hret, rfl⟩

#print axioms TCSPhase4.mem_retainedTypedPairs
#print axioms TCSPhase4.shortestTypedLength_spec
#print axioms TCSPhase4.shortestTypedLength_le
#print axioms TCSPhase4.shortest_length_characterization
#print axioms TCSPhase4.shortest_le_typedThickness
end TCSPhase4
