# #1 — fixed-h CFG

**Title:** Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing  
**Journal:** Theoretical Computer Science  
**Manuscript ID:** TCS-D-26-00494

## Current working baseline

- `main.tex` — English major-revision manuscript, internal v103; this is the source of truth.
- `japanese/main_JP.tex` — Japanese reference translation synchronized to the current v103 English source.
- `response/response_round1.tex` — Round-1 Response to Reviewers, synchronized with v103. The substantive responses and a selected old-to-new renumbering guide are current; exact final page/paragraph/line locators still have to be inserted after the manuscript PDF is frozen.

## v103 Literature-grounded quantitative limitation

To reduce review risk, the revision removes the post-submission operator-independent ordinary-thickness lower-bound theorem and its level-coded-tree Appendix D. Section 6 now keeps only the direct source-to-typed thickness gap needed for the paper's reconstruction analysis, and explicitly positions the representation-sensitivity issue against Clark--Eyraud (2007), Yoshinaka (2008), and Eyraud--Heinz--Yoshinaka (2016). The abstract, contribution summary, conclusion, Japanese reference translation, and reviewer response are synchronized. The manuscript now has three technical appendices (A--C) and 30 numbered theorem-like environments. No new theorem claim is introduced by this pass.

## v101 Reviewer-response audit

The manuscript sources remain at the v100 mathematical/expository state. The v101 project pass revises the English Round-1 response letter: newly added material is mapped explicitly to the reviewer comments that motivated it; Section 6.2 and Appendix D are acknowledged as genuinely new lower-bound material; R2.1 now corrects the reading that a separate morphism is required for each target and states instead that one homomorphism h is fixed for the entire slice, exactly as one pair (k,l) is fixed in Yoshinaka's hierarchy; and three claims withdrawn or narrowed from the submitted manuscript are listed near the opening. The old Japanese response memo has been replaced by an archival stub and is not authoritative.

## v100 Section consolidation and final exposition cleanup

The v100 pass folds the former standalone complexity section into Section 5, reducing the main-text section count from 11 to 10 while leaving the four appendices as repositories for displaced technical proofs. It also removes redundant productivity/reachability qualifiers from Appendix A.1, makes the conjunction spacing in $\mathcal E(x)$ explicit, rewrites the ordinary-thickness lower-bound theorem statement as one sentence, removes an abstract-level forward reference to an undefined refinement parameter, and repairs the occurrence-recognition argument in Appendix D by using bracket matching directly rather than an unstated induction hypothesis. English, Japanese, and the reviewer-response numbering are synchronized.

## v99 de la Higuera comparison clarification

The v99 pass corrects the explanatory paragraph after the linear characteristic-data theorem. De la Higuera (1997, Theorem 2) concerns the full representation class of linear grammars. The manuscript now states instead that the present positive result is restricted to the fixed-$h$ substitutable subclass $\mathcal C_h^{\mathrm{lin}}$ and uses the paper's positive-data characteristic-sample notion for $\mathcal B_h$; it therefore makes no polynomial time-and-data claim for the full LIN representation class. The Response to Reviewer 2.3 and the Japanese reference translation are synchronized.

## v98 Source and response audit

The v98 pass aligns the manuscript and response letter with the final source audit before resubmission. It corrects the IPTtD attribution to Yoshinaka (2008), cites Eyraud--Heinz--Yoshinaka (2016) as a later formulation, adds an explicit explanation of why the fixed-$h$ linear result does not contradict de la Higuera's negative result for the full linear-grammar representation class, clarifies the $\rho\ge2$ endpoint, and weakens source claims that had not been directly verified at the required level of specificity. The response letter now matches the actual manuscript: the unsupported bounded-advice paragraph is removed, the Section 10 description is corrected, the reduction in numbered theorem-like environments (86 to 34) is recorded, and a selected renumbering guide is included.

## v97 Metavariable and terminology audit

The v97 pass removes the metavariable collisions identified in the round-2 precheck, including competing uses of $P$, $r$, $N$, $d$, $A_i$, and $Z_i$, and unifies $N_t$. Proof-local labels such as `anchor`, `rule witness`, `residual height`, `difference core`, and `replay-admissible` were removed or replaced by direct descriptions. Appendix D was rewritten with a smaller vocabulary while preserving its mathematical claim. English and Japanese sources were synchronized.

## v96 Data-availability cleanup

The manuscript Data availability statement now says only that no empirical data were used. The Lean/Zenodo archive is no longer mentioned in the manuscript itself; formalization metadata remain project-internal.

## Historical baseline

- `archive/tcs-round1-arxiv-v4/main.tex` — exact historical source for the first TCS submission; this is also the arXiv v4 manuscript baseline.
- SHA-256 of that historical source: `fcdcff7fc09140e7f3e83982d6cd57fa297f30ece0bc607f7f7859bb91c71b0d`.

The historical file is preserved as an immutable archival baseline and should not be edited in place.

## v95 Display-math editorial pass

Reviewed all standalone display equations in the English main manuscript and Japanese reference translation. Converted 22 English and 32 Japanese unnecessary displays to inline math, preserving multi-line grammars, long or structurally important definitions and inequalities, and all numbered/labeled equations. The ordinary-thickness lower-bound theorem has smoother prose around its inline target identities. Claims, equation labels, theorem numbers, bibliography, and proofs are unchanged.

## v94 Explicit shortcut grammar

In the ordinary-thickness lower-bound proof (Section 7), the grammar `R_n^-` now has its complete production list written out, including `S^-`, all `Z_i`, the ordinary `A_i` for `0 <= i < n`, and shortcut-bearing `A_i^-` for `0 <= i <= n`. The follow-up witness argument is self-contained. Both English and Japanese texts are synchronized; theorem claims and numbering are unchanged.

## v93 Typed-thickness exposition

Section 7's exponential source-to-typed thickness gap remark now explicitly explains why the untyped grammar has ordinary thickness 1 and why the type-1 branch must generate words of length 2^n. It links the exponential gap to the failure of polynomial bounds in grammar size and ordinary thickness, while preserving the limitation to full-refinement witnesses. Both language versions are synchronized; the response letter needs no change in numbering or substance.

## v92 SGL motivation inline

In Section 4.2, the footnote illustrating syntactic instability of naive batch rebuilding with the center-marker language was folded into the running prose and joined to the conservative SGL wrapper motivation, retaining the Eyraud--Heinz--Yoshinaka Appendix citation. This removes one footnote in both English and Japanese without changing any theorem, proof, or citation key. The Response to Reviewers remains applicable as written.

## v91 Order-dependence compression

The standalone paragraph on presentation-order dependence in Section 4.2 was replaced with a brief continuation of the learner description. Both language versions and reviewer notes are synchronized; the underlying argument is unchanged.

## v90 Reviewer 1 terminology and redundancy preflight

The v90 preflight defines RNF and letter-count notation, expands SGL and the initial acceptance-set notation, and specifies short-word prefix/suffix conventions. Three trivial numbered statements, an unused syntactic-class symbol and an unused macro are removed; the center-marker example uses $P$ throughout. Substantive theorem claims and proofs are unchanged, but numbering shifts downstream of the removed statements. The Japanese reference translation and reviewer responses have been synchronized. The archived Lean v88 baseline does not separately certify v90 as an exact artifact.

## v85 citation-source audit

The current revision tightens three literature attributions without changing any theorem or proof:

- Kanazawa (1998) is not directly held in the project library. The current manuscript therefore cites the available Kanazawa (1993) CWI Report CS-R9351 for the general positive-data categorial-grammar learning background. The 1996 JoLLI article is not used as a source claim in the current manuscript.
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
- The archived v88 theorem-facing source is synchronized by `V88FullManuscriptAudit.lean` and `FORMALIZATION_TCS1_V88.md`. The current v103 manuscript contains later presentation, notation, source-attribution, and response-consistency revisions; the v103 pass also removes the later operator-independent lower-bound construction. No separate v103 Lean archive has been minted. The v88 archive therefore remains the theorem-facing verification baseline rather than an exact synchronization claim for v98.
- The v88 Lean delta verifies the endpoint-complete Section 10.1 center-marker language $P=\{a^ncb^n:n\ge0\}$, prefix/suffix freeness, substitutability of $L_\times=PdP$, its $(0,0)$ fixed-window membership, exact semantics of the displayed CFG $S\to XdX$, $X\to aXb\mid c$, the erasing image onto $\Delta\Delta$, and an internal pumping proof that $L_\times$ is nonlinear. The later parity-typing footnote is covered by the existing yield-typing invariant.
- The archived v88 verification source is fixed by GitHub release `tcs1-v88-formalization-3.0.0` at commit `0c917ba836ff830feeac9dcd31a91e6569afe8c7`. The exact archival commit passed the theorem-facing critical path, full `TCS1.All`, no-`sorry`, and no-project-axiom gates before publication.

The manuscript proofs remain self-contained; the Lean development is a reproducibility and verification artifact, not a substitute for the paper proofs.


## v89 preflight note

The v89 manuscript/response pass resolves the round-2 precheck issues around forward use of $\omega$, keeps the yield-typing motivation in the main text, compresses the unnumbered $L_\times$ comparison, and marks response-letter page/line locators for regeneration from the final frozen PDF. Appendix D is unchanged because the occurrence-recognition and replay-admissibility arguments were already explicit in v88.
