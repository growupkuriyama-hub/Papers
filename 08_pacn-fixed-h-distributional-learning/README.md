# #8 — PAC_n fixed-h distributional learning

**Title:** *PAC_n and Higher-Arity VC Geometry under Fixed Finite-Monoid Distributional Typing*  
**Status:** exploratory working draft  
**Source of truth:** `main.tex`

## Current theorem package

- Typed-box obstruction: `VC_{d+1} <= |h(Sigma^+)| <= |M|`, strengthened for `d>=2` to `VC_{d+1}^{d-1} <= |h(Sigma^+)|`.
- Fan-out-one sharpness: the `VC_2` bound is attained by an explicit family of finite regular fixed-`h` substitutable languages.
- PAC model audit: Takeuchi 2020 gives an old-definition `PAC_2` counterexample to the 2015 necessity claim, while Chernikov–Towsner 2025 again use full slices and claim equivalence. PAC transfer is therefore quarantined until the definitions/assumptions are reconciled.
- Higher-arity sharpness: the root exponent is attained on a prime-power family of observer sizes by explicit finite regular `(d,h)`-tuple-substitutable targets.
- Arbitrary observer budgets: the optimum is `Theta_d(T^{1/(d-1)})`, via monoid padding of the finite-field construction.
- Fixed-observer separation: the two-element observer from #1 has uniformly bounded `VC_2 <= 2` in the incidence model while exact set-driven characteristic exposure has an exponential lower bound. This VC statement is unconditional; any PAC interpretation is conditional on the model audit.
- Current research tasks: exact arbitrary-size spectrum, reconciliation of the 2020/2025 PAC definitions, a repaired higher-arity PAC model, and only then effective/quantitative PAC reconstruction.

## Relation to the project

This note links the fixed-observer CFG/MCFG program (#1/#2) to the Kuriyama–Takeuchi `PAC_n` line and modern higher-arity VC/packing theory. It remains separate from the degree-critical manuscripts until the theorem package stabilizes.
