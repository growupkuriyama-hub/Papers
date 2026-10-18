import TCSPhase8OccurrenceLists
import TCSPhase8StartLexical

/-!
Ordered lexical/start/epsilon candidate emission from an executable
List of input words. None of the functions below converts a Finset to
a List during execution.
-/
namespace TCSPhase8
open TCSPhase5

variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet] [Monoid M]

def emitLexicalCandidates (sample : List (List Alphabet)) : List Alphabet :=
  (enumerateOccurrencesList sample).filterMap
    (fun occ => match occ.2.1 with
      | [a] => some a
      | _ => none)

def emitStartCandidates (sample : List (List Alphabet)) :
    List (List Alphabet) :=
  sample.filter (fun w => w ≠ [])

def emitStartEmpty (sample : List (List Alphabet)) : Bool :=
  decide (([] : List Alphabet) ∈ sample)

/-- Start rules are exactly the nonempty sample words, as a set. -/
theorem emitStartCandidates_toFinset_eq
    (sample : List (List Alphabet)) :
    (emitStartCandidates sample).toFinset =
      efficientStartRules sample.toFinset := by
  classical
  ext w
  simp [emitStartCandidates, efficientStartRules]

theorem emitStartEmpty_eq
    (sample : List (List Alphabet)) :
    emitStartEmpty sample = efficientStartEmpty sample.toFinset := by
  simp [emitStartEmpty, efficientStartEmpty]

/-- Lexical rules arise precisely from an observed one-letter interval. -/
theorem emitLexicalCandidates_toFinset_eq
    (sample : List (List Alphabet)) :
    (emitLexicalCandidates sample).toFinset =
      efficientLexicalRules sample.toFinset := by
  classical
  ext a
  constructor
  · intro hm
    obtain ⟨⟨u,x,v⟩,ho,hx⟩ :=
      List.mem_filterMap.mp ((List.mem_toFinset).mp hm)
    cases x with
    | nil => simp [emitLexicalCandidates] at hx
    | cons b xs =>
      cases xs with
      | nil =>
        have hb : b = a := by simpa using hx
        subst b
        have hobs := (mem_enumerateOccurrencesList_iff sample u [a] v).mp ho
        apply Finset.mem_filter.mpr
        constructor
        · simp
        · exact (efficient_observed_factors_iff sample.toFinset [a]).mpr
            ⟨by simp, u, v, by simpa using hobs.2⟩
      | cons c cs => simp at hx
  · intro hm
    have hs : [a] ∈ efficientObservedFactors sample.toFinset :=
      (Finset.mem_filter.mp hm).2
    obtain ⟨hne,u,v,hK⟩ :=
      (efficient_observed_factors_iff sample.toFinset [a]).mp hs
    apply List.mem_toFinset.mpr
    apply List.mem_filterMap.mpr
    refine ⟨(u,[a],v), ?_, rfl⟩
    exact (mem_enumerateOccurrencesList_iff sample u [a] v).mpr
      ⟨by simp, by simpa using hK⟩

#print axioms TCSPhase8.emitStartCandidates_toFinset_eq
#print axioms TCSPhase8.emitStartEmpty_eq
#print axioms TCSPhase8.emitLexicalCandidates_toFinset_eq

end TCSPhase8
