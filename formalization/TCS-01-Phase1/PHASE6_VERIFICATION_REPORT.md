# Phase 6 — Verification report (active, commit-matched audit)

**Review state:** IN PROGRESS. No unconditional Phase 6 result should be described as kernel-verified before the *final HEAD's* dedicated CI succeeds. This report records the exact checks and will be updated with their definitive results.

## Inputs and immutable baseline

- TCS original paper: `01_fixed-h-cfg/main.tex`, current `PAPER.yaml` internal **v227**; original proof labels `lem:typed-thickness-bound` and `cor:typed-thickness-data`. Read `main.tex` lines 1039–1110; original blob `6bef291fc39cef7c4bcb42bdb9ee055cc9608966`.
- Source base commit `417529d221c7ff73e0622373479e88d68ea00335` (Phase 5B verified proof tree plus handoff).
- Baseline regression [39038218785](https://github.com/growupkuriyama-hub/Papers/actions/runs/39038218785): SUCCESS, job `117412239721`, Lean 4.24.0, Mathlib v4.24.0.
- Branch: `formalization/tcs-phase6-typed-witness-bounds-20261017`; current/final HEAD **to be filled after CI**.
- No inherited theorem statement changed, and **no** paper, `PAPER.yaml`, translation, reviewer response, PDF, arXiv, or Editorial Manager action was requested or undertaken.

## Intended exact Lean theorem statements

New `TCSPhase6.typedThickness G h` is the supremum of the finite set of actual chosen retained typed-yield lengths together with `1`.

- `one_le_typedThickness`: `1 ≤ typedThickness G h`.
- `chosenYield_length_le_typedThickness`: retained `(A,μ)` implies `(chosenYield G h A μ).length ≤ typedThickness G h`.
- `chosenContext_is_shortest`: all actual `TypedContext G h A μ u v` have total length at least the chosen context.
- `context_compression_bound`: `ContextCompressionBound G h`, with `chosenContext` length at most `((finiteTypedRefinement G h).symbols.card - 1) * typedThickness G h` for each retained symbol.
- `typed_symbols_card_le`: typed retained symbol count at most `Fintype.card NT * Fintype.card M`.
- `typed_terminal_card_le`: actual refined terminal-rule count at most `G.terminalRules.card`.
- `typed_binary_card_le`: actual refined binary-rule count at most `G.binaryRules.card * Fintype.card M ^ 2`.
- `positive_witnesses_card_le`: bound by `N*m + |Pter| + |Pbin|*m^2 + 1`, using images and subadditive unions, not disjointness.
- `canonical_witness_length_bound`: every element of the **unchanged** `PositiveWitnesses G h` has length at most `(Nt+1)*tau`.
- `canonical_witness_encoded_size_bound`: for actual `encodedSize W := ∑ w ∈ W, w.length+1`,
```text
encodedSize (PositiveWitnesses G h)
 ≤ (Fintype.card NT * Fintype.card M
     + G.terminalRules.card + G.binaryRules.card * Fintype.card M ^ 2 + 1)
   * ((Fintype.card NT * Fintype.card M + 1) * typedThickness G h + 1)
```
- `polynomial_characteristic_data`: existential witness `W = PositiveWitnesses G h` with existing `TCSPhase1.Characteristic (RecLanguage h) (GrammarLanguage G) W` and the above size inequality, assuming only the same fixed-`h` substitutability premise as Phase 5B.
- Boundary cases: type-cardinality zero, language empty and epsilon-only, and Nat truncated subtraction are handled by proving cardinal positivity **only when a retained symbol exists**. In the epsilon-only case the singleton empty-witness family remains of size at most 1.

## Verification status / CI evidence

**Status is preliminary until final SHA is audited.** Early partial CI `39044122784` was **SUCCESS** for the thickness-only source (`8ac1857187ff81e2835af8198bf9cdae09cc3fc1`). Additional interim runs detected *actual* compiler errors in successor modules; these failed runs do **not** establish verification. Some independent subtheorems of the typed-rule cardinality proof printed only `propext`, `Classical.choice`, and `Quot.sound` in interim build logs; final verdict must come from the final full CI.

Outstanding CI URL / job ID / final SHA: **PENDING**.
Outstanding mathematical/Lean issue: the productive context predecessor inductive case split and integration of the context-count and witness-length inequalities. No mathematical counterexample has been verified. Conditional lemmas `witness_word_length_le_of_context_bound`, `encoded_size_le_of_context_bound`, and `quantitative_characteristic_sample_of_context_bound` **do not** by themselves discharge `ContextCompressionBound`. The separate `context_compression_bound` must kernel-compile for the unconditional target.

## Audit and acceptance controls

The direct compilation and entire inherited 49-module regression, plus `lake build`, are required. `#print axioms` must show only the normal Lean kernel axioms where applicable; source check must reject `sorry`, `admit`, `axiom`, `opaque`, and output logs must reject `sorryAx`. **A failed compilation generates temporary `sorryAx`-reported declarations; none can count as successful evidence.**

Compare final new branch against immutable baseline with `compare_commits` and verify the diff is *restricted* to new Phase 6 Lean source files, the two Phase 6 reports, and `.github/workflows/tcs-phase6-lean.yml`. Keep `main` untouched. Report shortlex tie-breaking as separately unverified even if the numerical bound is completely proved.

**Provisional grade: E (final CI not yet complete).** Update to A only when *all* explicit bounds, characteristic result and the final HEAD's CI are successful; otherwise distinguish B, C, D or E honestly.
