# Phase 2 — Formal Verification Audit (2026-10-16)

## A. Reproducibility and provenance

- Canonical GitHub repository: `growupkuriyama-hub/Papers`.
- Phase 2 based on Phase 1 verified commit `5ece996e51591e3f2e62bb8d937ef95d8dea02e6`. The **original** `TCSPhase1.lean` was not changed.
- Source manuscript inspected at main HEAD `011a9f5ae4463241b7fe24a16f6d21169b14c4ba`, `main.tex` blob `db070f7c4b8b70fe1afb6bfe682f90f8c3f068b9`, `PAPER.yaml` v211. From v209 to v211 the letter shapes (binary floor vs former triangle, unary ceiling vs former square) and characteristic-sample variable naming were renamed, but the rules and claimed bounds remained. The Lean constructors inherited from Phase 1 retain their original names but are reinterpreted *as literal floor and ceiling terminals* according to v211.
- Source manuscript: `main.tex` lines 281–294 for samples/size, 1108–1227 for G_n and Proposition 6.3, 2197–2358 for Appendix C.
- Lean 4.24.0 commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`; Lake 5.0.0; Mathlib v4.24.0, resolved git SHA `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`; runner Ubuntu 24.04.
- Commands: `lake update`, `lake exe cache get`, `lean --version`, `lake --version`, `lake build`, `lake env lean TCSPhase1.lean`, `lake env lean TCSPhase2.lean`, `lake env lean TCSPhase2Bridge.lean`, forbidden-token grep, forbidden `sorryAx` grep.

## B. Machine-checked statements

The following all compiled at successful [Actions run #38901825970](https://github.com/growupkuriyama-hub/Papers/actions/runs/38901825970), job `116975678324`, proof commit `f0f1e75f725027aef04199108995783524148f1e`.

| Lean theorem | Exact proposition (mathematical rendering) | Status and source |
|---|---|---|
| `start_iff n w` | `StartDerives n w ↔ w ∈ Language n` | unconditional; G_n start rule |
| `derives_iff_enumerate n w` | `Derives n w ↔ w ∈ enumerate n` | unconditional; rules E_0 and E_(i+1) |
| `language_eq_enumerate n` | `Language n = ↑(enumerate n)` | unconditional; explicit CFG/enumeration equivalence |
| `language_finite n` | `(Language n).Finite` | unconditional |
| `witness_derives n` | `Derives n (witness n)` | unconditional; Phase 1 witness reused literally |
| `witness_mem_language n` | `witness n ∈ Language n` | unconditional |
| `noSquare_iff_witness n w hw` | if `w ∈ Language n`, `NoSquareBrackets w ↔ w = witness n` | unconditional; induction on derivation |
| `hU_mul u v` | `hU (u ++ v) = hU u * hU v` | unconditional; genuine monoid homomorphism (`hU : Word →* U1`) |
| `hU_one_iff_noSquare w` | `hU w = U1.one ↔ NoSquareBrackets w` | unconditional |
| `language_type_one_singleton n` | `{w | w ∈ Language n ∧ hU w = U1.one} = {witness n}` | unconditional; **main Phase 2 goal** |
| `languageMinus_type_zero n` | `LanguageMinus n = {w | w ∈ Language n ∧ hU w = U1.zero}` | unconditional |
| `grammar_characteristic_exponential_lower_bound Op n hMinus S hS` | `3*2^n−1 ≤ encodedSize S` | conditional on `∃T, Characteristic Op (LanguageMinus n) T` and `Characteristic Op (Language n) S`; **witness membership was proved**, no longer assumed |
| `filter_distributions_eq` | equality of distributions under equal-type factor substitution survives filtering by any `F : Set U1` | unconditional from the input distributions equality and equal types |
| `ce_filter_is_typed` | `ClarkEyraud L → TypedSubstitutable h (L ∩ {w | h w ∈ F})` | conditional, arbitrary type filter F |
| `languageMinus_typed_of_CE n hCE` | `ClarkEyraud (Language n) → TypedSubstitutable hU (LanguageMinus n)` | **conditional**: `ClarkEyraud (Language n)` not proved |

**Exact formalization scope:** `Derives` is the *specialized* inductive derivation relation of the displayed CFG, not a general CFG framework with arbitrary sentential-form rewriting. `StartDerives` implements S_0 → E_n, and `start_iff` confirms the matching language. The finite enumeration `enumerate` was defined independently, and equivalence proved via induction on n and rule derivations; it was not silently identified with the CFG language.

The concrete two-element type `U1` has constructors `one`, `zero` with an associative multiplication and identity; zero is absorbing by the multiplication pattern matching and a left-zero lemma. `Word` uses concatenation as multiplication and [] as identity. `hU` is an actual Lean monoid homomorphism, not merely a claimed numerical property.

**Critical hypotheses retained:** The conditional exponential lower bound needs characteristic samples for both *concrete* languages under the SAME set-driven operator. The source paper's existence claim for the actual fixed-typing learning operator and `L_n^- ∈ C_{h_U}^{cf}` are not discharged by these hypotheses. The conditional typed-substitutability bridge assumes CE(L_n) — exactly the unresolved Appendix C theorem. No `axiom` was introduced in place of that theorem.

## C. Compiler and axiom evidence

Final successful CI run: [#38901825970](https://github.com/growupkuriyama-hub/Papers/actions/runs/38901825970), job `116975678324`.

```text
Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)
Lake version 5.0.0-src+797c613 (Lean version 4.24.0)
Built TCSPhase1
Built TCSPhase2
Built TCSPhase2Bridge
Build completed successfully (7356 jobs).
Both phases and conditional bridge compiled without holes
```

Complete Phase 2 `#print axioms` results:

```text
'TCSPhase2.derives_iff_enumerate' depends on axioms: [propext, Classical.choice, Quot.sound]
'TCSPhase2.language_finite' depends on axioms: [propext, Classical.choice, Quot.sound]
'TCSPhase2.witness_mem_language' depends on axioms: [propext]
'TCSPhase2.noSquare_iff_witness' depends on axioms: [propext]
'TCSPhase2.hU_mul' depends on axioms: [propext]
'TCSPhase2.hU_one_iff_noSquare' depends on axioms: [propext]
'TCSPhase2.language_type_one_singleton' depends on axioms: [propext, Quot.sound]
'TCSPhase2.languageMinus_type_zero' depends on axioms: [propext, Quot.sound]
'TCSPhase2.grammar_characteristic_exponential_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'TCSPhase2.filter_distributions_eq' depends on axioms: [propext, Quot.sound]
'TCSPhase2.ce_filter_is_typed' depends on axioms: [propext, Quot.sound]
'TCSPhase2.languageMinus_typed_of_CE' depends on axioms: [propext, Quot.sound]
```

Phase 1 `#print axioms` was also re-executed in the same CI job and matches Phase 1's earlier successful results. Only standard Lean logical axioms were reported: `propext`, `Classical.choice`, and `Quot.sound`. There were NO `sorryAx` dependencies. File scan checked three Lean files for `sorry`, `admit`, `axiom` and `opaque` tokens and found none.

Development runs: `38900312739` exposed missing word-monoid structure; `38900634731` reached all core theorems with two final proof-elaboration issues; `38900970050` successfully compiled Milestones A–C and the concrete conditional lower bound. `38901517284` identified an explicit list-concatenation/monoid-product elaboration issue in the newly added optional bridge. `38901825970` compiled all three Lean modules and passed the axiom and forbidden-syntax audit. None of these intermediate compile errors revealed a mathematical counterexample.

## D. Unverified claims

- **Unproved:** Clark–Eyraud substitutability of `Language n`. This is Appendix C and the central challenge of Phase 3.
- **Unproved:** unconditional typed substitutability and formal fixed-typing CFG-class membership for `LanguageMinus n`.
- **Unproved:** characteristic sample existence for the actual `Rec_h`, full proof of Theorem 4.2 soundness, grammar-size and ordinary-thickness bounds, and Corollary 6.4's universal SSBNF representation claim.
- **Not claimed:** bounds on convergence stages/runtimes for arbitrary Gold learners.
- The abstraction `Op : Finset Word → Set Word` continues to denote the generated language of a set-driven grammar-valued reconstruction operator; no monotonicity or additional global learner correctness is imposed.

## E. Phase 3 recommended order (Appendix C v211 lines 2197–2358)

1. Define parser states as stacks of indexed E_i and literal floor/ceiling closing terminals. Formalize one-step labelled transitions and their reflexive-transitive word action; prove deterministic transitions.
2. Prove one-letter reverse injectivity for fixed inputs and derive injectivity of fixed-word partial actions. Define weight via `4^i` and show strict decrease on nonempty transitions.
3. Prove untouched-suffix lemma and first-visit stack factorization; isolate last-closing-marker invariance.
4. Establish Appendix C recognition lemma `E_i ψ --w→ ψ ↔ w∈L_i` including arbitrary starting-stack recognition.
5. Prove complete-subtree exchange (`w,w'∈L_i → D_{L_n}(w)=D_{L_n}(w')`).
6. Prove branch synchronization for the different opening terminals using weight and last-marker cases.
7. Prove equal-endpoint path-congruence by induction on total input length and combine common-context determinism with right-injectivity to derive unconditional `ClarkEyraud (Language n)`.
8. Reuse the now-verified `languageMinus_typed_of_CE` as a theorem, not an assumption; only then consider separately formalizing class membership and the reconstruction operator's actual sample existence/soundness.

## F. Verdict

**A — all requested Milestone A–C general theorems completely verified.** Milestone D bridge likewise verified, but *conditional on CE(L_n)*. This does not certify Appendix C or Proposition 6.3's remaining unformalized language-class and learner-specific premises. No protected manuscript/PDF/reviewer-response files were changed.
