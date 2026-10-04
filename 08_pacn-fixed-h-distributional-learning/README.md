# #8 — PAC_n fixed-h distributional learning

**Title:** *PAC_n and Higher-Arity VC Geometry under Fixed Finite-Monoid Distributional Typing*  
**Status:** exploratory working draft  
**Source of truth:** `main.tex`

## Current theorem package

- Typed-box obstruction: `VC_{d+1} <= |h(Sigma^+)| <= |M|`, strengthened for `d>=2` to `VC_{d+1}^{d-1} <= |h(Sigma^+)|`.
- Rectangular product capacity `rpc_r(h)`: a sharper observer-algebra invariant with `VC_{d+1} <= rpc_{d-1}(h)`, monotone under typing refinement.
- Type-level form: `rpc_r` depends only on the finite marked image monoid `(im h, h(Sigma^+))`, hence is effectively computable from finite algebra data.
- Kernel invariance/refinement: equal observer kernels give equal `rpc_r`; product typing can only increase capacity.
- Product law: for a full direct-product marked observer, `rpc_r` is supermultiplicative.
- Same-cardinality observer separation: for every `d>=3` and prime power `q>=d+1`, two observers of the same size `q^{d-1}` can have `VC_{d+1}=q` versus `VC_{d+1}<=1`.
- Fan-out-one sharpness: the `VC_2` bound is attained by an explicit family of finite regular fixed-`h` substitutable languages.
- PAC direction audit: Takeuchi 2020 refutes the old full-slice necessity direction `PAC_2 => finite VC_2`. Chernikov–Towsner 2025 Theorem 6.5 proves the opposite direction `finite VC_k => proper PAC_k` from packing, independently of that disputed necessity claim.
- Support-sensitive repaired PAC: on finite/countable product domains, the Takeuchi support restriction extends to every arity `k`; combining finite-support necessity with Chernikov–Towsner sufficiency gives `finite VC_k <=> proper support-PAC_k`. This resolves Takeuchi 2020 Problem 11 in the countable setting and restores the KKT finite-box sample lower bound.
- Repaired PAC lower bounds: the sharp higher-arity families force `N = Omega_d(t_h^{1/(d-1)})` for fixed `(epsilon,delta)`, and the padded construction gives the same order for every sufficiently large observer budget up to constants.
- Higher-arity sharpness: an abstract MDS-type direct-factor system in an abelian observer yields exact `VC_{d+1}=q` at observer size `q^{d-1}`. Extended Vandermonde/finite-field systems instantiate this for prime powers (`q>=d` for `d>=3`; all prime powers for `d=2`).
- Worst-case observer-budget law: if `V_d(T)` is the largest possible `VC_{d+1}` under `|h(Sigma^+)|<=T`, then `V_1(T)=V_2(T)=T`, while for every fixed `d>=3`, `V_d(T)=Theta_d(T^{1/(d-1)})`; exact attainment holds on the direct-factor sizes.
- Cyclic observers: `rpc_r(C_N)=floor(N^{1/r})` when all group elements are nonempty-realizable.
- Group factorization form: for full group observers, `rpc_r` is exactly the largest equal-side unique `r`-fold product factorization.
- Semilattice extremes: at the same observer size, a chain semilattice has `rpc_r=1` while a Boolean semilattice can attain the cardinality root bound; even commutative idempotent observers of equal size can therefore have maximally different rectangular capacities.
- Boundary-window collapse: for the prefix/suffix observer `h^{k,l}`, `rpc_r=1` whenever `ceil(k/2)+ceil(l/2)<r`; hence small boundary windows force `VC_{d+1}<=1` at sufficiently high tuple arity.
- Fixed-observer separation: the two-element observer from #1 has `VC_2 <= 2`, hence proper `PAC_2` learnability via Chernikov–Towsner Theorem 6.5, while exact set-driven characteristic exposure has an exponential lower bound.
- Architecture-vs-VC separation: under the trivial observer, the ambient CFG and fan-out-two MCFG incidence classes have `VC_2 <= 1` and `VC_3 <= 1`, yet the same `X_{k,r}` targets require `k^r` vs `1+r(k-1)` exact positive examples for the two reconstruction architectures.
- Current research tasks: exact arbitrary-size spectrum, explicit quantitative bounds for repaired support-PAC_n, effective grammar-valued reconstruction, and the old full-slice necessity discrepancy as a separate historical/model issue.

## Relation to the project

This note links the fixed-observer CFG/MCFG program (#1/#2) to the Kuriyama–Takeuchi `PAC_n` line and modern higher-arity VC/packing theory. It remains separate from the degree-critical manuscripts until the theorem package stabilizes.

## Research utility

- Brute-force utility: `tools/rpc_bruteforce.py` exactly searches `rpc_r` for small marked monoids (built-in cyclic groups, chain semilattices, and Boolean semilattices).
