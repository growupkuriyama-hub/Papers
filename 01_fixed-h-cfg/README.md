# #1 — fixed-h CFG

## Always-latest English and Japanese PDFs (automatic)

- **English clean manuscript (GitHub viewer):** [TCS-D-26-00494_Manuscript_Clean.pdf](https://github.com/growupkuriyama-hub/Papers/blob/main/01_fixed-h-cfg/TCS-D-26-00494_Manuscript_Clean.pdf)
- **Japanese reference translation (GitHub viewer):** [main_JP.pdf](https://github.com/growupkuriyama-hub/Papers/blob/main/01_fixed-h-cfg/japanese/main_JP.pdf)
- **Direct English PDF:** https://raw.githubusercontent.com/growupkuriyama-hub/Papers/main/01_fixed-h-cfg/TCS-D-26-00494_Manuscript_Clean.pdf
- **Direct Japanese PDF:** https://raw.githubusercontent.com/growupkuriyama-hub/Papers/main/01_fixed-h-cfg/japanese/main_JP.pdf
- English source: `main.tex`, byte-identical to `TCS-D-26-00494_Manuscript_Clean.tex`.
- Japanese source: `japanese/main_JP.tex`, a reference translation; mathematical/source synchronization remains an editorial responsibility.
- The `publish-tcs1-clean-pdf.yml` workflow automatically recompiles **both** PDFs (pdfLaTeX for English, LuaLaTeX for Japanese) and updates these tracked PDFs on `main` whenever either English or Japanese source is changed. URLs stay stable; PDF content updates after the workflow succeeds.
- The journal submission uses the English manuscript; the Japanese PDF is a reading/reference translation.

## v149 — 2026-10-10 remove redundant Japanese completion sentence

- In `japanese/main_JP.tex`, deleted the explicit `uxv in Delta^* => a^q x b^(q+beta(x)) in Delta^*` sentence just after the canonical-completion definition. The concise interpretation as realizable entry heights and its boundary-replacement justification remain.
- English explanation was already concise and is unchanged; English canonical and Clean TeX remain byte-identical. Seven examples, star/star-star identities, nonlinear proof and reviewer response unchanged. Japanese SHA256 and baseline version refreshed.
- PDF build and marked reviewer-response page/line locator checks remain pending before TCS resubmission.

## v148 — 2026-10-10 remove unused entry-height recursion

- Removed the displayed one-letter recurrence for `Q(lambda)`, `Q(xa)`, and `Q(xb)` and the immediately following explanation from both English and Japanese. After the canonical-completion definition and seven examples, the text now directly presents the concatenation identity (star-star).
- Kept the complete star-star formula and its separate boundary-condition explanation, the star membership criterion, all seven examples, and the nonlinear substitutability and fixed-window proofs unchanged.
- English canonical/clean TeX are byte-identical, JP reference synchronized, SHA256 metadata updated. Reviewer response unchanged; PDF build and marked-response locators need a final check before TCS resubmission.

## v147 — 2026-10-10 canonical-completion definition of admissible entry heights

- Changed the definition of `Q(x)` in English and Japanese directly to `{q in Z_{>=0}: q+beta(x)>=0 and a^q x b^(q+beta(x)) in Delta^*}`.
- Removed the duplicate "more precisely, iff" exposition. Retained a short proof that these are exactly the entry heights of contextual occurrences; the substitutability proof cites this characterization instead of the former definition.
- Kept the seven examples, one-letter recurrence, (star) membership criterion, (star-star) concatenation identity, theorem and fixed-window separation intact. English canonical and Clean TeX match, JP reference synced, SHA256 updated, reviewer response unchanged; final PDFs and marked reviewer-response locators still require verification.

## v146 — 2026-10-10 direct admissible entry-height definition

- Redefined `Q(x)` directly as the set of realized heights `beta(u)` over contexts `uxv in Delta^*`. Canonical completion `a^q x b^(q+beta(x))` gives a concrete witness without auxiliary `Occ_ba`, `eta`, or prefix-minimum notation.
- Added the one-letter recursions for `Q(lambda)`, `Q(xa)`, and `Q(xb)`, and retained the seven examples, membership criterion (star), and concatenation identity (star-star). The substitutability proof explicitly treats the case `x=rbat` and uses the same formal two-step concatenation argument.
- Updated both English and Japanese TeX and verified English main equals Clean TeX; refreshed SHA256 metadata. All numbered claims and fixed-window witness unchanged. Round-1 reviewer response unchanged. PDF builds and final marked-PDF locators must be checked before resubmission.

## v145 — 2026-10-10 seven admissible entry-height examples

- Expanded the `Q(x)` examples immediately before the membership criterion in both EN and JP: `ab, aa, lambda` give `Z_{>=0}`, `bb` gives `Z_{>=2}`, `ba` gives `{1}`, `bbaa` gives `{2}`, and `baaba` gives the empty set.
- Checked all seven against the defining prefix-minimum and `ba`-occurrence conditions. No mathematical theorem, formula, or proof was changed. English main and Clean TeX remain byte-identical, Japanese synced, EN/JP checksums refreshed; reviewer response unchanged. Verify PDF builds and marked response line locators before journal resubmission.

## v144 — 2026-10-10 algebraic concatenation proof for nonlinear Delta-star example

- Define the named concepts height, `ba` occurrence set, and admissible entry-height set `Q(x)` for every word (including the empty word). Preserve `Q(ab)=Z_{>=0}` and `Q(ba)={1}`.
- Criterion (star) now expresses whole-word `Delta^*` membership as `beta(w)=0` and `0 in Q(w)`; identity (star-star) explicitly computes `Q(st)` from `Q(s)`, `Q(t)`, `beta(s)`, and the boundary letters. The substitutability proof uses this identity twice instead of prose tracking of two boundaries.
- EN `main.tex` and clean TeX mirror are identical, JP reference synchronized, hashes updated, all numbered results and fixed-window witnesses retained. Review response unchanged. PDF builds and marked-PDF line locators require checking; journal revision not submitted.

## v143 — 2026-10-10 height and entry-height clarification for nonlinear example

- In the nonlinear `Delta^*` example, explicitly define the height at a prefix `p` as `beta(p)` before using height terminology; an occurrence `w=ubav` of `ba` has height `beta(ub)`.
- Define `Occ_ba(x)` by the factorization `x=ubav`, put `eta_x((u,v))=beta(ub)`, name `Q(x)` the admissible entry-height set, and add `Q(ab)=Z_{>=0}` versus `Q(ba)={1}`. Statement (star-star) is specifically about conditions *within x*, not membership of the whole word `uxv` in `Delta^*`. The proof cites this scoped statement.
- English source and Clean mirror identical; Japanese synchronized and SHA-256 metadata updated. Mathematical proposition and Round-1 reviewer response unchanged. Recompile both PDFs and re-audit marked-PDF response page/line locators before resubmission.

## v142 — 2026-10-10 regular-filter proof of the nonregular linear example

- The main proof of `prop:linear-separator-example` now derives a fixed finite typing from the Clark--Eyraud substitutable linear language `L_all` intersected with regular `Q`, using Proposition 3.2(ii) and the linear regular-intersection closure. Linearity, nonregularity, and separation from Clark--Eyraud and all fixed-window classes are retained.
- The four-element `h_{pm,e}` is retained in a short, unnumbered paragraph after the proof with a concise verification. No theorem numbering is changed; the former long direct proof and membership equation are removed.
- English canonical and Clean TeX are identical, Japanese reference matches the new organization, and R2.3 reviewer-response wording is synchronized. All three SHA-256 metadata fields updated. Recompile PDFs and audit page/line locators before TCS resubmission; not yet submitted.

## v141 — 2026-10-10 direct enumeration proof for polynomial-time reconstruction

- Replaced the proof of `thm:poly-build` in English and Japanese with direct enumeration. Rule (U) pairs each observed nonempty factor occurrence `(u,x,v)` with every sample word `w`; when `w=uyv` with nonempty `y` and the `h`-values agree, emit `[x] -> [y]`.
- Removed buckets, tries and identifier sorting from the proof, and used no displayed equations. The bounds remain `O(n_K^3)` rule candidates and `O(n_K^4)` explicit construction. Japanese proof matches the user's supplied TeX; English source and Clean TeX are byte-identical.
- Reviewer response unchanged. Verify PDF workflows and re-audit response page/line references against the final marked PDF before TCS resubmission; journal resubmission not performed.

## v140 — 2026-10-10 formal reconstruction-complexity proof

- Theorem `thm:poly-build` now defines the observed occurrence set `O_K`, the prefix-extended `h`-value cache `H_w(i,j)`, context/type buckets `B_{u,v,mu}`, and the nonempty-bucket index set `I_K`. The bucket sum is explicitly indexed; each EN/JP proof has just one display.
- Rule (B)/(U) enumeration stays `O(n_K^3)` and full explicit reconstruction remains `O(n_K^4)`. English canonical source, Clean TeX mirror, Japanese reference, and SHA-256 metadata are synchronized. The referee response is unchanged.
- **Pre-resubmission:** verify PDF builds and re-audit all response references against the final marked PDF; no journal resubmission has been performed.

## v139 — 2026-10-10 short-word idempotent explanation in footnote

- Added brief English and Japanese footnotes to the locally trivial positive-image argument, explaining why short-word types in `h_{k,l}(Sigma+)` cannot be idempotent: a large enough positive power is encoded as a distinct long-word type.
- The surrounding proof text, theorem statements and reviewer response were left unchanged; `main.tex`, Clean TeX, and the Japanese reference TeX are synchronized, with SHA-256 metadata refreshed.
- **Before TCS resubmission:** verify rebuilt PDFs and the marked-PDF page/line locators. No journal resubmission has occurred.

## v138 — 2026-10-10 explicit short-word bound in the fixed-window product

- In the proof constructing $M_{k,\ell}$, English and Japanese manuscript text now states that the short-word factors satisfy $|x|,|y|<m_0$, where $m_0=\max\{1,k+\ell\}$; the case $|w|=m_0$ remains in the long-word tag.
- Synchronized canonical `main.tex`, Clean TeX mirror, Japanese reference TeX, and source SHA-256 metadata. The theorem and proof argument, as well as the existing reviewer response, are unchanged.
- **Before TCS resubmission:** check PDF builds and re-audit response page/line references against the final marked PDF. No journal resubmission has been made.

## v137 — 2026-10-10 explicit universal idempotent quantifier

- English and Japanese proofs of the locally trivial typing/fixed-window criterion now explicitly state the identity for **all `e,f` in `E(S)`** and all middle elements of `S`, following Pin (2025, Proposition XI.4.17).
- `main.tex`, the canonical Clean TeX mirror, the Japanese reference manuscript, and `PAPER.yaml` SHA-256 metadata are synchronized. No theorem or proof argument changed; reviewer-response text is unchanged.
- **Pre-resubmission:** rebuild the clean/marked/JP PDFs and re-audit response page/line locators against the final marked PDF. No journal resubmission performed.

## v136 — 2026-10-10 fixed-h fiber attribution in Yoshinaka framework

- The EN/JP Introduction explicitly attributes nonempty fibers `h^{-1}(m) ∩ Σ+` to the **finite-monoid homomorphism fixed in this paper**, represented as sorts within Yoshinaka (2015)'s general signature framework.
- Synchronized the response overview, R1.3 and R2.1; clean TeX mirror and SHA-256 metadata updated, including repair of a previously stale response checksum. No theorem or proof was changed.
- **Before journal resubmission:** rebuild/review the clean, marked, Japanese, and response PDFs, then re-audit marked-PDF page/line locators. No journal resubmission has been made.

## v135 — 2026-10-09 concise Yoshinaka comparison and L0 placement

- Section 3 now states only Yoshinaka (2008, Proposition 1)'s regular-intersection and erasing-inverse-image nonclosure, his nonerasing inverse-image closure, and the contrast with Proposition 3.2 under a changed finite typing.
- Moved the regular counterexample's **inline definition** `L0=ae*ce*a ∪ ae*de*a ∪ be*ce*b` to Section 9.2, where it is first used for the regular counter separation comparison.
- Synchronized English, Japanese, canonical Clean TeX, Round-1 referee replies R1.34/R2.1, and SHA-256 metadata; no theorem or proof changed.
- **Pre-resubmission:** rebuild clean/marked/JP/response PDFs and re-audit all response page/line locators against the v135 marked manuscript. No journal resubmission has been made.

## v134 — 2026-10-09 minimal typing example in the Introduction

- Added the concise example `L={a,aa}` immediately after the fixed-`h` definition in Section 1.1 in English and Japanese. Trivial typing fails due to overlapping but unequal distributions; the parity morphism separates the factors.
- No early introduction of substring-grammar inference rules and no claim of a new separation from fixed-window classes.
- Synchronized Round-1 reviewer answers R1.5 and R2.1, the English clean TeX mirror, and `PAPER.yaml` hashes. No theorem or proof changed.
- Before journal resubmission, rebuild clean, marked, Japanese and response PDFs and check response page/line references against the new marked PDF. No journal submission has been made.

## v133 — 2026-10-09 Yoshinaka comparison before Proposition 3.2

- Moved the existing Yoshinaka (2008, Proposition 1) paragraph and known regular language `L0` directly before Proposition 3.2 in English and Japanese.
- The transition distinguishes regular-filter and erasing-inverse-image closure under **refinement of finite typing** from nonclosure of an unchanged fixed-window or fixed-`h` class.
- Updated Round-1 referee responses R1.34 and R2.1; the clean TeX mirror remains identical to canonical `main.tex`. No theorem/proof was changed.
- Updated `PAPER.yaml` SHA-256 checksums and metadata. Before TCS resubmission, rebuild English clean/marked, Japanese, and referee-response PDFs and re-audit marked-PDF page/line locators: the v132 25-page/971-line audit is historical. No journal resubmission has been made.

## v132 — 2026-10-09 final R1 pre-submission source sync

- Corrected the 2014 preprint title to *Learning Algorithm for Relation-Substitutable Context-Free Languages* and the Coste--Garet--Nicolas (2012) title to *Locally Substitutable Languages for Enhanced Inductive Leaps*; synchronized English and Japanese citations.
- Aligned the 49 editor/reviewer response locators with the freshly compiled **25-page** additions-only marked PDF (margin lines 1--971), including corrected locations for Proposition 5.2, Theorem 5.6, Proposition 8.4, and Lemma 9.6. Removed obsolete 24-page/929-line notice.
- Added marked-only `\\AtBeginDocument{\\sloppy}` in `response/latexdiff_compat.tex` to eliminate marked-up overfull boxes without altering the clean or Japanese manuscript typography.
- Local builds: English clean 24 pages, marked 25 pages, Japanese 28 pages, response 14 pages; all compiled. The first-submission source remains unchanged in `archive/tcs-round1-arxiv-v4/`.
- `TCS-D-26-00494_Manuscript_Clean.tex` mirrors canonical `main.tex` exactly. This is a working **unsubmitted** revision; journal upload must be performed separately.


## 2026-10-09 — R1 prior-art and response synchronization (working draft)

- Updated \`main.tex\`, \`japanese/main_JP.tex\`, and \`response/response_round1.tex\` with the 2014 Kuriyama preprint chronology, the general many-sorted signature perspective of Yoshinaka (2015), and explicit distinctions between qualitative learner existence and finite-monoid-specific quantitative/algebraic results.
- Added citations for Clark--Yoshinaka (2016), Coste--Garet--Nicolas (2012), and Coste--Nicolas (2019), and corrected the response to R2.5 to cite Eilenberg (1974), matching the manuscript.
- These are **working source changes, not an already submitted R1 revision**. The reviewer-response page/line locator table is **stale** after insertion and MUST be regenerated from the final marked PDF. Verify clean and marked PDFs, bibliography and CI before resubmission.
- The 2014 historical draft remains an earlier formulation, not a claim that all its older proofs and polynomial-data assertions were correct.



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

- `main.tex` — English major-revision manuscript, internal v149; this is the source of truth.
- `japanese/main_JP.tex` — Japanese reference translation synchronized to v149.
- `response/response_round1.tex` — Round-1 Response to Reviewers, updated in v142 for R2.3 (unchanged in v143/v144/v145/v146/v147/v148/v149); page/paragraph/line locators require re-audit against the new marked PDF before resubmission.

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
