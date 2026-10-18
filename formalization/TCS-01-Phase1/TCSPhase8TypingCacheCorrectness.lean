import TCSPhase8TypingCache

/-!
# Correctness of the incrementally cached monoid values
Each stored value arises from an actual, nonempty prefix of the scanned suffix.
Combining this fact with the preexisting `codeWord_eq_h` theorem gives
correct typing for the source paper's monoid homomorphism.
-/
namespace TCSPhase8

variable {Alphabet M : Type*} [Monoid M]

theorem cachedScan_sound (t : LetterTable Alphabet M) (acc : M)
    (w : List Alphabet) :
    ∀ r ∈ (cachedScan t acc w).1,
      ∃ p suffix, p ≠ [] ∧ w = p ++ suffix ∧
        r = acc * codeWord t p := by
  induction w generalizing acc with
  | nil =>
      intro r hr
      simp [cachedScan] at hr
  | cons a rest ih =>
      intro r hr
      have hmem : r = acc * t.letter a ∨
          r ∈ (cachedScan t (acc * t.letter a) rest).1 := by
        simpa [cachedScan] using hr
      rcases hmem with hfirst | htail
      · subst r
        refine ⟨[a], rest, by simp, rfl, ?_⟩
        simp [codeWord]
      · obtain ⟨p, suffix, hp, hword, hvalue⟩ :=
          ih (acc * t.letter a) r htail
        refine ⟨a::p, suffix, by simp, ?_, ?_⟩
        · simp [hword]
        · rw [hvalue]
          simp [codeWord, mul_assoc]

/-- No stored type is fabricated: for every cached value, there is a
genuine positive-length factor beginning at this scan position and
the cached value equals its abstract monoid type. -/
theorem cachedScan_sound_h
    (h : List Alphabet →* M)
    (t : LetterTable Alphabet M)
    (ht : ∀ a, t.letter a = h [a])
    (w : List Alphabet) :
    ∀ r ∈ (cachedScan t 1 w).1,
      ∃ p suffix, p ≠ [] ∧ w = p ++ suffix ∧ r = h p := by
  intro r hr
  obtain ⟨p, suffix, hp, hword, hvalue⟩ :=
    cachedScan_sound t 1 w r hr
  refine ⟨p, suffix, hp, hword, ?_⟩
  simpa [codeWord_eq_h h t ht p] using hvalue

#print axioms TCSPhase8.cachedScan_sound
#print axioms TCSPhase8.cachedScan_sound_h
end TCSPhase8
