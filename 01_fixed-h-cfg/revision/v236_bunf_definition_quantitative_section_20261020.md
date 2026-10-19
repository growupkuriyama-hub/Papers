# TCS v236 — Move BUNF definition to quantitative Section 6

Date: 2026-10-20. Canonical branch main.

## Author-requested reorganization
- Qualitative Section 5 now contains **no occurrence** of BUNF; it types arbitrary CFG rules `A -> u0 B1 u1 ... Br ur` and proves lifting, rule-witness completeness, exact reconstruction, Gold identification and polynomial-time sample reconstruction independently of any normal form.
- The original **numbered** BUNF definition is relocated to the opening of quantitative Section 6 (Definition 6.1) immediately before typed-thickness estimates, rather than being replaced with an unnumbered or hidden-counter workaround. Its syntax and mathematical meaning are unchanged.
- Only quantitative Sections 6--8 and Appendices A--B impose BUNF when needed for polynomial typed grammar size, witness length, two-child branching or linear-spine arguments.
- No new mathematical result is claimed and no proof content beyond explanatory quantitative section opening has changed.

## Renumbering map
Section 5: Prop 5.2 -> Prop 5.1; Thm 5.3 -> Thm 5.2; Thm 5.4 -> Thm 5.3; Cor 5.5 -> Cor 5.4; Thm 5.6 -> Thm 5.5.
Section 6: new Def 6.1; Lem 6.1 -> Lem 6.2; Cor 6.2 -> Cor 6.3; Prop 6.3 -> Prop 6.4; Cor 6.4 -> Cor 6.5.
Source LaTeX cross-references use unchanged labels, so resolve automatically; reviewer response contains number strings and was explicitly updated. No numbering in other sections changes.

## Validation gate
- `main.tex` and Clean TeX are byte-identical, SHA-256 `2640c590cd2c8853b4484fb44963c1fc12d0d74def79083aaef4e66d7c61c9a1`.
- Same original 58 labels, same environment counts, all local refs resolved; no BUNF mention in Section 5.
- Reviewer response R1.2/R1.5/R1.22, number strings and the 49-item locator table synchronized at source level. The workflow must rebuild PDF and verify all marked manuscript page-margin line anchors before a release is considered verified.
- Japanese versions not synchronized. No journal/arXiv submission.
