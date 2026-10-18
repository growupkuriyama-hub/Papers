import TCSPhase8Occurrences
import TCSPhase8Typing
import TCSPhase5FiniteDerivation

/-! Direct overlap unary rules from a pair (observed occurrence, sample
word). No transitive closure or global candidate-word enumeration. -/
namespace TCSPhase8
open TCSPhase5

variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Monoid M] [DecidableEq M]

/-- The unique middle slice proposed by one left/right context in a word. -/
def middle (u v w : List Alphabet) : List Alphabet :=
  (w.drop u.length).take (w.length-u.length-v.length)

theorem middle_append (u x v : List Alphabet) :
    middle u v (u ++ x ++ v) = x := by
  have hlen : (u ++ x ++ v).length - u.length - v.length = x.length := by
    simp [List.length_append]
  simp [middle, hlen]

/-- The only possible candidate for each occurrence and sample-word pair. -/
def efficientUnaryRules (t : LetterTable Alphabet M)
    (K : Finset (List Alphabet)) :
    Finset (List Alphabet × List Alphabet) :=
  (((enumerateOccurrences K).product K).filter
    (fun q =>
      let u := q.1.1
      let x := q.1.2.1
      let v := q.1.2.2
      let y := middle u v q.2
      y ≠ [] ∧ u ++ y ++ v = q.2 ∧ codeWord t x = codeWord t y)).image
    (fun q => (q.1.2.1, middle q.1.1 q.1.2.2 q.2))

/-- Exact (U) rule equality under a constructively supplied letter table
matching h on every singleton word. -/
theorem efficient_unary_rules_eq
    (h : List Alphabet →* M) (t : LetterTable Alphabet M)
    (ht : ∀ a, t.letter a = h [a])
    (K : Finset (List Alphabet)) :
    efficientUnaryRules t K = (makeRecGrammar h K).unaryRules := by
  classical
  ext p
  rcases p with ⟨x,y⟩
  rw [rec_unary_rule_iff]
  constructor
  · intro hmem
    obtain ⟨⟨⟨u,x',v⟩,w⟩, hcandidate, heq⟩ :=
      Finset.mem_image.mp hmem
    have hpair := Finset.mem_filter.mp hcandidate
    have hdata := Finset.mem_product.mp hpair.1
    have hocc := (mem_enumerateOccurrences_iff K u x' v).mp hdata.1
    have hxx : x' = x := congrArg Prod.fst heq
    have hyy : middle u v w = y := congrArg Prod.snd heq
    have hcondition : middle u v w ≠ [] ∧
        u ++ middle u v w ++ v = w ∧
        codeWord t x' = codeWord t (middle u v w) := hpair.2
    have hobsx : ObservedFactor K x := by
      rw [← hxx]
      exact ⟨hocc.1,u,v,hocc.2⟩
    have hobsy : ObservedFactor K y := by
      refine ⟨?_,u,v,?_⟩
      · rw [← hyy]
        exact hcondition.1
      · rw [← hyy, hcondition.2.1]
        exact hdata.2
    have htypes : h x = h y := by
      have hcode : codeWord t x = codeWord t y := by
        simpa [hxx,hyy] using hcondition.2.2
      rw [codeWord_eq_h h t ht x,codeWord_eq_h h t ht y] at hcode
      exact hcode
    refine ⟨hobsx,hobsy,htypes,⟨(u,v),?_,?_⟩⟩
    · change u ++ x ++ v ∈ K
      rw [← hxx]
      exact hocc.2
    · change u ++ y ++ v ∈ K
      rw [← hyy, hcondition.2.1]
      exact hdata.2
  · rintro ⟨hx,hy,hdir⟩
    obtain ⟨htype,⟨⟨u,v⟩,hcx,hcy⟩⟩ := hdir
    change u ++ x ++ v ∈ K at hcx
    change u ++ y ++ v ∈ K at hcy
    apply Finset.mem_image.mpr
    refine ⟨((u,x,v),u++y++v), ?_, ?_⟩
    · apply Finset.mem_filter.mpr
      constructor
      · exact Finset.mem_product.mpr
          ⟨(mem_enumerateOccurrences_iff K u x v).mpr
            ⟨hx.1,hcx⟩, hcy⟩
      · dsimp
        rw [middle_append]
        refine ⟨hy.1,rfl,?_⟩
        rw [codeWord_eq_h h t ht x,codeWord_eq_h h t ht y]
        exact htype
    · simpa [List.append_assoc] using (middle_append u y v)

#print axioms TCSPhase8.middle_append
#print axioms TCSPhase8.efficient_unary_rules_eq
end TCSPhase8
