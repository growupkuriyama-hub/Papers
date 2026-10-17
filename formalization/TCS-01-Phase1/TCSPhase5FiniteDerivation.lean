import TCSPhase5Grammar

/-! Independent derivations from the actually constructed *finite*
B/U/L/S rule collections, and their precise correspondence to RecFactorDerives
and RecStartDerives used in the learning theorems. -/
namespace TCSPhase5
variable {Alphabet M : Type*}
variable [Fintype Alphabet] [DecidableEq Alphabet] [Monoid M]

inductive FiniteRecFactorDerives (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) : Word Alphabet → Word Alphabet → Prop
  | lexical {a : Alphabet}
      (hr : a ∈ (makeRecGrammar h K).lexicalRules) :
      FiniteRecFactorDerives h K [a] [a]
  | binary {x y u v : Word Alphabet}
      (hr : (x ++ y,x,y) ∈ (makeRecGrammar h K).binaryRules)
      (hl : FiniteRecFactorDerives h K x u)
      (hright : FiniteRecFactorDerives h K y v) :
      FiniteRecFactorDerives h K (x ++ y) (u ++ v)
  | unary {x y w : Word Alphabet}
      (hr : (x,y) ∈ (makeRecGrammar h K).unaryRules)
      (hd : FiniteRecFactorDerives h K y w) :
      FiniteRecFactorDerives h K x w

inductive FiniteRecStartDerives (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) : Word Alphabet → Prop
  | empty (hr : (makeRecGrammar h K).startEmpty = true) :
      FiniteRecStartDerives h K []
  | root {x w : Word Alphabet}
      (hr : x ∈ (makeRecGrammar h K).startRules)
      (hd : FiniteRecFactorDerives h K x w) :
      FiniteRecStartDerives h K w

/-- The finite B/U/L grammar has *exactly* the same derivation trees
as the independent inductive B/U/L rules. -/
theorem finite_rec_factor_iff (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) (x w : Word Alphabet) :
    FiniteRecFactorDerives h K x w ↔ RecFactorDerives h K x w := by
  constructor
  · intro hd
    induction hd with
    | lexical hr =>
        exact RecFactorDerives.lexical
          ((rec_lexical_rule_iff h K _).mp hr)
    | binary hr hl hright ihl ihr =>
        obtain ⟨_,hx,hy,hxy⟩ :=
          (rec_binary_rule_iff h K _ _ _).mp hr
        exact RecFactorDerives.binary hx hy hxy ihl ihr
    | unary hr hd ih =>
        obtain ⟨hx,hy,hs⟩ :=
          (rec_unary_rule_iff h K _ _).mp hr
        exact RecFactorDerives.unary hx hy hs ih
  · intro hd
    induction hd with
    | lexical hr =>
        exact FiniteRecFactorDerives.lexical
          ((rec_lexical_rule_iff h K _).mpr hr)
    | binary hx hy hxy hl hright ihl ihr =>
        exact FiniteRecFactorDerives.binary
          ((rec_binary_rule_iff h K _ _ _).mpr
            ⟨rfl,hx,hy,hxy⟩) ihl ihr
    | unary hx hy hs hd ih =>
        exact FiniteRecFactorDerives.unary
          ((rec_unary_rule_iff h K _ _).mpr
            ⟨hx,hy,hs⟩) ih

theorem finite_rec_start_iff (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) (w : Word Alphabet) :
    FiniteRecStartDerives h K w ↔ RecStartDerives h K w := by
  constructor
  · intro hd
    cases hd with
    | empty hr =>
        exact RecStartDerives.empty ((rec_start_empty_iff h K).mp hr)
    | root hr hf =>
        have hsample := (rec_start_rule_iff h K _).mp hr
        exact RecStartDerives.root hsample.1 hsample.2
          ((finite_rec_factor_iff h K _ _).mp hf)
  · intro hd
    cases hd with
    | empty hr =>
        exact FiniteRecStartDerives.empty
          ((rec_start_empty_iff h K).mpr hr)
    | root hr hne hf =>
        exact FiniteRecStartDerives.root
          ((rec_start_rule_iff h K _).mpr ⟨hr,hne⟩)
          ((finite_rec_factor_iff h K _ _).mpr hf)

/-- Full equivalence with the real finite production-set grammar's
generated language, not simply a semantic definition by closure. -/
theorem finite_rec_language_iff (h : Word Alphabet →* M)
    (K : Finset (Word Alphabet)) (w : Word Alphabet) :
    FiniteRecStartDerives h K w ↔ w ∈ RecLanguage h K :=
  finite_rec_start_iff h K w

#print axioms TCSPhase5.finite_rec_factor_iff
#print axioms TCSPhase5.finite_rec_start_iff
#print axioms TCSPhase5.finite_rec_language_iff
end TCSPhase5
