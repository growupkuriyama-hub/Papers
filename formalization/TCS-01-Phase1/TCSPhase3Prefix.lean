import TCSPhase3Congruence

/-! Appendix C's common opening-prefix invariant for actual grammar derivations. -/
namespace TCSPhase3
open TCSPhase1 TCSPhase2

/-- The first i symbols are unary/binary openers; the next symbol is a. -/
inductive OpeningPrefix : Nat → Word → Prop
  | atom (suffix : Word) :
      OpeningPrefix 0 (Terminal.a :: suffix)
  | ceil {i : Nat} {w : Word} (h : OpeningPrefix i w) :
      OpeningPrefix (i + 1) (Terminal.squareLeft :: w)
  | floor {i : Nat} {w : Word} (h : OpeningPrefix i w) :
      OpeningPrefix (i + 1) (Terminal.left :: w)

theorem openingPrefix_append {i : Nat} {w : Word}
    (h : OpeningPrefix i w) (suffix : Word) :
    OpeningPrefix i (w ++ suffix) := by
  induction h with
  | atom tail =>
      simpa using (OpeningPrefix.atom (tail ++ suffix))
  | ceil h ih =>
      simpa using (OpeningPrefix.ceil ih)
  | floor h ih =>
      simpa using (OpeningPrefix.floor ih)

theorem derived_opening_prefix {i : Nat} {w : Word}
    (hd : Derives i w) : OpeningPrefix i w := by
  induction hd with
  | atom => exact OpeningPrefix.atom []
  | unary hu ih =>
      simpa [unaryWord] using
        (OpeningPrefix.ceil (openingPrefix_append ih [Terminal.squareRight]))
  | @binary i u v hu hv ihU ihV =>
      simpa [binaryWord, List.append_assoc] using
        (OpeningPrefix.floor
          (openingPrefix_append ihU (v ++ [Terminal.right])))

theorem language_opening_prefix (i : Nat) (w : Word)
    (hw : w ∈ Language i) : OpeningPrefix i w :=
  derived_opening_prefix hw

#print axioms TCSPhase3.derived_opening_prefix
#print axioms TCSPhase3.language_opening_prefix

end TCSPhase3
