# v86 F3 integration audit

Branch: mcfg-v86-f3-type-indexed-integration
Draft PR: https://github.com/growupkuriyama-hub/Papers/pull/55
Base: mcfg-v85-ic-theorem-absorption.

## Mathematical change
The earlier semilattice-indexed abelian-coset theorem is replaced by the type-indexed theorem, allowing an arbitrary coset offset determined by the fixed finite-monoid type h(w). This is an upper bound for characteristic positive-data total length relative to original rule thickness. It assumes a reduced good bounded-rank MCFG presentation. It does not assert that arbitrary intersections with nonregular abelian filters are MCFLs.

The proof uses (i) at most |M|^2 distinct quotient-offset differences, (ii) a minimum-derivation-height induction bounding minimum-norm coset representatives, (iii) regular-fiber Parikh semilinearity, (iv) the nonnegative integer small-solution bound of Papadimitriou (1981), and (v) the existing relaxed distributional witnesses proposition. Short representatives are existential, not efficiently computable.

## Corollaries retained
- thm:mcfg-semilattice-twisted-polydata
- thm:mcfg-abelian-filter-data
- cor:mcfg-one-marker-split-polydata

All remain in EN and JP versions. Prior v85 source is preserved on its own branch.

## Prior work
Yoshinaka (2009/2011/2015) establishes multidimensional positive-data learning and the associated general framework. Parikh (1966) gives semilinearity; Papadimitriou (1981) gives the integer-programming small-solution theorem. Searches did not locate a theorem with this exact uniform finite-type-indexed original-thickness characteristic-data bound. The search is not exhaustive, so absolute novelty and priority are not certified. The claim of novelty is limited to this bound and its finite-difference-coset argument, not to the existing learning model or underlying algebraic methods.

## Outstanding checks
- Latest GitHub Actions EN/JP compile logs and PDF inspection.
- Mathematical review of the D-closure height induction and semilinear small-solution instantiation.
- External expert prior-art check and author signoff.
- PAPER.yaml hash synchronization after final text modifications.

This remains an unmerged draft PR.