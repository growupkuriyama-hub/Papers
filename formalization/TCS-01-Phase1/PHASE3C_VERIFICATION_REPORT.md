# Phase 3C — Independent Lean 4 Verification Report for TCS Appendix C

**Research target:** Kuriyama, *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*, Theoretical Computer Science, submission **TCS-D-26-00494**.

**Formal verification verdict: A for the stated Phase 3C language-theoretic targets.** The fully unconditional branch-synchronization, path-congruence, Clark–Eyraud and fixed-typing claims are checked by the Lean 4 kernel using the exact original Phase 2 definitions. Class membership beyond those modeled language properties is not claimed.

## A. Source audit and immutable baseline

1. Latest checked manuscript (2026-10-17): GitHub `growupkuriyama-hub/Papers`, main HEAD **`97d5e57b24f13901c0164e9ce248f2eca8dc40a0`**.
2. English manuscript `01_fixed-h-cfg/main.tex`, Git **blob SHA `64c6db794e6438a71a706569621ae35038329541`**. `01_fixed-h-cfg/PAPER.yaml` reports **internal version v217** (the supplied instruction anticipated v217). The paper lists a separate SHA256 of the main source, `3bb2add15c843371bd2fcbf767e5279384ce3eae597bc87bd44e15c4fba593f7`.
3. Read and compared the canonical Appendix C parser, Recognition Lemma, branch synchronization lemma, path congruence proposition and proof of Proposition 6.3(i) against the verified Phase 3B interpretation. The terminal notation maps exactly as in the Phase 1–3B code: `a`, floor brackets (`left,right`), ceiling brackets (`squareLeft,squareRight`). No new parser rule or modified proof hypothesis was detected in the relevant v217 passages. The latest manuscript is authoritative for this verification.
4. Working branch `formalization/tcs-phase3c-ce-proof-20261017` created from the Phase 3B final HEAD `c94039d7482b8930b16515e77409fb7214b00737`. All earlier Phase 1–3B source files and statements were preserved. No manuscript, `PAPER.yaml`, Japanese translation, reviewer response, marked/clean PDF, or other protected artifact has been edited.
5. Environment: Lean **4.24.0**, compiler commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`; Lake **5.0.0**; Mathlib tag **v4.24.0**, historical resolved mathlib SHA `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. On the CI runner, `lake update` resolves the tag; this project does not track a generated manifest.

## B. Mathematical results and exact Lean interfaces

### Milestone A. Branch prerequisites — `TCSPhase3CAux.lean`

1. `frame_weight_pos (f : Frame) : 0 < frameWeight f` (all frames have positive weight).
2. `weight_append (α ψ : Stack) : weight (α ++ ψ) = weight α + weight ψ`.
3. `weight_pos_of_ne (h : α ≠ []) : 0 < weight α`.
4. `weight_nonempty_prefix_gt (α ψ : Stack) (h : α ≠ []) : weight ψ < weight (α ++ ψ)`.
5. `weight_of_run_suffix_le (h : Run bound ψ w θ) : weight θ ≤ weight ψ`. Derived from the already certified `run_weight_le`.
6. `suffix_cancel_right (α β ψ : Stack) (h : α ++ ψ = β ++ ψ) : α = β`.
7. `classified_first_visit` proves:
   ```lean
   α ≠ [] → Run bound (α ++ ψ) w θ →
     (∃ β, β ≠ [] ∧ Run bound α w β ∧
       θ = β ++ ψ ∧ weight ψ < weight θ)
     ∨ (∃ u v, w = u ++ v ∧ Run bound α u [] ∧
       Run bound ψ v θ ∧ weight θ ≤ weight ψ)
   ```
   The two sides are strictly disjoint by weight.
8. `distinct_initial_steps`: for `c ≠ d` and two one-letter transitions `Step bound σ c σ₁`, `Step bound σ d σ₂`, there are `i`, `ψ`, `i+1 ≤ bound`, `σ = Frame.nt (i+1) :: ψ` and exactly two cases. Either `c=squareLeft`, `d=left` with successors `E_i ceilClose ψ` and `E_i E_i floorClose ψ`; or the roles are reversed. Proven by eliminating all pairs of the five `Step` constructors.

### Milestone B. Full branch synchronization — `TCSPhase3CSynchronization.lean`

- `opposite_branches_both_visit` assumes actual suffix runs from `E_i ceilClose ψ` and `E_i E_i floorClose ψ` to a *common* endpoint. It produces first-visit factors `u,v,xr,yr`, with `Run bound [E_i,ceilClose] u []` and `Run bound [E_i,E_i,floorClose] v []`, plus residual runs `Run bound ψ xr θ`, `Run bound ψ yr θ`. Both one-sided-visitation cases are excluded by opposite weight inequalities. The two-unvisited case is excluded using Phase 3B `run_preserves_last_marker` and `ceil_floor_suffix_ne` after right cancellation.
- `oriented_branch_synchronization` combines these visits with the initial opening character and invokes the already proved `recognition_converse`, obtaining **actual** `Language (i+1)` membership of the complete bracketed factors.
- `branch_synchronization` (the final appendix lemma):
   ```lean
   theorem branch_synchronization {bound : Nat} {σ θ : Stack}
       {c d : Terminal} {x y : Word}
       (hc : c ≠ d) (hx : Run bound σ (c :: x) θ)
       (hy : Run bound σ (d :: y) θ) :
       ∃ (i : Nat) (ψ : Stack) (w w' xr yr : Word),
         1 ≤ i ∧ i ≤ bound ∧ σ = Frame.nt i :: ψ ∧
         c :: x = w ++ xr ∧ d :: y = w' ++ yr ∧
         w ∈ TCSPhase2.Language i ∧ w' ∈ TCSPhase2.Language i ∧
         Run bound ψ xr θ ∧ Run bound ψ yr θ
   ```
   No assumption on `ClarkEyraud`, `path_congruence`, or original start state appears.

### Milestone C. Path congruence — `TCSPhase3CPathCongruence.lean`

- `language_word_nonempty (i) (w) (hw : w∈Language i) : w ≠ []`. Derived from `language_opening_prefix` verified in Phase 3.
- `path_congruence`:
   ```lean
   theorem path_congruence (n : Nat) :
       ∀ (σ θ : Stack) (x y : Word),
         Run n σ x θ → Run n σ y θ →
         Distributions (TCSPhase2.Language n) x =
           Distributions (TCSPhase2.Language n) y
   ```
   **Measure:** `x.length + y.length`, proved by `Nat.strong_induction_on`. Cases: empty word (using `run_no_nonempty_cycle`); equal first symbol (using `step_deterministic` and `distributions_left_congruent`); different first symbol (using certified `branch_synchronization`, `complete_subtree_exchange`, right then left distribution congruence).
   The required `xr.length + yr.length < x.length + y.length` is **proved in Lean from both exact factorization equalities and the nonemptiness of the two actual grammar words**. No recursion hypothesis is used at a non-decreasing measure.

### Milestone D. Unconditional Clark–Eyraud — `TCSPhase3CClarkEyraud.lean`

   ```lean
   theorem language_clark_eyraud (n : Nat) :
       ClarkEyraud (TCSPhase2.Language n)
   ```

   `ClarkEyraud`, `SharedContext`, `Distributions` are exactly the Phase 2 declarations. For arbitrary nonempty factors x, y and a shared context (p,q) in the original `Language n`, use `grammar_language_parses` to construct *two independently verified actual grammar parses*. Split the accepting runs into p, x/y, q with `run_append_split`. Their states after p are equal by `run_deterministic`; states before q are equal by `run_reverse_injective`. The resulting co-terminal runs of x and y meet `path_congruence` exactly. No CE premise is imported.

   The theorem holds for all natural n, including zero; the manuscript focuses on n≥1, making this formally a stronger height domain for the structurally equivalent construction.

### Milestone E. Unconditional fixed typing and finiteness — same file

   ```lean
   theorem punctured_language_finite (n : Nat) :
       (LanguageMinus n).Finite

   theorem languageMinus_typed (n : Nat) :
       TypedSubstitutable hU (LanguageMinus n)
   ```

   Finiteness follows by subset from Phase 2's unconditional `language_finite`. Typed substitutability follows from the **unchanged** Phase 2 bridge `languageMinus_typed_of_CE`, providing the theorem above as its CE input. The conclusion has **no hCE hypothesis**. The regular finite-monoid morphism `hU`, the `LanguageMinus` target and the Phase 2 language are unchanged.

## C. Compilation and axiom evidence

### Successful, staged GitHub Actions jobs

- Aux lemmas: [#39014948700](https://github.com/growupkuriyama-hub/Papers/actions/runs/39014948700), 7,380 jobs, direct compiler and logical axiom audit successful.
- Branch synchronization: [#39015203388](https://github.com/growupkuriyama-hub/Papers/actions/runs/39015203388), 7,382 jobs, fully successful.
- Path congruence: [#39015277582](https://github.com/growupkuriyama-hub/Papers/actions/runs/39015277582), 7,384 jobs, fully successful.
- Clark–Eyraud and typed substitutability: [#39015332915](https://github.com/growupkuriyama-hub/Papers/actions/runs/39015332915), 7,386 jobs, fully successful.

The final aggregation module is `TCSPhase3CMain.lean` and is included in the branch's default Lake targets and direct CI audit loop.

### Axiom output observed in successful jobs

```text
TCSPhase3.distinct_initial_steps:
  [propext, Quot.sound]
TCSPhase3.classified_first_visit:
  [propext, Classical.choice, Quot.sound]
TCSPhase3.branch_synchronization:
  [propext, Classical.choice, Quot.sound]
TCSPhase3.language_word_nonempty:
  [propext]
TCSPhase3.path_congruence:
  [propext, Classical.choice, Quot.sound]
TCSPhase3.language_clark_eyraud:
  [propext, Classical.choice, Quot.sound]
TCSPhase3.punctured_language_finite:
  [propext, Classical.choice, Quot.sound]
TCSPhase3.languageMinus_typed:
  [propext, Classical.choice, Quot.sound]
```

Only Lean's permitted, built-in logical principles appear. There are no new mathematical postulates, no unfilled proofs and **no `sorryAx`**. The CI also scans sources for all forbidden proof tokens. `TCSPhase1.lean`, `TCSPhase2.lean`, `TCSPhase2Bridge.lean`, and every Phase 3/3B theorem file are compiled again without changes. Build coverage includes every one of the branch's 19 direct Lean source files.

The initial auxiliary-module attempt had one unnecessary specialized marker helper whose binder could not be inferred; it was removed and replaced by the already-proved general marker theorem. The first branch synchronization attempt had an ambiguity between `_root_.Language` and the actual `TCSPhase2.Language`; qualification fixed that error. These were elaboration failures, not mathematical counterexamples. No failed intermediate run was represented as proof success.

## D. Paper correspondence

| Paper source, Appendix C or Section 6 | Verified Lean theorem |
| --- | --- |
| Five deterministic reversible parser transitions, Appendix C parser properties | `Step`, `Run`, `step_deterministic`, `run_reverse_injective` (Phase 3) |
| Strictly decreasing stack weight | `step_weight_lt`, `run_no_nonempty_cycle` (Phase 3) |
| Initial-suffix visit decomposition and last closing marker | `first_visit_factorization` (Phase 3B), `run_preserves_last_marker` (Phase 3B), `classified_first_visit` (Phase 3C) |
| Recognition Lemma C.1, both assertions | `recognition_iff`, `recognition_arbitrary_start` (Phase 3B) |
| Complete-subtree exchange | `complete_subtree_exchange` (Phase 3B) |
| Branch synchronization lemma, manuscript approx. lines 2297–2321 | `distinct_initial_steps`, `opposite_branches_both_visit`, **`branch_synchronization`** |
| Path congruence proposition, approx. lines 2323–2341 | **`path_congruence`** |
| Proof of Proposition 6.3(i), approx. lines 2343–2358 | **`language_clark_eyraud`**, `language_finite` |
| Singleton-puncture's typed substitutability | `languageMinus_type_zero` (Phase 2), `languageMinus_typed_of_CE` (Phase 2), **`languageMinus_typed`** |
| Punctured language finite | **`punctured_language_finite`** |

### What has NOT been claimed

- The paper's class-membership notation `Ccf{h_0} ∩ Ccf{h_U}` is not formally represented by a Lean `Ccf` predicate here. The **finite + CE** language-theoretic ingredients have been proved; finite languages are context-free in ordinary mathematics, but a formal class-membership theorem under a separately encoded definition has NOT been proved.
- The algorithmic results on `Rec_h`, class-level proper inclusions, exponential *typed-thickness* guarantees from actual learning operators, actual characteristic-sample existence for specific reconstruction procedures, arbitrary grammar presentations and Corollary 6.4 are not claimed.
- Formalizing the **entire TCS manuscript** is not the same thing as completing Appendix C's language-theoretic core. The latter is what this phase establishes.

## E. Dependency independence and integrity checks

```text
Phase 3 parser Step/Run, actual Phase 2 CFG Derives & Language
   -> Phase 3B first-visit factorization and exact recognizer
   -> Phase 3B complete-subtree exchange
   -> Phase 3C branching case analysis and positive weights
   -> Phase 3C branch_synchronization
   -> Phase 3C path_congruence
   -> Phase 3C language_clark_eyraud
   -> unchanged Phase 2 languageMinus_typed_of_CE
   -> Phase 3C languageMinus_typed
```

Every arrow is a Lean module import or theorem application checked by the compiler. In particular neither branch synchronization nor path congruence nor Clark–Eyraud substitutability is assumed by its own proof, and there is no helper relation silently redefined into the desired conclusion. No existing phase statement, original `Distributions` or `ClarkEyraud` definition, original `TCSPhase2.Language` or `LanguageMinus`, monoid morphism, or protected TCS submission artifact was altered.

**Verdict: A — all four Phase 3C requested theorems have been machine verified.** This does not imply that all possible TCS publication obligations have been formalized.
