# MCFG #2 v84 — concentrated M6 thickness-transfer proof hardening

Date: 2026-10-22
Working source: \`main\`, \`02_fixed-h-mcfg/main.tex\`
Japanese cross-review source: \`02_fixed-h-mcfg/japanese/main_JP.tex\`
Status: **pre-submission working manuscript; not externally certified**.

## Reason

Claude's focused review of M6 in v83 argues that the structural good-form
normalization of a **reduced lambda-free MCFG** (possibly with deleting rules)
preserves nonterminal thickness up to nonincrease:

\`t_G <= t_Gin\`,

and hence transfers the polynomial rule-thickness bound. The former v83 proof
was a sketch and did not explicitly explain how fully omitted children were
reinstated, or why nonmerging establishes a direct image rather than a
set of preimages.

## Applied corrections (EN and JP)

1. Replaced the proof of \`prop:structural-good-thickness\` with a
   derivation-level account of each operation:
   - Projection \`pi_I\` in the (f3) nondeleting conversion;
   - Permutation of tuple components;
   - Triviality of empty-component splitting for lambda-free source;
   - Merge of consecutive components in Yoshinaka's construction;
   - Final trimming.
2. Established \`L_{A^I} = pi_I(L_A)\` using induction **both ways**.
   For the converse, every omitted child must be productive;
   that uses the **reduced** assumption on the source grammar.
3. Established the merge-language **image equality**
   \`L_{A^mu} = mu(L_A)\`; does not use a false inverse-image
   uniqueness property because the merge map is not injective.
4. Derived \`t_G <= t_Gin\` explicitly, then the fixed-parameter
   size estimate and \`theta_G <= 2||G||max(1,t_G)\`.
5. Clarified Kanazawa (2019) §2.1 as an **existence** claim, not
   an external source for an unquoted size/thickness bound; clarified
   use of Seki et al. (1991) (f3) and Yoshinaka (2011) Lemma 1.
6. Restated the lambda-free input-presentation corollary of
   \`thm:boundary-polydata\` as
   \`O_{f,r,k,l,s,Sigma}(||G_in||^3 max(1,t_Gin))\`.
7. Applied parallel edits to English and Japanese source. All theorem
   labels and the quantitative main theorem are retained.

## Explicitly NOT adopted

- No speculative exact formula \`2^(2f-1) f!\` for total encoding size;
  the encoding model and total grammar overhead require an
  independent detailed count. The paper retains
  \`O_{f,r_max}(||G_in||)\`.
- No change of the factor 2 in \`lem:thickness-equivalence\`;
  its existing inequality is adequate and does not depend on an
  unverified sharpened coding convention.
- No assertion that general non-lambda-free normalization preserves
  thickness. \`prop:empty-component-blowup\` remains in the paper.
- No change to the ring of results for reduced good input grammars,
  the group/abelian/LG appendices, or the previously parked
  separation results.

## Submission gates remaining

1. Bilingual LaTeX compile, reference validation and PDF publish.
2. Visual review of all pages and spacing/labels.
3. Independent mathematical/primary-source audit of the explicit
   projection, merging and quantified good-normalization facts.
4. Cross-check Papadimitriou and Davenport bounds if separately required.
5. Author signoff and later I&C submission.

The uploaded Claude M6 concentrated referee report is an audit input,
not a peer-reviewed certificate. Its finite random testing does not
replace the derivational argument.

## Source snapshots

- English: https://github.com/growupkuriyama-hub/Papers/blob/main/02_fixed-h-mcfg/main.tex
- Japanese: https://github.com/growupkuriyama-hub/Papers/blob/main/02_fixed-h-mcfg/japanese/main_JP.tex
- Previous v83 revision report:
  \`revision/v83_claude_review_corrections.md\`
