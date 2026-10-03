# #8 — PAC_n fixed-h distributional learning

**Title:** *PAC_n and Higher-Arity VC Geometry under Fixed Finite-Monoid Distributional Typing*  
**Status:** exploratory working draft  
**Source of truth:** `main.tex`

## Current theorem package

- Typed-box obstruction: `VC_{d+1} <= |h(Sigma^+)| <= |M|`, strengthened for `d>=2` to `VC_{d+1}^{d-1} <= |h(Sigma^+)|`.
- Rectangular product capacity `rpc_r(h)`: a sharper observer-algebra invariant with `VC_{d+1} <= rpc_{d-1}(h)`, monotone under typing refinement.
- Same-cardinality observer separation: for image size `q^2`, a finite-field observer supports `VC_4 >= q`, while a left-zero-band observer forces `VC_4 <= 1`.
- Fan-out-one sharpness: the `VC_2` bound is attained by an explicit family of finite regular fixed-`h` substitutable languages.
- PAC direction audit: Takeuchi 2020 refutes the old full-slice necessity direction `PAC_2 => finite VC_2`. Chernikov–Towsner 2025 Theorem 6.5 proves the opposite direction `finite VC_k => proper PAC_k` from packing, independently of that disputed necessity claim. This sufficiency direction is used here; the reverse/equivalence and the 2015 sample lower bound are quarantined.
- Higher-arity sharpness: the root exponent is attained on a prime-power family of observer sizes by explicit finite regular `(d,h)`-tuple-substitutable targets.
- Arbitrary observer budgets: the optimum is `Theta_d(T^{1/(d-1)})`, via monoid padding of the finite-field construction.
- Fixed-observer separation: the two-element observer from #1 has `VC_2 <= 2`, hence proper `PAC_2` learnability via Chernikov–Towsner Theorem 6.5, while exact set-driven characteristic exposure has an exponential lower bound.
- Current research tasks: exact arbitrary-size spectrum, reconciliation of the disputed PAC necessity direction, effective grammar-valued PAC reconstruction, and quantitative upper sample bounds.

## Relation to the project

This note links the fixed-observer CFG/MCFG program (#1/#2) to the Kuriyama–Takeuchi `PAC_n` line and modern higher-arity VC/packing theory. It remains separate from the degree-critical manuscripts until the theorem package stabilizes.
