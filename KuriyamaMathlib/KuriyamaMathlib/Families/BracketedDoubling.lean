import KuriyamaMathlib.Distribution.DeletionCapture

/-! The five-letter, two-bracket-kind family shared by the current 01
(Prop. 6.4) and 09 (sec:deletion). This is NOT the historical six-letter
LevelTree family of the v83 formalization. The exact CFG and node-occurrence
bridges are subsequent proof obligations. -/
namespace KuriyamaMathlib.BracketedDoubling

inductive Letter where
  | leaf | binaryOpen | binaryClose | unaryOpen | unaryClose
  deriving DecidableEq, Fintype, Repr

open Letter

inductive Tree : Nat → Type where
  | leaf : Tree 0
  | unary {n : Nat} : Tree n → Tree (n + 1)
  | binary {n : Nat} : Tree n → Tree n → Tree (n + 1)

def Tree.serialize : {n : Nat} → Tree n → Word Letter
  | _, .leaf => [leaf]
  | _, .unary t => [unaryOpen] ++ t.serialize ++ [unaryClose]
  | _, .binary l r => [binaryOpen] ++ l.serialize ++ r.serialize ++ [binaryClose]

def cleanTree : (n : Nat) → Tree n
  | 0 => .leaf
  | n + 1 => .binary (cleanTree n) (cleanTree n)

def unaryTree : (n : Nat) → Tree n
  | 0 => .leaf
  | n + 1 => .unary (unaryTree n)

def cleanWord (n : Nat) : Word Letter := (cleanTree n).serialize

def unaryWord (n : Nat) : Word Letter := (unaryTree n).serialize

def fullLanguage (n : Nat) : Set (Word Letter) :=
  {w | ∃ t : Tree n, t.serialize = w}

def deletedLanguage (n : Nat) : Set (Word Letter) :=
  fullLanguage n \ {cleanWord n}

theorem cleanWord_mem (n : Nat) : cleanWord n ∈ fullLanguage n :=
  ⟨cleanTree n, rfl⟩

theorem unaryWord_mem (n : Nat) : unaryWord n ∈ fullLanguage n :=
  ⟨unaryTree n, rfl⟩

theorem cleanWord_succ (n : Nat) :
    cleanWord (n + 1) = [binaryOpen] ++ cleanWord n ++ cleanWord n ++ [binaryClose] := rfl

theorem unaryWord_succ (n : Nat) :
    unaryWord (n + 1) = [unaryOpen] ++ unaryWord n ++ [unaryClose] := rfl

theorem cleanWord_length_add_two (n : Nat) :
    (cleanWord n).length + 2 = 3 * 2 ^ n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [cleanWord_succ]
    simp only [List.length_append, List.length_singleton, pow_succ]
    omega

theorem cleanWord_length (n : Nat) :
    (cleanWord n).length = 3 * 2 ^ n - 2 := by
  have h := cleanWord_length_add_two n
  omega

theorem unaryWord_length (n : Nat) : (unaryWord n).length = 2 * n + 1 := by
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [unaryWord_succ]
    simp only [List.length_append, List.length_singleton, ih]
    omega

theorem cleanWord_no_mark (n : Nat) : unaryOpen ∉ cleanWord n := by
  induction n with
  | zero => simp [cleanWord, cleanTree, Tree.serialize]
  | succ n ih => simp [cleanWord_succ, ih]

theorem Tree.eq_clean_of_no_mark {n : Nat} (t : Tree n)
    (h : unaryOpen ∉ t.serialize) : t.serialize = cleanWord n := by
  induction t with
  | leaf => rfl
  | unary t ih =>
    exfalso
    exact h (by simp [Tree.serialize])
  | @binary n l r ihl ihr =>
    have hl : unaryOpen ∉ l.serialize := by
      intro hm
      exact h (by simp [Tree.serialize, hm])
    have hr : unaryOpen ∉ r.serialize := by
      intro hm
      exact h (by simp [Tree.serialize, hm])
    simp only [Tree.serialize, cleanWord_succ, ihl hl, ihr hr]

theorem deleted_iff_marked {n : Nat} {w : Word Letter}
    (hw : w ∈ fullLanguage n) : w ∈ deletedLanguage n ↔ unaryOpen ∈ w := by
  constructor
  · intro hd
    by_contra hn
    rcases hw with ⟨t, ht⟩
    have he : t.serialize = cleanWord n := t.eq_clean_of_no_mark (by simpa [ht] using hn)
    exact hd.2 (ht.symm.trans he)
  · intro hm
    refine ⟨hw, ?_⟩
    intro he
    have he' : w = cleanWord n := he
    exact cleanWord_no_mark n (by simpa [he'] using hm)

end KuriyamaMathlib.BracketedDoubling
