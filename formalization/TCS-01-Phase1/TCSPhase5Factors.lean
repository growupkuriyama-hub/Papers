import TCSPhase4Main

/-! Finite positive substrings and sample contexts for the actual
(B)(U)(L)(S) reconstruction of the TCS manuscript (Section 4). -/
namespace TCSPhase5

variable {Alphabet : Type*} {M : Type*}

/-- The free word monoid is concatenation. -/
instance (Alphabet : Type*) : Monoid (List Alphabet) where
  one := []
  mul := List.append
  one_mul := by intro x; rfl
  mul_one := by intro x; exact List.append_nil x
  mul_assoc := by intro x y z; exact List.append_assoc x y z

abbrev Word (Alphabet : Type*) := List Alphabet

/-- A nonempty CONTIGUOUS factor of some sample word. -/
def ObservedFactor (K : Finset (Word Alphabet))
    (x : Word Alphabet) : Prop :=
  x ≠ [] ∧ ∃ u v : Word Alphabet, u ++ x ++ v ∈ K

/-- Exactly the sample-level two-sided distribution, with no quotienting. -/
def SampleDistributions (K : Finset (Word Alphabet))
    (x : Word Alphabet) : Set (Word Alphabet × Word Alphabet) :=
  {p | p.1 ++ x ++ p.2 ∈ K}

/-- Arbitrary-target two-sided distributions. -/
def Distributions (L : Set (Word Alphabet))
    (x : Word Alphabet) : Set (Word Alphabet × Word Alphabet) :=
  {p | p.1 ++ x ++ p.2 ∈ L}

/-- Direct, NONTRANSITIVE sample overlap, with equal h-types. -/
def DirectSimilar [Monoid M] (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) (x y : Word Alphabet) : Prop :=
  h x = h y ∧
    ∃ p : Word Alphabet × Word Alphabet,
      p ∈ SampleDistributions K x ∧
      p ∈ SampleDistributions K y

/-- Fixed-typing substitutability for NONEMPTY factors, over any alphabet
and any target monoid; no regularity or context-freeness premise. -/
def TypedSubstitutable [Monoid M] (h : Word Alphabet →* M)
    (L : Set (Word Alphabet)) : Prop :=
  ∀ x y : Word Alphabet, x ≠ [] → y ≠ [] → h x = h y →
    (∃ p, p ∈ Distributions L x ∧ p ∈ Distributions L y) →
    Distributions L x = Distributions L y

theorem observed_nonempty {K : Finset (Word Alphabet)}
    {x : Word Alphabet} (h : ObservedFactor K x) : x ≠ [] :=
  h.1

theorem sample_word_observed [DecidableEq Alphabet]
    {K : Finset (Word Alphabet)} {x : Word Alphabet}
    (hx : x ∈ K) (hne : x ≠ []) : ObservedFactor K x := by
  refine ⟨hne, [], [], ?_⟩
  simpa using hx

theorem observed_of_infix [DecidableEq Alphabet]
    {K : Finset (Word Alphabet)} {x y : Word Alphabet}
    (hx : ObservedFactor K x) (hy : y ≠ [])
    (hfactor : ∃ a b : Word Alphabet, x = a ++ y ++ b) :
    ObservedFactor K y := by
  obtain ⟨_, u, v, hmem⟩ := hx
  obtain ⟨a, b, hab⟩ := hfactor
  refine ⟨hy, u ++ a, b ++ v, ?_⟩
  simpa [hab, List.append_assoc] using hmem

theorem observed_mono [DecidableEq Alphabet]
    {K K' : Finset (Word Alphabet)}
    (hKK : K ⊆ K') {x : Word Alphabet}
    (hx : ObservedFactor K x) : ObservedFactor K' x := by
  obtain ⟨hne,u,v,hmem⟩ := hx
  exact ⟨hne,u,v,hKK hmem⟩

theorem sample_distributions_mono [DecidableEq Alphabet]
    {K K' : Finset (Word Alphabet)} (hKK : K ⊆ K')
    (x : Word Alphabet) :
    SampleDistributions K x ⊆ SampleDistributions K' x := by
  intro p hp
  exact hKK hp

theorem direct_similar_mono [DecidableEq Alphabet] [Monoid M]
    (h : Word Alphabet →* M)
    {K K' : Finset (Word Alphabet)} (hKK : K ⊆ K')
    {x y : Word Alphabet}
    (hs : DirectSimilar h K x y) : DirectSimilar h K' x y := by
  obtain ⟨ht,p,hx,hy⟩ := hs
  exact ⟨ht,p,hKK hx,hKK hy⟩

theorem distribution_left_congruent (L : Set (Word Alphabet))
    (x y z : Word Alphabet)
    (hxy : Distributions L x = Distributions L y) :
    Distributions L (z ++ x) = Distributions L (z ++ y) := by
  ext p
  have h := Set.ext_iff.mp hxy (p.1 ++ z, p.2)
  simpa [Distributions, List.append_assoc] using h

theorem distribution_right_congruent (L : Set (Word Alphabet))
    (x y z : Word Alphabet)
    (hxy : Distributions L x = Distributions L y) :
    Distributions L (x ++ z) = Distributions L (y ++ z) := by
  ext p
  have h := Set.ext_iff.mp hxy (p.1, z ++ p.2)
  simpa [Distributions, List.append_assoc] using h

#print axioms TCSPhase5.observed_of_infix
#print axioms TCSPhase5.observed_mono
#print axioms TCSPhase5.direct_similar_mono
#print axioms TCSPhase5.distribution_left_congruent
#print axioms TCSPhase5.distribution_right_congruent

end TCSPhase5
