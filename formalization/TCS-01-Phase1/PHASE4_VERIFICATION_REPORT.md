# Independent verification report: Corollary 6.4 (Phase 4)

## 1. Source identity, baseline and CI checkpoints

- Repository: `growupkuriyama-hub/Papers`.
- Phase 4 branch: `formalization/tcs-phase4-intrinsic-thickness-20261017`; immutable initial Phase 4 HEAD audited: `494441ade3511f8dc0a93f3b003977a1ec3392a2`; Phase 3C base `673939835e5fade5812b5808f5fb41fb57662c6c`.
- Authoritative main as of 2026-10-17: `7eecac48a1fc2391a0300ffcd7746609eaa62997`. `PAPER.yaml`: **v222**. `01_fixed-h-cfg/main.tex` Git blob: `3963c9f93c08d00cb47e0421ad5e16932d651051`. The entire `\begin{corollary}[presentation-independent typed-thickness gap]` through its following `\end{proof}` is **exactly byte-identical** to the text at v218/main `8d4fcb749c58ffa513725eb459dcadc3964247ac`; no proof-target drift.
- Lean **4.24.0**, release commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`; Lake **5.0.0**, Mathlib release tag **v4.24.0**; CI resolves Mathlib with `lake update`.
- Successful precedent for the underlying complete language-theoretic proof: [run #39019851949](https://github.com/growupkuriyama-hub/Papers/actions/runs/39019851949), job `117359327257`, 7404 jobs, including finite production sets and minimum lengths.
- The first fully extended operational-trimming code build [run #39020321571](https://github.com/growupkuriyama-hub/Papers/actions/runs/39020321571), job `117360664052`, completed **`lake build` successfully in 7406 jobs** and directly compiled **28 source modules**, including `TCSPhase4OperationalTrim.lean`. All printed theorem axioms were standard. The *subsequent* forbidden-token scan failed solely because a prose comment on line 8 of `TCSPhase4OperationalTrim.lean` contained the English word `admit`. This run is explicitly **NOT reported as a passing CI run**.
- **First fully passing CI after the false-positive fix:** [run #39023165114](https://github.com/growupkuriyama-hub/Papers/actions/runs/39023165114), job **`117368862951`**, code commit **`28a1353ed54c6e397bd81abc3223cf93c0c426ff`**. The log confirms `Build completed successfully (7406 jobs).` followed by `Phase 1-4 modules compiled and audited`; source forbidden-token scan and axiom scan both passed. This run includes all nine Phase 4 source files and 19 regression files. It predates the additional explicit `TCSPhase4Main.lean` audit imports, which must be checked by the later final-HEAD run.
- Comment-only fix commit: `28a1353ed54c6e397bd81abc3223cf93c0c426ff`, replacing `both child typed symbols admit completed terminal derivations` with `both child typed symbols have completed terminal derivations`. Neither code/proofs/statements nor the forbidden-token check were weakened.
- **Fully integrated main-module CI passed**: [run #39023247505](https://github.com/growupkuriyama-hub/Papers/actions/runs/39023247505), job **`117369099968`**, exact code commit **`408ca64b604afa872bfcc95ddfa0e026f6024c68`**. All **7406** Lake jobs passed, all 28 Lean sources were directly compiled, the forbidden-proof-token scan passed, and no `sorryAx` was present. In particular `TCSPhase4Main.lean` printed standard logical axioms for the added finite refinement and operational trimming theorems, together with the original lower bound: `[propext, Classical.choice, Quot.sound]` in general; `operational_retained_iff` and `typed_lifting` need only `[propext, Quot.sound]`.
- Final integration-code audit commit: `408ca64b604afa872bfcc95ddfa0e026f6024c68`; adds the explicit imports and 13 additional `#print axioms` declarations in `TCSPhase4Main.lean`. The proof code in the other modules is unchanged from the prior kernel-verified code. The branch HEAD after README/report commits is to be read from the branch ref; these documentation commits contain no changes to Lean theorem statements or proofs. The successful workflow run for the final documentation HEAD must be checked separately.

## 2. Exact mathematical models: universal quantification and independent derivations

The `TCSPhase4SSBNF.lean` grammar is a *structural finite grammar presentation*, not a `Set Word`:
```lean
structure SSBNFGrammar (NT : Type) [Fintype NT] [DecidableEq NT] where
  startRules    : Finset NT
  startEmpty    : Bool
  terminalRules : Finset (NT × Terminal)
  binaryRules   : Finset (NT × NT × NT)
```
There is a distinguished start symbol outside `NT`, with start-only `S0 → A | ε`; non-start rules have only `A → c | BC`. The start does not occur on a non-start production RHS by construction. Finiteness of symbols/rules is explicit, but **no bound** on `Fintype.card NT` or rule-set size is assumed.

```lean
inductive DerivesFrom (G : SSBNFGrammar NT) : NT → Word → Prop
  | terminal (hr : (A,c) ∈ G.terminalRules) : DerivesFrom G A [c]
  | binary (hr : (A,B,C) ∈ G.binaryRules)
      (hB : DerivesFrom G B u) (hC : DerivesFrom G C v) :
      DerivesFrom G A (u ++ v)
```
(*Constructor schema shown with implicit indices abbreviated only in this documentation; actual source contains full Lean syntax.*)

**Validated statement:**
```lean
theorem nonempty_start_has_root {G : SSBNFGrammar NT} {w : Word}
    (hw : w ∈ GrammarLanguage G) (hne : w ≠ []) :
    ∃ A : NT, A ∈ G.startRules ∧ DerivesFrom G A w
```
`start_rule_generates` proves the reverse membership for any root start production. The class of grammars is broader than reduced SSBNF: there is no reducedness requirement. Since the proof applies to all grammars of this syntax, restricting to reduced ones is mathematically valid.

**Independent typed rules:**
```lean
inductive TypedDerives (G : SSBNFGrammar NT) : NT → U1 → Word → Prop
  | terminal (hr : (A,c) ∈ G.terminalRules) :
      TypedDerives G A (hU [c]) [c]
  | binary (hr : (A,B,C) ∈ G.binaryRules)
      (hB : TypedDerives G B μ u) (hC : TypedDerives G C ν v) :
      TypedDerives G A (μ * ν) (u ++ v)
```
```lean
theorem typed_lifting {G : SSBNFGrammar NT} {A : NT} {μ : U1} {w : Word} :
    TypedDerives G A μ w ↔ DerivesFrom G A w ∧ hU w = μ
```
The two directions `typed_sound` and `typed_complete` prove the invariant by induction. Typed lifting is **not definitionally assumed**, and the actual `TCSPhase2.U1` and `TCSPhase2.hU` are reused unchanged.

## 3. Semantic retention, trimming, and original-language preservation

`TypedOccurrence G S τ X ρ` is a genuine independent inductive path relation, each left/right descent requiring a correctly typed binary production **and a successful derivation of the other child**. `RetainedTypedSymbol G X ρ` is existential over a start child `S` with `S ∈ G.startRules` and such an occurrence path. Thus it means *appearing in a successful start derivation*, not merely `∃w, TypedDerives G X ρ w`.

The following are compiled:
```lean
theorem retained_productive
    (h : RetainedTypedSymbol G A μ) :
    ∃ w, TypedDerives G A μ w

theorem trimmed_lifting
    (hret : RetainedTypedSymbol G A μ) :
    TrimmedTypedDerives G A μ w ↔
      DerivesFrom G A w ∧ hU w = μ

theorem trimmed_grammar_language_eq (G : SSBNFGrammar NT) :
    TrimmedGrammarLanguage G = GrammarLanguage G
```
`TrimmedTypedDerives` and `TrimmedStartDerives` are independent inductive productions, and `trimmed_complete` uses `retained_binary_children`, itself based on actual successful-tree occurrence and subtree grafting.

## 4. Finite typed rule-set refinement: statements and proof audit

`FiniteTrimmedRefinement G : SSBNFGrammar (NT × U1)` has **explicit finite `Finset.univ.filter` terminal/binary/start production sets** and exactly the original `startEmpty` bit. `Fintype Terminal` enumerates the five *distinct* bracketed letters and `Fintype U1` enumerates `one,zero`. It never substitutes `G = Set Word`.

Let `Gtilde := FiniteTrimmedRefinement G`. The *actual Lean theorem statements* are:

```lean
theorem finite_trimmed_start_iff (G : SSBNFGrammar NT)
    (A : NT) (μ : U1) :
    (A, μ) ∈ (FiniteTrimmedRefinement G).startRules ↔
      A ∈ G.startRules ∧ RetainedTypedSymbol G A μ

theorem finite_trimmed_terminal_iff (G : SSBNFGrammar NT)
    (A : NT) (μ : U1) (c : Terminal) :
    ((A, μ), c) ∈ (FiniteTrimmedRefinement G).terminalRules ↔
      (A, c) ∈ G.terminalRules ∧ μ = hU [c] ∧
        RetainedTypedSymbol G A μ

theorem finite_trimmed_binary_iff (G : SSBNFGrammar NT)
    (A B C : NT) (μ ν ρ : U1) :
    ((A, μ), (B, ν), (C, ρ)) ∈
      (FiniteTrimmedRefinement G).binaryRules ↔
      (A, B, C) ∈ G.binaryRules ∧ μ = ν * ρ ∧
      RetainedTypedSymbol G A μ ∧
      RetainedTypedSymbol G B ν ∧ RetainedTypedSymbol G C ρ

theorem finite_trimmed_complete
    (h : TrimmedTypedDerives G A μ w) :
    DerivesFrom (FiniteTrimmedRefinement G) (A, μ) w

theorem finite_trimmed_sound
    (h : DerivesFrom (FiniteTrimmedRefinement G) X w) :
    TrimmedTypedDerives G X.1 X.2 w

theorem finite_trimmed_productive_iff_retained
    (G : SSBNFGrammar NT) (A : NT) (μ : U1) :
    (∃ w : Word,
      DerivesFrom (FiniteTrimmedRefinement G) (A, μ) w) ↔
        RetainedTypedSymbol G A μ

theorem finite_trimmed_lifting
    (G : SSBNFGrammar NT) (A : NT) (μ : U1) (w : Word) :
    DerivesFrom (FiniteTrimmedRefinement G) (A, μ) w ↔
      (DerivesFrom G A w ∧ hU w = μ) ∧
        RetainedTypedSymbol G A μ

theorem finite_trimmed_grammar_language_eq
    (G : SSBNFGrammar NT) :
    GrammarLanguage (FiniteTrimmedRefinement G) = GrammarLanguage G

theorem finite_trimmed_shortest_length
    (G : SSBNFGrammar NT) (A : NT) (μ : U1)
    (hret : RetainedTypedSymbol G A μ) :
    ∃ w : Word,
      DerivesFrom (FiniteTrimmedRefinement G) (A, μ) w ∧
      w.length = shortestTypedLength G A μ ∧
      (∀ v : Word,
        DerivesFrom (FiniteTrimmedRefinement G) (A, μ) v →
          shortestTypedLength G A μ ≤ v.length)
```

In the two rule-membership lemmas, proof is `simp [FiniteTrimmedRefinement]`: this expands **real finite production filters**, not a tautological language predicate. `finite_trimmed_complete` reconstructs ordinary derivations using the finite rule-set membership and retained children; `finite_trimmed_sound` erases and checks each concrete finite rule; `finite_trimmed_lifting` composes these with independently proved typed lifting. The productive-symbol equivalence and shortest-yield property then prove **exactly** that the symbols and lengths feeding `typedThickness G` agree with those in the actual finite trimmed CFG. The start-language theorem likewise proves preservation for every yield.

## 5. Independent operational reachability = successful-tree retention

A *second*, nondefinitional, inductive predicate has constructors:
```lean
inductive OperationalReachable (G : SSBNFGrammar NT) : NT → U1 → Prop
  | root (hs : A ∈ G.startRules) (hd : TypedDerives G A μ w) :
      OperationalReachable G A μ
  | left (ha : OperationalReachable G A (μ * ν))
      (hr : (A, B, C) ∈ G.binaryRules)
      (hB : TypedDerives G B μ u)
      (hC : TypedDerives G C ν v) :
      OperationalReachable G B μ
  | right (ha : OperationalReachable G A (μ * ν))
      (hr : (A, B, C) ∈ G.binaryRules)
      (hB : TypedDerives G B μ u)
      (hC : TypedDerives G C ν v) :
      OperationalReachable G C ν
```
This is a least inductive productive-rule reachability relation. Unlike `RetainedTypedSymbol`, it is not defined using `TypedOccurrence` or an existential successful start-tree path. The nontrivial theorem **proves** their coincidence, in both directions:
```lean
theorem operational_retained_iff (G : SSBNFGrammar NT)
    (A : NT) (μ : U1) :
    OperationalReachable G A μ ↔ RetainedTypedSymbol G A μ
```
The forward proof is induction on `OperationalReachable`, using `retained_at_start` and `retained_binary_children`. The reverse proof extracts an actual typed derivation from the root occurrence and transports the operational reachability along the occurrence path by induction (`occurrence_to_operational`).

Exact finite rule correspondences:
```lean
theorem finite_operational_terminal_iff (G : SSBNFGrammar NT)
    (A : NT) (μ : U1) (c : Terminal) :
    ((A, μ), c) ∈ (FiniteTrimmedRefinement G).terminalRules ↔
      (A, c) ∈ G.terminalRules ∧ μ = hU [c] ∧
        OperationalReachable G A μ

theorem finite_operational_binary_iff (G : SSBNFGrammar NT)
    (A B C : NT) (μ ν ρ : U1) :
    ((A, μ), (B, ν), (C, ρ)) ∈
      (FiniteTrimmedRefinement G).binaryRules ↔
      (A, B, C) ∈ G.binaryRules ∧ μ = ν * ρ ∧
        OperationalReachable G A μ ∧
        OperationalReachable G B ν ∧ OperationalReachable G C ρ
```
Both follow from concrete finite-rule iff lemmas and separately proved `operational_retained_iff`. Thus the mathematical **productive/reachable trimming fixed-point characterization** is proved. No executable trimming algorithm, its termination or resource bound is part of this report; those are separate claims.

## 6. Minimum-length typed thickness, and intrinsic lower bound

`shortestTypedLength` uses **`Nat.find`** on the set of lengths of actual `TrimmedTypedDerives` terminal yields, using a fallback of 0 only for non-retained/unproductive symbols. Retained symbols are always productive. `shortestTypedLength_spec` proves this least length is realized; `shortestTypedLength_le` proves it is minimal; `shortest_length_characterization` identifies it with **any** shortest-length or shortlex-minimal terminal yield. Shortlex tie-breaking is irrelevant to *length*.

`retainedTypedPairs G : Finset (NT × U1)` is exactly `{(A,μ) | RetainedTypedSymbol G A μ}`. The user-facing `typedThickness G` is the `Finset.max'` of the image of this set under `shortestTypedLength`, union `{1}`. The proof `shortest_le_typedThickness` is a real `Finset.le_max'` application. **It is not the longest word in `GrammarLanguage G`; it is not defined from `witness n`; it has no language-dependent shortcut.** By `finite_trimmed_productive_iff_retained` and `finite_trimmed_shortest_length`, the finite typed CFG's productive non-start symbols and each least yield length are precisely those used in the image defining thickness.

Universal main theorem:
```lean
theorem intrinsic_typed_thickness_lower_bound_all (n : Nat)
    {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT)
    (hLang : GrammarLanguage G = TCSPhase2.Language n) :
    3 * 2 ^ n - 2 ≤ typedThickness G

theorem intrinsic_typed_thickness_lower_bound (n : Nat) (hn : 1 ≤ n)
    {NT : Type} [Fintype NT] [DecidableEq NT]
    (G : SSBNFGrammar NT)
    (hLang : GrammarLanguage G = TCSPhase2.Language n) :
    3 * 2 ^ n - 2 ≤ typedThickness G
```
This quantifies over **ALL** finite SSBNF production presentations of the given language, with no bound on NT or P and not even a reducedness condition. The first theorem has no `n ≥ 1` premise (it also handles n=0). The exact proof pipeline:
1. Use existing `TCSPhase2.witness_mem_language` and language equality to put `witness n` in `GrammarLanguage G`.
2. Prove it is nonempty and extract a real `S0 → A` via `nonempty_start_has_root`.
3. Existing `TCSPhase2.witness_noSquare` and `hU_one_iff_noSquare` give `hU(witness n)=U1.one`. Lift the actual derivation with `typed_complete`; the start rule gives `RetainedTypedSymbol G A U1.one`.
4. For an arbitrary `TrimmedTypedDerives G A U1.one v`, `trimmed_lifting` yields the original derivation and hU-type. `start_rule_generates` and `hLang` put `v` in `Language n`. Existing `TCSPhase2.unique_type_one` proves `v=witness n`. Thus the typed language at this retained child is a true singleton, proved from syntax—not assumed.
5. Realize the minimum by `shortestTypedLength_spec`. It must be `(witness n).length`; substitute unchanged `TCSPhase1.witness_length` and apply `shortest_le_typedThickness`.

Mathematically distinct Phase 1/2 evidence: `grammar_characteristic_exponential_lower_bound` is a **conditional** lower bound for set-driven operators with characteristic samples for the punctured target; it requires its own `hMinus` and `hS` premises. This is NOT the intrinsic *representation* lower bound, which is unconditional once `GrammarLanguage G = Language n`, and assumes no characteristic sample, learner, convergence stage or mind-change bound. Phase 3C's `language_clark_eyraud` and `languageMinus_typed` remain independently proved and regression-compiled.

## 7. Lean build, logical axiom audit and source integrity

The CI workflow `.github/workflows/tcs-phase4-lean.yml` performs `lake update`, `lake exe cache get`, `lean --version`, `lake --version`, `lake build`, then *directly* runs `lake env lean` on the **19 Phase 1–3C modules and 9 Phase 4 modules (28 total)**, piping their logs to individual files. It then scans every Lean source `TCSPhase*.lean` for whole forbidden proof tokens `sorry|admit|axiom|opaque`, and scans all recorded `#print axioms` logs for `sorryAx`. The checks are fully enabled.

The source/comment issue in run #39020321571 was a false positive **in a comment**, after complete successful compilation and standard-only axiom printing. It was fixed with a one-line comment-only edit; the proof checker and scan were **not** relaxed.

The fully compiled prior run #39020321571 showed these exact axiom dependencies (rechecked again in the final integrated `TCSPhase4Main.lean`):

| Key group | Recorded `#print axioms` output |
| --- | --- |
| `typed_lifting`, `trimmed_lifting`, `trimmed_grammar_language_eq`, `operational_retained_iff` | `[propext, Quot.sound]` |
| `finite_trimmed_lifting`, `finite_trimmed_grammar_language_eq`, `finite_trimmed_shortest_length` | `[propext, Classical.choice, Quot.sound]` |
| `shortestTypedLength_spec`, `shortest_length_characterization`, `shortest_le_typedThickness` | `[propext, Classical.choice, Quot.sound]` |
| `intrinsic_typed_thickness_lower_bound_all` and manuscript n-positive theorem | `[propext, Classical.choice, Quot.sound]` |

No independent mathematical `axiom`, `opaque` theorem, or `sorryAx` occurs in the verified dependencies. These are Lean's permitted built-in logical axioms.

The source-level names in `TCSPhase4Main.lean` now explicitly import **both** `TCSPhase4FiniteRefinement.lean` and `TCSPhase4OperationalTrim.lean` and print their central axioms in addition to the intrinsic theorem. All original Phase 1–3C sources are unchanged from Phase 3C base. Manuscript/response/PDF files were not edited. A final `compare_commits` audit and head-matching CI are performed separately and recorded in the final user-facing result.

## 8. Scope and final evaluation

**Fully established for Corollary 6.4:** finite arbitrary SSBNF with real production sets and start trees; independently defined original/typed derivations and lifting equivalence; actual successful typed-tree retained symbols; finite filtered SSBNF typed refinement; semantic and independent productive-rule operational reachability agreement; exact typed-symbol languages and whole grammar start-language preservation; true shortest yields and max over retained symbols; size-unrestricted presentation-independent exponential lower bound.

**Still outside this Phase 4 scope:** CFG-to-SSBNF normalization *algorithm* and its complexity, an **executable** typed-pruning algorithm's termination and runtime (as distinct from the proved inductive least-reachability characterization), general-monoid `h` beyond fixed `hU`, all alphabets beyond the actual five bracket terminals, `Rec_h` algorithm soundness/completeness, particular Gold learning convergence times, any theorem on the full TCS paper not cited above.

**Judgment A** when and only when the final branch HEAD CI reports success after compilation, full forbidden-token scan and axiom scan. A purely mathematical compilation with a failing audit is **not** treated as full CI success. The claimed A pertains to Corollary 6.4's **mathematical SSBNF/operational-trimming formulation**, not to executable algorithm correctness or the entire manuscript.
