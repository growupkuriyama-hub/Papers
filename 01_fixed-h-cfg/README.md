# #1 — fixed-h CFG

**Title:** Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing  
**Journal:** Theoretical Computer Science  
**Manuscript ID:** TCS-D-26-00494

## Current working baseline

- `main.tex` — English major-revision manuscript, internal v83; this is the source of truth.
- `japanese/main_JP.tex` — Japanese reference version; synchronization with the current English manuscript is pending.
- `response/response_round1.tex` — Round-1 Response to Reviewers, synchronized with the current revision.

## Historical baseline

- `archive/tcs-round1-arxiv-v4/main.tex` — exact historical source for the first TCS submission; this is also the arXiv v4 manuscript baseline.
- SHA-256 of that historical source: `fcdcff7fc09140e7f3e83982d6cd57fa297f30ece0bc607f7f7859bb91c71b0d`.

The historical file is preserved as an immutable archival baseline and should not be edited in place.

## Formalization

The theorem-facing Lean 4 formalization is maintained separately in
`growupkuriyama-hub/tcs1-lean-formalization`.

- The immutable historical release is `tcs1-v79-formalization-1.0.0`, archived on Zenodo at DOI `10.5281/zenodo.22939434`.
- The v83 theorem-facing re-verification has been completed and merged into the formalization repository's `main` branch.
- The v83 audit covers the revised fibre restriction, typed-thickness and fixed-window bounds, the level-coded Appendix argument, the compact `R_n,R_n^-` grammars, reducedness, ordinary-thickness bounds, and the exponential characteristic-sample lower-bound package.
- The integration checkpoint passed the repository CI gates, including full `TCS1.All`, no-`sorry`, and no-project-axiom checks.

The manuscript proofs remain self-contained; the Lean development is a reproducibility and verification artifact, not a substitute for the paper proofs.
