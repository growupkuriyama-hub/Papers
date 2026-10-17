import TCSPhase4Thickness

namespace TCSPhase4
open TCSPhase1 TCSPhase2

theorem witness_nonempty (n : Nat) : witness n ≠ [] := by
  cases n <;> simp [witness]

/-- Presentation-independent exponential bound. The grammar ranges over
all finite, separated-start SSBNF productions, without a reducedness
assumption or any bound on the size of its rule and nonterminal sets. -/
theorem intrinsic_typed_thickness_lower_bound_all (n : Nat)
    {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT)
    (hLang : GrammarLanguage G = TCSPhase2.Language n) :
    3 * 2 ^ n - 2 ≤ typedThickness G := by
  have hwG : witness n ∈ GrammarLanguage G := by
    rw [hLang]
    exact witness_mem_language n
  obtain ⟨A, hs, hd⟩ :=
    nonempty_start_has_root hwG (witness_nonempty n)
  have hone : hU (witness n) = U1.one :=
    (hU_one_iff_noSquare _).mpr (witness_noSquare n)
  have htyped : TypedDerives G A U1.one (witness n) := by
    simpa only [hone] using (typed_complete hd)
  have hret : RetainedTypedSymbol G A U1.one :=
    retained_at_start hs htyped
  have huniq : ∀ v : Word, TrimmedTypedDerives G A U1.one v →
      v = witness n := by
    intro v hv
    obtain ⟨hvG, hvtype⟩ := (trimmed_lifting hret).mp hv
    have hvLang : v ∈ TCSPhase2.Language n := by
      rw [← hLang]
      exact start_rule_generates hs hvG
    exact unique_type_one n v hvLang hvtype
  obtain ⟨v, hvTrim, hvMin⟩ := shortestTypedLength_spec hret
  have hvEq : v = witness n := huniq v hvTrim
  have hMin : shortestTypedLength G A U1.one =
      (witness n).length := by
    rw [hvEq] at hvMin
    exact hvMin.symm
  calc
    3 * 2 ^ n - 2 = (witness n).length := (witness_length n).symm
    _ = shortestTypedLength G A U1.one := hMin.symm
    _ ≤ typedThickness G := shortest_le_typedThickness G A U1.one hret

/-- Corollary 6.4's n≥1 version (even reducedness is unnecessary). -/
theorem intrinsic_typed_thickness_lower_bound (n : Nat) (hn : 1 ≤ n)
    {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT)
    (hLang : GrammarLanguage G = TCSPhase2.Language n) :
    3 * 2 ^ n - 2 ≤ typedThickness G := by
  exact intrinsic_typed_thickness_lower_bound_all n G hLang

#print axioms TCSPhase4.witness_nonempty
#print axioms TCSPhase4.intrinsic_typed_thickness_lower_bound_all
#print axioms TCSPhase4.intrinsic_typed_thickness_lower_bound
end TCSPhase4
