import TCSPhase6WitnessLengths

/-! Explicit encoded sample size: distinct words cost their length plus one.
No disjointness assumption is used about the witness families. -/
namespace TCSPhase6
open TCSPhase5B
variable {Alphabet NT M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Fintype NT] [DecidableEq NT]
variable [Monoid M] [Fintype M] [DecidableEq M]

def encodedSize (W : Finset (List Alphabet)) : Nat :=
  ∑ w ∈ W, w.length + 1

/-- All quantitative work except the separate context-compression
proof is discharged here; this theorem is intentionally conditional. -/
theorem encoded_size_le_of_context_bound
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (hctx : ContextCompressionBound G h) :
    encodedSize (PositiveWitnesses G h) ≤
      (Fintype.card NT * Fintype.card M +
        G.terminalRules.card +
        G.binaryRules.card * Fintype.card M ^ 2 + 1) *
      ((Fintype.card NT * Fintype.card M + 1) *
        typedThickness G h + 1) := by
  classical
  let W := PositiveWitnesses G h
  let n := (finiteTypedRefinement G h).symbols.card
  let nMax := Fintype.card NT * Fintype.card M
  let countMax := nMax + G.terminalRules.card +
      G.binaryRules.card * Fintype.card M ^ 2 + 1
  let τ := typedThickness G h
  have hn : n ≤ nMax := typed_symbols_card_le G h
  have hcount : W.card ≤ countMax :=
    positive_witnesses_card_le G h
  have hlength : ∀ w ∈ W, w.length ≤ (n+1)*τ :=
    witness_word_length_le_of_context_bound G h hctx
  have hterm : ∀ w ∈ W, w.length + 1 ≤ (n+1)*τ+1 := by
    intro w hw
    exact Nat.add_le_add_right (hlength w hw) 1
  have hsumbound :
      encodedSize W ≤ W.card * ((n+1)*τ + 1) := by
    unfold encodedSize
    calc
      (∑ w ∈ W, w.length + 1) ≤
          ∑ _w ∈ W, ((n+1)*τ + 1) :=
        by simpa only [] using (Finset.sum_le_sum hterm)
      _ = W.card * ((n+1)*τ + 1) := by simp
  have hfactor : (n+1)*τ+1 ≤ (nMax+1)*τ+1 := by
    have hmul := Nat.mul_le_mul_right τ (Nat.add_le_add_right hn 1)
    omega
  calc
    encodedSize W ≤ W.card * ((n+1)*τ + 1) := hsumbound
    _ ≤ countMax * ((n+1)*τ + 1) :=
      Nat.mul_le_mul_right _ hcount
    _ ≤ countMax * ((nMax+1)*τ + 1) :=
      Nat.mul_le_mul_left _ hfactor

#print axioms TCSPhase6.encoded_size_le_of_context_bound
end TCSPhase6
