import TCSPhase8CandidateBounds
import TCSPhase8BinaryEnumeration
import TCSPhase8UnaryEnumeration

/-! Candidate-count inequalities, separate from a time-cost semantics. -/
namespace TCSPhase8
open TCSPhase5
variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Monoid M] [DecidableEq M]

theorem sample_card_le_encoded_size (K : Finset (List Alphabet)) :
    K.card ≤ TCSPhase1.encodedSize K := by
  classical
  calc
    K.card = ∑ _w ∈ K, (1 : Nat) := by simp
    _ ≤ ∑ w ∈ K, (w.length+1) := by
      apply Finset.sum_le_sum
      intro w hw
      omega
    _ = TCSPhase1.encodedSize K := rfl

/-- Number of pairs fed to the direct-overlap unary candidate constructor. -/
theorem unary_candidate_pairs_card_le_cube (K : Finset (List Alphabet)) :
    ((enumerateOccurrences K).product K).card ≤
      (TCSPhase1.encodedSize K)^3 := by
  classical
  rw [Finset.card_product]
  have hocc := enumerateOccurrences_card_le_square K
  have hk := sample_card_le_encoded_size K
  calc
    (enumerateOccurrences K).card * K.card ≤
      (TCSPhase1.encodedSize K)^2 * (TCSPhase1.encodedSize K) :=
        Nat.mul_le_mul hocc hk
    _ = (TCSPhase1.encodedSize K)^3 := by ring

/-- Even before coalescing identical rules, the indexed binary collection
has a cubic polynomial cardinal bound. -/
theorem binary_rules_card_le_cubic (K : Finset (List Alphabet)) :
    (efficientBinaryRules K).card ≤
      (TCSPhase1.encodedSize K)^2 *
        (TCSPhase1.encodedSize K + 1) := by
  classical
  let n := TCSPhase1.encodedSize K
  have hfac : (efficientObservedFactors K).card ≤ n^2 := by
    calc
      (efficientObservedFactors K).card ≤
        (enumerateOccurrences K).card := Finset.card_image_le
      _ ≤ n^2 := enumerateOccurrences_card_le_square K
  calc
    (efficientBinaryRules K).card ≤
        ∑ z ∈ efficientObservedFactors K,
          (((splits z).filter (fun p => p.1 ≠ [] ∧ p.2 ≠ [])).image
            (fun p => (z,p.1,p.2))).card := by
      unfold efficientBinaryRules
      exact Finset.card_biUnion_le
    _ ≤ ∑ _z ∈ efficientObservedFactors K, n+1 := by
      apply Finset.sum_le_sum
      intro z hz
      have h1 :
          (((splits z).filter (fun p => p.1 ≠ [] ∧ p.2 ≠ [])).image
            (fun p => (z,p.1,p.2))).card ≤
            ((splits z).filter (fun p => p.1 ≠ [] ∧ p.2 ≠ [])).card :=
        Finset.card_image_le
      have h2 :
          ((splits z).filter (fun p => p.1 ≠ [] ∧ p.2 ≠ [])).card ≤
            (splits z).card := Finset.card_filter_le _ _
      have h3 := splits_card_le z
      have h4 : z.length ≤ n :=
        observed_length_le K ((efficient_observed_factors_iff K z).mp hz)
      omega
    _ = (efficientObservedFactors K).card * (n+1) := by simp
    _ ≤ n^2 * (n+1) := Nat.mul_le_mul_right (n+1) hfac

#print axioms TCSPhase8.sample_card_le_encoded_size
#print axioms TCSPhase8.unary_candidate_pairs_card_le_cube
#print axioms TCSPhase8.binary_rules_card_le_cubic
end TCSPhase8
