# Phase 6 — Typed thickness and quantitative characteristic data

Paper: *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing* (TCS-D-26-00494).

- Protected source of truth: `01_fixed-h-cfg/main.tex` (main `PAPER.yaml`: **internal v227**, checked 2026-10-18 JST; corresponding manuscript labels `lem:typed-thickness-bound`, `cor:typed-thickness-data`).
- Immutable inherited baseline: `417529d221c7ff73e0622373479e88d68ea00335`, Phase 5B handoff. Its CI **SUCCESS**: [39038218785](https://github.com/growupkuriyama-hub/Papers/actions/runs/39038218785), job `117412239721`.
- Isolated working branch: `formalization/tcs-phase6-typed-witness-bounds-20261017`. **Do not merge to main.**
- Toolchain: Lean 4.24.0 / Mathlib v4.24.0, unchanged.
- Original Phase 1–5B declarations and witnesses are reused without modifying a single previous source.

## Verification modules

| File | Mathematical content |
|---|---|
| `TCSPhase6Thickness.lean` | Finset supremum of `chosenYield` lengths and `1`, minimum thickness and yield bound |
| `TCSPhase6Contexts.lean` | Derives `chosenYield_is_shortest` and `chosenContext_is_shortest` from the existing `Nat.find` choices |
| `TCSPhase6DependencyPaths.lean` | A successful `TypedContext` yields a productive typed dependency walk |
| `TCSPhase6ContextCompression.lean` | Minimum-context descent, finite rank of strictly cheaper typed symbols, bound by `(Nt-1)*tau` |
| `TCSPhase6RuleCounts.lean` | Finite symbol/product cardinality, unique typed terminal copy, binary copy bound via two child types, witness-cardinal bound from `Finset.image`/`union` |
| `TCSPhase6WitnessLengths.lean` | Four witness families and length bound; `ContextCompressionBound` is an explicit bridge proposition that `TCSPhase6ContextCompression` must establish, not an axiom |
| `TCSPhase6EncodedSize.lean` | Actual `Finset.sum (fun w => w.length + 1)` and manuscript-size bound |
| `TCSPhase6CharacteristicData.lean` | Combines bound with existing Phase 5B characteristic proof |
| `TCSPhase6Main.lean` | Top-level **unconditional** theorem targets, requiring the completed context compression theorem |

Numerical target, with `N=Fintype.card NT`, `m=Fintype.card M`, `Nt=(finiteTypedRefinement G h).symbols.card`, `tau=typedThickness G h`:

```text
chosen context length ≤ (Nt - 1) * tau
∀ w ∈ PositiveWitnesses G h, w.length ≤ (Nt + 1) * tau
Nt ≤ N * m
typed terminal rules ≤ G.terminalRules.card
typed binary rules ≤ G.binaryRules.card * m^2
encodedSize (PositiveWitnesses G h)
  ≤ (N*m + |Pter| + |Pbin|*m^2 + 1) * ((N*m+1)*tau + 1)
```

Empty and epsilon-only grammars require no retained-node assumption. For a *retained* node `Nt ≥ 1` is proved before using subtraction. The witness family is a **set**; duplicates are not counted more than once.

## Canonicality and mathematical method

Phase 5B choices are minimum **length**, and remain not necessarily the literal manuscript's shortlex tie-breaking among equal-length candidates. Phase 6 proves bounds for the **same already-existing** `PositiveWitnesses G h`, not for a redefined set.

Rather than assume a graph-diameter estimate, context compression uses a strict descent in the minimum terminal-context cost to a productive parent in a genuine binary production. The finite rank is the number of retained typed symbols with strictly shorter chosen contexts. Each descent lowers this rank, and adds at most one canonical sibling yield of length `tau`. Thus the bound is a direct consequence of finiteness, *once the formal Lean proof compiles*.

## CI contract

Dedicated [workflow](../../.github/workflows/tcs-phase6-lean.yml) `tcs-phase6-lean.yml`: `lake build`, direct compilation of all new modules in dependency order, direct checking of all inherited modules, printed axioms, and forbidden-token / `sorryAx` scans. The authoritative machine-verification state belongs to [PHASE6_VERIFICATION_REPORT.md](PHASE6_VERIFICATION_REPORT.md), updated to match the final commit.

No paper, `PAPER.yaml`, Japanese text, reviewer response, PDF, arXiv or journal submission is modified.
