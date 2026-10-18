import TCSPhase8TrieSemantics

/-!
A concrete self-delimiting unary bit encoding for lists of bounded symbol
indices. This is a primitive for a future *fixed-alphabet* rule encoder,
not yet a complete rule serializer. Its length is exactly the sum of
index+1; with bounded indices it is linear in the number of tokens.
-/
namespace TCSPhase8

/-- Encode a natural number as that many true bits terminated by false. -/
def unaryBits (n : Nat) : List Bool :=
  List.replicate n true ++ [false]

/-- A concrete bitstream encoder for sequences of token indices. -/
def encodeIndices (ns : List Nat) : List Bool :=
  ns.flatMap unaryBits

/-- Decoder with a running count of true bits since the previous delimiter. -/
def decodeIndicesAux (count : Nat) : List Bool → Option (List Nat)
  | [] => if count = 0 then some [] else none
  | true :: rest => decodeIndicesAux (count + 1) rest
  | false :: rest =>
      (decodeIndicesAux 0 rest).map (fun xs => count :: xs)

theorem decodeIndicesAux_prefix
    (k : Nat) (rest : List Bool) :
    ∀ count : Nat,
      decodeIndicesAux count (unaryBits k ++ rest) =
      (decodeIndicesAux 0 rest).map (fun xs => (count + k) :: xs) := by
  induction k with
  | zero =>
    intro count
    rfl
  | succ k ih =>
    intro count
    change decodeIndicesAux (count + 1)
        (List.replicate k true ++ false :: rest) =
      (decodeIndicesAux 0 rest).map
        (fun xs => (count + (k+1)) :: xs)
    simpa [unaryBits, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm]
      using (ih (count+1))

theorem decodeIndices_encodeIndices (ns : List Nat) :
    decodeIndicesAux 0 (encodeIndices ns) = some ns := by
  induction ns with
  | nil => rfl
  | cons n rest ih =>
    change decodeIndicesAux 0
      (unaryBits n ++ encodeIndices rest) = some (n :: rest)
    rw [decodeIndicesAux_prefix]
    simpa [ih]

/-- The bit encoder is genuinely injective; repeated numeric values
and empty sequences are correctly distinguished. -/
theorem encodeIndices_injective : Function.Injective encodeIndices := by
  intro xs ys h
  have hc := congrArg (decodeIndicesAux 0) h
  rw [decodeIndices_encodeIndices, decodeIndices_encodeIndices] at hc
  exact Option.some.inj hc

theorem unaryBits_length (n : Nat) :
    (unaryBits n).length = n+1 := by
  simp [unaryBits]

theorem encodeIndices_length (ns : List Nat) :
    (encodeIndices ns).length = (ns.map (fun n => n+1)).sum := by
  induction ns with
  | nil => rfl
  | cons n rest ih =>
    simp [encodeIndices, unaryBits_length, ih]

/-- If all token indices are bounded by c-1, the bitstream has
at most c bits per token; no unbounded Gödel-number assumption. -/
theorem encodeIndices_length_le
    (ns : List Nat) (c : Nat)
    (hc : ∀ n ∈ ns, n+1 ≤ c) :
    (encodeIndices ns).length ≤ ns.length * c := by
  rw [encodeIndices_length]
  induction ns with
  | nil => simp
  | cons n rest ih =>
    have hn := hc n (by simp)
    have ht : ∀ x ∈ rest, x+1 ≤ c := by
      intro x hx
      exact hc x (by simp [hx])
    have hb := ih ht
    simp only [List.map_cons, List.sum_cons, List.length_cons, Nat.succ_mul]
    omega

#print axioms TCSPhase8.decodeIndices_encodeIndices
#print axioms TCSPhase8.encodeIndices_injective
#print axioms TCSPhase8.encodeIndices_length_le

end TCSPhase8
