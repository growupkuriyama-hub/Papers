# Phase 1 verification audit — 2026-10-16

## A. Environment and provenance

- Manuscript: Takayuki Kuriyama, *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing* (TCS-D-26-00494).
- GitHub source `growupkuriyama-hub/Papers`, `01_fixed-h-cfg/main.tex`, internal `v209`. Frozen `main` HEAD: `55c2f818c64ff51aaea3940ebad1c08b655dc4f6`; manuscript blob `3d9824996701c768a264c5f2f947f07b93c9e1f4`. `PAPER.yaml` and `response/response_round1.tex` were also read; none of these protected files was edited.
- Main.tex source locations: lines 281–294 characteristic sample and encoded size; 1108–1131 bracketed construction; 1133–1227 Proposition 6.3.
- Execution on GitHub Actions Ubuntu 24.04, Lean 4.24.0 (commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`), Lake 5.0.0, Mathlib `v4.24.0` resolving to `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.
- Commands: `lake update`; `lake exe cache get`; `lean --version`; `lake --version`; `lake build`; `lake env lean TCSPhase1.lean`; prohibited-token grep.

## B. Verified statements and precise hypotheses

`Characteristic Op L S` abbreviates
`(↑S : Set α) ⊆ L ∧ ∀ K : Finset α, S ⊆ K → (↑K : Set α) ⊆ L → Op K = L`.
This agrees with the manuscript's set-based characteristic sample. The manuscript's grammar-valued reconstruction operator is represented only by its generated language, of type `Finset α → Set α`. The operator's output depends on the finite set alone; no monotonicity, correctness or finiteness property is added.

1. `distinguishing_word`, Proposition 6.3(iv). Assumptions: arbitrary L ⊆ α, w ∈ L, existence of characteristic sample for L \ {w}, and S characteristic for L under the **same** Op. Proves w ∈ S. The arbitrary target need not be finite or context-free. **Compiled.**
2. `witness_length_plus_two` and `witness_length`, main.tex 1127–1131. Constructs genuine list words over five literal terminals; establishes length + 2 = 3·2^n and length = 3·2^n−2 for every n. **Compiled.**
3. `encodedSize_ge`, encoded sample size definition main.tex 292–294. `encodedSize K := K.sum (fun x => x.length + 1)`. If witness n ∈ K, the sum is ≥ 3·2^n−1. **Compiled.**
4. `characteristic_exponential_lower_bound`, Proposition 6.3(iv) quantitative conclusion. From w_n ∈ L, a characteristic sample for L\{w_n}, and S characteristic for L, proves encodedSize S ≥ 3·2^n−1. The concrete proof w_n ∈ L_n has **not** been formalized. **Compiled as a conditional theorem.**
5. `soundness_excludes`, Proposition 6.3(iii) abstract step. Assumes ∀ J ⊆ L\{w}, Rec J ⊆ L\{w}; if K ⊆ L and w ∉ K, then w ∉ Rec K. This is **not** a verification of Theorem 4.2 soundness. **Compiled.**

## C. Machine evidence

[Successful GitHub Actions execution #38897242015](https://github.com/growupkuriyama-hub/Papers/actions/runs/38897242015); job `116960547839`; exact proof commit `db7abdd3f2d3185f52658e76494408604ed68f63`.

```text
Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)
Lake version 5.0.0-src+797c613 (Lean version 4.24.0)
[7351/7352] Built TCSPhase1 (3.7s)
Build completed successfully (7352 jobs).
No forbidden proof tokens found
```

Actual `#print axioms` output (both from `lake build` and direct Lean invocation):

```text
'TCSPhase1.distinguishing_word' depends on axioms: [propext, Classical.choice, Quot.sound]
'TCSPhase1.witness_length_plus_two' depends on axioms: [propext, Quot.sound]
'TCSPhase1.witness_length' depends on axioms: [propext, Quot.sound]
'TCSPhase1.encodedSize_ge' depends on axioms: [propext, Classical.choice, Quot.sound]
'TCSPhase1.characteristic_exponential_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'TCSPhase1.soundness_excludes' depends on axioms: [propext, Quot.sound]
```

**No `sorryAx`, `sorry`, `admit`, user-defined `axiom` or `opaque`.** Axioms listed here are Lean standard logical principles, not newly introduced mathematical assumptions.

Five CI attempts were performed. Run `38895974534` failed before compiling (missing Lake manifest); run `38896145234` identified two absent library-lemma names and one type inference issue; run `38896525803` showed the abstract theorem, word length, and conditional soundness had compiled, with one encoded-size elaboration issue; run `38896933816` diagnosed incorrectly parsed Lean summation syntax in the **formalization**, which was fixed by changing to `K.sum (fun x => x.length + 1)`; run `38897242015` succeeded. These are code errors and do not constitute mathematical counterexamples to the TCS claim.

## D. Unverified concrete premises and Phase 2 tasks

- A CFG formalization of exact G_n derivations and proof that the constructed w_n is in L_n.
- Unique no-square-bracket word for L_n, and faithful construction of L_n^-.
- Clark–Eyraud substitutability of L_n; membership L_n^- ∈ C_{h_U}^{cf} (including Appendix C's parser-related results).
- Existence of characteristic samples for the **actual** Rec_h and proof of Theorem 4.2 soundness.
- All SSBNF grammar-presentation-independent typed-thickness claims of Corollary 6.4, and the full deterministic stack parser.

Phase 1 does not claim lower bounds for Gold convergence stages, runtime or mind changes of arbitrary learners.

## E. Verdict

**A — complete machine-checked success for the specified Phase 1 abstract theorem suite.** All six Lean theorems compile with only standard logical axioms. This does **not** mean all *concrete CFG and class-membership hypotheses* of Proposition 6.3(iv) have been formally discharged. The latter are explicitly reserved for Phase 2.
