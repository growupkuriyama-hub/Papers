# v86 — restore the genuine fan-out-two separation (EN/JP)

Date: 2026-10-19; status: I&C Draft (not merged or submitted).

## Restored result

- Theorem `thm:arbitrary-filter-separation`: `L_star = {a^n c^(n+1) b^n : n>=0} union {a^n d^(n+1) b^(2n) : n>=0}`.
- Fixed typing `h_star = (h_Sigma^(1,1), g_star)`, where `g_star` detects which of c,d occurs.
- This explicit language has minimum fan-out 2, minimum fan-out-two rule rank 1, and lies in `C_{f,h_star}^{mcf} \ F_f^{arb}` for every f>=2, where `F_f^{arb}` comprises languages expressible as a multidimensionally substitutable language intersected with an arbitrary regular language (and is intersected with f-MCFL).
- Complete short proof restored: rank-one fan-out-two grammar; non-CFL by regular intersection and inverse homomorphic image of the three-count equality language; typed substitutability by strictly-2-local boundary control and branch-specific Parikh differences; non-representability as an untyped substitutable language intersected with regular language, using substitution and the DFA loop on final b-run.
- Required supporting lemma `lem:sl2-boundary-control` restored as a general lemma in the comparison section.
- Aligned the English/Japanese abstracts, Introduction, comparison, Conclusion. No algebraic main theorem or learning-algorithm proof changed.

## Deliberately not restored

- The separate archived theorem `thm:intrinsic-ranktwo-witness`, about a non-CFL minimum-rank-two language, remains in `archive/trim-v83/{en,jp}/typed_separations.tex`.
- Other v83/v85 deletions remain intact. The original v85 review is preserved as branch `mcfg-v85-ic-theorem-absorption` and Draft PR #54.
- No claim that this example proves the open higher-fan-out superpolynomial data lower bound.

## Validation

- [x] Citation keys, theorem references, duplicate LaTeX labels, and begin/end environments cross-checked in each language and retained appendices before PDF build.
- [x] GitHub Actions EN/JP LaTeX build, PDF output and final citation/ref pass (runs 39144550652, 39144550669, 39144550674, 39144550680; all successful).
- [x] EN 40 pages, JP 43 pages; 0 Overfull hboxes and 0 unresolved refs/citations in final logs; relevant theorem/proof pages visually inspected.
- [ ] Author-side independent verification and journal sign-off.

GitHub: `02_fixed-h-mcfg/main.tex`, `japanese/main_JP.tex`; the full archived original theorem remains untouched.
