# Phase 6 — Final proof and CI verification report

**Mathematical proof status: VERIFIED** on commit `bda98879d4090c070608d478d94d5afcb6d53d6c`, [successful CI 39077209572](https://github.com/growupkuriyama-hub/Papers/actions/runs/39077209572), job **117526739086**. The subsequent report-only HEAD is independently CI-checked before Phase 7 branches from it. This document deliberately records the stable proof-code commit, rather than a self-referential documentation commit hash.

## Source identification and inheritance
- TCS manuscript: `01_fixed-h-cfg/main.tex`, Git blob `6bef291fc39cef7c4bcb42bdb9ee055cc9608966`, `PAPER.yaml` **internal v227** (checked on main, 2026-10-18 JST).
- Theorem labels: `lem:typed-thickness-bound` and `cor:typed-thickness-data`.
- Original preserved Phase 5B base: `417529d221c7ff73e0622373479e88d68ea00335`.
- Working branch: `formalization/tcs-phase6-typed-witness-bounds-20261017`.
- Initial failed run: [39047451947](https://github.com/growupkuriyama-hub/Papers/actions/runs/39047451947), job 117438952113. It compiled all mathematics but failed because a comment contained a banned command token.
- One-line comment-only repair commit: `bda98879d4090c070608d478d94d5afcb6d53d6c`, replacing the detected comment without changing the checker.
- Successful proof-code CI: [39077209572](https://github.com/growupkuriyama-hub/Papers/actions/runs/39077209572), job `117526739086`. The docs-only closing commit must also pass its workflow.
- Lean 4.24.0, Mathlib v4.24.0; `lake build` **7448 jobs**, nine new modules directly checked, 49 prior modules directly checked.

## Kernel-verified numerical results
Let `Nt = (finiteTypedRefinement G h).symbols.card`, `tau = typedThickness G h`,
`N = Fintype.card NT`, `m = Fintype.card M`, `T = G.terminalRules.card`, `B = G.binaryRules.card`.

1. `TCSPhase6.one_le_typedThickness`: `1 ≤ typedThickness G h`. The thickness is the **Finset supremum** of lengths of the actual `chosenYield` over retained symbols, union `{1}`.
2. `TCSPhase6.chosenYield_length_le_typedThickness`: each retained typed symbol's chosen terminal yield has length at most `tau`.
3. `TCSPhase6.context_compression_bound G h : ContextCompressionBound G h`, and `TCSPhase6.canonical_context_length_bound`: for retained `(A,μ)`,
   `(chosenContext G h A μ).1.length + (chosenContext G h A μ).2.length ≤ (Nt - 1) * tau`.
   The proof uses productive `TypedContext` predecessors, a strict rank counting retained symbols with smaller minimum context cost, well-founded descent, and one canonical sibling yield of length at most `tau` per step. The finite rank is bounded by `Nt-1`; no path-diameter bound is postulated.
4. `TCSPhase6.canonical_witness_length_bound`: every `w ∈ PositiveWitnesses G h` has `w.length ≤ (Nt+1)*tau`. Proof analyzes all four original witness families, without changing their definitions.
5. `TCSPhase6.typed_symbols_card_le`: `Nt ≤ N*m`.
6. `TCSPhase6.typed_terminal_card_le`: `(finiteTypedRefinement G h).terminalRules.card ≤ T`.
7. `TCSPhase6.typed_binary_card_le`: `(finiteTypedRefinement G h).binaryRules.card ≤ B*m^2`.
8. `TCSPhase6.positive_witnesses_card_le`: `(PositiveWitnesses G h).card ≤ N*m + T + B*m^2 + 1`. Images and unions are bounded without requiring witness families to be disjoint.
9. `TCSPhase6.canonical_witness_encoded_size_bound`:
```lean
encodedSize (PositiveWitnesses G h) ≤
  (Fintype.card NT * Fintype.card M +
    G.terminalRules.card +
    G.binaryRules.card * Fintype.card M ^ 2 + 1) *
  ((Fintype.card NT * Fintype.card M + 1) *
    typedThickness G h + 1)
```
where `encodedSize W = ∑ w ∈ W, w.length + 1` and duplicate words count only once.
10. `TCSPhase6.polynomial_characteristic_data`: under
`hSub : TypedSubstitutable h (GrammarLanguage G)`,
```lean
∃ W : Finset (List Alphabet),
  W = PositiveWitnesses G h ∧
  TCSPhase1.Characteristic (RecLanguage h) (GrammarLanguage G) W ∧
  encodedSize W ≤
    (Fintype.card NT * Fintype.card M +
      G.terminalRules.card +
      G.binaryRules.card * Fintype.card M ^ 2 + 1) *
    ((Fintype.card NT * Fintype.card M + 1) *
      typedThickness G h + 1)
```
This composes the actual finite `PositiveWitnesses` with the Phase 5B `canonical_witnesses_characteristic` and Phase 5A `RecLanguage`, not a surrogate learner.

## Audit
`#print axioms` for `context_compression_bound`, `canonical_witness_length_bound`, `canonical_witness_encoded_size_bound`, and `polynomial_characteristic_data` in the successful job reported **[propext, Classical.choice, Quot.sound]** only. No `sorryAx`, custom unproven mathematical `axiom`, `sorry`, `admit`, or shortcut `opaque` survived. The source scan and end-of-job audit returned success.

The retained-cardinality-zero and epsilon-only cases are treated by the existing source proof with truncated Nat subtraction guarded by positive retained cardinality. The source construction chooses representatives of **minimum length** but does not formalize the manuscript's **shortlex tie-breaking**; therefore we establish the stated bounds and positive characteristic-data existence for the constructed `PositiveWitnesses`, not equality with the paper's literal shortlex-canonical sample.

Compared with `417529d...`, the recorded change list consists solely of `.github/workflows/tcs-phase6-lean.yml`, the nine `TCSPhase6*.lean` modules, and the two Phase 6 reports. The protected `01_fixed-h-cfg/main.tex`, `PAPER.yaml`, Japanese manuscript, reviewer response, submitted PDF, and inherited Phase 1–5B theorem files remain unmodified. No merge to `main`, arXiv upload, or Editorial Manager action was made.

**Scientific verdict: A — the explicitly formalized Phase 6 numeric bound and quantitative characteristic-data theorem were kernel-checked.** This is not a claim of verification of the entire TCS paper, shortlex literal canonicality, algorithmic time complexity, or general CFG normalization.
