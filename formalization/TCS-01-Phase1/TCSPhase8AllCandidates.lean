import TCSPhase8RecItem
import TCSPhase8RuleListCounts

/-!
Count the *raw, duplicate-tolerant List output* of all six grammar
fields, not a Finset of productions. Constants are deliberately
generous to keep each field's charge explicit.
-/
namespace TCSPhase8

variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet]
variable [Monoid M] [DecidableEq M]

theorem emitAllRecItems_length_le
    (t : LetterTable Alphabet M) (sample : List (List Alphabet)) :
    (emitAllRecItems t sample).length ≤
      3 * (encodedListSample sample + 1)^3 := by
  let n := encodedListSample sample
  have hocc :
      (enumerateOccurrencesList sample).length ≤ n^2 :=
    enumerateOccurrencesList_length_le_square sample
  have hbin :
      (emitBinaryCandidates sample).length ≤ n^2 * (n+1) :=
    emitBinaryCandidates_length_le_cubic sample
  have hun :
      (emitUnaryCandidates t sample).length ≤ n^3 :=
    emitUnaryCandidates_length_le_cube t sample
  have hlex :
      (emitLexicalCandidates sample).length ≤
        (enumerateOccurrencesList sample).length := by
    unfold emitLexicalCandidates
    exact List.length_filterMap_le _ _
  have hstart :
      (emitStartCandidates sample).length ≤ sample.length := by
    unfold emitStartCandidates
    exact List.length_filter_le _ _
  have hsamp : sample.length ≤ n :=
    sample_length_le_encodedListSample sample
  have heq :
      (emitAllRecItems t sample).length =
        (enumerateOccurrencesList sample).length +
        (emitBinaryCandidates sample).length +
        (emitUnaryCandidates t sample).length +
        (emitLexicalCandidates sample).length +
        (emitStartCandidates sample).length +
        (if emitStartEmpty sample then 1 else 0) := by
    cases h : emitStartEmpty sample <;>
      simp [emitAllRecItems, ListedRecGrammar.items, buildListedRecGrammar, h] <;>
      omega
  rw [heq]
  have hflag : (if emitStartEmpty sample then 1 else 0) ≤ 1 := by
    split <;> omega
  calc
    _ ≤ n^2 + n^2*(n+1) + n^3 + n^2 + n + 1 := by
      omega
    _ ≤ 3 * (n+1)^3 := by nlinarith

#print axioms TCSPhase8.emitAllRecItems_length_le
end TCSPhase8
