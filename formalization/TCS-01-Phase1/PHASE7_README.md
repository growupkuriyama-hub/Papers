# Phase 7 — Conservative Gold learner and syntactic convergence

**Mathematical source: VERIFIED.** [Run 39079689703](https://github.com/growupkuriyama-hub/Papers/actions/runs/39079689703), job `117533933589`, proof-code commit `e5256bdf086f4b3ac7e10cf3d85ce0b6fc996d11`. Full Lean 4.24.0 / Mathlib v4.24.0 direct compilation and kernel axiom audit succeeded, including the new four Phase 7 Lean files, all nine Phase 6 files, and all 49 inherited Phase 1–5B files. `lake build` completed (7448 jobs).

## Inheritance and source

- Repo: growupkuriyama-hub/Papers; new branch: `formalization/tcs-phase7-gold-convergence-20261018`.
- Created **only after** the Phase 6 final proof-and-report HEAD `da6cdc7c0e601d967069d582b120979a3beea010` succeeded in [run 39077871376](https://github.com/growupkuriyama-hub/Papers/actions/runs/39077871376), job `117528675709`.
- TCS manuscript: `01_fixed-h-cfg/main.tex`, `PAPER.yaml` internal `v227`; target `cor:ilt`.
- `TCSPhase7Texts.lean`: `PositiveText Alphabet L` (all inputs in L, every L-word occurs) and cumulative finite sample `observed T n := (Finset.range n).image T`, including finite-witness eventual observation from enumeration.
- `TCSPhase7Learner.lean`: `Hypothesis.initial` and `Hypothesis.reconstructed K` distinguish the empty no-start-production finite grammar from `TCSPhase5.makeRecGrammar h K`. The language semantics of the actual finite reconstructed production sets are linked via `finite_rec_language_iff`. The `Nat.rec` learner conservatively retains the current hypothesis if the newest datum is generated; otherwise it uses **the entire sample** `observed T (n+1)`.
- `TCSPhase7Convergence.lean`: characteristic sample stage, exact rebuild, stability of grammatical snapshots, no-rebuild case from text coverage, at-most-one later rebuild/change and Gold identification.
- `TCSPhase7Main.lean`: direct kernel axiom audit of the main theorems.
- `.github/workflows/tcs-phase7-lean.yml`: `lake build`, direct compilation with `.olean` outputs in dependency order for all new modules, inherited module regression, forbidden proof-command and `sorryAx` scans.

## Stage convention and chief conclusion

At zero-based input index `n`, the hypothesis changes from `learner n` to `learner (n+1)`; `observed T n` contains precisely inputs of indices less than `n`. A `RebuildAt n` is an event **at output stage n+1**. The post-characteristic theorem requires `n₀ ≤ n+1`, including output stage `n₀` itself.

Under a positive text for the SSBNF target `GrammarLanguage G` and `hSub : TypedSubstitutable h (GrammarLanguage G)`:

```lean
TCSPhase7.gold_identification G h T hSub :
  ∃ N : Nat,
    (∀ n : Nat, N ≤ n → learner h T.data n = learner h T.data N) ∧
    hypothesisLanguage h (learner h T.data N) = GrammarLanguage G
```

The equality is of actual hypothesis **snapshots**; consequently their finite CFG objects, obtained by `hypothesisGrammar`, are also identical. The at-most-one lemmas distinguish rebuild events from real syntactic changes. A text may enumerate `{[]}`; empty targets have no everywhere-positive texts.

**Exclusions:** no polynomial-time learner/update proof, CFG membership time analysis, arbitrary normalization, polynomial data bounds beyond inherited Phase 6, or shortlex tie-breaking. All protected paper and Phase 1–6 theorem files remain unchanged. See `PHASE7_VERIFICATION_REPORT.md` for the exact statements and CI audit.

The source-proof run above is successful. A separate workflow run checks this documentation closing commit at its own final HEAD; that result is independently confirmed after the commit.
