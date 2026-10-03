# #8 — PAC_n fixed-h distributional learning

**Title:** *PAC_n Learning under Fixed Finite-Monoid Distributional Typing*  
**Status:** exploratory working draft  
**Source of truth:** `main.tex`

## Current theorem package

- Typed-box obstruction: `VC_{d+1} <= |h(Sigma^+)| <= |M|` for incidence relations induced by `(f,h)`-tuple-substitutable languages.
- Fan-out-one sharpness: the `VC_2` bound is attained by an explicit family of finite regular fixed-`h` substitutable languages.
- PAC consequence: combine finite higher-arity VC dimension with Chernikov–Towsner's proper `PAC_k` theorem, with probability-space/model assumptions stated explicitly.
- Current research tasks: higher-fan-out sharpness, effective grammar-valued PAC reconstruction, and exact-vs-statistical separation.

## Relation to the project

This note links the fixed-observer CFG/MCFG program (#1/#2) to the Kuriyama–Takeuchi `PAC_n` line and modern higher-arity VC/packing theory. It remains separate from the degree-critical manuscripts until the theorem package stabilizes.
