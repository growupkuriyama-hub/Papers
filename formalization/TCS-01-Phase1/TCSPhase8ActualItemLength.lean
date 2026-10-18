import TCSPhase8ActualTrieCost
import TCSPhase8BinaryRuleLists
import TCSPhase8UnaryRuleLists
import TCSPhase8RuleListCounts

/-!
Every letter in a genuine emitted candidate is charged to some concrete
input sample occurrence. This discharges the previously conditional
linear-key-size premise for the real trie insertion program, but does
NOT account for candidate construction, lookup, decoding, or output cost.
-/
namespace TCSPhase8
open TCSPhase5

variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Monoid M] [DecidableEq M]

theorem observed_factor_length_le_encodedListSample
    (sample : List (List Alphabet)) (x : List Alphabet)
    (hx : ObservedFactor sample.toFinset x) :
    x.length ≤ encodedListSample sample := by
  obtain ⟨_,u,v,hK⟩ := hx
  have hw : u ++ x ++ v ∈ sample := by
    simpa using hK
  have hlen := word_length_le_encodedListSample sample (u++x++v) hw
  simp only [List.length_append] at hlen
  omega

/-- Every tagged item of the actual operational emitter has at most
twice the encoded sample size in source letters. The extra +1 allows
the lexical singleton and the empty sample case uniformly. -/
theorem emitAllRecItems_letterCount_le
    (t : LetterTable Alphabet M) (sample : List (List Alphabet)) :
    ∀ r ∈ emitAllRecItems t sample,
      r.letterCount ≤ 2 * (encodedListSample sample + 1) := by
  intro r hr
  change r ∈ (buildListedRecGrammar t sample).items at hr
  unfold ListedRecGrammar.items buildListedRecGrammar at hr
  simp only [List.mem_append] at hr
  rcases hr with hnt | hb | hu | hl | hs | heps
  · obtain ⟨st,hst,heq⟩ := List.mem_map.mp hnt
    rcases st with ⟨u,x,v⟩
    cases heq
    have hp := (mem_enumerateOccurrencesList_iff sample u x v).mp hst
    have hword :=
      word_length_le_encodedListSample sample (u++x++v) hp.2
    simp only [List.length_append] at hword
    change x.length ≤ 2*(encodedListSample sample+1)
    omega
  · obtain ⟨p,hp,heq⟩ := List.mem_map.mp hb
    rcases p with ⟨z,x,y⟩
    cases heq
    have hspec := (efficient_binary_spec sample.toFinset z x y).mp
      ((mem_emitBinaryCandidates_iff sample z x y).mp hp)
    rcases hspec with ⟨hzw,_,_,hz⟩
    have hlen := observed_factor_length_le_encodedListSample sample z hz
    have hsum : z.length = x.length + y.length := by
      simpa [hzw, List.length_append]
    change z.length + x.length + y.length ≤
      2*(encodedListSample sample+1)
    omega
  · obtain ⟨p,hp,heq⟩ := List.mem_map.mp hu
    rcases p with ⟨x,y⟩
    cases heq
    have hmem := (mem_emitUnaryCandidates_iff t sample x y).mp hp
    obtain ⟨⟨⟨u,x',v⟩,w⟩, hfilter, heq⟩ := Finset.mem_image.mp hmem
    have hd := Finset.mem_filter.mp hfilter
    have hpair := Finset.mem_product.mp hd.1
    have hxeq : x' = x := congrArg Prod.fst heq
    have hyeq : middle u v w = y := congrArg Prod.snd heq
    have hocc := (mem_enumerateOccurrences_iff sample.toFinset u x' v).mp
      hpair.1
    have hobsx : ObservedFactor sample.toFinset x := by
      rw [← hxeq]
      exact ⟨hocc.1,u,v,hocc.2⟩
    have hobsy : ObservedFactor sample.toFinset y := by
      refine ⟨?_,u,v,?_⟩
      · rw [← hyeq]
        exact hd.2.1
      · rw [← hyeq, hd.2.2.1]
        exact hpair.2
    have hxlen := observed_factor_length_le_encodedListSample sample x hobsx
    have hylen := observed_factor_length_le_encodedListSample sample y hobsy
    change x.length + y.length ≤ 2*(encodedListSample sample+1)
    omega
  · obtain ⟨a,_,heq⟩ := List.mem_map.mp hl
    cases heq
    change 1 ≤ 2*(encodedListSample sample+1)
    omega
  · obtain ⟨w,hw,heq⟩ := List.mem_map.mp hs
    cases heq
    have hmem : w ∈ sample := (List.mem_filter.mp hw).1
    have hlen := word_length_le_encodedListSample sample w hmem
    change w.length ≤ 2*(encodedListSample sample+1)
    omega
  · cases hh : emitStartEmpty sample with
    | false => simp [hh] at heps
    | true =>
        simp [hh] at heps
        subst r
        simp [RecItem.letterCount]

/-- Unconditional quartic bound on the counted bit-insertion visits of
the real six-field candidate stream with complete injective encoding.
This is not yet the full reconstruction running time. -/
theorem buildItemTrie_insertion_steps_fourth
    (c : LetterNumbering Alphabet) (t : LetterTable Alphabet M)
    (sample : List (List Alphabet)) :
    (buildItemTrie c t sample).2 ≤
      (18 * tokenBound c + 3) * (encodedListSample sample + 1)^4 := by
  exact buildItemTrie_steps_le_fourth_if_linear_letters c t sample
    (emitAllRecItems_letterCount_le t sample)

#print axioms TCSPhase8.observed_factor_length_le_encodedListSample
#print axioms TCSPhase8.emitAllRecItems_letterCount_le
#print axioms TCSPhase8.buildItemTrie_insertion_steps_fourth
end TCSPhase8
