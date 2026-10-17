# MCFG #2 v71 — Selective-results I&C reduction

Date: 2026-10-17
Branch: `revision/02-v71-selective-results`
Base: v70 main (merged as commit `8de71485799120c963b58b701921e25eb62aede4`)
Status: **manuscript trial; final verification via [PR #33](https://github.com/growupkuriyama-hub/Papers/pull/33)**.

## Editorial decision

Narrow paper #2 around quantitative positive characteristic-data length
for typed MCFGs, and only the structural witnesses needed to establish
that the higher-rank/fan-out setting is meaningful and not reducible
to existing untyped learning or arbitrary regular filtering.

### Results preserved in manuscript

- `lem:boundary-short-canonical`, `thm:boundary-polydata`: main simultaneous multi-component boundary conservation and `O(||G||^3 theta)` characteristic-data bound.
- `thm:window-abelian-polydata` and its two lemmas in `appendix_window_abelian.tex`: separate window-plus-finite-abelian-group extension with `O(||G||^4 theta)` bound.
- `thm:intrinsic-ranktwo-witness`: non-CFL typed target with intrinsic fan-out two and intrinsic rule rank two, including the Gallot citation chain.
- `prop:strong-fanout-separation`: failure at fan-out two for every finite typing despite success at fan-out one.
- `thm:arbitrary-filter-separation`: typed non-CFL rank-one fan-out-two language not obtainable by *any* regular filtering of a Yoshinaka-untyped language.
- `thm:rankone-polydata`, soundness/completeness/identification proofs, full signature correspondence and normalization details, for continuity and auditability.
- `lem:sl2-boundary-control` because two preserved separation proofs need it.

### Results withdrawn from compiled manuscript

1. `prop:fanout-one-lower-bound` and the bracketed doubling appendix: a consequence from companion CFG #1, not a novel MCFG theorem. The manuscript cites #1 instead. The higher-fan-out open problem is preserved and accurately worded.
2. `prop:nonboundary-rankone-separator` and its special DFA/language `J_s`: useful as a standalone example, but less probative than the remaining non-context-free regular-filter theorem.
3. `thm:every-fanout-strictness` / `H_m`: a separate fan-out hierarchy project rather than necessary to establish the paper's quantitative core.
4. `prop:bounded-unknown-typing`: off-scope union-of-typings observation.
5. `rem:copy`: auxiliary folklore counterexample, not used in retained proofs.

The original v70 text of these results, **including the entire bracketed
doubling appendix**, is preserved verbatim in
`revision/v71_retired_results_archive.md`; complete v70 is also
available from the original merge commit. No research result is
claimed to be mathematically disproved merely because it was
removed from the I&C manuscript.

### Presentation repairs

- Abstract, contributions, data-complexity comparison table, and
  conclusion no longer present #1's lower-bound construction as a new
  #2 proposition; cite the companion CFG manuscript for the prior
  operator-independent obstruction.
- Correct dependent cross-references to removed hierarchy/DFA results
  and remove the old `\\input` to the lower-bound appendix.
- Retain local-boundary control lemma needed by both the intrinsic-rank
  example and the arbitrary-regular-filter separation.
- Retain the substantive Yoshinaka 2015 signature appendix for explicit
  prior-art accountability in the first reduction trial.
- Do not invent new theorems, alter the boundary/group estimates, or
  change the journal AI declaration.

## Validation / next gates

- [x] Main TeX and included abelian appendix static checks: no duplicate
  labels, missing cross-references, missing bibitem keys, or unbalanced
  theorem/proof/list environments.
- [x] Removed result text archived in a separate noncompiled Markdown file.
- [ ] Full v71 GitHub Actions PDF build, final page count and layout check;
  use [PR #33](https://github.com/growupkuriyama-hub/Papers/pull/33) for run logs.
- [ ] If too long, consider *individually* compressing the independent
  Yoshinaka-signature appendix and rank-one exposition, without deleting
  dependencies or losing novelty attribution.
- [ ] Independently referee the already-added finite-abelian-group
  theorem; this update does not claim human verification.
- [ ] Confirm factual AI-use disclosure and I&C journal file/metadata
  requirements with the author before submission.

The v71 revision is a scoped manuscript, **not an I&C portal submission**.
