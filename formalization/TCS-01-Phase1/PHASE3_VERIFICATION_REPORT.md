# Appendix C Phase 3 — machine-verification audit (2026-10-17)

## 1. Provenance and environment

Paper: Takayuki Kuriyama, *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*; Theoretical Computer Science, TCS-D-26-00494.

Canonical manuscript: `growupkuriyama-hub/Papers/01_fixed-h-cfg/main.tex`, internal **v212**, main HEAD at inspection `4193be1fb437a67479ca75ace368571c7d38d389`; manuscript blob SHA `b64aea13d875e7ebd8aa8c5a57ec46dd9def3006`. The `PAPER.yaml` at the same revision identifies v212. Appendix C is around manuscript lines 2197–2358, and the target CFG near 1108–1131. The v211→v212 differences were mathematical-notation/renaming changes, not changes to the five CFG or parser rules.

Phase 3 branch: `formalization/tcs-phase3-appendix-c-20261016` from proven Phase 2 commit `adf208645921f54b9ce4d9a1f05ee08396dca50e`. No earlier Lean proof was modified. Only `lakefile.lean` was extended to register the new modules.

Lean 4.24.0 (Lean commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`), Lake 5.0.0, Mathlib v4.24.0 (previously resolved SHA `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`), Ubuntu GitHub Actions. A `lake-manifest.json` is not tracked in this GitHub project; each CI run executes `lake update` to resolve the pinned tag, followed by `lake exe cache get`.

Terminal symbol correspondence: Phase 2 `Terminal.a`→a, `left`→floor left, `right`→floor right, `squareLeft`→ceiling left, `squareRight`→ceiling right. All are genuine, distinct terminals.

## 2. Executed compiler evidence

**Final successful CI:** [Actions run #39004829263](https://github.com/growupkuriyama-hub/Papers/actions/runs/39004829263), job `117315042499`, proof/CI commit `8847815b9992905964d01465564c8b3168058250`.

```text
Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)
Lake version 5.0.0-src+797c613 (Lean version 4.24.0)
Built TCSPhase1
Built TCSPhase2
Built TCSPhase2Bridge
Built TCSPhase3Parser
Built TCSPhase3Recognition
Built TCSPhase3Congruence
Built TCSPhase3Prefix
Built TCSPhase3Main
Build completed successfully (7366 jobs).
All modules compiled with no holes
```

The workflow executed `lake build`, then directly compiled every one of the eight Lean source files with `lake env lean`, including **`lake env lean TCSPhase3Main.lean`**. The source scan found no forbidden proof token and none of the printed axiom outputs contained `sorryAx`. The dependency axioms reported are only the standard `propext`, `Classical.choice`, and `Quot.sound`, or no axioms at all.

## 3. Exact proved Lean statements

All results below are unconditional (other than their mathematically specified input assumptions such as an actual `Step` or `Run` proof).

### Milestone A — Appendix C lines 2209–2229 (verified core)

- `Step bound : Stack → Terminal → Stack → Prop`: five independently defined inductive parser rules including the precise expansion premise `i+1 ≤ bound`.
- `Run bound : Stack → Word → Stack → Prop`: empty run constructor and a constructor extending any letter transition with a remaining-word run. Neither definition uses CFG derivation or the desired theorem as a premise.
- `run_empty bound s : Run bound s [] s`.
- `step_deterministic`: `Step bound s c t → Step bound s c u → t = u`.
- `step_reverse_injective`: `Step bound s c u → Step bound t c u → s = t`.
- `run_append`: `Run bound s x t → Run bound t y u → Run bound s (x ++ y) u`.
- `run_append_split`: `Run bound s (x ++ y) t → ∃mid, Run bound s x mid ∧ Run bound mid y t`.
- `run_deterministic`: `Run bound s w t → Run bound s w u → t = u`.
- `run_reverse_injective`: `Run bound s w u → Run bound t w u → s = t`. In particular this verifies the crucial **fixed-word partial-injection** principle for arbitrary stacks and words.

Audit limitation: `Stack` is a list of `Frame.nt i` for arbitrary natural i or closing markers; the transition relation gates expansions by `bound`. A separate `WellFormedStack` predicate and preservation proof ensuring *all* inactive stack frames have index ≤ bound have not yet been added. This is an explicit modeling distinction from the manuscript's bounded stack alphabet, not an extra mathematical assumption in the proved parser claims.

### Milestone B — Appendix C lines 2231–2245 (partial)

- `step_suffix` and `run_suffix`: appended stack suffixes remain untouched **when following an already established run of the isolated prefix**.
- `step_weight_lt`: `Step bound s c t → weight t < weight s` with weights `4^i` on `E_i`, and one on either closing marker.
- `run_weight_le`: `Run bound s w t → weight t ≤ weight s`.
- `run_weight_lt`: `Run bound s w t → w ≠ [] → weight t < weight s`.
- `run_no_nonempty_cycle`: `Run bound s w s → w = []`.

NOT proved: complete **first-visit** suffix factorization for an arbitrary run beginning at `prefix ++ suffix`; preservation of the bottom closing marker up to its pop. The one-way suffix-extension theorem must not be mistaken for these stronger statements.

### Milestone C — Lemma C.1, lines 2247–2281 (forward only)

- `derives_run`: `Derives i w → ∀ bound ψ, i ≤ bound → Run bound (Frame.nt i :: ψ) w ψ`. It constructs parser runs from actual Phase 2 CFG derivations using concatenation of child runs and correct closing markers.
- `generated_word_parses`: `i ≤ bound → w ∈ Language i → Run bound (Frame.nt i :: ψ) w ψ`.
- `grammar_language_parses`: `w ∈ Language n → Run n [Frame.nt n] w []`.
- `OpeningPrefix i w` inductively expresses i unary/binary opening terminal symbols followed by the literal `a` (and an arbitrary suffix).
- `derived_opening_prefix`: `Derives i w → OpeningPrefix i w` and `language_opening_prefix`: `w ∈ Language i → OpeningPrefix i w`, both for every i.

NOT proved: reverse implication `Run bound (Frame.nt i :: ψ) w ψ → w ∈ Language i`, or the statement that *any* `Run bound s w t` with `w ∈ Language i` forces `s = Frame.nt i :: ψ` and `t = ψ`. Recognition Lemma C.1 is therefore NOT completely verified.

### Milestone D — lines 2283–2294 (congruence only)

- `distributions_left_congruent`: equality of `Distributions L x` and `Distributions L y` entails equality after prefixing both factors by arbitrary z.
- `distributions_right_congruent`: same after suffixing.
- `distributions_two_sided_congruent`: same after both prefixing and suffixing.

NOT proved: complete-subtree exchange for two arbitrary members of `Language i` in a surrounding `Language n` context. This still requires the full Recognition Lemma.

### Milestones E and F and final targets — NOT proved

- Branch synchronization (lines 2296–2319): missing the precise first-visit suffix and distinct-closing-marker invariants.
- Path congruence (lines 2322–2340): missing branch synchronization, subtree exchange, and the strictly-decreasing recursive-measure proof.
- `language_clark_eyraud (n : Nat) : ClarkEyraud (Language n)` (lines 2342–2357): NOT declared as a theorem, because it has not been proved.
- `languageMinus_typed (n : Nat) : TypedSubstitutable hU (LanguageMinus n)`: NOT declared. The pre-existing Phase 2 lemma `languageMinus_typed_of_CE` still **explicitly assumes** `ClarkEyraud (Language n)`.
- The `TCSPhase3Main.lean` file is a checked audit/import aggregator and does not claim these absent theorems.

There is **no mathematical counterexample** identified in this phase. The gap is the actual missing proof chain and detailed stack invariants, not a newly introduced assumption.

## 4. Axiom audit from #print axioms

```text
TCSPhase3.step_deterministic: [propext]
TCSPhase3.step_reverse_injective: no axioms
TCSPhase3.run_append: no axioms
TCSPhase3.run_append_split: no axioms
TCSPhase3.run_deterministic: [propext]
TCSPhase3.run_reverse_injective: no axioms
TCSPhase3.step_suffix: no axioms
TCSPhase3.run_suffix: no axioms
TCSPhase3.step_weight_lt: [propext, Classical.choice, Quot.sound]
TCSPhase3.run_no_nonempty_cycle: [propext, Classical.choice, Quot.sound]
TCSPhase3.derives_run: [propext, Quot.sound]
TCSPhase3.generated_word_parses: [propext, Quot.sound]
TCSPhase3.grammar_language_parses: [propext, Quot.sound]
TCSPhase3.distributions_left_congruent: [propext, Quot.sound]
TCSPhase3.distributions_right_congruent: [propext, Quot.sound]
TCSPhase3.distributions_two_sided_congruent: [propext, Quot.sound]
TCSPhase3.derived_opening_prefix: [propext]
TCSPhase3.language_opening_prefix: [propext]
```

All of these axiom results were observed after successful compilation; none includes `sorryAx`. No user-defined mathematical axiom or opaque oracle was supplied. Phase 1 and Phase 2 axiom audits were rerun unchanged in the same successful job.

Intermediate diagnostics: run #39003830032 initially exposed Lean binder/proof-application errors, fixed by #39003981149 (successful parser-only CI); #39004225352 verified parser/recognition/congruence; #39004458200 exposed harmless elaboration errors in prefix proof; #39004601678 verified that proof; #39004829263 verified the integrated aggregator and all modules. Compiler errors in intermediate commits were repaired; no partial/failed file is described as verified in the final result.

## 5. Recommended next proof order

1. Define `WellFormedStack bound`, prove transitions preserve it from the initial `E_n` stack; then formalize an *inverse* prefix decomposition of a step on `prefix ++ suffix` when `prefix ≠ []`.
2. Prove a first-visit decomposition of entire runs (with strict nonemptiness of the active prefix before the visit), carefully allowing suffix consumption **after** the visit.
3. Prove the invariant preserving the last floor/ceiling closing marker until it is popped.
4. Deduce the converse direction of Recognition Lemma C.1 by induction on i and the exact first-visit lemma; then prove the lemma's arbitrary-stack assertion from the verified opening-prefix invariant.
5. Prove complete-subtree exchange using complete Recognition and the existing `Distributions` and syntactic-congruence theorems.
6. Prove the branch synchronization lemma with separate weight-comparison and distinct bottom-marker cases.
7. Prove path congruence by well-founded induction on `x.length + y.length`; verify a strict decrease in each branch.
8. Derive unconditional `ClarkEyraud (Language n)`, and only then eliminate the hypothesis of `languageMinus_typed_of_CE`.

Still outside scope even if the above succeeds: reconstruction algorithm `Rec_h`, actual characteristic-sample existence, Corollary 6.4's arbitrary SSBNF lower bound, or the entirety of the TCS manuscript.

## 6. Verdict

**C — foundational partial success.** Parser determinism, reverse partial injection, weight decrease, no nonempty cycle, CFG-to-parser direction, opening prefix, and distribution congruence are fully machine verified, for all applicable finite words and heights. First-visit factorization, full recognition, subtree exchange, branch synchronization, path congruence and the two final targets remain unproved. Do not classify this phase as completion of Appendix C or Proposition 6.3(i).
