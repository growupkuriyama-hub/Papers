import TCSPhase8Occurrences
import TCSPhase5FiniteDerivation

/-! Binary rules split actually observed substrings, without global word generation. -/
namespace TCSPhase8
open TCSPhase5
variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet] [Monoid M]

def efficientBinaryRules (K : Finset (List Alphabet)) :
    Finset (List Alphabet × List Alphabet × List Alphabet) :=
  (efficientObservedFactors K).biUnion (fun z =>
    ((splits z).filter (fun p => p.1 ≠ [] ∧ p.2 ≠ [])).image
      (fun p => (z,p.1,p.2)))

theorem efficient_binary_spec (K : Finset (List Alphabet))
    (z x y : List Alphabet) :
    (z,x,y) ∈ efficientBinaryRules K ↔
      z = x ++ y ∧ ObservedFactor K x ∧
      ObservedFactor K y ∧ ObservedFactor K z := by
  classical
  constructor
  · intro hm
    obtain ⟨z',hz',hrule⟩ := Finset.mem_biUnion.mp hm
    obtain ⟨⟨x',y'⟩, hpart, heq⟩ := Finset.mem_image.mp hrule
    have hp := Finset.mem_filter.mp hpart
    have hzz : z' = z := congrArg Prod.fst heq
    have hxy : (x',y') = (x,y) := congrArg Prod.snd heq
    have hxx : x' = x := congrArg Prod.fst hxy
    have hyy : y' = y := congrArg Prod.snd hxy
    have hzw : z = x ++ y := by
      have hs := (mem_splits_iff z' x' y').mp hp.1
      simpa [hzz,hxx,hyy] using hs
    have hz : ObservedFactor K z := by
      simpa [hzz] using (efficient_observed_factors_iff K z').mp hz'
    have hxne : x ≠ [] := by simpa [hxx] using hp.2.1
    have hyne : y ≠ [] := by simpa [hyy] using hp.2.2
    have hx : ObservedFactor K x :=
      observed_of_infix hz hxne ⟨[],y,by simpa using hzw⟩
    have hy : ObservedFactor K y :=
      observed_of_infix hz hyne ⟨x,[],by simpa using hzw⟩
    exact ⟨hzw,hx,hy,hz⟩
  · rintro ⟨hzw,hx,hy,hz⟩
    apply Finset.mem_biUnion.mpr
    refine ⟨z, (efficient_observed_factors_iff K z).mpr hz, ?_⟩
    apply Finset.mem_image.mpr
    exact ⟨(x,y), Finset.mem_filter.mpr
      ⟨(mem_splits_iff z x y).mpr hzw, hx.1, hy.1⟩, rfl⟩

theorem efficient_binary_rules_eq
    (h : List Alphabet →* M) (K : Finset (List Alphabet)) :
    efficientBinaryRules K = (makeRecGrammar h K).binaryRules := by
  classical
  ext r
  rcases r with ⟨z,x,y⟩
  rw [efficient_binary_spec, rec_binary_rule_iff]

#print axioms TCSPhase8.efficient_binary_spec
#print axioms TCSPhase8.efficient_binary_rules_eq
end TCSPhase8
