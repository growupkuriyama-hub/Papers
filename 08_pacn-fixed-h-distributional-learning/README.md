# #8 — PAC_n fixed-h distributional learning

**Title:** *PAC_n and Higher-Arity VC Geometry under Fixed Finite-Monoid Distributional Typing*  
**Status:** exploratory working draft  
**Source of truth:** `main.tex`

## Current theorem package

- Typed-box obstruction: `VC_{d+1} <= |h(Sigma^+)| <= |M|`, strengthened for `d>=2` to `VC_{d+1}^{d-1} <= |h(Sigma^+)|`.
- Rectangular product capacity `rpc_r(h)`: a sharper observer-algebra invariant with `VC_{d+1} <= rpc_{d-1}(h)`, monotone under typing refinement.
- Type-level form: `rpc_r` depends only on the finite marked image monoid `(im h, h(Sigma^+))`, hence is effectively computable from finite algebra data.
- Product law: for a full direct-product marked observer, `rpc_r` is supermultiplicative.
- Same-cardinality observer separation: for every `d>=3` and prime power `q>=d+1`, two observers of the same size `q^{d-1}` can have `VC_{d+1}=q` versus `VC_{d+1}<=1`.
- Fan-out-one sharpness: the `VC_2` bound is attained by an explicit family of finite regular fixed-`h` substitutable languages.
- PAC direction audit: Takeuchi 2020 refutes the old full-slice necessity direction `PAC_2 => finite VC_2`. Chernikov–Towsner 2025 Theorem 6.5 proves the opposite direction `finite VC_k => proper PAC_k` from packing, independently of that disputed necessity claim. This sufficiency direction is used here; the reverse/equivalence and the 2015 sample lower bound are quarantined.
- Higher-arity sharpness: the root exponent is attained on a prime-power family of observer sizes by explicit finite regular `(d,h)`-tuple-substitutable targets.
- Arbitrary observer budgets: the optimum is `Theta_d(T^{1/(d-1)})`, via monoid padding of the finite-field construction.
- Cyclic observers: `rpc_r(C_N)=floor(N^{1/r})` when all group elements are nonempty-realizable.
- Boundary-window collapse: for the prefix/suffix observer `h^{k,l}`, `rpc_r=1` whenever `ceil(k/2)+ceil(l/2)<r`; hence small boundary windows force `VC_{d+1}<=1` at sufficiently high tuple arity.
- Fixed-observer separation: the two-element observer from #1 has `VC_2 <= 2`, hence proper `PAC_2` learnability via Chernikov–Towsner Theorem 6.5, while exact set-driven characteristic exposure has an exponential lower bound.
- Architecture-vs-VC separation: under the trivial observer, the ambient CFG and fan-out-two MCFG incidence classes have `VC_2 <= 1` and `VC_3 <= 1`, yet the same `X_{k,r}` targets require `k^r` vs `1+r(k-1)` exact positive examples for the two reconstruction architectures.
- Current research tasks: exact arbitrary-size spectrum, reconciliation of the disputed PAC necessity direction, effective grammar-valued PAC reconstruction, and quantitative upper sample bounds.

## Relation to the project

This note links the fixed-observer CFG/MCFG program (#1/#2) to the Kuriyama–Takeuchi `PAC_n` line and modern higher-arity VC/packing theory. It remains separate from the degree-critical manuscripts until the theorem package stabilizes.
