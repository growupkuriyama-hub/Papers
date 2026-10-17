import TCSPhase5Derivations

/-! Kernel-checkable soundness of the four genuine sample-generated rules:
an induction on the *finite* grammar derivation tree. -/
namespace TCSPhase5

variable {Alphabet M : Type*}
variable [DecidableEq Alphabet] [Monoid M]

theorem sample_overlap_to_target
    (K : Finset (Word Alphabet)) (L : Set (Word Alphabet))
    (hKL : (↑K : Set (Word Alphabet)) ⊆ L)
    {x y : Word Alphabet}
    (hs : ∃ p, p ∈ SampleDistributions K x ∧
                  p ∈ SampleDistributions K y) :
    ∃ p, p ∈ Distributions L x ∧ p ∈ Distributions L y := by
  obtain ⟨p, hpx, hpy⟩ := hs
  exact ⟨p, hKL hpx, hKL hpy⟩

/-- The exact manuscript equation (soundness-invariant), proved for the
actual B/U/L derivation relation, without a substitute language relation. -/
theorem rec_factor_soundness_invariant
    (h : Word Alphabet →* M) (K : Finset (Word Alphabet))
    (L : Set (Word Alphabet))
    (hKL : (↑K : Set (Word Alphabet)) ⊆ L)
    (hSub : TypedSubstitutable h L)
    {x w : Word Alphabet} (hd : RecFactorDerives h K x w) :
    Distributions L x = Distributions L w ∧ h w = h x := by
  induction hd with
  | lexical hobs =>
      exact ⟨rfl, rfl⟩
  | @binary x y u v hx hy hxy hl hr ihl ihr =>
      constructor
      · calc
          Distributions L (x ++ y) =
              Distributions L (u ++ y) :=
            distribution_right_congruent L x u y ihl.1
          _ = Distributions L (u ++ v) :=
            distribution_left_congruent L y v u ihr.1
      · change h (u * v) = h (x * y)
        simp only [map_mul, ihl.2, ihr.2]
  | @unary x y w hx hy hxy hder ih =>
      have hxyD : Distributions L x = Distributions L y :=
        hSub x y hx.1 hy.1 hxy.1
          (sample_overlap_to_target K L hKL hxy.2)
      exact ⟨hxyD.trans ih.1, ih.2.trans hxy.1.symm⟩

/-- Main Theorem 4.2 (soundness): no additional mathematical assumptions
beyond positive-sample inclusion and fixed-h substitutability of L. -/
theorem rec_soundness
    (h : Word Alphabet →* M) (K : Finset (Word Alphabet))
    (L : Set (Word Alphabet))
    (hKL : (↑K : Set (Word Alphabet)) ⊆ L)
    (hSub : TypedSubstitutable h L) :
    RecLanguage h K ⊆ L := by
  intro w hw
  change RecStartDerives h K w at hw
  cases hw with
  | empty hmem =>
      exact hKL hmem
  | @root x w hmem hx hder =>
      have hInv :=
        rec_factor_soundness_invariant h K L hKL hSub hder
      have hctx : (([], []) : Word Alphabet × Word Alphabet) ∈
          Distributions L x := by
        change ([] ++ x ++ [] : Word Alphabet) ∈ L
        simpa using hKL hmem
      rw [hInv.1] at hctx
      simpa [Distributions] using hctx

#print axioms TCSPhase5.sample_overlap_to_target
#print axioms TCSPhase5.rec_factor_soundness_invariant
#print axioms TCSPhase5.rec_soundness

end TCSPhase5
