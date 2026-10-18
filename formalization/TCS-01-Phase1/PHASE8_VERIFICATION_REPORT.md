# Phase 8 — Verification status (ongoing; not a claim of completion)

**Status: IN PROGRESS.** A theorem is accepted only after the corresponding commit's dedicated GitHub Actions direct Lean compilation, axiom audit, and final HEAD success. Phase 7 is complete and must remain unchanged.

## Scope and provenance

- Manuscript: `01_fixed-h-cfg/main.tex`, `thm:poly-build`, `PAPER.yaml` **v227**.
- Phase 7 immutable baseline SHA: `295d0f7d2142e60c832c6a10cb457eabebcf6d76`.
- Baseline CI: [39080411807](https://github.com/growupkuriyama-hub/Papers/actions/runs/39080411807), job `117536025642`, success.
- Phase 8 branch: `formalization/tcs-phase8-rec-poly-build-20261018`.
- Lean 4.24.0 / Mathlib v4.24.0.

## Intended exact statements and implementation audits

### Occurrences

`mem_splits_iff`: `(u,v) ∈ splits w ↔ w = u ++ v`.

`mem_occurrencesIn_iff`: `(u,x,v) ∈ occurrencesIn w ↔ x ≠ [] ∧ w = u ++ x ++ v`.

`mem_enumerateOccurrences_iff`: `(u,x,v) ∈ enumerateOccurrences K ↔ x ≠ [] ∧ u ++ x ++ v ∈ K`.

`efficient_observed_factors_eq`: `efficientObservedFactors K = TCSPhase5.ObservedFactors K`.

Here enumeration visits only split boundaries of actual sample words; it never calls `CandidateWords` at runtime. Finset-level deduplication is not yet costed.

### Remaining obligations

1. Actual number of nonempty substring occurrences = sum over words of `m*(m+1)/2`, and explicit O(n_K^2) inequality.
2. Per-start incremental type caching with exactly bounded multiplication/update count and agreement with h, rather than computing h for all factors separately.
3. Binary candidate enumeration, correctness and O(n_K^3) count.
4. Unary construction from one occurrence `(u,x,v)` and one sample word `w=u++y++v`; extraction of unique `y`, direct-context and monoid-type equality, reverse completeness; O(n_K^3) count.
5. Lexical/start/epsilon productions and all six fields of literal grammar equality `buildRecGrammar ... = makeRecGrammar ...`.
6. Executable data structure for duplicate elimination and a linked cost semantics for substring processing, comparison, typing, candidate insertion, output, and an O(n_K^4) operation bound.
7. Audit of final HEAD, `lake build`, direct new-module and inherited regression compilation, forbidden-token and `sorryAx` scan, `#print axioms` standard logical axioms only.

Even an executable collection equality, if achieved, does not by itself establish the paper's O(n^4) machine-cost claim. Any runtime polynomial statement must account for the concrete data structures.

## Results

CI and kernel status to be filled **only** from final action logs. No new Phase 8 theorem is asserted as successfully verified in this preliminary report. Protected Phase 1–7 sources and manuscript are not edited.