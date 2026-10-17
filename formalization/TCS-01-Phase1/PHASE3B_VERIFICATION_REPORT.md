# TCS Phase 3B — Lean 4 Formal Verification Audit (2026-10-17)

## A. Source of truth, GitHub and environment

- Research paper: Takayuki Kuriyama, *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*, TCS-D-26-00494.
- Main GitHub source at inspection: `9a094b68ed683c85e2eab8f33cd978f45af0a19f`. `01_fixed-h-cfg/main.tex` blob SHA `bc638f6032cb04414cb36a88ad6953188097add1`; `PAPER.yaml` internal **v215**. The supplied instructions anticipated v213. Comparison with the Phase 3 source v212 found no changes to the five CFG productions, to the five bounded parser transition rules, or to Appendix C's recognition and exchange claims. Intermediate revisions affected mathematical notation and presentation elsewhere, notably Proposition 6.3(ii).
- Branch: `formalization/tcs-phase3b-suffix-recognition-20261017` from the Phase 3 verified HEAD `1e400c20d05d49648095bc8324303c0b5e67cf77`. Existing Phase 1, 2, 3 proof modules were not edited.
- Lean 4.24.0 / compiler commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`; Lake 5.0.0; Mathlib tag v4.24.0, previously resolved commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.
- Terminal mapping inherited unchanged: `Terminal.a` = a; `Terminal.left`/`right` = literal floor brackets; `squareLeft`/`squareRight` = literal ceiling brackets. Nonterminal `Frame.nt i` is bounded in the parser's expansion rules, which enforce `i+1 ≤ bound`.
- The existing stack type admits natural-number indices at arbitrary inactive stack positions; the transition relation enforces the bound when expanding a nonterminal, and the grammar/recognition theorems restrict `i ≤ bound`. An explicit well-formedness predicate for all inactive stack frames is not needed in these proved implications and has not been introduced.

## B. Verified statements, exact hypotheses, and manuscript correspondence

**Every theorem below compiled for arbitrary finite words and arbitrary naturals, not just fixed small examples.**

### Milestone A: reverse one-step suffix decomposition

File: `TCSPhase3Suffix.lean`. Paper: Appendix C "Parser and stack properties", untouched-suffix claim.

- `no_step_from_nil`:
  `¬ Step bound [] c t` (no assumptions).
- `run_from_nil`:
  `Run bound [] w t → w=[] ∧ t=[]`.
- `step_prefix_decompose`:
  `α ≠ [] → Step bound (α ++ ψ) c θ → ∃β, Step bound α c β ∧ θ=β ++ ψ`.
  This supports a single-frame prefix that is popped completely; **β is allowed to be []**. The nonempty-prefix premise is explicit. The first-step relation and index bound are unchanged from the earlier parser.

### Milestone B: first-visit factorization

Same file. Paper Appendix C's crucial first-visit suffix property.

- `first_visit_factorization`:
  ```lean
  theorem first_visit_factorization {bound : Nat}
      {α ψ θ : Stack} {w : Word} (hα : α ≠ [])
      (h : Run bound (α ++ ψ) w θ) :
      (∃ β : Stack, β ≠ [] ∧ Run bound α w β ∧ θ = β ++ ψ) ∨
      (∃ u v : Word, w = u ++ v ∧ Run bound α u [] ∧
        Run bound ψ v θ)
  ```
  This is inductively proved on the input word, applying `step_prefix_decompose` at every nonempty-active-prefix step. When an active-prefix transition first produces the empty prefix, the *remaining* word is routed to the suffix's independent run, without asserting that the suffix must remain intact afterward. Consequently the first visit occurs at the exact split constructed by induction, not at a guessed index.
- `run_to_suffix_iff_run_to_nil`:
  ```lean
  theorem run_to_suffix_iff_run_to_nil {bound : Nat}
      {α ψ : Stack} {w : Word} (hα : α ≠ []) :
      Run bound (α ++ ψ) w ψ ↔ Run bound α w []
  ```
  The 'active prefix never empties' case is excluded using `List.length_append`. In the visited-suffix case, `run_no_nonempty_cycle` eliminates any nonempty remainder, so the first visit consumes the **entire input**. The converse reuses `run_suffix`.

### Milestone C: closing marker preservation

File: `TCSPhase3Marker.lean`. Paper Appendix C's last-marker invariant.

- `run_single_closer`:
  `(m=Frame.ceilClose ∨ m=Frame.floorClose) → Run bound [m] w θ → (θ=[] ∨ θ=[m])`.
- `run_preserves_last_marker`:
  ```lean
  theorem run_preserves_last_marker {bound : Nat} {m : Frame}
      (hm : m = Frame.ceilClose ∨ m = Frame.floorClose)
      {α θ : Stack} {w : Word}
      (h : Run bound (α ++ [m]) w θ) (hθ : θ ≠ []) :
      ∃ β : Stack, θ = β ++ [m]
  ```
  This proves exact persistence of the bottom closing marker in any *nonempty* result. The restriction to literal closing markers is necessary; not a claim for arbitrary nonterminal bottom symbols.
- `ceil_floor_suffix_ne`:
  `∀ α β : Stack, α ++ [Frame.ceilClose] ≠ β ++ [Frame.floorClose]`.

### Milestone D: reverse CFG recognition

File: `TCSPhase3RecognitionConverse.lean`. Paper Appendix C Recognition Lemma, converse.

- `split_run_to_nil`:
  for nonempty α and nonempty ψ,
  `Run bound (α++ψ) w [] → ∃u v, w=u++v ∧ Run bound α u [] ∧ Run bound ψ v []`.
  Derived directly from the verified first-visit disjunction.
- `run_ceil_close_exact`:
  `Run bound [Frame.ceilClose] w [] → w=[Terminal.squareRight]`.
- `run_floor_close_exact`:
  `Run bound [Frame.floorClose] w [] → w=[Terminal.right]`.
- `run_nt_nil_derives`:
  ```lean
  theorem run_nt_nil_derives (bound : Nat) :
      ∀ (i : Nat) (w : Word), i ≤ bound →
        Run bound [Frame.nt i] w [] → Derives i w
  ```
  Proved by general induction on the **nonterminal height**. The atom case consumes exactly the letter a. Unary expansion uses first-visit splitting and a precisely consumed ceiling close; binary expansion splits two child parses successively and requires precisely the floor close. Both children are converted via the induction hypothesis into actual `TCSPhase2.Derives` constructors, not a new recognizer-language definition.
- `recognition_converse`:
  ```lean
  theorem recognition_converse (bound i : Nat) (ψ : Stack) (w : Word)
      (hi : i ≤ bound)
      (h : Run bound (Frame.nt i :: ψ) w ψ) :
      w ∈ Language i
  ```
  Uses `run_to_suffix_iff_run_to_nil`, then `run_nt_nil_derives`.
- `recognition_iff`:
  ```lean
  theorem recognition_iff (bound i : Nat) (ψ : Stack) (w : Word)
      (hi : i ≤ bound) :
      Run bound (Frame.nt i :: ψ) w ψ ↔ w ∈ Language i
  ```
  Both directions established: forward recognition from Phase 3, reverse recognition in this file. This is the actual Phase 2 CFG language.

### Milestone E: the SECOND assertion of Recognition Lemma C.1

File: `TCSPhase3RecognitionFull.lean`. Paper Appendix C Recognition Lemma's "Moreover" statement.

- `initial_nt_of_opening_prefix`:
  `OpeningPrefix i w → Run bound s w t → ∃ψ, s=Frame.nt i::ψ`.
  Proved by structural induction on `OpeningPrefix`, using the independently proved parser transition cases to show each opening symbol decreases the exposed nonterminal height before an a is read.
- `recognition_arbitrary_start`:
  ```lean
  theorem recognition_arbitrary_start (bound i : Nat)
      (s t : Stack) (w : Word) (hi : i ≤ bound)
      (h : Run bound s w t) (hw : w ∈ Language i) :
      ∃ ψ : Stack, s = Frame.nt i :: ψ ∧ t = ψ
  ```
  Apply the already verified `language_opening_prefix` (Phase 3) to establish the initial frame, then `generated_word_parses` and `run_deterministic` to identify its final remainder. This discharges the entirety of Recognition Lemma C.1 **without any external premise of substitutability**.

### Optional: complete-subtree exchange

File: `TCSPhase3Subtree.lean`. Paper's independent complete-subtree-exchange lemma.

- `grammar_context_replace`: for `i ≤ n`, `x,y ∈ Language i`, and `p++x++q∈Language n`, conclude `p++y++q∈Language n`. The accepting run of the outer language is split at the left context and the original subtree. `recognition_arbitrary_start` identifies the exact intermediate stack; the alternate subtree is parsed using `generated_word_parses`. Finally `recognition_converse` converts the recombined run into *actual* `Language n` membership.
- `complete_subtree_exchange`:
  ```lean
  theorem complete_subtree_exchange (n i : Nat) (hi : i ≤ n)
      (x y : Word) (hx : x ∈ Language i) (hy : y ∈ Language i) :
      Distributions (Language n) x = Distributions (Language n) y
  ```
  Extensionality on every pair of concrete left/right contexts, with replacement proved in both directions. **No Clark–Eyraud premise is used.**

## C. Actual CI and axiom audit

Successful integrated GitHub Actions run: **[#39010703450](https://github.com/growupkuriyama-hub/Papers/actions/runs/39010703450)**; job **`117332450214`**; exact compiled proof-and-workflow commit **`4319a5c5a9671da10121764232df1e7bf5e96f4e`**.

The workflow executed `lake update`, `lake exe cache get`, `lean --version`, `lake --version`, **`lake build`** and individual **`lake env lean` for each of 14 source modules**, including `TCSPhase3BMain.lean`. The forbidden-word scan on all Lean files and the `sorryAx` scan on printed-axiom logs passed.

```text
Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)
Lake version 5.0.0-src+797c613 (Lean version 4.24.0)
Built TCSPhase3Suffix
Built TCSPhase3RecognitionConverse
Built TCSPhase3Marker
Built TCSPhase3RecognitionFull
Built TCSPhase3Subtree
Built TCSPhase3BMain
Build completed successfully (7378 jobs).
All Phase 1-3B modules compiled without proof holes
```

`#print axioms` results observed in the successful CI run (the printed lists below are exact, with the module prefixes omitted for compactness):

```text
step_prefix_decompose        : []
first_visit_factorization    : [propext]
run_to_suffix_iff_run_to_nil : [propext, Classical.choice, Quot.sound]
run_single_closer            : []
run_preserves_last_marker    : [propext]
ceil_floor_suffix_ne         : [propext]
split_run_to_nil             : [propext, Quot.sound]
run_ceil_close_exact         : []
run_floor_close_exact        : []
run_nt_nil_derives           : [propext, Quot.sound]
recognition_converse         : [propext, Classical.choice, Quot.sound]
recognition_iff              : [propext, Classical.choice, Quot.sound]
initial_nt_of_opening_prefix : []
recognition_arbitrary_start  : [propext, Quot.sound]
grammar_context_replace      : [propext, Classical.choice, Quot.sound]
complete_subtree_exchange    : [propext, Classical.choice, Quot.sound]
```

Empty lists indicate that Lean reports no logical axiom dependencies. All nonempty lists contain *only standard* Lean logical axioms. There is no `sorryAx` dependency, no custom mathematical axiom, and no hidden assumptions. All Phase 1–3 files were built again unchanged.

Intermediate CI attempts were genuinely run. Syntax, binder and type-metavariable elaboration failures were repaired; after the proof code compiled, a strict forbidden-token scan reported a *comment-only* false positive twice, and these comments were revised. The final run passed the complete build **and** both scans. Earlier failed CI runs are not represented as verification successes.

## D. Outstanding proof obligations

**The Phase 3B requested core is complete.** The following are for the subsequent Phase 3C and further downstream work:

1. Appendix C **branch synchronization** for different first input letters, including the matching first-return split and the equal-final-stack weight comparison.
2. Appendix C **path congruence** for any two input words carrying the same parser state to the same state, using the optional complete-subtree exchange now available.
3. **Unconditional `ClarkEyraud (Language n)`**, and the unconditional `TypedSubstitutable hU (LanguageMinus n)` by eliminating the antecedent of the verified Phase 2 bridge.
4. The paper's grammar-size/thickness bounds, reconstruction algorithm `Rec_h`, class-membership proof in the precise manuscript framework, and actual characteristic-sample existence are separate and not covered by this module.

No mathematical counterexample to the manuscript claims was identified. There were no modifications to `main.tex`, `PAPER.yaml`, translations, reviewer responses, PDF artifacts, arXiv, or Editorial Manager; main was not merged.

## E. Verdict

**A — First-visit factorization and both assertions of Recognition Lemma C.1 completely machine verified.**

The optional complete-subtree exchange also succeeded as an unconditional general theorem. This success does not imply that branch synchronization, path congruence or the full Clark–Eyraud claim has already been machine verified.
