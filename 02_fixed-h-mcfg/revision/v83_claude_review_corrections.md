# MCFG #2 v83 — Claude review corrections, lean I&C draft

Date: 2026-10-22. Branch: \`mcfg2-v83-review-corrections\`.
Parent: \`mcfg2-v82-lean-ic-experiment\`.
The separately preserved full v82 branch, \`main\` v81 and TCS #1 frozen R1
have not been edited.

## Accepted and committed

- **M1:** Strengthened \`lem:semigroup-transfer\` in English and Japanese:
  explicit \`f>=1\`, nonempty tuple equality, distinguishing untrimmed
  vs trimmed refinements, equality of typed evaluations on the positive
  semigroup subimage and equality of consistently selected witness words.
- **M9:** Refinement \`def:h-refinement\` contains just the definition.
  Fresh identity preservation of kernel refinements and product typings
  is proved in independent \`lem:fresh-refinement\` in EN/JP.
  Eliminated the duplicated Japanese definition and vacuous heading.
- **M3/M4:** Replaced the overlapping Yoshinaka start sort
  \`O_* = Sigma*\` with an explicitly disjoint tagged copy
  \`{bar(w):w in Sigma*}\`, applied the tags to all nonstart sorts and
  to the promotions/epsilon constant, and changed signature-context
  functions to return the tagged start object. Corrected Lemma 3
  attribution of characteristic cardinality: the numerical bound is
  stated just after that lemma for SUBST_D.
- **M5:** Explicitly quantified good grammar witnesses as
  \`L(G)=L intersect Sigma+\` for the fixed-window theorem, the
  abelian-filtered theorem, and the six bilingual group/abelian/LG
  appendix theorem statements. The necessary \`epsilon\` word is
  included separately in the positive sample. The abelian-filter
  theorem no longer assumes a good grammar generates epsilon.
  Rank-one normalization already has a separate direct-start datum.
- **M2:** Corrected both references in each local-group appendix to
  the frozen #1 TCS R1 **Proposition 6.4/6.4(iv)**.
- **M8/E1:** Disclosed the earlier, differently scoped arXiv:2605.11644
  draft in both Introductions and changed data-availability links to
  this branch rather than old v81 \`main\`. Do not say the earlier
  public arXiv has been updated or withdrawn.
- **E8/E11:** Listed LG alongside both group appendices in the
  effective-characteristic-data proposition and corrected the
  Yoshinaka Example 5 section reference in EN/JP.

## Static source quality checks

English/Japanese both have:
- Matching theorem/definition/lemma-environment counts, including
  the new \`lem:fresh-refinement\`;
- No duplicate LaTeX labels and no missing internal \`ref/eqref\`
  references across main plus all three included math appendices;
- No old Proposition 6.3 references to TCS #1 in the LG appendices.

## Verified branch-only bilingual build

The final mathematical TeX changes were built and validated on
commit \`b6773e1adffe437ef7747d928d6802099dd6c843\`,
GitHub Actions **run 39776717646**:

- English PDF: **50 pages** (lean predecessor 49, full v82 54).
- Japanese PDF: **54 pages** (lean predecessor 53, full v82 59).
- Both compilers, reference-validation script and preview-artifact upload:
  **passed**.
- No overfull boxes; English reported two minor underfull boxes.
- Artifact: \`mcfg2-v82-semigroup-preview\` (historical workflow artifact name)
  from run **39776717646**, ID **12423959424**.
- Build success verifies TeX integrity and final references only.
  It is **not** independent mathematical certification or visual PDF QA.

Build URL:
https://github.com/growupkuriyama-hub/Papers/actions/runs/39776717646

## NOT settled by the review or these edits

1. **M6 / highest mathematical hold:** Independent line-by-line
   validation of Seki et al. (1991) Lemma 2.2(f3), Kanazawa (2019)
   rank-preserving normalization, Yoshinaka (2011) nonmerging
   conversion, and especially
   \`prop:structural-good-thickness\` claiming
   \`t_G<=t_Gin\` and
   \`theta_G=O(||G_in||max{1,t_Gin})\`.
   The text has an argument, but neither Claude's audit nor the
   present update establishes this entire dependency from primary
   sources. Do **not** call this certified.
2. Verify the cited precise forms/numbers of Papadimitriou's integer
   bound and Geroldinger--Halter-Koch's Davenport inequalities.
3. Full Japanese paragraph-by-paragraph mathematical proofreading,
   independent expert proof verification and PDF page-by-page visual
   inspection remain open.
4. **M7, E3--E5:** The rare-types, power-transfer and companion-CFG
   doubling results are parked in
   \`revision/parked_structural_results_EN.tex\` and
   \`revision/parked_structural_results_JP.tex\` in this lean branch.
   They have **not** been silently discarded or claimed as results
   of this submission candidate. The original v82 full draft still
   contains them; their remaining editorial issues would need work
   if they are reincorporated.
5. The source's quantitative-group and LG arguments were reviewed
   by Claude, but finite computational checks are not a proof; these
   results have not received an independent theorem-by-theorem
   formal certification.

**Release gate:** Two-language LaTeX build, reference checks,
proof-dependency checks and author review must pass before the
lean branch can be considered a submission candidate. This record
does not authorize merging or journal submission.
