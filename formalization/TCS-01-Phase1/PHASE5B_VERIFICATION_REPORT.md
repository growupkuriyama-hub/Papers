# Phase 5B Verification Report — General typed positive witness construction

## 1. Canonical inputs and untouched baseline

- Manuscript: `01_fixed-h-cfg/main.tex`, main HEAD `b7abdcf95d537a4f7ef364e387ec01ebd87d3e32`, `PAPER.yaml` **v225**, manuscript Git blob `7a3ed5ca1aaaf376a1e5104d12e08f59f424ab0d`.
- Paper: Takayuki Kuriyama, *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*, `TCS-D-26-00494`. LaTeX definitions inspected by labels `prop:typed-core`, `eq:W`, `thm:complete`, `thm:reconstruction-fixed-h`, `lem:sample-consistency`, `thm:soundness`.
- New branch `formalization/tcs-phase5b-canonical-witnesses-20261017`, based exactly on successful Phase 5A HEAD `013400b7e53f55209c1c7555ecbdd0c5e3c66ada`.
- Lean **4.24.0**, Mathlib **v4.24.0**, Lake **5.0.0** as inherited from unchanged pinned lakefile requirement.
- Early verified baseline: [Actions #39030778953](https://github.com/growupkuriyama-hub/Papers/actions/runs/39030778953) compiled the new `TCSPhase5BGeneralSSBNF`, `TCSPhase5BTypedRefinement`, `TCSPhase5BRetained` modules. The earlier CI includes all 38 Phase 1–5A sources. At that point the choice/witness/completeness modules were not yet built; **do not treat that early successful run as evidence for later milestones**.

## 2. General SSBNF / genuine typed refinement

`SSBNFGrammar Alphabet NT` uses real finite `Finset` fields for start, terminal, binary productions and a Boolean epsilon start rule; the distinguished start is **not** in `NT`. `DerivesFrom` and `StartDerives` are independently inductive.

For any actual `h : List Alphabet →* M` and arbitrary finite non-start symbols:
```lean
theorem typed_lifting
    {G : SSBNFGrammar Alphabet NT} {h : List Alphabet →* M}
    {A : NT} {μ : M} {w : List Alphabet} :
    TypedDerives G h A μ w ↔
      DerivesFrom G A w ∧ h w = μ
```
The entire definition is independent of the earlier Phase 4 five-letter special case; type preservation is proven by induction and the real `MonoidHom.map_mul`, not stipulated.

`TypedContext` is an independent typed tree-occurrence relation with root/left/right constructors. Each descent requires a real original binary production plus **both productive typed children**, so no false unproductive sibling assumptions are hidden. The following are proved separately:
```lean
context_productive:
  TypedContext G h A μ u v → ∃w, TypedDerives G h A μ w

retained_productive:
  RetainedTypedSymbol G h A μ → ∃w, TypedDerives G h A μ w

context_plug:
  TypedContext G h A μ u v →
  TypedDerives G h A μ w →
  u ++ w ++ v ∈ GrammarLanguage G

trimmed_lifting:
  RetainedTypedSymbol G h A μ →
  (TrimmedTypedDerives G h A μ w ↔
     DerivesFrom G A w ∧ h w = μ)
```

The additional `finiteTypedRefinement G h` is a **literal finite grammar** on pairs `(A,μ)`: `symbols`, `startRules`, `terminalRules`, and `binaryRules` are `Finset.univ.filter` based on actual original productions, h-type equations and successful-context retention. `finite_{symbols,start,terminal,binary}_iff` characterizes every finite filtered production. `FiniteTypedDerives`, `finite_typed_iff`, and `finite_typed_start_iff` explicitly establish the agreement of these finite rules with independently generated trimmed derivations and original start language.

## 3. Chosen yields / contexts; exact canonicality scope

`chosenYield G h A μ` is selected from `shortestYieldOfRet`, itself chosen from a `Nat.find` least-yield-length proof; `chosenYield_spec` proves actual typed derivability, `chosenYield_nonempty` proves nonempty, and `chosenYield_type` proves `h(chosenYield)=μ`.

`chosenContext G h A μ` is selected from a `Nat.find` minimum-sum-length actual successful `TypedContext`, so `chosenContext_spec` gives a real terminal reaching context and `chosenContext_start_empty` derives `([],[])` for each productive start child from the **zero minimum**, not from an extra theorem hypothesis.

**The manuscript makes a further shortlex tie-break within equal-length yields and contexts. This tie-break has not been formalized.** Hence the chosen witness `Finset` below may differ from the *literal* `eq:W` canonical set, even though it is constructed by the same four families, has shortest-length representatives, and (if the full CI succeeds) is characteristic. The correct final judgment in that case is **B**, not A.

## 4. Four explicit finite witness families and their meanings

`PositiveWitnesses G h` is a finite `Finset` union of:

1. `WitnessSymbols G h`: `u_X ++ chosenYield(X) ++ v_X` for every retained typed pair `X`.
2. `WitnessLexical G h`: `u_X ++ [a] ++ v_X` for each retained real typed rule `X→a`.
3. `WitnessBinary G h`: `u_X ++ chosenYield(Y) ++ chosenYield(Z) ++ v_X` for each retained real typed rule `X→YZ`.
4. `WitnessEmpty G`: `{[]}` if and only if the original start generates epsilon; otherwise empty.

All sets are literal finite images of actual finite production sets. Repetitions are automatically deduplicated. The `positive_witnesses_subset_language` proof checks each family by `context_plug` and real typed derivations. This is the user-specified `eq:W` **shape** with a documented, non-shortlex choice convention.

## 5. True Rec_h simulation and three theorem goals

All downstream targets operate on the **unchanged actual Phase 5A `TCSPhase5.RecFactorDerives`, `RecStartDerives`, and `RecLanguage`** with precisely the sample-generated (B)(U)(L)(S) productions, already proved equivalent to finite actual Rec grammar productions by Phase 5A `finite_rec_language_iff`.

```lean
witness_unary:
  RetainedTypedSymbol G h A μ →
  y ≠ [] → h y = μ →
  PositiveWitnesses G h ⊆ K →
  wrapYield G h A μ y ∈ PositiveWitnesses G h →
  DirectSimilar h K (chosenYield G h A μ) y ∧
  ObservedFactor K (chosenYield G h A μ) ∧
  ObservedFactor K y

simulate_terminal:
  (A,a) ∈ G.terminalRules →
  RetainedTypedSymbol G h A (h [a]) →
  PositiveWitnesses G h ⊆ K →
  RecFactorDerives h K (chosenYield G h A (h [a])) [a]

simulate_binary:
  (A,B,C) ∈ G.binaryRules →
  RetainedTypedSymbol G h A (μ*ν) →
  RetainedTypedSymbol G h B μ →
  RetainedTypedSymbol G h C ν →
  PositiveWitnesses G h ⊆ K →
  RecFactorDerives h K (chosenYield G h B μ) wB →
  RecFactorDerives h K (chosenYield G h C ν) wC →
  RecFactorDerives h K (chosenYield G h A (μ*ν)) (wB++wC)

canonical_symbol_reconstructs:
  PositiveWitnesses G h ⊆ K →
  TrimmedTypedDerives G h A μ w →
  RecFactorDerives h K (chosenYield G h A μ) w
```

The critical (U) rule is not an assumed equivalence class: it is **constructed from two actual sampled words sharing the same original terminal reaching context**, with equal h-types established from the independent typed derivations. Both x and y are nonempty observed factors. Binary simulation uses a witnessed observed concatenation and recursively derived children.

**Central completeness statement:**
```lean
theorem rec_complete_from_positive_witnesses
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (K : Finset (List Alphabet))
    (hW : PositiveWitnesses G h ⊆ K) :
    GrammarLanguage G ⊆ RecLanguage h K
```
**There is NO premise `K ⊆ GrammarLanguage G` and NO target-substitutability premise.** Start children have a forced empty chosen context, so their chosen yield is itself in K and an actual (S) rule can start the subtree simulation; epsilon is witnessed separately.

**Exact reconstruction and characteristic samples:**
```lean
theorem rec_exact_reconstruction
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (K : Finset (List Alphabet))
    (hSub : TypedSubstitutable h (GrammarLanguage G))
    (hW : PositiveWitnesses G h ⊆ K)
    (hKL : (↑K : Set (List Alphabet)) ⊆ GrammarLanguage G) :
    RecLanguage h K = GrammarLanguage G

theorem canonical_witnesses_characteristic
    (G : SSBNFGrammar Alphabet NT) (h : List Alphabet →* M)
    (hSub : TypedSubstitutable h (GrammarLanguage G)) :
    TCSPhase1.Characteristic (RecLanguage h)
      (GrammarLanguage G) (PositiveWitnesses G h)
```
The latter is the **actual unchanged Phase 1** set-driven characteristic predicate, not a new weakened definition. It requires substitutability only to use the already-verified Phase 5A soundness.

## 6. CI, axioms, honest success boundary

CI workflow `.github/workflows/tcs-phase5b-lean.yml` pins Lean 4.24.0 and Mathlib v4.24.0, runs `lake build`, compiles every old and new source separately with `lake env lean`, performs `#print axioms`, and scans sources and theorem logs for forbidden proof tokens and `sorryAx`.

**Status at initial report save:** The generic SSBNF, typed lifting, and retained contexts have successful CI evidence in Actions #39030778953. Later choice/witness/completeness modules require additional CI; early failing elaborations are not a mathematical counterexample, and no unverified theorem is to be counted as complete.

**Final successful full-HEAD workflow run and job ID:** To be recorded only after a successful run at the exact final branch HEAD; any incomplete CI does not justify verdict A/B.

No local source changes to Phase 1–5A theorem statements or proofs, `01_fixed-h-cfg/main.tex`, `PAPER.yaml`, responses or PDFs are intended.

## 7. Explicitly unverified research goals

Even if the full **minimum-choice** positive-witness reconstruction is kernel-verified, this is not yet an exact formalization of the manuscript's **shortlex** canonical tie-breaking. Also out of scope: the polynomial characteristic-data upper bound, Gold learner's conservative convergence, polynomial-time construction of Rec_h, general CFG-to-SSBNF normalization, and all remaining TCS statements.

**Conditional classification:** B if full theorem set and CI succeeds with minimum-choice witnesses but shortlex unresolved; C/D if only lower milestones compile; F if compilation/CI cannot be completed. No stronger classification is asserted ahead of actual workflow completion.
