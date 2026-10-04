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
- Repaired PAC lower bounds: for every observer budget `T`, the exact padded sharp family has `VC_{d+1}=floor(T^{1/(d-1)})`, giving the explicit lower bound `N >= floor(T^{1/(d-1)})(1-(2(epsilon+delta))^{1/(d+1)})` whenever positive.
- Higher-arity sharpness for every integer `q`: the exact grammar-relevant object is a cyclic interval direct-factor system. A unimodular cyclic frame over `(Z/qZ)^{d-1}` exists for every `q>=2`, yielding `VC_{d+1}=q` at observer size `q^{d-1}`. MDS/all-subset direct-factor systems are a stronger special case.
- Arcs-over-groups relation: subgroup-valued direct-factor systems are exactly in the regular MODS / orthogonal-array / arc-over-groups regime of Bailey–Cameron–Kinyon–Praeger. Their Hall–Paige/fixed-point-free-automorphism obstructions show that several remaining congruence classes cannot be solved by subgroup witnesses; any positive solution there must use genuinely non-subgroup factors.
- Exact worst-case observer-budget law: `V_1(T)=T`, and for every `d>=2`, `V_d(T)=floor(T^{1/(d-1)})`. The upper bound is attained for every `T`, not merely asymptotically or on prime-power sizes.
- Cyclic observers: `rpc_r(C_N)=floor(N^{1/r})` when all group elements are nonempty-realizable.
- Group factorization form: for full group observers, `rpc_r` is exactly the largest equal-side unique `r`-fold product factorization.
- Semilattice extremes: at the same observer size, a chain semilattice has `rpc_r=1` while a Boolean semilattice can attain the cardinality root bound; even commutative idempotent observers of equal size can therefore have maximally different rectangular capacities.
- Boundary-window collapse: for the prefix/suffix observer `h^{k,l}`, `rpc_r=1` whenever `ceil(k/2)+ceil(l/2)<r`; hence small boundary windows force `VC_{d+1}<=1` at sufficiently high tuple arity.
- Fixed-observer separation: the two-element observer from #1 has `VC_2 <= 2`, hence proper `PAC_2` learnability via Chernikov–Towsner Theorem 6.5, while exact set-driven characteristic exposure has an exponential lower bound.
- Architecture-vs-VC separation: under the trivial observer, the ambient CFG and fan-out-two MCFG incidence classes have `VC_2 <= 1` and `VC_3 <= 1`, yet the same `X_{k,r}` targets require `k^r` vs `1+r(k-1)` exact positive examples for the two reconstruction architectures.
- Current research tasks: fixed-observer sharpness (`VC_{d+1}` versus `rpc_{d-1}(h)` for one marked monoid), explicit quantitative upper bounds for repaired support-PAC_n, effective grammar-valued reconstruction, and the old full-slice necessity discrepancy as a separate historical/model issue.

## Relation to the project

This note links the fixed-observer CFG/MCFG program (#1/#2) to the Kuriyama–Takeuchi `PAC_n` line and modern higher-arity VC/packing theory. It remains separate from the degree-critical manuscripts until the theorem package stabilizes.

## Research utility

- Brute-force utility: `tools/rpc_bruteforce.py` exactly searches `rpc_r` for small marked monoids (built-in cyclic groups, chain semilattices, and Boolean semilattices).

## MDS/direct-factor comparison

- The stronger all-pairs MDS/direct-factor route is **not necessary** for grammar sharpness.
- At `d=3,q=6`, exhaustive search over all four abelian groups of order `36` finds no four 6-subsets forming a pairwise exact-factorization `K4`, yet the cyclic-interval construction over `(Z/6Z)^2` attains `VC_4=6`.
- Reproduction: `tools/q6_k4_factorization_search.py`; recorded output: `computations/q6_k4_factorization.txt`.
- Bailey–Cameron–Kinyon–Praeger still describes the subgroup/MODS special case and its congruence obstructions; those obstructions concern the stronger MDS geometry, not the exact grammar VC spectrum.
