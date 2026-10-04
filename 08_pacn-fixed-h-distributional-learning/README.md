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
- Same-cardinality observer separation: for every `d>=3` and every integer `q>=2`, two observers of the same size `q^{d-1}` can have `VC_{d+1}=q` versus `VC_{d+1}<=1`.
- Fan-out-one sharpness: the `VC_2` bound is attained by an explicit family of finite regular fixed-`h` substitutable languages.
- **Independent PAC sufficiency:** A direct one-sided relation-valued learner, using only observed full or support-sensitive coordinate slices and exploiting all factor-coordinate projections, achieves `N(eps,delta) <= ceil((2/(e eps))(1+q^d/d)) * ceil(log_2(1/delta))` for `q=|h(Sigma^+)|`. No Chernikov–Towsner Theorem 6.5 is used. Proof: `direct-improper-learner.tex`.
- **Semantic proper PAC via Horn closure (new):** Closing all observed positive words under the full `(f,h)`-tuple substitutability axioms yields a genuine, conservative, `(f,h)`-substitutable **word-language** hypothesis with the **same PAC bound**. This is proper for the unrestricted semantic class of all typed-substitutable languages, but need not be CFG/MCFG-presentable. Proof: `direct-semantic-proper-learner.tex`.
- **CFG-valued improvement for full slices (new):** At arity one, each captured rectangle has a context-free string image (CFL quotients, inverse homomorphisms, substitution). Finite unions yield `K subset L` with the same PAC upper bound and a CFG output. This does **not** guarantee that `K` is fixed-`h` substitutable; the explicit finite `L={aa,bb,aaa,bba,abb}` example shows failure.
- **Finite-target grammar-proper PAC (new):** For any *finite* `(f,h)`-substitutable target, positive Horn closure is itself finite, regular, and `(f,h)`-substitutable. Complete finite positive slice data therefore admit a terminating rule-saturation algorithm and proper CFG/MCFG output with the same `ceil((2/(e eps))(1+q^d/d)) * ceil(log_2(1/delta))` anchor bound, independent of target size. This does not supply an effective positive-list completion test for an infinite slice oracle; infinite-target proper grammar learning remains open. Proof: `direct-finite-grammar-proper-learner.tex`.
- **Forced-positive completeness:** For any realizable positive/negative slice observations, the meet of all compatible semantic target languages equals the positive Horn closure; negative labels do not force extra positives.
- **Grammar-properness remains open:** The semantic closure learner is proper for all typed-substitutable languages; neither proper fixed-`h` CFG/MCFG output nor Takeuchi's unrestricted Problem 11 is claimed solved. The CFG selection from infinite full slices is non-effective.
- PAC direction audit: Takeuchi 2020 refutes the old full-slice necessity direction `PAC_2 => finite VC_2`. Malliaris 2025 gives a counterexample to Chernikov–Towsner v1 and identifies an error in the proposed proof of the revised v2 sufficiency theorem. General `finite VC_k => proper PAC_k` is therefore treated as disputed/conditional here.
- Support-sensitive model: the Takeuchi support restriction extends naturally to every arity `k`. The finite-support necessity/lower-bound direction is proved directly. The sufficiency/equivalence direction is conditional on a correct replacement for the disputed Chernikov–Towsner v2 proof; Takeuchi 2020 Problem 11 is therefore not claimed solved.
- Repaired PAC lower bounds: for every observer budget `T`, the exact padded sharp family has `VC_{d+1}=floor(T^{1/(d-1)})`, giving the explicit lower bound `N >= floor(T^{1/(d-1)})(1-(2(epsilon+delta))^{1/(d+1)})` whenever positive.
- Higher-arity sharpness for every integer `q`: the exact grammar-relevant object is a cyclic interval direct-factor system. A unimodular cyclic frame over `(Z/qZ)^{d-1}` exists for every `q>=2`, yielding `VC_{d+1}=q` at observer size `q^{d-1}`. MDS/all-subset direct-factor systems are a stronger special case.
- Arcs-over-groups relation: subgroup-valued direct-factor systems are exactly in the regular MODS / orthogonal-array / arc-over-groups regime of Bailey–Cameron–Kinyon–Praeger. Their Hall–Paige/fixed-point-free-automorphism obstructions show that several remaining congruence classes cannot be solved by subgroup witnesses; any positive solution there must use genuinely non-subgroup factors.
- Exact worst-case observer-budget law: `V_1(T)=T`, and for every `d>=2`, `V_d(T)=floor(T^{1/(d-1)})`. The upper bound is attained for every `T`, not merely asymptotically or on prime-power sizes.
- Cyclic observers: `rpc_r(C_N)=floor(N^{1/r})` when all group elements are nonempty-realizable.
- Group factorization form: for full group observers, `rpc_r` is exactly the largest equal-side unique `r`-fold product factorization.
- Semilattice extremes: at the same observer size, a chain semilattice has `rpc_r=1` while a Boolean semilattice can attain the cardinality root bound; even commutative idempotent observers of equal size can therefore have maximally different rectangular capacities.
- Boundary-window collapse: for the prefix/suffix observer `h^{k,l}`, `rpc_r=1` whenever `ceil(k/2)+ceil(l/2)<r`; hence small boundary windows force `VC_{d+1}<=1` at sufficiently high tuple arity.
- Fixed-observer separation: the two-element observer from #1 has `VC_2 <= 2` while exact set-driven characteristic exposure has an exponential lower bound. No PAC sufficiency claim is needed for this separation.
- Architecture-vs-VC separation: under the trivial observer, the ambient CFG and fan-out-two MCFG incidence classes have `VC_2 <= 1` and `VC_3 <= 1`, yet the same `X_{k,r}` targets require `k^r` vs `1+r(k-1)` exact positive examples for the two reconstruction architectures.
- Current research tasks: effective, proper **grammar-presentable** fixed-`h` PAC learning; effective extraction of CFGs from full slices; support-sensitive CFG-valued output; and fixed-observer sharpness (`VC_{d+1}` versus `rpc_{d-1}(h)` for one marked monoid).

## Relation to the project

This note links the fixed-observer CFG/MCFG program (#1/#2) to the Kuriyama–Takeuchi `PAC_n` line and modern higher-arity VC/packing theory. It remains separate from the degree-critical manuscripts until the theorem package stabilizes.

## Proof-audit status

- Manual PAC audit: `DIRECT_PAC_PROOF_AUDIT.md` checks the direct improper, semantic-proper, and finite-target grammar-proper PAC routes independently of CT25. It also records the sharpened all-factor-slices bound and the remaining representation/effectivity gaps.
- Manual sharpness audit: `INTERVAL_SHARPNESS_PROOF_AUDIT.md` checks the arbitrary-sublanguage step, the universal cyclic interval frame, and the exact observer-budget law. `tools/interval_sharpness_audit.py` exhaustively searches all legal tuple-hole patterns in representative small cases; output is in `computations/interval_sharpness_audit.txt`.

## Research utility

- Brute-force utility: `tools/rpc_bruteforce.py` exactly searches `rpc_r` for small marked monoids (built-in cyclic groups, chain semilattices, and Boolean semilattices).

## MDS/direct-factor comparison

- The stronger all-pairs MDS/direct-factor route is **not necessary** for grammar sharpness.
- At `d=3,q=6`, exhaustive search over all four abelian groups of order `36` finds no four 6-subsets forming a pairwise exact-factorization `K4`, yet the cyclic-interval construction over `(Z/6Z)^2` attains `VC_4=6`.
- Reproduction: `tools/q6_k4_factorization_search.py`; recorded output: `computations/q6_k4_factorization.txt`.
- Bailey–Cameron–Kinyon–Praeger still describes the subgroup/MODS special case and its congruence obstructions; those obstructions concern the stronger MDS geometry, not the exact grammar VC spectrum.

## Claim-audit source

- Malliaris 2025 audit source: `Remarks on a recent preprint of Chernikov and Towsner` (arXiv:2510.19665) is treated as a claim-audit source. It records a counterexample to CT25 v1 and a proof error in CT25 v2; the v2 theorem statement itself is not asserted false by Malliaris.
