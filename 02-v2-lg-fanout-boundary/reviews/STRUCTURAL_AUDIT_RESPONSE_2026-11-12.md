# Paper #2 — structural audit response and mathematical checkpoint (2026-11-12)

Base main commit: 39e5a46b9b05b7548944e38832d6de79b11f71da (43 EN / 50 JP pages).
The full 675-line independent structural-audit text was supplied by the author separately; this file records our decisions, proof checks and deferred questions.

## 1. Conservative redundancy cleanup (EN and JP)

Applied A1 (three unused macros), A3(d) (duplicate fan-out-two caveat), A4 (ambiguous assertion about IPTtD at fan-out two), A7 (second convergence-time disclaimer), A8 (appendix-A duplicate roadmap), A10 (outdated claim that only window-group has explicit constants), A13 (repeated independence from substitutability) and A14 (duplicate declaration of self-contained proofs).
Retained A3(c) distinguishing fixed canonical from class-wide learners, retained the cross-theorem scope table, retained alias labels for compatibility with strict check_port.py, retained the original formal results and arguments. Japanese-only mathematical statements were not deleted merely because English lacks them.

## 2. G1-a: an applied stronger estimate with a separate new proof

New corollary label: cor:lg-type-level-shortest.

If the original typing s is a factor of the sliding-factor morphism lambda_{k,nu}, then for any nonterminal B and any realized s-component type a tuple with that s-type exists with total length at most

  (r_max+1) theta_bar(G) C_buf(k,H,f) |V| |S|^f,

where S=s(Sigma+), C_buf=2kf+(4kf+1)c_{H,f}.

The existing lemma lem:local-group-shortest continues to assert the stronger preservation of the full lambda-vector. We do NOT weaken or silently change this lemma. Instead choose an s-minimal derivation. The marking/thinning/buffering/block-replacement construction of the lambda lemma works on every derivation and heavy antichain, with minimality used only at the final contradiction. If the antichain were too large, it would have a strictly shortening replacement preserving the finer lambda-vector and therefore the original s-vector, contradicting s-minimality. Lemma heavy-node-count(i) then counts at most |V||S|^f realized (nonterminal, s-vector) labels.

With k=|S|, H a maximal subgroup of the minimal ideal of S, and |H|<=|S|, the theorem-A coefficient is

  |S-sharp|^(f*r_max) [3+r_max(r_max+1) C_buf(k,H,f)|S|^f],

bounded in terms of f,r_max,|S| only; no dependence on alphabet cardinality or the auxiliary sliding-factor monoid size is needed. This is an UPPER bound from the proof, not an optimal lower bound. English/Japanese theorem statements, proofs and explicit estimates were updated.

## 3. U1: characteristic-data sandwich — deferred

Theorem data-from-typed-thickness, corollary distribution-representatives, equation root-thickness, proposition rare-type and the Japanese-only corollary typed-sandwich have closely related bounds but differing scopes (canonical vs class-wide operators; type-yield representatives vs distributional class representatives). A complete merger is possible only with separate statement-by-statement equivalence checks and compatible reference updates. The Japanese-only corollary should not simply be deleted without judging its mathematical contribution.

## 4. G1-b: a candidate theorem about arbitrary simultaneous replacements (not in manuscript)

Define rho_f(s) as the least c>=0 such that every configuration of at most f nonempty rows, with m>c nonempty owners, each owner occupying at most f disjoint nonempty intervals, and arbitrary nonempty replacement words, has a nonempty owner subset whose simultaneous replacement preserves each row's s-value.

Candidate:
  S=s(Sigma+) belongs to LG
    iff rho_1(s) is finite
    iff rho_f(s) is finite for every f>=1.

Forward direction: mark up to 2kf row-end positions, discard owners intersecting marks, thin remaining owners using lg-buffered-owners, enlarge and apply local-group-blocks plus block-replacement to preserve sliding-factor coordinates, hence s-values. This yields rho_f(s) <= 2kf+(4kf+1)c_{H,f} for k=|S|.

Reverse: if S is not LG, there is a two-element U1={e,z} inside S. Choose nonempty x,y with s(x)=e and s(y)=z; on the row x^m give each copy of x a distinct owner, replacing it by y. Every nonempty owner selection changes the product from e to z. Therefore rho_1(s)=infinity.

This identifies the boundary of this STRONG REPLACEMENT METHOD, not the open fan-out-two positive-data boundary. The candidate has not been merged into a mathematical theorem of the manuscript, pending independent audit and novelty checks.

For a surjective finite abelian group typing onto A, the further conjectured identity rho_f(s)=d(A^f) follows by the zero-sum upper bound, and lower bound by assigning to f rows per-owner difference vectors forming a maximal zero-sum-free sequence. Not merged.

## 5. G2-a: a false equivalence in the submitted proof and a candidate repair (not in manuscript)

The auditor's assertion for a cut-type comparison,
  lt(i,j)=1 iff i>=i*,
is FALSE for all i<j. A counterexample using actual distinct points on a line is p_t(i)=101-10i, p_u(j)=10j, i,j in [8]. Then lt(i,j)=[i+j>=11], the least i with lt(i,i+1)=1 is i*=5, but lt(3,8)=1 while 3<5.

The original two-sequence lemma only guarantees lt(i,j)=0 when i<j<=i*, and lt(i,j)=1 when i*<=i<j. Cross-region values are unrestricted. With THIS correct cut-type definition, the suggested simultaneous-threshold argument may be reconstructed:

If p_c pair-comparisons have a cut with homogeneous left and right triangles and p_t comparisons are threshold functions lt_q(i,j)=[j>=T_q(i)] with nondecreasing T_q(i)>i, then m>=2^(p_c)*(n0-1)^(p_t)*n0 suffices for a jointly homogeneous n0-subset. For each cut function select the larger of the left and right homogeneous index portions, losing at most factor two. For threshold functions let T*=max T_q and take a greedy chain. If it has n0 points all threshold comparisons are 1. Otherwise the at most n0-1 half-open chain intervals partition the current indices; some interval has >=m/(n0-1) points. On it, the function attaining the maximum threshold at the left endpoint is constantly 0 by monotonicity; discard that function and recurse.

After f diagonal monotonic-subsequence extractions, this may reduce the noncommutative homogenization exponent from 2^(f^2) to (f^2-f+1)*2^f. It DOES NOT settle the uniform-in-f degree question, and should NOT be inserted in the current manuscript before a stand-alone, independently checked proof of threshold/cut classification, the endpoint cases and stability under subsequences.

## 6. Release gates

1. Strict v1-v2 label-port check registers only the one genuinely new corollary label.
2. Verify English pdfLaTeX and Japanese LuaLaTeX builds, citation/ref integrity, theorem/proof preservation, and exact page counts.
3. Preserve all parked materials.
4. After successful merge, regenerate the fixed PDF URLs, and update PAPER.yaml, the handoff and README from measured results.
5. Human mathematical review remains appropriate before TCS submission.
