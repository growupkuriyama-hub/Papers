# #1 — fixed-h CFG

## v117 — Post-v116 source audit (2026-10-07)

- Corrected the explanatory sentence after Theorem 9.2: for $\rho=1$, the proposed distinguishing context $(\uparrow,\lambda)$ fails because $\uparrow s$ itself already violates the cap; the common context is not the issue.
- Rechecked the Wakatsuki--Tomita originals supplied by M. Wakatsuki. The manuscript now cites 1992 p.951 for the stack-symbol thickness parameter and 1993 p.1229 for the later inclusion algorithm's explicit computation/use of those thicknesses.
- Cleaned Section 3.1 notation: $p,q$ are the fixed prefix/suffix windows, $r,s$ the variable interiors, and the compared factors are $prq,psq$. The duplicate local definition of $m_0$ in the fixed-window counterexample criterion was removed.
- Replaced the broad Pin citation by the exact finite-monoid recognition result, Theorem IV.3.21.
- Synchronized the Japanese reference manuscript and Round-1 response. The English source remains 2143 lines and the clean revised PDF remains 24 pages, so the audited response's page/line locator table remains valid.
- Removed stale repository metadata claiming that `archive/pre-wakatsuki-v106/` exists. That temporary snapshot had been intentionally deleted; the first-submission baseline `archive/tcs-round1-arxiv-v4/` remains the historical archive.
- Main theorem statements and the v116 substring-indexed learning construction are unchanged. The Lean v88 archive remains the theorem-facing formalization baseline.
- **No claim is made that v117 has been submitted.**

## v116 — Substring-indexed reconstruction and round-2 preflight (2026-10-07)

- Collapsed the occurrence/context-indexed hypothesis states `[x:u,v]` to one state `[x]` per observed nonempty factor. The old and new batch constructors are language-equivalent for every finite sample; the exact two-way simulation is recorded in `revision/v115_to_v116_context_index_collapse.md`.
- The resulting reconstruction is Clark (2013, Algorithm 1)'s substring-indexed architecture with unary rules filtered by the fixed `h`-type, plus the paper's explicit start/empty-word convention.
- Replaced the old context-sensitive soundness invariant by `[x] =>* w => x ≡_L w and h(w)=h(x)`. The existing canonical witness set still proves completeness without change.
- Tightened the explicit reconstruction bound from `O(n_K^5)` to `O(n_K^4)`.
- Narrowed the parity toy example to the role of yield-type splitting in the present completeness proof; promoted the exponential typed-thickness gap from a remark to a proposition; moved formula-adjacent footnote markers; reduced metavariable collisions and singleton subsection fragmentation.
- Added one sentence explaining the design of the nonregular linear separator: `c` and `d` deliberately share one `h`-value, so the example does not merely encode center-symbol names as types.
- English manuscript, Japanese reference translation, and Round-1 response are synchronized at the theorem/label level. Source-level preflight finds balanced environments/braces, no duplicate labels, and no unresolved internal references. GitHub Actions also passes the English, Japanese, response, and marked-up-revision builds; all four generated PDFs pass basic PDF preflight.
- Final response audit: corrected the stale v115 terminal-rule response to use v116 Rules `(U)` and `(L)`, replaced the overstrong congruence-class wording by the proved soundness invariant, clarified the precise Clark (2013) relationship, corrected the main-text subsection count to 16, and added a complete E.1/R1.1–R1.37/R2.1–R2.11 locator table.
- The archived Lean v88 release remains the theorem-facing verification baseline; v116 is not claimed to be an exact separately formalized artifact.
- **No claim is made that v116 has been submitted.**

## v107 — Source-verified Wakatsuki primary-source positioning (2026-10-05)

- Citation-source improvement only: the Wakatsuki--Tomita originals were directly examined. The later v117 audit refined the exact locators to 1992 p. 951 for the stack-symbol thickness parameter and 1993 p. 1229 for its explicit use in the inclusion algorithm.
- **Model boundary:** the DPDA stack-configuration shortest-accepting-input parameter is historically related, but not identical as a mathematical object, to Yoshinaka's shortest-CFG-yield thickness; this manuscript's *typed* thickness after finite-monoid splitting is separate again.
- Note the distinct **membership/equivalence-query plus representative-sample** assumptions of Tajima--Tomita--Wakatsuki (2000), not a result for positive-text-only characteristic data.
- Main theorems, algorithm, definitions of ordinary/typed thickness, proofs and separation examples are unchanged. EN/JP source edits are synchronized.
- The temporary `archive/pre-wakatsuki-v106/` snapshot mentioned in the original v107 note was later intentionally deleted and is not part of the current repository. **No claim is made that v107 has been submitted.**


**Title:** Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing  
**Journal:** Theoretical Computer Science  
**Manuscript ID:** TCS-D-26-00494

## Current working baseline

- `main.tex` — English major-revision manuscript, internal v117; this is the source of truth.
- `japanese/main_JP.tex` — Japanese reference translation synchronized to the current v117 theorem/label surface.
- `response/response_round1.tex` — Round-1 Response to Reviewers, synchronized with v117 and re-audited against the actual TCS decision letter. The editor-required page/paragraph/line locators remain valid because the v117 English source retains the v116 line count and 24-page pagination.

## v106 Yoshinaka prior-art correction

This pass corrects the positioning of the regular fixed-window separation against Yoshinaka (2008, Proposition 1). Yoshinaka's proof already gives the regular language `L0 = ae*ce*a ∪ ae*de*a ∪ be*ce*b`, which is not `(k,l)`-substitutable for any `k,l`. The abstract, Introduction, contribution summary, Section 3, Section 9.2, Conclusion, Japanese translation, and reviewer response now state this explicitly. Ordinary intersection is also no longer presented as a contrast with the fixed-window hierarchy; the relevant structural differences are regular filtering and erasing inverse homomorphisms. The capped family `CTR_rho` is retained only as the finite-state companion to the uncapped counter obstruction. Two small wording issues were also fixed: the nonempty-fragment convention now points back to Definition 2.1, and the height of a `ba` occurrence is defined grammatically. No theorem statement or learning result is strengthened by this pass.

## v105 Round-2 preflight synchronization

The v105 pass incorporates the final preflight corrections identified after the v104 reviewer-response audit. Proposition 3.1 (regular languages via finite monoids) is moved before its first use, the finite-information closure result is promoted from an unnumbered statement to Proposition 3.2, and the fixed-window correspondence becomes Proposition 3.3. The Yoshinaka (2008) comparison now distinguishes the full `(k,l)`-substitutable class from its context-free subfamily and points to Theorem 9.2 as the manuscript's own regular-filter counterexample. The doubling-family attribution is corrected to Clark--Eyraud Example 2 and Eyraud--Heinz--Yoshinaka Example 2.3, with de la Higuera Theorem 3 described as a related variant. The optional `L_x` comparison is removed, the nonlinear `Delta^*` substitutability proof is made explicit at both factor boundaries, and the pushdown connection is stated as an open direction. The Japanese reference translation and response letter are synchronized with these changes. The revised English manuscript has 31 numbered theorem-like environments and compiles to 22 pages under the current preamble.

## v104 R2.1 structural-closure response

The v104 pass answers Reviewer 2.1 with a low-risk structural consequence of the existing product-typing framework rather than a new large theorem. An unnumbered proposition in Section 3 proves closure of `RS` under intersection and arbitrary inverse homomorphism, and shows that regular filtering preserves context-free fixed-`h` slices after passing to a product typing. This is contrasted explicitly with Yoshinaka (2008, Proposition 1), whose fixed-window hierarchy has counterexamples to closure under regular filtering and arbitrary inverse homomorphism. Section 3 also separates correctness of a typing (it must separate shared-context factors with unequal distributions) from quantitative efficiency (typed-thickness control). The English manuscript, Japanese reference translation, and R2.1 response are synchronized. The proposition is intentionally unnumbered, so downstream theorem numbering remains unchanged and the manuscript still has 30 numbered theorem-like environments.

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
- The archived v88 theorem-facing source is synchronized by `V88FullManuscriptAudit.lean` and `FORMALIZATION_TCS1_V88.md`. The current v116 manuscript contains later presentation, notation, source-attribution, numbering, reconstruction-simplification, and response-consistency revisions; v103 removed the later operator-independent lower-bound construction, v104 added the product-typing closure argument, and v105 numbers that result, tightens the nonlinear boundary proof, and removes the optional `L_x` comparison. No separate v116 Lean archive has been minted. The v88 archive therefore remains the theorem-facing verification baseline rather than an exact synchronization claim for v105.
- The v88 Lean delta verifies the endpoint-complete Section 10.1 center-marker language $P=\{a^ncb^n:n\ge0\}$, prefix/suffix freeness, substitutability of $L_\times=PdP$, its $(0,0)$ fixed-window membership, exact semantics of the displayed CFG $S\to XdX$, $X\to aXb\mid c$, the erasing image onto $\Delta\Delta$, and an internal pumping proof that $L_\times$ is nonlinear. The later parity-typing footnote is covered by the existing yield-typing invariant.
- The archived v88 verification source is fixed by GitHub release `tcs1-v88-formalization-3.0.0` at commit `0c917ba836ff830feeac9dcd31a91e6569afe8c7`. The exact archival commit passed the theorem-facing critical path, full `TCS1.All`, no-`sorry`, and no-project-axiom gates before publication.

The manuscript proofs remain self-contained; the Lean development is a reproducibility and verification artifact, not a substitute for the paper proofs.


## v89 preflight note

The v89 manuscript/response pass resolves the round-2 precheck issues around forward use of $\omega$, keeps the yield-typing motivation in the main text, compresses the unnumbered $L_\times$ comparison, and marks response-letter page/line locators for regeneration from the final frozen PDF. Appendix D is unchanged because the occurrence-recognition and replay-admissibility arguments were already explicit in v88.
