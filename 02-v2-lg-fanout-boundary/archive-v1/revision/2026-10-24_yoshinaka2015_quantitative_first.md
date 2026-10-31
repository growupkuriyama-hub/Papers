# MCFG #2 — Quantitative-first restructuring (2026-10-24)

Status: **implemented in the canonical English and Japanese TeX files**; I&C submission still requires author review and mathematical cross-checking.

## Editorial objective

The contribution of this paper is the **quantitative analysis of total encoded positive characteristic-data length**, not a rediscovery of qualitative MCFG learning. State existing qualitative results by specializing Yoshinaka (2015), and minimize the preliminary section without losing the mathematical dependencies required by the new length bounds.

Primary source: Ryo Yoshinaka, *General Perspective on Distributionally Learnable Classes*, MoL 2015, Sections 6–8, Theorem 1, Lemmas 2–3 (https://aclanthology.org/W15-2308/).

## Changes to both canonical manuscripts

- Section 3 now introduces the concrete observed-tuple operator, **immediately specializes Yoshinaka's signature**, and proves only the finite-sort/class-identification bridge and language equivalence with \`SUBST_P\`.
- Added \`cor:yoshinaka2015-qualitative\`: fixed-rank qualitative identification and polynomial updates are stated as inherited, not novel.
- The standard soundness/complete-rule simulation and Gold convergence arguments were compressed and explicitly attributed to the existing framework.
- Retained \`prop:completeness\` for **arbitrary same-type witness representatives**, including representatives not derived from their assigned nonterminal; this is necessary for later quantitative shortening.
- Retained \`thm:exact-reconstruction\` for capped and **uncapped rule rank**, because Yoshinaka's fixed-arity Assumption 2 does not itself imply the uncapped result.
- The auxiliary proofs of \`prop:output-invariants\`, \`lem:semigroup-transfer\`, \`lem:identity-canonical-contexts\`, and \`lem:typed-homogeneity\` were relocated from the pre-quantitative exposition to \`app:typed-witness-aux-proofs\` in the appendix. Their statements and numbered labels remain in place.
- Explicitly distinguished Yoshinaka's \`SUBST_D\` proof from Section 7's \`SUBST_P\` statement under Assumptions 1, 2 and 7. The actual capped \`B_{f,s}\` implementation remains linked by \`lem:substp\`.
- All pre-existing quantitative theorems, constructive witness bounds and lower-bound analyses were retained.

## Future editorial guardrails

1. **Do not restore the full general qualitative soundness/completeness/Gold re-proofs** merely to make the article self-contained. The general principle is cited.
2. **Do not remove** the concrete \`SUBST_P\` correspondence or the explicit witness transfer without proving a replacement: those are the interfaces needed to analyze the concrete finite sample and its total length.
3. **Do not infer total length from cardinality**; Yoshinaka (2015) bounds the number of characteristic words for \`SUBST_D\`, not their total encoded length.
4. **Do not apply the fixed-rank theorem uniformly to unbounded rank**; the uncapped extension needs the separate concrete finite-witness argument.
5. Keep English \`main.tex\` and Japanese \`japanese/main_JP.tex\` synchronized in statements and references. Treat the English file as the submission source.
6. Before I&C submission, review all dependencies, verify the Yoshinaka (2015) Assumption 7 specialization carefully, and inspect rebuilt PDFs and cross-references.

## Build and validation

The first structural rewrite (before moving four auxiliary proofs) passed the GitHub Actions bilingual build:
- English: 46 pages before -> **45** after.
- Japanese: 59 pages before -> **58** after.
- Compiling finished successfully with standard nonfatal font warnings.

The final auxiliary-proof relocation and Section 7 note require a later current-head build. Static checks on both revised source files showed no duplicate labels, unresolved internal \`\\ref\` targets, or imbalanced theorem/proof environments.
