# TCS Phase 1 — Lean 4 formal verification (v209)

**Canonical paper:** *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*, TCS-D-26-00494. Source: `01_fixed-h-cfg/main.tex`, frozen `main` commit `55c2f818c64ff51aaea3940ebad1c08b655dc4f6` (blob SHA `3d9824996701c768a264c5f2f947f07b93c9e1f4`).

## Reproduce

This standalone project pins Lean v4.24.0 via `lean-toolchain` and Mathlib tag v4.24.0 in `lakefile.lean`.

```sh
cd formalization/TCS-01-Phase1
lake update
lake exe cache get
lake build
lake env lean TCSPhase1.lean
grep -nE '(^|[^[:alnum:]_])(sorry|admit|axiom|opaque)([^[:alnum:]_]|$)' TCSPhase1.lean
```

The final grep is expected to produce no matches. The Lean module itself executes six `#print axioms` directives. CI: [successful GitHub Actions run #38897242015](https://github.com/growupkuriyama-hub/Papers/actions/runs/38897242015), proof commit `db7abdd3f2d3185f52658e76494408604ed68f63`. Output: `Build completed successfully (7352 jobs).`; direct compilation succeeded; no forbidden proof tokens; no `sorryAx`.

## Manuscript-to-formalization mapping

| Lean declaration | Paper statement | Outcome |
|---|---|---|
| `Characteristic` | Main `main.tex` lines 281–294 | S ⊆ L and for all finite K with S ⊆ K ⊆ L, Op K = L. |
| `distinguishing_word` | Proposition 6.3(iv), lines 1212–1217 | Same set-driven Op on L and L\{w}: characteristic samples for both imply every sample for L contains w. |
| `witness_length_plus_two` | Lines 1127–1131 | Constructed terminal-list witness satisfies length + 2 = 3*2^n. |
| `witness_length` | Lines 1127–1131 | Exact length 3*2^n−2. |
| `encodedSize_ge` | Lines 292–294, Proposition 6.3(iii–iv) | Witness membership forces encoded size ≥ 3*2^n−1. |
| `characteristic_exponential_lower_bound` | Proposition 6.3(iv) | Combination of characteristic lemma, genuine word construction, and encoded size bound. |
| `soundness_excludes` | Proposition 6.3(iii), lines 1203–1208 | Soundness *assumed* for punctured target implies omission of the removed witness from Rec K. |

The output of `Op : Finset α → Set α` is the *generated language* of the paper's grammar-valued operator, not a reconstructed grammar itself. This faithfully preserves the set-driven characteristic condition while avoiding any assumption of Op monotonicity or L finiteness.

**Critical scope:** The Lean code does not derive CFG generation of L_n, the fact that its witness is in L_n, Clark–Eyraud substitutability, fixed-typing class membership of L_n^-, correctness/existence of characteristic samples for concrete Rec_h, Theorem 4.2 soundness, Corollary 6.4, or Appendix C. It verifies the abstract distinguishing-pair and quantitative implication, **not all concrete premises** of Proposition 6.3(iv). See `VERIFICATION_REPORT.md`.
