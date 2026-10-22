# MCFG #2 v85 — Yoshinaka (2015) qualitative reconstruction reorganization

Status: **editorial/mathematical integration candidate**, not independently
certified or submitted. Canonical main source remains v84 until bilingual
validation and merge; parent commit is
\`0b81b1fdb64d867cd6ed6d43a94ef7967cc349e7\`.

## Scope

Make the *known* bounded-arity positive-data learning principle explicit as
a specialization of Yoshinaka (2015), while reserving original claims
for the *total encoded length* of positive characteristic data and
related higher-rank/algebraic results.

Primary source:
Ryo Yoshinaka, **General Perspective on Distributionally Learnable
Classes**, MoL 2015, Theorem 1, Assumptions 1–3, Lemma 3 and Section 7.
https://aclanthology.org/W15-2308.pdf

## Changes in EN and JP

1. Move the detailed typed signature
   \`sec:general-framework\`, signature-context lemma
   \`lem:signature-contexts\`, class identification
   \`prop:yoshinaka2015-embedding\`, and concrete
   \`lem:substp\` **from the last appendix to Section 3 immediately
   after the reconstruction operator definition**.
2. State new \`cor:yoshinaka2015-qualitative\`, deriving fixed-rank
   qualitative identification, characteristic-set *existence* and
   polynomial-time updates using Yoshinaka's Theorem 1 / Section 7.
   Note that Yoshinaka's main proof describes SUBST_D, whereas
   Section 7 explicitly allows SUBST_P under Assumptions 1, 2 and 7.
   For our signature, Assumption 3 supplies the stronger required
   enumerability; productive trimmed target symbols have both a
   substructure and a successful context.
3. Retain \`lem:substp\` with its **direct finite-sample proof**
   of language equality between the Yoshinaka substructure grammar
   and the actual \`B_{f,h}^{<=r}\` implementation. This bridge is
   essential; a general learnability citation does not by itself
   establish algorithm equality.
4. Replace the separate \`prop:yoshinaka-type-guard\` proof
   re-checking the earlier 2011 grammar with a short cited
   explanation; its statement duplicated \`lem:substp\`.
5. Explain \`prop:reconstruction-soundness\` as the
   substructure-indexed Yoshinaka substitution invariant while
   retaining the explicit induction needed for arbitrary-rank
   hypotheses.
6. Compress \`prop:completeness\` to Yoshinaka's rule-witness
   argument **plus the concrete Link/Const/Comp and uncapped-rank
   handling**. The particular finite witness set
   \`Wit(tilde G_0)\` is still constructed: later length bounds
   rely on it and do not follow from Yoshinaka (2015).
7. Move the source's 'Characteristic witness correspondence'
   after the concrete witness-cardinality proposition.
8. Rewrite the Abstract/Section 3 lead to attribute qualitative
   learnability to Yoshinaka (2015), with quantitative length
   as the distinctive contribution.
9. Retain the full \`thm:exact-reconstruction\` including
   **unbounded rule rank**, since Assumption 2 of a *single*
   bounded-arity signature cannot prove that variant directly.
10. All original main quantitative theorems, the M6 v84
    normalization proof, three abelian/group/LG appendices,
    and historic source branches are unchanged.

## Important reviewer caveats

- Do **not** claim the total characteristic-word length
  is bounded by Yoshinaka's cardinality theorem.
- Do **not** infer unbounded rule-rank identification from one
  application of Assumption 2.
- Do **not** confuse the context-indexed SUBST_D proof with
  the substructure-indexed SUBST_P construction; Section 7 and
  the direct finite-sample equivalence lemma are both required.
- The newly positioned signature verification is a specific
  author proof and should still be independently reviewed.
- This is a restructuring of attribution and proof flow,
  not a new mathematical improvement to the O(||G||² theta)
  and O(||G||³ theta) theorems.
- The exact page delta is to be determined by bilingual PDF build.

## Validated bilingual proof-layout build

The **final revision on PR #67** (commit
\`122a3641b0bf3f13bd06d6a5d0d493756264099e\`)
passed bilingual, cross-reference and artifact-upload checks in
GitHub Actions run **39848545315**:

https://github.com/growupkuriyama-hub/Papers/actions/runs/39848545315

- English PDF **51 pages** (same as v84);
- Japanese PDF **54 pages** (one fewer than v84);
- Both built without LaTeX errors or overfull hboxes;
- Two mild English underfull hboxes remain.
- Publication to main is a separate GitHub Actions workflow
  triggered by the PR merge; verify the fixed URLs independently.

The point of the reorganization is to improve attribution and
mathematical exposition; it is **not** a claim of a 4–7-page reduction.
Full rendered-page visual inspection and independent proof
certification remain open.

## Release gates

- EN and JP LaTeX compilation and cross-reference validation;
- No duplicate or missing labels in main and three appendices;
- Compare rendered PDFs before/after and inspect mathematics;
- Merge into main after checks; update PDF fixed paths;
- Independent author review before I&C submission.
