# #1 — fixed-h CFG

**Title:** Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing  
**Journal:** Theoretical Computer Science  
**Manuscript ID:** TCS-D-26-00494

## Current working baseline

- `main.tex` — English major-revision manuscript, internal v91; this is the source of truth.
- `japanese/main_JP.tex` — Japanese reference translation synchronized to the current v91 English source on 2026-10-04; section structure, labels, theorem environments, citations, and previously missing material were audited against `main.tex`.
- `response/response_round1.tex` — Round-1 Response to Reviewers, synchronized with the current revision; final PDF page/line locators remain to be regenerated after freeze.

## Historical baseline

- `archive/tcs-round1-arxiv-v4/main.tex` — exact historical source for the first TCS submission; this is also the arXiv v4 manuscript baseline.
- SHA-256 of that historical source: `fcdcff7fc09140e7f3e83982d6cd57fa297f30ece0bc607f7f7859bb91c71b0d`.

The historical file is preserved as an immutable archival baseline and should not be edited in place.

## v91 Order-dependence compression

The standalone paragraph on presentation-order dependence in Section 4.2 was replaced with a brief continuation of the learner description. Both language versions and reviewer notes are synchronized; the underlying argument is unchanged.

## v90 Reviewer 1 terminology and redundancy preflight

The v90 preflight defines RNF and letter-count notation, expands SGL and the initial acceptance-set notation, and specifies short-word prefix/suffix conventions. Three trivial numbered statements, an unused syntactic-class symbol and an unused macro are removed; the center-marker example uses $P$ throughout. Substantive theorem claims and proofs are unchanged, but numbering shifts downstream of the removed statements. The Japanese reference translation and reviewer responses have been synchronized. The archived Lean v88 baseline does not separately certify v90 as an exact artifact.

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

- The current theorem-facing public archive is `tcs1-v88-formalization-3.0.0`, archived on Zenodo at DOI `10.5281/zenodo.23120560`. The preceding v87 release remains available at DOI `10.5281/zenodo.23114558`, and the immutable historical v79 release remains available at DOI `10.5281/zenodo.22939434`.
- The v83 development remains the completed mathematical proof layer; v86 and v87 were synchronized against that theorem surface by their exact-version audit modules and coverage reports.
- The archived v88 theorem-facing source is synchronized by `V88FullManuscriptAudit.lean` and `FORMALIZATION_TCS1_V88.md`. The current v89 working manuscript is a preflight/presentation revision: it moves the canonical-yield definition before first use, moves the parity motivation into the main text, compresses the unnumbered Section 10.1 comparison, and clarifies the $\rho=1$ endpoint. No numbered theorem/proposition/lemma/corollary statement was added or removed in this preflight, so no separate v89 Lean archive has been minted; v88 remains the theorem-facing verification baseline.
- The v88 Lean delta verifies the endpoint-complete Section 10.1 center-marker language $P=\{a^ncb^n:n\ge0\}$, prefix/suffix freeness, substitutability of $L_\times=PdP$, its $(0,0)$ fixed-window membership, exact semantics of the displayed CFG $S\to XdX$, $X\to aXb\mid c$, the erasing image onto $\Delta\Delta$, and an internal pumping proof that $L_\times$ is nonlinear. The later parity-typing footnote is covered by the existing yield-typing invariant.
- The archived v88 verification source is fixed by GitHub release `tcs1-v88-formalization-3.0.0` at commit `0c917ba836ff830feeac9dcd31a91e6569afe8c7`. The exact archival commit passed the theorem-facing critical path, full `TCS1.All`, no-`sorry`, and no-project-axiom gates before publication.

The manuscript proofs remain self-contained; the Lean development is a reproducibility and verification artifact, not a substitute for the paper proofs.


## v89 preflight note

The v89 manuscript/response pass resolves the round-2 precheck issues around forward use of $\omega$, keeps the yield-typing motivation in the main text, compresses the unnumbered $L_\times$ comparison, and marks response-letter page/line locators for regeneration from the final frozen PDF. Appendix D is unchanged because the occurrence-recognition and replay-admissibility arguments were already explicit in v88.
