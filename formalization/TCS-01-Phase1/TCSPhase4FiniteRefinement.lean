import TCSPhase4TrimmingLanguage
import TCSPhase4Thickness

namespace TCSPhase4
open TCSPhase1 TCSPhase2

/-- Finite enumeration of the five literal bracketed terminals. -/
instance : Fintype Terminal where
  elems := {Terminal.a, Terminal.left, Terminal.right,
    Terminal.squareLeft, Terminal.squareRight}
  complete := by
    intro x
    cases x <;> simp

/-- An explicit finite presentation of the semantically trimmed typed
refinement: distinct nonterminals are pairs (A,μ), terminal and binary
rules are finite filters of actual original rules and type equations,
and all retained symbols must occur in a successful typed start tree. -/
noncomputable def FiniteTrimmedRefinement {NT : Type}
    [Fintype NT] [DecidableEq NT] (G : SSBNFGrammar NT) :
    SSBNFGrammar (NT × U1) := by
  classical
  exact {
    startRules := Finset.univ.filter
      (fun p => p.1 ∈ G.startRules ∧ RetainedTypedSymbol G p.1 p.2)
    startEmpty := G.startEmpty
    terminalRules := Finset.univ.filter
      (fun p => (p.1.1, p.2) ∈ G.terminalRules ∧
        p.1.2 = hU [p.2] ∧ RetainedTypedSymbol G p.1.1 p.1.2)
    binaryRules := Finset.univ.filter
      (fun p => (p.1.1, p.2.1.1, p.2.2.1) ∈ G.binaryRules ∧
        p.1.2 = p.2.1.2 * p.2.2.2 ∧
        RetainedTypedSymbol G p.1.1 p.1.2 ∧
        RetainedTypedSymbol G p.2.1.1 p.2.1.2 ∧
        RetainedTypedSymbol G p.2.2.1 p.2.2.2)
  }

/-- Each terminal rule of the finite trimmed refinement corresponds
to a real original terminal rule, its exact hU annotation, and a
successfully retained parent. -/
theorem finite_trimmed_terminal_iff {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT)
    (A : NT) (μ : U1) (c : Terminal) :
    ((A, μ), c) ∈ (FiniteTrimmedRefinement G).terminalRules ↔
      (A, c) ∈ G.terminalRules ∧ μ = hU [c] ∧
      RetainedTypedSymbol G A μ := by
  classical
  simp [FiniteTrimmedRefinement]

theorem finite_trimmed_binary_iff {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT)
    (A B C : NT) (μ ν ρ : U1) :
    ((A, μ), (B, ν), (C, ρ)) ∈
      (FiniteTrimmedRefinement G).binaryRules ↔
      (A, B, C) ∈ G.binaryRules ∧ μ = ν * ρ ∧
      RetainedTypedSymbol G A μ ∧
      RetainedTypedSymbol G B ν ∧
      RetainedTypedSymbol G C ρ := by
  classical
  simp [FiniteTrimmedRefinement]

theorem trimmed_root_retained {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT}
    {A : NT} {μ : U1} {w : Word}
    (h : TrimmedTypedDerives G A μ w) :
    RetainedTypedSymbol G A μ := by
  cases h with
  | terminal hr hret => exact hret
  | binary hr hret hB hC => exact hret

/-- From the independent inductive retained typed derivation to an actual
derivation of the finite rule-set refinement. -/
theorem finite_trimmed_complete {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT}
    {A : NT} {μ : U1} {w : Word}
    (h : TrimmedTypedDerives G A μ w) :
    DerivesFrom (FiniteTrimmedRefinement G) (A, μ) w := by
  induction h with
  | terminal hr hret =>
      apply DerivesFrom.terminal
      exact (finite_trimmed_terminal_iff G _ _ _).mpr
        ⟨hr, rfl, hret⟩
  | binary hr hret hB hC ihB ihC =>
      have hretB := trimmed_root_retained hB
      have hretC := trimmed_root_retained hC
      apply DerivesFrom.binary
        ((finite_trimmed_binary_iff G _ _ _ _ _ _).mpr
          ⟨hr, rfl, hret, hretB, hretC⟩) ihB ihC

/-- Every derivation from the actual finite typed rule set is sound for
the independent semantic trimmed derivation relation. -/
theorem finite_trimmed_sound {NT : Type} [Fintype NT]
    [DecidableEq NT] {G : SSBNFGrammar NT}
    {X : NT × U1} {w : Word}
    (h : DerivesFrom (FiniteTrimmedRefinement G) X w) :
    TrimmedTypedDerives G X.1 X.2 w := by
  induction h with
  | @terminal Z c hr =>
      rcases Z with ⟨A, μ⟩
      obtain ⟨hr', ht, hret⟩ :=
        (finite_trimmed_terminal_iff G A μ c).mp hr
      subst μ
      exact TrimmedTypedDerives.terminal hr' hret
  | @binary Z Y W u v hr hB hC ihB ihC =>
      rcases Z with ⟨A, μ⟩
      rcases Y with ⟨B, ν⟩
      rcases W with ⟨C, ρ⟩
      obtain ⟨hr', ht, hret, _, _⟩ :=
        (finite_trimmed_binary_iff G A B C μ ν ρ).mp hr
      subst μ
      exact TrimmedTypedDerives.binary hr' hret ihB ihC


/-- Start-rule filtering has the same exact retained-symbol criterion
as the terminal and binary rule filters. -/
theorem finite_trimmed_start_iff {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) (A : NT) (μ : U1) :
    (A, μ) ∈ (FiniteTrimmedRefinement G).startRules ↔
      A ∈ G.startRules ∧ RetainedTypedSymbol G A μ := by
  classical
  simp [FiniteTrimmedRefinement]

/-- A typed symbol is productive in the actual finite pruned grammar iff
it appeared in a successful typed derivation tree from the original start. -/
theorem finite_trimmed_productive_iff_retained {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) (A : NT) (μ : U1) :
    (∃ w : Word, DerivesFrom (FiniteTrimmedRefinement G) (A, μ) w) ↔
      RetainedTypedSymbol G A μ := by
  constructor
  · rintro ⟨w, hd⟩
    exact trimmed_root_retained (finite_trimmed_sound hd)
  · intro hret
    obtain ⟨w, htyped⟩ := retained_productive hret
    exact ⟨w, finite_trimmed_complete (trimmed_complete htyped hret)⟩

/-- The finite trimmed CFG's actual derivations are exactly original
untyped derivations of the same type from a successfully retained node. -/
theorem finite_trimmed_lifting {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT)
    (A : NT) (μ : U1) (w : Word) :
    DerivesFrom (FiniteTrimmedRefinement G) (A, μ) w ↔
      (DerivesFrom G A w ∧ hU w = μ) ∧
      RetainedTypedSymbol G A μ := by
  constructor
  · intro hd
    have ht := finite_trimmed_sound hd
    exact ⟨(trimmed_lifting (trimmed_root_retained ht)).mp ht,
      trimmed_root_retained ht⟩
  · rintro ⟨hOrig, hret⟩
    exact finite_trimmed_complete ((trimmed_lifting hret).mpr hOrig)

/-- The finite typed production-set representation really preserves the
whole original generated language, including the optional empty start. -/
theorem finite_trimmed_grammar_language_eq {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) :
    GrammarLanguage (FiniteTrimmedRefinement G) = GrammarLanguage G := by
  rw [← trimmed_grammar_language_eq G]
  ext w
  constructor
  · intro hw
    change StartDerives (FiniteTrimmedRefinement G) w at hw
    cases hw with
    | empty he =>
        exact TrimmedStartDerives.empty
          (by simpa [FiniteTrimmedRefinement] using he)
    | root hs hd =>
        have hs' := (finite_trimmed_start_iff G _ _).mp hs
        exact TrimmedStartDerives.root hs'.1 (finite_trimmed_sound hd)
  · intro hw
    change TrimmedStartDerives G w at hw
    cases hw with
    | empty he =>
        exact StartDerives.empty
          (by simpa [FiniteTrimmedRefinement] using he)
    | root hs hd =>
        have hret := trimmed_root_retained hd
        exact StartDerives.root
          ((finite_trimmed_start_iff G _ _).mpr ⟨hs, hret⟩)
          (finite_trimmed_complete hd)

/-- Minimum lengths of the explicit finite CFG and the semantic
typed-thickness parameter coincide on every retained node. -/
theorem finite_trimmed_shortest_length {NT : Type} [Fintype NT]
    [DecidableEq NT] (G : SSBNFGrammar NT) (A : NT) (μ : U1)
    (hret : RetainedTypedSymbol G A μ) :
    ∃ w : Word,
      DerivesFrom (FiniteTrimmedRefinement G) (A, μ) w ∧
      w.length = shortestTypedLength G A μ ∧
      (∀ v : Word,
        DerivesFrom (FiniteTrimmedRefinement G) (A, μ) v →
          shortestTypedLength G A μ ≤ v.length) := by
  obtain ⟨w, hw, hlen⟩ := shortestTypedLength_spec hret
  exact ⟨w, finite_trimmed_complete hw, hlen,
    fun v hv => shortestTypedLength_le (finite_trimmed_sound hv)⟩

#print axioms TCSPhase4.finite_trimmed_terminal_iff
#print axioms TCSPhase4.finite_trimmed_binary_iff
#print axioms TCSPhase4.finite_trimmed_complete
#print axioms TCSPhase4.finite_trimmed_sound
#print axioms TCSPhase4.finite_trimmed_productive_iff_retained
#print axioms TCSPhase4.finite_trimmed_lifting
#print axioms TCSPhase4.finite_trimmed_grammar_language_eq
#print axioms TCSPhase4.finite_trimmed_shortest_length
end TCSPhase4
