import TCSPhase5Consistency

namespace TCSPhase5
variable {Alphabet M : Type*}
variable [DecidableEq Alphabet] [Monoid M]

/-- Every genuine (B)(U)(L) derivation survives enlargement of K. -/
theorem rec_factor_mono
    (h : Word Alphabet →* M)
    {K K' : Finset (Word Alphabet)} (hKK : K ⊆ K')
    {x w : Word Alphabet} (hd : RecFactorDerives h K x w) :
    RecFactorDerives h K' x w := by
  induction hd with
  | lexical hobs =>
      exact RecFactorDerives.lexical (observed_mono hKK hobs)
  | binary hx hy hxy hl hr ihl ihr =>
      exact RecFactorDerives.binary
        (observed_mono hKK hx)
        (observed_mono hKK hy)
        (observed_mono hKK hxy) ihl ihr
  | unary hx hy hxy hd ih =>
      exact RecFactorDerives.unary
        (observed_mono hKK hx)
        (observed_mono hKK hy)
        (direct_similar_mono h hKK hxy) ih

/-- Sample monotonicity of the actual generated language; no equality
of finite grammar objects and no substitutability hypothesis. -/
theorem rec_monotone
    (h : Word Alphabet →* M)
    {K K' : Finset (Word Alphabet)} (hKK : K ⊆ K') :
    RecLanguage h K ⊆ RecLanguage h K' := by
  intro w hw
  change RecStartDerives h K w at hw
  change RecStartDerives h K' w
  cases hw with
  | empty hm =>
      exact RecStartDerives.empty (hKK hm)
  | root hm hn hd =>
      exact RecStartDerives.root (hKK hm) hn
        (rec_factor_mono h hKK hd)

#print axioms TCSPhase5.rec_factor_mono
#print axioms TCSPhase5.rec_monotone

end TCSPhase5
