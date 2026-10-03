# #1 — fixed-h CFG

**Title:** Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing  
**Journal:** Theoretical Computer Science  
**Manuscript ID:** TCS-D-26-00494

## Current working baseline

- `main.tex` — English major-revision manuscript, internal v87; this is the source of truth.
- `japanese/main_JP.tex` — Japanese reference version; the v85 bibliographic source audit is synchronized, while broader synchronization with the English manuscript remains pending.
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

- The immutable historical release is `tcs1-v79-formalization-1.0.0`, archived on Zenodo at DOI `10.5281/zenodo.22939434`.
- The v83 development remains the completed mathematical proof layer; v86 was synchronized against that theorem surface by `V86FullManuscriptAudit.lean` and `FORMALIZATION_TCS1_V86.md`.
- The current v87 source is now exactly synchronized by `V87FullManuscriptAudit.lean` and `FORMALIZATION_TCS1_V87.md`. A direct v86-to-v87 comparison found 34 theorem/proposition/lemma/corollary environments in each version and no changes to any of those environment contents; the v87 edits are proof-exposition clarifications only.
- The v87 synchronization is merged at `cefe7e904fc1e16174761b726008363666fe8b71`. TCS1 Lean CI run #308 passed the theorem-facing critical path, full `TCS1.All`, no-`sorry`, and no-project-axiom gates.

The manuscript proofs remain self-contained; the Lean development is a reproducibility and verification artifact, not a substitute for the paper proofs.
