# #8 — PAC_n fixed-h distributional learning

**Title:** *PAC_n Learning under Fixed Finite-Monoid Distributional Typing*  
**Status:** exploratory working draft  
**Source of truth:** `main.tex`

## Current theorem package

- Typed-box obstruction: `VC_{d+1} <= |h(Sigma^+)| <= |M|`, strengthened for `d>=2` to `VC_{d+1}^{d-1} <= |h(Sigma^+)|`.
- Fan-out-one sharpness: the `VC_2` bound is attained by an explicit family of finite regular fixed-`h` substitutable languages.
- PAC consequence: combine finite higher-arity VC dimension with Chernikov–Towsner's proper `PAC_k` theorem, with probability-space/model assumptions stated explicitly.
- Higher-arity sharpness: the root exponent is attained on a prime-power family of observer sizes by explicit finite regular `(d,h)`-tuple-substitutable targets.
- Fixed-observer separation: the two-element observer from #1 has uniformly bounded `VC_2 <= 2` in the incidence model while exact set-driven characteristic exposure has an exponential lower bound.
- Current research tasks: exact arbitrary-size spectrum, effective grammar-valued PAC reconstruction, and explicit quantitative PAC sample bounds.

## Relation to the project

This note links the fixed-observer CFG/MCFG program (#1/#2) to the Kuriyama–Takeuchi `PAC_n` line and modern higher-arity VC/packing theory. It remains separate from the degree-critical manuscripts until the theorem package stabilizes.
