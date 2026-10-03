# #1 — fixed-h CFG

**Title:** Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing  
**Journal:** Theoretical Computer Science  
**Manuscript ID:** TCS-D-26-00494

## Current working baseline

- `main.tex` — English major-revision manuscript, internal v88; this is the source of truth.
- `japanese/main_JP.tex` — Japanese reference translation synchronized to the current v88 English source on 2026-10-03; section structure, labels, theorem environments, citations, and previously missing material were audited against `main.tex`.
- `response/response_round1.tex` — Round-1 Response to Reviewers, synchronized with the current revision.

## Historical baseline

- `archive/tcs-round1-arxiv-v4/main.tex` — exact historical source for the first TCS submission; this is also the arXiv v4 manuscript baseline.
- SHA-256 of that historical source: `fcdcff7fc09140e7f3e83982d6cd57fa297f30ece0bc607f7f7859bb91c71b0d`.

The historical file is preserved as an immutable archival baseline and should not be edited in place.

## v85 citation-source audit

The current revision tightens three literature attributions without changing any theorem or proof:

- Kanazawa (1998) is replaced in the current manuscript by Kanazawa (1996) for the positive-data learnability result for $k$-valued categorial grammars.
- The standard finite-monoid characterization is cited to the directly checked modern source Pin (2025) rather than relying on Eilenberg (1974).
- The thickness attribution to Wakatsuki--Tomita is made through Yoshinaka (2008); the 1993 paper is no longer presented as independently checked support.

The exact first-submission snapshot under `archive/tcs-round1-arxiv-v4/` remains untouched.

## Submission-format preflight

The current manuscript remains on the `article` class while the journal-specific
submission requirement is being confirmed.  Elsevier recommends `elsarticle`
for LaTeX manuscripts, but a template change should be made only if required
for this TCS revision because it changes every page/line locator in the response.

## Formalization

The theorem-facing Lean 4 formalization is maintained separately in
`growupkuriyama-hub/tcs1-lean-formalization`.

- The current public archive is `tcs1-v88-formalization-3.0.0`, archived on Zenodo at DOI `10.5281/zenodo.23120560`. The preceding v87 release remains available at DOI `10.5281/zenodo.23114558`, and the immutable historical v79 release remains available at DOI `10.5281/zenodo.22939434`.
- The v83 development remains the completed mathematical proof layer; v86 and v87 were synchronized against that theorem surface by their exact-version audit modules and coverage reports.
- The current v88 theorem-facing source is synchronized by `V88FullManuscriptAudit.lean` and `FORMALIZATION_TCS1_V88.md`. A direct v87-to-v88 comparison found 34 theorem/proposition/lemma/corollary environments in each version and identical contents.
- The v88 Lean delta verifies the endpoint-complete Section 10.1 center-marker language $P=\{a^ncb^n:n\ge0\}$, prefix/suffix freeness, substitutability of $L_\times=PdP$, its $(0,0)$ fixed-window membership, exact semantics of the displayed CFG $S\to XdX$, $X\to aXb\mid c$, the erasing image onto $\Delta\Delta$, and an internal pumping proof that $L_\times$ is nonlinear. The later parity-typing footnote is covered by the existing yield-typing invariant.
- The archived v88 verification source is fixed by GitHub release `tcs1-v88-formalization-3.0.0` at commit `0c917ba836ff830feeac9dcd31a91e6569afe8c7`. The exact archival commit passed the theorem-facing critical path, full `TCS1.All`, no-`sorry`, and no-project-axiom gates before publication.

The manuscript proofs remain self-contained; the Lean development is a reproducibility and verification artifact, not a substitute for the paper proofs.
