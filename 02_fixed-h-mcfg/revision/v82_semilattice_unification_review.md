# #2 MCFG v82-draft — Semilattice-indexed abelian coset unification

Date: 2026-10-18
Status: DRAFT / NOT MERGED / NOT SUBMITTED
Baseline: v81 on the main branch
Branch: mcfg-v82-semilattice-unification-draft

## Summary of edits

- English: main.tex, Japanese: japanese/main_JP.tex.
- Section "Distributional Representatives and Abelian-Filtered Targets" renamed "Distributional Representatives and Semilattice-Indexed Cosets"; old section label retained.
- Original \`prop:mcfg-relaxed-witnesses\` and proof retained.
- New generic \`lem:mcfg-coset-representative-transfer\`: three explicit premises: joint h/quotient acceptance saturation; quotient-value constancy on each typed non-start symbol; a short **generated** tuple for every realizable quotient value of each untyped nonterminal. Inductive short lattice defects and the fixed-equation small-integer-solution bound yield kappa_G=O(T^{3|Sigma|+1}), where T=(r+1)B+||G||.
- New structural lemmas: \`lem:mcfg-sl-rectangle\`, \`lem:mcfg-sl-height\`, \`lem:mcfg-sl-short-value\`.
- Main \`thm:mcfg-semilattice-twisted-polydata\`: uniform polynomial characteristic length for targets indexed by a fixed semilattice morphism eta refining through h.
- Previous D is now \`corollary\`, keeping the **existing label** \`thm:mcfg-abelian-filter-data\`. It explicitly refers to the nonempty core; epsilon is optional separately.
- One-marker specialization \`cor:mcfg-one-marker-split-polydata\`.
- EN/JP abstracts and conclusions updated.
- PAPER.yaml marks v82-draft and records updated EN/JP SHA-256, leaving inclusion appendices unchanged.
- The existing positive-image local-group theorem and its three input appendices remain unchanged.

## Dependencies and quantitative claim

For fixed Sigma,h,eta,Y,f,r, let T_G=||G|| max(1,theta_G). Then:

  kappa_G <= C T_G^(3|Sigma|+1)
  ||Kdagger||_+ <= C' T_G^(3|Sigma|+2).

Constants are independent of the auxiliary abelian group A, morphism phi, subgroup H, map gamma and accepting h-types Acc.

The potential proof uses:
1. Value function F_A(eta(u))=pi phi(u) for all generated tuples u of nonterminal A.
2. Rectangle cancellation: a joined equality y vee W=y' vee W implies F_B(y)=F_B(y').
3. Height descent: if a rule has at least two occurrences of multivalued children, each such child has strictly smaller maximum semilattice height than the parent.
4. Lexicographically minimal derivations and a rule-budget path charge, yielding Bsharp = r^(max(0,ht(Y)-1)) |Y|(||G||+r|V|t_G).
5. Inductive Parikh lattice-defect generation, semilinearity of fixed regular typing fibers, Papadimitriou 1981's nonnegative small-solution bound and the existing relaxed-distributional-witness proposition.

No finite enumeration is used as proof of a general theorem. No statement about computable short representatives for arbitrary auxiliary groups is made.

## Quality gates

- [x] Prepared synchronized EN/JP mathematical statements and proof structure.
- [x] Retained pre-existing section/theorem labels for external references.
- [x] Updated YAML file checksums and version on the branch.
- [x] Added review-only GitHub Actions workflow; no automatic PDF publication to main.
- [ ] GitHub Actions bilingual full-document LaTeX build passes.
- [ ] EN/JP PDF whole-page human visual review.
- [ ] Independent mathematical review of the rectangle/height/path-charge lemmas after integration.
- [ ] Independent new-novelty/prior-art review.
- [ ] Author approval to merge to main and publish updated PDFs.
- [ ] I&C submission checklist and cover letter, if submitted.

## Notes

The parent v81 paper is a pre-submission working manuscript. This v82 branch is not a journal submission, nor an independently refereed proof certification. Appendix sources are unchanged. The family-level fan-out >=2 superpolynomial-data lower-bound open problem remains open.
