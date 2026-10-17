import TCSPhase5Factors

/-! Independent inductive (B)(U)(L)(S) derivations of the real
substring-indexed reconstruction. All non-start nodes are explicitly
required to be positive observed factors of the finite sample. -/
namespace TCSPhase5

variable {Alphabet : Type*} {M : Type*}
variable [DecidableEq Alphabet] [Monoid M]

/-- The (B)(U)(L) derivation relation; these are the sole constructors.
Unary cycles/self-loops are permitted, but derivation trees remain finite. -/
inductive RecFactorDerives (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) :
    Word Alphabet → Word Alphabet → Prop
  | lexical {c : Alphabet}
      (hobs : ObservedFactor K [c]) :
      RecFactorDerives h K [c] [c]
  | binary {x y u v : Word Alphabet}
      (hx : ObservedFactor K x) (hy : ObservedFactor K y)
      (hxy : ObservedFactor K (x ++ y))
      (hleft : RecFactorDerives h K x u)
      (hright : RecFactorDerives h K y v) :
      RecFactorDerives h K (x ++ y) (u ++ v)
  | unary {x y w : Word Alphabet}
      (hx : ObservedFactor K x) (hy : ObservedFactor K y)
      (hxy : DirectSimilar h K x y)
      (hder : RecFactorDerives h K y w) :
      RecFactorDerives h K x w

/-- The only start rules are S -> [w] for observed positive sample
members, plus S -> epsilon exactly when epsilon occurs in K. -/
inductive RecStartDerives (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) : Word Alphabet → Prop
  | empty (hmem : ([] : Word Alphabet) ∈ K) :
      RecStartDerives h K []
  | root {x w : Word Alphabet}
      (hmem : x ∈ K) (hx : x ≠ [])
      (hder : RecFactorDerives h K x w) :
      RecStartDerives h K w

def RecLanguage (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) : Set (Word Alphabet) :=
  {w | RecStartDerives h K w}

/-- Every non-start yield is nonempty: no epsilon lexical or binary
rules, and unary rules do not create epsilon yields. -/
theorem rec_factor_nonempty {h : Word Alphabet →* M}
    {K : Finset (Word Alphabet)} {x w : Word Alphabet}
    (hd : RecFactorDerives h K x w) : w ≠ [] := by
  induction hd with
  | lexical hobs => simp
  | binary hx hy hxy hl hr ihl ihr =>
      intro he
      exact ihl ((List.append_eq_nil_iff.mp he).1)
  | unary hx hy hxy hd ih =>
      exact ih

/-- All factor nonterminal indices occurring at the root are actual
positive observed sample factors, including after unary steps. -/
theorem rec_factor_root_observed {h : Word Alphabet →* M}
    {K : Finset (Word Alphabet)} {x w : Word Alphabet}
    (hd : RecFactorDerives h K x w) : ObservedFactor K x := by
  cases hd with
  | lexical hobs => exact hobs
  | binary hx hy hxy hl hr => exact hxy
  | unary hx hy hxy hd => exact hx

#print axioms TCSPhase5.rec_factor_nonempty
#print axioms TCSPhase5.rec_factor_root_observed

end TCSPhase5
