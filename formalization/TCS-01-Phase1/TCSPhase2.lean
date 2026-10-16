import TCSPhase1

/-!
Phase 2: literal bracketed CFG G_n and its semantic language.
Canonical paper: v211 (main HEAD 011a9f5ae4463241b7fe24a16f6d21169b14c4ba).
Phase 1 terms left/right stand for literal floor terminals;
squareLeft/squareRight stand for literal ceiling terminals.
-/

namespace TCSPhase2
open TCSPhase1

abbrev Word := List Terminal

/-- Free-word monoid: multiplication is literal list concatenation. -/
instance : Monoid Word where
  one := []
  mul := List.append
  one_mul := by intro w; rfl
  mul_one := by intro w; simp
  mul_assoc := by intro a b c; exact List.append_assoc a b c

def unaryWord (u : Word) : Word :=
  [Terminal.squareLeft] ++ u ++ [Terminal.squareRight]

def binaryWord (u v : Word) : Word :=
  [Terminal.left] ++ u ++ v ++ [Terminal.right]

/-- Independent inductive CFG derivation: E_0 → a, E_(i+1) →
ceiling E_i ceiling OR floor E_i E_i floor. -/
inductive Derives : Nat → Word → Prop
  | atom : Derives 0 [Terminal.a]
  | unary {n : Nat} {u : Word} :
      Derives n u → Derives (n + 1) (unaryWord u)
  | binary {n : Nat} {u v : Word} :
      Derives n u → Derives n v → Derives (n + 1) (binaryWord u v)

/-- Independent finite-set recursive semantics, to be proved equivalent to Derives. -/
def enumerate : Nat → Finset Word
  | 0 => {[Terminal.a]}
  | n + 1 =>
      (enumerate n).image unaryWord ∪
      ((enumerate n).product (enumerate n)).image
        (fun p => binaryWord p.1 p.2)

/-- The grammar language is DEFINED using inductive derivations, not enumeration. -/
def Language (n : Nat) : Set Word := {w | Derives n w}

/-- The start production S₀ → Eₙ. -/
inductive StartDerives (n : Nat) : Word → Prop
  | start {w : Word} : Derives n w → StartDerives n w

theorem start_iff (n : Nat) (w : Word) :
    StartDerives n w ↔ w ∈ Language n := by
  constructor
  · intro h
    cases h with
    | start h => exact h
  · exact StartDerives.start

theorem derives_iff_enumerate (n : Nat) (w : Word) :
    Derives n w ↔ w ∈ enumerate n := by
  induction n generalizing w with
  | zero =>
      constructor
      · intro h
        cases h with
        | atom => simp [enumerate]
      · intro h
        have hw : w = [Terminal.a] := by simpa [enumerate] using h
        subst w
        exact Derives.atom
  | succ n ih =>
      constructor
      · intro h
        cases h with
        | unary hu =>
            apply Finset.mem_union.mpr
            left
            exact Finset.mem_image.mpr ⟨_, (ih _).mp hu, rfl⟩
        | binary hu hv =>
            apply Finset.mem_union.mpr
            right
            exact Finset.mem_image.mpr
              ⟨(_, _), Finset.mem_product.mpr ⟨(ih _).mp hu, (ih _).mp hv⟩, rfl⟩
      · intro h
        rcases Finset.mem_union.mp h with hs | hb
        · obtain ⟨u, hu, he⟩ := Finset.mem_image.mp hs
          exact he ▸ Derives.unary ((ih _).mpr hu)
        · obtain ⟨⟨u, v⟩, hp, he⟩ := Finset.mem_image.mp hb
          have hp' := Finset.mem_product.mp hp
          exact he ▸ Derives.binary ((ih _).mpr hp'.1) ((ih _).mpr hp'.2)

theorem language_eq_enumerate (n : Nat) :
    Language n = (↑(enumerate n) : Set Word) := by
  ext w
  exact derives_iff_enumerate n w

theorem language_finite (n : Nat) : (Language n).Finite := by
  rw [language_eq_enumerate]
  exact Finset.finite_toSet _

theorem witness_derives (n : Nat) : Derives n (witness n) := by
  induction n with
  | zero => exact Derives.atom
  | succ n ih =>
      simpa [witness, binaryWord] using (Derives.binary ih ih)

theorem witness_mem_language (n : Nat) : witness n ∈ Language n :=
  witness_derives n

def NoSquareBrackets (w : Word) : Prop :=
  Terminal.squareLeft ∉ w ∧ Terminal.squareRight ∉ w

theorem noSquare_unary (u : Word) :
    ¬ NoSquareBrackets (unaryWord u) := by
  simp [NoSquareBrackets, unaryWord]

theorem noSquare_binary_iff (u v : Word) :
    NoSquareBrackets (binaryWord u v) ↔
      NoSquareBrackets u ∧ NoSquareBrackets v := by
  simp [NoSquareBrackets, binaryWord, List.mem_append,
    and_assoc, and_left_comm]

theorem witness_noSquare (n : Nat) :
    NoSquareBrackets (witness n) := by
  induction n with
  | zero => simp [witness, NoSquareBrackets]
  | succ n ih =>
      simpa [witness, binaryWord] using
        ((noSquare_binary_iff (witness n) (witness n)).mpr ⟨ih, ih⟩)

theorem derives_noSquare_unique {n : Nat} {w : Word}
    (hd : Derives n w) (hs : NoSquareBrackets w) :
    w = witness n := by
  induction hd with
  | atom => rfl
  | unary hu ih => exact False.elim (noSquare_unary _ hs)
  | binary hu hv ihU ihV =>
      obtain ⟨hsU, hsV⟩ := (noSquare_binary_iff _ _).mp hs
      simpa [witness, binaryWord] using
        congrArg₂ binaryWord (ihU hsU) (ihV hsV)

theorem noSquare_iff_witness (n : Nat) (w : Word)
    (hw : w ∈ Language n) :
    NoSquareBrackets w ↔ w = witness n := by
  constructor
  · exact derives_noSquare_unique hw
  · intro he
    rw [he]
    exact witness_noSquare n

/-- U₁ = {1, ζ}, where ζ is a two-sided absorbing zero. -/
inductive U1 where
  | one | zero
  deriving DecidableEq, Repr

instance : Monoid U1 where
  one := U1.one
  mul a b := match a, b with
    | U1.one, U1.one => U1.one
    | _, _ => U1.zero
  one_mul := by intro a; cases a <;> rfl
  mul_one := by intro a; cases a <;> rfl
  mul_assoc := by intro a b c; cases a <;> cases b <;> cases c <;> rfl

@[simp] theorem u1_one_mul (a : U1) : U1.one * a = a := by
  cases a <;> rfl

@[simp] theorem u1_zero_mul (a : U1) : U1.zero * a = U1.zero := by
  cases a <;> rfl

def symbolType : Terminal → U1
  | .squareLeft | .squareRight => .zero
  | _ => .one

def typeWord : Word → U1
  | [] => U1.one
  | x :: xs => symbolType x * typeWord xs

theorem typeWord_append (u v : Word) :
    typeWord (u ++ v) = typeWord u * typeWord v := by
  induction u with
  | nil => simp [typeWord]
  | cons letter us ih => simp [typeWord, ih, mul_assoc]

/-- The actual free-monoid homomorphism h_U. -/
def hU : Word →* U1 where
  toFun := typeWord
  map_one' := rfl
  map_mul' := typeWord_append

theorem hU_mul (u v : Word) : hU (u ++ v) = hU u * hU v := by
  exact map_mul hU u v

theorem typeWord_one_iff_noSquare (w : Word) :
    typeWord w = U1.one ↔ NoSquareBrackets w := by
  induction w with
  | nil => simp [typeWord, NoSquareBrackets]
  | cons c cs ih =>
      cases c <;> simp [typeWord, symbolType, NoSquareBrackets, ih]

theorem hU_one_iff_noSquare (w : Word) :
    hU w = U1.one ↔ NoSquareBrackets w :=
  typeWord_one_iff_noSquare w

theorem unique_type_one (n : Nat) (w : Word)
    (hw : w ∈ Language n) (ht : hU w = U1.one) :
    w = witness n :=
  (noSquare_iff_witness n w hw).mp ((hU_one_iff_noSquare w).mp ht)

theorem language_type_one_singleton (n : Nat) :
    {w | w ∈ Language n ∧ hU w = U1.one} =
      {witness n} := by
  ext w
  constructor
  · rintro ⟨hw, ht⟩
    exact Set.mem_singleton_iff.mpr (unique_type_one n w hw ht)
  · intro hw
    have he : w = witness n := Set.mem_singleton_iff.mp hw
    subst w
    exact ⟨witness_mem_language n,
      (hU_one_iff_noSquare _).mpr (witness_noSquare n)⟩

def LanguageMinus (n : Nat) : Set Word :=
  Language n \ {witness n}

theorem languageMinus_type_zero (n : Nat) :
    LanguageMinus n = {w | w ∈ Language n ∧ hU w = U1.zero} := by
  ext w
  constructor
  · rintro ⟨hw, hne⟩
    refine ⟨hw, ?_⟩
    cases ht : hU w with
    | one =>
        exact False.elim (hne (Set.mem_singleton_iff.mpr
          (unique_type_one n w hw ht)))
    | zero => exact ht
  · rintro ⟨hw, ht⟩
    refine ⟨hw, ?_⟩
    intro he
    have hw' : w = witness n := Set.mem_singleton_iff.mp he
    subst w
    have hone : hU (witness n) = U1.one :=
      (hU_one_iff_noSquare _).mpr (witness_noSquare n)
    rw [hone] at ht
    cases ht

/-- Explicit application of the previously verified abstract bound to L(G_n).
Only the characteristic-sample-existence premise for L_n^- remains. -/
theorem grammar_characteristic_exponential_lower_bound
    (Op : Finset Word → Set Word) (n : Nat)
    (hMinus : ∃ T : Finset Word,
      Characteristic Op (LanguageMinus n) T)
    (S : Finset Word) (hS : Characteristic Op (Language n) S) :
    3 * 2 ^ n - 1 ≤ encodedSize S := by
  exact characteristic_exponential_lower_bound Op (Language n) n
    (witness_mem_language n) hMinus S hS

#print axioms TCSPhase2.derives_iff_enumerate
#print axioms TCSPhase2.language_finite
#print axioms TCSPhase2.witness_mem_language
#print axioms TCSPhase2.noSquare_iff_witness
#print axioms TCSPhase2.hU_mul
#print axioms TCSPhase2.hU_one_iff_noSquare
#print axioms TCSPhase2.language_type_one_singleton
#print axioms TCSPhase2.languageMinus_type_zero
#print axioms TCSPhase2.grammar_characteristic_exponential_lower_bound

end TCSPhase2
